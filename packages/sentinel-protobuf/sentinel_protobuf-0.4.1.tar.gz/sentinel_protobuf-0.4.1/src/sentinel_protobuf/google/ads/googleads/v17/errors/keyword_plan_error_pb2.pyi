from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanErrorEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        UNKNOWN: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        BID_MULTIPLIER_OUT_OF_RANGE: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        BID_TOO_HIGH: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        BID_TOO_LOW: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        BID_TOO_MANY_FRACTIONAL_DIGITS: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        DAILY_BUDGET_TOO_LOW: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        INVALID_VALUE: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        KEYWORD_PLAN_HAS_NO_KEYWORDS: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        KEYWORD_PLAN_NOT_ENABLED: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        KEYWORD_PLAN_NOT_FOUND: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        MISSING_BID: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        MISSING_FORECAST_PERIOD: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        INVALID_FORECAST_DATE_RANGE: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
        INVALID_NAME: _ClassVar[KeywordPlanErrorEnum.KeywordPlanError]
    UNSPECIFIED: KeywordPlanErrorEnum.KeywordPlanError
    UNKNOWN: KeywordPlanErrorEnum.KeywordPlanError
    BID_MULTIPLIER_OUT_OF_RANGE: KeywordPlanErrorEnum.KeywordPlanError
    BID_TOO_HIGH: KeywordPlanErrorEnum.KeywordPlanError
    BID_TOO_LOW: KeywordPlanErrorEnum.KeywordPlanError
    BID_TOO_MANY_FRACTIONAL_DIGITS: KeywordPlanErrorEnum.KeywordPlanError
    DAILY_BUDGET_TOO_LOW: KeywordPlanErrorEnum.KeywordPlanError
    DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS: KeywordPlanErrorEnum.KeywordPlanError
    INVALID_VALUE: KeywordPlanErrorEnum.KeywordPlanError
    KEYWORD_PLAN_HAS_NO_KEYWORDS: KeywordPlanErrorEnum.KeywordPlanError
    KEYWORD_PLAN_NOT_ENABLED: KeywordPlanErrorEnum.KeywordPlanError
    KEYWORD_PLAN_NOT_FOUND: KeywordPlanErrorEnum.KeywordPlanError
    MISSING_BID: KeywordPlanErrorEnum.KeywordPlanError
    MISSING_FORECAST_PERIOD: KeywordPlanErrorEnum.KeywordPlanError
    INVALID_FORECAST_DATE_RANGE: KeywordPlanErrorEnum.KeywordPlanError
    INVALID_NAME: KeywordPlanErrorEnum.KeywordPlanError

    def __init__(self) -> None:
        ...