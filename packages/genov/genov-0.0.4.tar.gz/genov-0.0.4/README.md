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

## Versions

* 0.0.1, as of 29-Nov-2024: framework initialized
* 0.0.2, as of 3-Dec-2024: get issues from jira, and persist in an Excel spreadsheet
* 0.0.4, as of 2-Jan-2025: framework enriched with test coverage, lint, typer documentation and sphinx documentation

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

* Run `hatch fmt`
  * Ensure you have no error
  * Message of the kind should be returned: `Found 2 errors (2 fixed, 0 remaining)`
* Notes:
  * Linting analyzes how the code runs and detects errors
  * Formatting restructures how code appears.

### Test coverage

* Run `hatch test --cover`
  * Ensure you have no error, and that you effectively have 80% coverage
* Notes:
  * Target is to have 80% of the code covered with tests
  * No publication allowed in case average of less than 80%.

### Documentation

#### Readme.md

* Run `hatch run docs:md`
  * Message of the kind should be returned: `Docs saved to: GENOV.md`
* Notes:
  * The typer command to generate docs for our package that we access through our README.md
  * Requires an environment where the distribution is installed
    * `rm -rf dist;hatch build;pip3 install dist/genov-*.tar.gz`
  * Run the typer command to document:
    * `typer genov.genov utils docs --output GENOV.md --name genov`
  * Modify the `README.md` file to append the typer documentation:
    * Step 1, we rename the file: `mv README.md README.md.previous`
    * Step 2, we discard the tail of the readme file (pattern modified to `Otomated documentation below`so script is not lost...): `awk '!(f>3);/Otomated documentation below/{f=1}; {if (f) {f=f+1}};' README.md.previous > README.md.tmp`
    * Step 3, we concatenate the latest documentation: `cat README.md.tmp GENOV.md > README.md`
    * Step 4, we cleanse the tmp version: `rm README.md.tmp`
    * Final command is: `rm -rf dist;hatch build;pip3 install dist/genov-*.tar.gz;typer genov.genov utils docs --output GENOV.md --name genov;mv README.md README.md.previous; awk '!(f>3);/Otomated documentation below/{{f=1}}; {{if (f) {{f=f+1}}}};' README.md.previous > README.md.tmp;cat README.md.tmp GENOV.md > README.md;rm README.md.tmp`

#### Sphinx documentation

* Run `hatch run docs:sphinx`
  * Message of the kind should be returned: `The HTML pages are in [./docs/]_build/html.`
* Note:
  * To auto-document the entire application, we use sphinx
  * The command is `make html` from the sub-directory `./docs`.

### Publish

* Update the `version`
  * In `pyproject.toml`
  * In `README.md`
* Run `rm -rf dist/*;hatch build;hatch publish -r test` (To build and publish in test)
  * Directory `dist` is generated (with distribution files)
  * Message of the kind should be returned: `https://test.pypi.org/project/genov/[...latest version...]/`
* Run `hatch publish` (Once verified in test, to publish in production)
  * Message of the kind should be returned: `https://pypi.org/project/genov/[...latest version...]/`
