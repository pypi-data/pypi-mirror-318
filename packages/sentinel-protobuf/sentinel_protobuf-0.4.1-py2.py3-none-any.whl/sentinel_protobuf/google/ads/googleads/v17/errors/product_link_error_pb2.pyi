from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductLinkErrorEnum(_message.Message):
    __slots__ = ()

    class ProductLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductLinkErrorEnum.ProductLinkError]
        UNKNOWN: _ClassVar[ProductLinkErrorEnum.ProductLinkError]
        INVALID_OPERATION: _ClassVar[ProductLinkErrorEnum.ProductLinkError]
        CREATION_NOT_PERMITTED: _ClassVar[ProductLinkErrorEnum.ProductLinkError]
        INVITATION_EXISTS: _ClassVar[ProductLinkErrorEnum.ProductLinkError]
        LINK_EXISTS: _ClassVar[ProductLinkErrorEnum.ProductLinkError]
    UNSPECIFIED: ProductLinkErrorEnum.ProductLinkError
    UNKNOWN: ProductLinkErrorEnum.ProductLinkError
    INVALID_OPERATION: ProductLinkErrorEnum.ProductLinkError
    CREATION_NOT_PERMITTED: ProductLinkErrorEnum.ProductLinkError
    INVITATION_EXISTS: ProductLinkErrorEnum.ProductLinkError
    LINK_EXISTS: ProductLinkErrorEnum.ProductLinkError

    def __init__(self) -> None:
        ...