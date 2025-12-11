# Changelog

All notable changes to the [plotly-stubs] project will be documented in this file.<br>
The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

-/-

## [0.1.0] - 2025-12-11

### Removed
* Removed support for Python 3.10 <br>
  Main reason being that this removes the need to support numpy 1.x  (numpy>=2.3 supports Python 3.11 upwards -> so do we) <br>

### Added
* Added graph types to the plotly.express subpackage. by @OutSquareCapital in https://github.com/ClaasRostock/plotly-stubs/pull/5

### Changed
* pyproject.toml:
  * added required-environments to uv.tools (windows, linux)
  * removed deprecated pyright setting 'reportShadowedImports'
  * removed deprecated mypy plugin 'numpy.typing.mypy_plugin'
  * removed leading carets and trailing slashes from 'exclude' paths
* .sourcery.yaml:
  * updated the lowest Python version the project supports to '3.11'
* ruff.toml:
  * updated target Python version to "py311"
* GitHub workflow _build_and_publish_documentation.yml:
  * changed 'uv sync --upgrade' to 'uv sync --frozen' to avoid unintentional package upgrades.
* .pre-commit-config.yaml:
  * updated rev of pre-commit-hooks to v6.0.0
  * updated rev of ruff-pre-commit to v0.14.3
  * updated id of ruff to ruff-check
* Sphinx documentation:
  * conf.py: removed ruff rule exception on file level
* VS Code settings:
  * Updated 'mypy-type-checker.reportingScope' to 'custom'.
* VS Code recommended extensions:
  * Removed deprecated IntelliCode extension and replaced it by GitHub Copilot Chat as recommended replacement.
    * Removed njqdev.vscode-python-typehint (Python Type Hint). Not maintained since 1 year, and the functionality is now covered by GitHub Copilot.
    * Added 'ms-python.debugpy' (Python Debugger).
    * Added 'ms-python.vscode-python-envs' (Python Environments). This VS Code extension is expected to replace the legacy VS Code Settings
      "python.terminal.activateEnvironment" and "python.terminal.activateEnvInCurrentTerminal".
      Correspondingly, the two legacy settings have been set to 'false'.

### Dependencies
* Added polars>=1.31
* Updated to ruff>=0.14.3  (from ruff>=0.11.0)
* Updated to pyright>=1.1.407  (from pyright>=1.1.396)
* Updated to sourcery>=1.40  (from sourcery>=1.35)
* Updated to numpy>=2.3  (removed split version specifiers)
* Updated to pandas-stubs>=2.3  (from pandas-stubs>=2.2)
* Updated to pytest>=8.4  (from pytest>=8.3)
* Updated to pytest-cov>=7.0  (from pytest-cov>=6.0)
* Updated to Sphinx>=8.2  (from Sphinx>=8.1)
* Updated to sphinx-argparse-cli>=1.20  (from sphinx-argparse-cli>=1.19)
* Updated to sphinx-autodoc-typehints>=3.5  (from sphinx-autodoc-typehints>=3.0)
* Updated to furo>=2025.9  (from furo>=2024.8)
* Updated to pre-commit>=4.3  (from pre-commit>=4.1)
* Updated to mypy>=1.18  (from mypy>=1.15)
* Updated to checkout@v5  (from checkout@v4)
* Updated to setup-python@v6  (from setup-python@v5)
* Updated to setup-uv@v7  (from setup-uv@v5)
* Updated to upload-artifact@v5  (from upload-artifact@v4)
* Updated to download-artifact@v5  (from download-artifact@v4)


## [0.0.6] - 2025-07-29

### Added
* Added stubs for candlestick graph object and accompanying subpackages. by @IAmAMetalHead in https://github.com/ClaasRostock/plotly-stubs/pull/3
* Added chart types to plotly express stubs. by @OutSquareCapital in https://github.com/ClaasRostock/plotly-stubs/pull/4


## [0.0.5] - 2025-03-20

### Removed
* src/plotly-stubs/__init__.pyi : removed import of plotly.version

### Dependencies
* Updated to ruff>=0.11.0  (from ruff>=0.9.5)
* Updated to pyright>=1.1.396  (from pyright>=1.1.393)
* Updated to sourcery>=1.35  (from sourcery>=1.33)
* Updated to pre-commit>=4.1  (from pre-commit>=4.0)


## [0.0.4] - 2025-02-18

* Beta release 0.0.4


## [0.0.3] - 2025-02-18

* Beta release 0.0.3


## [0.0.2] - 2025-02-18

* Beta release 0.0.2


## [0.0.1] - 2025-02-18

* Beta release 0.0.1

<!-- Markdown link & img dfn's -->
[unreleased]: https://github.com/ClaasRostock/plotly-stubs/compare/v0.0.5...HEAD
[0.0.5]: https://github.com/ClaasRostock/plotly-stubs/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/ClaasRostock/plotly-stubs/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/ClaasRostock/plotly-stubs/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/ClaasRostock/plotly-stubs/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/ClaasRostock/plotly-stubs/releases/tag/v0.0.1
[plotly-stubs]: https://github.com/ClaasRostock/plotly-stubs
