from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductBiddingCategoryLevelEnum(_message.Message):
    __slots__ = ()

    class ProductBiddingCategoryLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel]
        UNKNOWN: _ClassVar[ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel]
        LEVEL1: _ClassVar[ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel]
        LEVEL2: _ClassVar[ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel]
        LEVEL3: _ClassVar[ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel]
        LEVEL4: _ClassVar[ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel]
        LEVEL5: _ClassVar[ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel]
    UNSPECIFIED: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    UNKNOWN: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    LEVEL1: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    LEVEL2: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    LEVEL3: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    LEVEL4: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    LEVEL5: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel

    def __init__(self) -> None:
        ...