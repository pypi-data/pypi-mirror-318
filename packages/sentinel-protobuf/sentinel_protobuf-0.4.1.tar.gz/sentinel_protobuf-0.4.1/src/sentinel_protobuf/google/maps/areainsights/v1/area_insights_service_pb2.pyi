from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Insight(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSIGHT_UNSPECIFIED: _ClassVar[Insight]
    INSIGHT_COUNT: _ClassVar[Insight]
    INSIGHT_PLACES: _ClassVar[Insight]

class OperatingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATING_STATUS_UNSPECIFIED: _ClassVar[OperatingStatus]
    OPERATING_STATUS_OPERATIONAL: _ClassVar[OperatingStatus]
    OPERATING_STATUS_PERMANENTLY_CLOSED: _ClassVar[OperatingStatus]
    OPERATING_STATUS_TEMPORARILY_CLOSED: _ClassVar[OperatingStatus]

class PriceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRICE_LEVEL_UNSPECIFIED: _ClassVar[PriceLevel]
    PRICE_LEVEL_FREE: _ClassVar[PriceLevel]
    PRICE_LEVEL_INEXPENSIVE: _ClassVar[PriceLevel]
    PRICE_LEVEL_MODERATE: _ClassVar[PriceLevel]
    PRICE_LEVEL_EXPENSIVE: _ClassVar[PriceLevel]
    PRICE_LEVEL_VERY_EXPENSIVE: _ClassVar[PriceLevel]
INSIGHT_UNSPECIFIED: Insight
INSIGHT_COUNT: Insight
INSIGHT_PLACES: Insight
OPERATING_STATUS_UNSPECIFIED: OperatingStatus
OPERATING_STATUS_OPERATIONAL: OperatingStatus
OPERATING_STATUS_PERMANENTLY_CLOSED: OperatingStatus
OPERATING_STATUS_TEMPORARILY_CLOSED: OperatingStatus
PRICE_LEVEL_UNSPECIFIED: PriceLevel
PRICE_LEVEL_FREE: PriceLevel
PRICE_LEVEL_INEXPENSIVE: PriceLevel
PRICE_LEVEL_MODERATE: PriceLevel
PRICE_LEVEL_EXPENSIVE: PriceLevel
PRICE_LEVEL_VERY_EXPENSIVE: PriceLevel

class ComputeInsightsRequest(_message.Message):
    __slots__ = ("insights", "filter")
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedScalarFieldContainer[Insight]
    filter: Filter
    def __init__(self, insights: _Optional[_Iterable[_Union[Insight, str]]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ...) -> None: ...

class ComputeInsightsResponse(_message.Message):
    __slots__ = ("count", "place_insights")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PLACE_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    count: int
    place_insights: _containers.RepeatedCompositeFieldContainer[PlaceInsight]
    def __init__(self, count: _Optional[int] = ..., place_insights: _Optional[_Iterable[_Union[PlaceInsight, _Mapping]]] = ...) -> None: ...

class PlaceInsight(_message.Message):
    __slots__ = ("place",)
    PLACE_FIELD_NUMBER: _ClassVar[int]
    place: str
    def __init__(self, place: _Optional[str] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("location_filter", "type_filter", "operating_status", "price_levels", "rating_filter")
    LOCATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    OPERATING_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRICE_LEVELS_FIELD_NUMBER: _ClassVar[int]
    RATING_FILTER_FIELD_NUMBER: _ClassVar[int]
    location_filter: LocationFilter
    type_filter: TypeFilter
    operating_status: _containers.RepeatedScalarFieldContainer[OperatingStatus]
    price_levels: _containers.RepeatedScalarFieldContainer[PriceLevel]
    rating_filter: RatingFilter
    def __init__(self, location_filter: _Optional[_Union[LocationFilter, _Mapping]] = ..., type_filter: _Optional[_Union[TypeFilter, _Mapping]] = ..., operating_status: _Optional[_Iterable[_Union[OperatingStatus, str]]] = ..., price_levels: _Optional[_Iterable[_Union[PriceLevel, str]]] = ..., rating_filter: _Optional[_Union[RatingFilter, _Mapping]] = ...) -> None: ...

class LocationFilter(_message.Message):
    __slots__ = ("circle", "region", "custom_area")
    class Circle(_message.Message):
        __slots__ = ("lat_lng", "place", "radius")
        LAT_LNG_FIELD_NUMBER: _ClassVar[int]
        PLACE_FIELD_NUMBER: _ClassVar[int]
        RADIUS_FIELD_NUMBER: _ClassVar[int]
        lat_lng: _latlng_pb2.LatLng
        place: str
        radius: int
        def __init__(self, lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., place: _Optional[str] = ..., radius: _Optional[int] = ...) -> None: ...
    class Region(_message.Message):
        __slots__ = ("place",)
        PLACE_FIELD_NUMBER: _ClassVar[int]
        place: str
        def __init__(self, place: _Optional[str] = ...) -> None: ...
    class CustomArea(_message.Message):
        __slots__ = ("polygon",)
        class Polygon(_message.Message):
            __slots__ = ("coordinates",)
            COORDINATES_FIELD_NUMBER: _ClassVar[int]
            coordinates: _containers.RepeatedCompositeFieldContainer[_latlng_pb2.LatLng]
            def __init__(self, coordinates: _Optional[_Iterable[_Union[_latlng_pb2.LatLng, _Mapping]]] = ...) -> None: ...
        POLYGON_FIELD_NUMBER: _ClassVar[int]
        polygon: LocationFilter.CustomArea.Polygon
        def __init__(self, polygon: _Optional[_Union[LocationFilter.CustomArea.Polygon, _Mapping]] = ...) -> None: ...
    CIRCLE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AREA_FIELD_NUMBER: _ClassVar[int]
    circle: LocationFilter.Circle
    region: LocationFilter.Region
    custom_area: LocationFilter.CustomArea
    def __init__(self, circle: _Optional[_Union[LocationFilter.Circle, _Mapping]] = ..., region: _Optional[_Union[LocationFilter.Region, _Mapping]] = ..., custom_area: _Optional[_Union[LocationFilter.CustomArea, _Mapping]] = ...) -> None: ...

class TypeFilter(_message.Message):
    __slots__ = ("included_types", "excluded_types", "included_primary_types", "excluded_primary_types")
    INCLUDED_TYPES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_TYPES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_PRIMARY_TYPES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PRIMARY_TYPES_FIELD_NUMBER: _ClassVar[int]
    included_types: _containers.RepeatedScalarFieldContainer[str]
    excluded_types: _containers.RepeatedScalarFieldContainer[str]
    included_primary_types: _containers.RepeatedScalarFieldContainer[str]
    excluded_primary_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, included_types: _Optional[_Iterable[str]] = ..., excluded_types: _Optional[_Iterable[str]] = ..., included_primary_types: _Optional[_Iterable[str]] = ..., excluded_primary_types: _Optional[_Iterable[str]] = ...) -> None: ...

class RatingFilter(_message.Message):
    __slots__ = ("min_rating", "max_rating")
    MIN_RATING_FIELD_NUMBER: _ClassVar[int]
    MAX_RATING_FIELD_NUMBER: _ClassVar[int]
    min_rating: float
    max_rating: float
    def __init__(self, min_rating: _Optional[float] = ..., max_rating: _Optional[float] = ...) -> None: ...
