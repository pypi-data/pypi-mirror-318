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
from pydantic.v1 import BaseModel, Field, conlist, constr
from lusid.models.market_data_key_rule import MarketDataKeyRule

class GroupOfMarketDataKeyRules(BaseModel):
    """
    Represents a collection of MarketDataKeyRules that should be resolved together when resolving market data.  That is, market data resolution will always attempt to resolve with all rules in the group  before deciding what market data to return.  # noqa: E501
    """
    market_data_key_rule_group_operation: constr(strict=True, min_length=1) = Field(..., alias="marketDataKeyRuleGroupOperation", description="The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used.  Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum]")
    market_rules: conlist(MarketDataKeyRule) = Field(..., alias="marketRules", description="The rules that should be grouped together in market data resolution.")
    __properties = ["marketDataKeyRuleGroupOperation", "marketRules"]

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
    def from_json(cls, json_str: str) -> GroupOfMarketDataKeyRules:
        """Create an instance of GroupOfMarketDataKeyRules from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in market_rules (list)
        _items = []
        if self.market_rules:
            for _item in self.market_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['marketRules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupOfMarketDataKeyRules:
        """Create an instance of GroupOfMarketDataKeyRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupOfMarketDataKeyRules.parse_obj(obj)

        _obj = GroupOfMarketDataKeyRules.parse_obj({
            "market_data_key_rule_group_operation": obj.get("marketDataKeyRuleGroupOperation"),
            "market_rules": [MarketDataKeyRule.from_dict(_item) for _item in obj.get("marketRules")] if obj.get("marketRules") is not None else None
        })
        return _obj
