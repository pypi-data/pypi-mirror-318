from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InvalidParameterErrorEnum(_message.Message):
    __slots__ = ()

    class InvalidParameterError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InvalidParameterErrorEnum.InvalidParameterError]
        UNKNOWN: _ClassVar[InvalidParameterErrorEnum.InvalidParameterError]
        INVALID_CURRENCY_CODE: _ClassVar[InvalidParameterErrorEnum.InvalidParameterError]
    UNSPECIFIED: InvalidParameterErrorEnum.InvalidParameterError
    UNKNOWN: InvalidParameterErrorEnum.InvalidParameterError
    INVALID_CURRENCY_CODE: InvalidParameterErrorEnum.InvalidParameterError

    def __init__(self) -> None:
        ...