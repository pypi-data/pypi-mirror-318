"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1alpha/route_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.maps.routes.v1 import compute_custom_routes_request_pb2 as google_dot_maps_dot_routes_dot_v1_dot_compute__custom__routes__request__pb2
from .....google.maps.routes.v1 import compute_custom_routes_response_pb2 as google_dot_maps_dot_routes_dot_v1_dot_compute__custom__routes__response__pb2
from .....google.maps.routes.v1 import compute_route_matrix_request_pb2 as google_dot_maps_dot_routes_dot_v1_dot_compute__route__matrix__request__pb2
from .....google.maps.routes.v1 import compute_routes_request_pb2 as google_dot_maps_dot_routes_dot_v1_dot_compute__routes__request__pb2
from .....google.maps.routes.v1 import compute_routes_response_pb2 as google_dot_maps_dot_routes_dot_v1_dot_compute__routes__response__pb2
from .....google.maps.routes.v1 import route_matrix_element_pb2 as google_dot_maps_dot_routes_dot_v1_dot_route__matrix__element__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/maps/routes/v1alpha/route_service.proto\x12\x1agoogle.maps.routes.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a9google/maps/routes/v1/compute_custom_routes_request.proto\x1a:google/maps/routes/v1/compute_custom_routes_response.proto\x1a8google/maps/routes/v1/compute_route_matrix_request.proto\x1a2google/maps/routes/v1/compute_routes_request.proto\x1a3google/maps/routes/v1/compute_routes_response.proto\x1a0google/maps/routes/v1/route_matrix_element.proto2\xc6\x04\n\x0bRoutesAlpha\x12\x8d\x01\n\rComputeRoutes\x12+.google.maps.routes.v1.ComputeRoutesRequest\x1a,.google.maps.routes.v1.ComputeRoutesResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/v1alpha:computeRoutes:\x01*\x12\x9b\x01\n\x12ComputeRouteMatrix\x120.google.maps.routes.v1.ComputeRouteMatrixRequest\x1a).google.maps.routes.v1.RouteMatrixElement"&\x82\xd3\xe4\x93\x02 "\x1b/v1alpha:computeRouteMatrix:\x01*0\x01\x12\xa5\x01\n\x13ComputeCustomRoutes\x121.google.maps.routes.v1.ComputeCustomRoutesRequest\x1a2.google.maps.routes.v1.ComputeCustomRoutesResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/v1alpha:computeCustomRoutes:\x01*\x1aa\xcaA\x1eroutespreferred.googleapis.com\xd2A=https://www.googleapis.com/auth/maps-platform.routespreferredB\xba\x01\n\x1ecom.google.maps.routes.v1alphaB\x17RoutesServiceAlphaProtoP\x01Z<cloud.google.com/go/maps/routes/apiv1alpha/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x1aGoogle.Maps.Routes.V1Alpha\xca\x02\x1aGoogle\\Maps\\Routes\\V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1alpha.route_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.maps.routes.v1alphaB\x17RoutesServiceAlphaProtoP\x01Z<cloud.google.com/go/maps/routes/apiv1alpha/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x1aGoogle.Maps.Routes.V1Alpha\xca\x02\x1aGoogle\\Maps\\Routes\\V1alpha'
    _globals['_ROUTESALPHA']._loaded_options = None
    _globals['_ROUTESALPHA']._serialized_options = b'\xcaA\x1eroutespreferred.googleapis.com\xd2A=https://www.googleapis.com/auth/maps-platform.routespreferred'
    _globals['_ROUTESALPHA'].methods_by_name['ComputeRoutes']._loaded_options = None
    _globals['_ROUTESALPHA'].methods_by_name['ComputeRoutes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/v1alpha:computeRoutes:\x01*'
    _globals['_ROUTESALPHA'].methods_by_name['ComputeRouteMatrix']._loaded_options = None
    _globals['_ROUTESALPHA'].methods_by_name['ComputeRouteMatrix']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/v1alpha:computeRouteMatrix:\x01*'
    _globals['_ROUTESALPHA'].methods_by_name['ComputeCustomRoutes']._loaded_options = None
    _globals['_ROUTESALPHA'].methods_by_name['ComputeCustomRoutes']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/v1alpha:computeCustomRoutes:\x01*'
    _globals['_ROUTESALPHA']._serialized_start = 466
    _globals['_ROUTESALPHA']._serialized_end = 1048