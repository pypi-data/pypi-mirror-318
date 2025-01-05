from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.maps.fleetengine.v1 import fleetengine_pb2 as _fleetengine_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VehicleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_VEHICLE_STATE: _ClassVar[VehicleState]
    OFFLINE: _ClassVar[VehicleState]
    ONLINE: _ClassVar[VehicleState]

class LocationPowerSaveMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_LOCATION_POWER_SAVE_MODE: _ClassVar[LocationPowerSaveMode]
    LOCATION_MODE_NO_CHANGE: _ClassVar[LocationPowerSaveMode]
    LOCATION_MODE_GPS_DISABLED_WHEN_SCREEN_OFF: _ClassVar[LocationPowerSaveMode]
    LOCATION_MODE_ALL_DISABLED_WHEN_SCREEN_OFF: _ClassVar[LocationPowerSaveMode]
    LOCATION_MODE_FOREGROUND_ONLY: _ClassVar[LocationPowerSaveMode]
    LOCATION_MODE_THROTTLE_REQUESTS_WHEN_SCREEN_OFF: _ClassVar[LocationPowerSaveMode]

class BatteryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_BATTERY_STATUS: _ClassVar[BatteryStatus]
    BATTERY_STATUS_CHARGING: _ClassVar[BatteryStatus]
    BATTERY_STATUS_DISCHARGING: _ClassVar[BatteryStatus]
    BATTERY_STATUS_FULL: _ClassVar[BatteryStatus]
    BATTERY_STATUS_NOT_CHARGING: _ClassVar[BatteryStatus]
    BATTERY_STATUS_POWER_LOW: _ClassVar[BatteryStatus]

class PowerSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_POWER_SOURCE: _ClassVar[PowerSource]
    POWER_SOURCE_AC: _ClassVar[PowerSource]
    POWER_SOURCE_USB: _ClassVar[PowerSource]
    POWER_SOURCE_WIRELESS: _ClassVar[PowerSource]
    POWER_SOURCE_UNPLUGGED: _ClassVar[PowerSource]
UNKNOWN_VEHICLE_STATE: VehicleState
OFFLINE: VehicleState
ONLINE: VehicleState
UNKNOWN_LOCATION_POWER_SAVE_MODE: LocationPowerSaveMode
LOCATION_MODE_NO_CHANGE: LocationPowerSaveMode
LOCATION_MODE_GPS_DISABLED_WHEN_SCREEN_OFF: LocationPowerSaveMode
LOCATION_MODE_ALL_DISABLED_WHEN_SCREEN_OFF: LocationPowerSaveMode
LOCATION_MODE_FOREGROUND_ONLY: LocationPowerSaveMode
LOCATION_MODE_THROTTLE_REQUESTS_WHEN_SCREEN_OFF: LocationPowerSaveMode
UNKNOWN_BATTERY_STATUS: BatteryStatus
BATTERY_STATUS_CHARGING: BatteryStatus
BATTERY_STATUS_DISCHARGING: BatteryStatus
BATTERY_STATUS_FULL: BatteryStatus
BATTERY_STATUS_NOT_CHARGING: BatteryStatus
BATTERY_STATUS_POWER_LOW: BatteryStatus
UNKNOWN_POWER_SOURCE: PowerSource
POWER_SOURCE_AC: PowerSource
POWER_SOURCE_USB: PowerSource
POWER_SOURCE_WIRELESS: PowerSource
POWER_SOURCE_UNPLUGGED: PowerSource

