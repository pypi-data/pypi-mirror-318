"""
Module to flatten a dict object.
"""

import numbers
from enum import Enum
from inspect import stack
from logging import Logger, getLogger


class JsonFlattener:
    """
    Class to flatten a given json instance, and return back a flatten dictionary with concatenated paths along with
    their associated values.

    E.g. {"a": {"b": ["c"]}} -> {"a.b[0]": "c"}
    """

    __ERROR_1__: str = "Incorrect parameter. Dict or List expected."

    __ERROR_2__: str = "Error(s) encountered while flattening."
    __ERROR_2_1__: str = "Error encountered while flattening. Ambiguous key(s)."

    __WARNING_1__: str = "Warning(s) encountered while flattening."
    __WARNING_1_1__: str = "Warning encountered while flattening. Key should be a string."
    __WARNING_1_2__: str = (
        "Warning encountered while flattening. Value should be a string, a number, a boolean, "
        "None, a dict or a list."
    )

    _obj_logger: Logger = getLogger(__name__)

    #: If strict, an exception is thrown in case the dict object to check does not comply to json standard.
    class Strictness(Enum):
        STRICT = True
        NOT_STRICT = False

    def flatten(self, json_instance: dict | list, e_strict: Strictness = Strictness.NOT_STRICT) -> dict[str:]:
        """
        Function that flattens a given json instance, and return back a flatten dictionary with concatenated paths
        along with their associated values.

        E.g. {"a": {"b": ["c"]}} -> {"a.b[0]": "c"}

        If e_strict is set to STRICT, an exception is thrown in case the json instance does not comply to json standard.
        Otherwise, only warnings are logged (in case the json instance does not comply to json standard).

        Errors that can be thrown:

        - ERROR 1: Incorrect parameter. Dict or List expected.
        - ERROR 2: Error(s) encountered while flattening. Ambiguous key(s)
          E.g. {"1": "key as string", 1: "key as number"} would return {"1": "which value?"}
        - WARNING 1: Warning(s) encountered while flattening, raised as errors if e_strict is set to STRICT
          - WARNING 1_1: Key should be a string.
          - WARNING 1_2: Value should be a string, a number, a boolean, None, a dict or a list.

        :param json_instance: the json_instance to flatten
        :param e_strict: to raise errors in case json standard is not fully respected
        :return: a flatten json instance
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        # Warnings if e_strict is NOT_STRICT, errors otherwise
        # Eg not fully aligned with json standard.
        _lst_warnings: list = []

        # Errors, independently of e_strict
        # Eg ambiguous key (numeric key `1` which is duplicate with string key "1")
        _lst_errors: list = []

        _dict_the_return: dict

        if isinstance(json_instance, dict):
            _dict_the_return, _lst_errors, _lst_warnings = self._flatten_dict(dict_instance=json_instance)

        elif isinstance(json_instance, list):
            _dict_the_return, _lst_errors, _lst_warnings = self._flatten_list(lst_instance=json_instance)

        else:
            self._obj_logger.error(
                "Parameter json_instance is of type '%', while 'list' or " "'dict' is expected.", type(json_instance)
            )
            raise TypeError(self.__ERROR_1__)

        # We log all the errors and warnings in the console
        if _lst_errors:
            self._obj_logger.error(
                "Errors encountered while validating json instance:\n" "- %\n", "\n- ".join(_lst_errors)
            )
        if _lst_warnings:
            self._obj_logger.warning(
                "Warnings encountered while validating json instance:\n" "- %\n", "\n- ".join(_lst_warnings)
            )

        if _lst_errors:
            raise KeyError(self.__ERROR_2__)
        if _lst_warnings and (e_strict == JsonFlattener.Strictness.STRICT):
            raise SyntaxWarning(self.__WARNING_1__)

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

        return _dict_the_return

    def _flatten_dict(self, dict_instance: dict, str_prefix: str | None = None) -> (dict[str], list, list):
        """
        Recursive function to process a dictionary

        :param dict_instance: the sub dictionary to flatten
        :param str_prefix: the root path inherited from the caller
        :return: a tuple of three:
                 - The flatten sub dictionary
                 - The errors faced while flattening
                 - The warnings faced while flattening
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        _dict_the_return: dict = {}
        _lst_errors: list = []
        _lst_warnings: list = []

        for k, v in dict_instance.items():
            if not isinstance(k, str):
                _lst_warnings.append(f"'{k}': {self.__WARNING_1_1__}")

            _str_updated_k = str(k).replace("/", "//").replace(".", "/.").replace("[", "/[").replace("]", "/]")

            _str_new_prefix: str = _str_updated_k if str_prefix is None else str_prefix + "." + _str_updated_k

            if _str_new_prefix in _dict_the_return:
                _lst_errors.append(f"'{_str_new_prefix}': {self.__ERROR_2_1__}")

            if isinstance(v, dict):
                _dict_the_sub_return, _lst_sub_errors, _lst_sub_warnings = self._flatten_dict(
                    dict_instance=v, str_prefix=_str_new_prefix
                )
                _dict_the_return = _dict_the_return | _dict_the_sub_return
                _lst_errors = _lst_errors + _lst_sub_errors
                _lst_warnings = _lst_warnings + _lst_sub_warnings
            elif isinstance(v, list):
                _dict_the_sub_return, _lst_sub_errors, _lst_sub_warnings = self._flatten_list(
                    lst_instance=v, str_prefix=_str_new_prefix
                )
                _dict_the_return = _dict_the_return | _dict_the_sub_return
                _lst_errors = _lst_errors + _lst_sub_errors
                _lst_warnings = _lst_warnings + _lst_sub_warnings

            # If string
            elif isinstance(v, numbers.Number | str):
                _dict_the_return[_str_new_prefix] = v

            # If None
            elif v is None:
                _dict_the_return[_str_new_prefix] = None

            else:
                _lst_warnings.append(f"'{_str_new_prefix}', value of type '{type(v)}': " f"{self.__WARNING_1_2__}")
                _dict_the_return[_str_new_prefix] = v

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

        return _dict_the_return, _lst_errors, _lst_warnings

    def _flatten_list(self, lst_instance: list, str_prefix: str | None = None) -> (dict[str], list, list):
        """
        Recursive function to process a list

        :param lst_instance: the sub list to flatten
        :param str_prefix: the root path inherited from the caller
        :return: a tuple of three:
                 - The flatten sub dictionary
                 - The errors faced while flattening
                 - The warnings faced while flattening
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        _dict_the_return: dict = {}
        _lst_errors: list = []
        _lst_warnings: list = []

        _i_index: int = 0

        for v in lst_instance:
            _str_new_prefix: str = (
                "[" + str(_i_index) + "]" if str_prefix is None else str_prefix + "[" + str(_i_index) + "]"
            )

            if isinstance(v, dict):
                _dict_the_sub_return, _lst_sub_errors, _lst_sub_warnings = self._flatten_dict(
                    dict_instance=v, str_prefix=_str_new_prefix
                )
                _dict_the_return = _dict_the_return | _dict_the_sub_return
                _lst_errors = _lst_errors + _lst_sub_errors
                _lst_warnings = _lst_warnings + _lst_sub_warnings
            elif isinstance(v, list):
                _dict_the_sub_return, _lst_sub_errors, _lst_sub_warnings = self._flatten_list(
                    lst_instance=v, str_prefix=_str_new_prefix
                )
                _dict_the_return = _dict_the_return | _dict_the_sub_return
                _lst_errors = _lst_errors + _lst_sub_errors
                _lst_warnings = _lst_warnings + _lst_sub_warnings

            # If string
            elif isinstance(v, numbers.Number | str):
                _dict_the_return[_str_new_prefix] = v

            # If None
            elif v is None:
                _dict_the_return[_str_new_prefix] = None

            else:
                _lst_warnings.append(f"'{_str_new_prefix}', value of type " f"'{type(v)}': {self.__WARNING_1_2__}")
                _dict_the_return[_str_new_prefix] = v

            _i_index = _i_index + 1

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

        return _dict_the_return, _lst_errors, _lst_warnings
