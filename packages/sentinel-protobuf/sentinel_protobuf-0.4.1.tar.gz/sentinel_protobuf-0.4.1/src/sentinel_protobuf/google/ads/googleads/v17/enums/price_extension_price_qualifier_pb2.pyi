from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PriceExtensionPriceQualifierEnum(_message.Message):
    __slots__ = ()

    class PriceExtensionPriceQualifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier]
        UNKNOWN: _ClassVar[PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier]
        FROM: _ClassVar[PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier]
        UP_TO: _ClassVar[PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier]
        AVERAGE: _ClassVar[PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier]
    UNSPECIFIED: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    UNKNOWN: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    FROM: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    UP_TO: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    AVERAGE: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier

    def __init__(self) -> None:
        ...