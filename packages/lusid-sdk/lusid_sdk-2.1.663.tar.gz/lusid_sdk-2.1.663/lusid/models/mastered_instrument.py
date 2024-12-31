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


from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, validator
from lusid.models.lusid_instrument import LusidInstrument

class MasteredInstrument(LusidInstrument):
    """
    LUSID representation of a reference to another instrument that has already been upserted (Mastered)  # noqa: E501
    """
    identifiers: Dict[str, StrictStr] = Field(..., description="Dictionary of identifiers of the mastered instrument")
    mastered_dom_ccy: Optional[StrictStr] = Field(None, alias="masteredDomCcy", description="DomCcy of the Instrument that Mastered Instrument points to - read only field")
    mastered_instrument_type: Optional[StrictStr] = Field(None, alias="masteredInstrumentType", description="Type of the Instrument that Mastered Instrument points to - read only field")
    mastered_lusid_instrument_id: Optional[StrictStr] = Field(None, alias="masteredLusidInstrumentId", description="Luid of the Instrument that Mastered Instrument points to - read only field")
    mastered_name: Optional[StrictStr] = Field(None, alias="masteredName", description="Name of the Instrument that Mastered Instrument points to - read only field")
    mastered_scope: Optional[StrictStr] = Field(None, alias="masteredScope", description="Scope of the Instrument that Mastered Instrument points to - read only field")
    mastered_asset_class: Optional[StrictStr] = Field(None, alias="masteredAssetClass", description="Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "identifiers", "masteredDomCcy", "masteredInstrumentType", "masteredLusidInstrumentId", "masteredName", "masteredScope", "masteredAssetClass"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash', 'MasteredInstrument', 'LoanFacility', 'FlexibleDeposit'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash', 'MasteredInstrument', 'LoanFacility', 'FlexibleDeposit')")
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
    def from_json(cls, json_str: str) -> MasteredInstrument:
        """Create an instance of MasteredInstrument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "mastered_dom_ccy",
                            "mastered_instrument_type",
                            "mastered_lusid_instrument_id",
                            "mastered_name",
                            "mastered_scope",
                            "mastered_asset_class",
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if mastered_dom_ccy (nullable) is None
        # and __fields_set__ contains the field
        if self.mastered_dom_ccy is None and "mastered_dom_ccy" in self.__fields_set__:
            _dict['masteredDomCcy'] = None

        # set to None if mastered_instrument_type (nullable) is None
        # and __fields_set__ contains the field
        if self.mastered_instrument_type is None and "mastered_instrument_type" in self.__fields_set__:
            _dict['masteredInstrumentType'] = None

        # set to None if mastered_lusid_instrument_id (nullable) is None
        # and __fields_set__ contains the field
        if self.mastered_lusid_instrument_id is None and "mastered_lusid_instrument_id" in self.__fields_set__:
            _dict['masteredLusidInstrumentId'] = None

        # set to None if mastered_name (nullable) is None
        # and __fields_set__ contains the field
        if self.mastered_name is None and "mastered_name" in self.__fields_set__:
            _dict['masteredName'] = None

        # set to None if mastered_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.mastered_scope is None and "mastered_scope" in self.__fields_set__:
            _dict['masteredScope'] = None

        # set to None if mastered_asset_class (nullable) is None
        # and __fields_set__ contains the field
        if self.mastered_asset_class is None and "mastered_asset_class" in self.__fields_set__:
            _dict['masteredAssetClass'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MasteredInstrument:
        """Create an instance of MasteredInstrument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MasteredInstrument.parse_obj(obj)

        _obj = MasteredInstrument.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "identifiers": obj.get("identifiers"),
            "mastered_dom_ccy": obj.get("masteredDomCcy"),
            "mastered_instrument_type": obj.get("masteredInstrumentType"),
            "mastered_lusid_instrument_id": obj.get("masteredLusidInstrumentId"),
            "mastered_name": obj.get("masteredName"),
            "mastered_scope": obj.get("masteredScope"),
            "mastered_asset_class": obj.get("masteredAssetClass")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
