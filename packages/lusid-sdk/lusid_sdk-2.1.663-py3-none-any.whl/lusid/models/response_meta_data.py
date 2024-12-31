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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

class ResponseMetaData(BaseModel):
    """
    Metadata related to an api response  # noqa: E501
    """
    type: Optional[StrictStr] = Field(None, description="The type of meta data information being provided")
    description: Optional[StrictStr] = Field(None, description="The description of what occured for this specific piece of meta data")
    identifier_type: Optional[StrictStr] = Field(None, alias="identifierType", description="The type of the listed identifiers")
    identifiers: Optional[conlist(StrictStr)] = Field(None, description="The related identifiers that were impacted by this event")
    __properties = ["type", "description", "identifierType", "identifiers"]

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
    def from_json(cls, json_str: str) -> ResponseMetaData:
        """Create an instance of ResponseMetaData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if identifier_type (nullable) is None
        # and __fields_set__ contains the field
        if self.identifier_type is None and "identifier_type" in self.__fields_set__:
            _dict['identifierType'] = None

        # set to None if identifiers (nullable) is None
        # and __fields_set__ contains the field
        if self.identifiers is None and "identifiers" in self.__fields_set__:
            _dict['identifiers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResponseMetaData:
        """Create an instance of ResponseMetaData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResponseMetaData.parse_obj(obj)

        _obj = ResponseMetaData.parse_obj({
            "type": obj.get("type"),
            "description": obj.get("description"),
            "identifier_type": obj.get("identifierType"),
            "identifiers": obj.get("identifiers")
        })
        return _obj
