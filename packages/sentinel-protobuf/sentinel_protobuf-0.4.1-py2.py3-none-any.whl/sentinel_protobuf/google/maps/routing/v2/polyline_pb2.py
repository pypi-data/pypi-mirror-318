"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/polyline.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/maps/routing/v2/polyline.proto\x12\x16google.maps.routing.v2\x1a\x1cgoogle/protobuf/struct.proto"o\n\x08Polyline\x12\x1a\n\x10encoded_polyline\x18\x01 \x01(\tH\x00\x126\n\x13geo_json_linestring\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00B\x0f\n\rpolyline_type*S\n\x0fPolylineQuality\x12 \n\x1cPOLYLINE_QUALITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cHIGH_QUALITY\x10\x01\x12\x0c\n\x08OVERVIEW\x10\x02*d\n\x10PolylineEncoding\x12!\n\x1dPOLYLINE_ENCODING_UNSPECIFIED\x10\x00\x12\x14\n\x10ENCODED_POLYLINE\x10\x01\x12\x17\n\x13GEO_JSON_LINESTRING\x10\x02B\xbf\x01\n\x1acom.google.maps.routing.v2B\rPolylineProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.polyline_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\rPolylineProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_POLYLINEQUALITY']._serialized_start = 208
    _globals['_POLYLINEQUALITY']._serialized_end = 291
    _globals['_POLYLINEENCODING']._serialized_start = 293
    _globals['_POLYLINEENCODING']._serialized_end = 393
    _globals['_POLYLINE']._serialized_start = 95
    _globals['_POLYLINE']._serialized_end = 206