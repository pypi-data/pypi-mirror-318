from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class StringFormatErrorEnum(_message.Message):
    __slots__ = ()

    class StringFormatError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[StringFormatErrorEnum.StringFormatError]
        UNKNOWN: _ClassVar[StringFormatErrorEnum.StringFormatError]
        ILLEGAL_CHARS: _ClassVar[StringFormatErrorEnum.StringFormatError]
        INVALID_FORMAT: _ClassVar[StringFormatErrorEnum.StringFormatError]
    UNSPECIFIED: StringFormatErrorEnum.StringFormatError
    UNKNOWN: StringFormatErrorEnum.StringFormatError
    ILLEGAL_CHARS: StringFormatErrorEnum.StringFormatError
    INVALID_FORMAT: StringFormatErrorEnum.StringFormatError

    def __init__(self) -> None:
        ...