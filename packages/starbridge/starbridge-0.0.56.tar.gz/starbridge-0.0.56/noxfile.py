import json
from pathlib import Path

import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv"

_INSTALL_ARGS = "-e .[dev,imaging]"
_INSTALL_NO_EXTRAS_ARGS = "-e .[dev]"
_JUNITXML_ARG = "--junitxml=junit.xml"


@nox.session(python=["3.11", "3.12", "3.13"])
def test(session: nox.Session):
    session.install(_INSTALL_ARGS)
    session.run("rm", "-rf", ".coverage", external=True)
    session.run(
        "pytest",
        "--disable-warnings",
        _JUNITXML_ARG,
        "-n",
        "auto",
        "--dist",
        "loadgroup",
        "-m",
        "not sequential",
    )
    session.run(
        "pytest",
        "--cov-append",
        "--disable-warnings",
        _JUNITXML_ARG,
        "-n",
        "auto",
        "--dist",
        "loadgroup",
        "-m",
        "sequential",
    )
    session.run(
        "bash",
        "-c",
        "docker compose ls --format json | jq -r '.[].Name' | grep ^pytest | xargs -I {} docker compose -p {} down --remove-orphans",
        external=True,
    )


@nox.session(python=["3.11", "3.12", "3.13"])
def test_no_extras(session: nox.Session):
    session.install(_INSTALL_NO_EXTRAS_ARGS)
    session.run(
        "pytest",
        "--cov-append",
        "--disable-warnings",
        _JUNITXML_ARG,
        "-n",
        "1",
        "-m",
        "no_extras",
    )
    session.run(
        "bash",
        "-c",
        "docker compose ls --format json | jq -r '.[].Name' | grep ^pytest | xargs -I {} docker compose -p {} down --remove-orphans",
        external=True,
    )


@nox.session(python=["3.11"])
def lint(session: nox.Session):
    session.install(_INSTALL_ARGS)
    session.run("ruff", "check", ".")
    session.run(
        "ruff",
        "format",
        "--check",
        ".",
    )


@nox.session(python=["3.11"])
def audit(session: nox.Session):
    session.install(_INSTALL_ARGS)
    session.run("pip-audit", "-f", "json", "-o", "vulnerabilities.json")
    session.run("jq", ".", "vulnerabilities.json", external=True)
    session.run("pip-licenses", "--format=json", "--output-file=licenses.json")
    session.run("jq", ".", "licenses.json", external=True)
    # Read and parse licenses.json
    licenses_data = json.loads(Path("licenses.json").read_text(encoding="utf-8"))

    licenses_inverted: dict[str, list[dict[str, str]]] = {}
    licenses_inverted = {}
    for pkg in licenses_data:
        license_name = pkg["License"]
        package_info = {"Name": pkg["Name"], "Version": pkg["Version"]}

        if license_name not in licenses_inverted:
            licenses_inverted[license_name] = []
        licenses_inverted[license_name].append(package_info)

    # Write inverted data
    Path("licenses-inverted.json").write_text(
        json.dumps(licenses_inverted, indent=2), encoding="utf-8"
    )
    session.run("jq", ".", "licenses-inverted.json", external=True)
    session.run("cyclonedx-py", "environment", "-o", "sbom.json")
    session.run("jq", ".", "sbom.json", external=True)
