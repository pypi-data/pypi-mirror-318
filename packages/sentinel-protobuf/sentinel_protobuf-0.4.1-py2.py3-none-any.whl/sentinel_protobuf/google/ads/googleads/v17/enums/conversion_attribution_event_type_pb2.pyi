from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionAttributionEventTypeEnum(_message.Message):
    __slots__ = ()

    class ConversionAttributionEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionAttributionEventTypeEnum.ConversionAttributionEventType]
        UNKNOWN: _ClassVar[ConversionAttributionEventTypeEnum.ConversionAttributionEventType]
        IMPRESSION: _ClassVar[ConversionAttributionEventTypeEnum.ConversionAttributionEventType]
        INTERACTION: _ClassVar[ConversionAttributionEventTypeEnum.ConversionAttributionEventType]
    UNSPECIFIED: ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    UNKNOWN: ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    IMPRESSION: ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    INTERACTION: ConversionAttributionEventTypeEnum.ConversionAttributionEventType

    def __init__(self) -> None:
        ...