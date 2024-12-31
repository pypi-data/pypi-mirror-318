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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from lusid.models.compliance_template_variation import ComplianceTemplateVariation
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId

class ComplianceTemplate(BaseModel):
    """
    ComplianceTemplate
    """
    id: ResourceId = Field(...)
    description: constr(strict=True, min_length=1) = Field(..., description="The description of the Compliance Template")
    tags: Optional[conlist(StrictStr)] = Field(None, description="Tags for a Compliance Template")
    variations: conlist(ComplianceTemplateVariation) = Field(..., description="Variation details of a Compliance Template")
    links: Optional[conlist(Link)] = None
    __properties = ["id", "description", "tags", "variations", "links"]

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
    def from_json(cls, json_str: str) -> ComplianceTemplate:
        """Create an instance of ComplianceTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in variations (list)
        _items = []
        if self.variations:
            for _item in self.variations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceTemplate:
        """Create an instance of ComplianceTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceTemplate.parse_obj(obj)

        _obj = ComplianceTemplate.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "description": obj.get("description"),
            "tags": obj.get("tags"),
            "variations": [ComplianceTemplateVariation.from_dict(_item) for _item in obj.get("variations")] if obj.get("variations") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
