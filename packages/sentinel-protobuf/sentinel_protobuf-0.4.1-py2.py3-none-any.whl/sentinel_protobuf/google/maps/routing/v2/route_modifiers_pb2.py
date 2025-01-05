"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/route_modifiers.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routing.v2 import toll_passes_pb2 as google_dot_maps_dot_routing_dot_v2_dot_toll__passes__pb2
from .....google.maps.routing.v2 import vehicle_info_pb2 as google_dot_maps_dot_routing_dot_v2_dot_vehicle__info__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/maps/routing/v2/route_modifiers.proto\x12\x16google.maps.routing.v2\x1a(google/maps/routing/v2/toll_passes.proto\x1a)google/maps/routing/v2/vehicle_info.proto"\xdc\x01\n\x0eRouteModifiers\x12\x13\n\x0bavoid_tolls\x18\x01 \x01(\x08\x12\x16\n\x0eavoid_highways\x18\x02 \x01(\x08\x12\x15\n\ravoid_ferries\x18\x03 \x01(\x08\x12\x14\n\x0cavoid_indoor\x18\x04 \x01(\x08\x129\n\x0cvehicle_info\x18\x05 \x01(\x0b2#.google.maps.routing.v2.VehicleInfo\x125\n\x0btoll_passes\x18\x06 \x03(\x0e2 .google.maps.routing.v2.TollPassB\xc5\x01\n\x1acom.google.maps.routing.v2B\x13RouteModifiersProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.route_modifiers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x13RouteModifiersProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_ROUTEMODIFIERS']._serialized_start = 158
    _globals['_ROUTEMODIFIERS']._serialized_end = 378