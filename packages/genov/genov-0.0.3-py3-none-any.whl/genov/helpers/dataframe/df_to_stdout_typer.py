"""
Module to print a DataFrame to the standard output stream through a Typer command.
"""

from inspect import stack
from logging import Logger, getLogger
from typing import Annotated

from pandas import DataFrame
from rich.console import Console
from rich.table import Table
from typer import Argument, Context

from genov.utils.typer.context_obj.context_obj import GContextObj

_logger: Logger = getLogger(__name__)


def df_to_stdout(
    ctx_context: Context,
    str_alias: Annotated[
        str,
        Argument(
            help="The alias for the dataframe stored in context to be printed.",
            metavar="alias",
            callback=GContextObj.check_alias_name_to_get,
        ),
    ],
):
    """
    The command prints into console the dataframe instance that is stored in context as ALIAS.
    """
    _logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

    _obj_the_context_obj: GContextObj = ctx_context.obj

    _df_to_print: DataFrame = _obj_the_context_obj.get_alias_value(
        str_alias=str_alias, typ_type=DataFrame, e_strict=GContextObj.Strictness.STRICT
    )

    console = Console()
    table = Table(str_alias)
    table.add_row(_df_to_print.to_string())
    console.print(table)

    _logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
