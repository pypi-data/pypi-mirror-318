"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/v1/vehicles.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.maps.fleetengine.v1 import fleetengine_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_fleetengine__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/maps/fleetengine/v1/vehicles.proto\x12\x13maps.fleetengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/maps/fleetengine/v1/fleetengine.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xe2\x0b\n\x07Vehicle\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x128\n\rvehicle_state\x18\x02 \x01(\x0e2!.maps.fleetengine.v1.VehicleState\x12;\n\x14supported_trip_types\x18\x03 \x03(\x0e2\x1d.maps.fleetengine.v1.TripType\x12\x1a\n\rcurrent_trips\x18\x04 \x03(\tB\x03\xe0A\x03\x12;\n\rlast_location\x18\x05 \x01(\x0b2$.maps.fleetengine.v1.VehicleLocation\x12\x18\n\x10maximum_capacity\x18\x06 \x01(\x05\x129\n\nattributes\x18\x08 \x03(\x0b2%.maps.fleetengine.v1.VehicleAttribute\x12C\n\x0cvehicle_type\x18\t \x01(\x0b2(.maps.fleetengine.v1.Vehicle.VehicleTypeB\x03\xe0A\x02\x128\n\rlicense_plate\x18\n \x01(\x0b2!.maps.fleetengine.v1.LicensePlate\x128\n\x05route\x18\x0c \x03(\x0b2%.maps.fleetengine.v1.TerminalLocationB\x02\x18\x01\x12\x1d\n\x15current_route_segment\x18\x14 \x01(\t\x12T\n\x1dcurrent_route_segment_traffic\x18\x1c \x01(\x0b2(.maps.fleetengine.v1.TrafficPolylineDataB\x03\xe0A\x04\x12F\n\x1dcurrent_route_segment_version\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12J\n\x1fcurrent_route_segment_end_point\x18\x18 \x01(\x0b2!.maps.fleetengine.v1.TripWaypoint\x12>\n\x19remaining_distance_meters\x18\x12 \x01(\x0b2\x1b.google.protobuf.Int32Value\x129\n\x15eta_to_first_waypoint\x18\x13 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12@\n\x16remaining_time_seconds\x18\x19 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x04\x124\n\twaypoints\x18\x16 \x03(\x0b2!.maps.fleetengine.v1.TripWaypoint\x12:\n\x11waypoints_version\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1c\n\x14back_to_back_enabled\x18\x17 \x01(\x08\x12@\n\x11navigation_status\x18\x1a \x01(\x0e2%.maps.fleetengine.v1.NavigationStatus\x12A\n\x0fdevice_settings\x18\x1b \x01(\x0b2#.maps.fleetengine.v1.DeviceSettingsB\x03\xe0A\x04\x1a\xb8\x01\n\x0bVehicleType\x12C\n\x08category\x18\x01 \x01(\x0e21.maps.fleetengine.v1.Vehicle.VehicleType.Category"d\n\x08Category\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04AUTO\x10\x01\x12\x08\n\x04TAXI\x10\x02\x12\t\n\x05TRUCK\x10\x03\x12\x0f\n\x0bTWO_WHEELER\x10\x04\x12\x0b\n\x07BICYCLE\x10\x05\x12\x0e\n\nPEDESTRIAN\x10\x06:P\xeaAM\n"fleetengine.googleapis.com/Vehicle\x12\'providers/{provider}/vehicles/{vehicle}"\x9d\x01\n\x0bBatteryInfo\x12:\n\x0ebattery_status\x18\x01 \x01(\x0e2".maps.fleetengine.v1.BatteryStatus\x126\n\x0cpower_source\x18\x02 \x01(\x0e2 .maps.fleetengine.v1.PowerSource\x12\x1a\n\x12battery_percentage\x18\x03 \x01(\x02"\xca\x01\n\x0eDeviceSettings\x12L\n\x18location_power_save_mode\x18\x01 \x01(\x0e2*.maps.fleetengine.v1.LocationPowerSaveMode\x12\x1a\n\x12is_power_save_mode\x18\x02 \x01(\x08\x12\x16\n\x0eis_interactive\x18\x03 \x01(\x08\x126\n\x0cbattery_info\x18\x04 \x01(\x0b2 .maps.fleetengine.v1.BatteryInfo"A\n\x0cLicensePlate\x12\x19\n\x0ccountry_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\x0elast_character\x18\x02 \x01(\t"\xf6\x02\n$VisualTrafficReportPolylineRendering\x12`\n\x0croad_stretch\x18\x01 \x03(\x0b2E.maps.fleetengine.v1.VisualTrafficReportPolylineRendering.RoadStretchB\x03\xe0A\x01\x1a\xeb\x01\n\x0bRoadStretch\x12_\n\x05style\x18\x01 \x01(\x0e2K.maps.fleetengine.v1.VisualTrafficReportPolylineRendering.RoadStretch.StyleB\x03\xe0A\x02\x12\x1a\n\roffset_meters\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x1a\n\rlength_meters\x18\x03 \x01(\x05B\x03\xe0A\x02"C\n\x05Style\x12\x15\n\x11STYLE_UNSPECIFIED\x10\x00\x12\x12\n\x0eSLOWER_TRAFFIC\x10\x01\x12\x0f\n\x0bTRAFFIC_JAM\x10\x02"k\n\x13TrafficPolylineData\x12T\n\x11traffic_rendering\x18\x01 \x01(\x0b29.maps.fleetengine.v1.VisualTrafficReportPolylineRendering*B\n\x0cVehicleState\x12\x19\n\x15UNKNOWN_VEHICLE_STATE\x10\x00\x12\x0b\n\x07OFFLINE\x10\x01\x12\n\n\x06ONLINE\x10\x02*\x92\x02\n\x15LocationPowerSaveMode\x12$\n UNKNOWN_LOCATION_POWER_SAVE_MODE\x10\x00\x12\x1b\n\x17LOCATION_MODE_NO_CHANGE\x10\x01\x12.\n*LOCATION_MODE_GPS_DISABLED_WHEN_SCREEN_OFF\x10\x02\x12.\n*LOCATION_MODE_ALL_DISABLED_WHEN_SCREEN_OFF\x10\x03\x12!\n\x1dLOCATION_MODE_FOREGROUND_ONLY\x10\x04\x123\n/LOCATION_MODE_THROTTLE_REQUESTS_WHEN_SCREEN_OFF\x10\x05*\xc0\x01\n\rBatteryStatus\x12\x1a\n\x16UNKNOWN_BATTERY_STATUS\x10\x00\x12\x1b\n\x17BATTERY_STATUS_CHARGING\x10\x01\x12\x1e\n\x1aBATTERY_STATUS_DISCHARGING\x10\x02\x12\x17\n\x13BATTERY_STATUS_FULL\x10\x03\x12\x1f\n\x1bBATTERY_STATUS_NOT_CHARGING\x10\x04\x12\x1c\n\x18BATTERY_STATUS_POWER_LOW\x10\x05*\x89\x01\n\x0bPowerSource\x12\x18\n\x14UNKNOWN_POWER_SOURCE\x10\x00\x12\x13\n\x0fPOWER_SOURCE_AC\x10\x01\x12\x14\n\x10POWER_SOURCE_USB\x10\x02\x12\x19\n\x15POWER_SOURCE_WIRELESS\x10\x03\x12\x1a\n\x16POWER_SOURCE_UNPLUGGED\x10\x04B\xd4\x01\n\x1ecom.google.maps.fleetengine.v1B\x08VehiclesP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.v1.vehicles_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.maps.fleetengine.v1B\x08VehiclesP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1'
    _globals['_VEHICLE'].fields_by_name['name']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLE'].fields_by_name['current_trips']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['current_trips']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLE'].fields_by_name['vehicle_type']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['vehicle_type']._serialized_options = b'\xe0A\x02'
    _globals['_VEHICLE'].fields_by_name['route']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['route']._serialized_options = b'\x18\x01'
    _globals['_VEHICLE'].fields_by_name['current_route_segment_traffic']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['current_route_segment_traffic']._serialized_options = b'\xe0A\x04'
    _globals['_VEHICLE'].fields_by_name['current_route_segment_version']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['current_route_segment_version']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLE'].fields_by_name['remaining_time_seconds']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['remaining_time_seconds']._serialized_options = b'\xe0A\x04'
    _globals['_VEHICLE'].fields_by_name['waypoints_version']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['waypoints_version']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLE'].fields_by_name['device_settings']._loaded_options = None
    _globals['_VEHICLE'].fields_by_name['device_settings']._serialized_options = b'\xe0A\x04'
    _globals['_VEHICLE']._loaded_options = None
    _globals['_VEHICLE']._serialized_options = b'\xeaAM\n"fleetengine.googleapis.com/Vehicle\x12\'providers/{provider}/vehicles/{vehicle}'
    _globals['_LICENSEPLATE'].fields_by_name['country_code']._loaded_options = None
    _globals['_LICENSEPLATE'].fields_by_name['country_code']._serialized_options = b'\xe0A\x02'
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH'].fields_by_name['style']._loaded_options = None
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH'].fields_by_name['style']._serialized_options = b'\xe0A\x02'
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH'].fields_by_name['offset_meters']._loaded_options = None
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH'].fields_by_name['offset_meters']._serialized_options = b'\xe0A\x02'
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH'].fields_by_name['length_meters']._loaded_options = None
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH'].fields_by_name['length_meters']._serialized_options = b'\xe0A\x02'
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING'].fields_by_name['road_stretch']._loaded_options = None
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING'].fields_by_name['road_stretch']._serialized_options = b'\xe0A\x01'
    _globals['_VEHICLESTATE']._serialized_start = 2664
    _globals['_VEHICLESTATE']._serialized_end = 2730
    _globals['_LOCATIONPOWERSAVEMODE']._serialized_start = 2733
    _globals['_LOCATIONPOWERSAVEMODE']._serialized_end = 3007
    _globals['_BATTERYSTATUS']._serialized_start = 3010
    _globals['_BATTERYSTATUS']._serialized_end = 3202
    _globals['_POWERSOURCE']._serialized_start = 3205
    _globals['_POWERSOURCE']._serialized_end = 3342
    _globals['_VEHICLE']._serialized_start = 238
    _globals['_VEHICLE']._serialized_end = 1744
    _globals['_VEHICLE_VEHICLETYPE']._serialized_start = 1478
    _globals['_VEHICLE_VEHICLETYPE']._serialized_end = 1662
    _globals['_VEHICLE_VEHICLETYPE_CATEGORY']._serialized_start = 1562
    _globals['_VEHICLE_VEHICLETYPE_CATEGORY']._serialized_end = 1662
    _globals['_BATTERYINFO']._serialized_start = 1747
    _globals['_BATTERYINFO']._serialized_end = 1904
    _globals['_DEVICESETTINGS']._serialized_start = 1907
    _globals['_DEVICESETTINGS']._serialized_end = 2109
    _globals['_LICENSEPLATE']._serialized_start = 2111
    _globals['_LICENSEPLATE']._serialized_end = 2176
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING']._serialized_start = 2179
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING']._serialized_end = 2553
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH']._serialized_start = 2318
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH']._serialized_end = 2553
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH_STYLE']._serialized_start = 2486
    _globals['_VISUALTRAFFICREPORTPOLYLINERENDERING_ROADSTRETCH_STYLE']._serialized_end = 2553
    _globals['_TRAFFICPOLYLINEDATA']._serialized_start = 2555
    _globals['_TRAFFICPOLYLINEDATA']._serialized_end = 2662