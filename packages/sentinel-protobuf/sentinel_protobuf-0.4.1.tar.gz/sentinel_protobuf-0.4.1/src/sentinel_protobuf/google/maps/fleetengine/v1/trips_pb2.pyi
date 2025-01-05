from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.maps.fleetengine.v1 import fleetengine_pb2 as _fleetengine_pb2
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

class TripStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TRIP_STATUS: _ClassVar[TripStatus]
    NEW: _ClassVar[TripStatus]
    ENROUTE_TO_PICKUP: _ClassVar[TripStatus]
    ARRIVED_AT_PICKUP: _ClassVar[TripStatus]
    ARRIVED_AT_INTERMEDIATE_DESTINATION: _ClassVar[TripStatus]
    ENROUTE_TO_INTERMEDIATE_DESTINATION: _ClassVar[TripStatus]
    ENROUTE_TO_DROPOFF: _ClassVar[TripStatus]
    COMPLETE: _ClassVar[TripStatus]
    CANCELED: _ClassVar[TripStatus]

class BillingPlatformIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BILLING_PLATFORM_IDENTIFIER_UNSPECIFIED: _ClassVar[BillingPlatformIdentifier]
    SERVER: _ClassVar[BillingPlatformIdentifier]
    WEB: _ClassVar[BillingPlatformIdentifier]
    ANDROID: _ClassVar[BillingPlatformIdentifier]
    IOS: _ClassVar[BillingPlatformIdentifier]
    OTHERS: _ClassVar[BillingPlatformIdentifier]

class TripView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIP_VIEW_UNSPECIFIED: _ClassVar[TripView]
    SDK: _ClassVar[TripView]
    JOURNEY_SHARING_V1S: _ClassVar[TripView]
UNKNOWN_TRIP_STATUS: TripStatus
NEW: TripStatus
ENROUTE_TO_PICKUP: TripStatus
ARRIVED_AT_PICKUP: TripStatus
ARRIVED_AT_INTERMEDIATE_DESTINATION: TripStatus
ENROUTE_TO_INTERMEDIATE_DESTINATION: TripStatus
ENROUTE_TO_DROPOFF: TripStatus
COMPLETE: TripStatus
CANCELED: TripStatus
BILLING_PLATFORM_IDENTIFIER_UNSPECIFIED: BillingPlatformIdentifier
SERVER: BillingPlatformIdentifier
WEB: BillingPlatformIdentifier
ANDROID: BillingPlatformIdentifier
IOS: BillingPlatformIdentifier
OTHERS: BillingPlatformIdentifier
TRIP_VIEW_UNSPECIFIED: TripView
SDK: TripView
JOURNEY_SHARING_V1S: TripView

