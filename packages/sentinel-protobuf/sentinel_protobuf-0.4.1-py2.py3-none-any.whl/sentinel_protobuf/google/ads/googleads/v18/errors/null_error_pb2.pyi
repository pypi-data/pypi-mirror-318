from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NullErrorEnum(_message.Message):
    __slots__ = ()

    class NullError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NullErrorEnum.NullError]
        UNKNOWN: _ClassVar[NullErrorEnum.NullError]
        NULL_CONTENT: _ClassVar[NullErrorEnum.NullError]
    UNSPECIFIED: NullErrorEnum.NullError
    UNKNOWN: NullErrorEnum.NullError
    NULL_CONTENT: NullErrorEnum.NullError

    def __init__(self) -> None:
        ...