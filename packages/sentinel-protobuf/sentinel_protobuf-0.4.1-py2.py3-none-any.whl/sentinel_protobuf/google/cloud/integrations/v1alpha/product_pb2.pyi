from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class Product(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_UNSPECIFIED: _ClassVar[Product]
    IP: _ClassVar[Product]
    APIGEE: _ClassVar[Product]
    SECURITY: _ClassVar[Product]
PRODUCT_UNSPECIFIED: Product
IP: Product
APIGEE: Product
SECURITY: Product