* Notes:
  * Python equivalent command to publish: `python3 -m twine upload --repository pypi dist/*`
  * Package viewable at [pypi](https://pypi.org/project/genov)

## Pycharm configuration

* Unit test configuration, from menu `Run > Edit Configurations...`
  * `Configuration > Target > Script path: ~/PycharmProjects/com_enovation.murex/tests`
  * `Configuration > Working directory: ~/PycharmProjects/com_enovation.murex/`
  * `Configuration > Add content roots to PYTHONPATH: checked`
  * `Configuration > Add source roots to PYTHONPATH: checked`

## Python Cheat sheet

* To get emojis that can be printed by `rich.print()`: run `python -m rich.emoji` in console

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

---
WARNING: do not modify below, as automatically override by script `hatch run docs:md!!!

Automated documentation below
---

# `genov`

Genov tool box, the application with all the commands you need in your day-to-day work at Genovation.

Use the VERBOSE parameter to set the level of logs you need, and let you guide by the HELP.

**Usage**:

```console
$ genov [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...
```

**Options**:

* `-v, --verbose / --no-verbose`: Level of logging verbosity: INFO (--verbose), WARNING (default) or ERROR (--no-verbose).  [default: (WARNING)]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `welcome`: Welcome to the Genovation toolbox! This...
* `jr-gt-iss`: Command to fetch issues from a Jira...
* `df-to-stdout`: The command prints into console the...
* `df-to-xlsx`: Persist the dataframe aliased as ALIAS in...
* `dict-to-stdout`: The command prints into console the...
* `dict-to-json`: The command persists the dictionary...
* `cfg-to-stdout`: Print into console the content of the...

## `genov welcome`

Welcome to the Genovation toolbox!
This command will greet NAME, and return welcome message.
It experiments the rich library that can be used across other commands.

**Usage**:

```console
$ genov welcome [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `genov jr-gt-iss`

Command to fetch issues from a Jira PROJECT within a given SITE using a predefined TOKEN belonging to an ACCOUNT.
The result is transformed through a MAP, returned depending on AS_DF as a DataFrame or a dict, and stored in
context as ALIAS.

To connect to the underlying Atlassian Rest API, the following parameters are required from the configuration file
under ~/.genov/genov.toml to retrieve the following parameters:

- SITE: a site contains instances of Atlassian products under an organization. An organization has one or more
  sites, each site can only have one instance of each product
  -&gt; path in configuration file: the site from atlassion.sites where label is SITE
- PROJECT: a project is a collection of issues (stories, bugs, tasks, etc), used to represent the development
  work for a product, project, or service in Jira
  -&gt; path in configuration file: the project from atlassion.sites.jira.projects where label is PROJECT
- Resource: the REST resources available in Jira Cloud
  -&gt; path in configuration file: the resource from atlassion.sites.jira.resources where label is
  &#x27;GET /rest/api/3/search/jql&#x27;
- MAP: used to transform complex and proprietary responses from Atlassian Rest APIs in data we can process,
  such as DataFrame, Dictionaries, etc.
  -&gt; path in configuration file: the map from atlassion.sites.jira.resources.maps where label is MAP
- ACCOUNT: an Atlassian account is an online Atlassian identity that exists independently of the Atlassian
  products that is used. An account is required to log in to any Atlassian products, such as Jira or Confluence. An
  Atlassian account is like a Google account. When you log into your Gmail account, you can also log in to YouTube,
  Google Docs, etc.
  -&gt; path in configuration file: the account from atlassion.accounts where label is ACCOUNT
- TOKEN: API tokens are used to authenticate users when making calls to Atlassian product APIs
  -&gt; path in configuration file: the token from atlassion.accounts where label is TOKEN.

Illustration of the expected configuration in the ~/.genov/genov.toml file

.. code-block:: text

    {
        &quot;atlassian&quot;: {
            &quot;accounts&quot;: [
                {
                    &quot;label&quot;: &quot;pro&quot;,
                    &quot;email&quot;: &quot;jsg@genovation.associates&quot;,
                    &quot;tokens&quot;: [
                        {
                            &quot;label&quot;: &quot;GSculpt&quot;,
                            &quot;token&quot;: &quot;whatever&quot;
                        }
                    ]
                }
            ],
            &quot;sites&quot;: [
                {
                    &quot;label&quot;: &quot;genovation&quot;,
                    &quot;jira&quot;: {
                        &quot;projects&quot;: [
                            {
                                &quot;label&quot;: &quot;GENOVATION&quot;,
                                &quot;key&quot;: &quot;GENO&quot;
                            }
                        ],
                    &quot;resources&quot;: [
                        {
                            &quot;label&quot;: &quot;GET /rest/api/3/search/jql&quot;,
                            &quot;url&quot;: &quot;https://genovation.atlassian.net/rest/api/3/search&quot;,
                            &quot;maps&quot;: [
                                {
                                    &quot;label&quot;: &quot;flatList&quot;,
                                    &quot;map&quot;: [
                                        {
                                            &quot;dict.path&quot;: &quot;id&quot;,
                                            &quot;df.column&quot;: &quot;id&quot;,
                                            &quot;df.type&quot;: &quot;int&quot;
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }

**Usage**:

```console
$ genov jr-gt-iss [OPTIONS]
```

**Options**:

* `-s, --site site`: Atlassian site to consider. If not set, defaulted to first configured site.  [default: (If not provided, defaulted with the first site configured in the configuration file)]
* `-p, --project project`: Atlassian jira project to consider. If not set, defaulted to first configured project.  [default: (If not provided, defaulted with the first project configured in the configuration file)]
* `-m, --map map`: Map to transform Atlassian responses. If not set, defaulted to first configured map.  [default: (If not provided, defaulted with the first map configured in the configuration file)]
* `--account account`: Atlassian account to consider. If not set, defaulted to first configured account.  [default: (If not provided, defaulted with the first account configured in the configuration file)]
* `-t, --token token`: The Atlassian token to connect to the REST APIs.  [default: (If not provided, defaulted with the first token configured in the configuration file)]
* `--as-df / --as-dict`: Either get the result as a DataFrame or as a dict.  [default: (As DataFrame)]
* `-a, --alias alias`: The alias for the issues stored in context.  [default: (issues)]
* `--help`: Show this message and exit.

## `genov df-to-stdout`

The command prints into console the dataframe instance that is stored in context as ALIAS.

**Usage**:

```console
$ genov df-to-stdout [OPTIONS] alias
```

**Arguments**:

* `alias`: The alias for the dataframe stored in context to be printed.  [required]

**Options**:

* `--help`: Show this message and exit.

## `genov df-to-xlsx`

Persist the dataframe aliased as ALIAS in the file system as FILE.

**Usage**:

```console
$ genov df-to-xlsx [OPTIONS] alias file
```

**Arguments**:

* `alias`: The alias for the dataframe stored in context to be printed.  [required]
* `file`: The file to export the dataframe.  [required]

**Options**:

* `--help`: Show this message and exit.

## `genov dict-to-stdout`

The command prints into console the dictionary instance that is stored in context as ALIAS.

**Usage**:

```console
$ genov dict-to-stdout [OPTIONS] alias
```

**Arguments**:

* `alias`: The alias for the json stored in context to be printed.  [required]

**Options**:

* `--help`: Show this message and exit.

## `genov dict-to-json`

The command persists the dictionary instance that is stored in context as ALIAS in the file system as FILE.

**Usage**:

```console
$ genov dict-to-json [OPTIONS] alias file
```

**Arguments**:

* `alias`: The alias for the json stored in context to be printed.  [required]
* `file`: The file to export the dict.  [required]

**Options**:

* `--help`: Show this message and exit.

## `genov cfg-to-stdout`

Print into console the content of the configuration file stored under ~/.genov/genov.toml.

**Usage**:

```console
$ genov cfg-to-stdout [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
