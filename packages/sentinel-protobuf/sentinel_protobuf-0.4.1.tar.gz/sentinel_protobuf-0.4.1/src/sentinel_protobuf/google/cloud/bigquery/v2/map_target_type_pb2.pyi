from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MapTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAP_TARGET_TYPE_UNSPECIFIED: _ClassVar[MapTargetType]
    ARRAY_OF_STRUCT: _ClassVar[MapTargetType]
MAP_TARGET_TYPE_UNSPECIFIED: MapTargetType
ARRAY_OF_STRUCT: MapTargetType