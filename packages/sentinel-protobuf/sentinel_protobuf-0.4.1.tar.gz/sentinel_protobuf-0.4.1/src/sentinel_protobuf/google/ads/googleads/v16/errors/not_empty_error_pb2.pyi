from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NotEmptyErrorEnum(_message.Message):
    __slots__ = ()

    class NotEmptyError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NotEmptyErrorEnum.NotEmptyError]
        UNKNOWN: _ClassVar[NotEmptyErrorEnum.NotEmptyError]
        EMPTY_LIST: _ClassVar[NotEmptyErrorEnum.NotEmptyError]
    UNSPECIFIED: NotEmptyErrorEnum.NotEmptyError
    UNKNOWN: NotEmptyErrorEnum.NotEmptyError
    EMPTY_LIST: NotEmptyErrorEnum.NotEmptyError

    def __init__(self) -> None:
        ...