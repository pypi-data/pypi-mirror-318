from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MultiplierErrorEnum(_message.Message):
    __slots__ = ()

    class MultiplierError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MultiplierErrorEnum.MultiplierError]
        UNKNOWN: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_TOO_HIGH: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_TOO_LOW: _ClassVar[MultiplierErrorEnum.MultiplierError]
        TOO_MANY_FRACTIONAL_DIGITS: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_NOT_ALLOWED_FOR_BIDDING_STRATEGY: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_NOT_ALLOWED_WHEN_BASE_BID_IS_MISSING: _ClassVar[MultiplierErrorEnum.MultiplierError]
        NO_MULTIPLIER_SPECIFIED: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_DAILY_BUDGET: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_MONTHLY_BUDGET: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_CUSTOM_BUDGET: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_MAX_ALLOWED_BID: _ClassVar[MultiplierErrorEnum.MultiplierError]
        BID_LESS_THAN_MIN_ALLOWED_BID_WITH_MULTIPLIER: _ClassVar[MultiplierErrorEnum.MultiplierError]
        MULTIPLIER_AND_BIDDING_STRATEGY_TYPE_MISMATCH: _ClassVar[MultiplierErrorEnum.MultiplierError]
    UNSPECIFIED: MultiplierErrorEnum.MultiplierError
    UNKNOWN: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_TOO_HIGH: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_TOO_LOW: MultiplierErrorEnum.MultiplierError
    TOO_MANY_FRACTIONAL_DIGITS: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_NOT_ALLOWED_FOR_BIDDING_STRATEGY: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_NOT_ALLOWED_WHEN_BASE_BID_IS_MISSING: MultiplierErrorEnum.MultiplierError
    NO_MULTIPLIER_SPECIFIED: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_CAUSES_BID_TO_EXCEED_DAILY_BUDGET: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_CAUSES_BID_TO_EXCEED_MONTHLY_BUDGET: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_CAUSES_BID_TO_EXCEED_CUSTOM_BUDGET: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_CAUSES_BID_TO_EXCEED_MAX_ALLOWED_BID: MultiplierErrorEnum.MultiplierError
    BID_LESS_THAN_MIN_ALLOWED_BID_WITH_MULTIPLIER: MultiplierErrorEnum.MultiplierError
    MULTIPLIER_AND_BIDDING_STRATEGY_TYPE_MISMATCH: MultiplierErrorEnum.MultiplierError

    def __init__(self) -> None:
        ...