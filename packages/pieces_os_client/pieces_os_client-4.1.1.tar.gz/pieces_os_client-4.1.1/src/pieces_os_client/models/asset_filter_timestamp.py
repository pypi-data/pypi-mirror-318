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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp

class AssetFilterTimestamp(BaseModel):
    """
    if you want a range between you can use from && to.  if you want anything before, use to and NO from.  if you want anything after, use from and NO to.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    var_from: Optional[GroupedTimestamp] = Field(default=None, alias="from")
    to: Optional[GroupedTimestamp] = None
    between: Optional[StrictBool] = None
    __properties = ["schema", "from", "to", "between"]

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
    def from_json(cls, json_str: str) -> AssetFilterTimestamp:
        """Create an instance of AssetFilterTimestamp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict['to'] = self.to.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetFilterTimestamp:
        """Create an instance of AssetFilterTimestamp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetFilterTimestamp.parse_obj(obj)

        _obj = AssetFilterTimestamp.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "var_from": GroupedTimestamp.from_dict(obj.get("from")) if obj.get("from") is not None else None,
            "to": GroupedTimestamp.from_dict(obj.get("to")) if obj.get("to") is not None else None,
            "between": obj.get("between")
        })
        return _obj


