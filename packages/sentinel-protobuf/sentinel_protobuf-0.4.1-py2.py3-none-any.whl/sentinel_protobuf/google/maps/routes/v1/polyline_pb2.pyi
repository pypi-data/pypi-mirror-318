from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PolylineQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLYLINE_QUALITY_UNSPECIFIED: _ClassVar[PolylineQuality]
    HIGH_QUALITY: _ClassVar[PolylineQuality]
    OVERVIEW: _ClassVar[PolylineQuality]

class PolylineEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLYLINE_ENCODING_UNSPECIFIED: _ClassVar[PolylineEncoding]
    ENCODED_POLYLINE: _ClassVar[PolylineEncoding]
    GEO_JSON_LINESTRING: _ClassVar[PolylineEncoding]
POLYLINE_QUALITY_UNSPECIFIED: PolylineQuality
HIGH_QUALITY: PolylineQuality
OVERVIEW: PolylineQuality
POLYLINE_ENCODING_UNSPECIFIED: PolylineEncoding
ENCODED_POLYLINE: PolylineEncoding
GEO_JSON_LINESTRING: PolylineEncoding

class Polyline(_message.Message):
    __slots__ = ('encoded_polyline', 'geo_json_linestring')
    ENCODED_POLYLINE_FIELD_NUMBER: _ClassVar[int]
    GEO_JSON_LINESTRING_FIELD_NUMBER: _ClassVar[int]
    encoded_polyline: str
    geo_json_linestring: _struct_pb2.Struct

    def __init__(self, encoded_polyline: _Optional[str]=..., geo_json_linestring: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...