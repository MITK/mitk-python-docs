# mitk-python-docs

Read the Docs build harness for the [MITK Python API](https://mitk-python.readthedocs.io) documentation.

The documentation source is **not** stored here. It lives in the MITK
repository under [`Wrapping/Python/docs`](https://github.com/MITK/MITK/tree/develop/Wrapping/Python/docs)
and is the same Sphinx site built locally by the `mitk_python_docs` CMake
target. On every Read the Docs build this repository fetches that source and
builds it against the [`mitk-python`](https://pypi.org/project/mitk-python/)
wheel from PyPI, so the published site stays a single source of truth with the
bindings.

## What this repository contains

```
.
├── .readthedocs.yaml  # RTD build config: fetches docs from MITK, then builds
├── requirements.txt   # the mitk-python wheel to document
├── .gitignore
├── LICENSE
└── README.md
```

`docs/` is created at build time (a sparse checkout of MITK) and is
git-ignored.

## How the build works

1. `post_checkout` sparse-clones `Wrapping/Python/docs` from MITK into `docs/`.
   The MITK ref is `${MITK_DOCS_REF:-develop}`; override it with the
   `MITK_DOCS_REF` environment variable in the Read the Docs project settings.
2. The toolchain is installed from the fetched `docs/requirements.txt` and the
   `mitk-python` wheel from this repository's `requirements.txt`.
3. Read the Docs runs Sphinx against `docs/conf.py`. Autodoc imports the
   installed `mitk` package to render the API reference.

## Build locally

Reproduce a Read the Docs build (Linux, macOS, or WSL; the `mitk-python` wheel
must exist for your platform and Python version, see
[PyPI](https://pypi.org/project/mitk-python/#files)):

```bash
# 1. Fetch the documentation source from MITK
git clone --depth 1 --no-tags --filter=blob:none --sparse \
    --branch "${MITK_DOCS_REF:-develop}" \
    https://github.com/MITK/MITK.git .mitk-src
git -C .mitk-src sparse-checkout set Wrapping/Python/docs
cp -r .mitk-src/Wrapping/Python/docs docs
rm -rf .mitk-src

# 2. Install the toolchain and the package being documented
pip install -r docs/requirements.txt -r requirements.txt

# 3. Build
python -m sphinx -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` to view the result.

## Versioning

`latest` tracks the development line: MITK `develop` plus the dev wheel pinned
in [`requirements.txt`](requirements.txt). When a newer dev wheel is published,
bump the `mitk-python==` pin. To document a release instead, set `MITK_DOCS_REF`
to the matching tag (e.g. `v2026.06`) and pin the released wheel.

## Contributing

The documentation content (Getting started, User guide, API reference) is
maintained in MITK under `Wrapping/Python/docs`; open documentation changes
there, not in this repository. Changes here should concern only the Read the
Docs build itself. For the `mitk-python` package, see the
[MITK project](https://www.mitk.org).

## License

BSD 3-Clause License, see [`LICENSE`](LICENSE).
