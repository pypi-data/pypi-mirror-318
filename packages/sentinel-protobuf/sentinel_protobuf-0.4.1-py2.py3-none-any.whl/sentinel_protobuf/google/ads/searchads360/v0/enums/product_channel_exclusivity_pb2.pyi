from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductChannelExclusivityEnum(_message.Message):
    __slots__ = ()

    class ProductChannelExclusivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductChannelExclusivityEnum.ProductChannelExclusivity]
        UNKNOWN: _ClassVar[ProductChannelExclusivityEnum.ProductChannelExclusivity]
        SINGLE_CHANNEL: _ClassVar[ProductChannelExclusivityEnum.ProductChannelExclusivity]
        MULTI_CHANNEL: _ClassVar[ProductChannelExclusivityEnum.ProductChannelExclusivity]
    UNSPECIFIED: ProductChannelExclusivityEnum.ProductChannelExclusivity
    UNKNOWN: ProductChannelExclusivityEnum.ProductChannelExclusivity
    SINGLE_CHANNEL: ProductChannelExclusivityEnum.ProductChannelExclusivity
    MULTI_CHANNEL: ProductChannelExclusivityEnum.ProductChannelExclusivity

    def __init__(self) -> None:
        ...