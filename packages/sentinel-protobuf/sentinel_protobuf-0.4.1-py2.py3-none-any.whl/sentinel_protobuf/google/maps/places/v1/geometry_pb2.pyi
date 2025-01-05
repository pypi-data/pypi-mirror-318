from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Circle(_message.Message):
    __slots__ = ('center', 'radius')
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    center: _latlng_pb2.LatLng
    radius: float

    def __init__(self, center: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., radius: _Optional[float]=...) -> None:
        ...