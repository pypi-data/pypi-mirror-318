from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataproc.v1 import clusters_pb2 as _clusters_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNodeGroupRequest(_message.Message):
    __slots__ = ("parent", "node_group", "node_group_id", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    node_group: _clusters_pb2.NodeGroup
    node_group_id: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., node_group: _Optional[_Union[_clusters_pb2.NodeGroup, _Mapping]] = ..., node_group_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ResizeNodeGroupRequest(_message.Message):
    __slots__ = ("name", "size", "request_id", "graceful_decommission_timeout")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    GRACEFUL_DECOMMISSION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    request_id: str
    graceful_decommission_timeout: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., request_id: _Optional[str] = ..., graceful_decommission_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GetNodeGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
