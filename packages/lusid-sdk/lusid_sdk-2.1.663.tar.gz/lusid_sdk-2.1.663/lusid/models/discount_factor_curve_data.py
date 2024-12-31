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
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from lusid.models.complex_market_data import ComplexMarketData
from lusid.models.market_data_options import MarketDataOptions

class DiscountFactorCurveData(ComplexMarketData):
    """
    A curve containing discount factors and dates to which they apply  # noqa: E501
    """
    base_date: datetime = Field(..., alias="baseDate", description="BaseDate for the Curve")
    dates: conlist(datetime) = Field(..., description="Dates for which the discount factors apply")
    discount_factors: conlist(Union[StrictFloat, StrictInt]) = Field(..., alias="discountFactors", description="Discount factors to be applied to cashflow on the specified dates")
    lineage: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.")
    market_data_options: Optional[MarketDataOptions] = Field(None, alias="marketDataOptions")
    market_data_type: StrictStr = Field(..., alias="marketDataType", description="The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface")
    additional_properties: Dict[str, Any] = {}
    __properties = ["marketDataType", "baseDate", "dates", "discountFactors", "lineage", "marketDataOptions"]

    @validator('market_data_type')
    def market_data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DiscountFactorCurveData', 'EquityVolSurfaceData', 'FxVolSurfaceData', 'IrVolCubeData', 'OpaqueMarketData', 'YieldCurveData', 'FxForwardCurveData', 'FxForwardPipsCurveData', 'FxForwardTenorCurveData', 'FxForwardTenorPipsCurveData', 'FxForwardCurveByQuoteReference', 'CreditSpreadCurveData', 'EquityCurveByPricesData', 'ConstantVolatilitySurface'):
            raise ValueError("must be one of enum values ('DiscountFactorCurveData', 'EquityVolSurfaceData', 'FxVolSurfaceData', 'IrVolCubeData', 'OpaqueMarketData', 'YieldCurveData', 'FxForwardCurveData', 'FxForwardPipsCurveData', 'FxForwardTenorCurveData', 'FxForwardTenorPipsCurveData', 'FxForwardCurveByQuoteReference', 'CreditSpreadCurveData', 'EquityCurveByPricesData', 'ConstantVolatilitySurface')")
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
    def from_json(cls, json_str: str) -> DiscountFactorCurveData:
        """Create an instance of DiscountFactorCurveData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of market_data_options
        if self.market_data_options:
            _dict['marketDataOptions'] = self.market_data_options.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if lineage (nullable) is None
        # and __fields_set__ contains the field
        if self.lineage is None and "lineage" in self.__fields_set__:
            _dict['lineage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiscountFactorCurveData:
        """Create an instance of DiscountFactorCurveData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiscountFactorCurveData.parse_obj(obj)

        _obj = DiscountFactorCurveData.parse_obj({
            "market_data_type": obj.get("marketDataType"),
            "base_date": obj.get("baseDate"),
            "dates": obj.get("dates"),
            "discount_factors": obj.get("discountFactors"),
            "lineage": obj.get("lineage"),
            "market_data_options": MarketDataOptions.from_dict(obj.get("marketDataOptions")) if obj.get("marketDataOptions") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
