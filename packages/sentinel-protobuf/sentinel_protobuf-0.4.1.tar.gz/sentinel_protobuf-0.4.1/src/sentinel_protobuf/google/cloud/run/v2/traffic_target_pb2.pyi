from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TrafficTargetAllocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED: _ClassVar[TrafficTargetAllocationType]
    TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST: _ClassVar[TrafficTargetAllocationType]
    TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION: _ClassVar[TrafficTargetAllocationType]
TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED: TrafficTargetAllocationType
TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST: TrafficTargetAllocationType
TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION: TrafficTargetAllocationType

class TrafficTarget(_message.Message):
    __slots__ = ('type', 'revision', 'percent', 'tag')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    type: TrafficTargetAllocationType
    revision: str
    percent: int
    tag: str

    def __init__(self, type: _Optional[_Union[TrafficTargetAllocationType, str]]=..., revision: _Optional[str]=..., percent: _Optional[int]=..., tag: _Optional[str]=...) -> None:
        ...

class TrafficTargetStatus(_message.Message):
    __slots__ = ('type', 'revision', 'percent', 'tag', 'uri')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    type: TrafficTargetAllocationType
    revision: str
    percent: int
    tag: str
    uri: str

    def __init__(self, type: _Optional[_Union[TrafficTargetAllocationType, str]]=..., revision: _Optional[str]=..., percent: _Optional[int]=..., tag: _Optional[str]=..., uri: _Optional[str]=...) -> None:
        ...