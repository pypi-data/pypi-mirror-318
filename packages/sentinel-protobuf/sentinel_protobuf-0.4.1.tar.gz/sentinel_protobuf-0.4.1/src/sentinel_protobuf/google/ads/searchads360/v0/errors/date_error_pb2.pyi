from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DateErrorEnum(_message.Message):
    __slots__ = ()

    class DateError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DateErrorEnum.DateError]
        UNKNOWN: _ClassVar[DateErrorEnum.DateError]
        INVALID_FIELD_VALUES_IN_DATE: _ClassVar[DateErrorEnum.DateError]
        INVALID_FIELD_VALUES_IN_DATE_TIME: _ClassVar[DateErrorEnum.DateError]
        INVALID_STRING_DATE: _ClassVar[DateErrorEnum.DateError]
        INVALID_STRING_DATE_TIME_MICROS: _ClassVar[DateErrorEnum.DateError]
        INVALID_STRING_DATE_TIME_SECONDS: _ClassVar[DateErrorEnum.DateError]
        INVALID_STRING_DATE_TIME_SECONDS_WITH_OFFSET: _ClassVar[DateErrorEnum.DateError]
        EARLIER_THAN_MINIMUM_DATE: _ClassVar[DateErrorEnum.DateError]
        LATER_THAN_MAXIMUM_DATE: _ClassVar[DateErrorEnum.DateError]
        DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE: _ClassVar[DateErrorEnum.DateError]
        DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL: _ClassVar[DateErrorEnum.DateError]
    UNSPECIFIED: DateErrorEnum.DateError
    UNKNOWN: DateErrorEnum.DateError
    INVALID_FIELD_VALUES_IN_DATE: DateErrorEnum.DateError
    INVALID_FIELD_VALUES_IN_DATE_TIME: DateErrorEnum.DateError
    INVALID_STRING_DATE: DateErrorEnum.DateError
    INVALID_STRING_DATE_TIME_MICROS: DateErrorEnum.DateError
    INVALID_STRING_DATE_TIME_SECONDS: DateErrorEnum.DateError
    INVALID_STRING_DATE_TIME_SECONDS_WITH_OFFSET: DateErrorEnum.DateError
    EARLIER_THAN_MINIMUM_DATE: DateErrorEnum.DateError
    LATER_THAN_MAXIMUM_DATE: DateErrorEnum.DateError
    DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE: DateErrorEnum.DateError
    DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL: DateErrorEnum.DateError

    def __init__(self) -> None:
        ...