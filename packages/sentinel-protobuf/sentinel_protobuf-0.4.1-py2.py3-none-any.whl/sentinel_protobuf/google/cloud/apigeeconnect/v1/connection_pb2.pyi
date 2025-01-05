from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConnectionsResponse(_message.Message):
    __slots__ = ('connections', 'next_page_token')
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    next_page_token: str

    def __init__(self, connections: _Optional[_Iterable[_Union[Connection, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Connection(_message.Message):
    __slots__ = ('endpoint', 'cluster', 'stream_count')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    STREAM_COUNT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    cluster: Cluster
    stream_count: int

    def __init__(self, endpoint: _Optional[str]=..., cluster: _Optional[_Union[Cluster, _Mapping]]=..., stream_count: _Optional[int]=...) -> None:
        ...

class Cluster(_message.Message):
    __slots__ = ('name', 'region')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    name: str
    region: str

    def __init__(self, name: _Optional[str]=..., region: _Optional[str]=...) -> None:
        ...