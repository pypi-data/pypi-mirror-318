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
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, constr, validator
from lusid.models.lusid_instrument import LusidInstrument

class ContractForDifference(LusidInstrument):
    """
    LUSID representation of a Contract for Difference.  # noqa: E501
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the CFD.")
    maturity_date: Optional[datetime] = Field(None, alias="maturityDate", description="The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set.")
    code: constr(strict=True, min_length=1) = Field(..., description="The code of the underlying.")
    contract_size: Union[StrictFloat, StrictInt] = Field(..., alias="contractSize", description="The size of the CFD contract, this should represent the total number of stocks that the CFD represents.")
    pay_ccy: StrictStr = Field(..., alias="payCcy", description="The currency that this CFD pays out, this can be different to the UnderlyingCcy.")
    reference_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="referenceRate", description="The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0.")
    type: constr(strict=True, min_length=1) = Field(..., description="The type of CFD.    Supported string (enumeration) values are: [Cash, Futures].")
    underlying_ccy: StrictStr = Field(..., alias="underlyingCcy", description="The currency of the underlying")
    underlying_identifier: constr(strict=True, min_length=1) = Field(..., alias="underlyingIdentifier", description="External market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].")
    lot_size: Optional[StrictInt] = Field(None, alias="lotSize", description="CFD LotSize, the minimum number of shares that can be bought or sold at once.  Optional, if set must be non-negative, if not set defaults to 1.")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "code", "contractSize", "payCcy", "referenceRate", "type", "underlyingCcy", "underlyingIdentifier", "lotSize"]

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
    def from_json(cls, json_str: str) -> ContractForDifference:
        """Create an instance of ContractForDifference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContractForDifference:
        """Create an instance of ContractForDifference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContractForDifference.parse_obj(obj)

        _obj = ContractForDifference.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "code": obj.get("code"),
            "contract_size": obj.get("contractSize"),
            "pay_ccy": obj.get("payCcy"),
            "reference_rate": obj.get("referenceRate"),
            "type": obj.get("type"),
            "underlying_ccy": obj.get("underlyingCcy"),
            "underlying_identifier": obj.get("underlyingIdentifier"),
            "lot_size": obj.get("lotSize")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
