from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeStatusErrorEnum(_message.Message):
    __slots__ = ()

    class ChangeStatusError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ChangeStatusErrorEnum.ChangeStatusError]
        UNKNOWN: _ClassVar[ChangeStatusErrorEnum.ChangeStatusError]
        START_DATE_TOO_OLD: _ClassVar[ChangeStatusErrorEnum.ChangeStatusError]
        CHANGE_DATE_RANGE_INFINITE: _ClassVar[ChangeStatusErrorEnum.ChangeStatusError]
        CHANGE_DATE_RANGE_NEGATIVE: _ClassVar[ChangeStatusErrorEnum.ChangeStatusError]
        LIMIT_NOT_SPECIFIED: _ClassVar[ChangeStatusErrorEnum.ChangeStatusError]
        INVALID_LIMIT_CLAUSE: _ClassVar[ChangeStatusErrorEnum.ChangeStatusError]
    UNSPECIFIED: ChangeStatusErrorEnum.ChangeStatusError
    UNKNOWN: ChangeStatusErrorEnum.ChangeStatusError
    START_DATE_TOO_OLD: ChangeStatusErrorEnum.ChangeStatusError
    CHANGE_DATE_RANGE_INFINITE: ChangeStatusErrorEnum.ChangeStatusError
    CHANGE_DATE_RANGE_NEGATIVE: ChangeStatusErrorEnum.ChangeStatusError
    LIMIT_NOT_SPECIFIED: ChangeStatusErrorEnum.ChangeStatusError
    INVALID_LIMIT_CLAUSE: ChangeStatusErrorEnum.ChangeStatusError

    def __init__(self) -> None:
        ...