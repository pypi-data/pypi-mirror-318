from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.routing.v2 import fallback_info_pb2 as _fallback_info_pb2
from google.maps.routing.v2 import geocoding_results_pb2 as _geocoding_results_pb2
from google.maps.routing.v2 import polyline_pb2 as _polyline_pb2
from google.maps.routing.v2 import route_pb2 as _route_pb2
from google.maps.routing.v2 import route_modifiers_pb2 as _route_modifiers_pb2
from google.maps.routing.v2 import route_travel_mode_pb2 as _route_travel_mode_pb2
from google.maps.routing.v2 import routing_preference_pb2 as _routing_preference_pb2
from google.maps.routing.v2 import traffic_model_pb2 as _traffic_model_pb2
from google.maps.routing.v2 import transit_preferences_pb2 as _transit_preferences_pb2
from google.maps.routing.v2 import units_pb2 as _units_pb2
from google.maps.routing.v2 import waypoint_pb2 as _waypoint_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RouteMatrixElementCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED: _ClassVar[RouteMatrixElementCondition]
    ROUTE_EXISTS: _ClassVar[RouteMatrixElementCondition]
    ROUTE_NOT_FOUND: _ClassVar[RouteMatrixElementCondition]
ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED: RouteMatrixElementCondition
ROUTE_EXISTS: RouteMatrixElementCondition
ROUTE_NOT_FOUND: RouteMatrixElementCondition

class ComputeRoutesRequest(_message.Message):
    __slots__ = ("origin", "destination", "intermediates", "travel_mode", "routing_preference", "polyline_quality", "polyline_encoding", "departure_time", "arrival_time", "compute_alternative_routes", "route_modifiers", "language_code", "region_code", "units", "optimize_waypoint_order", "requested_reference_routes", "extra_computations", "traffic_model", "transit_preferences")
    class ReferenceRoute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REFERENCE_ROUTE_UNSPECIFIED: _ClassVar[ComputeRoutesRequest.ReferenceRoute]
        FUEL_EFFICIENT: _ClassVar[ComputeRoutesRequest.ReferenceRoute]
        SHORTER_DISTANCE: _ClassVar[ComputeRoutesRequest.ReferenceRoute]
    REFERENCE_ROUTE_UNSPECIFIED: ComputeRoutesRequest.ReferenceRoute
    FUEL_EFFICIENT: ComputeRoutesRequest.ReferenceRoute
    SHORTER_DISTANCE: ComputeRoutesRequest.ReferenceRoute
    class ExtraComputation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTRA_COMPUTATION_UNSPECIFIED: _ClassVar[ComputeRoutesRequest.ExtraComputation]
        TOLLS: _ClassVar[ComputeRoutesRequest.ExtraComputation]
        FUEL_CONSUMPTION: _ClassVar[ComputeRoutesRequest.ExtraComputation]
        TRAFFIC_ON_POLYLINE: _ClassVar[ComputeRoutesRequest.ExtraComputation]
        HTML_FORMATTED_NAVIGATION_INSTRUCTIONS: _ClassVar[ComputeRoutesRequest.ExtraComputation]
        FLYOVER_INFO_ON_POLYLINE: _ClassVar[ComputeRoutesRequest.ExtraComputation]
        NARROW_ROAD_INFO_ON_POLYLINE: _ClassVar[ComputeRoutesRequest.ExtraComputation]
    EXTRA_COMPUTATION_UNSPECIFIED: ComputeRoutesRequest.ExtraComputation
    TOLLS: ComputeRoutesRequest.ExtraComputation
    FUEL_CONSUMPTION: ComputeRoutesRequest.ExtraComputation
    TRAFFIC_ON_POLYLINE: ComputeRoutesRequest.ExtraComputation
    HTML_FORMATTED_NAVIGATION_INSTRUCTIONS: ComputeRoutesRequest.ExtraComputation
    FLYOVER_INFO_ON_POLYLINE: ComputeRoutesRequest.ExtraComputation
    NARROW_ROAD_INFO_ON_POLYLINE: ComputeRoutesRequest.ExtraComputation
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATES_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ALTERNATIVE_ROUTES_FIELD_NUMBER: _ClassVar[int]
    ROUTE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_WAYPOINT_ORDER_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_REFERENCE_ROUTES_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COMPUTATIONS_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_MODEL_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    origin: _waypoint_pb2.Waypoint
    destination: _waypoint_pb2.Waypoint
    intermediates: _containers.RepeatedCompositeFieldContainer[_waypoint_pb2.Waypoint]
    travel_mode: _route_travel_mode_pb2.RouteTravelMode
    routing_preference: _routing_preference_pb2.RoutingPreference
    polyline_quality: _polyline_pb2.PolylineQuality
    polyline_encoding: _polyline_pb2.PolylineEncoding
    departure_time: _timestamp_pb2.Timestamp
    arrival_time: _timestamp_pb2.Timestamp
    compute_alternative_routes: bool
    route_modifiers: _route_modifiers_pb2.RouteModifiers
    language_code: str
    region_code: str
    units: _units_pb2.Units
    optimize_waypoint_order: bool
    requested_reference_routes: _containers.RepeatedScalarFieldContainer[ComputeRoutesRequest.ReferenceRoute]
    extra_computations: _containers.RepeatedScalarFieldContainer[ComputeRoutesRequest.ExtraComputation]
    traffic_model: _traffic_model_pb2.TrafficModel
    transit_preferences: _transit_preferences_pb2.TransitPreferences
    def __init__(self, origin: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]] = ..., destination: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]] = ..., intermediates: _Optional[_Iterable[_Union[_waypoint_pb2.Waypoint, _Mapping]]] = ..., travel_mode: _Optional[_Union[_route_travel_mode_pb2.RouteTravelMode, str]] = ..., routing_preference: _Optional[_Union[_routing_preference_pb2.RoutingPreference, str]] = ..., polyline_quality: _Optional[_Union[_polyline_pb2.PolylineQuality, str]] = ..., polyline_encoding: _Optional[_Union[_polyline_pb2.PolylineEncoding, str]] = ..., departure_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., arrival_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., compute_alternative_routes: bool = ..., route_modifiers: _Optional[_Union[_route_modifiers_pb2.RouteModifiers, _Mapping]] = ..., language_code: _Optional[str] = ..., region_code: _Optional[str] = ..., units: _Optional[_Union[_units_pb2.Units, str]] = ..., optimize_waypoint_order: bool = ..., requested_reference_routes: _Optional[_Iterable[_Union[ComputeRoutesRequest.ReferenceRoute, str]]] = ..., extra_computations: _Optional[_Iterable[_Union[ComputeRoutesRequest.ExtraComputation, str]]] = ..., traffic_model: _Optional[_Union[_traffic_model_pb2.TrafficModel, str]] = ..., transit_preferences: _Optional[_Union[_transit_preferences_pb2.TransitPreferences, _Mapping]] = ...) -> None: ...

