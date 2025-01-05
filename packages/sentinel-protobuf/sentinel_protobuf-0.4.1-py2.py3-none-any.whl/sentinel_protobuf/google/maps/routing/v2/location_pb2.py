"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/location.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/maps/routing/v2/location.proto\x12\x16google.maps.routing.v2\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"^\n\x08Location\x12$\n\x07lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12,\n\x07heading\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\xbf\x01\n\x1acom.google.maps.routing.v2B\rLocationProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.location_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\rLocationProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_LOCATION']._serialized_start = 123
    _globals['_LOCATION']._serialized_end = 217