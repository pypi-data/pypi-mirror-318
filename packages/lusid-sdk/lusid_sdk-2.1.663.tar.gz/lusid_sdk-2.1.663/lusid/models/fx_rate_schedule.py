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


from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from lusid.models.flow_conventions import FlowConventions
from lusid.models.schedule import Schedule

class FxRateSchedule(Schedule):
    """
    Schedule to define fx conversion of cashflows on complex bonds. If an fx schedule is defined then  on payment schedule generation the coupon and principal payoffs will be wrapped in an fx rate payoff method.  Either the fx rate is predefined (fixed) or relies on fx resets (floating).  Used in representation of dual currency bond.  # noqa: E501
    """
    flow_conventions: Optional[FlowConventions] = Field(None, alias="flowConventions")
    fx_conversion_types: Optional[conlist(StrictStr)] = Field(None, alias="fxConversionTypes", description="List of flags to indicate if coupon payments, principal payments or both are converted")
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate")
    to_currency: Optional[StrictStr] = Field(None, alias="toCurrency", description="Currency that payments are converted to")
    schedule_type: StrictStr = Field(..., alias="scheduleType", description="The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid")
    additional_properties: Dict[str, Any] = {}
    __properties = ["scheduleType", "flowConventions", "fxConversionTypes", "rate", "toCurrency"]

    @validator('schedule_type')
    def schedule_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FixedSchedule', 'FloatSchedule', 'OptionalitySchedule', 'StepSchedule', 'Exercise', 'FxRateSchedule', 'FxLinkedNotionalSchedule', 'BondConversionSchedule', 'Invalid'):
            raise ValueError("must be one of enum values ('FixedSchedule', 'FloatSchedule', 'OptionalitySchedule', 'StepSchedule', 'Exercise', 'FxRateSchedule', 'FxLinkedNotionalSchedule', 'BondConversionSchedule', 'Invalid')")
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
    def from_json(cls, json_str: str) -> FxRateSchedule:
        """Create an instance of FxRateSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_conventions
        if self.flow_conventions:
            _dict['flowConventions'] = self.flow_conventions.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if fx_conversion_types (nullable) is None
        # and __fields_set__ contains the field
        if self.fx_conversion_types is None and "fx_conversion_types" in self.__fields_set__:
            _dict['fxConversionTypes'] = None

        # set to None if to_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.to_currency is None and "to_currency" in self.__fields_set__:
            _dict['toCurrency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FxRateSchedule:
        """Create an instance of FxRateSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxRateSchedule.parse_obj(obj)

        _obj = FxRateSchedule.parse_obj({
            "schedule_type": obj.get("scheduleType"),
            "flow_conventions": FlowConventions.from_dict(obj.get("flowConventions")) if obj.get("flowConventions") is not None else None,
            "fx_conversion_types": obj.get("fxConversionTypes"),
            "rate": obj.get("rate"),
            "to_currency": obj.get("toCurrency")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
