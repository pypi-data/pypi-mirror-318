# 🧰 diego-utils

[![Deploy MkDocs](https://github.com/diego-lda/diego-utils/actions/workflows/deploy_mkdocs.yaml/badge.svg?branch=main)](https://github.com/diego-lds/diego-utils/actions/workflows/deploy_mkdocs.yaml)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The `diego-utils` package is a Python library with some utility functions that I find useful for data science and econometrics.
It is also a place for me to try and formalise some code built across different projects taht I think might be useful in the future.

It is built with Python 3.11 and higher, and uses `setup.py`, `setup.cfg`, and `pyproject.toml` for dependency management and packaging.

## 📋 Prerequisites

- Python 3.11 or higher

## 🛫 Set Up

`diego-utils` can be installed by first cloning the repository, navigating into the home directory and then running:

```bash
pip install .
```

This will install into your computer the `diego-utils` package.

## 🗂️ How the Project is Organised

The package has several modules, which split the functionality into themes:

- **metrics**: These are econometrics functions, to help with the analysis of data.
- **evaluate**: These are evaluation functions, designed to monitor a pipelines performance.
- **handle**: These are data handling functions, useful in data manipulation and transformation.

## 📖 Documentation and Further Information

The documentation is automatically generated using **GitHub Actions** and **MkDocs**.
For an in-depth understanding of `diego-utils`, how to contribute to `rdsa-utils`, and more, please refer to the [MkDocs-generated documentation](https://diego-lda.github.io/diego-utils/).

## 🛡️ Licence

Unless stated otherwise, the codebase is released under the [MIT License][mit].
This covers both the codebase and any sample code in the documentation.

[mit]: LICENSE
