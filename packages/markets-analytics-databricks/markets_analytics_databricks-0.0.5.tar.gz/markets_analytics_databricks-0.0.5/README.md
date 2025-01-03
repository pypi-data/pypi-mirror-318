# Markets Analytics - Databricks Package

This [package](https://pypi.org/project/markets-analytics-databricks/) is created by the Markets Analytics team at Zalando Lounge to help provide utility functions which in turn reduce boilerplate code such as connecting to data stores, reading and writing to Google Sheets, managing ETL pipelines, and many more.

## Installation

```sh
pip install markets-analytics-databricks
pip install markets-analytics-databricks==X.Y.Z
```

## Releasing New Versions

In order to release new version(s), always update the `pyproject.toml` file's version number.

A version is defined as X.Y.Z, where X is major, Y is minor, and Z is patch. Based on your changes, increment the number you're interested in by 1, and reset the lower numbers to 0 (if applicable).

Example #1: If we are live on 2.3.2, and you release a minor version then the next version should be 2.4.0.

Example #2: If we are live on 2.3.2, and you fix a bug then the next version should be 2.3.3.

Once the version number has been incremented, the package is ready to be published:

```sh
python3 -m pip install --upgrade build twine
python3 -m build
python3 -m twine upload dist/*
```

If you face any metadata package errors then make sure to update your `pkginfo` package as well:

```sh
python3 -m pip install --upgrade pkginfo
```

PS: Make sure that you have set your credentials before running the commands above, otherwise the package won't be published to the PyPI server (or you could manually do it in your command line when the upload process prompts you).

```sh
set TWINE_USERNAME=__token__
set TWINE_PASSWORD=<pypi-token>
```

In case you don't have a token then create one on the PyPI server.