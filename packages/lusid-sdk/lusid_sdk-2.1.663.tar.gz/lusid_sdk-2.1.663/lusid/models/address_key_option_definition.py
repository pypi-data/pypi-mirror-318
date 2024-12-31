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
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr

class AddressKeyOptionDefinition(BaseModel):
    """
    The definition of an Address Key Option  # noqa: E501
    """
    name: constr(strict=True, min_length=1) = Field(..., description="The name of the option")
    type: constr(strict=True, min_length=1) = Field(..., description="The type of the option")
    description: constr(strict=True, min_length=1) = Field(..., description="The description of the option")
    optional: StrictBool = Field(..., description="Is this option required or optional?")
    allowed_value_set: Optional[conlist(StrictStr)] = Field(None, alias="allowedValueSet", description="If the option is a string or enum, the allowed set of values it can take.")
    default_value: Optional[StrictStr] = Field(None, alias="defaultValue", description="If the option is not required, what is the default value?")
    __properties = ["name", "type", "description", "optional", "allowedValueSet", "defaultValue"]

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
    def from_json(cls, json_str: str) -> AddressKeyOptionDefinition:
        """Create an instance of AddressKeyOptionDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if allowed_value_set (nullable) is None
        # and __fields_set__ contains the field
        if self.allowed_value_set is None and "allowed_value_set" in self.__fields_set__:
            _dict['allowedValueSet'] = None

        # set to None if default_value (nullable) is None
        # and __fields_set__ contains the field
        if self.default_value is None and "default_value" in self.__fields_set__:
            _dict['defaultValue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddressKeyOptionDefinition:
        """Create an instance of AddressKeyOptionDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressKeyOptionDefinition.parse_obj(obj)

        _obj = AddressKeyOptionDefinition.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "description": obj.get("description"),
            "optional": obj.get("optional"),
            "allowed_value_set": obj.get("allowedValueSet"),
            "default_value": obj.get("defaultValue")
        })
        return _obj
