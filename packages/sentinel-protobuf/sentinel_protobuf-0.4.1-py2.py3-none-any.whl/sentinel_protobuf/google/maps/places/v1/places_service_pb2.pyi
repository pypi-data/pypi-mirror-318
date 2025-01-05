from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.geo.type import viewport_pb2 as _viewport_pb2
from google.maps.places.v1 import contextual_content_pb2 as _contextual_content_pb2
from google.maps.places.v1 import ev_charging_pb2 as _ev_charging_pb2
from google.maps.places.v1 import geometry_pb2 as _geometry_pb2
from google.maps.places.v1 import place_pb2 as _place_pb2
from google.maps.places.v1 import polyline_pb2 as _polyline_pb2
from google.maps.places.v1 import route_modifiers_pb2 as _route_modifiers_pb2
from google.maps.places.v1 import routing_preference_pb2 as _routing_preference_pb2
from google.maps.places.v1 import routing_summary_pb2 as _routing_summary_pb2
from google.maps.places.v1 import travel_mode_pb2 as _travel_mode_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingParameters(_message.Message):
    __slots__ = ("origin", "travel_mode", "route_modifiers", "routing_preference")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    origin: _latlng_pb2.LatLng
    travel_mode: _travel_mode_pb2.TravelMode
    route_modifiers: _route_modifiers_pb2.RouteModifiers
    routing_preference: _routing_preference_pb2.RoutingPreference
    def __init__(self, origin: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., travel_mode: _Optional[_Union[_travel_mode_pb2.TravelMode, str]] = ..., route_modifiers: _Optional[_Union[_route_modifiers_pb2.RouteModifiers, _Mapping]] = ..., routing_preference: _Optional[_Union[_routing_preference_pb2.RoutingPreference, str]] = ...) -> None: ...

class SearchNearbyRequest(_message.Message):
    __slots__ = ("language_code", "region_code", "included_types", "excluded_types", "included_primary_types", "excluded_primary_types", "max_result_count", "location_restriction", "rank_preference", "routing_parameters")
    class RankPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RANK_PREFERENCE_UNSPECIFIED: _ClassVar[SearchNearbyRequest.RankPreference]
        DISTANCE: _ClassVar[SearchNearbyRequest.RankPreference]
        POPULARITY: _ClassVar[SearchNearbyRequest.RankPreference]
    RANK_PREFERENCE_UNSPECIFIED: SearchNearbyRequest.RankPreference
    DISTANCE: SearchNearbyRequest.RankPreference
    POPULARITY: SearchNearbyRequest.RankPreference
    class LocationRestriction(_message.Message):
        __slots__ = ("circle",)
        CIRCLE_FIELD_NUMBER: _ClassVar[int]
        circle: _geometry_pb2.Circle
        def __init__(self, circle: _Optional[_Union[_geometry_pb2.Circle, _Mapping]] = ...) -> None: ...
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_TYPES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_TYPES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_PRIMARY_TYPES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PRIMARY_TYPES_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    RANK_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    region_code: str
    included_types: _containers.RepeatedScalarFieldContainer[str]
    excluded_types: _containers.RepeatedScalarFieldContainer[str]
    included_primary_types: _containers.RepeatedScalarFieldContainer[str]
    excluded_primary_types: _containers.RepeatedScalarFieldContainer[str]
    max_result_count: int
    location_restriction: SearchNearbyRequest.LocationRestriction
    rank_preference: SearchNearbyRequest.RankPreference
    routing_parameters: RoutingParameters
    def __init__(self, language_code: _Optional[str] = ..., region_code: _Optional[str] = ..., included_types: _Optional[_Iterable[str]] = ..., excluded_types: _Optional[_Iterable[str]] = ..., included_primary_types: _Optional[_Iterable[str]] = ..., excluded_primary_types: _Optional[_Iterable[str]] = ..., max_result_count: _Optional[int] = ..., location_restriction: _Optional[_Union[SearchNearbyRequest.LocationRestriction, _Mapping]] = ..., rank_preference: _Optional[_Union[SearchNearbyRequest.RankPreference, str]] = ..., routing_parameters: _Optional[_Union[RoutingParameters, _Mapping]] = ...) -> None: ...

class SearchNearbyResponse(_message.Message):
    __slots__ = ("places", "routing_summaries")
    PLACES_FIELD_NUMBER: _ClassVar[int]
    ROUTING_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    places: _containers.RepeatedCompositeFieldContainer[_place_pb2.Place]
    routing_summaries: _containers.RepeatedCompositeFieldContainer[_routing_summary_pb2.RoutingSummary]
    def __init__(self, places: _Optional[_Iterable[_Union[_place_pb2.Place, _Mapping]]] = ..., routing_summaries: _Optional[_Iterable[_Union[_routing_summary_pb2.RoutingSummary, _Mapping]]] = ...) -> None: ...

