from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionCustomVariableErrorEnum(_message.Message):
    __slots__ = ()

    class ConversionCustomVariableError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionCustomVariableErrorEnum.ConversionCustomVariableError]
        UNKNOWN: _ClassVar[ConversionCustomVariableErrorEnum.ConversionCustomVariableError]
        DUPLICATE_NAME: _ClassVar[ConversionCustomVariableErrorEnum.ConversionCustomVariableError]
        DUPLICATE_TAG: _ClassVar[ConversionCustomVariableErrorEnum.ConversionCustomVariableError]
        RESERVED_TAG: _ClassVar[ConversionCustomVariableErrorEnum.ConversionCustomVariableError]
    UNSPECIFIED: ConversionCustomVariableErrorEnum.ConversionCustomVariableError
    UNKNOWN: ConversionCustomVariableErrorEnum.ConversionCustomVariableError
    DUPLICATE_NAME: ConversionCustomVariableErrorEnum.ConversionCustomVariableError
    DUPLICATE_TAG: ConversionCustomVariableErrorEnum.ConversionCustomVariableError
    RESERVED_TAG: ConversionCustomVariableErrorEnum.ConversionCustomVariableError

    def __init__(self) -> None:
        ...