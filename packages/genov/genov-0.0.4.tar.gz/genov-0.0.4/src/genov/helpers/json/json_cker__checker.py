"""
Module to check a dict object against json standard or a given json schema provided at instantiation.
"""

from enum import Enum
from inspect import stack
from logging import Logger, getLogger
from typing import TYPE_CHECKING, ClassVar

from jsonschema.validators import validator_for

if TYPE_CHECKING:
    from jsonschema import Validator


class JsonChecker:
    """
    Class to check json objects, aka dict or list, against a given schema using the library
    (jsonschema)[https://json-schema.org/]. In case no schema is provided, the class check json objects against the
    json standards.

    (Note)[https://json-schema.org/understanding-json-schema/basics]

    - They are plenty of standards defined
    - And it's not always easy to tell which draft a JSON Schema is using
    - Therefore, it is good practice to declare which version of the JSON Schema specification the schema is written to.

    We packaged the jsonschema module to later handle composition of complex schema, if need be...
    """

    #: The json schema for standard json. Used by default when the checker is instantiated without providing any schema.
    SCHEMA_JSON: ClassVar[dict] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "http://www.genovation.associates/schemas/json",
        "title": "Json Standard",
        "description": "Schema to validate json instances against Json Standard.",
        "oneOf": [
            {
                "type": "object",
                "description": "Json is composed of json objects and json arrays. json objects are modelled as 'dict' "
                "in python. json objects have keys as string. json objects have values as string, "
                "number, boolean, `None`, json  objects or json arrays.",
                "additionalProperties": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "number"},
                        {"type": "boolean"},
                        {"const": None},
                        {"$ref": "#"},  # -> Recursion
                    ]
                },
                "propertyNames": {"type": "string"},
            },
            {
                "type": "array",
                "description": "Json is composed of json objects and json arrays. json arrays are modelled as 'list' "
                "in python. json arrays have values as string, number, boolean, `None`, json  objects "
                "or json arrays.",
                "items": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "number"},
                        {"type": "boolean"},
                        {"const": None},
                        {"$ref": "#"},  # -> Recursion
                    ]
                },
            },
        ],
    }

    _obj_logger: Logger = getLogger(__name__)

    #: If strict, the json standard is systematically checked. Otherwise, only the provided schema is checked.
    class Strictness(Enum):
        STRICT = True
        NOT_STRICT = False

    def __init__(self, dict_schema: dict | None = None, e_strict: Strictness = Strictness.NOT_STRICT):
        """
        Instantiation of a Json Checker for a given schema. If e_strict, the checker validates against json standards
        before validating against the bespoke schema.

        (Note)[https://json-schema.org/understanding-json-schema/basics]

        - They are plenty of standards defined
        - And it's not always easy to tell which draft a JSON Schema is using
        - Therefore, it is good practice to declare which version of the JSON Schema specification the schema is
          written to.

        :param dict_schema: the schema description
        :param e_strict: to check the json instances against the json standard
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        # The validator for the schema provided by the caller
        self._obj_validator_bespoke: Validator | None = None

        # The default validator to check instances against json standard
        self._obj_validator_json: Validator | None = None

        # We instantiate the validator that matches the specification mentioned by the json schema. This "specification"
        # is set under the node "$schema" (at the root of the schema).
        # E.g.
        #   - With the following node: {"$schema": "https://json-schema.org/draft/2020-12/schema"}
        #   - The function returns an instance of Draft202012Validator.
        # If no schema is mentioned, the latest version supported will be returned.
        # Always including the keyword when authoring schemas is highly recommended.
        if dict_schema is not None:
            if "$schema" not in dict_schema:
                self._obj_logger.warning(
                    "The '$schema' is not defined, therefore the latest version supported will be "
                    "returned, but it remains better practice to always include this information."
                )

            # The validator for the schema provided by the caller
            _typ_the_validator_class: type[Validator] = validator_for(schema=dict_schema)
            self._obj_validator_bespoke = _typ_the_validator_class(schema=dict_schema)

        if (e_strict == JsonChecker.Strictness.STRICT) or dict_schema is None:
            # The default validator to check instances against json standard
            _typ_the_validator_class: type[Validator] = validator_for(schema=self.SCHEMA_JSON)
            self._obj_validator_json = _typ_the_validator_class(schema=self.SCHEMA_JSON)

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

    def check(self, json_instance: dict | list):
        """
        The json instance, aka a dict or a list, is validated:

        - Against the json standards, if e_strict is set to STRICT at instantiation
        - Against bespoke schema, if provided at instantiation.

        If the json instance is validated, the function returns. Otherwise, an exception ValidationError is thrown.

        :param json_instance: the json instance to validate against the schema
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        if self._obj_validator_json:
            self._obj_validator_json.validate(instance=json_instance)

        if self._obj_validator_bespoke:
            self._obj_validator_bespoke.validate(instance=json_instance)

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)
