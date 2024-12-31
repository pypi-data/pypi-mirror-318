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
from pieces_os_client.models.classification import Classification
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.language_server_protocol_location import LanguageServerProtocolLocation
from pieces_os_client.models.transferable_string import TransferableString

class IDESelection(BaseModel):
    """
    This is a given bit of text/code that is selected in the IDE, this can be a copy/paste/selection  location: this is the given location provided by the LSP(might need to be a different object we will see)  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    location: Optional[LanguageServerProtocolLocation] = None
    classification: Optional[Classification] = None
    value: Optional[TransferableString] = None
    __properties = ["schema", "location", "classification", "value"]

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
    def from_json(cls, json_str: str) -> IDESelection:
        """Create an instance of IDESelection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IDESelection:
        """Create an instance of IDESelection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IDESelection.parse_obj(obj)

        _obj = IDESelection.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "location": LanguageServerProtocolLocation.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "classification": Classification.from_dict(obj.get("classification")) if obj.get("classification") is not None else None,
            "value": TransferableString.from_dict(obj.get("value")) if obj.get("value") is not None else None
        })
        return _obj


