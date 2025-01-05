from google.maps.routing.v2 import location_pb2 as _location_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Waypoint(_message.Message):
    __slots__ = ('location', 'place_id', 'address', 'via', 'vehicle_stopover', 'side_of_road')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VIA_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_STOPOVER_FIELD_NUMBER: _ClassVar[int]
    SIDE_OF_ROAD_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    place_id: str
    address: str
    via: bool
    vehicle_stopover: bool
    side_of_road: bool

    def __init__(self, location: _Optional[_Union[_location_pb2.Location, _Mapping]]=..., place_id: _Optional[str]=..., address: _Optional[str]=..., via: bool=..., vehicle_stopover: bool=..., side_of_road: bool=...) -> None:
        ...