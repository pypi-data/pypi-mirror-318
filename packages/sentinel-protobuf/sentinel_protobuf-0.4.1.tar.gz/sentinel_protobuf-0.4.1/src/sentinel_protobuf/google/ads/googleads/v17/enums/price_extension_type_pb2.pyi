from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PriceExtensionTypeEnum(_message.Message):
    __slots__ = ()

    class PriceExtensionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        UNKNOWN: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        BRANDS: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        EVENTS: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        LOCATIONS: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        NEIGHBORHOODS: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        PRODUCT_CATEGORIES: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        PRODUCT_TIERS: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        SERVICES: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        SERVICE_CATEGORIES: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
        SERVICE_TIERS: _ClassVar[PriceExtensionTypeEnum.PriceExtensionType]
    UNSPECIFIED: PriceExtensionTypeEnum.PriceExtensionType
    UNKNOWN: PriceExtensionTypeEnum.PriceExtensionType
    BRANDS: PriceExtensionTypeEnum.PriceExtensionType
    EVENTS: PriceExtensionTypeEnum.PriceExtensionType
    LOCATIONS: PriceExtensionTypeEnum.PriceExtensionType
    NEIGHBORHOODS: PriceExtensionTypeEnum.PriceExtensionType
    PRODUCT_CATEGORIES: PriceExtensionTypeEnum.PriceExtensionType
    PRODUCT_TIERS: PriceExtensionTypeEnum.PriceExtensionType
    SERVICES: PriceExtensionTypeEnum.PriceExtensionType
    SERVICE_CATEGORIES: PriceExtensionTypeEnum.PriceExtensionType
    SERVICE_TIERS: PriceExtensionTypeEnum.PriceExtensionType

    def __init__(self) -> None:
        ...