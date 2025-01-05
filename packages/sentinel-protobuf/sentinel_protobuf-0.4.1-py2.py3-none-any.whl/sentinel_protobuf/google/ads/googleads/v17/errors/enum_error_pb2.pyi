from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class EnumErrorEnum(_message.Message):
    __slots__ = ()

    class EnumError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[EnumErrorEnum.EnumError]
        UNKNOWN: _ClassVar[EnumErrorEnum.EnumError]
        ENUM_VALUE_NOT_PERMITTED: _ClassVar[EnumErrorEnum.EnumError]
    UNSPECIFIED: EnumErrorEnum.EnumError
    UNKNOWN: EnumErrorEnum.EnumError
    ENUM_VALUE_NOT_PERMITTED: EnumErrorEnum.EnumError

    def __init__(self) -> None:
        ...