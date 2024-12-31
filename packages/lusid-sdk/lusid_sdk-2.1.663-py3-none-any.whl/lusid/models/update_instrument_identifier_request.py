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


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

class UpdateInstrumentIdentifierRequest(BaseModel):
    """
    UpdateInstrumentIdentifierRequest
    """
    type: constr(strict=True, min_length=1) = Field(..., description="The allowable instrument identifier to update, insert or remove e.g. 'Figi'.")
    value: Optional[StrictStr] = Field(None, description="The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument.")
    effective_at: Optional[StrictStr] = Field(None, alias="effectiveAt", description="The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified.")
    __properties = ["type", "value", "effectiveAt"]

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
    def from_json(cls, json_str: str) -> UpdateInstrumentIdentifierRequest:
        """Create an instance of UpdateInstrumentIdentifierRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        # set to None if effective_at (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_at is None and "effective_at" in self.__fields_set__:
            _dict['effectiveAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateInstrumentIdentifierRequest:
        """Create an instance of UpdateInstrumentIdentifierRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateInstrumentIdentifierRequest.parse_obj(obj)

        _obj = UpdateInstrumentIdentifierRequest.parse_obj({
            "type": obj.get("type"),
            "value": obj.get("value"),
            "effective_at": obj.get("effectiveAt")
        })
        return _obj
