from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BiddingStrategySystemStatusEnum(_message.Message):
    __slots__ = ()

    class BiddingStrategySystemStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        UNKNOWN: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        ENABLED: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LEARNING_NEW: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LEARNING_SETTING_CHANGE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LEARNING_BUDGET_CHANGE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LEARNING_COMPOSITION_CHANGE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LEARNING_CONVERSION_TYPE_CHANGE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LEARNING_CONVERSION_SETTING_CHANGE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LIMITED_BY_CPC_BID_CEILING: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LIMITED_BY_CPC_BID_FLOOR: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LIMITED_BY_DATA: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LIMITED_BY_BUDGET: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LIMITED_BY_LOW_PRIORITY_SPEND: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LIMITED_BY_LOW_QUALITY: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        LIMITED_BY_INVENTORY: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MISCONFIGURED_ZERO_ELIGIBILITY: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MISCONFIGURED_CONVERSION_TYPES: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MISCONFIGURED_CONVERSION_SETTINGS: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MISCONFIGURED_SHARED_BUDGET: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MISCONFIGURED_STRATEGY_TYPE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        PAUSED: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        UNAVAILABLE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MULTIPLE_LEARNING: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MULTIPLE_LIMITED: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MULTIPLE_MISCONFIGURED: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
        MULTIPLE: _ClassVar[BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus]
    UNSPECIFIED: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    UNKNOWN: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    ENABLED: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LEARNING_NEW: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LEARNING_SETTING_CHANGE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LEARNING_BUDGET_CHANGE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LEARNING_COMPOSITION_CHANGE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LEARNING_CONVERSION_TYPE_CHANGE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LEARNING_CONVERSION_SETTING_CHANGE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LIMITED_BY_CPC_BID_CEILING: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LIMITED_BY_CPC_BID_FLOOR: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LIMITED_BY_DATA: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LIMITED_BY_BUDGET: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LIMITED_BY_LOW_PRIORITY_SPEND: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LIMITED_BY_LOW_QUALITY: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    LIMITED_BY_INVENTORY: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MISCONFIGURED_ZERO_ELIGIBILITY: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MISCONFIGURED_CONVERSION_TYPES: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MISCONFIGURED_CONVERSION_SETTINGS: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MISCONFIGURED_SHARED_BUDGET: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MISCONFIGURED_STRATEGY_TYPE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    PAUSED: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    UNAVAILABLE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MULTIPLE_LEARNING: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MULTIPLE_LIMITED: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MULTIPLE_MISCONFIGURED: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    MULTIPLE: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus

    def __init__(self) -> None:
        ...