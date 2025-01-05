"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/compute_routes_request.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.routes.v1 import polyline_pb2 as google_dot_maps_dot_routes_dot_v1_dot_polyline__pb2
from .....google.maps.routes.v1 import toll_passes_pb2 as google_dot_maps_dot_routes_dot_v1_dot_toll__passes__pb2
from .....google.maps.routes.v1 import vehicle_emission_type_pb2 as google_dot_maps_dot_routes_dot_v1_dot_vehicle__emission__type__pb2
from .....google.maps.routes.v1 import waypoint_pb2 as google_dot_maps_dot_routes_dot_v1_dot_waypoint__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/maps/routes/v1/compute_routes_request.proto\x12\x15google.maps.routes.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a$google/maps/routes/v1/polyline.proto\x1a\'google/maps/routes/v1/toll_passes.proto\x1a1google/maps/routes/v1/vehicle_emission_type.proto\x1a$google/maps/routes/v1/waypoint.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbb\x05\n\x14ComputeRoutesRequest\x12/\n\x06origin\x18\x01 \x01(\x0b2\x1f.google.maps.routes.v1.Waypoint\x124\n\x0bdestination\x18\x02 \x01(\x0b2\x1f.google.maps.routes.v1.Waypoint\x126\n\rintermediates\x18\x03 \x03(\x0b2\x1f.google.maps.routes.v1.Waypoint\x12;\n\x0btravel_mode\x18\x04 \x01(\x0e2&.google.maps.routes.v1.RouteTravelMode\x12D\n\x12routing_preference\x18\x05 \x01(\x0e2(.google.maps.routes.v1.RoutingPreference\x12@\n\x10polyline_quality\x18\x06 \x01(\x0e2&.google.maps.routes.v1.PolylineQuality\x12B\n\x11polyline_encoding\x18\x0c \x01(\x0e2\'.google.maps.routes.v1.PolylineEncoding\x122\n\x0edeparture_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12"\n\x1acompute_alternative_routes\x18\x08 \x01(\x08\x12>\n\x0froute_modifiers\x18\t \x01(\x0b2%.google.maps.routes.v1.RouteModifiers\x12\x15\n\rlanguage_code\x18\n \x01(\t\x12+\n\x05units\x18\x0b \x01(\x0e2\x1c.google.maps.routes.v1.Units\x12\x1f\n\x17optimize_waypoint_order\x18\r \x01(\x08"\xda\x01\n\x0eRouteModifiers\x12\x13\n\x0bavoid_tolls\x18\x01 \x01(\x08\x12\x16\n\x0eavoid_highways\x18\x02 \x01(\x08\x12\x15\n\ravoid_ferries\x18\x03 \x01(\x08\x12\x14\n\x0cavoid_indoor\x18\x04 \x01(\x08\x128\n\x0cvehicle_info\x18\x05 \x01(\x0b2".google.maps.routes.v1.VehicleInfo\x124\n\x0btoll_passes\x18\x06 \x03(\x0e2\x1f.google.maps.routes.v1.TollPass"v\n\x0bVehicleInfo\x12$\n\x1clicense_plate_last_character\x18\x01 \x01(\t\x12A\n\remission_type\x18\x02 \x01(\x0e2*.google.maps.routes.v1.VehicleEmissionType*k\n\x0fRouteTravelMode\x12\x1b\n\x17TRAVEL_MODE_UNSPECIFIED\x10\x00\x12\t\n\x05DRIVE\x10\x01\x12\x0b\n\x07BICYCLE\x10\x02\x12\x08\n\x04WALK\x10\x03\x12\x0f\n\x0bTWO_WHEELER\x10\x04\x12\x08\n\x04TAXI\x10\x05*z\n\x11RoutingPreference\x12"\n\x1eROUTING_PREFERENCE_UNSPECIFIED\x10\x00\x12\x13\n\x0fTRAFFIC_UNAWARE\x10\x01\x12\x11\n\rTRAFFIC_AWARE\x10\x02\x12\x19\n\x15TRAFFIC_AWARE_OPTIMAL\x10\x03*8\n\x05Units\x12\x15\n\x11UNITS_UNSPECIFIED\x10\x00\x12\n\n\x06METRIC\x10\x01\x12\x0c\n\x08IMPERIAL\x10\x02B\xa8\x01\n\x19com.google.maps.routes.v1B\x19ComputeRoutesRequestProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.compute_routes_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B\x19ComputeRoutesRequestProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_ROUTETRAVELMODE']._serialized_start = 1354
    _globals['_ROUTETRAVELMODE']._serialized_end = 1461
    _globals['_ROUTINGPREFERENCE']._serialized_start = 1463
    _globals['_ROUTINGPREFERENCE']._serialized_end = 1585
    _globals['_UNITS']._serialized_start = 1587
    _globals['_UNITS']._serialized_end = 1643
    _globals['_COMPUTEROUTESREQUEST']._serialized_start = 312
    _globals['_COMPUTEROUTESREQUEST']._serialized_end = 1011
    _globals['_ROUTEMODIFIERS']._serialized_start = 1014
    _globals['_ROUTEMODIFIERS']._serialized_end = 1232
    _globals['_VEHICLEINFO']._serialized_start = 1234
    _globals['_VEHICLEINFO']._serialized_end = 1352