class ComputeRoutesResponse(_message.Message):
    __slots__ = ("routes", "fallback_info", "geocoding_results")
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_INFO_FIELD_NUMBER: _ClassVar[int]
    GEOCODING_RESULTS_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[_route_pb2.Route]
    fallback_info: _fallback_info_pb2.FallbackInfo
    geocoding_results: _geocoding_results_pb2.GeocodingResults
    def __init__(self, routes: _Optional[_Iterable[_Union[_route_pb2.Route, _Mapping]]] = ..., fallback_info: _Optional[_Union[_fallback_info_pb2.FallbackInfo, _Mapping]] = ..., geocoding_results: _Optional[_Union[_geocoding_results_pb2.GeocodingResults, _Mapping]] = ...) -> None: ...

class ComputeRouteMatrixRequest(_message.Message):
    __slots__ = ("origins", "destinations", "travel_mode", "routing_preference", "departure_time", "arrival_time", "language_code", "region_code", "units", "extra_computations", "traffic_model", "transit_preferences")
    class ExtraComputation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTRA_COMPUTATION_UNSPECIFIED: _ClassVar[ComputeRouteMatrixRequest.ExtraComputation]
        TOLLS: _ClassVar[ComputeRouteMatrixRequest.ExtraComputation]
    EXTRA_COMPUTATION_UNSPECIFIED: ComputeRouteMatrixRequest.ExtraComputation
    TOLLS: ComputeRouteMatrixRequest.ExtraComputation
    ORIGINS_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COMPUTATIONS_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_MODEL_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    origins: _containers.RepeatedCompositeFieldContainer[RouteMatrixOrigin]
    destinations: _containers.RepeatedCompositeFieldContainer[RouteMatrixDestination]
    travel_mode: _route_travel_mode_pb2.RouteTravelMode
    routing_preference: _routing_preference_pb2.RoutingPreference
    departure_time: _timestamp_pb2.Timestamp
    arrival_time: _timestamp_pb2.Timestamp
    language_code: str
    region_code: str
    units: _units_pb2.Units
    extra_computations: _containers.RepeatedScalarFieldContainer[ComputeRouteMatrixRequest.ExtraComputation]
    traffic_model: _traffic_model_pb2.TrafficModel
    transit_preferences: _transit_preferences_pb2.TransitPreferences
    def __init__(self, origins: _Optional[_Iterable[_Union[RouteMatrixOrigin, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[RouteMatrixDestination, _Mapping]]] = ..., travel_mode: _Optional[_Union[_route_travel_mode_pb2.RouteTravelMode, str]] = ..., routing_preference: _Optional[_Union[_routing_preference_pb2.RoutingPreference, str]] = ..., departure_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., arrival_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., language_code: _Optional[str] = ..., region_code: _Optional[str] = ..., units: _Optional[_Union[_units_pb2.Units, str]] = ..., extra_computations: _Optional[_Iterable[_Union[ComputeRouteMatrixRequest.ExtraComputation, str]]] = ..., traffic_model: _Optional[_Union[_traffic_model_pb2.TrafficModel, str]] = ..., transit_preferences: _Optional[_Union[_transit_preferences_pb2.TransitPreferences, _Mapping]] = ...) -> None: ...

class RouteMatrixOrigin(_message.Message):
    __slots__ = ("waypoint", "route_modifiers")
    WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    waypoint: _waypoint_pb2.Waypoint
    route_modifiers: _route_modifiers_pb2.RouteModifiers
    def __init__(self, waypoint: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]] = ..., route_modifiers: _Optional[_Union[_route_modifiers_pb2.RouteModifiers, _Mapping]] = ...) -> None: ...