class Vehicle(_message.Message):
    __slots__ = ('name', 'vehicle_state', 'supported_trip_types', 'current_trips', 'last_location', 'maximum_capacity', 'attributes', 'vehicle_type', 'license_plate', 'route', 'current_route_segment', 'current_route_segment_traffic', 'current_route_segment_version', 'current_route_segment_end_point', 'remaining_distance_meters', 'eta_to_first_waypoint', 'remaining_time_seconds', 'waypoints', 'waypoints_version', 'back_to_back_enabled', 'navigation_status', 'device_settings')

    class VehicleType(_message.Message):
        __slots__ = ('category',)

        class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[Vehicle.VehicleType.Category]
            AUTO: _ClassVar[Vehicle.VehicleType.Category]
            TAXI: _ClassVar[Vehicle.VehicleType.Category]
            TRUCK: _ClassVar[Vehicle.VehicleType.Category]
            TWO_WHEELER: _ClassVar[Vehicle.VehicleType.Category]
            BICYCLE: _ClassVar[Vehicle.VehicleType.Category]
            PEDESTRIAN: _ClassVar[Vehicle.VehicleType.Category]
        UNKNOWN: Vehicle.VehicleType.Category
        AUTO: Vehicle.VehicleType.Category
        TAXI: Vehicle.VehicleType.Category
        TRUCK: Vehicle.VehicleType.Category
        TWO_WHEELER: Vehicle.VehicleType.Category
        BICYCLE: Vehicle.VehicleType.Category
        PEDESTRIAN: Vehicle.VehicleType.Category
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        category: Vehicle.VehicleType.Category

        def __init__(self, category: _Optional[_Union[Vehicle.VehicleType.Category, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_STATE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TRIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TRIPS_FIELD_NUMBER: _ClassVar[int]
    LAST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_PLATE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_END_POINT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    ETA_TO_FIRST_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_VERSION_FIELD_NUMBER: _ClassVar[int]
    BACK_TO_BACK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    vehicle_state: VehicleState
    supported_trip_types: _containers.RepeatedScalarFieldContainer[_fleetengine_pb2.TripType]
    current_trips: _containers.RepeatedScalarFieldContainer[str]
    last_location: _fleetengine_pb2.VehicleLocation
    maximum_capacity: int
    attributes: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.VehicleAttribute]
    vehicle_type: Vehicle.VehicleType
    license_plate: LicensePlate
    route: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.TerminalLocation]
    current_route_segment: str
    current_route_segment_traffic: TrafficPolylineData
    current_route_segment_version: _timestamp_pb2.Timestamp
    current_route_segment_end_point: _fleetengine_pb2.TripWaypoint
    remaining_distance_meters: _wrappers_pb2.Int32Value
    eta_to_first_waypoint: _timestamp_pb2.Timestamp
    remaining_time_seconds: _wrappers_pb2.Int32Value
    waypoints: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.TripWaypoint]
    waypoints_version: _timestamp_pb2.Timestamp
    back_to_back_enabled: bool
    navigation_status: _fleetengine_pb2.NavigationStatus
    device_settings: DeviceSettings

    def __init__(self, name: _Optional[str]=..., vehicle_state: _Optional[_Union[VehicleState, str]]=..., supported_trip_types: _Optional[_Iterable[_Union[_fleetengine_pb2.TripType, str]]]=..., current_trips: _Optional[_Iterable[str]]=..., last_location: _Optional[_Union[_fleetengine_pb2.VehicleLocation, _Mapping]]=..., maximum_capacity: _Optional[int]=..., attributes: _Optional[_Iterable[_Union[_fleetengine_pb2.VehicleAttribute, _Mapping]]]=..., vehicle_type: _Optional[_Union[Vehicle.VehicleType, _Mapping]]=..., license_plate: _Optional[_Union[LicensePlate, _Mapping]]=..., route: _Optional[_Iterable[_Union[_fleetengine_pb2.TerminalLocation, _Mapping]]]=..., current_route_segment: _Optional[str]=..., current_route_segment_traffic: _Optional[_Union[TrafficPolylineData, _Mapping]]=..., current_route_segment_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., current_route_segment_end_point: _Optional[_Union[_fleetengine_pb2.TripWaypoint, _Mapping]]=..., remaining_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., eta_to_first_waypoint: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., remaining_time_seconds: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., waypoints: _Optional[_Iterable[_Union[_fleetengine_pb2.TripWaypoint, _Mapping]]]=..., waypoints_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., back_to_back_enabled: bool=..., navigation_status: _Optional[_Union[_fleetengine_pb2.NavigationStatus, str]]=..., device_settings: _Optional[_Union[DeviceSettings, _Mapping]]=...) -> None:
        ...

