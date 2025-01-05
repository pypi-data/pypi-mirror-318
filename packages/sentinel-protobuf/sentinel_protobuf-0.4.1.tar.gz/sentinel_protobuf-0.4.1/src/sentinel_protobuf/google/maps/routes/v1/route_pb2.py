"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routes/v1/route.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.geo.type import viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2
from .....google.maps.routes.v1 import polyline_pb2 as google_dot_maps_dot_routes_dot_v1_dot_polyline__pb2
from .....google.maps.routes.v1 import waypoint_pb2 as google_dot_maps_dot_routes_dot_v1_dot_waypoint__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/maps/routes/v1/route.proto\x12\x15google.maps.routes.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/geo/type/viewport.proto\x1a$google/maps/routes/v1/polyline.proto\x1a$google/maps/routes/v1/waypoint.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/type/money.proto"\xab\x03\n\x05Route\x12-\n\x04legs\x18\x01 \x03(\x0b2\x1f.google.maps.routes.v1.RouteLeg\x12\x17\n\x0fdistance_meters\x18\x02 \x01(\x05\x12+\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fstatic_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x121\n\x08polyline\x18\x05 \x01(\x0b2\x1f.google.maps.routes.v1.Polyline\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x10\n\x08warnings\x18\x07 \x03(\t\x12+\n\x08viewport\x18\x08 \x01(\x0b2\x19.google.geo.type.Viewport\x12C\n\x0ftravel_advisory\x18\t \x01(\x0b2*.google.maps.routes.v1.RouteTravelAdvisory\x12-\n%optimized_intermediate_waypoint_index\x18\n \x03(\x05"\xa6\x02\n\x13RouteTravelAdvisory\x12F\n\x13traffic_restriction\x18\x01 \x01(\x0b2).google.maps.routes.v1.TrafficRestriction\x122\n\ttoll_info\x18\x02 \x01(\x0b2\x1f.google.maps.routes.v1.TollInfo\x12L\n\x17speed_reading_intervals\x18\x03 \x03(\x0b2+.google.maps.routes.v1.SpeedReadingInterval\x12E\n\x11custom_layer_info\x18\x04 \x01(\x0b2&.google.maps.routes.v1.CustomLayerInfoB\x02\x18\x01"\xe1\x01\n\x16RouteLegTravelAdvisory\x122\n\ttoll_info\x18\x01 \x01(\x0b2\x1f.google.maps.routes.v1.TollInfo\x12L\n\x17speed_reading_intervals\x18\x02 \x03(\x0b2+.google.maps.routes.v1.SpeedReadingInterval\x12E\n\x11custom_layer_info\x18\x03 \x01(\x0b2&.google.maps.routes.v1.CustomLayerInfoB\x02\x18\x01"j\n\x1aRouteLegStepTravelAdvisory\x12L\n\x17speed_reading_intervals\x18\x01 \x03(\x0b2+.google.maps.routes.v1.SpeedReadingInterval"\x83\x01\n\x12TrafficRestriction\x12m\n(license_plate_last_character_restriction\x18\x01 \x01(\x0b2;.google.maps.routes.v1.LicensePlateLastCharacterRestriction"G\n$LicensePlateLastCharacterRestriction\x12\x1f\n\x17allowed_last_characters\x18\x01 \x03(\t"\xa3\x03\n\x08RouteLeg\x12\x17\n\x0fdistance_meters\x18\x01 \x01(\x05\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fstatic_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x121\n\x08polyline\x18\x04 \x01(\x0b2\x1f.google.maps.routes.v1.Polyline\x127\n\x0estart_location\x18\x05 \x01(\x0b2\x1f.google.maps.routes.v1.Location\x125\n\x0cend_location\x18\x06 \x01(\x0b2\x1f.google.maps.routes.v1.Location\x122\n\x05steps\x18\x07 \x03(\x0b2#.google.maps.routes.v1.RouteLegStep\x12F\n\x0ftravel_advisory\x18\x08 \x01(\x0b2-.google.maps.routes.v1.RouteLegTravelAdvisory"7\n\x08TollInfo\x12+\n\x0festimated_price\x18\x01 \x03(\x0b2\x12.google.type.Money"\x98\x03\n\x0cRouteLegStep\x12\x17\n\x0fdistance_meters\x18\x01 \x01(\x05\x122\n\x0fstatic_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x121\n\x08polyline\x18\x03 \x01(\x0b2\x1f.google.maps.routes.v1.Polyline\x127\n\x0estart_location\x18\x04 \x01(\x0b2\x1f.google.maps.routes.v1.Location\x125\n\x0cend_location\x18\x05 \x01(\x0b2\x1f.google.maps.routes.v1.Location\x12L\n\x16navigation_instruction\x18\x06 \x01(\x0b2,.google.maps.routes.v1.NavigationInstruction\x12J\n\x0ftravel_advisory\x18\x07 \x01(\x0b21.google.maps.routes.v1.RouteLegStepTravelAdvisory"`\n\x15NavigationInstruction\x121\n\x08maneuver\x18\x01 \x01(\x0e2\x1f.google.maps.routes.v1.Maneuver\x12\x14\n\x0cinstructions\x18\x02 \x01(\t"\xe5\x01\n\x14SpeedReadingInterval\x12"\n\x1astart_polyline_point_index\x18\x01 \x01(\x05\x12 \n\x18end_polyline_point_index\x18\x02 \x01(\x05\x12@\n\x05speed\x18\x03 \x01(\x0e21.google.maps.routes.v1.SpeedReadingInterval.Speed"E\n\x05Speed\x12\x15\n\x11SPEED_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04SLOW\x10\x02\x12\x0f\n\x0bTRAFFIC_JAM\x10\x03"\xb0\x02\n\x0fCustomLayerInfo\x12B\n\tarea_info\x18\x01 \x03(\x0b2/.google.maps.routes.v1.CustomLayerInfo.AreaInfo\x12&\n\x1etotal_distance_in_areas_meters\x18\x02 \x01(\x02\x12:\n\x17total_duration_in_areas\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x1aq\n\x08AreaInfo\x12\x0f\n\x07area_id\x18\x01 \x01(\t\x12\x1f\n\x17distance_in_area_meters\x18\x02 \x01(\x02\x123\n\x10duration_in_area\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration:\x02\x18\x01*\xf7\x02\n\x08Maneuver\x12\x18\n\x14MANEUVER_UNSPECIFIED\x10\x00\x12\x14\n\x10TURN_SLIGHT_LEFT\x10\x01\x12\x13\n\x0fTURN_SHARP_LEFT\x10\x02\x12\x0e\n\nUTURN_LEFT\x10\x03\x12\r\n\tTURN_LEFT\x10\x04\x12\x15\n\x11TURN_SLIGHT_RIGHT\x10\x05\x12\x14\n\x10TURN_SHARP_RIGHT\x10\x06\x12\x0f\n\x0bUTURN_RIGHT\x10\x07\x12\x0e\n\nTURN_RIGHT\x10\x08\x12\x0c\n\x08STRAIGHT\x10\t\x12\r\n\tRAMP_LEFT\x10\n\x12\x0e\n\nRAMP_RIGHT\x10\x0b\x12\t\n\x05MERGE\x10\x0c\x12\r\n\tFORK_LEFT\x10\r\x12\x0e\n\nFORK_RIGHT\x10\x0e\x12\t\n\x05FERRY\x10\x0f\x12\x0f\n\x0bFERRY_TRAIN\x10\x10\x12\x13\n\x0fROUNDABOUT_LEFT\x10\x11\x12\x14\n\x10ROUNDABOUT_RIGHT\x10\x12\x12\n\n\x06DEPART\x10\x13\x12\x0f\n\x0bNAME_CHANGE\x10\x14B\x99\x01\n\x19com.google.maps.routes.v1B\nRouteProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routes.v1.route_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.routes.v1B\nRouteProtoP\x01Z7cloud.google.com/go/maps/routes/apiv1/routespb;routespb\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1'
    _globals['_ROUTETRAVELADVISORY'].fields_by_name['custom_layer_info']._loaded_options = None
    _globals['_ROUTETRAVELADVISORY'].fields_by_name['custom_layer_info']._serialized_options = b'\x18\x01'
    _globals['_ROUTELEGTRAVELADVISORY'].fields_by_name['custom_layer_info']._loaded_options = None
    _globals['_ROUTELEGTRAVELADVISORY'].fields_by_name['custom_layer_info']._serialized_options = b'\x18\x01'
    _globals['_CUSTOMLAYERINFO']._loaded_options = None
    _globals['_CUSTOMLAYERINFO']._serialized_options = b'\x18\x01'
    _globals['_MANEUVER']._serialized_start = 3056
    _globals['_MANEUVER']._serialized_end = 3431
    _globals['_ROUTE']._serialized_start = 259
    _globals['_ROUTE']._serialized_end = 686
    _globals['_ROUTETRAVELADVISORY']._serialized_start = 689
    _globals['_ROUTETRAVELADVISORY']._serialized_end = 983
    _globals['_ROUTELEGTRAVELADVISORY']._serialized_start = 986
    _globals['_ROUTELEGTRAVELADVISORY']._serialized_end = 1211
    _globals['_ROUTELEGSTEPTRAVELADVISORY']._serialized_start = 1213
    _globals['_ROUTELEGSTEPTRAVELADVISORY']._serialized_end = 1319
    _globals['_TRAFFICRESTRICTION']._serialized_start = 1322
    _globals['_TRAFFICRESTRICTION']._serialized_end = 1453
    _globals['_LICENSEPLATELASTCHARACTERRESTRICTION']._serialized_start = 1455
    _globals['_LICENSEPLATELASTCHARACTERRESTRICTION']._serialized_end = 1526
    _globals['_ROUTELEG']._serialized_start = 1529
    _globals['_ROUTELEG']._serialized_end = 1948
    _globals['_TOLLINFO']._serialized_start = 1950
    _globals['_TOLLINFO']._serialized_end = 2005
    _globals['_ROUTELEGSTEP']._serialized_start = 2008
    _globals['_ROUTELEGSTEP']._serialized_end = 2416
    _globals['_NAVIGATIONINSTRUCTION']._serialized_start = 2418
    _globals['_NAVIGATIONINSTRUCTION']._serialized_end = 2514
    _globals['_SPEEDREADINGINTERVAL']._serialized_start = 2517
    _globals['_SPEEDREADINGINTERVAL']._serialized_end = 2746
    _globals['_SPEEDREADINGINTERVAL_SPEED']._serialized_start = 2677
    _globals['_SPEEDREADINGINTERVAL_SPEED']._serialized_end = 2746
    _globals['_CUSTOMLAYERINFO']._serialized_start = 2749
    _globals['_CUSTOMLAYERINFO']._serialized_end = 3053
    _globals['_CUSTOMLAYERINFO_AREAINFO']._serialized_start = 2936
    _globals['_CUSTOMLAYERINFO_AREAINFO']._serialized_end = 3049