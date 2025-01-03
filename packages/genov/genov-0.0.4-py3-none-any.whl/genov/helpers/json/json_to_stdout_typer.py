"""
Module to print a dict object to the standard output stream through a Typer command.
"""

from inspect import stack
from logging import Logger, getLogger
from typing import Annotated

from rich.console import Console
from rich.json import JSON
from typer import Argument, Context

from genov.utils.typer.context_obj.context_obj import GContextObj

_logger: Logger = getLogger(__name__)


def json_to_stdout(
    ctx_context: Context,
    str_alias: Annotated[
        str,
        Argument(
            help="The alias for the json stored in context to be printed.",
            metavar="alias",
            callback=GContextObj.check_alias_name_to_get,
        ),
    ],
):
    """
    The command prints into console the dictionary instance that is stored in context as ALIAS.
    """
    _logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

    _obj_the_context_obj: GContextObj = ctx_context.obj

    _dict_to_print: dict = _obj_the_context_obj.get_alias_value(
        str_alias=str_alias, typ_type=dict, e_strict=GContextObj.Strictness.STRICT
    )

    console = Console()
    console.print(JSON.from_data(_dict_to_print))

    _logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