class RouteMatrixDestination(_message.Message):
    __slots__ = ("waypoint",)
    WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    waypoint: _waypoint_pb2.Waypoint
    def __init__(self, waypoint: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]] = ...) -> None: ...

class RouteMatrixElement(_message.Message):
    __slots__ = ("origin_index", "destination_index", "status", "condition", "distance_meters", "duration", "static_duration", "travel_advisory", "fallback_info", "localized_values")
    class LocalizedValues(_message.Message):
        __slots__ = ("distance", "duration", "static_duration", "transit_fare")
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
        TRANSIT_FARE_FIELD_NUMBER: _ClassVar[int]
        distance: _localized_text_pb2.LocalizedText
        duration: _localized_text_pb2.LocalizedText
        static_duration: _localized_text_pb2.LocalizedText
        transit_fare: _localized_text_pb2.LocalizedText
        def __init__(self, distance: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., duration: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., static_duration: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., transit_fare: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ...) -> None: ...
    ORIGIN_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_ADVISORY_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_VALUES_FIELD_NUMBER: _ClassVar[int]
    origin_index: int
    destination_index: int
    status: _status_pb2.Status
    condition: RouteMatrixElementCondition
    distance_meters: int
    duration: _duration_pb2.Duration
    static_duration: _duration_pb2.Duration
    travel_advisory: _route_pb2.RouteTravelAdvisory
    fallback_info: _fallback_info_pb2.FallbackInfo
    localized_values: RouteMatrixElement.LocalizedValues
    def __init__(self, origin_index: _Optional[int] = ..., destination_index: _Optional[int] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., condition: _Optional[_Union[RouteMatrixElementCondition, str]] = ..., distance_meters: _Optional[int] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., travel_advisory: _Optional[_Union[_route_pb2.RouteTravelAdvisory, _Mapping]] = ..., fallback_info: _Optional[_Union[_fallback_info_pb2.FallbackInfo, _Mapping]] = ..., localized_values: _Optional[_Union[RouteMatrixElement.LocalizedValues, _Mapping]] = ...) -> None: ...
