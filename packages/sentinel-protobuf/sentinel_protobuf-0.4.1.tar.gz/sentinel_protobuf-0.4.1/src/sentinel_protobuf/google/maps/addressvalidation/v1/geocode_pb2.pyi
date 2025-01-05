from google.geo.type import viewport_pb2 as _viewport_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Geocode(_message.Message):
    __slots__ = ('location', 'plus_code', 'bounds', 'feature_size_meters', 'place_id', 'place_types')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLUS_CODE_FIELD_NUMBER: _ClassVar[int]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SIZE_METERS_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLACE_TYPES_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    plus_code: PlusCode
    bounds: _viewport_pb2.Viewport
    feature_size_meters: float
    place_id: str
    place_types: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., plus_code: _Optional[_Union[PlusCode, _Mapping]]=..., bounds: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]]=..., feature_size_meters: _Optional[float]=..., place_id: _Optional[str]=..., place_types: _Optional[_Iterable[str]]=...) -> None:
        ...

class PlusCode(_message.Message):
    __slots__ = ('global_code', 'compound_code')
    GLOBAL_CODE_FIELD_NUMBER: _ClassVar[int]
    COMPOUND_CODE_FIELD_NUMBER: _ClassVar[int]
    global_code: str
    compound_code: str

    def __init__(self, global_code: _Optional[str]=..., compound_code: _Optional[str]=...) -> None:
        ...