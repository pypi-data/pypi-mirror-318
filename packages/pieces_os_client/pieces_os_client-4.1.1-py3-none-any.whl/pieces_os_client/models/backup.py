# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.platform_enum import PlatformEnum

class Backup(BaseModel):
    """
    This is a cloud Backup. This is specific metadata needed inorder to retrieve a Backup.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(...)
    version: StrictStr = Field(...)
    timestamp: StrictStr = Field(...)
    bytes: Union[StrictFloat, StrictInt] = Field(...)
    created: GroupedTimestamp = Field(...)
    device_name: StrictStr = Field(...)
    platform: PlatformEnum = Field(...)
    __properties = ["schema", "id", "version", "timestamp", "bytes", "created", "device_name", "platform"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Backup:
        """Create an instance of Backup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Backup:
        """Create an instance of Backup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Backup.parse_obj(obj)

        _obj = Backup.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "version": obj.get("version"),
            "timestamp": obj.get("timestamp"),
            "bytes": obj.get("bytes"),
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "device_name": obj.get("device_name"),
            "platform": obj.get("platform")
        })
        return _obj


