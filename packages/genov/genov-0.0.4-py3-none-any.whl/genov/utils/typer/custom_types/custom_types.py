"""
The module that introduces custom types for Typer commands to accept lists and dictionaries.
"""

from ast import literal_eval

from typer import BadParameter


class CustomTypes:
    """
    A parser for Typer commands to accept dict and list parameters.
    """

    @staticmethod
    def parse_custom_class(value: str):
        """
        Callback function called by Typer when parameters are annotated as below:
        a_var: Annotated[dict, typer.Argument(parser=CustomTypes.parse_custom_class)]
        a_var: Annotated[list, typer.Argument(parser=CustomTypes.parse_custom_class)]

        :param value: the value to parse
        :return: the value parsed in the proper type
        """

        if isinstance(value, str):
            try:
                return literal_eval(value)
            except Exception as exception:
                raise BadParameter(value) from exception
        else:
            # This happens when the default value is already a typed instance (aka not a string)
            return value
