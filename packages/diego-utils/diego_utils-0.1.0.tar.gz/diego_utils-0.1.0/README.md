# 🧰 diego-utils

[![Deploy to PyPI](https://github.com/diego-lda/diego-utils/actions/workflows/deploy_pypi.yaml/badge.svg?branch=main)](https://github.com/diego-lda/diego-utils/actions/workflows/deploy_pypi.yaml)
[![Deploy MkDocs](https://github.com/diego-lda/diego-utils/actions/workflows/deploy_mkdocs.yaml/badge.svg?branch=main)](https://github.com/diego-lda/diego-utils/actions/workflows/deploy_mkdocs.yaml)
[![PyPI version](https://badge.fury.io/py/diego-utils.svg)](https://pypi.org/project/diego-utils/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/diego-utils.svg)](#)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The `diego-utils` package is a Python library with some utility functions that I find useful for data science and econometrics.
It is also a place for me to try and formalise some code built across different projects taht I think might be useful in the future.

## 📋 Prerequisites

This package is requires a Python version between 3.11 and 3.13.
It uses `setup.py`, `setup.cfg`, and `pyproject.toml` for dependency management and packaging.

## 🛫 Set Up

### Install with PyPI

The faster and easier way to install `diego-utils` in using PyPI. From your terminal just run:

```bash
pip install diego-utils
```

### Install through Cloning the repository

Alternatively, `diego-utils` can also be installed by first cloning the repository:

```bash
git clone https://github.com/diego-lda/diego-utils.git
```

Then navigating into the home directory and running:

```bash
pip install .
```

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
