# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ModelTypeEnum(str, Enum):
    """
    This will describe the type of Model balanced, speed, accuracy...
    """

    """
    allowed enum values
    """
    BALANCED = 'BALANCED'
    SPEED = 'SPEED'
    ACCURACY = 'ACCURACY'

    @classmethod
    def from_json(cls, json_str: str) -> ModelTypeEnum:
        """Create an instance of ModelTypeEnum from a JSON string"""
        return ModelTypeEnum(json.loads(json_str))


