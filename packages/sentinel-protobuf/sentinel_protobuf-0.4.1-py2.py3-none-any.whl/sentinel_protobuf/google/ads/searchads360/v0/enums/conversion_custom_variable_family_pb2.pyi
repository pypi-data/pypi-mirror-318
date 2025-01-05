from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionCustomVariableFamilyEnum(_message.Message):
    __slots__ = ()

    class ConversionCustomVariableFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily]
        UNKNOWN: _ClassVar[ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily]
        STANDARD: _ClassVar[ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily]
        FLOODLIGHT: _ClassVar[ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily]
    UNSPECIFIED: ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily
    UNKNOWN: ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily
    STANDARD: ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily
    FLOODLIGHT: ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily

    def __init__(self) -> None:
        ...