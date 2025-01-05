"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/route_matrix_element.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routes.v1 import fallback_info_pb2 as google_dot_maps_dot_routes_dot_v1_dot_fallback__info__pb2
from .....google.maps.routes.v1 import route_pb2 as google_dot_maps_dot_routes_dot_v1_dot_route__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/maps/routes/v1/route_matrix_element.proto\x12\x15google.maps.routes.v1\x1a)google/maps/routes/v1/fallback_info.proto\x1a!google/maps/routes/v1/route.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto"\xab\x03\n\x12RouteMatrixElement\x12\x14\n\x0corigin_index\x18\x01 \x01(\x05\x12\x19\n\x11destination_index\x18\x02 \x01(\x05\x12"\n\x06status\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12E\n\tcondition\x18\t \x01(\x0e22.google.maps.routes.v1.RouteMatrixElementCondition\x12\x17\n\x0fdistance_meters\x18\x04 \x01(\x05\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fstatic_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12C\n\x0ftravel_advisory\x18\x07 \x01(\x0b2*.google.maps.routes.v1.RouteTravelAdvisory\x12:\n\rfallback_info\x18\x08 \x01(\x0b2#.google.maps.routes.v1.FallbackInfo*t\n\x1bRouteMatrixElementCondition\x12.\n*ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED\x10\x00\x12\x10\n\x0cROUTE_EXISTS\x10\x01\x12\x13\n\x0fROUTE_NOT_FOUND\x10\x02B\xad\x01\n\x19com.google.maps.routes.v1B\x1eComputeRouteMatrixElementProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.route_matrix_element_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B\x1eComputeRouteMatrixElementProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_ROUTEMATRIXELEMENTCONDITION']._serialized_start = 640
    _globals['_ROUTEMATRIXELEMENTCONDITION']._serialized_end = 756
    _globals['_ROUTEMATRIXELEMENT']._serialized_start = 211
    _globals['_ROUTEMATRIXELEMENT']._serialized_end = 638