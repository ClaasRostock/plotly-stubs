[![pypi](https://img.shields.io/pypi/v/plotly-stubs.svg?color=blue)](https://pypi.python.org/pypi/plotly-stubs)
[![versions](https://img.shields.io/pypi/pyversions/plotly-stubs.svg?color=blue)](https://pypi.python.org/pypi/plotly-stubs)
[![license](https://img.shields.io/pypi/l/plotly-stubs.svg)](https://github.com/ClaasRostock/plotly-stubs/blob/main/LICENSE)
![ci](https://img.shields.io/github/actions/workflow/status/ClaasRostock/plotly-stubs/.github%2Fworkflows%2Fnightly_build.yml?label=ci)
[![docs](https://img.shields.io/github/actions/workflow/status/ClaasRostock/plotly-stubs/.github%2Fworkflows%2Fpush_to_release.yml?label=docs)][plotly_stubs_docs]

# plotly-stubs
plotly-stubs is a [stub-only package](https://typing.readthedocs.io/en/latest/spec/distributing.html#stub-only-packages) containing static type annotations for [plotly](https://plotly.com/python/).


## Installation

```sh
pip install plotly-stubs
```

## Documentation

See plotly-stubs's [documentation][plotly_stubs_docs].
> Note: Only very basic documentation as per now.


## Development Setup

### 1. Install uv
This project uses `uv` as package manager.
If you haven't already, install [uv](https://docs.astral.sh/uv), preferably using it's ["Standalone installer"](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2) method: <br>
..on Windows:
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
..on MacOS and Linux:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
(see [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) for all / alternative installation methods.)

Once installed, you can update `uv` to its latest version, anytime, by running:
```sh
uv self update
```

### 2. Install Python
This project requires Python 3.10 or later. <br>
If you don't already have a compatible version installed on your machine, the probably most comfortable way to install Python is through `uv`:
```sh
uv python install
```
This will install the latest stable version of Python into the uv Python directory, i.e. as a uv-managed version of Python.

Alternatively, and if you want a standalone version of Python on your machine, you can install Python either via `winget`:
```sh
winget install --id Python.Python
```
or you can download and install Python from the [python.org](https://www.python.org/downloads/) website.

### 3. Clone the repository
Clone the plotly-stubs repository into your local development directory:
```sh
git clone https://github.com/ClaasRostock/plotly-stubs path/to/your/dev/plotly-stubs
```
Change into the project directory after cloning:
```sh
cd plotly-stubs
```

### 4. Install dependencies
Run `uv sync -U` to create a virtual environment and install all project dependencies into it:
```sh
uv sync -U
```
> **Note**: Using `--no-dev` will omit installing development dependencies.

> **Explanation**: The `-U` option stands for `--update`. It forces `uv` to fetch and install the latest versions of all dependencies,
> ensuring that your environment is up-to-date.

> **Note**: `uv` will create a new virtual environment called `.venv` in the project root directory when running
> `uv sync -U` the first time. Optionally, you can create your own virtual environment using e.g. `uv venv`, before running
> `uv sync -U`.

### 5. (Optional) Activate the virtual environment
When using `uv`, there is in almost all cases no longer a need to manually activate the virtual environment. <br>
`uv` will find the `.venv` virtual environment in the working directory or any parent directory, and activate it on the fly whenever you run a command via `uv` inside your project folder structure:
```sh
uv run <command>
```

However, you still _can_ manually activate the virtual environment if needed.
When developing in an IDE, for instance, this can in some cases be necessary depending on your IDE settings.
To manually activate the virtual environment, run one of the "known" legacy commands: <br>
..on Windows:
```sh
.venv\Scripts\activate.bat
```
..on Linux:
```sh
source .venv/bin/activate
```

### 6. Install pre-commit hooks
The `.pre-commit-config.yaml` file in the project root directory contains a configuration for pre-commit hooks.
To install the pre-commit hooks defined therein in your local git repository, run:
```sh
uv run pre-commit install
```

All pre-commit hooks configured in `.pre-commit-config.yaml` will now run each time you commit changes.

pre-commit can also manually be invoked, at anytime, using:
```sh
uv run pre-commit run --all-files
```

To skip the pre-commit validation on commits (e.g. when intentionally committing broken code), run:
```sh
uv run git commit -m <MSG> --no-verify
```

To update the hooks configured in `.pre-commit-config.yaml` to their newest versions, run:
```sh
uv run pre-commit autoupdate
```

### 7. Test that the installation works
To test that the installation works, run pytest in the project root folder:
```sh
uv run pytest
```

## Meta

Copyright (c) 2025 [Claas Rostock](https://github.com/ClaasRostock). All rights reserved.

Claas Rostock - [@LinkedIn](https://www.linkedin.com/in/claasrostock/?locale=en_US) - claas.rostock@dnv.com

Distributed under the MIT license. See [LICENSE](LICENSE.md) for more information.

[https://github.com/ClaasRostock/plotly-stubs](https://github.com/ClaasRostock/plotly-stubs)

## Contributing

1. Fork it (<https://github.com/ClaasRostock/plotly-stubs/fork>)
2. Create an issue in your GitHub repo
3. Create your branch based on the issue number and type (`git checkout -b issue-name`)
4. Evaluate and stage the changes you want to commit (`git add -i`)
5. Commit your changes (`git commit -am 'place a descriptive commit message here'`)
6. Push to the branch (`git push origin issue-name`)
7. Create a new Pull Request in GitHub

<!-- Markdown link & img dfn's -->
[plotly_stubs_docs]: https://ClaasRostock.github.io/plotly-stubs/README.html
