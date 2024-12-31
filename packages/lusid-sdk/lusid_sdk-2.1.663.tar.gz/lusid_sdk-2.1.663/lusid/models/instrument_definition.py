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
from pydantic.v1 import BaseModel, Field, conlist, constr
from lusid.models.instrument_id_value import InstrumentIdValue
from lusid.models.lusid_instrument import LusidInstrument
from lusid.models.model_property import ModelProperty
from lusid.models.resource_id import ResourceId
from lusid.models.settlement_cycle import SettlementCycle

class InstrumentDefinition(BaseModel):
    """
    InstrumentDefinition
    """
    name: constr(strict=True, min_length=1) = Field(..., description="The name of the instrument.")
    identifiers: Dict[str, InstrumentIdValue] = Field(..., description="A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier.")
    properties: Optional[conlist(ModelProperty)] = Field(None, description="Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.")
    look_through_portfolio_id: Optional[ResourceId] = Field(None, alias="lookThroughPortfolioId")
    definition: Optional[LusidInstrument] = None
    settlement_cycle: Optional[SettlementCycle] = Field(None, alias="settlementCycle")
    __properties = ["name", "identifiers", "properties", "lookThroughPortfolioId", "definition", "settlementCycle"]

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
    def from_json(cls, json_str: str) -> InstrumentDefinition:
        """Create an instance of InstrumentDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in identifiers (dict)
        _field_dict = {}
        if self.identifiers:
            for _key in self.identifiers:
                if self.identifiers[_key]:
                    _field_dict[_key] = self.identifiers[_key].to_dict()
            _dict['identifiers'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of look_through_portfolio_id
        if self.look_through_portfolio_id:
            _dict['lookThroughPortfolioId'] = self.look_through_portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settlement_cycle
        if self.settlement_cycle:
            _dict['settlementCycle'] = self.settlement_cycle.to_dict()
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstrumentDefinition:
        """Create an instance of InstrumentDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstrumentDefinition.parse_obj(obj)

        _obj = InstrumentDefinition.parse_obj({
            "name": obj.get("name"),
            "identifiers": dict(
                (_k, InstrumentIdValue.from_dict(_v))
                for _k, _v in obj.get("identifiers").items()
            )
            if obj.get("identifiers") is not None
            else None,
            "properties": [ModelProperty.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None,
            "look_through_portfolio_id": ResourceId.from_dict(obj.get("lookThroughPortfolioId")) if obj.get("lookThroughPortfolioId") is not None else None,
            "definition": LusidInstrument.from_dict(obj.get("definition")) if obj.get("definition") is not None else None,
            "settlement_cycle": SettlementCycle.from_dict(obj.get("settlementCycle")) if obj.get("settlementCycle") is not None else None
        })
        return _obj
