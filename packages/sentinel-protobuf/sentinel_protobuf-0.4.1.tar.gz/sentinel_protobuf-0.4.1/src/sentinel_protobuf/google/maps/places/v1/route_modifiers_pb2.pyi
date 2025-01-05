from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class RouteModifiers(_message.Message):
    __slots__ = ('avoid_tolls', 'avoid_highways', 'avoid_ferries', 'avoid_indoor')
    AVOID_TOLLS_FIELD_NUMBER: _ClassVar[int]
    AVOID_HIGHWAYS_FIELD_NUMBER: _ClassVar[int]
    AVOID_FERRIES_FIELD_NUMBER: _ClassVar[int]
    AVOID_INDOOR_FIELD_NUMBER: _ClassVar[int]
    avoid_tolls: bool
    avoid_highways: bool
    avoid_ferries: bool
    avoid_indoor: bool

    def __init__(self, avoid_tolls: bool=..., avoid_highways: bool=..., avoid_ferries: bool=..., avoid_indoor: bool=...) -> None:
        ...