"""
Module to print the loaded configuration to the standard output stream. Handy to check and debut your configuration
file that is stored under '~/.genov/genov.toml'.
"""

from inspect import stack
from logging import Logger, getLogger
from typing import TYPE_CHECKING

from rich.console import Console
from rich.json import JSON
from typer import Context

if TYPE_CHECKING:
    from genov.utils.typer.config.config import GConfig

_obj_logger: Logger = getLogger(__name__)


def cfg_to_stdout(
    ctx_context: Context,
):
    """
    Print into console the content of the configuration file stored under ~/.genov/genov.toml.
    """
    _obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

    _config: GConfig = ctx_context.obj.config

    console = Console()
    console.print(JSON.from_data(_config))

    _obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
