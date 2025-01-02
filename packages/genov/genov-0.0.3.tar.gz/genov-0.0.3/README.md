# The Genovation python toolbox

This python tool-box is made to support Genovation associates in their day-to-day work.

# INSTALL

## Pre-requisites

* Windows PowerShell (Terminal on MS Windows)
  * Console to run `genov` tool box, and its commands
  * How-to from Microsoft: https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows

* Python:
  * `genov` is tested with Python 3.13
  * As of EoY 2024, Python 3.13.0 is available at: https://www.python.org/downloads/
  * Note: starting with Python 3.4, `pip` is by default included

Once installed, you can check in your terminal:
```console
foo@bar:~$ python3 --version
           >> Python 3.13.0
foo@bar:~$ pip3 --version
           >> pip 24.3.1 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)
```

Notes:
* On your system, you might have to replace the `python3` command with `python`
* To check where is your python installed: `which python3`: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`

## Install Genov

* Simply type in your Terminal: `pip3 install genov`

# Use

## Cheat sheet

[Commands are documented here](./GENOV.md)

## Versions

* 0.0.1, as of 29-Nov-2024: framework initialized
* 0.0.2, as of 3-Dec-2024: get issues from jira, and persist in an Excel spreadsheet
* 0.0.3, as of 2-Jan-2025: framework enriched with test coverage, lint, typer documentation and sphinx documentation

# Contribute

## Dependencies

### To run

| Dependencies     | Description                                                                                                            |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------|
| `com-enovation`  | The seed toolbox that we use to initialize this toolbox. To decommission as commands are being re-instantiated here... |
| `typer`          | Library for building CLI applications, based on Click                                                                  |
| `tomlkit`        | Library for manipulating configuration file                                                                            |
| `pydash`         | Library for manipulating dictionaries with path... TODO - TO BE REPLACED BY JSONATA-PYTHON                             |
| `jsonschema`     | Library for validating json schema                                                                                     |
| `jsonata-python` | Library for exploring dictionaries and json                                                                            |

### To contribute

| Dependencies               | Description                                                                                               |
|:---------------------------|:----------------------------------------------------------------------------------------------------------|
| `hatch`                    | Extensible, standards compliant build backend.                                                            |
| `pytest`                   | To run tests (natively imported by hatch).                                                                |
| `pytest-cov`               | To measure test coverage (natively imported by hatch).                                                    |
| `sphinx`                   | To document project                                                                                       |
| `sphinx-autodoc-typehints` | To use Python 3 annotations for documenting acceptable argument types and return value types of functions |
| `sphinx_rtd_theme`         | The 'read the docs' theme                                                                                 |

## Steps to publish changes/ enhancements to genov

### Code formatting and linting

* Note:
  * Linting analyzes how the code runs and detects errors
  * Formatting restructures how code appears.
* Run `hatch fmt`
* Ensure you have no error
* Message of the kind should be returned: `Found 2 errors (2 fixed, 0 remaining)`. 

### Test coverage

* Note:
  * Target is to have 80% of the code covered with tests
  * No publication allowed in case average of less than 80%
* Run `hatch test --cover`
* Ensure you have no error, and that you effectively have 80% coverage.

### Documentation

#### Readme.md

* Note:
  * The typer command to generate docs for our package that we access through our README.md
  * Requires an environment where the distribution is installed, and the following command can be executed
  * `typer genov.genov utils docs --output GENOV.md --name genov`
* Run `hatch run docs:md`
* Message of the kind should be returned: `Docs saved to: GENOV.md`

#### Sphinx documentation

* Note:
  * To auto-document the entire application, we use sphinx
  * The command is `make html` from the sub-directory `./docs`
* Run `hatch run docs:sphinx`
* Message of the kind should be returned: `The HTML pages are in [./docs/]_build/html.`

### Publish

## Cheat sheet

### Distribution

The following steps have to be executed in order (from root directory):
1. Build a first temporary distribution, install and document it
   * Run: `rm -rf dist;python3 -m build;pip3 uninstall -y genov;pip3 install dist/genov-*.tar.gz;typer genov.genov utils docs --output GENOV.md --name genov`
   * Directories `build` and `dist` are generated (with distribution files)
   * File `Genov.md` is updated (with the typer application documentation)
   * Temporary distribution is installed locally
2. Update the `project.version` in `pyproject.toml`
3. Rebuild the final distribution, and uninstall the temporary distribution
   * Run: `rm -rf dist;python3 -m build;pip3 uninstall genov`
4. Publish the final distribution to pypi
   * Run: `python3 -m twine upload --repository pypi dist/*`
   * In case you face an error `No module named twine`, you need first to run `pip install twine`
   * Package viewable at [pypi](https://pypi.org/project/genov)
5. Finally, if you need to, you can install locally the final package
   * Run: pip3 install genov

`hatch build`
`hatch fmt`
`hatch test --cover`
`make html`

#### Typer documentation

* To publish 

### Typer

* To get emojis that can be printed by `rich.print()`: run `python -m rich.emoji` in console

### Pycharm configuration

* Unit test configuration, from menu `Run > Edit Configurations...`
  * `Configuration > Target > Script path: ~/PycharmProjects/com_enovation.murex/tests`
  * `Configuration > Working directory: ~/PycharmProjects/com_enovation.murex/`
  * `Configuration > Add content roots to PYTHONPATH: checked`
  * `Configuration > Add source roots to PYTHONPATH: checked`

### Python stuff

* Check we have the latest versions:
  * pip: `python3 -m pip install --upgrade pip`
  * build to generate the distribution: `python3 -m pip install --upgrade build`

* Update packages using pip
  * Check all packages are fine: `pip check`
  * List all packages outdated: `pip list --outdated`
  * Update all packages outdated:
    * On Mac: `pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U`
    * On Windows: `pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}`
* A simple example package. You can use [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/) to write your content.
