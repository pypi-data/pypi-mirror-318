"""
The main entry point for Python Typer commands. All commands made accessible through command lines are declared here,
along with the higher level options (such as verbosity).
"""

from inspect import stack
from logging import Logger, basicConfig, getLogger
from typing import Annotated

from rich import print
from rich.panel import Panel
from typer import Context, Option, Typer

from genov.atlassian.jira.get_issues.jr_gt_iss_typer import jira_get_issues_typer
from genov.helpers.dataframe.df_to_stdout_typer import df_to_stdout
from genov.helpers.dataframe.df_to_xlsx_typer import df_to_xlsx
from genov.helpers.json.json_to_file_typer import json_to_file
from genov.helpers.json.json_to_stdout_typer import json_to_stdout
from genov.utils.typer.config.config import GConfig
from genov.utils.typer.config.config_typer import cfg_to_stdout
from genov.utils.typer.context_obj.context_obj import GContextObj

# The commands
from genov.welcome.welcome_typer import welcome_typer

# We instantiate the typer application
obj_genov = Typer(
    chain=True,  # To chain commands
    no_args_is_help=True,  # When no parameter, help is displayed
    rich_markup_mode="rich",  # To get rich markup in helpers
)

# We register the commands here.
obj_genov.command("welcome")(welcome_typer)
obj_genov.command("jr-gt-iss")(jira_get_issues_typer)
obj_genov.command("df-to-stdout")(df_to_stdout)
obj_genov.command("df-to-xlsx")(df_to_xlsx)
obj_genov.command("dict-to-stdout")(json_to_stdout)
obj_genov.command("dict-to-json")(json_to_file)
obj_genov.command("cfg-to-stdout")(cfg_to_stdout)


## We add a callback
@obj_genov.callback()
def main(
    ctx_context: Context,
    b_verbose: Annotated[
        bool | None,
        Option(
            "--verbose/--no-verbose",
            "-v",
            help="Level of logging verbosity: INFO (--verbose), WARNING (default) or ERROR (--no-verbose).",
            show_default="WARNING",
        ),
    ] = None,
):
    """
    Genov tool box, the application with all the commands you need in your day-to-day work at Genovation.

    Use the VERBOSE parameter to set the level of logs you need, and let you guide by the HELP.
    """

    _obj_logger: Logger = getLogger(__name__)
    _str_log_msg: str

    _obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

    if b_verbose is True:
        _str_log_msg = "[bold red]Logging: DEBUG[/bold red]"
        basicConfig(level="DEBUG")
    elif b_verbose is False:
        _str_log_msg = "[bold blue]Logging: ERROR[/bold blue]"
        basicConfig(level="ERROR")
    else:
        _str_log_msg = "[bold orange]Logging: WARNING[/bold orange]"
        basicConfig(level="WARNING")

    print(Panel(f"{_str_log_msg}\n" f"Welcome to the Genovation toolbox!"))

    # We load the configuration
    try:
        _obj_the_config: GConfig = GConfig()
        dict_the_config: dict = _obj_the_config
    except Exception as an_exception:
        msg = "Configuration file is incorrect! Run cfg_check to get the issues to fix."
        raise SyntaxError(msg) from an_exception

    # Ensure that ctx_context.obj exists and is an instance of genov.utils.context.Context
    # This is effectively the context, that is shared across commands
    if not ctx_context.obj:
        _obj_logger.debug("We call function ctx_context.ensure_object(genov.utils.context.context.Context)")
        ctx_context.ensure_object(GContextObj)

    ctx_context.obj.config = dict_the_config

    _obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
    _obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)


if __name__ == "__main__":
    obj_genov()
