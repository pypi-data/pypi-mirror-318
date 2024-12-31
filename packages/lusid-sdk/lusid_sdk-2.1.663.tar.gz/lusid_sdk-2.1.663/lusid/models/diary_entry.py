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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class DiaryEntry(BaseModel):
    """
    DiaryEntry
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    abor_id: Optional[ResourceId] = Field(None, alias="aborId")
    diary_entry_code: Optional[StrictStr] = Field(None, alias="diaryEntryCode", description="The code of the diary entry.")
    type: constr(strict=True, min_length=1) = Field(..., description="The type of the diary entry.")
    name: Optional[constr(strict=True, max_length=256, min_length=1)] = Field(None, description="The name of the diary entry.")
    status: constr(strict=True, min_length=1) = Field(..., description="The status of the diary entry. Statuses are constrained and defaulted by 'Type' specified.   Type 'Other' defaults to 'Undefined' and supports 'Undefined', 'Estimate', 'Candidate', and 'Final'.  Type 'PeriodBoundary' defaults to 'Estimate' when closing a period, and supports 'Estimate' and 'Final' for closing periods and 'Final' for locking periods.  Type 'ValuationPoint' defaults to 'Estimate' when upserting a diary entry, moves to 'Candidate' or 'Final' when a ValuationPoint is accepted, and 'Final' when it is finalised.")
    effective_at: datetime = Field(..., alias="effectiveAt", description="The effective time of the diary entry.")
    query_as_at: Optional[datetime] = Field(None, alias="queryAsAt", description="The query time of the diary entry. Defaults to latest.")
    previous_entry_time: Optional[datetime] = Field(None, alias="previousEntryTime", description="The entry time of the previous diary entry.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties for the diary entry.")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["href", "aborId", "diaryEntryCode", "type", "name", "status", "effectiveAt", "queryAsAt", "previousEntryTime", "properties", "version", "links"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^\\<>&\"]+$", value):
            raise ValueError(r"must validate the regular expression /^[^\\<>&\"]+$/")
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
    def from_json(cls, json_str: str) -> DiaryEntry:
        """Create an instance of DiaryEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of abor_id
        if self.abor_id:
            _dict['aborId'] = self.abor_id.to_dict()
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
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if diary_entry_code (nullable) is None
        # and __fields_set__ contains the field
        if self.diary_entry_code is None and "diary_entry_code" in self.__fields_set__:
            _dict['diaryEntryCode'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiaryEntry:
        """Create an instance of DiaryEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiaryEntry.parse_obj(obj)

        _obj = DiaryEntry.parse_obj({
            "href": obj.get("href"),
            "abor_id": ResourceId.from_dict(obj.get("aborId")) if obj.get("aborId") is not None else None,
            "diary_entry_code": obj.get("diaryEntryCode"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "effective_at": obj.get("effectiveAt"),
            "query_as_at": obj.get("queryAsAt"),
            "previous_entry_time": obj.get("previousEntryTime"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
