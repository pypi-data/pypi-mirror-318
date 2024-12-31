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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.recipients import Recipients

class SeededGitHubGistDistribution(BaseModel):
    """
    This is the minimum information needed to distribute a Piece to a Gist.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    recipients: Optional[Recipients] = None
    public: Optional[StrictBool] = Field(default=None, description="we will default to true")
    description: Optional[StrictStr] = Field(default=None, description="This is the description of the Gist Distribution")
    name: StrictStr = Field(default=..., description="This is the name of the gist you will add.")
    __properties = ["schema", "recipients", "public", "description", "name"]

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
    def from_json(cls, json_str: str) -> SeededGitHubGistDistribution:
        """Create an instance of SeededGitHubGistDistribution from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recipients
        if self.recipients:
            _dict['recipients'] = self.recipients.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededGitHubGistDistribution:
        """Create an instance of SeededGitHubGistDistribution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededGitHubGistDistribution.parse_obj(obj)

        _obj = SeededGitHubGistDistribution.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "recipients": Recipients.from_dict(obj.get("recipients")) if obj.get("recipients") is not None else None,
            "public": obj.get("public"),
            "description": obj.get("description"),
            "name": obj.get("name")
        })
        return _obj


