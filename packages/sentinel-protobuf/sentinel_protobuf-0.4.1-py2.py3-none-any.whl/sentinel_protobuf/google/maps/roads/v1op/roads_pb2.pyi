from google.api import client_pb2 as _client_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TravelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAVEL_MODE_UNSPECIFIED: _ClassVar[TravelMode]
    DRIVING: _ClassVar[TravelMode]
    CYCLING: _ClassVar[TravelMode]
    WALKING: _ClassVar[TravelMode]
TRAVEL_MODE_UNSPECIFIED: TravelMode
DRIVING: TravelMode
CYCLING: TravelMode
WALKING: TravelMode

class SnapToRoadsRequest(_message.Message):
    __slots__ = ('path', 'interpolate', 'asset_id', 'travel_mode')
    PATH_FIELD_NUMBER: _ClassVar[int]
    INTERPOLATE_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    path: str
    interpolate: bool
    asset_id: str
    travel_mode: TravelMode

    def __init__(self, path: _Optional[str]=..., interpolate: bool=..., asset_id: _Optional[str]=..., travel_mode: _Optional[_Union[TravelMode, str]]=...) -> None:
        ...

class SnappedPoint(_message.Message):
    __slots__ = ('location', 'original_index', 'place_id')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_INDEX_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    original_index: _wrappers_pb2.UInt32Value
    place_id: str

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., original_index: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]]=..., place_id: _Optional[str]=...) -> None:
        ...

class SnapToRoadsResponse(_message.Message):
    __slots__ = ('snapped_points', 'warning_message')
    SNAPPED_POINTS_FIELD_NUMBER: _ClassVar[int]
    WARNING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    snapped_points: _containers.RepeatedCompositeFieldContainer[SnappedPoint]
    warning_message: str

    def __init__(self, snapped_points: _Optional[_Iterable[_Union[SnappedPoint, _Mapping]]]=..., warning_message: _Optional[str]=...) -> None:
        ...

class ListNearestRoadsRequest(_message.Message):
    __slots__ = ('points', 'travel_mode')
    POINTS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    points: str
    travel_mode: TravelMode

    def __init__(self, points: _Optional[str]=..., travel_mode: _Optional[_Union[TravelMode, str]]=...) -> None:
        ...

class ListNearestRoadsResponse(_message.Message):
    __slots__ = ('snapped_points',)
    SNAPPED_POINTS_FIELD_NUMBER: _ClassVar[int]
    snapped_points: _containers.RepeatedCompositeFieldContainer[SnappedPoint]

    def __init__(self, snapped_points: _Optional[_Iterable[_Union[SnappedPoint, _Mapping]]]=...) -> None:
        ...