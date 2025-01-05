from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductCategoryLevelEnum(_message.Message):
    __slots__ = ()

    class ProductCategoryLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductCategoryLevelEnum.ProductCategoryLevel]
        UNKNOWN: _ClassVar[ProductCategoryLevelEnum.ProductCategoryLevel]
        LEVEL1: _ClassVar[ProductCategoryLevelEnum.ProductCategoryLevel]
        LEVEL2: _ClassVar[ProductCategoryLevelEnum.ProductCategoryLevel]
        LEVEL3: _ClassVar[ProductCategoryLevelEnum.ProductCategoryLevel]
        LEVEL4: _ClassVar[ProductCategoryLevelEnum.ProductCategoryLevel]
        LEVEL5: _ClassVar[ProductCategoryLevelEnum.ProductCategoryLevel]
    UNSPECIFIED: ProductCategoryLevelEnum.ProductCategoryLevel
    UNKNOWN: ProductCategoryLevelEnum.ProductCategoryLevel
    LEVEL1: ProductCategoryLevelEnum.ProductCategoryLevel
    LEVEL2: ProductCategoryLevelEnum.ProductCategoryLevel
    LEVEL3: ProductCategoryLevelEnum.ProductCategoryLevel
    LEVEL4: ProductCategoryLevelEnum.ProductCategoryLevel
    LEVEL5: ProductCategoryLevelEnum.ProductCategoryLevel

    def __init__(self) -> None:
        ...