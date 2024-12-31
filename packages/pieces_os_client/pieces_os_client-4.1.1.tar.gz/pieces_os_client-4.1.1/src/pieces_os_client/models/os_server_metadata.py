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
from pydantic import BaseModel, Field
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.tracked_summary_totals import TrackedSummaryTotals

class OSServerMetadata(BaseModel):
    """
    This will return metadata (total materials) in your pieces drive.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    totals: Optional[TrackedSummaryTotals] = None
    __properties = ["schema", "totals"]

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
    def from_json(cls, json_str: str) -> OSServerMetadata:
        """Create an instance of OSServerMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of totals
        if self.totals:
            _dict['totals'] = self.totals.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OSServerMetadata:
        """Create an instance of OSServerMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OSServerMetadata.parse_obj(obj)

        _obj = OSServerMetadata.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "totals": TrackedSummaryTotals.from_dict(obj.get("totals")) if obj.get("totals") is not None else None
        })
        return _obj


