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
from lusid.models.aggregation_measure_failure_detail import AggregationMeasureFailureDetail
from lusid.models.link import Link
from lusid.models.result_data_schema import ResultDataSchema

class ListAggregationResponse(BaseModel):
    """
    ListAggregationResponse
    """
    aggregation_effective_at: Optional[datetime] = Field(None, alias="aggregationEffectiveAt")
    aggregation_as_at: Optional[datetime] = Field(None, alias="aggregationAsAt")
    href: Optional[StrictStr] = None
    data: Optional[conlist(Dict[str, Any])] = None
    aggregation_currency: Optional[StrictStr] = Field(None, alias="aggregationCurrency")
    data_schema: Optional[ResultDataSchema] = Field(None, alias="dataSchema")
    aggregation_failures: Optional[conlist(AggregationMeasureFailureDetail)] = Field(None, alias="aggregationFailures")
    links: Optional[conlist(Link)] = None
    __properties = ["aggregationEffectiveAt", "aggregationAsAt", "href", "data", "aggregationCurrency", "dataSchema", "aggregationFailures", "links"]

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
    def from_json(cls, json_str: str) -> ListAggregationResponse:
        """Create an instance of ListAggregationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data_schema
        if self.data_schema:
            _dict['dataSchema'] = self.data_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in aggregation_failures (list)
        _items = []
        if self.aggregation_failures:
            for _item in self.aggregation_failures:
                if _item:
                    _items.append(_item.to_dict())
            _dict['aggregationFailures'] = _items
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

        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        # set to None if aggregation_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.aggregation_currency is None and "aggregation_currency" in self.__fields_set__:
            _dict['aggregationCurrency'] = None

        # set to None if aggregation_failures (nullable) is None
        # and __fields_set__ contains the field
        if self.aggregation_failures is None and "aggregation_failures" in self.__fields_set__:
            _dict['aggregationFailures'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListAggregationResponse:
        """Create an instance of ListAggregationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListAggregationResponse.parse_obj(obj)

        _obj = ListAggregationResponse.parse_obj({
            "aggregation_effective_at": obj.get("aggregationEffectiveAt"),
            "aggregation_as_at": obj.get("aggregationAsAt"),
            "href": obj.get("href"),
            "data": obj.get("data"),
            "aggregation_currency": obj.get("aggregationCurrency"),
            "data_schema": ResultDataSchema.from_dict(obj.get("dataSchema")) if obj.get("dataSchema") is not None else None,
            "aggregation_failures": [AggregationMeasureFailureDetail.from_dict(_item) for _item in obj.get("aggregationFailures")] if obj.get("aggregationFailures") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
