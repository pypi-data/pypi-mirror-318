from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BiddingStrategyTypeEnum(_message.Message):
    __slots__ = ()

    class BiddingStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        UNKNOWN: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        COMMISSION: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        ENHANCED_CPC: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        INVALID: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        MANUAL_CPA: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        MANUAL_CPC: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        MANUAL_CPM: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        MANUAL_CPV: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        MAXIMIZE_CONVERSIONS: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        MAXIMIZE_CONVERSION_VALUE: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        PAGE_ONE_PROMOTED: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        PERCENT_CPC: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        TARGET_CPA: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        TARGET_CPM: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        TARGET_IMPRESSION_SHARE: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        TARGET_OUTRANK_SHARE: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        TARGET_ROAS: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
        TARGET_SPEND: _ClassVar[BiddingStrategyTypeEnum.BiddingStrategyType]
    UNSPECIFIED: BiddingStrategyTypeEnum.BiddingStrategyType
    UNKNOWN: BiddingStrategyTypeEnum.BiddingStrategyType
    COMMISSION: BiddingStrategyTypeEnum.BiddingStrategyType
    ENHANCED_CPC: BiddingStrategyTypeEnum.BiddingStrategyType
    INVALID: BiddingStrategyTypeEnum.BiddingStrategyType
    MANUAL_CPA: BiddingStrategyTypeEnum.BiddingStrategyType
    MANUAL_CPC: BiddingStrategyTypeEnum.BiddingStrategyType
    MANUAL_CPM: BiddingStrategyTypeEnum.BiddingStrategyType
    MANUAL_CPV: BiddingStrategyTypeEnum.BiddingStrategyType
    MAXIMIZE_CONVERSIONS: BiddingStrategyTypeEnum.BiddingStrategyType
    MAXIMIZE_CONVERSION_VALUE: BiddingStrategyTypeEnum.BiddingStrategyType
    PAGE_ONE_PROMOTED: BiddingStrategyTypeEnum.BiddingStrategyType
    PERCENT_CPC: BiddingStrategyTypeEnum.BiddingStrategyType
    TARGET_CPA: BiddingStrategyTypeEnum.BiddingStrategyType
    TARGET_CPM: BiddingStrategyTypeEnum.BiddingStrategyType
    TARGET_IMPRESSION_SHARE: BiddingStrategyTypeEnum.BiddingStrategyType
    TARGET_OUTRANK_SHARE: BiddingStrategyTypeEnum.BiddingStrategyType
    TARGET_ROAS: BiddingStrategyTypeEnum.BiddingStrategyType
    TARGET_SPEND: BiddingStrategyTypeEnum.BiddingStrategyType

    def __init__(self) -> None:
        ...