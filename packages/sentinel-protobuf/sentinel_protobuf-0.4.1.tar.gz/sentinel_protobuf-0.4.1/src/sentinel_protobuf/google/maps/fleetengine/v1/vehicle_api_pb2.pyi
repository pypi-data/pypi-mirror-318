from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.geo.type import viewport_pb2 as _viewport_pb2
from google.maps.fleetengine.v1 import fleetengine_pb2 as _fleetengine_pb2
from google.maps.fleetengine.v1 import header_pb2 as _header_pb2
from google.maps.fleetengine.v1 import vehicles_pb2 as _vehicles_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateVehicleRequest(_message.Message):
    __slots__ = ('header', 'parent', 'vehicle_id', 'vehicle')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    parent: str
    vehicle_id: str
    vehicle: _vehicles_pb2.Vehicle

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., parent: _Optional[str]=..., vehicle_id: _Optional[str]=..., vehicle: _Optional[_Union[_vehicles_pb2.Vehicle, _Mapping]]=...) -> None:
        ...

class GetVehicleRequest(_message.Message):
    __slots__ = ('header', 'name', 'current_route_segment_version', 'waypoints_version')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_VERSION_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    name: str
    current_route_segment_version: _timestamp_pb2.Timestamp
    waypoints_version: _timestamp_pb2.Timestamp

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., name: _Optional[str]=..., current_route_segment_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., waypoints_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateVehicleRequest(_message.Message):
    __slots__ = ('header', 'name', 'vehicle', 'update_mask')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    name: str
    vehicle: _vehicles_pb2.Vehicle
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., name: _Optional[str]=..., vehicle: _Optional[_Union[_vehicles_pb2.Vehicle, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateVehicleAttributesRequest(_message.Message):
    __slots__ = ('header', 'name', 'attributes')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    name: str
    attributes: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.VehicleAttribute]

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., name: _Optional[str]=..., attributes: _Optional[_Iterable[_Union[_fleetengine_pb2.VehicleAttribute, _Mapping]]]=...) -> None:
        ...

class UpdateVehicleAttributesResponse(_message.Message):
    __slots__ = ('attributes',)
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.VehicleAttribute]

    def __init__(self, attributes: _Optional[_Iterable[_Union[_fleetengine_pb2.VehicleAttribute, _Mapping]]]=...) -> None:
        ...

