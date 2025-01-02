"""
Module to handle the configuration file that is expected to be persisted under '~/.genov/genov.toml'.
"""

from inspect import stack
from logging import Logger, getLogger
from pathlib import Path

from rich import print
from rich.panel import Panel
from rich.text import Text
from tomlkit import TOMLDocument, parse
from tomlkit.exceptions import ParseError


class GConfig(dict):
    """
    The genov application relies on a configuration file stored under ~/.genov/genov.toml. This file is loaded when
    the command line genov is called, and available through this GConfig class which extends dict.
    """

    __FILE_NAME__: str = ".genov/genov.toml"

    __ERROR_01__ = "[ERROR_01 - Missing configuration file]"
    __ERROR_02__ = "[ERROR_02 - Incorrect toml file]"

    _obj_logger: Logger = getLogger(__name__)

    def __init__(self):
        """
        During instantiation, the path to the configuration file is retrieved as ~/.genov/genov.toml, then its content
        is loaded and initialized as a dictionary instance.
        """
        self._path: Path = self._get_path_to_config_file()
        self._toml_document: TOMLDocument = self._load_config(path=self._path)
        super().__init__(self._toml_document.value)

    def _load_config(self, path: Path) -> TOMLDocument:
        """
        The function loads the configuration file that is stored under ~/.genov/genov.toml, and parses its content.

        Errors can occur, and exceptions are thrown:
        - ERROR 1, configuration file is missing at path
        - ERROR 2, configuration file could not be parsed as a toml file.
        :param path: the path where the configuration file is stored
        :return: an instance of tomlkit.TOMLDocument
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        if path.is_file() is False:
            text = (
                Text()
                .append("Error:\n", style="bold blink red")
                .append(f"ERROR 1 - Configuration file is missing at path '{path}'.")
            )
            print(Panel(text))
            raise FileNotFoundError(GConfig.__ERROR_01__)

        try:
            obj_the_return: TOMLDocument = parse(path.read_text())
        except ParseError as an_exception:
            text = (
                Text()
                .append("Error:\n", style="bold blink red")
                .append(f"ERROR 2 - Configuration file at path '{path}' could not be parsed as a Toml file.")
            )
            print(Panel(text))
            raise SyntaxError(GConfig.__ERROR_02__) from an_exception

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

        return obj_the_return

    def _get_path_to_config_file(self) -> Path:
        """
        Function that returns the path where the configuration file is stored, aka ~/.genov/genov.toml. This
        function is mocked within tests, not to rely on the file system where the tests are executed.
        """
        return Path.home().joinpath(GConfig.__FILE_NAME__)
