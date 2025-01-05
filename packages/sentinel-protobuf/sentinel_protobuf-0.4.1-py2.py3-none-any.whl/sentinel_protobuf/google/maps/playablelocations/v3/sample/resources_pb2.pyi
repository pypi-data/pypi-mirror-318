from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PlayableLocation(_message.Message):
    __slots__ = ('name', 'place_id', 'plus_code', 'types', 'center_point', 'snapped_point')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLUS_CODE_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    CENTER_POINT_FIELD_NUMBER: _ClassVar[int]
    SNAPPED_POINT_FIELD_NUMBER: _ClassVar[int]
    name: str
    place_id: str
    plus_code: str
    types: _containers.RepeatedScalarFieldContainer[str]
    center_point: _latlng_pb2.LatLng
    snapped_point: _latlng_pb2.LatLng

    def __init__(self, name: _Optional[str]=..., place_id: _Optional[str]=..., plus_code: _Optional[str]=..., types: _Optional[_Iterable[str]]=..., center_point: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., snapped_point: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=...) -> None:
        ...

class SpacingOptions(_message.Message):
    __slots__ = ('min_spacing_meters', 'point_type')

    class PointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POINT_TYPE_UNSPECIFIED: _ClassVar[SpacingOptions.PointType]
        CENTER_POINT: _ClassVar[SpacingOptions.PointType]
        SNAPPED_POINT: _ClassVar[SpacingOptions.PointType]
    POINT_TYPE_UNSPECIFIED: SpacingOptions.PointType
    CENTER_POINT: SpacingOptions.PointType
    SNAPPED_POINT: SpacingOptions.PointType
    MIN_SPACING_METERS_FIELD_NUMBER: _ClassVar[int]
    POINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    min_spacing_meters: float
    point_type: SpacingOptions.PointType

    def __init__(self, min_spacing_meters: _Optional[float]=..., point_type: _Optional[_Union[SpacingOptions.PointType, str]]=...) -> None:
        ...

class Filter(_message.Message):
    __slots__ = ('max_location_count', 'spacing', 'included_types')
    MAX_LOCATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_TYPES_FIELD_NUMBER: _ClassVar[int]
    max_location_count: int
    spacing: SpacingOptions
    included_types: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, max_location_count: _Optional[int]=..., spacing: _Optional[_Union[SpacingOptions, _Mapping]]=..., included_types: _Optional[_Iterable[str]]=...) -> None:
        ...

class Criterion(_message.Message):
    __slots__ = ('game_object_type', 'filter', 'fields_to_return')
    GAME_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_TO_RETURN_FIELD_NUMBER: _ClassVar[int]
    game_object_type: int
    filter: Filter
    fields_to_return: _field_mask_pb2.FieldMask

    def __init__(self, game_object_type: _Optional[int]=..., filter: _Optional[_Union[Filter, _Mapping]]=..., fields_to_return: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class AreaFilter(_message.Message):
    __slots__ = ('s2_cell_id',)
    S2_CELL_ID_FIELD_NUMBER: _ClassVar[int]
    s2_cell_id: int

    def __init__(self, s2_cell_id: _Optional[int]=...) -> None:
        ...

class PlayableLocationList(_message.Message):
    __slots__ = ('locations',)
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.RepeatedCompositeFieldContainer[PlayableLocation]

    def __init__(self, locations: _Optional[_Iterable[_Union[PlayableLocation, _Mapping]]]=...) -> None:
        ...