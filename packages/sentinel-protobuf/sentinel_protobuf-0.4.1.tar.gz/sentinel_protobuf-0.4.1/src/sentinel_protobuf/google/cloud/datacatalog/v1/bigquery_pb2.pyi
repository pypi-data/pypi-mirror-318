from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BigQueryConnectionSpec(_message.Message):
    __slots__ = ('connection_type', 'cloud_sql', 'has_credential')

    class ConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_TYPE_UNSPECIFIED: _ClassVar[BigQueryConnectionSpec.ConnectionType]
        CLOUD_SQL: _ClassVar[BigQueryConnectionSpec.ConnectionType]
    CONNECTION_TYPE_UNSPECIFIED: BigQueryConnectionSpec.ConnectionType
    CLOUD_SQL: BigQueryConnectionSpec.ConnectionType
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_FIELD_NUMBER: _ClassVar[int]
    HAS_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    connection_type: BigQueryConnectionSpec.ConnectionType
    cloud_sql: CloudSqlBigQueryConnectionSpec
    has_credential: bool

    def __init__(self, connection_type: _Optional[_Union[BigQueryConnectionSpec.ConnectionType, str]]=..., cloud_sql: _Optional[_Union[CloudSqlBigQueryConnectionSpec, _Mapping]]=..., has_credential: bool=...) -> None:
        ...

class CloudSqlBigQueryConnectionSpec(_message.Message):
    __slots__ = ('instance_id', 'database', 'type')

    class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_TYPE_UNSPECIFIED: _ClassVar[CloudSqlBigQueryConnectionSpec.DatabaseType]
        POSTGRES: _ClassVar[CloudSqlBigQueryConnectionSpec.DatabaseType]
        MYSQL: _ClassVar[CloudSqlBigQueryConnectionSpec.DatabaseType]
    DATABASE_TYPE_UNSPECIFIED: CloudSqlBigQueryConnectionSpec.DatabaseType
    POSTGRES: CloudSqlBigQueryConnectionSpec.DatabaseType
    MYSQL: CloudSqlBigQueryConnectionSpec.DatabaseType
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    database: str
    type: CloudSqlBigQueryConnectionSpec.DatabaseType

    def __init__(self, instance_id: _Optional[str]=..., database: _Optional[str]=..., type: _Optional[_Union[CloudSqlBigQueryConnectionSpec.DatabaseType, str]]=...) -> None:
        ...

class BigQueryRoutineSpec(_message.Message):
    __slots__ = ('imported_libraries',)
    IMPORTED_LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    imported_libraries: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, imported_libraries: _Optional[_Iterable[str]]=...) -> None:
        ...