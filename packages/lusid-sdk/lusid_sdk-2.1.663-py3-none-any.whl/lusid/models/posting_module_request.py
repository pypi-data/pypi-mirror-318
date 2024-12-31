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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator
from lusid.models.posting_module_rule import PostingModuleRule

class PostingModuleRequest(BaseModel):
    """
    A Posting Module request definition  # noqa: E501
    """
    code: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The code of the Posting Module.")
    display_name: constr(strict=True, max_length=256, min_length=1) = Field(..., alias="displayName", description="The name of the Posting Module.")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="A description for the Posting Module.")
    rules: Optional[conlist(PostingModuleRule)] = Field(None, description="The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection.")
    __properties = ["code", "displayName", "description", "rules"]

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('display_name')
    def display_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[^\\<>&\"]+$", value):
            raise ValueError(r"must validate the regular expression /^[^\\<>&\"]+$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

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
    def from_json(cls, json_str: str) -> PostingModuleRequest:
        """Create an instance of PostingModuleRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if rules (nullable) is None
        # and __fields_set__ contains the field
        if self.rules is None and "rules" in self.__fields_set__:
            _dict['rules'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostingModuleRequest:
        """Create an instance of PostingModuleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostingModuleRequest.parse_obj(obj)

        _obj = PostingModuleRequest.parse_obj({
            "code": obj.get("code"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "rules": [PostingModuleRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj
