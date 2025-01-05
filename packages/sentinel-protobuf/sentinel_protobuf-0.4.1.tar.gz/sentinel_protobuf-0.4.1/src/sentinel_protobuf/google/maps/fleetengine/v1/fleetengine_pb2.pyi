from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.fleetengine.v1 import traffic_pb2 as _traffic_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TripType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TRIP_TYPE: _ClassVar[TripType]
    SHARED: _ClassVar[TripType]
    EXCLUSIVE: _ClassVar[TripType]

class WaypointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_WAYPOINT_TYPE: _ClassVar[WaypointType]
    PICKUP_WAYPOINT_TYPE: _ClassVar[WaypointType]
    DROP_OFF_WAYPOINT_TYPE: _ClassVar[WaypointType]
    INTERMEDIATE_DESTINATION_WAYPOINT_TYPE: _ClassVar[WaypointType]

class PolylineFormatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_FORMAT_TYPE: _ClassVar[PolylineFormatType]
    LAT_LNG_LIST_TYPE: _ClassVar[PolylineFormatType]
    ENCODED_POLYLINE_TYPE: _ClassVar[PolylineFormatType]

class NavigationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_NAVIGATION_STATUS: _ClassVar[NavigationStatus]
    NO_GUIDANCE: _ClassVar[NavigationStatus]
    ENROUTE_TO_DESTINATION: _ClassVar[NavigationStatus]
    OFF_ROUTE: _ClassVar[NavigationStatus]
    ARRIVED_AT_DESTINATION: _ClassVar[NavigationStatus]

class LocationSensor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_SENSOR: _ClassVar[LocationSensor]
    GPS: _ClassVar[LocationSensor]
    NETWORK: _ClassVar[LocationSensor]
    PASSIVE: _ClassVar[LocationSensor]
    ROAD_SNAPPED_LOCATION_PROVIDER: _ClassVar[LocationSensor]
    CUSTOMER_SUPPLIED_LOCATION: _ClassVar[LocationSensor]
    FLEET_ENGINE_LOCATION: _ClassVar[LocationSensor]
    FUSED_LOCATION_PROVIDER: _ClassVar[LocationSensor]
    CORE_LOCATION: _ClassVar[LocationSensor]
UNKNOWN_TRIP_TYPE: TripType
SHARED: TripType
EXCLUSIVE: TripType
UNKNOWN_WAYPOINT_TYPE: WaypointType
PICKUP_WAYPOINT_TYPE: WaypointType
DROP_OFF_WAYPOINT_TYPE: WaypointType
INTERMEDIATE_DESTINATION_WAYPOINT_TYPE: WaypointType
UNKNOWN_FORMAT_TYPE: PolylineFormatType
LAT_LNG_LIST_TYPE: PolylineFormatType
ENCODED_POLYLINE_TYPE: PolylineFormatType
UNKNOWN_NAVIGATION_STATUS: NavigationStatus
NO_GUIDANCE: NavigationStatus
ENROUTE_TO_DESTINATION: NavigationStatus
OFF_ROUTE: NavigationStatus
ARRIVED_AT_DESTINATION: NavigationStatus
UNKNOWN_SENSOR: LocationSensor
GPS: LocationSensor
NETWORK: LocationSensor
PASSIVE: LocationSensor
ROAD_SNAPPED_LOCATION_PROVIDER: LocationSensor
CUSTOMER_SUPPLIED_LOCATION: LocationSensor
FLEET_ENGINE_LOCATION: LocationSensor
FUSED_LOCATION_PROVIDER: LocationSensor
CORE_LOCATION: LocationSensor

class TerminalPointId(_message.Message):
    __slots__ = ('place_id', 'generated_id', 'value')
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATED_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    generated_id: str
    value: str

    def __init__(self, place_id: _Optional[str]=..., generated_id: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class TerminalLocation(_message.Message):
    __slots__ = ('point', 'terminal_point_id', 'access_point_id', 'trip_id', 'terminal_location_type')
    POINT_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIP_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    point: _latlng_pb2.LatLng
    terminal_point_id: TerminalPointId
    access_point_id: str
    trip_id: str
    terminal_location_type: WaypointType

    def __init__(self, point: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., terminal_point_id: _Optional[_Union[TerminalPointId, _Mapping]]=..., access_point_id: _Optional[str]=..., trip_id: _Optional[str]=..., terminal_location_type: _Optional[_Union[WaypointType, str]]=...) -> None:
        ...

class TripWaypoint(_message.Message):
    __slots__ = ('location', 'trip_id', 'waypoint_type', 'path_to_waypoint', 'encoded_path_to_waypoint', 'traffic_to_waypoint', 'distance_meters', 'eta', 'duration')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TRIP_ID_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_TO_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    ENCODED_PATH_TO_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_TO_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    ETA_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    location: TerminalLocation
    trip_id: str
    waypoint_type: WaypointType
    path_to_waypoint: _containers.RepeatedCompositeFieldContainer[_latlng_pb2.LatLng]
    encoded_path_to_waypoint: str
    traffic_to_waypoint: _traffic_pb2.ConsumableTrafficPolyline
    distance_meters: _wrappers_pb2.Int32Value
    eta: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration

    def __init__(self, location: _Optional[_Union[TerminalLocation, _Mapping]]=..., trip_id: _Optional[str]=..., waypoint_type: _Optional[_Union[WaypointType, str]]=..., path_to_waypoint: _Optional[_Iterable[_Union[_latlng_pb2.LatLng, _Mapping]]]=..., encoded_path_to_waypoint: _Optional[str]=..., traffic_to_waypoint: _Optional[_Union[_traffic_pb2.ConsumableTrafficPolyline, _Mapping]]=..., distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., eta: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class VehicleAttribute(_message.Message):
    __slots__ = ('key', 'value', 'string_value', 'bool_value', 'number_value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    string_value: str
    bool_value: bool
    number_value: float

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=..., string_value: _Optional[str]=..., bool_value: bool=..., number_value: _Optional[float]=...) -> None:
        ...

class VehicleLocation(_message.Message):
    __slots__ = ('location', 'horizontal_accuracy', 'latlng_accuracy', 'heading', 'bearing_accuracy', 'heading_accuracy', 'altitude', 'vertical_accuracy', 'altitude_accuracy', 'speed_kmph', 'speed', 'speed_accuracy', 'update_time', 'server_time', 'location_sensor', 'is_road_snapped', 'is_gps_sensor_enabled', 'time_since_update', 'num_stale_updates', 'raw_location', 'raw_location_time', 'raw_location_sensor', 'raw_location_accuracy', 'supplemental_location', 'supplemental_location_time', 'supplemental_location_sensor', 'supplemental_location_accuracy', 'road_snapped')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    LATLNG_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    BEARING_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    HEADING_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    SPEED_KMPH_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    SPEED_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    IS_ROAD_SNAPPED_FIELD_NUMBER: _ClassVar[int]
    IS_GPS_SENSOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIME_SINCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    NUM_STALE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_TIME_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ROAD_SNAPPED_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    horizontal_accuracy: _wrappers_pb2.DoubleValue
    latlng_accuracy: _wrappers_pb2.DoubleValue
    heading: _wrappers_pb2.Int32Value
    bearing_accuracy: _wrappers_pb2.DoubleValue
    heading_accuracy: _wrappers_pb2.DoubleValue
    altitude: _wrappers_pb2.DoubleValue
    vertical_accuracy: _wrappers_pb2.DoubleValue
    altitude_accuracy: _wrappers_pb2.DoubleValue
    speed_kmph: _wrappers_pb2.Int32Value
    speed: _wrappers_pb2.DoubleValue
    speed_accuracy: _wrappers_pb2.DoubleValue
    update_time: _timestamp_pb2.Timestamp
    server_time: _timestamp_pb2.Timestamp
    location_sensor: LocationSensor
    is_road_snapped: _wrappers_pb2.BoolValue
    is_gps_sensor_enabled: _wrappers_pb2.BoolValue
    time_since_update: _wrappers_pb2.Int32Value
    num_stale_updates: _wrappers_pb2.Int32Value
    raw_location: _latlng_pb2.LatLng
    raw_location_time: _timestamp_pb2.Timestamp
    raw_location_sensor: LocationSensor
    raw_location_accuracy: _wrappers_pb2.DoubleValue
    supplemental_location: _latlng_pb2.LatLng
    supplemental_location_time: _timestamp_pb2.Timestamp
    supplemental_location_sensor: LocationSensor
    supplemental_location_accuracy: _wrappers_pb2.DoubleValue
    road_snapped: bool

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., horizontal_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., latlng_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., heading: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., bearing_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., heading_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., altitude: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., vertical_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., altitude_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., speed_kmph: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., speed: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., speed_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., server_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., location_sensor: _Optional[_Union[LocationSensor, str]]=..., is_road_snapped: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., is_gps_sensor_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., time_since_update: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., num_stale_updates: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., raw_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., raw_location_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., raw_location_sensor: _Optional[_Union[LocationSensor, str]]=..., raw_location_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., supplemental_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., supplemental_location_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., supplemental_location_sensor: _Optional[_Union[LocationSensor, str]]=..., supplemental_location_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., road_snapped: bool=...) -> None:
        ...