"""
Module to export a dict object as a json file through a Typer command.
"""

from inspect import stack
from json import dump
from logging import Logger, getLogger
from pathlib import Path
from typing import Annotated

from typer import Argument, Context

from genov.utils.typer.context_obj.context_obj import GContextObj

_logger: Logger = getLogger(__name__)


def json_to_file(
    ctx_context: Context,
    str_alias: Annotated[
        str,
        Argument(
            help="The alias for the json stored in context to be printed.",
            metavar="alias",
            callback=GContextObj.check_alias_name_to_get,
        ),
    ],
    path_file: Annotated[
        Path,
        Argument(
            help="The file to export the dict.",
            metavar="file",
            exists=False,
            file_okay=True,
            dir_okay=False,
            writable=True,
            readable=True,
            resolve_path=True,
        ),
    ],
):
    """
    The command persists the dictionary instance that is stored in context as ALIAS in the file system as FILE.
    """
    _logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

    _obj_the_context_obj: GContextObj = ctx_context.obj

    _dict_to_persist: dict = _obj_the_context_obj.get_alias_value(
        str_alias=str_alias, typ_type=dict, e_strict=GContextObj.Strictness.STRICT
    )

    with open(path_file, "w") as file:
        dump(_dict_to_persist, indent=4, fp=file)

    _logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
