from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseEngine(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_ENGINE_UNSPECIFIED: _ClassVar[DatabaseEngine]
    MYSQL: _ClassVar[DatabaseEngine]
    POSTGRESQL: _ClassVar[DatabaseEngine]
    SQLSERVER: _ClassVar[DatabaseEngine]
    ORACLE: _ClassVar[DatabaseEngine]
    SPANNER: _ClassVar[DatabaseEngine]

class DatabaseProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_PROVIDER_UNSPECIFIED: _ClassVar[DatabaseProvider]
    CLOUDSQL: _ClassVar[DatabaseProvider]
    RDS: _ClassVar[DatabaseProvider]
    AURORA: _ClassVar[DatabaseProvider]
    ALLOYDB: _ClassVar[DatabaseProvider]
DATABASE_ENGINE_UNSPECIFIED: DatabaseEngine
MYSQL: DatabaseEngine
POSTGRESQL: DatabaseEngine
SQLSERVER: DatabaseEngine
ORACLE: DatabaseEngine
SPANNER: DatabaseEngine
DATABASE_PROVIDER_UNSPECIFIED: DatabaseProvider
CLOUDSQL: DatabaseProvider
RDS: DatabaseProvider
AURORA: DatabaseProvider
ALLOYDB: DatabaseProvider

class DatabaseType(_message.Message):
    __slots__ = ('provider', 'engine')
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    provider: DatabaseProvider
    engine: DatabaseEngine

    def __init__(self, provider: _Optional[_Union[DatabaseProvider, str]]=..., engine: _Optional[_Union[DatabaseEngine, str]]=...) -> None:
        ...

class LoggedMigrationJob(_message.Message):
    __slots__ = ('name', 'labels', 'display_name', 'state', 'phase', 'type', 'dump_path', 'source', 'destination', 'duration', 'connectivity_type', 'error', 'end_time', 'source_database', 'destination_database')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LoggedMigrationJob.State]
        MAINTENANCE: _ClassVar[LoggedMigrationJob.State]
        DRAFT: _ClassVar[LoggedMigrationJob.State]
        CREATING: _ClassVar[LoggedMigrationJob.State]
        NOT_STARTED: _ClassVar[LoggedMigrationJob.State]
        RUNNING: _ClassVar[LoggedMigrationJob.State]
        FAILED: _ClassVar[LoggedMigrationJob.State]
        COMPLETED: _ClassVar[LoggedMigrationJob.State]
        DELETING: _ClassVar[LoggedMigrationJob.State]
        STOPPING: _ClassVar[LoggedMigrationJob.State]
        STOPPED: _ClassVar[LoggedMigrationJob.State]
        DELETED: _ClassVar[LoggedMigrationJob.State]
        UPDATING: _ClassVar[LoggedMigrationJob.State]
        STARTING: _ClassVar[LoggedMigrationJob.State]
        RESTARTING: _ClassVar[LoggedMigrationJob.State]
        RESUMING: _ClassVar[LoggedMigrationJob.State]
    STATE_UNSPECIFIED: LoggedMigrationJob.State
    MAINTENANCE: LoggedMigrationJob.State
    DRAFT: LoggedMigrationJob.State
    CREATING: LoggedMigrationJob.State
    NOT_STARTED: LoggedMigrationJob.State
    RUNNING: LoggedMigrationJob.State
    FAILED: LoggedMigrationJob.State
    COMPLETED: LoggedMigrationJob.State
    DELETING: LoggedMigrationJob.State
    STOPPING: LoggedMigrationJob.State
    STOPPED: LoggedMigrationJob.State
    DELETED: LoggedMigrationJob.State
    UPDATING: LoggedMigrationJob.State
    STARTING: LoggedMigrationJob.State
    RESTARTING: LoggedMigrationJob.State
    RESUMING: LoggedMigrationJob.State

    class Phase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHASE_UNSPECIFIED: _ClassVar[LoggedMigrationJob.Phase]
        FULL_DUMP: _ClassVar[LoggedMigrationJob.Phase]
        CDC: _ClassVar[LoggedMigrationJob.Phase]
        PROMOTE_IN_PROGRESS: _ClassVar[LoggedMigrationJob.Phase]
        WAITING_FOR_SOURCE_WRITES_TO_STOP: _ClassVar[LoggedMigrationJob.Phase]
        PREPARING_THE_DUMP: _ClassVar[LoggedMigrationJob.Phase]
    PHASE_UNSPECIFIED: LoggedMigrationJob.Phase
    FULL_DUMP: LoggedMigrationJob.Phase
    CDC: LoggedMigrationJob.Phase
    PROMOTE_IN_PROGRESS: LoggedMigrationJob.Phase
    WAITING_FOR_SOURCE_WRITES_TO_STOP: LoggedMigrationJob.Phase
    PREPARING_THE_DUMP: LoggedMigrationJob.Phase

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[LoggedMigrationJob.Type]
        ONE_TIME: _ClassVar[LoggedMigrationJob.Type]
        CONTINUOUS: _ClassVar[LoggedMigrationJob.Type]
    TYPE_UNSPECIFIED: LoggedMigrationJob.Type
    ONE_TIME: LoggedMigrationJob.Type
    CONTINUOUS: LoggedMigrationJob.Type

    class ConnectivityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTIVITY_TYPE_UNSPECIFIED: _ClassVar[LoggedMigrationJob.ConnectivityType]
        STATIC_IP: _ClassVar[LoggedMigrationJob.ConnectivityType]
        REVERSE_SSH: _ClassVar[LoggedMigrationJob.ConnectivityType]
        VPC_PEERING: _ClassVar[LoggedMigrationJob.ConnectivityType]
    CONNECTIVITY_TYPE_UNSPECIFIED: LoggedMigrationJob.ConnectivityType
    STATIC_IP: LoggedMigrationJob.ConnectivityType
    REVERSE_SSH: LoggedMigrationJob.ConnectivityType
    VPC_PEERING: LoggedMigrationJob.ConnectivityType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DUMP_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CONNECTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DATABASE_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    display_name: str
    state: LoggedMigrationJob.State
    phase: LoggedMigrationJob.Phase
    type: LoggedMigrationJob.Type
    dump_path: str
    source: str
    destination: str
    duration: _duration_pb2.Duration
    connectivity_type: LoggedMigrationJob.ConnectivityType
    error: _status_pb2.Status
    end_time: _timestamp_pb2.Timestamp
    source_database: DatabaseType
    destination_database: DatabaseType

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., state: _Optional[_Union[LoggedMigrationJob.State, str]]=..., phase: _Optional[_Union[LoggedMigrationJob.Phase, str]]=..., type: _Optional[_Union[LoggedMigrationJob.Type, str]]=..., dump_path: _Optional[str]=..., source: _Optional[str]=..., destination: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., connectivity_type: _Optional[_Union[LoggedMigrationJob.ConnectivityType, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., source_database: _Optional[_Union[DatabaseType, _Mapping]]=..., destination_database: _Optional[_Union[DatabaseType, _Mapping]]=...) -> None:
        ...

class MySqlConnectionProfile(_message.Message):
    __slots__ = ('version', 'cloud_sql_id')

    class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERSION_UNSPECIFIED: _ClassVar[MySqlConnectionProfile.Version]
        V5_5: _ClassVar[MySqlConnectionProfile.Version]
        V5_6: _ClassVar[MySqlConnectionProfile.Version]
        V5_7: _ClassVar[MySqlConnectionProfile.Version]
        V8_0: _ClassVar[MySqlConnectionProfile.Version]
    VERSION_UNSPECIFIED: MySqlConnectionProfile.Version
    V5_5: MySqlConnectionProfile.Version
    V5_6: MySqlConnectionProfile.Version
    V5_7: MySqlConnectionProfile.Version
    V8_0: MySqlConnectionProfile.Version
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    version: MySqlConnectionProfile.Version
    cloud_sql_id: str

    def __init__(self, version: _Optional[_Union[MySqlConnectionProfile.Version, str]]=..., cloud_sql_id: _Optional[str]=...) -> None:
        ...

class PostgreSqlConnectionProfile(_message.Message):
    __slots__ = ('version', 'cloud_sql_id')

    class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERSION_UNSPECIFIED: _ClassVar[PostgreSqlConnectionProfile.Version]
        V9_6: _ClassVar[PostgreSqlConnectionProfile.Version]
        V11: _ClassVar[PostgreSqlConnectionProfile.Version]
        V10: _ClassVar[PostgreSqlConnectionProfile.Version]
        V12: _ClassVar[PostgreSqlConnectionProfile.Version]
        V13: _ClassVar[PostgreSqlConnectionProfile.Version]
    VERSION_UNSPECIFIED: PostgreSqlConnectionProfile.Version
    V9_6: PostgreSqlConnectionProfile.Version
    V11: PostgreSqlConnectionProfile.Version
    V10: PostgreSqlConnectionProfile.Version
    V12: PostgreSqlConnectionProfile.Version
    V13: PostgreSqlConnectionProfile.Version
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    version: PostgreSqlConnectionProfile.Version
    cloud_sql_id: str

    def __init__(self, version: _Optional[_Union[PostgreSqlConnectionProfile.Version, str]]=..., cloud_sql_id: _Optional[str]=...) -> None:
        ...

class CloudSqlConnectionProfile(_message.Message):
    __slots__ = ('cloud_sql_id',)
    CLOUD_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_sql_id: str

    def __init__(self, cloud_sql_id: _Optional[str]=...) -> None:
        ...

class OracleConnectionProfile(_message.Message):
    __slots__ = ('connectivity_type',)

    class ConnectivityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTIVITY_TYPE_UNSPECIFIED: _ClassVar[OracleConnectionProfile.ConnectivityType]
        STATIC_SERVICE_IP: _ClassVar[OracleConnectionProfile.ConnectivityType]
        FORWARD_SSH_TUNNEL: _ClassVar[OracleConnectionProfile.ConnectivityType]
        PRIVATE_CONNECTIVITY: _ClassVar[OracleConnectionProfile.ConnectivityType]
    CONNECTIVITY_TYPE_UNSPECIFIED: OracleConnectionProfile.ConnectivityType
    STATIC_SERVICE_IP: OracleConnectionProfile.ConnectivityType
    FORWARD_SSH_TUNNEL: OracleConnectionProfile.ConnectivityType
    PRIVATE_CONNECTIVITY: OracleConnectionProfile.ConnectivityType
    CONNECTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    connectivity_type: OracleConnectionProfile.ConnectivityType

    def __init__(self, connectivity_type: _Optional[_Union[OracleConnectionProfile.ConnectivityType, str]]=...) -> None:
        ...

class LoggedConnectionProfile(_message.Message):
    __slots__ = ('name', 'labels', 'state', 'display_name', 'mysql', 'postgresql', 'cloudsql', 'oracle', 'error', 'provider')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LoggedConnectionProfile.State]
        DRAFT: _ClassVar[LoggedConnectionProfile.State]
        CREATING: _ClassVar[LoggedConnectionProfile.State]
        READY: _ClassVar[LoggedConnectionProfile.State]
        UPDATING: _ClassVar[LoggedConnectionProfile.State]
        DELETING: _ClassVar[LoggedConnectionProfile.State]
        DELETED: _ClassVar[LoggedConnectionProfile.State]
        FAILED: _ClassVar[LoggedConnectionProfile.State]
    STATE_UNSPECIFIED: LoggedConnectionProfile.State
    DRAFT: LoggedConnectionProfile.State
    CREATING: LoggedConnectionProfile.State
    READY: LoggedConnectionProfile.State
    UPDATING: LoggedConnectionProfile.State
    DELETING: LoggedConnectionProfile.State
    DELETED: LoggedConnectionProfile.State
    FAILED: LoggedConnectionProfile.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MYSQL_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_FIELD_NUMBER: _ClassVar[int]
    CLOUDSQL_FIELD_NUMBER: _ClassVar[int]
    ORACLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    state: LoggedConnectionProfile.State
    display_name: str
    mysql: MySqlConnectionProfile
    postgresql: PostgreSqlConnectionProfile
    cloudsql: CloudSqlConnectionProfile
    oracle: OracleConnectionProfile
    error: _status_pb2.Status
    provider: DatabaseProvider

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[LoggedConnectionProfile.State, str]]=..., display_name: _Optional[str]=..., mysql: _Optional[_Union[MySqlConnectionProfile, _Mapping]]=..., postgresql: _Optional[_Union[PostgreSqlConnectionProfile, _Mapping]]=..., cloudsql: _Optional[_Union[CloudSqlConnectionProfile, _Mapping]]=..., oracle: _Optional[_Union[OracleConnectionProfile, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., provider: _Optional[_Union[DatabaseProvider, str]]=...) -> None:
        ...

class MigrationJobEventLog(_message.Message):
    __slots__ = ('migration_job', 'occurrence_timestamp', 'code', 'text_message', 'original_code', 'original_message')
    MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CODE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    migration_job: LoggedMigrationJob
    occurrence_timestamp: _timestamp_pb2.Timestamp
    code: int
    text_message: str
    original_code: int
    original_message: str

    def __init__(self, migration_job: _Optional[_Union[LoggedMigrationJob, _Mapping]]=..., occurrence_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., code: _Optional[int]=..., text_message: _Optional[str]=..., original_code: _Optional[int]=..., original_message: _Optional[str]=...) -> None:
        ...

class ConnectionProfileEventLog(_message.Message):
    __slots__ = ('connection_profile', 'occurrence_timestamp', 'code', 'text_message', 'original_code', 'original_message')
    CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CODE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    connection_profile: LoggedConnectionProfile
    occurrence_timestamp: _timestamp_pb2.Timestamp
    code: int
    text_message: str
    original_code: int
    original_message: str

    def __init__(self, connection_profile: _Optional[_Union[LoggedConnectionProfile, _Mapping]]=..., occurrence_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., code: _Optional[int]=..., text_message: _Optional[str]=..., original_code: _Optional[int]=..., original_message: _Optional[str]=...) -> None:
        ...

class LoggedPrivateConnection(_message.Message):
    __slots__ = ('name', 'labels', 'display_name', 'state', 'error', 'vpc_peering_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LoggedPrivateConnection.State]
        CREATING: _ClassVar[LoggedPrivateConnection.State]
        CREATED: _ClassVar[LoggedPrivateConnection.State]
        FAILED: _ClassVar[LoggedPrivateConnection.State]
        DELETING: _ClassVar[LoggedPrivateConnection.State]
        FAILED_TO_DELETE: _ClassVar[LoggedPrivateConnection.State]
        DELETED: _ClassVar[LoggedPrivateConnection.State]
    STATE_UNSPECIFIED: LoggedPrivateConnection.State
    CREATING: LoggedPrivateConnection.State
    CREATED: LoggedPrivateConnection.State
    FAILED: LoggedPrivateConnection.State
    DELETING: LoggedPrivateConnection.State
    FAILED_TO_DELETE: LoggedPrivateConnection.State
    DELETED: LoggedPrivateConnection.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VPC_PEERING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    display_name: str
    state: LoggedPrivateConnection.State
    error: _status_pb2.Status
    vpc_peering_config: VpcPeeringConfig

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., state: _Optional[_Union[LoggedPrivateConnection.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., vpc_peering_config: _Optional[_Union[VpcPeeringConfig, _Mapping]]=...) -> None:
        ...

class VpcPeeringConfig(_message.Message):
    __slots__ = ('vpc_name', 'subnet')
    VPC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    vpc_name: str
    subnet: str

    def __init__(self, vpc_name: _Optional[str]=..., subnet: _Optional[str]=...) -> None:
        ...

class PrivateConnectionEventLog(_message.Message):
    __slots__ = ('private_connection', 'occurrence_timestamp', 'code', 'text_message', 'original_code', 'original_message')
    PRIVATE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CODE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    private_connection: LoggedPrivateConnection
    occurrence_timestamp: _timestamp_pb2.Timestamp
    code: int
    text_message: str
    original_code: int
    original_message: str

    def __init__(self, private_connection: _Optional[_Union[LoggedPrivateConnection, _Mapping]]=..., occurrence_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., code: _Optional[int]=..., text_message: _Optional[str]=..., original_code: _Optional[int]=..., original_message: _Optional[str]=...) -> None:
        ...