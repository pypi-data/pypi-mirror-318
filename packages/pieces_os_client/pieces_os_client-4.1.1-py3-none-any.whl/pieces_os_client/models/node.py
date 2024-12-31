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



from pydantic import BaseModel, Field, StrictBool, StrictStr
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.node_type_enum import NodeTypeEnum

class Node(BaseModel):
    """
    This describes a node within a relationship graph used to related like types. ie asset to asset, tag to tag, ...etc  created: is here to let us know when the node was attached.  id: this is the the id of the type ie, if the type is Asset the id here points to the asset that this node represents.  # noqa: E501
    """
    id: StrictStr = Field(...)
    type: NodeTypeEnum = Field(...)
    root: StrictBool = Field(default=..., description="This is a boolean to let us know if this node is the root or origin of the relationship graph.")
    created: GroupedTimestamp = Field(...)
    __properties = ["id", "type", "root", "created"]

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
    def from_json(cls, json_str: str) -> Node:
        """Create an instance of Node from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Node:
        """Create an instance of Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Node.parse_obj(obj)

        _obj = Node.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "root": obj.get("root"),
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None
        })
        return _obj


