"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/vehicle_info.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routing.v2 import vehicle_emission_type_pb2 as google_dot_maps_dot_routing_dot_v2_dot_vehicle__emission__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/maps/routing/v2/vehicle_info.proto\x12\x16google.maps.routing.v2\x1a2google/maps/routing/v2/vehicle_emission_type.proto"Q\n\x0bVehicleInfo\x12B\n\remission_type\x18\x02 \x01(\x0e2+.google.maps.routing.v2.VehicleEmissionTypeB\xc5\x01\n\x1acom.google.maps.routing.v2B\x10VehicleInfoProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xf8\x01\x01\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.vehicle_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x10VehicleInfoProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xf8\x01\x01\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_VEHICLEINFO']._serialized_start = 121
    _globals['_VEHICLEINFO']._serialized_end = 202