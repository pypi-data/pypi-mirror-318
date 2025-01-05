from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomColumnErrorEnum(_message.Message):
    __slots__ = ()

    class CustomColumnError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomColumnErrorEnum.CustomColumnError]
        UNKNOWN: _ClassVar[CustomColumnErrorEnum.CustomColumnError]
        CUSTOM_COLUMN_NOT_FOUND: _ClassVar[CustomColumnErrorEnum.CustomColumnError]
        CUSTOM_COLUMN_NOT_AVAILABLE: _ClassVar[CustomColumnErrorEnum.CustomColumnError]
    UNSPECIFIED: CustomColumnErrorEnum.CustomColumnError
    UNKNOWN: CustomColumnErrorEnum.CustomColumnError
    CUSTOM_COLUMN_NOT_FOUND: CustomColumnErrorEnum.CustomColumnError
    CUSTOM_COLUMN_NOT_AVAILABLE: CustomColumnErrorEnum.CustomColumnError

    def __init__(self) -> None:
        ...