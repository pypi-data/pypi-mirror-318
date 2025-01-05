from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlOperationsGetRequest(_message.Message):
    __slots__ = ("operation", "project")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    operation: str
    project: str
    def __init__(self, operation: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlOperationsListRequest(_message.Message):
    __slots__ = ("instance", "max_results", "page_token", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    max_results: int
    page_token: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., max_results: _Optional[int] = ..., page_token: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class OperationsListResponse(_message.Message):
    __slots__ = ("kind", "items", "next_page_token")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[_cloud_sql_resources_pb2.Operation]
    next_page_token: str
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.Operation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SqlOperationsCancelRequest(_message.Message):
    __slots__ = ("operation", "project")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    operation: str
    project: str
    def __init__(self, operation: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...
