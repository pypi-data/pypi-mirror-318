from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TrafficModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAFFIC_MODEL_UNSPECIFIED: _ClassVar[TrafficModel]
    BEST_GUESS: _ClassVar[TrafficModel]
    PESSIMISTIC: _ClassVar[TrafficModel]
    OPTIMISTIC: _ClassVar[TrafficModel]
TRAFFIC_MODEL_UNSPECIFIED: TrafficModel
BEST_GUESS: TrafficModel
PESSIMISTIC: TrafficModel
OPTIMISTIC: TrafficModel