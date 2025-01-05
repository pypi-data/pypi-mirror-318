from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductCategoryStateEnum(_message.Message):
    __slots__ = ()

    class ProductCategoryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductCategoryStateEnum.ProductCategoryState]
        UNKNOWN: _ClassVar[ProductCategoryStateEnum.ProductCategoryState]
        ENABLED: _ClassVar[ProductCategoryStateEnum.ProductCategoryState]
        OBSOLETE: _ClassVar[ProductCategoryStateEnum.ProductCategoryState]
    UNSPECIFIED: ProductCategoryStateEnum.ProductCategoryState
    UNKNOWN: ProductCategoryStateEnum.ProductCategoryState
    ENABLED: ProductCategoryStateEnum.ProductCategoryState
    OBSOLETE: ProductCategoryStateEnum.ProductCategoryState

    def __init__(self) -> None:
        ...