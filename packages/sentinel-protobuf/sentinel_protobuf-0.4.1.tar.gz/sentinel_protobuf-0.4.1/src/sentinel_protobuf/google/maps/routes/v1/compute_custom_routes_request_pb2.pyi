from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.routes.v1 import compute_routes_request_pb2 as _compute_routes_request_pb2
from google.maps.routes.v1 import polyline_pb2 as _polyline_pb2
from google.maps.routes.v1 import waypoint_pb2 as _waypoint_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeCustomRoutesRequest(_message.Message):
    __slots__ = ('origin', 'destination', 'intermediates', 'travel_mode', 'routing_preference', 'polyline_quality', 'polyline_encoding', 'departure_time', 'route_modifiers', 'route_objective', 'language_code', 'units')
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATES_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    ROUTE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    origin: _waypoint_pb2.Waypoint
    destination: _waypoint_pb2.Waypoint
    intermediates: _containers.RepeatedCompositeFieldContainer[_waypoint_pb2.Waypoint]
    travel_mode: _compute_routes_request_pb2.RouteTravelMode
    routing_preference: _compute_routes_request_pb2.RoutingPreference
    polyline_quality: _polyline_pb2.PolylineQuality
    polyline_encoding: _polyline_pb2.PolylineEncoding
    departure_time: _timestamp_pb2.Timestamp
    route_modifiers: _compute_routes_request_pb2.RouteModifiers
    route_objective: RouteObjective
    language_code: str
    units: _compute_routes_request_pb2.Units

    def __init__(self, origin: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]]=..., destination: _Optional[_Union[_waypoint_pb2.Waypoint, _Mapping]]=..., intermediates: _Optional[_Iterable[_Union[_waypoint_pb2.Waypoint, _Mapping]]]=..., travel_mode: _Optional[_Union[_compute_routes_request_pb2.RouteTravelMode, str]]=..., routing_preference: _Optional[_Union[_compute_routes_request_pb2.RoutingPreference, str]]=..., polyline_quality: _Optional[_Union[_polyline_pb2.PolylineQuality, str]]=..., polyline_encoding: _Optional[_Union[_polyline_pb2.PolylineEncoding, str]]=..., departure_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., route_modifiers: _Optional[_Union[_compute_routes_request_pb2.RouteModifiers, _Mapping]]=..., route_objective: _Optional[_Union[RouteObjective, _Mapping]]=..., language_code: _Optional[str]=..., units: _Optional[_Union[_compute_routes_request_pb2.Units, str]]=...) -> None:
        ...

class RouteObjective(_message.Message):
    __slots__ = ('rate_card', 'custom_layer')

    class RateCard(_message.Message):
        __slots__ = ('cost_per_minute', 'cost_per_km', 'include_tolls')

        class MonetaryCost(_message.Message):
            __slots__ = ('value',)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: float

            def __init__(self, value: _Optional[float]=...) -> None:
                ...
        COST_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
        COST_PER_KM_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_TOLLS_FIELD_NUMBER: _ClassVar[int]
        cost_per_minute: RouteObjective.RateCard.MonetaryCost
        cost_per_km: RouteObjective.RateCard.MonetaryCost
        include_tolls: bool

        def __init__(self, cost_per_minute: _Optional[_Union[RouteObjective.RateCard.MonetaryCost, _Mapping]]=..., cost_per_km: _Optional[_Union[RouteObjective.RateCard.MonetaryCost, _Mapping]]=..., include_tolls: bool=...) -> None:
            ...

    class CustomLayer(_message.Message):
        __slots__ = ('dataset_info',)

        class DatasetInfo(_message.Message):
            __slots__ = ('dataset_id', 'display_name')
            DATASET_ID_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            dataset_id: str
            display_name: str

            def __init__(self, dataset_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
                ...
        DATASET_INFO_FIELD_NUMBER: _ClassVar[int]
        dataset_info: RouteObjective.CustomLayer.DatasetInfo

        def __init__(self, dataset_info: _Optional[_Union[RouteObjective.CustomLayer.DatasetInfo, _Mapping]]=...) -> None:
            ...
    RATE_CARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LAYER_FIELD_NUMBER: _ClassVar[int]
    rate_card: RouteObjective.RateCard
    custom_layer: RouteObjective.CustomLayer

    def __init__(self, rate_card: _Optional[_Union[RouteObjective.RateCard, _Mapping]]=..., custom_layer: _Optional[_Union[RouteObjective.CustomLayer, _Mapping]]=...) -> None:
        ...