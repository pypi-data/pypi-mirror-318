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
from pydantic import BaseModel, Field, StrictInt
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class Score(BaseModel):
    """
    This is use as the score for an asset.  Manual: will be the raw sum of the asset activity events ranks with mechanismEnum == manual Automatic: will be the raw sum of the asset activity events ranks with mechanismEnum == automatic  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    manual: StrictInt = Field(default=..., description="These are points assigned via manual user driven events.")
    automatic: StrictInt = Field(default=..., description="These are point assigned via automatic activity events.")
    priority: Optional[StrictInt] = None
    reuse: Optional[StrictInt] = None
    update: Optional[StrictInt] = None
    reference: Optional[StrictInt] = None
    searched: Optional[StrictInt] = None
    __properties = ["schema", "manual", "automatic", "priority", "reuse", "update", "reference", "searched"]

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
    def from_json(cls, json_str: str) -> Score:
        """Create an instance of Score from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Score:
        """Create an instance of Score from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Score.parse_obj(obj)

        _obj = Score.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "manual": obj.get("manual"),
            "automatic": obj.get("automatic"),
            "priority": obj.get("priority"),
            "reuse": obj.get("reuse"),
            "update": obj.get("update"),
            "reference": obj.get("reference"),
            "searched": obj.get("searched")
        })
        return _obj


