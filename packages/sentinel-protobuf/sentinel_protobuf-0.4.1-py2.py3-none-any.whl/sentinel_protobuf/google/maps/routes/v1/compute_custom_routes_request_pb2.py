"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/compute_custom_routes_request.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.routes.v1 import compute_routes_request_pb2 as google_dot_maps_dot_routes_dot_v1_dot_compute__routes__request__pb2
from .....google.maps.routes.v1 import polyline_pb2 as google_dot_maps_dot_routes_dot_v1_dot_polyline__pb2
from .....google.maps.routes.v1 import waypoint_pb2 as google_dot_maps_dot_routes_dot_v1_dot_waypoint__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/maps/routes/v1/compute_custom_routes_request.proto\x12\x15google.maps.routes.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a2google/maps/routes/v1/compute_routes_request.proto\x1a$google/maps/routes/v1/polyline.proto\x1a$google/maps/routes/v1/waypoint.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf8\x05\n\x1aComputeCustomRoutesRequest\x124\n\x06origin\x18\x01 \x01(\x0b2\x1f.google.maps.routes.v1.WaypointB\x03\xe0A\x02\x129\n\x0bdestination\x18\x02 \x01(\x0b2\x1f.google.maps.routes.v1.WaypointB\x03\xe0A\x02\x12;\n\rintermediates\x18\x03 \x03(\x0b2\x1f.google.maps.routes.v1.WaypointB\x03\xe0A\x01\x12@\n\x0btravel_mode\x18\x04 \x01(\x0e2&.google.maps.routes.v1.RouteTravelModeB\x03\xe0A\x01\x12I\n\x12routing_preference\x18\x05 \x01(\x0e2(.google.maps.routes.v1.RoutingPreferenceB\x03\xe0A\x01\x12E\n\x10polyline_quality\x18\x06 \x01(\x0e2&.google.maps.routes.v1.PolylineQualityB\x03\xe0A\x01\x12G\n\x11polyline_encoding\x18\r \x01(\x0e2\'.google.maps.routes.v1.PolylineEncodingB\x03\xe0A\x01\x127\n\x0edeparture_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12C\n\x0froute_modifiers\x18\x0b \x01(\x0b2%.google.maps.routes.v1.RouteModifiersB\x03\xe0A\x01\x12C\n\x0froute_objective\x18\x0c \x01(\x0b2%.google.maps.routes.v1.RouteObjectiveB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\t \x01(\tB\x03\xe0A\x01\x120\n\x05units\x18\n \x01(\x0e2\x1c.google.maps.routes.v1.UnitsB\x03\xe0A\x01"\xe2\x04\n\x0eRouteObjective\x12C\n\trate_card\x18\x01 \x01(\x0b2..google.maps.routes.v1.RouteObjective.RateCardH\x00\x12L\n\x0ccustom_layer\x18\x02 \x01(\x0b21.google.maps.routes.v1.RouteObjective.CustomLayerB\x03\xe0A\x01\x1a\xfc\x01\n\x08RateCard\x12Y\n\x0fcost_per_minute\x18\x02 \x01(\x0b2;.google.maps.routes.v1.RouteObjective.RateCard.MonetaryCostB\x03\xe0A\x01\x12U\n\x0bcost_per_km\x18\x03 \x01(\x0b2;.google.maps.routes.v1.RouteObjective.RateCard.MonetaryCostB\x03\xe0A\x01\x12\x1a\n\rinclude_tolls\x18\x04 \x01(\x08B\x03\xe0A\x01\x1a"\n\x0cMonetaryCost\x12\x12\n\x05value\x18\x01 \x01(\x01B\x03\xe0A\x02\x1a\xb0\x01\n\x0bCustomLayer\x12X\n\x0cdataset_info\x18\x01 \x01(\x0b2=.google.maps.routes.v1.RouteObjective.CustomLayer.DatasetInfoB\x03\xe0A\x02\x1aC\n\x0bDatasetInfo\x12\x19\n\ndataset_id\x18\x01 \x01(\tB\x05\x18\x01\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01:\x02\x18\x01B\x0b\n\tobjectiveB\xae\x01\n\x19com.google.maps.routes.v1B\x1fComputeCustomRoutesRequestProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.compute_custom_routes_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B\x1fComputeCustomRoutesRequestProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['origin']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['origin']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['destination']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['destination']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['intermediates']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['intermediates']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['travel_mode']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['travel_mode']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['routing_preference']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['routing_preference']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['polyline_quality']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['polyline_quality']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['polyline_encoding']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['polyline_encoding']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['departure_time']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['departure_time']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['route_modifiers']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['route_modifiers']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['route_objective']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['route_objective']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['units']._loaded_options = None
    _globals['_COMPUTECUSTOMROUTESREQUEST'].fields_by_name['units']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEOBJECTIVE_RATECARD_MONETARYCOST'].fields_by_name['value']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_RATECARD_MONETARYCOST'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTEOBJECTIVE_RATECARD'].fields_by_name['cost_per_minute']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_RATECARD'].fields_by_name['cost_per_minute']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEOBJECTIVE_RATECARD'].fields_by_name['cost_per_km']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_RATECARD'].fields_by_name['cost_per_km']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEOBJECTIVE_RATECARD'].fields_by_name['include_tolls']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_RATECARD'].fields_by_name['include_tolls']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER_DATASETINFO'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER_DATASETINFO'].fields_by_name['dataset_id']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER_DATASETINFO'].fields_by_name['display_name']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER_DATASETINFO'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER'].fields_by_name['dataset_info']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER'].fields_by_name['dataset_info']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER']._loaded_options = None
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER']._serialized_options = b'\x18\x01'
    _globals['_ROUTEOBJECTIVE'].fields_by_name['custom_layer']._loaded_options = None
    _globals['_ROUTEOBJECTIVE'].fields_by_name['custom_layer']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECUSTOMROUTESREQUEST']._serialized_start = 279
    _globals['_COMPUTECUSTOMROUTESREQUEST']._serialized_end = 1039
    _globals['_ROUTEOBJECTIVE']._serialized_start = 1042
    _globals['_ROUTEOBJECTIVE']._serialized_end = 1652
    _globals['_ROUTEOBJECTIVE_RATECARD']._serialized_start = 1208
    _globals['_ROUTEOBJECTIVE_RATECARD']._serialized_end = 1460
    _globals['_ROUTEOBJECTIVE_RATECARD_MONETARYCOST']._serialized_start = 1426
    _globals['_ROUTEOBJECTIVE_RATECARD_MONETARYCOST']._serialized_end = 1460
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER']._serialized_start = 1463
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER']._serialized_end = 1639
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER_DATASETINFO']._serialized_start = 1568
    _globals['_ROUTEOBJECTIVE_CUSTOMLAYER_DATASETINFO']._serialized_end = 1635