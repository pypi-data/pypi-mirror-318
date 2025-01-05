from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionStatusEnum(_message.Message):
    __slots__ = ()

    class ConversionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionStatusEnum.ConversionStatus]
        UNKNOWN: _ClassVar[ConversionStatusEnum.ConversionStatus]
        ENABLED: _ClassVar[ConversionStatusEnum.ConversionStatus]
        REMOVED: _ClassVar[ConversionStatusEnum.ConversionStatus]
    UNSPECIFIED: ConversionStatusEnum.ConversionStatus
    UNKNOWN: ConversionStatusEnum.ConversionStatus
    ENABLED: ConversionStatusEnum.ConversionStatus
    REMOVED: ConversionStatusEnum.ConversionStatus

    def __init__(self) -> None:
        ...