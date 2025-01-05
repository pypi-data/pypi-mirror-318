from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.datastream.v1 import datastream_resources_pb2 as _datastream_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoverConnectionProfileRequest(_message.Message):
    __slots__ = ("parent", "connection_profile", "connection_profile_name", "full_hierarchy", "hierarchy_depth", "oracle_rdbms", "mysql_rdbms", "postgresql_rdbms", "sql_server_rdbms")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_DEPTH_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RDBMS_FIELD_NUMBER: _ClassVar[int]
    MYSQL_RDBMS_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_RDBMS_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_RDBMS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection_profile: _datastream_resources_pb2.ConnectionProfile
    connection_profile_name: str
    full_hierarchy: bool
    hierarchy_depth: int
    oracle_rdbms: _datastream_resources_pb2.OracleRdbms
    mysql_rdbms: _datastream_resources_pb2.MysqlRdbms
    postgresql_rdbms: _datastream_resources_pb2.PostgresqlRdbms
    sql_server_rdbms: _datastream_resources_pb2.SqlServerRdbms
    def __init__(self, parent: _Optional[str] = ..., connection_profile: _Optional[_Union[_datastream_resources_pb2.ConnectionProfile, _Mapping]] = ..., connection_profile_name: _Optional[str] = ..., full_hierarchy: bool = ..., hierarchy_depth: _Optional[int] = ..., oracle_rdbms: _Optional[_Union[_datastream_resources_pb2.OracleRdbms, _Mapping]] = ..., mysql_rdbms: _Optional[_Union[_datastream_resources_pb2.MysqlRdbms, _Mapping]] = ..., postgresql_rdbms: _Optional[_Union[_datastream_resources_pb2.PostgresqlRdbms, _Mapping]] = ..., sql_server_rdbms: _Optional[_Union[_datastream_resources_pb2.SqlServerRdbms, _Mapping]] = ...) -> None: ...

class DiscoverConnectionProfileResponse(_message.Message):
    __slots__ = ("oracle_rdbms", "mysql_rdbms", "postgresql_rdbms", "sql_server_rdbms")
    ORACLE_RDBMS_FIELD_NUMBER: _ClassVar[int]
    MYSQL_RDBMS_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_RDBMS_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_RDBMS_FIELD_NUMBER: _ClassVar[int]
    oracle_rdbms: _datastream_resources_pb2.OracleRdbms
    mysql_rdbms: _datastream_resources_pb2.MysqlRdbms
    postgresql_rdbms: _datastream_resources_pb2.PostgresqlRdbms
    sql_server_rdbms: _datastream_resources_pb2.SqlServerRdbms
    def __init__(self, oracle_rdbms: _Optional[_Union[_datastream_resources_pb2.OracleRdbms, _Mapping]] = ..., mysql_rdbms: _Optional[_Union[_datastream_resources_pb2.MysqlRdbms, _Mapping]] = ..., postgresql_rdbms: _Optional[_Union[_datastream_resources_pb2.PostgresqlRdbms, _Mapping]] = ..., sql_server_rdbms: _Optional[_Union[_datastream_resources_pb2.SqlServerRdbms, _Mapping]] = ...) -> None: ...

class FetchStaticIpsRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class FetchStaticIpsResponse(_message.Message):
    __slots__ = ("static_ips", "next_page_token")
    STATIC_IPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    static_ips: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    def __init__(self, static_ips: _Optional[_Iterable[str]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListConnectionProfilesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListConnectionProfilesResponse(_message.Message):
    __slots__ = ("connection_profiles", "next_page_token", "unreachable")
    CONNECTION_PROFILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    connection_profiles: _containers.RepeatedCompositeFieldContainer[_datastream_resources_pb2.ConnectionProfile]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, connection_profiles: _Optional[_Iterable[_Union[_datastream_resources_pb2.ConnectionProfile, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetConnectionProfileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateConnectionProfileRequest(_message.Message):
    __slots__ = ("parent", "connection_profile_id", "connection_profile", "request_id", "validate_only", "force")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection_profile_id: str
    connection_profile: _datastream_resources_pb2.ConnectionProfile
    request_id: str
    validate_only: bool
    force: bool
    def __init__(self, parent: _Optional[str] = ..., connection_profile_id: _Optional[str] = ..., connection_profile: _Optional[_Union[_datastream_resources_pb2.ConnectionProfile, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., force: bool = ...) -> None: ...

class UpdateConnectionProfileRequest(_message.Message):
    __slots__ = ("update_mask", "connection_profile", "request_id", "validate_only", "force")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    connection_profile: _datastream_resources_pb2.ConnectionProfile
    request_id: str
    validate_only: bool
    force: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., connection_profile: _Optional[_Union[_datastream_resources_pb2.ConnectionProfile, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., force: bool = ...) -> None: ...

class DeleteConnectionProfileRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListStreamsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListStreamsResponse(_message.Message):
    __slots__ = ("streams", "next_page_token", "unreachable")
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    streams: _containers.RepeatedCompositeFieldContainer[_datastream_resources_pb2.Stream]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, streams: _Optional[_Iterable[_Union[_datastream_resources_pb2.Stream, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetStreamRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateStreamRequest(_message.Message):
    __slots__ = ("parent", "stream_id", "stream", "request_id", "validate_only", "force")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    stream_id: str
    stream: _datastream_resources_pb2.Stream
    request_id: str
    validate_only: bool
    force: bool
    def __init__(self, parent: _Optional[str] = ..., stream_id: _Optional[str] = ..., stream: _Optional[_Union[_datastream_resources_pb2.Stream, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., force: bool = ...) -> None: ...

class UpdateStreamRequest(_message.Message):
    __slots__ = ("update_mask", "stream", "request_id", "validate_only", "force")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    stream: _datastream_resources_pb2.Stream
    request_id: str
    validate_only: bool
    force: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., stream: _Optional[_Union[_datastream_resources_pb2.Stream, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., force: bool = ...) -> None: ...

class DeleteStreamRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class RunStreamRequest(_message.Message):
    __slots__ = ("name", "cdc_strategy", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CDC_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    cdc_strategy: _datastream_resources_pb2.CdcStrategy
    force: bool
    def __init__(self, name: _Optional[str] = ..., cdc_strategy: _Optional[_Union[_datastream_resources_pb2.CdcStrategy, _Mapping]] = ..., force: bool = ...) -> None: ...

class GetStreamObjectRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LookupStreamObjectRequest(_message.Message):
    __slots__ = ("parent", "source_object_identifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_object_identifier: _datastream_resources_pb2.SourceObjectIdentifier
    def __init__(self, parent: _Optional[str] = ..., source_object_identifier: _Optional[_Union[_datastream_resources_pb2.SourceObjectIdentifier, _Mapping]] = ...) -> None: ...

class StartBackfillJobRequest(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: str
    def __init__(self, object: _Optional[str] = ...) -> None: ...

class StartBackfillJobResponse(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _datastream_resources_pb2.StreamObject
    def __init__(self, object: _Optional[_Union[_datastream_resources_pb2.StreamObject, _Mapping]] = ...) -> None: ...

class StopBackfillJobRequest(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: str
    def __init__(self, object: _Optional[str] = ...) -> None: ...

class StopBackfillJobResponse(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _datastream_resources_pb2.StreamObject
    def __init__(self, object: _Optional[_Union[_datastream_resources_pb2.StreamObject, _Mapping]] = ...) -> None: ...

class ListStreamObjectsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListStreamObjectsResponse(_message.Message):
    __slots__ = ("stream_objects", "next_page_token")
    STREAM_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    stream_objects: _containers.RepeatedCompositeFieldContainer[_datastream_resources_pb2.StreamObject]
    next_page_token: str
    def __init__(self, stream_objects: _Optional[_Iterable[_Union[_datastream_resources_pb2.StreamObject, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version", "validation_result")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    validation_result: _datastream_resources_pb2.ValidationResult
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ..., validation_result: _Optional[_Union[_datastream_resources_pb2.ValidationResult, _Mapping]] = ...) -> None: ...

class CreatePrivateConnectionRequest(_message.Message):
    __slots__ = ("parent", "private_connection_id", "private_connection", "request_id", "force")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    private_connection_id: str
    private_connection: _datastream_resources_pb2.PrivateConnection
    request_id: str
    force: bool
    def __init__(self, parent: _Optional[str] = ..., private_connection_id: _Optional[str] = ..., private_connection: _Optional[_Union[_datastream_resources_pb2.PrivateConnection, _Mapping]] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class ListPrivateConnectionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListPrivateConnectionsResponse(_message.Message):
    __slots__ = ("private_connections", "next_page_token", "unreachable")
    PRIVATE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    private_connections: _containers.RepeatedCompositeFieldContainer[_datastream_resources_pb2.PrivateConnection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, private_connections: _Optional[_Iterable[_Union[_datastream_resources_pb2.PrivateConnection, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class DeletePrivateConnectionRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class GetPrivateConnectionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRouteRequest(_message.Message):
    __slots__ = ("parent", "route_id", "route", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    route_id: str
    route: _datastream_resources_pb2.Route
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., route_id: _Optional[str] = ..., route: _Optional[_Union[_datastream_resources_pb2.Route, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListRoutesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListRoutesResponse(_message.Message):
    __slots__ = ("routes", "next_page_token", "unreachable")
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[_datastream_resources_pb2.Route]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, routes: _Optional[_Iterable[_Union[_datastream_resources_pb2.Route, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteRouteRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetRouteRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
