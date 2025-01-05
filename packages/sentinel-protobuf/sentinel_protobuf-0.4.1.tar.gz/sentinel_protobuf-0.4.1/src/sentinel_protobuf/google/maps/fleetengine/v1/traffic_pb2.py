"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/v1/traffic.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/maps/fleetengine/v1/traffic.proto\x12\x13maps.fleetengine.v1"\xe3\x01\n\x14SpeedReadingInterval\x12"\n\x1astart_polyline_point_index\x18\x01 \x01(\x05\x12 \n\x18end_polyline_point_index\x18\x02 \x01(\x05\x12>\n\x05speed\x18\x03 \x01(\x0e2/.maps.fleetengine.v1.SpeedReadingInterval.Speed"E\n\x05Speed\x12\x15\n\x11SPEED_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04SLOW\x10\x02\x12\x0f\n\x0bTRAFFIC_JAM\x10\x03"\x88\x01\n\x19ConsumableTrafficPolyline\x12I\n\x16speed_reading_interval\x18\x01 \x03(\x0b2).maps.fleetengine.v1.SpeedReadingInterval\x12 \n\x18encoded_path_to_waypoint\x18\x02 \x01(\tB\xd8\x01\n\x1ecom.google.maps.fleetengine.v1B\x0cTrafficProtoP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.v1.traffic_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.maps.fleetengine.v1B\x0cTrafficProtoP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1'
    _globals['_SPEEDREADINGINTERVAL']._serialized_start = 66
    _globals['_SPEEDREADINGINTERVAL']._serialized_end = 293
    _globals['_SPEEDREADINGINTERVAL_SPEED']._serialized_start = 224
    _globals['_SPEEDREADINGINTERVAL_SPEED']._serialized_end = 293
    _globals['_CONSUMABLETRAFFICPOLYLINE']._serialized_start = 296
    _globals['_CONSUMABLETRAFFICPOLYLINE']._serialized_end = 432