from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BiddingStrategyErrorEnum(_message.Message):
    __slots__ = ()

    class BiddingStrategyError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BiddingStrategyErrorEnum.BiddingStrategyError]
        UNKNOWN: _ClassVar[BiddingStrategyErrorEnum.BiddingStrategyError]
        DUPLICATE_NAME: _ClassVar[BiddingStrategyErrorEnum.BiddingStrategyError]
        CANNOT_CHANGE_BIDDING_STRATEGY_TYPE: _ClassVar[BiddingStrategyErrorEnum.BiddingStrategyError]
        CANNOT_REMOVE_ASSOCIATED_STRATEGY: _ClassVar[BiddingStrategyErrorEnum.BiddingStrategyError]
        BIDDING_STRATEGY_NOT_SUPPORTED: _ClassVar[BiddingStrategyErrorEnum.BiddingStrategyError]
        INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE: _ClassVar[BiddingStrategyErrorEnum.BiddingStrategyError]
    UNSPECIFIED: BiddingStrategyErrorEnum.BiddingStrategyError
    UNKNOWN: BiddingStrategyErrorEnum.BiddingStrategyError
    DUPLICATE_NAME: BiddingStrategyErrorEnum.BiddingStrategyError
    CANNOT_CHANGE_BIDDING_STRATEGY_TYPE: BiddingStrategyErrorEnum.BiddingStrategyError
    CANNOT_REMOVE_ASSOCIATED_STRATEGY: BiddingStrategyErrorEnum.BiddingStrategyError
    BIDDING_STRATEGY_NOT_SUPPORTED: BiddingStrategyErrorEnum.BiddingStrategyError
    INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE: BiddingStrategyErrorEnum.BiddingStrategyError

    def __init__(self) -> None:
        ...