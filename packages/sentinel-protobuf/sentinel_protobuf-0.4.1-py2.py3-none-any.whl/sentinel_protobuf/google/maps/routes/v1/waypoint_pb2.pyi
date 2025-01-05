from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Waypoint(_message.Message):
    __slots__ = ('location', 'place_id', 'via', 'vehicle_stopover', 'side_of_road')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIA_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_STOPOVER_FIELD_NUMBER: _ClassVar[int]
    SIDE_OF_ROAD_FIELD_NUMBER: _ClassVar[int]
    location: Location
    place_id: str
    via: bool
    vehicle_stopover: bool
    side_of_road: bool

    def __init__(self, location: _Optional[_Union[Location, _Mapping]]=..., place_id: _Optional[str]=..., via: bool=..., vehicle_stopover: bool=..., side_of_road: bool=...) -> None:
        ...

class Location(_message.Message):
    __slots__ = ('lat_lng', 'heading')
    LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    lat_lng: _latlng_pb2.LatLng
    heading: _wrappers_pb2.Int32Value

    def __init__(self, lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., heading: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=...) -> None:
        ...