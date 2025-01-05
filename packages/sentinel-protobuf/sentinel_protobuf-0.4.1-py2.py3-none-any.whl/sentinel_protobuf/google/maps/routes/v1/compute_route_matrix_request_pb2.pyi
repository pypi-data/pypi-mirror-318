from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.routes.v1 import compute_routes_request_pb2 as _compute_routes_request_pb2
from google.maps.routes.v1 import waypoint_pb2 as _waypoint_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeRouteMatrixRequest(_message.Message):
    __slots__ = ('origins', 'destinations', 'travel_mode', 'routing_preference', 'departure_time')
    ORIGINS_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    origins: _containers.RepeatedCompositeFieldContainer[RouteMatrixOrigin]
    destinations: _containers.RepeatedCompositeFieldContainer[RouteMatrixDestination]
    travel_mode: _compute_routes_request_pb2.RouteTravelMode
    routing_preference: _compute_routes_request_pb2.RoutingPreference
    departure_time: _timestamp_pb2.Timestamp

    def __init__(self, origins: _Optional[_Iterable[_Union[RouteMatrixOrigin, _Mapping]]]=..., destinations: _Optional[_Iterable[_Union[RouteMatrixDestination, _Mapping]]]=..., travel_mode: _Optional[_Union[_compute_routes_request_pb2.RouteTravelMode, str]]=..., routing_preference: _Optional[_Union[_compute_routes_request_pb2.RoutingPreference, str]]=..., departure_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RouteMatrixOrigin(_message.Message):
    __slots__ = ('waypoint', 'route_modifiers')
    WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    waypoint: _waypoint_pb2.Waypoint
    route_modifiers: _compute_routes_request_pb2.RouteModifiers

    def __init__(self, waypoint: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]]=..., route_modifiers: _Optional[_Union[_compute_routes_request_pb2.RouteModifiers, _Mapping]]=...) -> None:
        ...

class RouteMatrixDestination(_message.Message):
    __slots__ = ('waypoint',)
    WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    waypoint: _waypoint_pb2.Waypoint

    def __init__(self, waypoint: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]]=...) -> None:
        ...