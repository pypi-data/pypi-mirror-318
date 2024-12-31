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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.version import Version

class ClosedPeriod(BaseModel):
    """
    ClosedPeriod
    """
    closed_period_id: Optional[StrictStr] = Field(None, alias="closedPeriodId", description="The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period")
    effective_start: Optional[datetime] = Field(None, alias="effectiveStart", description="The effective start of the Closed Period")
    effective_end: Optional[datetime] = Field(None, alias="effectiveEnd", description="The effective end of the Closed Period")
    as_at_closed: Optional[datetime] = Field(None, alias="asAtClosed", description="The asAt datetime the Closed Period was created")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="The Closed Periods properties. These will be from the 'ClosedPeriod' domain.")
    version: Optional[Version] = None
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime.")
    links: Optional[conlist(Link)] = None
    __properties = ["closedPeriodId", "effectiveStart", "effectiveEnd", "asAtClosed", "properties", "version", "href", "links"]

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
    def from_json(cls, json_str: str) -> ClosedPeriod:
        """Create an instance of ClosedPeriod from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if closed_period_id (nullable) is None
        # and __fields_set__ contains the field
        if self.closed_period_id is None and "closed_period_id" in self.__fields_set__:
            _dict['closedPeriodId'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClosedPeriod:
        """Create an instance of ClosedPeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClosedPeriod.parse_obj(obj)

        _obj = ClosedPeriod.parse_obj({
            "closed_period_id": obj.get("closedPeriodId"),
            "effective_start": obj.get("effectiveStart"),
            "effective_end": obj.get("effectiveEnd"),
            "as_at_closed": obj.get("asAtClosed"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "href": obj.get("href"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
