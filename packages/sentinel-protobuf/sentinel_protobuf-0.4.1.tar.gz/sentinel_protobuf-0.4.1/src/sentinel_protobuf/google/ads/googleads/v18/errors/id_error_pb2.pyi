from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IdErrorEnum(_message.Message):
    __slots__ = ()

    class IdError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[IdErrorEnum.IdError]
        UNKNOWN: _ClassVar[IdErrorEnum.IdError]
        NOT_FOUND: _ClassVar[IdErrorEnum.IdError]
    UNSPECIFIED: IdErrorEnum.IdError
    UNKNOWN: IdErrorEnum.IdError
    NOT_FOUND: IdErrorEnum.IdError

    def __init__(self) -> None:
        ...