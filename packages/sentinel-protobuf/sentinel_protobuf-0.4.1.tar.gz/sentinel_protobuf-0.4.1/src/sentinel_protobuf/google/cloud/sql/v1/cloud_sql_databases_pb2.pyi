from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlDatabasesDeleteRequest(_message.Message):
    __slots__ = ("database", "instance", "project")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    database: str
    instance: str
    project: str
    def __init__(self, database: _Optional[str] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlDatabasesGetRequest(_message.Message):
    __slots__ = ("database", "instance", "project")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    database: str
    instance: str
    project: str
    def __init__(self, database: _Optional[str] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlDatabasesInsertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.Database
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.Database, _Mapping]] = ...) -> None: ...

class SqlDatabasesListRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlDatabasesUpdateRequest(_message.Message):
    __slots__ = ("database", "instance", "project", "body")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    database: str
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.Database
    def __init__(self, database: _Optional[str] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.Database, _Mapping]] = ...) -> None: ...

class DatabasesListResponse(_message.Message):
    __slots__ = ("kind", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[_cloud_sql_resources_pb2.Database]
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.Database, _Mapping]]] = ...) -> None: ...
