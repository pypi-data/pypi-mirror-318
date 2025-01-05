from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionActionCountingTypeEnum(_message.Message):
    __slots__ = ()

    class ConversionActionCountingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionActionCountingTypeEnum.ConversionActionCountingType]
        UNKNOWN: _ClassVar[ConversionActionCountingTypeEnum.ConversionActionCountingType]
        ONE_PER_CLICK: _ClassVar[ConversionActionCountingTypeEnum.ConversionActionCountingType]
        MANY_PER_CLICK: _ClassVar[ConversionActionCountingTypeEnum.ConversionActionCountingType]
    UNSPECIFIED: ConversionActionCountingTypeEnum.ConversionActionCountingType
    UNKNOWN: ConversionActionCountingTypeEnum.ConversionActionCountingType
    ONE_PER_CLICK: ConversionActionCountingTypeEnum.ConversionActionCountingType
    MANY_PER_CLICK: ConversionActionCountingTypeEnum.ConversionActionCountingType

    def __init__(self) -> None:
        ...