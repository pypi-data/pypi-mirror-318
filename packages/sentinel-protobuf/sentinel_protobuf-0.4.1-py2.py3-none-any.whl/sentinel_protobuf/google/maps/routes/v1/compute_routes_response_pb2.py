"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/compute_routes_response.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routes.v1 import fallback_info_pb2 as google_dot_maps_dot_routes_dot_v1_dot_fallback__info__pb2
from .....google.maps.routes.v1 import route_pb2 as google_dot_maps_dot_routes_dot_v1_dot_route__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/maps/routes/v1/compute_routes_response.proto\x12\x15google.maps.routes.v1\x1a)google/maps/routes/v1/fallback_info.proto\x1a!google/maps/routes/v1/route.proto"\x81\x01\n\x15ComputeRoutesResponse\x12,\n\x06routes\x18\x01 \x03(\x0b2\x1c.google.maps.routes.v1.Route\x12:\n\rfallback_info\x18\x02 \x01(\x0b2#.google.maps.routes.v1.FallbackInfoB\xa9\x01\n\x19com.google.maps.routes.v1B\x1aComputeRoutesResponseProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.compute_routes_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B\x1aComputeRoutesResponseProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_COMPUTEROUTESRESPONSE']._serialized_start = 157
    _globals['_COMPUTEROUTESRESPONSE']._serialized_end = 286