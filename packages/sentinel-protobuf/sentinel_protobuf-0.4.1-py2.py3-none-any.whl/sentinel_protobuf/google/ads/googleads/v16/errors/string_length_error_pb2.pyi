from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class StringLengthErrorEnum(_message.Message):
    __slots__ = ()

    class StringLengthError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[StringLengthErrorEnum.StringLengthError]
        UNKNOWN: _ClassVar[StringLengthErrorEnum.StringLengthError]
        EMPTY: _ClassVar[StringLengthErrorEnum.StringLengthError]
        TOO_SHORT: _ClassVar[StringLengthErrorEnum.StringLengthError]
        TOO_LONG: _ClassVar[StringLengthErrorEnum.StringLengthError]
    UNSPECIFIED: StringLengthErrorEnum.StringLengthError
    UNKNOWN: StringLengthErrorEnum.StringLengthError
    EMPTY: StringLengthErrorEnum.StringLengthError
    TOO_SHORT: StringLengthErrorEnum.StringLengthError
    TOO_LONG: StringLengthErrorEnum.StringLengthError

    def __init__(self) -> None:
        ...