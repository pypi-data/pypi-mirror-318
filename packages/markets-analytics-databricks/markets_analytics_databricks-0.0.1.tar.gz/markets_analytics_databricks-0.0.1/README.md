# Databricks Package

This [package]() is created by the Markets Analytics team at Zalando Lounge to help provide utility functions which in turn reduce boilerplate code such as connecting to data stores, reading and writing to Google Sheets, managing ETL pipelines, and many more.

## Installation

```sh
pip install databricks_package
pip install databricks_package==X.Y.Z
```

## Releasing New Versions

In order to release new version(s), always update the `pyproject.toml` file's version number and increment either the minor (bug fixes) or major (new feature) by 1 before creating the distribution file and publishing it on PyPI.

Once the version number has been incremented, then run the following commands in your command line:

```sh
pip install --upgrade build twine
build
twine upload --repository testpypi dist/*
```

In case you need to publish the distribution to the production PyPI server then run the following command:

```sh
twine upload dist/*
```

PS: Make sure that you're set your credentials before running the commands above, otherwise the package won't be published to the PyPI server.

```sh
set TWINE_USERNAME=__token__
set TWINE_PASSWORD=<pypi-token>
```