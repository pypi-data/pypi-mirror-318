"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/v1/fleetengine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.fleetengine.v1 import traffic_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_traffic__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/maps/fleetengine/v1/fleetengine.proto\x12\x13maps.fleetengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/maps/fleetengine/v1/traffic.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"b\n\x0fTerminalPointId\x12\x16\n\x08place_id\x18\x02 \x01(\tB\x02\x18\x01H\x00\x12\x1a\n\x0cgenerated_id\x18\x03 \x01(\tB\x02\x18\x01H\x00\x12\x11\n\x05value\x18\x04 \x01(\tB\x02\x18\x01:\x02\x18\x01B\x04\n\x02Id"\xf9\x01\n\x10TerminalLocation\x12\'\n\x05point\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12C\n\x11terminal_point_id\x18\x02 \x01(\x0b2$.maps.fleetengine.v1.TerminalPointIdB\x02\x18\x01\x12\x1b\n\x0faccess_point_id\x18\x03 \x01(\tB\x02\x18\x01\x12\x13\n\x07trip_id\x18\x04 \x01(\tB\x02\x18\x01\x12E\n\x16terminal_location_type\x18\x05 \x01(\x0e2!.maps.fleetengine.v1.WaypointTypeB\x02\x18\x01"\xbc\x03\n\x0cTripWaypoint\x127\n\x08location\x18\x01 \x01(\x0b2%.maps.fleetengine.v1.TerminalLocation\x12\x0f\n\x07trip_id\x18\x02 \x01(\t\x128\n\rwaypoint_type\x18\x03 \x01(\x0e2!.maps.fleetengine.v1.WaypointType\x12-\n\x10path_to_waypoint\x18\x04 \x03(\x0b2\x13.google.type.LatLng\x12 \n\x18encoded_path_to_waypoint\x18\x05 \x01(\t\x12K\n\x13traffic_to_waypoint\x18\n \x01(\x0b2..maps.fleetengine.v1.ConsumableTrafficPolyline\x124\n\x0fdistance_meters\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12\'\n\x03eta\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x08duration\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration"\x8f\x01\n\x10VehicleAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0cnumber_value\x18\x05 \x01(\x01H\x00B\x19\n\x17vehicle_attribute_value"\xa4\x0c\n\x0fVehicleLocation\x12%\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12=\n\x13horizontal_accuracy\x18\x08 \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x02\x18\x01\x125\n\x0flatlng_accuracy\x18\x16 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12,\n\x07heading\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12:\n\x10bearing_accuracy\x18\n \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x02\x18\x01\x126\n\x10heading_accuracy\x18\x17 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12.\n\x08altitude\x18\x05 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12;\n\x11vertical_accuracy\x18\t \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x02\x18\x01\x127\n\x11altitude_accuracy\x18\x18 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x123\n\nspeed_kmph\x18\x03 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x02\x18\x01\x12+\n\x05speed\x18\x06 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x124\n\x0espeed_accuracy\x18\x07 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x0bserver_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x0flocation_sensor\x18\x0b \x01(\x0e2#.maps.fleetengine.v1.LocationSensor\x123\n\x0fis_road_snapped\x18\x1b \x01(\x0b2\x1a.google.protobuf.BoolValue\x12>\n\x15is_gps_sensor_enabled\x18\x0c \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x04\x12;\n\x11time_since_update\x18\x0e \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x04\x12=\n\x11num_stale_updates\x18\x0f \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x05\x18\x01\xe0A\x04\x12)\n\x0craw_location\x18\x10 \x01(\x0b2\x13.google.type.LatLng\x125\n\x11raw_location_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12@\n\x13raw_location_sensor\x18\x1c \x01(\x0e2#.maps.fleetengine.v1.LocationSensor\x12;\n\x15raw_location_accuracy\x18\x19 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x122\n\x15supplemental_location\x18\x12 \x01(\x0b2\x13.google.type.LatLng\x12>\n\x1asupplemental_location_time\x18\x13 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12I\n\x1csupplemental_location_sensor\x18\x14 \x01(\x0e2#.maps.fleetengine.v1.LocationSensor\x12D\n\x1esupplemental_location_accuracy\x18\x15 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12\x18\n\x0croad_snapped\x18\x1a \x01(\x08B\x02\x18\x01*<\n\x08TripType\x12\x15\n\x11UNKNOWN_TRIP_TYPE\x10\x00\x12\n\n\x06SHARED\x10\x01\x12\r\n\tEXCLUSIVE\x10\x02*\x8b\x01\n\x0cWaypointType\x12\x19\n\x15UNKNOWN_WAYPOINT_TYPE\x10\x00\x12\x18\n\x14PICKUP_WAYPOINT_TYPE\x10\x01\x12\x1a\n\x16DROP_OFF_WAYPOINT_TYPE\x10\x02\x12*\n&INTERMEDIATE_DESTINATION_WAYPOINT_TYPE\x10\x03*_\n\x12PolylineFormatType\x12\x17\n\x13UNKNOWN_FORMAT_TYPE\x10\x00\x12\x15\n\x11LAT_LNG_LIST_TYPE\x10\x01\x12\x19\n\x15ENCODED_POLYLINE_TYPE\x10\x02*\x89\x01\n\x10NavigationStatus\x12\x1d\n\x19UNKNOWN_NAVIGATION_STATUS\x10\x00\x12\x0f\n\x0bNO_GUIDANCE\x10\x01\x12\x1a\n\x16ENROUTE_TO_DESTINATION\x10\x02\x12\r\n\tOFF_ROUTE\x10\x03\x12\x1a\n\x16ARRIVED_AT_DESTINATION\x10\x04*\xd7\x01\n\x0eLocationSensor\x12\x12\n\x0eUNKNOWN_SENSOR\x10\x00\x12\x07\n\x03GPS\x10\x01\x12\x0b\n\x07NETWORK\x10\x02\x12\x0b\n\x07PASSIVE\x10\x03\x12"\n\x1eROAD_SNAPPED_LOCATION_PROVIDER\x10\x04\x12\x1e\n\x1aCUSTOMER_SUPPLIED_LOCATION\x10\x05\x12\x19\n\x15FLEET_ENGINE_LOCATION\x10\x06\x12\x1b\n\x17FUSED_LOCATION_PROVIDER\x10d\x12\x12\n\rCORE_LOCATION\x10\xc8\x01B\xd7\x01\n\x1ecom.google.maps.fleetengine.v1B\x0bFleetEngineP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.v1.fleetengine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.maps.fleetengine.v1B\x0bFleetEngineP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1'
    _globals['_TERMINALPOINTID'].fields_by_name['place_id']._loaded_options = None
    _globals['_TERMINALPOINTID'].fields_by_name['place_id']._serialized_options = b'\x18\x01'
    _globals['_TERMINALPOINTID'].fields_by_name['generated_id']._loaded_options = None
    _globals['_TERMINALPOINTID'].fields_by_name['generated_id']._serialized_options = b'\x18\x01'
    _globals['_TERMINALPOINTID'].fields_by_name['value']._loaded_options = None
    _globals['_TERMINALPOINTID'].fields_by_name['value']._serialized_options = b'\x18\x01'
    _globals['_TERMINALPOINTID']._loaded_options = None
    _globals['_TERMINALPOINTID']._serialized_options = b'\x18\x01'
    _globals['_TERMINALLOCATION'].fields_by_name['point']._loaded_options = None
    _globals['_TERMINALLOCATION'].fields_by_name['point']._serialized_options = b'\xe0A\x02'
    _globals['_TERMINALLOCATION'].fields_by_name['terminal_point_id']._loaded_options = None
    _globals['_TERMINALLOCATION'].fields_by_name['terminal_point_id']._serialized_options = b'\x18\x01'
    _globals['_TERMINALLOCATION'].fields_by_name['access_point_id']._loaded_options = None
    _globals['_TERMINALLOCATION'].fields_by_name['access_point_id']._serialized_options = b'\x18\x01'
    _globals['_TERMINALLOCATION'].fields_by_name['trip_id']._loaded_options = None
    _globals['_TERMINALLOCATION'].fields_by_name['trip_id']._serialized_options = b'\x18\x01'
    _globals['_TERMINALLOCATION'].fields_by_name['terminal_location_type']._loaded_options = None
    _globals['_TERMINALLOCATION'].fields_by_name['terminal_location_type']._serialized_options = b'\x18\x01'
    _globals['_VEHICLELOCATION'].fields_by_name['horizontal_accuracy']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['horizontal_accuracy']._serialized_options = b'\x18\x01'
    _globals['_VEHICLELOCATION'].fields_by_name['bearing_accuracy']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['bearing_accuracy']._serialized_options = b'\x18\x01'
    _globals['_VEHICLELOCATION'].fields_by_name['vertical_accuracy']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['vertical_accuracy']._serialized_options = b'\x18\x01'
    _globals['_VEHICLELOCATION'].fields_by_name['speed_kmph']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['speed_kmph']._serialized_options = b'\x18\x01'
    _globals['_VEHICLELOCATION'].fields_by_name['server_time']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['server_time']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLELOCATION'].fields_by_name['is_gps_sensor_enabled']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['is_gps_sensor_enabled']._serialized_options = b'\xe0A\x04'
    _globals['_VEHICLELOCATION'].fields_by_name['time_since_update']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['time_since_update']._serialized_options = b'\xe0A\x04'
    _globals['_VEHICLELOCATION'].fields_by_name['num_stale_updates']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['num_stale_updates']._serialized_options = b'\x18\x01\xe0A\x04'
    _globals['_VEHICLELOCATION'].fields_by_name['road_snapped']._loaded_options = None
    _globals['_VEHICLELOCATION'].fields_by_name['road_snapped']._serialized_options = b'\x18\x01'
    _globals['_TRIPTYPE']._serialized_start = 2787
    _globals['_TRIPTYPE']._serialized_end = 2847
    _globals['_WAYPOINTTYPE']._serialized_start = 2850
    _globals['_WAYPOINTTYPE']._serialized_end = 2989
    _globals['_POLYLINEFORMATTYPE']._serialized_start = 2991
    _globals['_POLYLINEFORMATTYPE']._serialized_end = 3086
    _globals['_NAVIGATIONSTATUS']._serialized_start = 3089
    _globals['_NAVIGATIONSTATUS']._serialized_end = 3226
    _globals['_LOCATIONSENSOR']._serialized_start = 3229
    _globals['_LOCATIONSENSOR']._serialized_end = 3444
    _globals['_TERMINALPOINTID']._serialized_start = 267
    _globals['_TERMINALPOINTID']._serialized_end = 365
    _globals['_TERMINALLOCATION']._serialized_start = 368
    _globals['_TERMINALLOCATION']._serialized_end = 617
    _globals['_TRIPWAYPOINT']._serialized_start = 620
    _globals['_TRIPWAYPOINT']._serialized_end = 1064
    _globals['_VEHICLEATTRIBUTE']._serialized_start = 1067
    _globals['_VEHICLEATTRIBUTE']._serialized_end = 1210
    _globals['_VEHICLELOCATION']._serialized_start = 1213
    _globals['_VEHICLELOCATION']._serialized_end = 2785