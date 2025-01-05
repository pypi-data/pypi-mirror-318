from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccessRight(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_RIGHT_UNSPECIFIED: _ClassVar[AccessRight]
    STANDARD: _ClassVar[AccessRight]
    ADMIN: _ClassVar[AccessRight]
    PERFORMANCE_REPORTING: _ClassVar[AccessRight]
ACCESS_RIGHT_UNSPECIFIED: AccessRight
STANDARD: AccessRight
ADMIN: AccessRight
PERFORMANCE_REPORTING: AccessRight