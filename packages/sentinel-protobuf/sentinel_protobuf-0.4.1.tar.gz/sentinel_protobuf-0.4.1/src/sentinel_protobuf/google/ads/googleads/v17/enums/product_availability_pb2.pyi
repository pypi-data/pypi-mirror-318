from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductAvailabilityEnum(_message.Message):
    __slots__ = ()

    class ProductAvailability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductAvailabilityEnum.ProductAvailability]
        UNKNOWN: _ClassVar[ProductAvailabilityEnum.ProductAvailability]
        IN_STOCK: _ClassVar[ProductAvailabilityEnum.ProductAvailability]
        OUT_OF_STOCK: _ClassVar[ProductAvailabilityEnum.ProductAvailability]
        PREORDER: _ClassVar[ProductAvailabilityEnum.ProductAvailability]
    UNSPECIFIED: ProductAvailabilityEnum.ProductAvailability
    UNKNOWN: ProductAvailabilityEnum.ProductAvailability
    IN_STOCK: ProductAvailabilityEnum.ProductAvailability
    OUT_OF_STOCK: ProductAvailabilityEnum.ProductAvailability
    PREORDER: ProductAvailabilityEnum.ProductAvailability

    def __init__(self) -> None:
        ...