from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductChannelEnum(_message.Message):
    __slots__ = ()

    class ProductChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductChannelEnum.ProductChannel]
        UNKNOWN: _ClassVar[ProductChannelEnum.ProductChannel]
        ONLINE: _ClassVar[ProductChannelEnum.ProductChannel]
        LOCAL: _ClassVar[ProductChannelEnum.ProductChannel]
    UNSPECIFIED: ProductChannelEnum.ProductChannel
    UNKNOWN: ProductChannelEnum.ProductChannel
    ONLINE: ProductChannelEnum.ProductChannel
    LOCAL: ProductChannelEnum.ProductChannel

    def __init__(self) -> None:
        ...