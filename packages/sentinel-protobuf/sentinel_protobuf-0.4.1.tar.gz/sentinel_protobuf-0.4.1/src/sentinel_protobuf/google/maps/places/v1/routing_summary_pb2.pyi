from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RoutingSummary(_message.Message):
    __slots__ = ('legs', 'directions_uri')

    class Leg(_message.Message):
        __slots__ = ('duration', 'distance_meters')
        DURATION_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        distance_meters: int

        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., distance_meters: _Optional[int]=...) -> None:
            ...
    LEGS_FIELD_NUMBER: _ClassVar[int]
    DIRECTIONS_URI_FIELD_NUMBER: _ClassVar[int]
    legs: _containers.RepeatedCompositeFieldContainer[RoutingSummary.Leg]
    directions_uri: str

    def __init__(self, legs: _Optional[_Iterable[_Union[RoutingSummary.Leg, _Mapping]]]=..., directions_uri: _Optional[str]=...) -> None:
        ...