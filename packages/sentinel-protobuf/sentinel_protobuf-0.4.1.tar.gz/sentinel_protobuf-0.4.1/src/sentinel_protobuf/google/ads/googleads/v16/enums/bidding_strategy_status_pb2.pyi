from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BiddingStrategyStatusEnum(_message.Message):
    __slots__ = ()

    class BiddingStrategyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BiddingStrategyStatusEnum.BiddingStrategyStatus]
        UNKNOWN: _ClassVar[BiddingStrategyStatusEnum.BiddingStrategyStatus]
        ENABLED: _ClassVar[BiddingStrategyStatusEnum.BiddingStrategyStatus]
        REMOVED: _ClassVar[BiddingStrategyStatusEnum.BiddingStrategyStatus]
    UNSPECIFIED: BiddingStrategyStatusEnum.BiddingStrategyStatus
    UNKNOWN: BiddingStrategyStatusEnum.BiddingStrategyStatus
    ENABLED: BiddingStrategyStatusEnum.BiddingStrategyStatus
    REMOVED: BiddingStrategyStatusEnum.BiddingStrategyStatus

    def __init__(self) -> None:
        ...