from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductBiddingCategoryStatusEnum(_message.Message):
    __slots__ = ()

    class ProductBiddingCategoryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus]
        UNKNOWN: _ClassVar[ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus]
        ACTIVE: _ClassVar[ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus]
        OBSOLETE: _ClassVar[ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus]
    UNSPECIFIED: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus
    UNKNOWN: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus
    ACTIVE: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus
    OBSOLETE: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus

    def __init__(self) -> None:
        ...