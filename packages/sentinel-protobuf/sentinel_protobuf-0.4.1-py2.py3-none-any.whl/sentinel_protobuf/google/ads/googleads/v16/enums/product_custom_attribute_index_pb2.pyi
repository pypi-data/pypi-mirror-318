from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductCustomAttributeIndexEnum(_message.Message):
    __slots__ = ()

    class ProductCustomAttributeIndex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex]
        UNKNOWN: _ClassVar[ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex]
        INDEX0: _ClassVar[ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex]
        INDEX1: _ClassVar[ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex]
        INDEX2: _ClassVar[ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex]
        INDEX3: _ClassVar[ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex]
        INDEX4: _ClassVar[ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex]
    UNSPECIFIED: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    UNKNOWN: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    INDEX0: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    INDEX1: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    INDEX2: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    INDEX3: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    INDEX4: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex

    def __init__(self) -> None:
        ...