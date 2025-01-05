from google.ads.searchads360.v0.enums import targeting_dimension_pb2 as _targeting_dimension_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TargetingSetting(_message.Message):
    __slots__ = ("target_restrictions",)
    TARGET_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    target_restrictions: _containers.RepeatedCompositeFieldContainer[TargetRestriction]
    def __init__(self, target_restrictions: _Optional[_Iterable[_Union[TargetRestriction, _Mapping]]] = ...) -> None: ...

class TargetRestriction(_message.Message):
    __slots__ = ("targeting_dimension", "bid_only")
    TARGETING_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    BID_ONLY_FIELD_NUMBER: _ClassVar[int]
    targeting_dimension: _targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension
    bid_only: bool
    def __init__(self, targeting_dimension: _Optional[_Union[_targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension, str]] = ..., bid_only: bool = ...) -> None: ...
