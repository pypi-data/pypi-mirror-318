"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/waypoint.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routing.v2 import location_pb2 as google_dot_maps_dot_routing_dot_v2_dot_location__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/maps/routing/v2/waypoint.proto\x12\x16google.maps.routing.v2\x1a%google/maps/routing/v2/location.proto"\xb5\x01\n\x08Waypoint\x124\n\x08location\x18\x01 \x01(\x0b2 .google.maps.routing.v2.LocationH\x00\x12\x12\n\x08place_id\x18\x02 \x01(\tH\x00\x12\x11\n\x07address\x18\x07 \x01(\tH\x00\x12\x0b\n\x03via\x18\x03 \x01(\x08\x12\x18\n\x10vehicle_stopover\x18\x04 \x01(\x08\x12\x14\n\x0cside_of_road\x18\x05 \x01(\x08B\x0f\n\rlocation_typeB\xbf\x01\n\x1acom.google.maps.routing.v2B\rWaypointProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.waypoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\rWaypointProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_WAYPOINT']._serialized_start = 105
    _globals['_WAYPOINT']._serialized_end = 286