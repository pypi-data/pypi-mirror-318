from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateConnectionRequest(_message.Message):
    __slots__ = ('parent', 'connection_id', 'connection')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection_id: str
    connection: Connection

    def __init__(self, parent: _Optional[str]=..., connection_id: _Optional[str]=..., connection: _Optional[_Union[Connection, _Mapping]]=...) -> None:
        ...

class GetConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'max_results', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    max_results: _wrappers_pb2.UInt32Value
    page_token: str

    def __init__(self, parent: _Optional[str]=..., max_results: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConnectionsResponse(_message.Message):
    __slots__ = ('next_page_token', 'connections')
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    connections: _containers.RepeatedCompositeFieldContainer[Connection]

    def __init__(self, next_page_token: _Optional[str]=..., connections: _Optional[_Iterable[_Union[Connection, _Mapping]]]=...) -> None:
        ...

class UpdateConnectionRequest(_message.Message):
    __slots__ = ('name', 'connection', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    connection: Connection
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., connection: _Optional[_Union[Connection, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateConnectionCredentialRequest(_message.Message):
    __slots__ = ('name', 'credential')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    credential: ConnectionCredential

    def __init__(self, name: _Optional[str]=..., credential: _Optional[_Union[ConnectionCredential, _Mapping]]=...) -> None:
        ...

class DeleteConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Connection(_message.Message):
    __slots__ = ('name', 'friendly_name', 'description', 'cloud_sql', 'creation_time', 'last_modified_time', 'has_credential')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    HAS_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    friendly_name: str
    description: str
    cloud_sql: CloudSqlProperties
    creation_time: int
    last_modified_time: int
    has_credential: bool

    def __init__(self, name: _Optional[str]=..., friendly_name: _Optional[str]=..., description: _Optional[str]=..., cloud_sql: _Optional[_Union[CloudSqlProperties, _Mapping]]=..., creation_time: _Optional[int]=..., last_modified_time: _Optional[int]=..., has_credential: bool=...) -> None:
        ...

class ConnectionCredential(_message.Message):
    __slots__ = ('cloud_sql',)
    CLOUD_SQL_FIELD_NUMBER: _ClassVar[int]
    cloud_sql: CloudSqlCredential

    def __init__(self, cloud_sql: _Optional[_Union[CloudSqlCredential, _Mapping]]=...) -> None:
        ...

class CloudSqlProperties(_message.Message):
    __slots__ = ('instance_id', 'database', 'type', 'credential', 'service_account_id')

    class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_TYPE_UNSPECIFIED: _ClassVar[CloudSqlProperties.DatabaseType]
        POSTGRES: _ClassVar[CloudSqlProperties.DatabaseType]
        MYSQL: _ClassVar[CloudSqlProperties.DatabaseType]
    DATABASE_TYPE_UNSPECIFIED: CloudSqlProperties.DatabaseType
    POSTGRES: CloudSqlProperties.DatabaseType
    MYSQL: CloudSqlProperties.DatabaseType
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    database: str
    type: CloudSqlProperties.DatabaseType
    credential: CloudSqlCredential
    service_account_id: str

    def __init__(self, instance_id: _Optional[str]=..., database: _Optional[str]=..., type: _Optional[_Union[CloudSqlProperties.DatabaseType, str]]=..., credential: _Optional[_Union[CloudSqlCredential, _Mapping]]=..., service_account_id: _Optional[str]=...) -> None:
        ...

class CloudSqlCredential(_message.Message):
    __slots__ = ('username', 'password')
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str

    def __init__(self, username: _Optional[str]=..., password: _Optional[str]=...) -> None:
        ...