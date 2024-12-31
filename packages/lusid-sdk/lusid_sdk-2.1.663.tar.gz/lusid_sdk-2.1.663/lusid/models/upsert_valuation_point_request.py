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
from pydantic.v1 import BaseModel, Field, constr, validator
from lusid.models.model_property import ModelProperty

class UpsertValuationPointRequest(BaseModel):
    """
    A definition for the period you wish to close  # noqa: E501
    """
    diary_entry_code: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="diaryEntryCode", description="Unique code for the Valuation Point.")
    name: Optional[constr(strict=True, max_length=512, min_length=1)] = Field(None, description="Identifiable Name assigned to the Valuation Point.")
    effective_at: datetime = Field(..., alias="effectiveAt", description="The effective time of the diary entry.")
    query_as_at: Optional[datetime] = Field(None, alias="queryAsAt", description="The query time of the diary entry. Defaults to latest.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties for the diary entry.")
    __properties = ["diaryEntryCode", "name", "effectiveAt", "queryAsAt", "properties"]

    @validator('diary_entry_code')
    def diary_entry_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('name')
    def name_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> UpsertValuationPointRequest:
        """Create an instance of UpsertValuationPointRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if query_as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.query_as_at is None and "query_as_at" in self.__fields_set__:
            _dict['queryAsAt'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertValuationPointRequest:
        """Create an instance of UpsertValuationPointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertValuationPointRequest.parse_obj(obj)

        _obj = UpsertValuationPointRequest.parse_obj({
            "diary_entry_code": obj.get("diaryEntryCode"),
            "name": obj.get("name"),
            "effective_at": obj.get("effectiveAt"),
            "query_as_at": obj.get("queryAsAt"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None
        })
        return _obj
