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
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from lusid.models.currency_and_amount import CurrencyAndAmount
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId

class BlockedOrderRequest(BaseModel):
    """
    BlockedOrderRequest
    """
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Client-defined properties associated with this order.")
    quantity: Union[StrictFloat, StrictInt] = Field(..., description="The quantity of given instrument ordered.")
    order_book_id: Optional[ResourceId] = Field(None, alias="orderBookId")
    portfolio_id: Optional[ResourceId] = Field(None, alias="portfolioId")
    id: ResourceId = Field(...)
    state: Optional[StrictStr] = Field(None, description="The order's state (examples: New, PartiallyFilled, ...)")
    var_date: Optional[datetime] = Field(None, alias="date", description="The date on which the order was made")
    price: Optional[CurrencyAndAmount] = None
    order_instruction: Optional[ResourceId] = Field(None, alias="orderInstruction")
    package: Optional[ResourceId] = None
    __properties = ["properties", "quantity", "orderBookId", "portfolioId", "id", "state", "date", "price", "orderInstruction", "package"]

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
    def from_json(cls, json_str: str) -> BlockedOrderRequest:
        """Create an instance of BlockedOrderRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order_book_id
        if self.order_book_id:
            _dict['orderBookId'] = self.order_book_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of portfolio_id
        if self.portfolio_id:
            _dict['portfolioId'] = self.portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_instruction
        if self.order_instruction:
            _dict['orderInstruction'] = self.order_instruction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package
        if self.package:
            _dict['package'] = self.package.to_dict()
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlockedOrderRequest:
        """Create an instance of BlockedOrderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BlockedOrderRequest.parse_obj(obj)

        _obj = BlockedOrderRequest.parse_obj({
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "quantity": obj.get("quantity"),
            "order_book_id": ResourceId.from_dict(obj.get("orderBookId")) if obj.get("orderBookId") is not None else None,
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "state": obj.get("state"),
            "var_date": obj.get("date"),
            "price": CurrencyAndAmount.from_dict(obj.get("price")) if obj.get("price") is not None else None,
            "order_instruction": ResourceId.from_dict(obj.get("orderInstruction")) if obj.get("orderInstruction") is not None else None,
            "package": ResourceId.from_dict(obj.get("package")) if obj.get("package") is not None else None
        })
        return _obj
