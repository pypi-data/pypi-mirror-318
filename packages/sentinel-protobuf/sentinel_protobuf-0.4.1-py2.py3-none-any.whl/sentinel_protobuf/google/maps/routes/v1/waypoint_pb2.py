"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/waypoint.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/maps/routes/v1/waypoint.proto\x12\x15google.maps.routes.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\xa1\x01\n\x08Waypoint\x123\n\x08location\x18\x01 \x01(\x0b2\x1f.google.maps.routes.v1.LocationH\x00\x12\x12\n\x08place_id\x18\x02 \x01(\tH\x00\x12\x0b\n\x03via\x18\x03 \x01(\x08\x12\x18\n\x10vehicle_stopover\x18\x04 \x01(\x08\x12\x14\n\x0cside_of_road\x18\x05 \x01(\x08B\x0f\n\rlocation_type"^\n\x08Location\x12$\n\x07lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12,\n\x07heading\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x9c\x01\n\x19com.google.maps.routes.v1B\rWaypointProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.waypoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B\rWaypointProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_WAYPOINT']._serialized_start = 122
    _globals['_WAYPOINT']._serialized_end = 283
    _globals['_LOCATION']._serialized_start = 285
    _globals['_LOCATION']._serialized_end = 379