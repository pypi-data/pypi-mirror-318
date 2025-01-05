from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class JsonExtension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON_EXTENSION_UNSPECIFIED: _ClassVar[JsonExtension]
    GEOJSON: _ClassVar[JsonExtension]
JSON_EXTENSION_UNSPECIFIED: JsonExtension
GEOJSON: JsonExtension