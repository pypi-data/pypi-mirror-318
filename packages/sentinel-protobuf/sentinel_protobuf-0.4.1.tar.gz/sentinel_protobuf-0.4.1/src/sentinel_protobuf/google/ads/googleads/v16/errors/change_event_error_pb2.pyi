from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeEventErrorEnum(_message.Message):
    __slots__ = ()

    class ChangeEventError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ChangeEventErrorEnum.ChangeEventError]
        UNKNOWN: _ClassVar[ChangeEventErrorEnum.ChangeEventError]
        START_DATE_TOO_OLD: _ClassVar[ChangeEventErrorEnum.ChangeEventError]
        CHANGE_DATE_RANGE_INFINITE: _ClassVar[ChangeEventErrorEnum.ChangeEventError]
        CHANGE_DATE_RANGE_NEGATIVE: _ClassVar[ChangeEventErrorEnum.ChangeEventError]
        LIMIT_NOT_SPECIFIED: _ClassVar[ChangeEventErrorEnum.ChangeEventError]
        INVALID_LIMIT_CLAUSE: _ClassVar[ChangeEventErrorEnum.ChangeEventError]
    UNSPECIFIED: ChangeEventErrorEnum.ChangeEventError
    UNKNOWN: ChangeEventErrorEnum.ChangeEventError
    START_DATE_TOO_OLD: ChangeEventErrorEnum.ChangeEventError
    CHANGE_DATE_RANGE_INFINITE: ChangeEventErrorEnum.ChangeEventError
    CHANGE_DATE_RANGE_NEGATIVE: ChangeEventErrorEnum.ChangeEventError
    LIMIT_NOT_SPECIFIED: ChangeEventErrorEnum.ChangeEventError
    INVALID_LIMIT_CLAUSE: ChangeEventErrorEnum.ChangeEventError

    def __init__(self) -> None:
        ...