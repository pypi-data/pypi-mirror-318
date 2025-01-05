from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductStatusEnum(_message.Message):
    __slots__ = ()

    class ProductStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductStatusEnum.ProductStatus]
        UNKNOWN: _ClassVar[ProductStatusEnum.ProductStatus]
        NOT_ELIGIBLE: _ClassVar[ProductStatusEnum.ProductStatus]
        ELIGIBLE_LIMITED: _ClassVar[ProductStatusEnum.ProductStatus]
        ELIGIBLE: _ClassVar[ProductStatusEnum.ProductStatus]
    UNSPECIFIED: ProductStatusEnum.ProductStatus
    UNKNOWN: ProductStatusEnum.ProductStatus
    NOT_ELIGIBLE: ProductStatusEnum.ProductStatus
    ELIGIBLE_LIMITED: ProductStatusEnum.ProductStatus
    ELIGIBLE: ProductStatusEnum.ProductStatus

    def __init__(self) -> None:
        ...