class SearchVehiclesRequest(_message.Message):
    __slots__ = ('header', 'parent', 'pickup_point', 'dropoff_point', 'pickup_radius_meters', 'count', 'minimum_capacity', 'trip_types', 'maximum_staleness', 'vehicle_types', 'required_attributes', 'required_one_of_attributes', 'required_one_of_attribute_sets', 'order_by', 'include_back_to_back', 'trip_id', 'current_trips_present', 'filter')

    class VehicleMatchOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_VEHICLE_MATCH_ORDER: _ClassVar[SearchVehiclesRequest.VehicleMatchOrder]
        PICKUP_POINT_ETA: _ClassVar[SearchVehiclesRequest.VehicleMatchOrder]
        PICKUP_POINT_DISTANCE: _ClassVar[SearchVehiclesRequest.VehicleMatchOrder]
        DROPOFF_POINT_ETA: _ClassVar[SearchVehiclesRequest.VehicleMatchOrder]
        PICKUP_POINT_STRAIGHT_DISTANCE: _ClassVar[SearchVehiclesRequest.VehicleMatchOrder]
        COST: _ClassVar[SearchVehiclesRequest.VehicleMatchOrder]
    UNKNOWN_VEHICLE_MATCH_ORDER: SearchVehiclesRequest.VehicleMatchOrder
    PICKUP_POINT_ETA: SearchVehiclesRequest.VehicleMatchOrder
    PICKUP_POINT_DISTANCE: SearchVehiclesRequest.VehicleMatchOrder
    DROPOFF_POINT_ETA: SearchVehiclesRequest.VehicleMatchOrder
    PICKUP_POINT_STRAIGHT_DISTANCE: SearchVehiclesRequest.VehicleMatchOrder
    COST: SearchVehiclesRequest.VehicleMatchOrder

    class CurrentTripsPresent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURRENT_TRIPS_PRESENT_UNSPECIFIED: _ClassVar[SearchVehiclesRequest.CurrentTripsPresent]
        NONE: _ClassVar[SearchVehiclesRequest.CurrentTripsPresent]
        ANY: _ClassVar[SearchVehiclesRequest.CurrentTripsPresent]
    CURRENT_TRIPS_PRESENT_UNSPECIFIED: SearchVehiclesRequest.CurrentTripsPresent
    NONE: SearchVehiclesRequest.CurrentTripsPresent
    ANY: SearchVehiclesRequest.CurrentTripsPresent
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PICKUP_POINT_FIELD_NUMBER: _ClassVar[int]
    DROPOFF_POINT_FIELD_NUMBER: _ClassVar[int]
    PICKUP_RADIUS_METERS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    TRIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_STALENESS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_TYPES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ONE_OF_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ONE_OF_ATTRIBUTE_SETS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_BACK_TO_BACK_FIELD_NUMBER: _ClassVar[int]
    TRIP_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TRIPS_PRESENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    parent: str
    pickup_point: _fleetengine_pb2.TerminalLocation
    dropoff_point: _fleetengine_pb2.TerminalLocation
    pickup_radius_meters: int
    count: int
    minimum_capacity: int
    trip_types: _containers.RepeatedScalarFieldContainer[_fleetengine_pb2.TripType]
    maximum_staleness: _duration_pb2.Duration
    vehicle_types: _containers.RepeatedCompositeFieldContainer[_vehicles_pb2.Vehicle.VehicleType]
    required_attributes: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.VehicleAttribute]
    required_one_of_attributes: _containers.RepeatedCompositeFieldContainer[VehicleAttributeList]
    required_one_of_attribute_sets: _containers.RepeatedCompositeFieldContainer[VehicleAttributeList]
    order_by: SearchVehiclesRequest.VehicleMatchOrder
    include_back_to_back: bool
    trip_id: str
    current_trips_present: SearchVehiclesRequest.CurrentTripsPresent
    filter: str

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., parent: _Optional[str]=..., pickup_point: _Optional[_Union[_fleetengine_pb2.TerminalLocation, _Mapping]]=..., dropoff_point: _Optional[_Union[_fleetengine_pb2.TerminalLocation, _Mapping]]=..., pickup_radius_meters: _Optional[int]=..., count: _Optional[int]=..., minimum_capacity: _Optional[int]=..., trip_types: _Optional[_Iterable[_Union[_fleetengine_pb2.TripType, str]]]=..., maximum_staleness: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., vehicle_types: _Optional[_Iterable[_Union[_vehicles_pb2.Vehicle.VehicleType, _Mapping]]]=..., required_attributes: _Optional[_Iterable[_Union[_fleetengine_pb2.VehicleAttribute, _Mapping]]]=..., required_one_of_attributes: _Optional[_Iterable[_Union[VehicleAttributeList, _Mapping]]]=..., required_one_of_attribute_sets: _Optional[_Iterable[_Union[VehicleAttributeList, _Mapping]]]=..., order_by: _Optional[_Union[SearchVehiclesRequest.VehicleMatchOrder, str]]=..., include_back_to_back: bool=..., trip_id: _Optional[str]=..., current_trips_present: _Optional[_Union[SearchVehiclesRequest.CurrentTripsPresent, str]]=..., filter: _Optional[str]=...) -> None:
        ...

class SearchVehiclesResponse(_message.Message):
    __slots__ = ('matches',)
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[VehicleMatch]

    def __init__(self, matches: _Optional[_Iterable[_Union[VehicleMatch, _Mapping]]]=...) -> None:
        ...

class ListVehiclesRequest(_message.Message):
    __slots__ = ('header', 'parent', 'page_size', 'page_token', 'minimum_capacity', 'trip_types', 'maximum_staleness', 'vehicle_type_categories', 'required_attributes', 'required_one_of_attributes', 'required_one_of_attribute_sets', 'vehicle_state', 'on_trip_only', 'filter', 'viewport')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    TRIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_STALENESS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_TYPE_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ONE_OF_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ONE_OF_ATTRIBUTE_SETS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_STATE_FIELD_NUMBER: _ClassVar[int]
    ON_TRIP_ONLY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    parent: str
    page_size: int
    page_token: str
    minimum_capacity: _wrappers_pb2.Int32Value
    trip_types: _containers.RepeatedScalarFieldContainer[_fleetengine_pb2.TripType]
    maximum_staleness: _duration_pb2.Duration
    vehicle_type_categories: _containers.RepeatedScalarFieldContainer[_vehicles_pb2.Vehicle.VehicleType.Category]
    required_attributes: _containers.RepeatedScalarFieldContainer[str]
    required_one_of_attributes: _containers.RepeatedScalarFieldContainer[str]
    required_one_of_attribute_sets: _containers.RepeatedScalarFieldContainer[str]
    vehicle_state: _vehicles_pb2.VehicleState
    on_trip_only: bool
    filter: str
    viewport: _viewport_pb2.Viewport

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., minimum_capacity: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., trip_types: _Optional[_Iterable[_Union[_fleetengine_pb2.TripType, str]]]=..., maximum_staleness: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., vehicle_type_categories: _Optional[_Iterable[_Union[_vehicles_pb2.Vehicle.VehicleType.Category, str]]]=..., required_attributes: _Optional[_Iterable[str]]=..., required_one_of_attributes: _Optional[_Iterable[str]]=..., required_one_of_attribute_sets: _Optional[_Iterable[str]]=..., vehicle_state: _Optional[_Union[_vehicles_pb2.VehicleState, str]]=..., on_trip_only: bool=..., filter: _Optional[str]=..., viewport: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]]=...) -> None:
        ...

