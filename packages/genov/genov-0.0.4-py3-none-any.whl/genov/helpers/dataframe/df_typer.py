"""
Module to type columns in a DataFrame.
"""

from inspect import stack
from logging import Logger, getLogger
from typing import ClassVar

from pandas import DataFrame, to_datetime, to_numeric

from genov.helpers.json.json_cker__checker import JsonChecker


class DfTyper:
    """
    Class to type columns in a DataFrame.
    """

    #: Column to type as a string
    TYPE_STRING: str = "string"
    #: Column to type as a datetime
    TYPE_DATETIME: str = "datetime"
    #: Column to type as a date
    TYPE_DATE: str = "date"
    #: Column to type as a float
    TYPE_FLOAT: str = "float"
    #: Column to type as an integer
    TYPE_INT: str = "int"

    #: All the eligible types
    TYPES: ClassVar[list[str]] = [TYPE_STRING, TYPE_DATE, TYPE_DATETIME, TYPE_INT, TYPE_FLOAT]

    #: In the map to type columns in a DataFrame, the node 'column.label' is the column label to type
    NODE_LBL: str = "column.label"
    #: In the map to type columns in a DataFrame, the node 'column.type' is the target type for a given column
    NODE_TYP: str = "column.type"

    #: The json schema for the map to type columns in a DataFrame
    DICT_MAP_SCHEMA: ClassVar[dict] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "array",
        "items": {
            "type": "object",
            "required": [NODE_LBL, NODE_TYP],
            "additionalProperties": False,
            "properties": {NODE_LBL: {"type": "string"}, NODE_TYP: {"enum": TYPES}},
        },
    }

    _obj_logger: Logger = getLogger(__name__)

    def __init__(self, lst_map: list[dict[str:str]]):
        """
        Instantiation of a DataFrame Typer.

        The map provided as a parameter lists the columns to be typed, along with the target type:

        .. code-block:: text

            [
                {   column.label: a column label, column.type: a type }
                ...
            ]

        Columns can be typed as:
        - string
        - datetime
        - date
        - float
        - int.

        :param lst_map: the map that list the columns to be typed, and the target types
        """
        # We check the map is correct, and persist it for later
        JsonChecker(dict_schema=self.DICT_MAP_SCHEMA).check(json_instance=lst_map)
        self._lst_map: list[dict[str:str]] = lst_map

    def df_type(self, df_instance: DataFrame) -> DataFrame:
        """
        The function transform the DataFrame df_instance according to the map provided at initialization.

        Exceptions are thrown:
        - When a column parametrized as to be typed cannot be found in the DataFrame instance
        - During the transformation, whenever errors occur.

        :param df_instance: the DataFrame to type
        :return: the same DataFrame with the relevant columns typed
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        # For each column to type
        for _i_dict_col in self._lst_map:
            _str_col_lbl: str = _i_dict_col[self.NODE_LBL]
            _str_col_typ: str = _i_dict_col[self.NODE_TYP]

            # If the column does not exist in the dataframe
            if _str_col_lbl not in df_instance.columns:
                msg = f"Column '{_str_col_lbl}' is to be typed to '{_str_col_typ}', but does not exist in" f"dataframe."
                raise TypeError(msg)

            if _str_col_typ == self.TYPE_STRING:
                try:
                    df_instance[_str_col_lbl] = df_instance[_str_col_lbl].astype(str)
                except Exception as an_exception:
                    msg = f"Exception when typing column '{_str_col_lbl}' to '{_str_col_typ}'."
                    raise TypeError(msg) from an_exception

            elif _str_col_typ == self.TYPE_DATETIME:
                try:
                    df_instance[_str_col_lbl] = to_datetime(df_instance[_str_col_lbl])
                except Exception as an_exception:
                    msg = f"Exception when typing column '{_str_col_lbl}' to '{_str_col_typ}'."
                    raise TypeError(msg) from an_exception

            elif _str_col_typ == self.TYPE_DATE:
                try:
                    df_instance[_str_col_lbl] = to_datetime(df_instance[_str_col_lbl]).dt.date
                except Exception as an_exception:
                    msg = f"Exception when typing column '{_str_col_lbl}' to '{_str_col_typ}'."
                    raise TypeError(msg) from an_exception

                # The below happens when column is empty, and fully made of NaT
                if str(df_instance[_str_col_lbl].dtype).startswith("datetime"):
                    df_instance[_str_col_lbl] = df_instance[_str_col_lbl].astype("object")

            elif _str_col_typ == self.TYPE_FLOAT:
                try:
                    df_instance[_str_col_lbl] = to_numeric(arg=df_instance[_str_col_lbl], downcast="float")
                except Exception as an_exception:
                    msg = f"Exception when typing column '{_str_col_lbl}' to '{_str_col_typ}'."
                    raise TypeError(msg) from an_exception

            elif _str_col_typ == self.TYPE_INT:
                try:
                    df_instance[_str_col_lbl] = to_numeric(arg=df_instance[_str_col_lbl], downcast="integer")
                except Exception as an_exception:
                    msg = f"Exception when typing column '{_str_col_lbl}' to '{_str_col_typ}'."
                    raise TypeError(msg) from an_exception
            else:
                msg = (
                    f"When transcoding the date extract, we did not know what to do with column '{_str_col_lbl}' "
                    f"as we don't know the target type '{_str_col_typ}'..."
                )
                raise TypeError(msg)

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

        return df_instance
