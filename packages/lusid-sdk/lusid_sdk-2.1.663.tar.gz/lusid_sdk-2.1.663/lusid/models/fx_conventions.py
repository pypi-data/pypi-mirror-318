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


from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, constr

class FxConventions(BaseModel):
    """
    The conventions for the calculation of FX fixings, where the fixing rate is expected to be the amount of  DomCcy per unit of FgnCcy.  As an example, assume the required fixing is the WM/R 4pm mid closing rate for the USD amount per 1 EUR.  This is published with RIC EURUSDFIXM=WM, which would be the FixingReference, with FgnCcy EUR and DomCcy USD.  # noqa: E501
    """
    fgn_ccy: StrictStr = Field(..., alias="fgnCcy", description="The foreign currency")
    dom_ccy: StrictStr = Field(..., alias="domCcy", description="The domestic currency")
    fixing_reference: constr(strict=True, max_length=64, min_length=0) = Field(..., alias="fixingReference", description="The reference name used to find the desired quote")
    __properties = ["fgnCcy", "domCcy", "fixingReference"]

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
    def from_json(cls, json_str: str) -> FxConventions:
        """Create an instance of FxConventions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FxConventions:
        """Create an instance of FxConventions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxConventions.parse_obj(obj)

        _obj = FxConventions.parse_obj({
            "fgn_ccy": obj.get("fgnCcy"),
            "dom_ccy": obj.get("domCcy"),
            "fixing_reference": obj.get("fixingReference")
        })
        return _obj
