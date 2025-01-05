from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DateRangeErrorEnum(_message.Message):
    __slots__ = ()

    class DateRangeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DateRangeErrorEnum.DateRangeError]
        UNKNOWN: _ClassVar[DateRangeErrorEnum.DateRangeError]
        INVALID_DATE: _ClassVar[DateRangeErrorEnum.DateRangeError]
        START_DATE_AFTER_END_DATE: _ClassVar[DateRangeErrorEnum.DateRangeError]
        CANNOT_SET_DATE_TO_PAST: _ClassVar[DateRangeErrorEnum.DateRangeError]
        AFTER_MAXIMUM_ALLOWABLE_DATE: _ClassVar[DateRangeErrorEnum.DateRangeError]
        CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED: _ClassVar[DateRangeErrorEnum.DateRangeError]
    UNSPECIFIED: DateRangeErrorEnum.DateRangeError
    UNKNOWN: DateRangeErrorEnum.DateRangeError
    INVALID_DATE: DateRangeErrorEnum.DateRangeError
    START_DATE_AFTER_END_DATE: DateRangeErrorEnum.DateRangeError
    CANNOT_SET_DATE_TO_PAST: DateRangeErrorEnum.DateRangeError
    AFTER_MAXIMUM_ALLOWABLE_DATE: DateRangeErrorEnum.DateRangeError
    CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED: DateRangeErrorEnum.DateRangeError

    def __init__(self) -> None:
        ...