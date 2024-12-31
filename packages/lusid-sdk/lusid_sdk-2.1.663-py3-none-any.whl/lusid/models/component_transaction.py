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
from pydantic.v1 import BaseModel, Field, StrictBool, conlist, constr
from lusid.models.transaction_field_map import TransactionFieldMap
from lusid.models.transaction_property_map import TransactionPropertyMap

class ComponentTransaction(BaseModel):
    """
    ComponentTransaction
    """
    display_name: constr(strict=True, max_length=100, min_length=0) = Field(..., alias="displayName")
    condition: Optional[constr(strict=True, max_length=1024, min_length=0)] = None
    transaction_field_map: TransactionFieldMap = Field(..., alias="transactionFieldMap")
    transaction_property_map: conlist(TransactionPropertyMap) = Field(..., alias="transactionPropertyMap")
    preserve_tax_lot_structure: Optional[StrictBool] = Field(None, alias="preserveTaxLotStructure", description="Controls if tax lot structure should be preserved when cost base is transferred to a new holding. For example in Spin Off instrument events.")
    __properties = ["displayName", "condition", "transactionFieldMap", "transactionPropertyMap", "preserveTaxLotStructure"]

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
    def from_json(cls, json_str: str) -> ComponentTransaction:
        """Create an instance of ComponentTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction_field_map
        if self.transaction_field_map:
            _dict['transactionFieldMap'] = self.transaction_field_map.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in transaction_property_map (list)
        _items = []
        if self.transaction_property_map:
            for _item in self.transaction_property_map:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactionPropertyMap'] = _items
        # set to None if condition (nullable) is None
        # and __fields_set__ contains the field
        if self.condition is None and "condition" in self.__fields_set__:
            _dict['condition'] = None

        # set to None if preserve_tax_lot_structure (nullable) is None
        # and __fields_set__ contains the field
        if self.preserve_tax_lot_structure is None and "preserve_tax_lot_structure" in self.__fields_set__:
            _dict['preserveTaxLotStructure'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComponentTransaction:
        """Create an instance of ComponentTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComponentTransaction.parse_obj(obj)

        _obj = ComponentTransaction.parse_obj({
            "display_name": obj.get("displayName"),
            "condition": obj.get("condition"),
            "transaction_field_map": TransactionFieldMap.from_dict(obj.get("transactionFieldMap")) if obj.get("transactionFieldMap") is not None else None,
            "transaction_property_map": [TransactionPropertyMap.from_dict(_item) for _item in obj.get("transactionPropertyMap")] if obj.get("transactionPropertyMap") is not None else None,
            "preserve_tax_lot_structure": obj.get("preserveTaxLotStructure")
        })
        return _obj
