from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TimeZoneErrorEnum(_message.Message):
    __slots__ = ()

    class TimeZoneError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TimeZoneErrorEnum.TimeZoneError]
        UNKNOWN: _ClassVar[TimeZoneErrorEnum.TimeZoneError]
        INVALID_TIME_ZONE: _ClassVar[TimeZoneErrorEnum.TimeZoneError]
    UNSPECIFIED: TimeZoneErrorEnum.TimeZoneError
    UNKNOWN: TimeZoneErrorEnum.TimeZoneError
    INVALID_TIME_ZONE: TimeZoneErrorEnum.TimeZoneError

    def __init__(self) -> None:
        ...