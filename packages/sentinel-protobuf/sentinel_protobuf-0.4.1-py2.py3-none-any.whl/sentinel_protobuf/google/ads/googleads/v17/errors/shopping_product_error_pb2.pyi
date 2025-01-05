from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ShoppingProductErrorEnum(_message.Message):
    __slots__ = ()

    class ShoppingProductError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ShoppingProductErrorEnum.ShoppingProductError]
        UNKNOWN: _ClassVar[ShoppingProductErrorEnum.ShoppingProductError]
        MISSING_CAMPAIGN_FILTER: _ClassVar[ShoppingProductErrorEnum.ShoppingProductError]
        MISSING_AD_GROUP_FILTER: _ClassVar[ShoppingProductErrorEnum.ShoppingProductError]
        UNSUPPORTED_DATE_SEGMENTATION: _ClassVar[ShoppingProductErrorEnum.ShoppingProductError]
    UNSPECIFIED: ShoppingProductErrorEnum.ShoppingProductError
    UNKNOWN: ShoppingProductErrorEnum.ShoppingProductError
    MISSING_CAMPAIGN_FILTER: ShoppingProductErrorEnum.ShoppingProductError
    MISSING_AD_GROUP_FILTER: ShoppingProductErrorEnum.ShoppingProductError
    UNSUPPORTED_DATE_SEGMENTATION: ShoppingProductErrorEnum.ShoppingProductError

    def __init__(self) -> None:
        ...