class Trip(_message.Message):
    __slots__ = ('name', 'vehicle_id', 'trip_status', 'trip_type', 'pickup_point', 'actual_pickup_point', 'actual_pickup_arrival_point', 'pickup_time', 'intermediate_destinations', 'intermediate_destinations_version', 'intermediate_destination_index', 'actual_intermediate_destination_arrival_points', 'actual_intermediate_destinations', 'dropoff_point', 'actual_dropoff_point', 'dropoff_time', 'remaining_waypoints', 'vehicle_waypoints', 'route', 'current_route_segment', 'current_route_segment_version', 'current_route_segment_traffic', 'current_route_segment_traffic_version', 'current_route_segment_end_point', 'remaining_distance_meters', 'eta_to_first_waypoint', 'remaining_time_to_first_waypoint', 'remaining_waypoints_version', 'remaining_waypoints_route_version', 'number_of_passengers', 'last_location', 'last_location_snappable', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    TRIP_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    PICKUP_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_PICKUP_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_PICKUP_ARRIVAL_POINT_FIELD_NUMBER: _ClassVar[int]
    PICKUP_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_DESTINATIONS_VERSION_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_DESTINATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_INTERMEDIATE_DESTINATION_ARRIVAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_INTERMEDIATE_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    DROPOFF_POINT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DROPOFF_POINT_FIELD_NUMBER: _ClassVar[int]
    DROPOFF_TIME_FIELD_NUMBER: _ClassVar[int]
    REMAINING_WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_TRAFFIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_END_POINT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    ETA_TO_FIRST_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_TIME_TO_FIRST_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_WAYPOINTS_VERSION_FIELD_NUMBER: _ClassVar[int]
    REMAINING_WAYPOINTS_ROUTE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_PASSENGERS_FIELD_NUMBER: _ClassVar[int]
    LAST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    LAST_LOCATION_SNAPPABLE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    vehicle_id: str
    trip_status: TripStatus
    trip_type: _fleetengine_pb2.TripType
    pickup_point: _fleetengine_pb2.TerminalLocation
    actual_pickup_point: StopLocation
    actual_pickup_arrival_point: StopLocation
    pickup_time: _timestamp_pb2.Timestamp
    intermediate_destinations: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.TerminalLocation]
    intermediate_destinations_version: _timestamp_pb2.Timestamp
    intermediate_destination_index: int
    actual_intermediate_destination_arrival_points: _containers.RepeatedCompositeFieldContainer[StopLocation]
    actual_intermediate_destinations: _containers.RepeatedCompositeFieldContainer[StopLocation]
    dropoff_point: _fleetengine_pb2.TerminalLocation
    actual_dropoff_point: StopLocation
    dropoff_time: _timestamp_pb2.Timestamp
    remaining_waypoints: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.TripWaypoint]
    vehicle_waypoints: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.TripWaypoint]
    route: _containers.RepeatedCompositeFieldContainer[_latlng_pb2.LatLng]
    current_route_segment: str
    current_route_segment_version: _timestamp_pb2.Timestamp
    current_route_segment_traffic: _traffic_pb2.ConsumableTrafficPolyline
    current_route_segment_traffic_version: _timestamp_pb2.Timestamp
    current_route_segment_end_point: _fleetengine_pb2.TripWaypoint
    remaining_distance_meters: _wrappers_pb2.Int32Value
    eta_to_first_waypoint: _timestamp_pb2.Timestamp
    remaining_time_to_first_waypoint: _duration_pb2.Duration
    remaining_waypoints_version: _timestamp_pb2.Timestamp
    remaining_waypoints_route_version: _timestamp_pb2.Timestamp
    number_of_passengers: int
    last_location: _fleetengine_pb2.VehicleLocation
    last_location_snappable: bool
    view: TripView

    def __init__(self, name: _Optional[str]=..., vehicle_id: _Optional[str]=..., trip_status: _Optional[_Union[TripStatus, str]]=..., trip_type: _Optional[_Union[_fleetengine_pb2.TripType, str]]=..., pickup_point: _Optional[_Union[_fleetengine_pb2.TerminalLocation, _Mapping]]=..., actual_pickup_point: _Optional[_Union[StopLocation, _Mapping]]=..., actual_pickup_arrival_point: _Optional[_Union[StopLocation, _Mapping]]=..., pickup_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., intermediate_destinations: _Optional[_Iterable[_Union[_fleetengine_pb2.TerminalLocation, _Mapping]]]=..., intermediate_destinations_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., intermediate_destination_index: _Optional[int]=..., actual_intermediate_destination_arrival_points: _Optional[_Iterable[_Union[StopLocation, _Mapping]]]=..., actual_intermediate_destinations: _Optional[_Iterable[_Union[StopLocation, _Mapping]]]=..., dropoff_point: _Optional[_Union[_fleetengine_pb2.TerminalLocation, _Mapping]]=..., actual_dropoff_point: _Optional[_Union[StopLocation, _Mapping]]=..., dropoff_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., remaining_waypoints: _Optional[_Iterable[_Union[_fleetengine_pb2.TripWaypoint, _Mapping]]]=..., vehicle_waypoints: _Optional[_Iterable[_Union[_fleetengine_pb2.TripWaypoint, _Mapping]]]=..., route: _Optional[_Iterable[_Union[_latlng_pb2.LatLng, _Mapping]]]=..., current_route_segment: _Optional[str]=..., current_route_segment_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., current_route_segment_traffic: _Optional[_Union[_traffic_pb2.ConsumableTrafficPolyline, _Mapping]]=..., current_route_segment_traffic_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., current_route_segment_end_point: _Optional[_Union[_fleetengine_pb2.TripWaypoint, _Mapping]]=..., remaining_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., eta_to_first_waypoint: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., remaining_time_to_first_waypoint: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., remaining_waypoints_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., remaining_waypoints_route_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., number_of_passengers: _Optional[int]=..., last_location: _Optional[_Union[_fleetengine_pb2.VehicleLocation, _Mapping]]=..., last_location_snappable: bool=..., view: _Optional[_Union[TripView, str]]=...) -> None:
        ...

class StopLocation(_message.Message):
    __slots__ = ('point', 'timestamp', 'stop_time')
    POINT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    point: _latlng_pb2.LatLng
    timestamp: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp

    def __init__(self, point: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., stop_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...