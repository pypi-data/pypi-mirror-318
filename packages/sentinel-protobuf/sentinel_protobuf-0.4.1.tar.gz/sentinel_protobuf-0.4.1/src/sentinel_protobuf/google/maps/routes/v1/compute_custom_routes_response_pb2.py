"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/compute_custom_routes_response.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routes.v1 import custom_route_pb2 as google_dot_maps_dot_routes_dot_v1_dot_custom__route__pb2
from .....google.maps.routes.v1 import fallback_info_pb2 as google_dot_maps_dot_routes_dot_v1_dot_fallback__info__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/maps/routes/v1/compute_custom_routes_response.proto\x12\x15google.maps.routes.v1\x1a(google/maps/routes/v1/custom_route.proto\x1a)google/maps/routes/v1/fallback_info.proto"\x9b\x05\n\x1bComputeCustomRoutesResponse\x122\n\x06routes\x18\x07 \x03(\x0b2".google.maps.routes.v1.CustomRoute\x129\n\rfastest_route\x18\x05 \x01(\x0b2".google.maps.routes.v1.CustomRoute\x12:\n\x0eshortest_route\x18\x06 \x01(\x0b2".google.maps.routes.v1.CustomRoute\x12V\n\rfallback_info\x18\x08 \x01(\x0b2?.google.maps.routes.v1.ComputeCustomRoutesResponse.FallbackInfo\x1a\xf8\x02\n\x0cFallbackInfo\x12@\n\x0crouting_mode\x18\x01 \x01(\x0e2*.google.maps.routes.v1.FallbackRoutingMode\x12B\n\x13routing_mode_reason\x18\x02 \x01(\x0e2%.google.maps.routes.v1.FallbackReason\x12o\n\x0froute_objective\x18\x03 \x01(\x0e2V.google.maps.routes.v1.ComputeCustomRoutesResponse.FallbackInfo.FallbackRouteObjective"q\n\x16FallbackRouteObjective\x12(\n$FALLBACK_ROUTE_OBJECTIVE_UNSPECIFIED\x10\x00\x12-\n)FALLBACK_RATECARD_WITHOUT_TOLL_PRICE_DATA\x10\x01B\xaf\x01\n\x19com.google.maps.routes.v1B ComputeCustomRoutesResponseProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.compute_custom_routes_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B ComputeCustomRoutesResponseProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_COMPUTECUSTOMROUTESRESPONSE']._serialized_start = 171
    _globals['_COMPUTECUSTOMROUTESRESPONSE']._serialized_end = 838
    _globals['_COMPUTECUSTOMROUTESRESPONSE_FALLBACKINFO']._serialized_start = 462
    _globals['_COMPUTECUSTOMROUTESRESPONSE_FALLBACKINFO']._serialized_end = 838
    _globals['_COMPUTECUSTOMROUTESRESPONSE_FALLBACKINFO_FALLBACKROUTEOBJECTIVE']._serialized_start = 725
    _globals['_COMPUTECUSTOMROUTESRESPONSE_FALLBACKINFO_FALLBACKROUTEOBJECTIVE']._serialized_end = 838