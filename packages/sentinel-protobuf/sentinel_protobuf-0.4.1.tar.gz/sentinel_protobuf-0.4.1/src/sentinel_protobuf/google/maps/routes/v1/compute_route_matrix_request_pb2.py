"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/compute_route_matrix_request.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.routes.v1 import compute_routes_request_pb2 as google_dot_maps_dot_routes_dot_v1_dot_compute__routes__request__pb2
from .....google.maps.routes.v1 import waypoint_pb2 as google_dot_maps_dot_routes_dot_v1_dot_waypoint__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/maps/routes/v1/compute_route_matrix_request.proto\x12\x15google.maps.routes.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a2google/maps/routes/v1/compute_routes_request.proto\x1a$google/maps/routes/v1/waypoint.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xeb\x02\n\x19ComputeRouteMatrixRequest\x12>\n\x07origins\x18\x01 \x03(\x0b2(.google.maps.routes.v1.RouteMatrixOriginB\x03\xe0A\x02\x12H\n\x0cdestinations\x18\x02 \x03(\x0b2-.google.maps.routes.v1.RouteMatrixDestinationB\x03\xe0A\x02\x12@\n\x0btravel_mode\x18\x03 \x01(\x0e2&.google.maps.routes.v1.RouteTravelModeB\x03\xe0A\x01\x12I\n\x12routing_preference\x18\x04 \x01(\x0e2(.google.maps.routes.v1.RoutingPreferenceB\x03\xe0A\x01\x127\n\x0edeparture_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"\x90\x01\n\x11RouteMatrixOrigin\x126\n\x08waypoint\x18\x01 \x01(\x0b2\x1f.google.maps.routes.v1.WaypointB\x03\xe0A\x02\x12C\n\x0froute_modifiers\x18\x02 \x01(\x0b2%.google.maps.routes.v1.RouteModifiersB\x03\xe0A\x01"P\n\x16RouteMatrixDestination\x126\n\x08waypoint\x18\x01 \x01(\x0b2\x1f.google.maps.routes.v1.WaypointB\x03\xe0A\x02B\xad\x01\n\x19com.google.maps.routes.v1B\x1eComputeRouteMatrixRequestProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.compute_route_matrix_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B\x1eComputeRouteMatrixRequestProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['origins']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['origins']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['destinations']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['destinations']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['travel_mode']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['travel_mode']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['routing_preference']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['routing_preference']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['departure_time']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['departure_time']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['waypoint']._loaded_options = None
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['waypoint']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['route_modifiers']._loaded_options = None
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['route_modifiers']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEMATRIXDESTINATION'].fields_by_name['waypoint']._loaded_options = None
    _globals['_ROUTEMATRIXDESTINATION'].fields_by_name['waypoint']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEROUTEMATRIXREQUEST']._serialized_start = 240
    _globals['_COMPUTEROUTEMATRIXREQUEST']._serialized_end = 603
    _globals['_ROUTEMATRIXORIGIN']._serialized_start = 606
    _globals['_ROUTEMATRIXORIGIN']._serialized_end = 750
    _globals['_ROUTEMATRIXDESTINATION']._serialized_start = 752
    _globals['_ROUTEMATRIXDESTINATION']._serialized_end = 832