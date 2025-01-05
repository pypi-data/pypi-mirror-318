from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.routes.v1 import polyline_pb2 as _polyline_pb2
from google.maps.routes.v1 import toll_passes_pb2 as _toll_passes_pb2
from google.maps.routes.v1 import vehicle_emission_type_pb2 as _vehicle_emission_type_pb2
from google.maps.routes.v1 import waypoint_pb2 as _waypoint_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RouteTravelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAVEL_MODE_UNSPECIFIED: _ClassVar[RouteTravelMode]
    DRIVE: _ClassVar[RouteTravelMode]
    BICYCLE: _ClassVar[RouteTravelMode]
    WALK: _ClassVar[RouteTravelMode]
    TWO_WHEELER: _ClassVar[RouteTravelMode]
    TAXI: _ClassVar[RouteTravelMode]

class RoutingPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_PREFERENCE_UNSPECIFIED: _ClassVar[RoutingPreference]
    TRAFFIC_UNAWARE: _ClassVar[RoutingPreference]
    TRAFFIC_AWARE: _ClassVar[RoutingPreference]
    TRAFFIC_AWARE_OPTIMAL: _ClassVar[RoutingPreference]

class Units(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNITS_UNSPECIFIED: _ClassVar[Units]
    METRIC: _ClassVar[Units]
    IMPERIAL: _ClassVar[Units]
TRAVEL_MODE_UNSPECIFIED: RouteTravelMode
DRIVE: RouteTravelMode
BICYCLE: RouteTravelMode
WALK: RouteTravelMode
TWO_WHEELER: RouteTravelMode
TAXI: RouteTravelMode
ROUTING_PREFERENCE_UNSPECIFIED: RoutingPreference
TRAFFIC_UNAWARE: RoutingPreference
TRAFFIC_AWARE: RoutingPreference
TRAFFIC_AWARE_OPTIMAL: RoutingPreference
UNITS_UNSPECIFIED: Units
METRIC: Units
IMPERIAL: Units

class ComputeRoutesRequest(_message.Message):
    __slots__ = ('origin', 'destination', 'intermediates', 'travel_mode', 'routing_preference', 'polyline_quality', 'polyline_encoding', 'departure_time', 'compute_alternative_routes', 'route_modifiers', 'language_code', 'units', 'optimize_waypoint_order')
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATES_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ALTERNATIVE_ROUTES_FIELD_NUMBER: _ClassVar[int]
    ROUTE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_WAYPOINT_ORDER_FIELD_NUMBER: _ClassVar[int]
    origin: _waypoint_pb2.Waypoint
    destination: _waypoint_pb2.Waypoint
    intermediates: _containers.RepeatedCompositeFieldContainer[_waypoint_pb2.Waypoint]
    travel_mode: RouteTravelMode
    routing_preference: RoutingPreference
    polyline_quality: _polyline_pb2.PolylineQuality
    polyline_encoding: _polyline_pb2.PolylineEncoding
    departure_time: _timestamp_pb2.Timestamp
    compute_alternative_routes: bool
    route_modifiers: RouteModifiers
    language_code: str
    units: Units
    optimize_waypoint_order: bool

    def __init__(self, origin: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]]=..., destination: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]]=..., intermediates: _Optional[_Iterable[_Union[_waypoint_pb2.Waypoint, _Mapping]]]=..., travel_mode: _Optional[_Union[RouteTravelMode, str]]=..., routing_preference: _Optional[_Union[RoutingPreference, str]]=..., polyline_quality: _Optional[_Union[_polyline_pb2.PolylineQuality, str]]=..., polyline_encoding: _Optional[_Union[_polyline_pb2.PolylineEncoding, str]]=..., departure_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., compute_alternative_routes: bool=..., route_modifiers: _Optional[_Union[RouteModifiers, _Mapping]]=..., language_code: _Optional[str]=..., units: _Optional[_Union[Units, str]]=..., optimize_waypoint_order: bool=...) -> None:
        ...

class RouteModifiers(_message.Message):
    __slots__ = ('avoid_tolls', 'avoid_highways', 'avoid_ferries', 'avoid_indoor', 'vehicle_info', 'toll_passes')
    AVOID_TOLLS_FIELD_NUMBER: _ClassVar[int]
    AVOID_HIGHWAYS_FIELD_NUMBER: _ClassVar[int]
    AVOID_FERRIES_FIELD_NUMBER: _ClassVar[int]
    AVOID_INDOOR_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_INFO_FIELD_NUMBER: _ClassVar[int]
    TOLL_PASSES_FIELD_NUMBER: _ClassVar[int]
    avoid_tolls: bool
    avoid_highways: bool
    avoid_ferries: bool
    avoid_indoor: bool
    vehicle_info: VehicleInfo
    toll_passes: _containers.RepeatedScalarFieldContainer[_toll_passes_pb2.TollPass]

    def __init__(self, avoid_tolls: bool=..., avoid_highways: bool=..., avoid_ferries: bool=..., avoid_indoor: bool=..., vehicle_info: _Optional[_Union[VehicleInfo, _Mapping]]=..., toll_passes: _Optional[_Iterable[_Union[_toll_passes_pb2.TollPass, str]]]=...) -> None:
        ...

class VehicleInfo(_message.Message):
    __slots__ = ('license_plate_last_character', 'emission_type')
    LICENSE_PLATE_LAST_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    EMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    license_plate_last_character: str
    emission_type: _vehicle_emission_type_pb2.VehicleEmissionType

    def __init__(self, license_plate_last_character: _Optional[str]=..., emission_type: _Optional[_Union[_vehicle_emission_type_pb2.VehicleEmissionType, str]]=...) -> None:
        ...