# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

class GroupReconciliationUserReviewRemove(BaseModel):
    """
    GroupReconciliationUserReviewRemove
    """
    break_code_as_at_added: Optional[datetime] = Field(None, alias="breakCodeAsAtAdded", description="The timestamp of the added User Review input.")
    match_key_as_at_added: Optional[datetime] = Field(None, alias="matchKeyAsAtAdded", description="The timestamp of the added User Review input.")
    comment_text_as_at_added: Optional[datetime] = Field(None, alias="commentTextAsAtAdded", description="The timestamp of the added User Review input.")
    __properties = ["breakCodeAsAtAdded", "matchKeyAsAtAdded", "commentTextAsAtAdded"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GroupReconciliationUserReviewRemove:
        """Create an instance of GroupReconciliationUserReviewRemove from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if break_code_as_at_added (nullable) is None
        # and __fields_set__ contains the field
        if self.break_code_as_at_added is None and "break_code_as_at_added" in self.__fields_set__:
            _dict['breakCodeAsAtAdded'] = None

        # set to None if match_key_as_at_added (nullable) is None
        # and __fields_set__ contains the field
        if self.match_key_as_at_added is None and "match_key_as_at_added" in self.__fields_set__:
            _dict['matchKeyAsAtAdded'] = None

        # set to None if comment_text_as_at_added (nullable) is None
        # and __fields_set__ contains the field
        if self.comment_text_as_at_added is None and "comment_text_as_at_added" in self.__fields_set__:
            _dict['commentTextAsAtAdded'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupReconciliationUserReviewRemove:
        """Create an instance of GroupReconciliationUserReviewRemove from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupReconciliationUserReviewRemove.parse_obj(obj)

        _obj = GroupReconciliationUserReviewRemove.parse_obj({
            "break_code_as_at_added": obj.get("breakCodeAsAtAdded"),
            "match_key_as_at_added": obj.get("matchKeyAsAtAdded"),
            "comment_text_as_at_added": obj.get("commentTextAsAtAdded")
        })
        return _obj
