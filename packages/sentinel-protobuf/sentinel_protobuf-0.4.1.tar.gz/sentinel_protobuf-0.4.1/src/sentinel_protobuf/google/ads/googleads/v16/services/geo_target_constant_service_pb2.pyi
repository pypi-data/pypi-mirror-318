from google.ads.googleads.v16.resources import geo_target_constant_pb2 as _geo_target_constant_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestGeoTargetConstantsRequest(_message.Message):
    __slots__ = ("locale", "country_code", "location_names", "geo_targets")
    class LocationNames(_message.Message):
        __slots__ = ("names",)
        NAMES_FIELD_NUMBER: _ClassVar[int]
        names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...
    class GeoTargets(_message.Message):
        __slots__ = ("geo_target_constants",)
        GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
        geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, geo_target_constants: _Optional[_Iterable[str]] = ...) -> None: ...
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMES_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGETS_FIELD_NUMBER: _ClassVar[int]
    locale: str
    country_code: str
    location_names: SuggestGeoTargetConstantsRequest.LocationNames
    geo_targets: SuggestGeoTargetConstantsRequest.GeoTargets
    def __init__(self, locale: _Optional[str] = ..., country_code: _Optional[str] = ..., location_names: _Optional[_Union[SuggestGeoTargetConstantsRequest.LocationNames, _Mapping]] = ..., geo_targets: _Optional[_Union[SuggestGeoTargetConstantsRequest.GeoTargets, _Mapping]] = ...) -> None: ...

class SuggestGeoTargetConstantsResponse(_message.Message):
    __slots__ = ("geo_target_constant_suggestions",)
    GEO_TARGET_CONSTANT_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    geo_target_constant_suggestions: _containers.RepeatedCompositeFieldContainer[GeoTargetConstantSuggestion]
    def __init__(self, geo_target_constant_suggestions: _Optional[_Iterable[_Union[GeoTargetConstantSuggestion, _Mapping]]] = ...) -> None: ...

class GeoTargetConstantSuggestion(_message.Message):
    __slots__ = ("locale", "reach", "search_term", "geo_target_constant", "geo_target_constant_parents")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    REACH_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CONSTANT_PARENTS_FIELD_NUMBER: _ClassVar[int]
    locale: str
    reach: int
    search_term: str
    geo_target_constant: _geo_target_constant_pb2.GeoTargetConstant
    geo_target_constant_parents: _containers.RepeatedCompositeFieldContainer[_geo_target_constant_pb2.GeoTargetConstant]
    def __init__(self, locale: _Optional[str] = ..., reach: _Optional[int] = ..., search_term: _Optional[str] = ..., geo_target_constant: _Optional[_Union[_geo_target_constant_pb2.GeoTargetConstant, _Mapping]] = ..., geo_target_constant_parents: _Optional[_Iterable[_Union[_geo_target_constant_pb2.GeoTargetConstant, _Mapping]]] = ...) -> None: ...
