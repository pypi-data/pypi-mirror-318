from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheckRequest(_message.Message):
    __slots__ = ('cluster',)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: str

    def __init__(self, cluster: _Optional[str]=...) -> None:
        ...

class HealthCheckResponse(_message.Message):
    __slots__ = ('healthy', 'reason', 'cluster_info')
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    healthy: bool
    reason: str
    cluster_info: ClusterInfo

    def __init__(self, healthy: bool=..., reason: _Optional[str]=..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]]=...) -> None:
        ...

class ClusterInfo(_message.Message):
    __slots__ = ('streams_count', 'processes_count')
    STREAMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_COUNT_FIELD_NUMBER: _ClassVar[int]
    streams_count: int
    processes_count: int

    def __init__(self, streams_count: _Optional[int]=..., processes_count: _Optional[int]=...) -> None:
        ...