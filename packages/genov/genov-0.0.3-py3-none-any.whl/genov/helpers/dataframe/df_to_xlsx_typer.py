"""
Module to export a DataFrame as an MS Excel spreadsheet on the file system through a Typer command.
"""

from inspect import stack
from logging import Logger, getLogger
from pathlib import Path
from typing import Annotated

from pandas import DataFrame
from typer import Argument, Context

from genov.utils.typer.context_obj.context_obj import GContextObj

_logger: Logger = getLogger(__name__)


def df_to_xlsx(
    ctx_context: Context,
    str_alias: Annotated[
        str,
        Argument(
            help="The alias for the dataframe stored in context to be printed.",
            metavar="alias",
            callback=GContextObj.check_alias_name_to_get,
        ),
    ],
    path_file: Annotated[
        Path,
        Argument(
            help="The file to export the dataframe.",
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
    Persist the dataframe aliased as ALIAS in the file system as FILE.
    """
    _logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

    _obj_the_context_obj: GContextObj = ctx_context.obj

    _df_to_persist: DataFrame = _obj_the_context_obj.get_alias_value(
        str_alias=str_alias, typ_type=DataFrame, e_strict=GContextObj.Strictness.STRICT
    )

    _df_to_persist.to_excel(excel_writer=path_file)
    _logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
