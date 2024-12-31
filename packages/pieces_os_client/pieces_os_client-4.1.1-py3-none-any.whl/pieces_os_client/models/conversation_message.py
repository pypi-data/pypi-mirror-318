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
from pydantic import BaseModel, Field, StrictStr
from pieces_os_client.models.conversation_message_sentiment_enum import ConversationMessageSentimentEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_anchors import FlattenedAnchors
from pieces_os_client.models.flattened_annotations import FlattenedAnnotations
from pieces_os_client.models.flattened_persons import FlattenedPersons
from pieces_os_client.models.flattened_websites import FlattenedWebsites
from pieces_os_client.models.fragment_format import FragmentFormat
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.model import Model
from pieces_os_client.models.qgpt_conversation_message_role_enum import QGPTConversationMessageRoleEnum
from pieces_os_client.models.referenced_conversation import ReferencedConversation
from pieces_os_client.models.score import Score

class ConversationMessage(BaseModel):
    """
    This is a fully referenced ConversationMessage.  This has the minimum amount of properties to keep this light weight  (will consider additional properties in the future like people/tags/links xyz)  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(...)
    created: GroupedTimestamp = Field(...)
    updated: GroupedTimestamp = Field(...)
    deleted: Optional[GroupedTimestamp] = None
    model: Optional[Model] = None
    fragment: Optional[FragmentFormat] = None
    conversation: ReferencedConversation = Field(...)
    sentiment: Optional[ConversationMessageSentimentEnum] = None
    role: QGPTConversationMessageRoleEnum = Field(...)
    score: Optional[Score] = None
    annotations: Optional[FlattenedAnnotations] = None
    websites: Optional[FlattenedWebsites] = None
    persons: Optional[FlattenedPersons] = None
    anchors: Optional[FlattenedAnchors] = None
    __properties = ["schema", "id", "created", "updated", "deleted", "model", "fragment", "conversation", "sentiment", "role", "score", "annotations", "websites", "persons", "anchors"]

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
    def from_json(cls, json_str: str) -> ConversationMessage:
        """Create an instance of ConversationMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fragment
        if self.fragment:
            _dict['fragment'] = self.fragment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConversationMessage:
        """Create an instance of ConversationMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConversationMessage.parse_obj(obj)

        _obj = ConversationMessage.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj.get("deleted")) if obj.get("deleted") is not None else None,
            "model": Model.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "fragment": FragmentFormat.from_dict(obj.get("fragment")) if obj.get("fragment") is not None else None,
            "conversation": ReferencedConversation.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None,
            "sentiment": obj.get("sentiment"),
            "role": obj.get("role"),
            "score": Score.from_dict(obj.get("score")) if obj.get("score") is not None else None,
            "annotations": FlattenedAnnotations.from_dict(obj.get("annotations")) if obj.get("annotations") is not None else None,
            "websites": FlattenedWebsites.from_dict(obj.get("websites")) if obj.get("websites") is not None else None,
            "persons": FlattenedPersons.from_dict(obj.get("persons")) if obj.get("persons") is not None else None,
            "anchors": FlattenedAnchors.from_dict(obj.get("anchors")) if obj.get("anchors") is not None else None
        })
        return _obj


