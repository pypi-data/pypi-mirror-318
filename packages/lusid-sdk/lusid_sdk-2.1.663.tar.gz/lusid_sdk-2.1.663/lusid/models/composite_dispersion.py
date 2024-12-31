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
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist
from lusid.models.resource_id import ResourceId

class CompositeDispersion(BaseModel):
    """
    A list of Dispersion calculations for the given years.  # noqa: E501
    """
    effective_at: datetime = Field(..., alias="effectiveAt", description="The date for which dipsersion calculation has been done. This should be 31 Dec for each given year.")
    dispersion_calculation: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="dispersionCalculation", description="The result for the dispersion calculation on the given effectiveAt.")
    variance: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The variance on the given effectiveAt.")
    first_quartile: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="firstQuartile", description="First Quartile (Q1) =  (lower quartile) = the middle of the bottom half of the returns.")
    third_quartile: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="thirdQuartile", description="Third Quartile (Q3) =  (higher quartile) = the middle of the top half of the returns.")
    range: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Highest return - Lowest return.")
    constituents_in_scope: Optional[conlist(ResourceId)] = Field(None, alias="constituentsInScope", description="List containing Composite members which are part of the dispersion calcualtion.")
    constituents_excluded: Optional[conlist(ResourceId)] = Field(None, alias="constituentsExcluded", description="List containing the Composite members which are not part of the dispersion calculation")
    __properties = ["effectiveAt", "dispersionCalculation", "variance", "firstQuartile", "thirdQuartile", "range", "constituentsInScope", "constituentsExcluded"]

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
    def from_json(cls, json_str: str) -> CompositeDispersion:
        """Create an instance of CompositeDispersion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in constituents_in_scope (list)
        _items = []
        if self.constituents_in_scope:
            for _item in self.constituents_in_scope:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constituentsInScope'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in constituents_excluded (list)
        _items = []
        if self.constituents_excluded:
            for _item in self.constituents_excluded:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constituentsExcluded'] = _items
        # set to None if dispersion_calculation (nullable) is None
        # and __fields_set__ contains the field
        if self.dispersion_calculation is None and "dispersion_calculation" in self.__fields_set__:
            _dict['dispersionCalculation'] = None

        # set to None if variance (nullable) is None
        # and __fields_set__ contains the field
        if self.variance is None and "variance" in self.__fields_set__:
            _dict['variance'] = None

        # set to None if first_quartile (nullable) is None
        # and __fields_set__ contains the field
        if self.first_quartile is None and "first_quartile" in self.__fields_set__:
            _dict['firstQuartile'] = None

        # set to None if third_quartile (nullable) is None
        # and __fields_set__ contains the field
        if self.third_quartile is None and "third_quartile" in self.__fields_set__:
            _dict['thirdQuartile'] = None

        # set to None if range (nullable) is None
        # and __fields_set__ contains the field
        if self.range is None and "range" in self.__fields_set__:
            _dict['range'] = None

        # set to None if constituents_in_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.constituents_in_scope is None and "constituents_in_scope" in self.__fields_set__:
            _dict['constituentsInScope'] = None

        # set to None if constituents_excluded (nullable) is None
        # and __fields_set__ contains the field
        if self.constituents_excluded is None and "constituents_excluded" in self.__fields_set__:
            _dict['constituentsExcluded'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompositeDispersion:
        """Create an instance of CompositeDispersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompositeDispersion.parse_obj(obj)

        _obj = CompositeDispersion.parse_obj({
            "effective_at": obj.get("effectiveAt"),
            "dispersion_calculation": obj.get("dispersionCalculation"),
            "variance": obj.get("variance"),
            "first_quartile": obj.get("firstQuartile"),
            "third_quartile": obj.get("thirdQuartile"),
            "range": obj.get("range"),
            "constituents_in_scope": [ResourceId.from_dict(_item) for _item in obj.get("constituentsInScope")] if obj.get("constituentsInScope") is not None else None,
            "constituents_excluded": [ResourceId.from_dict(_item) for _item in obj.get("constituentsExcluded")] if obj.get("constituentsExcluded") is not None else None
        })
        return _obj
