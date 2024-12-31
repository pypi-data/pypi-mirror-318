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


from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr, validator
from lusid.models.compliance_template_variation_request import ComplianceTemplateVariationRequest

class UpdateComplianceTemplateRequest(BaseModel):
    """
    UpdateComplianceTemplateRequest
    """
    code: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The code given for the Compliance Template")
    description: constr(strict=True, max_length=1024, min_length=0) = Field(..., description="The description of the Compliance Template")
    variations: conlist(ComplianceTemplateVariationRequest) = Field(..., description="Variation details of a Compliance Template")
    __properties = ["code", "description", "variations"]

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
    def from_json(cls, json_str: str) -> UpdateComplianceTemplateRequest:
        """Create an instance of UpdateComplianceTemplateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in variations (list)
        _items = []
        if self.variations:
            for _item in self.variations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateComplianceTemplateRequest:
        """Create an instance of UpdateComplianceTemplateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateComplianceTemplateRequest.parse_obj(obj)

        _obj = UpdateComplianceTemplateRequest.parse_obj({
            "code": obj.get("code"),
            "description": obj.get("description"),
            "variations": [ComplianceTemplateVariationRequest.from_dict(_item) for _item in obj.get("variations")] if obj.get("variations") is not None else None
        })
        return _obj