class SearchTextRequest(_message.Message):
    __slots__ = ("text_query", "language_code", "region_code", "rank_preference", "included_type", "open_now", "min_rating", "max_result_count", "price_levels", "strict_type_filtering", "location_bias", "location_restriction", "ev_options", "routing_parameters", "search_along_route_parameters", "include_pure_service_area_businesses")
    class RankPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RANK_PREFERENCE_UNSPECIFIED: _ClassVar[SearchTextRequest.RankPreference]
        DISTANCE: _ClassVar[SearchTextRequest.RankPreference]
        RELEVANCE: _ClassVar[SearchTextRequest.RankPreference]
    RANK_PREFERENCE_UNSPECIFIED: SearchTextRequest.RankPreference
    DISTANCE: SearchTextRequest.RankPreference
    RELEVANCE: SearchTextRequest.RankPreference
    class LocationBias(_message.Message):
        __slots__ = ("rectangle", "circle")
        RECTANGLE_FIELD_NUMBER: _ClassVar[int]
        CIRCLE_FIELD_NUMBER: _ClassVar[int]
        rectangle: _viewport_pb2.Viewport
        circle: _geometry_pb2.Circle
        def __init__(self, rectangle: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]] = ..., circle: _Optional[_Union[_geometry_pb2.Circle, _Mapping]] = ...) -> None: ...
    class LocationRestriction(_message.Message):
        __slots__ = ("rectangle",)
        RECTANGLE_FIELD_NUMBER: _ClassVar[int]
        rectangle: _viewport_pb2.Viewport
        def __init__(self, rectangle: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]] = ...) -> None: ...
    class EVOptions(_message.Message):
        __slots__ = ("minimum_charging_rate_kw", "connector_types")
        MINIMUM_CHARGING_RATE_KW_FIELD_NUMBER: _ClassVar[int]
        CONNECTOR_TYPES_FIELD_NUMBER: _ClassVar[int]
        minimum_charging_rate_kw: float
        connector_types: _containers.RepeatedScalarFieldContainer[_ev_charging_pb2.EVConnectorType]
        def __init__(self, minimum_charging_rate_kw: _Optional[float] = ..., connector_types: _Optional[_Iterable[_Union[_ev_charging_pb2.EVConnectorType, str]]] = ...) -> None: ...
    class SearchAlongRouteParameters(_message.Message):
        __slots__ = ("polyline",)
        POLYLINE_FIELD_NUMBER: _ClassVar[int]
        polyline: _polyline_pb2.Polyline
        def __init__(self, polyline: _Optional[_Union[_polyline_pb2.Polyline, _Mapping]] = ...) -> None: ...
    TEXT_QUERY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    RANK_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPEN_NOW_FIELD_NUMBER: _ClassVar[int]
    MIN_RATING_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_LEVELS_FIELD_NUMBER: _ClassVar[int]
    STRICT_TYPE_FILTERING_FIELD_NUMBER: _ClassVar[int]
    LOCATION_BIAS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    EV_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ALONG_ROUTE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PURE_SERVICE_AREA_BUSINESSES_FIELD_NUMBER: _ClassVar[int]
    text_query: str
    language_code: str
    region_code: str
    rank_preference: SearchTextRequest.RankPreference
    included_type: str
    open_now: bool
    min_rating: float
    max_result_count: int
    price_levels: _containers.RepeatedScalarFieldContainer[_place_pb2.PriceLevel]
    strict_type_filtering: bool
    location_bias: SearchTextRequest.LocationBias
    location_restriction: SearchTextRequest.LocationRestriction
    ev_options: SearchTextRequest.EVOptions
    routing_parameters: RoutingParameters
    search_along_route_parameters: SearchTextRequest.SearchAlongRouteParameters
    include_pure_service_area_businesses: bool
    def __init__(self, text_query: _Optional[str] = ..., language_code: _Optional[str] = ..., region_code: _Optional[str] = ..., rank_preference: _Optional[_Union[SearchTextRequest.RankPreference, str]] = ..., included_type: _Optional[str] = ..., open_now: bool = ..., min_rating: _Optional[float] = ..., max_result_count: _Optional[int] = ..., price_levels: _Optional[_Iterable[_Union[_place_pb2.PriceLevel, str]]] = ..., strict_type_filtering: bool = ..., location_bias: _Optional[_Union[SearchTextRequest.LocationBias, _Mapping]] = ..., location_restriction: _Optional[_Union[SearchTextRequest.LocationRestriction, _Mapping]] = ..., ev_options: _Optional[_Union[SearchTextRequest.EVOptions, _Mapping]] = ..., routing_parameters: _Optional[_Union[RoutingParameters, _Mapping]] = ..., search_along_route_parameters: _Optional[_Union[SearchTextRequest.SearchAlongRouteParameters, _Mapping]] = ..., include_pure_service_area_businesses: bool = ...) -> None: ...

