"""
The module where objects can be staged and shared across Typer commands, as part of the context.
"""

import re
from enum import Enum
from inspect import stack
from logging import Logger, getLogger
from typing import TypeVar

from rich import print
from rich.panel import Panel
from rich.text import Text
from typer import BadParameter, Context


class GContextObj(dict):
    """
    Typer framework provides a context where commands stage data to be shared with others. Commands access a property
    `Context.obj` that we declare as an instance of GContextObj.

    GContextObj is primarily extending `dict`, where commands can stage date under a given alias, or retrieve date
    from a given alias.

    GContextObj provides as well a few helper functions, among which:

    - When getting data from an alias, checking whether the alias was previously set by another command
    - When staging date under an alias, checking whether the alias was previously used
    - Getting data from an alias within the proper class
    - When staging data, the alias is checked to comply to the regex `^[a-z_]+$` (aka lowercase alpha, and underscore).
    """

    __ERROR_01__ = "[ERROR_01 - Incorrect alias name]"
    __ERROR_02__ = "[ERROR_02 - Inexistant alias name]"
    __ERROR_03__ = "[ERROR_03 - Incorrect type]"

    _obj_logger: Logger = getLogger(__name__)

    _obj_alias_regex: re.Pattern = re.compile("^[a-z_]+$")

    @property
    def alias(self) -> list[str]:
        return self._alias

    def __init__(self):
        """
        During initialization, we instantiate:

        - A list with all the alias that are set/get, so we can spot when commands try to access missing alias, or
          when a command override an alias previously set
        - The regex we will use to check the alias' names, so they are only lower case alphas, with `_`.
        """
        super().__init__()
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        self._alias: list[str] = []

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

    def __setitem__(self, alias, data):
        """
        Called to implement staging of data to self[alias].
        The super dict function is called after having checked that key complies to the regex `^[a-z_]+$` (aka
        lowercase alpha, and underscore). If alias does not comply to the regex, an error is thrown.

        :param alias: alias for the data to stage
        :param data: the data to stage
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        # The alias should only contain alpha characters and "_"
        if self._obj_alias_regex.match(alias) is None:
            self._obj_logger.fatal(f"{self.__ERROR_01__} {stack()[0].function}")
            raise SyntaxError(self.__ERROR_01__)

        if alias in self:
            self._obj_logger.info(
                "Function '% - %': alias '%' overridden.", stack()[0].filename, stack()[0].function, alias
            )

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

        dict.__setitem__(self, alias, data)

    @staticmethod
    def check_alias_name_to_get(ctx_context: Context, str_alias: str) -> str:
        """
        Used as callback in Typer commands to check during completion that the alias about to be requested was
        effectively set previously. Raise an exception otherwise.

        :param ctx_context: the Typer context
        :param str_alias: the alias to check
        :return: str_alias, as requested by Typer
        """
        if ctx_context.resilient_parsing:
            return str_alias

        if GContextObj._obj_alias_regex.match(str_alias) is None:
            GContextObj._obj_logger.fatal(f"{GContextObj.__ERROR_01__} " f"{stack()[0].function}")
            print(
                Panel(
                    Text()
                    .append("Error:\n", style="bold blink red")
                    .append(f"Alias '{str_alias}' is incorrect, as it does not follow naming convention: '^[a-z_]+$'.")
                )
            )
            raise BadParameter(GContextObj.__ERROR_01__)

        _obj_the_obj: GContextObj = ctx_context.obj

        if str_alias not in _obj_the_obj.alias:
            GContextObj._obj_logger.fatal(f"{GContextObj.__ERROR_02__} " f"{stack()[0].function}")
            print(
                Panel(
                    Text()
                    .append("Error:\n", style="bold blink red")
                    .append(f"Alias '{str_alias}' does not exist in context.")
                )
            )
            raise BadParameter(GContextObj.__ERROR_02__)

        return str_alias

    @staticmethod
    def check_alias_name_to_set(ctx_context: Context, str_alias: str) -> str:
        """
        Used as callback in the typer commands to check during completion that the alias about to be set was not
        previously used. Warn the user otherwise.

        :param ctx_context: the Typer context
        :param str_alias: the alias to check
        :return: str_alias, as requested by Typer
        """
        if ctx_context.resilient_parsing:
            return str_alias

        if GContextObj._obj_alias_regex.match(str_alias) is None:
            GContextObj._obj_logger.fatal(f"{GContextObj.__ERROR_01__} " f"{stack()[0].function}")
            print(
                Panel(
                    Text()
                    .append("Error:\n", style="bold blink red")
                    .append(f"Alias '{str_alias}' is incorrect, as it does not follow naming convention: '^[a-z_]+$'.")
                )
            )
            raise BadParameter(GContextObj.__ERROR_01__)

        _obj_the_obj: GContextObj = ctx_context.obj

        if str_alias in _obj_the_obj.alias:
            text = Text()
            text.append("Warning:\n", style="bold orange_red1")
            text.append(f"Alias '{str_alias}' already exists in context. It will be override.")
            print(Panel(text))

        _obj_the_obj.alias.append(str_alias)

        return str_alias

    T = TypeVar("T")

    class Strictness(Enum):
        STRICT = True
        NOT_STRICT = False

    def get_alias_value(
        self, str_alias: str, typ_type: type[T], e_strict: Strictness = Strictness.NOT_STRICT
    ) -> T | None:
        """
        Get the value of an alias cast in the requested type. When the alias value is not an instance of the
        requested type:
        - If b-strict is set to True, an exception is thrown
        - Otherwise, a warning is displayed in the console, and None is returned.

        :param str_alias: the alias for the staged data to retrieve
        :param typ_type: the type to cast staged data
        :param e_strict: to raise Exception in case the staged data is not an instance of the requested return type
        :return: the staged data
        """

        if str_alias not in self:
            raise KeyError(str_alias)

        _obj_the_object: typ_type = self[str_alias]

        if not isinstance(_obj_the_object, typ_type):
            if e_strict == self.Strictness.STRICT:
                GContextObj._obj_logger.fatal(f"{GContextObj.__ERROR_03__} " f"{stack()[0].function}")
                print(
                    Panel(
                        Text()
                        .append("Error:\n", style="bold blink red")
                        .append(
                            f"Alias '{str_alias}' is of type '{type(_obj_the_object)}', which is not an instance "
                            f"of '{typ_type}'."
                        )
                    )
                )
                raise BadParameter(GContextObj.__ERROR_03__)

            text = Text()
            text.append("Warning:\n", style="bold orange_red1")
            text.append(
                f"Alias '{str_alias}' is of type '{type(_obj_the_object)}', which is not an instance of "
                f"'{typ_type}'."
            )
            print(Panel(text))
            return None

        return _obj_the_object
