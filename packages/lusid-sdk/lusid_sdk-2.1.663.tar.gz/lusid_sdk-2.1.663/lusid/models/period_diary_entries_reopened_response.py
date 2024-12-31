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
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from lusid.models.link import Link

class PeriodDiaryEntriesReopenedResponse(BaseModel):
    """
    PeriodDiaryEntriesReopenedResponse
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    effective_from: Optional[datetime] = Field(None, alias="effectiveFrom", description="The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable.")
    as_at: datetime = Field(..., alias="asAt", description="The asAt datetime at which the deletion was committed to LUSID.")
    period_diary_entries_removed: StrictInt = Field(..., alias="periodDiaryEntriesRemoved", description="Number of Diary Entries removed as a result of reopening periods")
    period_diary_entries_from: datetime = Field(..., alias="periodDiaryEntriesFrom", description="The start point where periods were removed from")
    period_diary_entries_to: datetime = Field(..., alias="periodDiaryEntriesTo", description="The end point where periods were removed to")
    links: Optional[conlist(Link)] = None
    __properties = ["href", "effectiveFrom", "asAt", "periodDiaryEntriesRemoved", "periodDiaryEntriesFrom", "periodDiaryEntriesTo", "links"]

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
    def from_json(cls, json_str: str) -> PeriodDiaryEntriesReopenedResponse:
        """Create an instance of PeriodDiaryEntriesReopenedResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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

        # set to None if effective_from (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_from is None and "effective_from" in self.__fields_set__:
            _dict['effectiveFrom'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PeriodDiaryEntriesReopenedResponse:
        """Create an instance of PeriodDiaryEntriesReopenedResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeriodDiaryEntriesReopenedResponse.parse_obj(obj)

        _obj = PeriodDiaryEntriesReopenedResponse.parse_obj({
            "href": obj.get("href"),
            "effective_from": obj.get("effectiveFrom"),
            "as_at": obj.get("asAt"),
            "period_diary_entries_removed": obj.get("periodDiaryEntriesRemoved"),
            "period_diary_entries_from": obj.get("periodDiaryEntriesFrom"),
            "period_diary_entries_to": obj.get("periodDiaryEntriesTo"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
