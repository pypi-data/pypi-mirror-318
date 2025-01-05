from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductConditionEnum(_message.Message):
    __slots__ = ()

    class ProductCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductConditionEnum.ProductCondition]
        UNKNOWN: _ClassVar[ProductConditionEnum.ProductCondition]
        OLD: _ClassVar[ProductConditionEnum.ProductCondition]
        NEW: _ClassVar[ProductConditionEnum.ProductCondition]
        REFURBISHED: _ClassVar[ProductConditionEnum.ProductCondition]
        USED: _ClassVar[ProductConditionEnum.ProductCondition]
    UNSPECIFIED: ProductConditionEnum.ProductCondition
    UNKNOWN: ProductConditionEnum.ProductCondition
    OLD: ProductConditionEnum.ProductCondition
    NEW: ProductConditionEnum.ProductCondition
    REFURBISHED: ProductConditionEnum.ProductCondition
    USED: ProductConditionEnum.ProductCondition

    def __init__(self) -> None:
        ...