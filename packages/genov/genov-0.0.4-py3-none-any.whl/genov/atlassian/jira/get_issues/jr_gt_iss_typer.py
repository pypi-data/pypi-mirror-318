"""
Module to retrieve issues from Jira through a Typer command.
"""

from inspect import stack
from logging import Logger, getLogger
from typing import TYPE_CHECKING, Annotated

import jsonata
from click import BadParameter
from jsonschema.exceptions import ValidationError
from rich import print
from typer import Context, Option

from genov.atlassian.jira.get_issues.jr_gt_iss import JiraIssuesGetter
from genov.helpers.json.json_cker__checker import JsonChecker
from genov.utils.typer.context_obj.context_obj import GContextObj

if TYPE_CHECKING:
    from pandas import DataFrame

DICT_CONFIGURATION_SCHEMA: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["atlassian"],
    "additionalProperties": True,
    "properties": {
        "atlassian": {
            "type": "object",
            "required": ["accounts", "sites"],
            "additionalProperties": True,
            "properties": {
                "accounts": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "required": ["label", "email", "tokens"],
                        "additionalProperties": True,
                        "properties": {
                            "label": {"type": "string"},
                            "email": {"type": "string"},
                            "tokens": {
                                "type": "array",
                                "minItems": 1,
                                "items": {
                                    "type": "object",
                                    "required": ["label", "token"],
                                    "additionalProperties": True,
                                    "properties": {"label": {"type": "string"}, "token": {"type": "string"}},
                                },
                            },
                        },
                    },
                },
                "sites": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "required": ["label", "jira"],
                        "additionalProperties": True,
                        "properties": {
                            "label": {"type": "string"},
                            "jira": {
                                "type": "object",
                                "required": ["projects", "resources"],
                                "additionalProperties": True,
                                "properties": {
                                    "projects": {
                                        "type": "array",
                                        "minItems": 1,
                                        "items": {
                                            "type": "object",
                                            "required": ["label", "key"],
                                            "additionalProperties": True,
                                            "properties": {"label": {"type": "string"}, "key": {"type": "string"}},
                                        },
                                    },
                                    "resources": {
                                        "type": "array",
                                        "minItems": 1,
                                        "items": {
                                            "type": "object",
                                            "required": ["label", "url"],
                                            "additionalProperties": True,
                                            "properties": {
                                                "label": {"type": "string"},
                                                "url": {"type": "string"},
                                                "maps": {
                                                    "type": "array",
                                                    "minItems": 0,
                                                    "items": {
                                                        "type": "object",
                                                        "required": ["label", "map"],
                                                        "additionalProperties": True,
                                                        "properties": {
                                                            "label": {"type": "string"},
                                                            "map": {
                                                                "type": "array",
                                                                "minItems": 1,
                                                                "items": {
                                                                    "type": "object",
                                                                    "required": ["dict.path", "df.column"],
                                                                    "additionalProperties": True,
                                                                    "properties": {
                                                                        "dict.path": {"type": "string"},
                                                                        "df.column": {"type": "string"},
                                                                        "df.type": {"type": "string"},
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    },
}


def jira_get_issues_typer(
    ctx_context: Context,
    str_site: Annotated[
        str | None,
        Option(
            "--site",
            "-s",
            help="Atlassian site to consider. If not set, defaulted to first configured site.",
            metavar="site",
            show_default="If not provided, defaulted with the first site configured in the configuration file",
        ),
    ] = None,
    str_project: Annotated[
        str | None,
        Option(
            "--project",
            "-p",
            help="Atlassian jira project to consider. If not set, defaulted to first configured project.",
            metavar="project",
            show_default="If not provided, defaulted with the first project configured in the configuration file",
        ),
    ] = None,
    str_map: Annotated[
        str | None,
        Option(
            "--map",
            "-m",
            help="Map to transform Atlassian responses. If not set, defaulted to first configured map.",
            metavar="map",
            show_default="If not provided, defaulted with the first map configured in the configuration file",
        ),
    ] = None,
    str_account: Annotated[
        str | None,
        Option(
            "--account",
            help="Atlassian account to consider. If not set, defaulted to first configured account.",
            metavar="account",
            show_default="If not provided, defaulted with the first account configured in the configuration file",
        ),
    ] = None,
    str_token: Annotated[
        str | None,
        Option(
            "--token",
            "-t",
            help="The Atlassian token to connect to the REST APIs.",
            metavar="token",
            show_default="If not provided, defaulted with the first token configured in the configuration file",
        ),
    ] = None,
    b_as_df: Annotated[  # noqa: FBT002
        bool,
        Option(
            "--as-df/--as-dict",
            help="Either get the result as a DataFrame or as a dict.",
            metavar="as_df",
            show_default="As DataFrame",
        ),
    ] = True,
    str_alias: Annotated[
        str,
        Option(
            "--alias",
            "-a",
            help="The alias for the issues stored in context.",
            metavar="alias",
            callback=GContextObj.check_alias_name_to_set,
            show_default="issues",
        ),
    ] = "issues",
):
    """
    Command to fetch issues from a Jira PROJECT within a given SITE using a predefined TOKEN belonging to an ACCOUNT.
    The result is transformed through a MAP, returned depending on AS_DF as a DataFrame or a dict, and stored in
    context as ALIAS.

    To connect to the underlying Atlassian Rest API, the following parameters are required from the configuration file
    under ~/.genov/genov.toml to retrieve the following parameters:

    - SITE: a site contains instances of Atlassian products under an organization. An organization has one or more
      sites, each site can only have one instance of each product
      -> path in configuration file: the site from atlassion.sites where label is SITE
    - PROJECT: a project is a collection of issues (stories, bugs, tasks, etc), used to represent the development
      work for a product, project, or service in Jira
      -> path in configuration file: the project from atlassion.sites[x].jira.projects where label is PROJECT
    - Resource: the REST resources available in Jira Cloud
      -> path in configuration file: the resource from atlassion.sites[x].jira.resources where label is
      'GET /rest/api/3/search/jql'
    - MAP: used to transform complex and proprietary responses from Atlassian Rest APIs in data we can process,
      such as DataFrame, Dictionaries, etc.
      -> path in configuration file: the map from atlassion.sites[x].jira.resources[x].maps where label is MAP
    - ACCOUNT: an Atlassian account is an online Atlassian identity that exists independently of the Atlassian
      products that is used. An account is required to log in to any Atlassian products, such as Jira or Confluence. An
      Atlassian account is like a Google account. When you log into your Gmail account, you can also log in to YouTube,
      Google Docs, etc.
      -> path in configuration file: the account from atlassion.accounts where label is ACCOUNT
    - TOKEN: API tokens are used to authenticate users when making calls to Atlassian product APIs
      -> path in configuration file: the token from atlassion.accounts where label is TOKEN.

    Illustration of the expected configuration in the ~/.genov/genov.toml file

    .. code-block:: text

        {
            "atlassian": {
                "accounts": [
                    {
                        "label": "pro",
                        "email": "jsg@genovation.associates",
                        "tokens": [
                            {
                                "label": "GSculpt",
                                "token": "whatever"
                            }
                        ]
                    }
                ],
                "sites": [
                    {
                        "label": "genovation",
                        "jira": {
                            "projects": [
                                {
                                    "label": "GENOVATION",
                                    "key": "GENO"
                                }
                            ],
                        "resources": [
                            {
                                "label": "GET /rest/api/3/search/jql",
                                "url": "https://genovation.atlassian.net/rest/api/3/search",
                                "maps": [
                                    {
                                        "label": "flatList",
                                        "map": [
                                            {
                                                "dict.path": "id",
                                                "df.column": "id",
                                                "df.type": "int"
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

    """
    _obj_logger: Logger = getLogger(__name__)
    _obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

    # We check configuration contains all the fields we expect
    try:
        JsonChecker(dict_schema=DICT_CONFIGURATION_SCHEMA).check(json_instance=ctx_context.obj.config)
    except ValidationError as an_exception:
        msg = "Configuration file is not correct. Check `~/.genov/genov.toml`."
        raise BadParameter(msg) from an_exception

    # We fetch the account, then the token
    _dict_the_account: dict = (
        jsonata.Jsonata("atlassian.accounts[0]").evaluate(ctx_context.obj.config)
        if str_account is None
        else jsonata.Jsonata(f"atlassian.accounts[label='{str_account}']").evaluate(ctx_context.obj.config)
    )
    if _dict_the_account is None:
        msg = f"The atlassian account '{str_account}' is not configured."
        raise BadParameter(msg)

    _dict_the_token: dict = (
        jsonata.Jsonata("tokens[0]").evaluate(_dict_the_account)
        if str_token is None
        else jsonata.Jsonata(f"tokens[label='{str_token}']").evaluate(_dict_the_account)
    )
    if _dict_the_token is None:
        msg = f"The token '{str_token}' for account '{_dict_the_account['label']}' is not configured."
        raise BadParameter(msg)
    _str_the_username: str = _dict_the_account["email"]
    _str_the_password: str = _dict_the_token["token"]

    # We fetch the site, then the project
    _dict_the_site: dict = (
        jsonata.Jsonata("atlassian.sites[0]").evaluate(ctx_context.obj.config)
        if str_site is None
        else jsonata.Jsonata(f"atlassian.sites[label='{str_site}']").evaluate(ctx_context.obj.config)
    )
    if _dict_the_site is None:
        msg = f"The site '{str_site}' is not configured."
        raise BadParameter(msg)
    _dict_the_project: dict = (
        jsonata.Jsonata("jira.projects[0]").evaluate(_dict_the_site)
        if str_project is None
        else jsonata.Jsonata(f"jira.projects[label='{str_project}']").evaluate(_dict_the_site)
    )
    if _dict_the_project is None:
        msg = f"The project '{str_project}' is not configured for the site '{_dict_the_site["label"]}'."
        raise BadParameter(msg)
    _str_the_project: str = _dict_the_project["key"]

    # We fetch the resource
    _dict_the_resource: dict = jsonata.Jsonata("jira.resources[label='GET /rest/api/3/search/jql']").evaluate(
        _dict_the_site
    )
    if _dict_the_resource is None:
        msg = (
            f"The resource 'GET /rest/api/3/search/jql' is not configured for the site " f"'{_dict_the_site["label"]}'"
        )
        raise BadParameter(msg)
    _str_the_url: str = _dict_the_resource["url"]

    # We fetch the map
    _lst_the_map: list[dict] = (
        jsonata.Jsonata(f"maps[label='{str_map}']").evaluate(_dict_the_resource) if str_map is None else None
    )

    if b_as_df:
        _df_the_issues: DataFrame = JiraIssuesGetter(
            str_username=_str_the_username, str_password=_str_the_password, str_url=_str_the_url, lst_map=_lst_the_map
        ).get_issues_as_df(str_project=_str_the_project)

        ctx_context.obj[str_alias] = _df_the_issues

        if _df_the_issues is None:
            print(f"[orange]No data was loaded. Alias '{str_alias}' is set to 'None'." f"[/orange]")
        else:
            print(
                f"[green]Loaded '{len(_df_the_issues.index)}' issues as a DataFrame staged under alias '{str_alias}'."
                f"[/green]"
            )

    else:
        _dict_the_issues: dict = JiraIssuesGetter(
            str_username=_str_the_username, str_password=_str_the_password, str_url=_str_the_url, lst_map=_lst_the_map
        ).get_issues(str_project=_str_the_project)

        ctx_context.obj[str_alias] = _dict_the_issues

        print(
            f"[green]Loaded '{_dict_the_issues[JiraIssuesGetter.__ATLASSIAN_NODE_TOTAL__]}' issues as a dictionary staged under "
            f"alias '{str_alias}'.[/green]\n"
            f"[grey]Equivalent curl: '{_dict_the_issues[JiraIssuesGetter.RETURN_NODE_CURL]}'[/grey]"
        )

    _obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
