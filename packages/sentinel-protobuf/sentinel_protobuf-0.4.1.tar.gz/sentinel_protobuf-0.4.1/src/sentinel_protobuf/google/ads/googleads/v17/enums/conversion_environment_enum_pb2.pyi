from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionEnvironmentEnum(_message.Message):
    __slots__ = ()

    class ConversionEnvironment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionEnvironmentEnum.ConversionEnvironment]
        UNKNOWN: _ClassVar[ConversionEnvironmentEnum.ConversionEnvironment]
        APP: _ClassVar[ConversionEnvironmentEnum.ConversionEnvironment]
        WEB: _ClassVar[ConversionEnvironmentEnum.ConversionEnvironment]
    UNSPECIFIED: ConversionEnvironmentEnum.ConversionEnvironment
    UNKNOWN: ConversionEnvironmentEnum.ConversionEnvironment
    APP: ConversionEnvironmentEnum.ConversionEnvironment
    WEB: ConversionEnvironmentEnum.ConversionEnvironment

    def __init__(self) -> None:
        ...