class SearchTextResponse(_message.Message):
    __slots__ = ("places", "routing_summaries", "contextual_contents")
    PLACES_FIELD_NUMBER: _ClassVar[int]
    ROUTING_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    places: _containers.RepeatedCompositeFieldContainer[_place_pb2.Place]
    routing_summaries: _containers.RepeatedCompositeFieldContainer[_routing_summary_pb2.RoutingSummary]
    contextual_contents: _containers.RepeatedCompositeFieldContainer[_contextual_content_pb2.ContextualContent]
    def __init__(self, places: _Optional[_Iterable[_Union[_place_pb2.Place, _Mapping]]] = ..., routing_summaries: _Optional[_Iterable[_Union[_routing_summary_pb2.RoutingSummary, _Mapping]]] = ..., contextual_contents: _Optional[_Iterable[_Union[_contextual_content_pb2.ContextualContent, _Mapping]]] = ...) -> None: ...

class GetPhotoMediaRequest(_message.Message):
    __slots__ = ("name", "max_width_px", "max_height_px", "skip_http_redirect")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    MAX_HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    SKIP_HTTP_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    max_width_px: int
    max_height_px: int
    skip_http_redirect: bool
    def __init__(self, name: _Optional[str] = ..., max_width_px: _Optional[int] = ..., max_height_px: _Optional[int] = ..., skip_http_redirect: bool = ...) -> None: ...

class PhotoMedia(_message.Message):
    __slots__ = ("name", "photo_uri")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    photo_uri: str
    def __init__(self, name: _Optional[str] = ..., photo_uri: _Optional[str] = ...) -> None: ...

class GetPlaceRequest(_message.Message):
    __slots__ = ("name", "language_code", "region_code", "session_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    region_code: str
    session_token: str
    def __init__(self, name: _Optional[str] = ..., language_code: _Optional[str] = ..., region_code: _Optional[str] = ..., session_token: _Optional[str] = ...) -> None: ...

class AutocompletePlacesRequest(_message.Message):
    __slots__ = ("input", "location_bias", "location_restriction", "included_primary_types", "included_region_codes", "language_code", "region_code", "origin", "input_offset", "include_query_predictions", "session_token", "include_pure_service_area_businesses")
    class LocationBias(_message.Message):
        __slots__ = ("rectangle", "circle")
        RECTANGLE_FIELD_NUMBER: _ClassVar[int]
        CIRCLE_FIELD_NUMBER: _ClassVar[int]
        rectangle: _viewport_pb2.Viewport
        circle: _geometry_pb2.Circle
        def __init__(self, rectangle: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]] = ..., circle: _Optional[_Union[_geometry_pb2.Circle, _Mapping]] = ...) -> None: ...
    class LocationRestriction(_message.Message):
        __slots__ = ("rectangle", "circle")
        RECTANGLE_FIELD_NUMBER: _ClassVar[int]
        CIRCLE_FIELD_NUMBER: _ClassVar[int]
        rectangle: _viewport_pb2.Viewport
        circle: _geometry_pb2.Circle
        def __init__(self, rectangle: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]] = ..., circle: _Optional[_Union[_geometry_pb2.Circle, _Mapping]] = ...) -> None: ...
    INPUT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_BIAS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_PRIMARY_TYPES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_REGION_CODES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    INPUT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_QUERY_PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PURE_SERVICE_AREA_BUSINESSES_FIELD_NUMBER: _ClassVar[int]
    input: str
    location_bias: AutocompletePlacesRequest.LocationBias
    location_restriction: AutocompletePlacesRequest.LocationRestriction
    included_primary_types: _containers.RepeatedScalarFieldContainer[str]
    included_region_codes: _containers.RepeatedScalarFieldContainer[str]
    language_code: str
    region_code: str
    origin: _latlng_pb2.LatLng
    input_offset: int
    include_query_predictions: bool
    session_token: str
    include_pure_service_area_businesses: bool
    def __init__(self, input: _Optional[str] = ..., location_bias: _Optional[_Union[AutocompletePlacesRequest.LocationBias, _Mapping]] = ..., location_restriction: _Optional[_Union[AutocompletePlacesRequest.LocationRestriction, _Mapping]] = ..., included_primary_types: _Optional[_Iterable[str]] = ..., included_region_codes: _Optional[_Iterable[str]] = ..., language_code: _Optional[str] = ..., region_code: _Optional[str] = ..., origin: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., input_offset: _Optional[int] = ..., include_query_predictions: bool = ..., session_token: _Optional[str] = ..., include_pure_service_area_businesses: bool = ...) -> None: ...

