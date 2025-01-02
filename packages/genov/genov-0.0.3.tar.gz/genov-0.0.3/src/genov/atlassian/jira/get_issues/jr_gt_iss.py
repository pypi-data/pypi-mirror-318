"""
Module to retrieve issues from Jira.
"""

from inspect import stack
from logging import Logger, getLogger
from typing import ClassVar

import requests
from jsonata.jsonata import Jsonata
from pandas import DataFrame, json_normalize
from requests import Response
from requests.auth import HTTPBasicAuth

from genov.helpers.dataframe.df_typer import DfTyper
from genov.helpers.json.json_cker__checker import JsonChecker


class JiraIssuesGetter:
    """
    Class to retrieve issues from a jira project, either as a dictionary or a dataframe.

    Atlassian provides a Rest API that returns issues through a json response. This json response is parsed:
    - Only the relevant json fields are kept
    - They are eventually mapped and typed into DataFrame columns.

    This parsing logic is configured through a map, which is a list of dictionaries of the kind:

    .. code-block:: text

        [
            dict.path: path to the field in the json,
            df.column: the label of the column in the DataFrame to be returned,
            df.type:   the type of the column in the DataFrame to be returned
        ]

    All the fields returned by Atlassian in the json response are discarded, unless provided in the map.

    `dict.path` should comply to [Jsonata](www.jsonata.org) standards.
    """

    # The keys to use in the map
    # We reuse the keys as defined in DfTyper

    #: In the map to transform the json message from Atlassian into a DataFrame, the node 'dict.path' is the json path
    #: to a field to retrieve
    MAP_NODE_PATH: str = "dict.path"
    #: In the map to transform the json message from Atlassian into a DataFrame, the node 'df.column' is the column
    #: label in the returned DataFrame
    MAP_NODE_COLUMN: str = "df.column"
    #: In the map to transform the json message from Atlassian into a DataFrame, the node 'df.type' is the column
    #: type in the returned DataFrame
    MAP_NODE_TYPE: str = "df.type"

    #: The json schema for the map to transform the json message from Atlassian into a DataFrame
    MAP_SCHEMA: ClassVar[dict] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "array",
        "minItems": 1,
        "items": {
            "type": "object",
            "required": [MAP_NODE_PATH, MAP_NODE_COLUMN],
            "additionalProperties": False,
            "properties": {
                MAP_NODE_PATH: {"type": "string"},
                MAP_NODE_COLUMN: {"type": "string"},
                MAP_NODE_TYPE: {"enum": DfTyper.TYPES},
            },
        },
    }

    # The types to use in the map
    # We reuse the types as defined in DfTyper

    #: In the map to transform the json message from Atlassian into a DataFrame, the DataFrame column typed as string
    MAP_TYPE_STRING: str = DfTyper.TYPE_STRING
    #: In the map to transform the json message from Atlassian into a DataFrame, the DataFrame column typed as datetime
    MAP_TYPE_DATETIME: str = DfTyper.TYPE_DATETIME
    #: In the map to transform the json message from Atlassian into a DataFrame, the DataFrame column typed as date
    MAP_TYPE_DATE: str = DfTyper.TYPE_DATE
    #: In the map to transform the json message from Atlassian into a DataFrame, the DataFrame column typed as float
    MAP_TYPE_FLOAT: str = DfTyper.TYPE_FLOAT
    #: In the map to transform the json message from Atlassian into a DataFrame, the DataFrame column typed as int
    MAP_TYPE_INT: str = DfTyper.TYPE_INT

    # Default map with only native fields
    __MAP_DEFAULT__: ClassVar[list[dict]] = [
        {MAP_NODE_PATH: "id", MAP_NODE_COLUMN: "id", MAP_NODE_TYPE: MAP_TYPE_INT},
        {MAP_NODE_PATH: "key", MAP_NODE_COLUMN: "key"},
        {MAP_NODE_PATH: "fields.summary", MAP_NODE_COLUMN: "summary"},
        {MAP_NODE_PATH: "fields.resolution.name", MAP_NODE_COLUMN: "resolution"},
        {MAP_NODE_PATH: "fields.status.name", MAP_NODE_COLUMN: "status"},
        {MAP_NODE_PATH: "fields.issuetype.name", MAP_NODE_COLUMN: "type"},
        {MAP_NODE_PATH: "fields.parent.id", MAP_NODE_COLUMN: "parent", MAP_NODE_TYPE: MAP_TYPE_INT},
        {MAP_NODE_PATH: "fields.created", MAP_NODE_COLUMN: "created", MAP_NODE_TYPE: MAP_TYPE_DATE},
        {MAP_NODE_PATH: "fields.updated", MAP_NODE_COLUMN: "updated", MAP_NODE_TYPE: MAP_TYPE_DATE},
        {MAP_NODE_PATH: "fields.priority.name", MAP_NODE_COLUMN: "priority"},
        {MAP_NODE_PATH: "fields.assignee.displayName", MAP_NODE_COLUMN: "assignee"},
        {MAP_NODE_PATH: "fields.creator.displayName", MAP_NODE_COLUMN: "creator"},
    ]

    # The keys in the json response received from Atlassian
    __ATLASSIAN_NODE_ISSUES__: str = "issues"
    __ATLASSIAN_NODE_MAX_RESULT__: str = "maxResults"
    __ATLASSIAN_NODE_START_AT__: str = "startAt"
    __ATLASSIAN_NODE_TOTAL__: str = "total"

    # The keys in the json we return

    #: When retrieving the issues from Atlassian as a json, the node that contains the list of issues
    RETURN_NODE_ISSUES: str = "issues"
    #: When retrieving the issues from Atlassian as a json, the node that contains the total number of issues fetched
    RETURN_NODE_TOTAL: str = "total"
    #: When retrieving the issues from Atlassian as a json, the node that contains the equivalent curl request
    RETURN_NODE_CURL: str = "curl"

    _obj_logger: Logger = getLogger(__name__)

    def __init__(self, str_username: str, str_password: str, str_url: str, lst_map: list[dict] | None = None):
        """
        The JiraIssuesGetter is instantiated for one user accessing to one project.

        :param str_username: the token username
        :param str_password: the token password
        :param str_url: the url to the REST API
        :param lst_map: the map to transform the message received from Atlassian, and only keep the meaningful data
        """

        self._str_username: str = str_username
        self._str_password: str = str_password
        self._str_url: str = str_url

        # We check the map is correct, and persist it for later
        if lst_map is None:
            lst_map = self.__MAP_DEFAULT__
        JsonChecker(dict_schema=self.MAP_SCHEMA).check(json_instance=lst_map)
        self._lst_map: list[dict] = lst_map

        # We instantiate an instance of jsonata to reduce the json response from atlassian
        self._str_jsonata_expression: str = self._jsonate(lst_map=lst_map)
        self._obj_jsonata: Jsonata = Jsonata(self._str_jsonata_expression)

        # We instantiate an instance of DataFrame Typer
        self._obj_df_typer: DfTyper = DfTyper(
            lst_map=[
                {DfTyper.NODE_LBL: _i_map_line[self.MAP_NODE_COLUMN], DfTyper.NODE_TYP: _i_map_line[self.MAP_NODE_TYPE]}
                for _i_map_line in self._lst_map
                if self.MAP_NODE_TYPE in _i_map_line
            ]
        )

    def _jsonate(self, lst_map: list[dict]) -> str:
        """
        Helper function to translate the map into a jsonata expression.

        Example:
        - For a map of the kind:
            [
                {'df.column': 'df.id',      'dict.path': 'id'},
                {'df.column': 'df.label',   'dict.path': 'label'}
            ]
        - We expect the following expression:
            (
                {
                    "total": total,
                    "issues": issues.{
                        "df.id": id,
                        "df.label": label
                    }
                }
            )

        :param lst_map: the map to translate
        :return: the resulting jsonate expression
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        _str_the_return: str = f"""
            (
                {{
                    "{self.RETURN_NODE_TOTAL}": {self.__ATLASSIAN_NODE_TOTAL__},
                    "{self.RETURN_NODE_ISSUES}": {JiraIssuesGetter.__ATLASSIAN_NODE_ISSUES__}.{{
                        {
                            ", ".join(
                                [
                                    f"\"{i_map[self.MAP_NODE_COLUMN]}\": {i_map[self.MAP_NODE_PATH]}"
                                    for i_map in lst_map
                                ]
                            )
                        }
                    }}
                }}
            )
            """

        self._obj_logger.debug("Jsonated map: %", _str_the_return)

        self._obj_logger.debug("Function '% - %' is returning", stack()[0].filename, stack()[0].function)

        return _str_the_return

    def get_response(self, str_project: str, int_start: int = 0, int_max: int = 50) -> dict:
        """
        Function to call the Atlassian REST API (eventually recursively in case the response contains several pages)
        and return a "concatenated" json response as received from Atlassian.

        :param str_project: the Jira project
        :param int_start: the index of the first item to return in a page of results (page offset).
        :param int_max: the maximum number of items to return per page.
        :return: a dict object with the full list of issues, in the json format received by Atlassian
        """

        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        _dict_the_query: dict = {
            "jql": "project = " + str_project,
            "startAt": int_start,
            "maxResults": int_max,
            # 'nextPageToken': '<string>',
            # 'fields': 'summary,key',
            # 'expand': 'versionedRepresentations',
            # 'reconcileIssues': '{versionedRepresentations}'
        }

        _obj_the_response: Response = requests.request(
            "GET",
            self._str_url,
            headers={"Accept": "application/json"},
            params=_dict_the_query,
            auth=HTTPBasicAuth(self._str_username, self._str_password),
        )

        if _obj_the_response.status_code != requests.codes["ok"]:
            msg = f"REST requested returned '{_obj_the_response.status_code}'."
            raise ConnectionError(msg)

        _dict_the_response_from_json: dict = _obj_the_response.json()

        _lst_missing_nodes: list[str] = [
            i_node
            for i_node in [
                self.__ATLASSIAN_NODE_ISSUES__,
                self.__ATLASSIAN_NODE_MAX_RESULT__,
                self.__ATLASSIAN_NODE_START_AT__,
                self.__ATLASSIAN_NODE_TOTAL__,
            ]
            if i_node not in _dict_the_response_from_json
        ]
        if len(_lst_missing_nodes) > 0:
            msg = (
                f"Unexpected answer from Atlassian which misses the following nodes: "
                f"{", ".join(_lst_missing_nodes)}"
            )
            raise SyntaxError(msg)

        # We recursively call the function...
        _int_the_max_result: int = _dict_the_response_from_json[self.__ATLASSIAN_NODE_MAX_RESULT__]
        _int_the_start_at: int = _dict_the_response_from_json[self.__ATLASSIAN_NODE_START_AT__]
        _int_the_total: int = _dict_the_response_from_json[self.__ATLASSIAN_NODE_TOTAL__]

        if _int_the_total > (_int_the_start_at + _int_the_max_result):
            _dict_next_page_response: dict = self.get_response(
                str_project=str_project, int_start=_int_the_start_at + _int_the_max_result, int_max=_int_the_max_result
            )

            # We concatenate the list of issues
            _dict_the_response_from_json[self.__ATLASSIAN_NODE_ISSUES__] = (
                _dict_the_response_from_json[self.__ATLASSIAN_NODE_ISSUES__]
                + _dict_next_page_response[self.__ATLASSIAN_NODE_ISSUES__]
            )

        self._obj_logger.debug(
            "Function '% - %' is returning a list containing '%' issues as json.",
            stack()[0].filename,
            stack()[0].function,
            len(_dict_the_response_from_json[self.__ATLASSIAN_NODE_ISSUES__]),
        )

        return _dict_the_response_from_json

    def get_issues(self, str_project: str, int_start: int = 0, int_max: int = 50) -> dict:
        """
        Function to call the Atlassian REST API (eventually recursively in case the response contains several pages)
        and return a "concatenated" list of issues as dict, with only the fields listed in the map.

        :param str_project: the Jira project
        :param int_start: the index of the first item to return in a page of results (page offset).
        :param int_max: the maximum number of items to return per page.
        :return: a dict object with the full list of issues, only containing the fields listed in the map.
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        _dict_full_response: dict = self.get_response(str_project=str_project, int_max=int_max, int_start=int_start)

        _dict_the_return: dict = self._obj_jsonata.evaluate(_dict_full_response)

        # In case the array "issues" is empty, jsonata does not return the node at all. We need to add it
        if self.__ATLASSIAN_NODE_ISSUES__ not in _dict_the_return:
            _dict_the_return[self.RETURN_NODE_ISSUES] = []

        # In case the node "total" is equal to 0, jsonata does not return the node at all. We need to add it
        # if self.NODE_total not in _dict_the_return:
        #    _dict_the_return[self.NODE_total] = 0

        _dict_the_return[self.RETURN_NODE_CURL] = (
            f"curl -D- -u {self._str_username}:[xxx password xxx] -X GET -H 'Content-Type: application/json' "
            f"'{self._str_url}?jql=project={str_project}'"
        )

        self._obj_logger.debug(
            "Function '% - %' is returning a list containing '%' issues as json.",
            stack()[0].filename,
            stack()[0].function,
            _dict_the_return[self.__ATLASSIAN_NODE_TOTAL__],
        )

        return _dict_the_return

    def get_issues_as_df(self, str_project: str, int_start: int = 0, int_max: int = 50) -> DataFrame | None:
        """
        Function to call the Atlassian REST API (eventually recursively in case the response contains several pages)
        and return a "concatenated" list of issues as a DataFrame as defined in the map (aka set of fields and types).

        :param str_project: the Jira project
        :param int_start: the index of the first item to return in a page of results (page offset).
        :param int_max: the maximum number of items to return per page.
        :return: a DataFrame with the full list of issues, None if no issue is to be returned.
        """
        self._obj_logger.debug("Function '% - %' is called", stack()[0].filename, stack()[0].function)

        _dict_issues_as_json: dict = self.get_issues(str_project=str_project, int_max=int_max, int_start=int_start)

        if len(_dict_issues_as_json[JiraIssuesGetter.RETURN_NODE_ISSUES]) == 0:
            return None

        _df_the_return: DataFrame = json_normalize(_dict_issues_as_json[JiraIssuesGetter.RETURN_NODE_ISSUES])

        _df_the_return = self._obj_df_typer.df_type(_df_the_return)

        self._obj_logger.debug(
            "Function '% - %' is returning a list containing '%' issues as lines in dataframe",
            stack()[0].filename,
            stack()[0].function,
            len(_df_the_return.index),
        )

        return _df_the_return
