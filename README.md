# mitk-python-docs

Source for the [MITK Python API](https://mitk-python.readthedocs.io) reference documentation.
The published docs are generated automatically from the [`mitk-python`](https://pypi.org/project/mitk-python/) package using [Sphinx](https://www.sphinx-doc.org) and hosted on [Read the Docs](https://readthedocs.org).

## What this repository contains

```
.
├── docs/
│   ├── conf.py       # Sphinx configuration
│   └── index.rst     # Documentation root (auto-generates API reference)
├── .readthedocs.yaml # Read the Docs build configuration
├── requirements.txt  # Sphinx build dependencies
└── LICENSE
```

## Prerequisites

- **Python 3.12** (matches the Read the Docs build environment)
- The `mitk-python` package (installed separately; see [Quick start](#quick-start))

## Quick start

```bash
# 1. Create and activate a virtual environment
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install Sphinx build dependencies
pip install -r requirements.txt

# 3. Install the mitk-python package
pip install mitk-python
```

> **Note:** `mitk-python` is a compiled package with binary wheels.
> If a wheel is not available for your platform or Python version, installation will fail.
> Check [PyPI](https://pypi.org/project/mitk-python/#files) for available wheels before installing.

## Build documentation locally

```bash
sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser to view the result.

## Read the Docs configuration

Publishing is controlled by [`.readthedocs.yaml`](.readthedocs.yaml).
Key settings:

| Setting | Value |
|---|---|
| OS | ubuntu-24.04 |
| Python | 3.12 |
| Sphinx config | `docs/conf.py` |

On every push to the default branch, Read the Docs installs the dependencies listed in `requirements.txt`, installs the `mitk-python` package, and builds the HTML docs.

## Versioning

The API reference tracks a specific release of `mitk-python`, pinned in [`.readthedocs.yaml`](.readthedocs.yaml).
To update the documented version, change the `mitk-python==<version>` line in that file.

## Contributing

Contributions to the documentation source are welcome.
Please open a pull request with your proposed changes.
For questions about the `mitk-python` package itself, refer to the [MITK project](https://www.mitk.org).

## License

This project is licensed under the **BSD 3-Clause License** — see [`LICENSE`](LICENSE) for details.