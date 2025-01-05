from google.ads.searchads360.v0.enums import bidding_strategy_type_pb2 as _bidding_strategy_type_pb2
from google.ads.searchads360.v0.enums import target_impression_share_location_pb2 as _target_impression_share_location_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessibleBiddingStrategy(_message.Message):
    __slots__ = ("resource_name", "id", "name", "type", "owner_customer_id", "owner_descriptive_name", "maximize_conversion_value", "maximize_conversions", "target_cpa", "target_impression_share", "target_roas", "target_spend")
    class MaximizeConversionValue(_message.Message):
        __slots__ = ("target_roas",)
        TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
        target_roas: float
        def __init__(self, target_roas: _Optional[float] = ...) -> None: ...
    class MaximizeConversions(_message.Message):
        __slots__ = ("target_cpa", "target_cpa_micros")
        TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
        TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        target_cpa: int
        target_cpa_micros: int
        def __init__(self, target_cpa: _Optional[int] = ..., target_cpa_micros: _Optional[int] = ...) -> None: ...
    class TargetCpa(_message.Message):
        __slots__ = ("target_cpa_micros",)
        TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        target_cpa_micros: int
        def __init__(self, target_cpa_micros: _Optional[int] = ...) -> None: ...
    class TargetImpressionShare(_message.Message):
        __slots__ = ("location", "location_fraction_micros", "cpc_bid_ceiling_micros")
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FRACTION_MICROS_FIELD_NUMBER: _ClassVar[int]
        CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
        location: _target_impression_share_location_pb2.TargetImpressionShareLocationEnum.TargetImpressionShareLocation
        location_fraction_micros: int
        cpc_bid_ceiling_micros: int
        def __init__(self, location: _Optional[_Union[_target_impression_share_location_pb2.TargetImpressionShareLocationEnum.TargetImpressionShareLocation, str]] = ..., location_fraction_micros: _Optional[int] = ..., cpc_bid_ceiling_micros: _Optional[int] = ...) -> None: ...
    class TargetRoas(_message.Message):
        __slots__ = ("target_roas",)
        TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
        target_roas: float
        def __init__(self, target_roas: _Optional[float] = ...) -> None: ...
    class TargetSpend(_message.Message):
        __slots__ = ("target_spend_micros", "cpc_bid_ceiling_micros")
        TARGET_SPEND_MICROS_FIELD_NUMBER: _ClassVar[int]
        CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
        target_spend_micros: int
        cpc_bid_ceiling_micros: int
        def __init__(self, target_spend_micros: _Optional[int] = ..., cpc_bid_ceiling_micros: _Optional[int] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
    TARGET_IMPRESSION_SHARE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SPEND_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    type: _bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType
    owner_customer_id: int
    owner_descriptive_name: str
    maximize_conversion_value: AccessibleBiddingStrategy.MaximizeConversionValue
    maximize_conversions: AccessibleBiddingStrategy.MaximizeConversions
    target_cpa: AccessibleBiddingStrategy.TargetCpa
    target_impression_share: AccessibleBiddingStrategy.TargetImpressionShare
    target_roas: AccessibleBiddingStrategy.TargetRoas
    target_spend: AccessibleBiddingStrategy.TargetSpend
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType, str]] = ..., owner_customer_id: _Optional[int] = ..., owner_descriptive_name: _Optional[str] = ..., maximize_conversion_value: _Optional[_Union[AccessibleBiddingStrategy.MaximizeConversionValue, _Mapping]] = ..., maximize_conversions: _Optional[_Union[AccessibleBiddingStrategy.MaximizeConversions, _Mapping]] = ..., target_cpa: _Optional[_Union[AccessibleBiddingStrategy.TargetCpa, _Mapping]] = ..., target_impression_share: _Optional[_Union[AccessibleBiddingStrategy.TargetImpressionShare, _Mapping]] = ..., target_roas: _Optional[_Union[AccessibleBiddingStrategy.TargetRoas, _Mapping]] = ..., target_spend: _Optional[_Union[AccessibleBiddingStrategy.TargetSpend, _Mapping]] = ...) -> None: ...
