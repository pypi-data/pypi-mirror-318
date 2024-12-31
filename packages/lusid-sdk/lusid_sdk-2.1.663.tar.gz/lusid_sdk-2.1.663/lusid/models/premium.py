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
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class Premium(BaseModel):
    """
    A class containing information for a given premium payment.  # noqa: E501
    """
    amount: Union[StrictFloat, StrictInt] = Field(..., description="Premium amount.")
    currency: StrictStr = Field(..., description="Premium currency.")
    var_date: datetime = Field(..., alias="date", description="Date when premium paid.")
    __properties = ["amount", "currency", "date"]

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
    def from_json(cls, json_str: str) -> Premium:
        """Create an instance of Premium from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Premium:
        """Create an instance of Premium from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Premium.parse_obj(obj)

        _obj = Premium.parse_obj({
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "var_date": obj.get("date")
        })
        return _obj