class ListVehiclesResponse(_message.Message):
    __slots__ = ('vehicles', 'next_page_token', 'total_size')
    VEHICLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    vehicles: _containers.RepeatedCompositeFieldContainer[_vehicles_pb2.Vehicle]
    next_page_token: str
    total_size: int

    def __init__(self, vehicles: _Optional[_Iterable[_Union[_vehicles_pb2.Vehicle, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class Waypoint(_message.Message):
    __slots__ = ('lat_lng', 'eta')
    LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    ETA_FIELD_NUMBER: _ClassVar[int]
    lat_lng: _latlng_pb2.LatLng
    eta: _timestamp_pb2.Timestamp

    def __init__(self, lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., eta: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class VehicleMatch(_message.Message):
    __slots__ = ('vehicle', 'vehicle_pickup_eta', 'vehicle_pickup_distance_meters', 'vehicle_pickup_straight_line_distance_meters', 'vehicle_dropoff_eta', 'vehicle_pickup_to_dropoff_distance_meters', 'trip_type', 'vehicle_trips_waypoints', 'vehicle_match_type', 'requested_ordered_by', 'ordered_by')

    class VehicleMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[VehicleMatch.VehicleMatchType]
        EXCLUSIVE: _ClassVar[VehicleMatch.VehicleMatchType]
        BACK_TO_BACK: _ClassVar[VehicleMatch.VehicleMatchType]
        CARPOOL: _ClassVar[VehicleMatch.VehicleMatchType]
        CARPOOL_BACK_TO_BACK: _ClassVar[VehicleMatch.VehicleMatchType]
    UNKNOWN: VehicleMatch.VehicleMatchType
    EXCLUSIVE: VehicleMatch.VehicleMatchType
    BACK_TO_BACK: VehicleMatch.VehicleMatchType
    CARPOOL: VehicleMatch.VehicleMatchType
    CARPOOL_BACK_TO_BACK: VehicleMatch.VehicleMatchType
    VEHICLE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_PICKUP_ETA_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_PICKUP_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_PICKUP_STRAIGHT_LINE_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_DROPOFF_ETA_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_PICKUP_TO_DROPOFF_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    TRIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_TRIPS_WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_ORDERED_BY_FIELD_NUMBER: _ClassVar[int]
    ORDERED_BY_FIELD_NUMBER: _ClassVar[int]
    vehicle: _vehicles_pb2.Vehicle
    vehicle_pickup_eta: _timestamp_pb2.Timestamp
    vehicle_pickup_distance_meters: _wrappers_pb2.Int32Value
    vehicle_pickup_straight_line_distance_meters: _wrappers_pb2.Int32Value
    vehicle_dropoff_eta: _timestamp_pb2.Timestamp
    vehicle_pickup_to_dropoff_distance_meters: _wrappers_pb2.Int32Value
    trip_type: _fleetengine_pb2.TripType
    vehicle_trips_waypoints: _containers.RepeatedCompositeFieldContainer[Waypoint]
    vehicle_match_type: VehicleMatch.VehicleMatchType
    requested_ordered_by: SearchVehiclesRequest.VehicleMatchOrder
    ordered_by: SearchVehiclesRequest.VehicleMatchOrder

    def __init__(self, vehicle: _Optional[_Union[_vehicles_pb2.Vehicle, _Mapping]]=..., vehicle_pickup_eta: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., vehicle_pickup_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., vehicle_pickup_straight_line_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., vehicle_dropoff_eta: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., vehicle_pickup_to_dropoff_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., trip_type: _Optional[_Union[_fleetengine_pb2.TripType, str]]=..., vehicle_trips_waypoints: _Optional[_Iterable[_Union[Waypoint, _Mapping]]]=..., vehicle_match_type: _Optional[_Union[VehicleMatch.VehicleMatchType, str]]=..., requested_ordered_by: _Optional[_Union[SearchVehiclesRequest.VehicleMatchOrder, str]]=..., ordered_by: _Optional[_Union[SearchVehiclesRequest.VehicleMatchOrder, str]]=...) -> None:
        ...

class VehicleAttributeList(_message.Message):
    __slots__ = ('attributes',)
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_fleetengine_pb2.VehicleAttribute]

    def __init__(self, attributes: _Optional[_Iterable[_Union[_fleetengine_pb2.VehicleAttribute, _Mapping]]]=...) -> None:
        ...