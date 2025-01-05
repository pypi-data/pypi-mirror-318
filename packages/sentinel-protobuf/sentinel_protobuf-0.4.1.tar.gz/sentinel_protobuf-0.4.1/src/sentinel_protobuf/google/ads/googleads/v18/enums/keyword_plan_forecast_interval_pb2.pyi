from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanForecastIntervalEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanForecastInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval]
        UNKNOWN: _ClassVar[KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval]
        NEXT_WEEK: _ClassVar[KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval]
        NEXT_MONTH: _ClassVar[KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval]
        NEXT_QUARTER: _ClassVar[KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval]
    UNSPECIFIED: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    UNKNOWN: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    NEXT_WEEK: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    NEXT_MONTH: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    NEXT_QUARTER: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval

    def __init__(self) -> None:
        ...