class AutocompletePlacesResponse(_message.Message):
    __slots__ = ("suggestions",)
    class Suggestion(_message.Message):
        __slots__ = ("place_prediction", "query_prediction")
        class StringRange(_message.Message):
            __slots__ = ("start_offset", "end_offset")
            START_OFFSET_FIELD_NUMBER: _ClassVar[int]
            END_OFFSET_FIELD_NUMBER: _ClassVar[int]
            start_offset: int
            end_offset: int
            def __init__(self, start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ...) -> None: ...
        class FormattableText(_message.Message):
            __slots__ = ("text", "matches")
            TEXT_FIELD_NUMBER: _ClassVar[int]
            MATCHES_FIELD_NUMBER: _ClassVar[int]
            text: str
            matches: _containers.RepeatedCompositeFieldContainer[AutocompletePlacesResponse.Suggestion.StringRange]
            def __init__(self, text: _Optional[str] = ..., matches: _Optional[_Iterable[_Union[AutocompletePlacesResponse.Suggestion.StringRange, _Mapping]]] = ...) -> None: ...
        class StructuredFormat(_message.Message):
            __slots__ = ("main_text", "secondary_text")
            MAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
            SECONDARY_TEXT_FIELD_NUMBER: _ClassVar[int]
            main_text: AutocompletePlacesResponse.Suggestion.FormattableText
            secondary_text: AutocompletePlacesResponse.Suggestion.FormattableText
            def __init__(self, main_text: _Optional[_Union[AutocompletePlacesResponse.Suggestion.FormattableText, _Mapping]] = ..., secondary_text: _Optional[_Union[AutocompletePlacesResponse.Suggestion.FormattableText, _Mapping]] = ...) -> None: ...
        class PlacePrediction(_message.Message):
            __slots__ = ("place", "place_id", "text", "structured_format", "types", "distance_meters")
            PLACE_FIELD_NUMBER: _ClassVar[int]
            PLACE_ID_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            STRUCTURED_FORMAT_FIELD_NUMBER: _ClassVar[int]
            TYPES_FIELD_NUMBER: _ClassVar[int]
            DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
            place: str
            place_id: str
            text: AutocompletePlacesResponse.Suggestion.FormattableText
            structured_format: AutocompletePlacesResponse.Suggestion.StructuredFormat
            types: _containers.RepeatedScalarFieldContainer[str]
            distance_meters: int
            def __init__(self, place: _Optional[str] = ..., place_id: _Optional[str] = ..., text: _Optional[_Union[AutocompletePlacesResponse.Suggestion.FormattableText, _Mapping]] = ..., structured_format: _Optional[_Union[AutocompletePlacesResponse.Suggestion.StructuredFormat, _Mapping]] = ..., types: _Optional[_Iterable[str]] = ..., distance_meters: _Optional[int] = ...) -> None: ...
        class QueryPrediction(_message.Message):
            __slots__ = ("text", "structured_format")
            TEXT_FIELD_NUMBER: _ClassVar[int]
            STRUCTURED_FORMAT_FIELD_NUMBER: _ClassVar[int]
            text: AutocompletePlacesResponse.Suggestion.FormattableText
            structured_format: AutocompletePlacesResponse.Suggestion.StructuredFormat
            def __init__(self, text: _Optional[_Union[AutocompletePlacesResponse.Suggestion.FormattableText, _Mapping]] = ..., structured_format: _Optional[_Union[AutocompletePlacesResponse.Suggestion.StructuredFormat, _Mapping]] = ...) -> None: ...
        PLACE_PREDICTION_FIELD_NUMBER: _ClassVar[int]
        QUERY_PREDICTION_FIELD_NUMBER: _ClassVar[int]
        place_prediction: AutocompletePlacesResponse.Suggestion.PlacePrediction
        query_prediction: AutocompletePlacesResponse.Suggestion.QueryPrediction
        def __init__(self, place_prediction: _Optional[_Union[AutocompletePlacesResponse.Suggestion.PlacePrediction, _Mapping]] = ..., query_prediction: _Optional[_Union[AutocompletePlacesResponse.Suggestion.QueryPrediction, _Mapping]] = ...) -> None: ...
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    suggestions: _containers.RepeatedCompositeFieldContainer[AutocompletePlacesResponse.Suggestion]
    def __init__(self, suggestions: _Optional[_Iterable[_Union[AutocompletePlacesResponse.Suggestion, _Mapping]]] = ...) -> None: ...
