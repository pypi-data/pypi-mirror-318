"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/v1/trips.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.maps.fleetengine.v1 import fleetengine_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_fleetengine__pb2
from .....google.maps.fleetengine.v1 import traffic_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_traffic__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/maps/fleetengine/v1/trips.proto\x12\x13maps.fleetengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/maps/fleetengine/v1/fleetengine.proto\x1a(google/maps/fleetengine/v1/traffic.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\xb7\x10\n\x04Trip\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\nvehicle_id\x18\x02 \x01(\t\x124\n\x0btrip_status\x18\x03 \x01(\x0e2\x1f.maps.fleetengine.v1.TripStatus\x120\n\ttrip_type\x18\x04 \x01(\x0e2\x1d.maps.fleetengine.v1.TripType\x12;\n\x0cpickup_point\x18\x05 \x01(\x0b2%.maps.fleetengine.v1.TerminalLocation\x12C\n\x13actual_pickup_point\x18\x16 \x01(\x0b2!.maps.fleetengine.v1.StopLocationB\x03\xe0A\x04\x12K\n\x1bactual_pickup_arrival_point\x18  \x01(\x0b2!.maps.fleetengine.v1.StopLocationB\x03\xe0A\x04\x124\n\x0bpickup_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x19intermediate_destinations\x18\x0e \x03(\x0b2%.maps.fleetengine.v1.TerminalLocation\x12E\n!intermediate_destinations_version\x18\x19 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12&\n\x1eintermediate_destination_index\x18\x0f \x01(\x05\x12^\n.actual_intermediate_destination_arrival_points\x18! \x03(\x0b2!.maps.fleetengine.v1.StopLocationB\x03\xe0A\x04\x12P\n actual_intermediate_destinations\x18" \x03(\x0b2!.maps.fleetengine.v1.StopLocationB\x03\xe0A\x04\x12<\n\rdropoff_point\x18\x07 \x01(\x0b2%.maps.fleetengine.v1.TerminalLocation\x12D\n\x14actual_dropoff_point\x18\x17 \x01(\x0b2!.maps.fleetengine.v1.StopLocationB\x03\xe0A\x04\x125\n\x0cdropoff_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x13remaining_waypoints\x18\x10 \x03(\x0b2!.maps.fleetengine.v1.TripWaypointB\x03\xe0A\x03\x12<\n\x11vehicle_waypoints\x18\x14 \x03(\x0b2!.maps.fleetengine.v1.TripWaypoint\x12\'\n\x05route\x18\t \x03(\x0b2\x13.google.type.LatLngB\x03\xe0A\x03\x12"\n\x15current_route_segment\x18\x15 \x01(\tB\x03\xe0A\x03\x12F\n\x1dcurrent_route_segment_version\x18\x11 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Z\n\x1dcurrent_route_segment_traffic\x18\x1c \x01(\x0b2..maps.fleetengine.v1.ConsumableTrafficPolylineB\x03\xe0A\x03\x12N\n%current_route_segment_traffic_version\x18\x1e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12O\n\x1fcurrent_route_segment_end_point\x18\x18 \x01(\x0b2!.maps.fleetengine.v1.TripWaypointB\x03\xe0A\x03\x12C\n\x19remaining_distance_meters\x18\x0c \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x03\x12>\n\x15eta_to_first_waypoint\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n remaining_time_to_first_waypoint\x18\x1b \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x12D\n\x1bremaining_waypoints_version\x18\x13 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12J\n!remaining_waypoints_route_version\x18\x1d \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12!\n\x14number_of_passengers\x18\n \x01(\x05B\x03\xe0A\x05\x12@\n\rlast_location\x18\x0b \x01(\x0b2$.maps.fleetengine.v1.VehicleLocationB\x03\xe0A\x03\x12$\n\x17last_location_snappable\x18\x1a \x01(\x08B\x03\xe0A\x03\x12+\n\x04view\x18\x1f \x01(\x0e2\x1d.maps.fleetengine.v1.TripView:G\xeaAD\n\x1ffleetengine.googleapis.com/Trip\x12!providers/{provider}/trips/{trip}"\x9c\x01\n\x0cStopLocation\x12\'\n\x05point\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12-\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\tstop_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x05\x18\x01\xe0A\x04*\xe2\x01\n\nTripStatus\x12\x17\n\x13UNKNOWN_TRIP_STATUS\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x15\n\x11ENROUTE_TO_PICKUP\x10\x02\x12\x15\n\x11ARRIVED_AT_PICKUP\x10\x03\x12\'\n#ARRIVED_AT_INTERMEDIATE_DESTINATION\x10\x07\x12\'\n#ENROUTE_TO_INTERMEDIATE_DESTINATION\x10\x08\x12\x16\n\x12ENROUTE_TO_DROPOFF\x10\x04\x12\x0c\n\x08COMPLETE\x10\x05\x12\x0c\n\x08CANCELED\x10\x06*\x7f\n\x19BillingPlatformIdentifier\x12+\n\'BILLING_PLATFORM_IDENTIFIER_UNSPECIFIED\x10\x00\x12\n\n\x06SERVER\x10\x01\x12\x07\n\x03WEB\x10\x02\x12\x0b\n\x07ANDROID\x10\x03\x12\x07\n\x03IOS\x10\x04\x12\n\n\x06OTHERS\x10\x05*G\n\x08TripView\x12\x19\n\x15TRIP_VIEW_UNSPECIFIED\x10\x00\x12\x07\n\x03SDK\x10\x01\x12\x17\n\x13JOURNEY_SHARING_V1S\x10\x02B\xd1\x01\n\x1ecom.google.maps.fleetengine.v1B\x05TripsP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.v1.trips_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.maps.fleetengine.v1B\x05TripsP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1'
    _globals['_TRIP'].fields_by_name['name']._loaded_options = None
    _globals['_TRIP'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['actual_pickup_point']._loaded_options = None
    _globals['_TRIP'].fields_by_name['actual_pickup_point']._serialized_options = b'\xe0A\x04'
    _globals['_TRIP'].fields_by_name['actual_pickup_arrival_point']._loaded_options = None
    _globals['_TRIP'].fields_by_name['actual_pickup_arrival_point']._serialized_options = b'\xe0A\x04'
    _globals['_TRIP'].fields_by_name['pickup_time']._loaded_options = None
    _globals['_TRIP'].fields_by_name['pickup_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['actual_intermediate_destination_arrival_points']._loaded_options = None
    _globals['_TRIP'].fields_by_name['actual_intermediate_destination_arrival_points']._serialized_options = b'\xe0A\x04'
    _globals['_TRIP'].fields_by_name['actual_intermediate_destinations']._loaded_options = None
    _globals['_TRIP'].fields_by_name['actual_intermediate_destinations']._serialized_options = b'\xe0A\x04'
    _globals['_TRIP'].fields_by_name['actual_dropoff_point']._loaded_options = None
    _globals['_TRIP'].fields_by_name['actual_dropoff_point']._serialized_options = b'\xe0A\x04'
    _globals['_TRIP'].fields_by_name['dropoff_time']._loaded_options = None
    _globals['_TRIP'].fields_by_name['dropoff_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['remaining_waypoints']._loaded_options = None
    _globals['_TRIP'].fields_by_name['remaining_waypoints']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['route']._loaded_options = None
    _globals['_TRIP'].fields_by_name['route']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['current_route_segment']._loaded_options = None
    _globals['_TRIP'].fields_by_name['current_route_segment']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['current_route_segment_version']._loaded_options = None
    _globals['_TRIP'].fields_by_name['current_route_segment_version']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['current_route_segment_traffic']._loaded_options = None
    _globals['_TRIP'].fields_by_name['current_route_segment_traffic']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['current_route_segment_traffic_version']._loaded_options = None
    _globals['_TRIP'].fields_by_name['current_route_segment_traffic_version']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['current_route_segment_end_point']._loaded_options = None
    _globals['_TRIP'].fields_by_name['current_route_segment_end_point']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['remaining_distance_meters']._loaded_options = None
    _globals['_TRIP'].fields_by_name['remaining_distance_meters']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['eta_to_first_waypoint']._loaded_options = None
    _globals['_TRIP'].fields_by_name['eta_to_first_waypoint']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['remaining_time_to_first_waypoint']._loaded_options = None
    _globals['_TRIP'].fields_by_name['remaining_time_to_first_waypoint']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['remaining_waypoints_version']._loaded_options = None
    _globals['_TRIP'].fields_by_name['remaining_waypoints_version']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['remaining_waypoints_route_version']._loaded_options = None
    _globals['_TRIP'].fields_by_name['remaining_waypoints_route_version']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['number_of_passengers']._loaded_options = None
    _globals['_TRIP'].fields_by_name['number_of_passengers']._serialized_options = b'\xe0A\x05'
    _globals['_TRIP'].fields_by_name['last_location']._loaded_options = None
    _globals['_TRIP'].fields_by_name['last_location']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP'].fields_by_name['last_location_snappable']._loaded_options = None
    _globals['_TRIP'].fields_by_name['last_location_snappable']._serialized_options = b'\xe0A\x03'
    _globals['_TRIP']._loaded_options = None
    _globals['_TRIP']._serialized_options = b'\xeaAD\n\x1ffleetengine.googleapis.com/Trip\x12!providers/{provider}/trips/{trip}'
    _globals['_STOPLOCATION'].fields_by_name['point']._loaded_options = None
    _globals['_STOPLOCATION'].fields_by_name['point']._serialized_options = b'\xe0A\x02'
    _globals['_STOPLOCATION'].fields_by_name['stop_time']._loaded_options = None
    _globals['_STOPLOCATION'].fields_by_name['stop_time']._serialized_options = b'\x18\x01\xe0A\x04'
    _globals['_TRIPSTATUS']._serialized_start = 2600
    _globals['_TRIPSTATUS']._serialized_end = 2826
    _globals['_BILLINGPLATFORMIDENTIFIER']._serialized_start = 2828
    _globals['_BILLINGPLATFORMIDENTIFIER']._serialized_end = 2955
    _globals['_TRIPVIEW']._serialized_start = 2957
    _globals['_TRIPVIEW']._serialized_end = 3028
    _globals['_TRIP']._serialized_start = 335
    _globals['_TRIP']._serialized_end = 2438
    _globals['_STOPLOCATION']._serialized_start = 2441
    _globals['_STOPLOCATION']._serialized_end = 2597