from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductTypeLevelEnum(_message.Message):
    __slots__ = ()

    class ProductTypeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductTypeLevelEnum.ProductTypeLevel]
        UNKNOWN: _ClassVar[ProductTypeLevelEnum.ProductTypeLevel]
        LEVEL1: _ClassVar[ProductTypeLevelEnum.ProductTypeLevel]
        LEVEL2: _ClassVar[ProductTypeLevelEnum.ProductTypeLevel]
        LEVEL3: _ClassVar[ProductTypeLevelEnum.ProductTypeLevel]
        LEVEL4: _ClassVar[ProductTypeLevelEnum.ProductTypeLevel]
        LEVEL5: _ClassVar[ProductTypeLevelEnum.ProductTypeLevel]
    UNSPECIFIED: ProductTypeLevelEnum.ProductTypeLevel
    UNKNOWN: ProductTypeLevelEnum.ProductTypeLevel
    LEVEL1: ProductTypeLevelEnum.ProductTypeLevel
    LEVEL2: ProductTypeLevelEnum.ProductTypeLevel
    LEVEL3: ProductTypeLevelEnum.ProductTypeLevel
    LEVEL4: ProductTypeLevelEnum.ProductTypeLevel
    LEVEL5: ProductTypeLevelEnum.ProductTypeLevel

    def __init__(self) -> None:
        ...