class BatteryInfo(_message.Message):
    __slots__ = ('battery_status', 'power_source', 'battery_percentage')
    BATTERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    POWER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    battery_status: BatteryStatus
    power_source: PowerSource
    battery_percentage: float

    def __init__(self, battery_status: _Optional[_Union[BatteryStatus, str]]=..., power_source: _Optional[_Union[PowerSource, str]]=..., battery_percentage: _Optional[float]=...) -> None:
        ...

class DeviceSettings(_message.Message):
    __slots__ = ('location_power_save_mode', 'is_power_save_mode', 'is_interactive', 'battery_info')
    LOCATION_POWER_SAVE_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_POWER_SAVE_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_INTERACTIVE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_INFO_FIELD_NUMBER: _ClassVar[int]
    location_power_save_mode: LocationPowerSaveMode
    is_power_save_mode: bool
    is_interactive: bool
    battery_info: BatteryInfo

    def __init__(self, location_power_save_mode: _Optional[_Union[LocationPowerSaveMode, str]]=..., is_power_save_mode: bool=..., is_interactive: bool=..., battery_info: _Optional[_Union[BatteryInfo, _Mapping]]=...) -> None:
        ...

class LicensePlate(_message.Message):
    __slots__ = ('country_code', 'last_character')
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LAST_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    last_character: str

    def __init__(self, country_code: _Optional[str]=..., last_character: _Optional[str]=...) -> None:
        ...

class VisualTrafficReportPolylineRendering(_message.Message):
    __slots__ = ('road_stretch',)

    class RoadStretch(_message.Message):
        __slots__ = ('style', 'offset_meters', 'length_meters')

        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STYLE_UNSPECIFIED: _ClassVar[VisualTrafficReportPolylineRendering.RoadStretch.Style]
            SLOWER_TRAFFIC: _ClassVar[VisualTrafficReportPolylineRendering.RoadStretch.Style]
            TRAFFIC_JAM: _ClassVar[VisualTrafficReportPolylineRendering.RoadStretch.Style]
        STYLE_UNSPECIFIED: VisualTrafficReportPolylineRendering.RoadStretch.Style
        SLOWER_TRAFFIC: VisualTrafficReportPolylineRendering.RoadStretch.Style
        TRAFFIC_JAM: VisualTrafficReportPolylineRendering.RoadStretch.Style
        STYLE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_METERS_FIELD_NUMBER: _ClassVar[int]
        LENGTH_METERS_FIELD_NUMBER: _ClassVar[int]
        style: VisualTrafficReportPolylineRendering.RoadStretch.Style
        offset_meters: int
        length_meters: int

        def __init__(self, style: _Optional[_Union[VisualTrafficReportPolylineRendering.RoadStretch.Style, str]]=..., offset_meters: _Optional[int]=..., length_meters: _Optional[int]=...) -> None:
            ...
    ROAD_STRETCH_FIELD_NUMBER: _ClassVar[int]
    road_stretch: _containers.RepeatedCompositeFieldContainer[VisualTrafficReportPolylineRendering.RoadStretch]

    def __init__(self, road_stretch: _Optional[_Iterable[_Union[VisualTrafficReportPolylineRendering.RoadStretch, _Mapping]]]=...) -> None:
        ...

class TrafficPolylineData(_message.Message):
    __slots__ = ('traffic_rendering',)
    TRAFFIC_RENDERING_FIELD_NUMBER: _ClassVar[int]
    traffic_rendering: VisualTrafficReportPolylineRendering

    def __init__(self, traffic_rendering: _Optional[_Union[VisualTrafficReportPolylineRendering, _Mapping]]=...) -> None:
        ...