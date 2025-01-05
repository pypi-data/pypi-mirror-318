from google.ads.searchads360.v0.enums import target_impression_share_location_pb2 as _target_impression_share_location_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnhancedCpc(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ManualCpa(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ManualCpc(_message.Message):
    __slots__ = ("enhanced_cpc_enabled",)
    ENHANCED_CPC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    enhanced_cpc_enabled: bool
    def __init__(self, enhanced_cpc_enabled: bool = ...) -> None: ...

class ManualCpm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaximizeConversions(_message.Message):
    __slots__ = ("cpc_bid_ceiling_micros", "cpc_bid_floor_micros", "target_cpa_micros")
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_FLOOR_MICROS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    target_cpa_micros: int
    def __init__(self, cpc_bid_ceiling_micros: _Optional[int] = ..., cpc_bid_floor_micros: _Optional[int] = ..., target_cpa_micros: _Optional[int] = ...) -> None: ...

class MaximizeConversionValue(_message.Message):
    __slots__ = ("target_roas", "cpc_bid_ceiling_micros", "cpc_bid_floor_micros")
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_FLOOR_MICROS_FIELD_NUMBER: _ClassVar[int]
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(self, target_roas: _Optional[float] = ..., cpc_bid_ceiling_micros: _Optional[int] = ..., cpc_bid_floor_micros: _Optional[int] = ...) -> None: ...

class TargetCpa(_message.Message):
    __slots__ = ("target_cpa_micros", "cpc_bid_ceiling_micros", "cpc_bid_floor_micros")
    TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_FLOOR_MICROS_FIELD_NUMBER: _ClassVar[int]
    target_cpa_micros: int
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(self, target_cpa_micros: _Optional[int] = ..., cpc_bid_ceiling_micros: _Optional[int] = ..., cpc_bid_floor_micros: _Optional[int] = ...) -> None: ...

class TargetCpm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TargetImpressionShare(_message.Message):
    __slots__ = ("location", "location_fraction_micros", "cpc_bid_ceiling_micros")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FRACTION_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    location: _target_impression_share_location_pb2.TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    location_fraction_micros: int
    cpc_bid_ceiling_micros: int
    def __init__(self, location: _Optional[_Union[_target_impression_share_location_pb2.TargetImpressionShareLocationEnum.TargetImpressionShareLocation, str]] = ..., location_fraction_micros: _Optional[int] = ..., cpc_bid_ceiling_micros: _Optional[int] = ...) -> None: ...

class TargetOutrankShare(_message.Message):
    __slots__ = ("cpc_bid_ceiling_micros",)
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    cpc_bid_ceiling_micros: _wrappers_pb2.Int64Value
    def __init__(self, cpc_bid_ceiling_micros: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class TargetRoas(_message.Message):
    __slots__ = ("target_roas", "cpc_bid_ceiling_micros", "cpc_bid_floor_micros")
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_FLOOR_MICROS_FIELD_NUMBER: _ClassVar[int]
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(self, target_roas: _Optional[float] = ..., cpc_bid_ceiling_micros: _Optional[int] = ..., cpc_bid_floor_micros: _Optional[int] = ...) -> None: ...

class TargetSpend(_message.Message):
    __slots__ = ("target_spend_micros", "cpc_bid_ceiling_micros")
    TARGET_SPEND_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    target_spend_micros: int
    cpc_bid_ceiling_micros: int
    def __init__(self, target_spend_micros: _Optional[int] = ..., cpc_bid_ceiling_micros: _Optional[int] = ...) -> None: ...

class PercentCpc(_message.Message):
    __slots__ = ("cpc_bid_ceiling_micros", "enhanced_cpc_enabled")
    CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    ENHANCED_CPC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    cpc_bid_ceiling_micros: int
    enhanced_cpc_enabled: bool
    def __init__(self, cpc_bid_ceiling_micros: _Optional[int] = ..., enhanced_cpc_enabled: bool = ...) -> None: ...
