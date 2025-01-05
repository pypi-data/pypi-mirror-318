from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OracleProfile(_message.Message):
    __slots__ = ("hostname", "port", "username", "password", "database_service", "connection_attributes", "oracle_ssl_config", "oracle_asm_config", "secret_manager_stored_password")
    class ConnectionAttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SSL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ASM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECRET_MANAGER_STORED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    port: int
    username: str
    password: str
    database_service: str
    connection_attributes: _containers.ScalarMap[str, str]
    oracle_ssl_config: OracleSslConfig
    oracle_asm_config: OracleAsmConfig
    secret_manager_stored_password: str
    def __init__(self, hostname: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., database_service: _Optional[str] = ..., connection_attributes: _Optional[_Mapping[str, str]] = ..., oracle_ssl_config: _Optional[_Union[OracleSslConfig, _Mapping]] = ..., oracle_asm_config: _Optional[_Union[OracleAsmConfig, _Mapping]] = ..., secret_manager_stored_password: _Optional[str] = ...) -> None: ...

class OracleAsmConfig(_message.Message):
    __slots__ = ("hostname", "port", "username", "password", "asm_service", "connection_attributes", "oracle_ssl_config")
    class ConnectionAttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ASM_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SSL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    port: int
    username: str
    password: str
    asm_service: str
    connection_attributes: _containers.ScalarMap[str, str]
    oracle_ssl_config: OracleSslConfig
    def __init__(self, hostname: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., asm_service: _Optional[str] = ..., connection_attributes: _Optional[_Mapping[str, str]] = ..., oracle_ssl_config: _Optional[_Union[OracleSslConfig, _Mapping]] = ...) -> None: ...

class MysqlProfile(_message.Message):
    __slots__ = ("hostname", "port", "username", "password", "ssl_config")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SSL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    port: int
    username: str
    password: str
    ssl_config: MysqlSslConfig
    def __init__(self, hostname: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., ssl_config: _Optional[_Union[MysqlSslConfig, _Mapping]] = ...) -> None: ...

class PostgresqlProfile(_message.Message):
    __slots__ = ("hostname", "port", "username", "password", "database")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    port: int
    username: str
    password: str
    database: str
    def __init__(self, hostname: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., database: _Optional[str] = ...) -> None: ...

class SqlServerProfile(_message.Message):
    __slots__ = ("hostname", "port", "username", "password", "database")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    port: int
    username: str
    password: str
    database: str
    def __init__(self, hostname: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., database: _Optional[str] = ...) -> None: ...

class GcsProfile(_message.Message):
    __slots__ = ("bucket", "root_path")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    root_path: str
    def __init__(self, bucket: _Optional[str] = ..., root_path: _Optional[str] = ...) -> None: ...

class BigQueryProfile(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StaticServiceIpConnectivity(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ForwardSshTunnelConnectivity(_message.Message):
    __slots__ = ("hostname", "username", "port", "password", "private_key")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    username: str
    port: int
    password: str
    private_key: str
    def __init__(self, hostname: _Optional[str] = ..., username: _Optional[str] = ..., port: _Optional[int] = ..., password: _Optional[str] = ..., private_key: _Optional[str] = ...) -> None: ...

class VpcPeeringConfig(_message.Message):
    __slots__ = ("vpc", "subnet")
    VPC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    vpc: str
    subnet: str
    def __init__(self, vpc: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...

class PrivateConnection(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "state", "error", "vpc_peering_config")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PrivateConnection.State]
        CREATING: _ClassVar[PrivateConnection.State]
        CREATED: _ClassVar[PrivateConnection.State]
        FAILED: _ClassVar[PrivateConnection.State]
        DELETING: _ClassVar[PrivateConnection.State]
        FAILED_TO_DELETE: _ClassVar[PrivateConnection.State]
    STATE_UNSPECIFIED: PrivateConnection.State
    CREATING: PrivateConnection.State
    CREATED: PrivateConnection.State
    FAILED: PrivateConnection.State
    DELETING: PrivateConnection.State
    FAILED_TO_DELETE: PrivateConnection.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VPC_PEERING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    state: PrivateConnection.State
    error: Error
    vpc_peering_config: VpcPeeringConfig
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., state: _Optional[_Union[PrivateConnection.State, str]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., vpc_peering_config: _Optional[_Union[VpcPeeringConfig, _Mapping]] = ...) -> None: ...

class PrivateConnectivity(_message.Message):
    __slots__ = ("private_connection",)
    PRIVATE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    private_connection: str
    def __init__(self, private_connection: _Optional[str] = ...) -> None: ...

class Route(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "destination_address", "destination_port")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    destination_address: str
    destination_port: int
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., destination_address: _Optional[str] = ..., destination_port: _Optional[int] = ...) -> None: ...

class MysqlSslConfig(_message.Message):
    __slots__ = ("client_key", "client_key_set", "client_certificate", "client_certificate_set", "ca_certificate", "ca_certificate_set")
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_SET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_SET_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_SET_FIELD_NUMBER: _ClassVar[int]
    client_key: str
    client_key_set: bool
    client_certificate: str
    client_certificate_set: bool
    ca_certificate: str
    ca_certificate_set: bool
    def __init__(self, client_key: _Optional[str] = ..., client_key_set: bool = ..., client_certificate: _Optional[str] = ..., client_certificate_set: bool = ..., ca_certificate: _Optional[str] = ..., ca_certificate_set: bool = ...) -> None: ...

class OracleSslConfig(_message.Message):
    __slots__ = ("ca_certificate", "ca_certificate_set")
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_SET_FIELD_NUMBER: _ClassVar[int]
    ca_certificate: str
    ca_certificate_set: bool
    def __init__(self, ca_certificate: _Optional[str] = ..., ca_certificate_set: bool = ...) -> None: ...

class ConnectionProfile(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "oracle_profile", "gcs_profile", "mysql_profile", "bigquery_profile", "postgresql_profile", "sql_server_profile", "static_service_ip_connectivity", "forward_ssh_connectivity", "private_connectivity")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    GCS_PROFILE_FIELD_NUMBER: _ClassVar[int]
    MYSQL_PROFILE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    STATIC_SERVICE_IP_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    FORWARD_SSH_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    oracle_profile: OracleProfile
    gcs_profile: GcsProfile
    mysql_profile: MysqlProfile
    bigquery_profile: BigQueryProfile
    postgresql_profile: PostgresqlProfile
    sql_server_profile: SqlServerProfile
    static_service_ip_connectivity: StaticServiceIpConnectivity
    forward_ssh_connectivity: ForwardSshTunnelConnectivity
    private_connectivity: PrivateConnectivity
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., oracle_profile: _Optional[_Union[OracleProfile, _Mapping]] = ..., gcs_profile: _Optional[_Union[GcsProfile, _Mapping]] = ..., mysql_profile: _Optional[_Union[MysqlProfile, _Mapping]] = ..., bigquery_profile: _Optional[_Union[BigQueryProfile, _Mapping]] = ..., postgresql_profile: _Optional[_Union[PostgresqlProfile, _Mapping]] = ..., sql_server_profile: _Optional[_Union[SqlServerProfile, _Mapping]] = ..., static_service_ip_connectivity: _Optional[_Union[StaticServiceIpConnectivity, _Mapping]] = ..., forward_ssh_connectivity: _Optional[_Union[ForwardSshTunnelConnectivity, _Mapping]] = ..., private_connectivity: _Optional[_Union[PrivateConnectivity, _Mapping]] = ...) -> None: ...

class OracleColumn(_message.Message):
    __slots__ = ("column", "data_type", "length", "precision", "scale", "encoding", "primary_key", "nullable", "ordinal_position")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    column: str
    data_type: str
    length: int
    precision: int
    scale: int
    encoding: str
    primary_key: bool
    nullable: bool
    ordinal_position: int
    def __init__(self, column: _Optional[str] = ..., data_type: _Optional[str] = ..., length: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ..., encoding: _Optional[str] = ..., primary_key: bool = ..., nullable: bool = ..., ordinal_position: _Optional[int] = ...) -> None: ...

class OracleTable(_message.Message):
    __slots__ = ("table", "oracle_columns")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ORACLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    table: str
    oracle_columns: _containers.RepeatedCompositeFieldContainer[OracleColumn]
    def __init__(self, table: _Optional[str] = ..., oracle_columns: _Optional[_Iterable[_Union[OracleColumn, _Mapping]]] = ...) -> None: ...

class OracleSchema(_message.Message):
    __slots__ = ("schema", "oracle_tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ORACLE_TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    oracle_tables: _containers.RepeatedCompositeFieldContainer[OracleTable]
    def __init__(self, schema: _Optional[str] = ..., oracle_tables: _Optional[_Iterable[_Union[OracleTable, _Mapping]]] = ...) -> None: ...

class OracleRdbms(_message.Message):
    __slots__ = ("oracle_schemas",)
    ORACLE_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    oracle_schemas: _containers.RepeatedCompositeFieldContainer[OracleSchema]
    def __init__(self, oracle_schemas: _Optional[_Iterable[_Union[OracleSchema, _Mapping]]] = ...) -> None: ...

class OracleSourceConfig(_message.Message):
    __slots__ = ("include_objects", "exclude_objects", "max_concurrent_cdc_tasks", "max_concurrent_backfill_tasks", "drop_large_objects", "stream_large_objects", "log_miner", "binary_log_parser")
    class DropLargeObjects(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StreamLargeObjects(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class LogMiner(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class BinaryLogParser(_message.Message):
        __slots__ = ("oracle_asm_log_file_access", "log_file_directories")
        class OracleAsmLogFileAccess(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class LogFileDirectories(_message.Message):
            __slots__ = ("online_log_directory", "archived_log_directory")
            ONLINE_LOG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
            ARCHIVED_LOG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
            online_log_directory: str
            archived_log_directory: str
            def __init__(self, online_log_directory: _Optional[str] = ..., archived_log_directory: _Optional[str] = ...) -> None: ...
        ORACLE_ASM_LOG_FILE_ACCESS_FIELD_NUMBER: _ClassVar[int]
        LOG_FILE_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
        oracle_asm_log_file_access: OracleSourceConfig.BinaryLogParser.OracleAsmLogFileAccess
        log_file_directories: OracleSourceConfig.BinaryLogParser.LogFileDirectories
        def __init__(self, oracle_asm_log_file_access: _Optional[_Union[OracleSourceConfig.BinaryLogParser.OracleAsmLogFileAccess, _Mapping]] = ..., log_file_directories: _Optional[_Union[OracleSourceConfig.BinaryLogParser.LogFileDirectories, _Mapping]] = ...) -> None: ...
    INCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_CDC_TASKS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_BACKFILL_TASKS_FIELD_NUMBER: _ClassVar[int]
    DROP_LARGE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    STREAM_LARGE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    LOG_MINER_FIELD_NUMBER: _ClassVar[int]
    BINARY_LOG_PARSER_FIELD_NUMBER: _ClassVar[int]
    include_objects: OracleRdbms
    exclude_objects: OracleRdbms
    max_concurrent_cdc_tasks: int
    max_concurrent_backfill_tasks: int
    drop_large_objects: OracleSourceConfig.DropLargeObjects
    stream_large_objects: OracleSourceConfig.StreamLargeObjects
    log_miner: OracleSourceConfig.LogMiner
    binary_log_parser: OracleSourceConfig.BinaryLogParser
    def __init__(self, include_objects: _Optional[_Union[OracleRdbms, _Mapping]] = ..., exclude_objects: _Optional[_Union[OracleRdbms, _Mapping]] = ..., max_concurrent_cdc_tasks: _Optional[int] = ..., max_concurrent_backfill_tasks: _Optional[int] = ..., drop_large_objects: _Optional[_Union[OracleSourceConfig.DropLargeObjects, _Mapping]] = ..., stream_large_objects: _Optional[_Union[OracleSourceConfig.StreamLargeObjects, _Mapping]] = ..., log_miner: _Optional[_Union[OracleSourceConfig.LogMiner, _Mapping]] = ..., binary_log_parser: _Optional[_Union[OracleSourceConfig.BinaryLogParser, _Mapping]] = ...) -> None: ...

class PostgresqlColumn(_message.Message):
    __slots__ = ("column", "data_type", "length", "precision", "scale", "primary_key", "nullable", "ordinal_position")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    column: str
    data_type: str
    length: int
    precision: int
    scale: int
    primary_key: bool
    nullable: bool
    ordinal_position: int
    def __init__(self, column: _Optional[str] = ..., data_type: _Optional[str] = ..., length: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ..., primary_key: bool = ..., nullable: bool = ..., ordinal_position: _Optional[int] = ...) -> None: ...

class PostgresqlTable(_message.Message):
    __slots__ = ("table", "postgresql_columns")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    table: str
    postgresql_columns: _containers.RepeatedCompositeFieldContainer[PostgresqlColumn]
    def __init__(self, table: _Optional[str] = ..., postgresql_columns: _Optional[_Iterable[_Union[PostgresqlColumn, _Mapping]]] = ...) -> None: ...

class PostgresqlSchema(_message.Message):
    __slots__ = ("schema", "postgresql_tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    postgresql_tables: _containers.RepeatedCompositeFieldContainer[PostgresqlTable]
    def __init__(self, schema: _Optional[str] = ..., postgresql_tables: _Optional[_Iterable[_Union[PostgresqlTable, _Mapping]]] = ...) -> None: ...

class PostgresqlRdbms(_message.Message):
    __slots__ = ("postgresql_schemas",)
    POSTGRESQL_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    postgresql_schemas: _containers.RepeatedCompositeFieldContainer[PostgresqlSchema]
    def __init__(self, postgresql_schemas: _Optional[_Iterable[_Union[PostgresqlSchema, _Mapping]]] = ...) -> None: ...

class PostgresqlSourceConfig(_message.Message):
    __slots__ = ("include_objects", "exclude_objects", "replication_slot", "publication", "max_concurrent_backfill_tasks")
    INCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_SLOT_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_BACKFILL_TASKS_FIELD_NUMBER: _ClassVar[int]
    include_objects: PostgresqlRdbms
    exclude_objects: PostgresqlRdbms
    replication_slot: str
    publication: str
    max_concurrent_backfill_tasks: int
    def __init__(self, include_objects: _Optional[_Union[PostgresqlRdbms, _Mapping]] = ..., exclude_objects: _Optional[_Union[PostgresqlRdbms, _Mapping]] = ..., replication_slot: _Optional[str] = ..., publication: _Optional[str] = ..., max_concurrent_backfill_tasks: _Optional[int] = ...) -> None: ...

class SqlServerColumn(_message.Message):
    __slots__ = ("column", "data_type", "length", "precision", "scale", "primary_key", "nullable", "ordinal_position")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    column: str
    data_type: str
    length: int
    precision: int
    scale: int
    primary_key: bool
    nullable: bool
    ordinal_position: int
    def __init__(self, column: _Optional[str] = ..., data_type: _Optional[str] = ..., length: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ..., primary_key: bool = ..., nullable: bool = ..., ordinal_position: _Optional[int] = ...) -> None: ...

class SqlServerTable(_message.Message):
    __slots__ = ("table", "columns")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    table: str
    columns: _containers.RepeatedCompositeFieldContainer[SqlServerColumn]
    def __init__(self, table: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[SqlServerColumn, _Mapping]]] = ...) -> None: ...

class SqlServerSchema(_message.Message):
    __slots__ = ("schema", "tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    tables: _containers.RepeatedCompositeFieldContainer[SqlServerTable]
    def __init__(self, schema: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[SqlServerTable, _Mapping]]] = ...) -> None: ...

class SqlServerRdbms(_message.Message):
    __slots__ = ("schemas",)
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[SqlServerSchema]
    def __init__(self, schemas: _Optional[_Iterable[_Union[SqlServerSchema, _Mapping]]] = ...) -> None: ...

class SqlServerSourceConfig(_message.Message):
    __slots__ = ("include_objects", "exclude_objects", "max_concurrent_cdc_tasks", "max_concurrent_backfill_tasks", "transaction_logs", "change_tables")
    INCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_CDC_TASKS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_BACKFILL_TASKS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_LOGS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TABLES_FIELD_NUMBER: _ClassVar[int]
    include_objects: SqlServerRdbms
    exclude_objects: SqlServerRdbms
    max_concurrent_cdc_tasks: int
    max_concurrent_backfill_tasks: int
    transaction_logs: SqlServerTransactionLogs
    change_tables: SqlServerChangeTables
    def __init__(self, include_objects: _Optional[_Union[SqlServerRdbms, _Mapping]] = ..., exclude_objects: _Optional[_Union[SqlServerRdbms, _Mapping]] = ..., max_concurrent_cdc_tasks: _Optional[int] = ..., max_concurrent_backfill_tasks: _Optional[int] = ..., transaction_logs: _Optional[_Union[SqlServerTransactionLogs, _Mapping]] = ..., change_tables: _Optional[_Union[SqlServerChangeTables, _Mapping]] = ...) -> None: ...

class SqlServerTransactionLogs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SqlServerChangeTables(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MysqlColumn(_message.Message):
    __slots__ = ("column", "data_type", "length", "collation", "primary_key", "nullable", "ordinal_position", "precision", "scale")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    column: str
    data_type: str
    length: int
    collation: str
    primary_key: bool
    nullable: bool
    ordinal_position: int
    precision: int
    scale: int
    def __init__(self, column: _Optional[str] = ..., data_type: _Optional[str] = ..., length: _Optional[int] = ..., collation: _Optional[str] = ..., primary_key: bool = ..., nullable: bool = ..., ordinal_position: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ...) -> None: ...

class MysqlTable(_message.Message):
    __slots__ = ("table", "mysql_columns")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    MYSQL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    table: str
    mysql_columns: _containers.RepeatedCompositeFieldContainer[MysqlColumn]
    def __init__(self, table: _Optional[str] = ..., mysql_columns: _Optional[_Iterable[_Union[MysqlColumn, _Mapping]]] = ...) -> None: ...

class MysqlDatabase(_message.Message):
    __slots__ = ("database", "mysql_tables")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    MYSQL_TABLES_FIELD_NUMBER: _ClassVar[int]
    database: str
    mysql_tables: _containers.RepeatedCompositeFieldContainer[MysqlTable]
    def __init__(self, database: _Optional[str] = ..., mysql_tables: _Optional[_Iterable[_Union[MysqlTable, _Mapping]]] = ...) -> None: ...

class MysqlRdbms(_message.Message):
    __slots__ = ("mysql_databases",)
    MYSQL_DATABASES_FIELD_NUMBER: _ClassVar[int]
    mysql_databases: _containers.RepeatedCompositeFieldContainer[MysqlDatabase]
    def __init__(self, mysql_databases: _Optional[_Iterable[_Union[MysqlDatabase, _Mapping]]] = ...) -> None: ...

class MysqlSourceConfig(_message.Message):
    __slots__ = ("include_objects", "exclude_objects", "max_concurrent_cdc_tasks", "max_concurrent_backfill_tasks", "binary_log_position", "gtid")
    class BinaryLogPosition(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Gtid(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    INCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_CDC_TASKS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_BACKFILL_TASKS_FIELD_NUMBER: _ClassVar[int]
    BINARY_LOG_POSITION_FIELD_NUMBER: _ClassVar[int]
    GTID_FIELD_NUMBER: _ClassVar[int]
    include_objects: MysqlRdbms
    exclude_objects: MysqlRdbms
    max_concurrent_cdc_tasks: int
    max_concurrent_backfill_tasks: int
    binary_log_position: MysqlSourceConfig.BinaryLogPosition
    gtid: MysqlSourceConfig.Gtid
    def __init__(self, include_objects: _Optional[_Union[MysqlRdbms, _Mapping]] = ..., exclude_objects: _Optional[_Union[MysqlRdbms, _Mapping]] = ..., max_concurrent_cdc_tasks: _Optional[int] = ..., max_concurrent_backfill_tasks: _Optional[int] = ..., binary_log_position: _Optional[_Union[MysqlSourceConfig.BinaryLogPosition, _Mapping]] = ..., gtid: _Optional[_Union[MysqlSourceConfig.Gtid, _Mapping]] = ...) -> None: ...

class SourceConfig(_message.Message):
    __slots__ = ("source_connection_profile", "oracle_source_config", "mysql_source_config", "postgresql_source_config", "sql_server_source_config")
    SOURCE_CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MYSQL_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    source_connection_profile: str
    oracle_source_config: OracleSourceConfig
    mysql_source_config: MysqlSourceConfig
    postgresql_source_config: PostgresqlSourceConfig
    sql_server_source_config: SqlServerSourceConfig
    def __init__(self, source_connection_profile: _Optional[str] = ..., oracle_source_config: _Optional[_Union[OracleSourceConfig, _Mapping]] = ..., mysql_source_config: _Optional[_Union[MysqlSourceConfig, _Mapping]] = ..., postgresql_source_config: _Optional[_Union[PostgresqlSourceConfig, _Mapping]] = ..., sql_server_source_config: _Optional[_Union[SqlServerSourceConfig, _Mapping]] = ...) -> None: ...

class AvroFileFormat(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JsonFileFormat(_message.Message):
    __slots__ = ("schema_file_format", "compression")
    class SchemaFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEMA_FILE_FORMAT_UNSPECIFIED: _ClassVar[JsonFileFormat.SchemaFileFormat]
        NO_SCHEMA_FILE: _ClassVar[JsonFileFormat.SchemaFileFormat]
        AVRO_SCHEMA_FILE: _ClassVar[JsonFileFormat.SchemaFileFormat]
    SCHEMA_FILE_FORMAT_UNSPECIFIED: JsonFileFormat.SchemaFileFormat
    NO_SCHEMA_FILE: JsonFileFormat.SchemaFileFormat
    AVRO_SCHEMA_FILE: JsonFileFormat.SchemaFileFormat
    class JsonCompression(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JSON_COMPRESSION_UNSPECIFIED: _ClassVar[JsonFileFormat.JsonCompression]
        NO_COMPRESSION: _ClassVar[JsonFileFormat.JsonCompression]
        GZIP: _ClassVar[JsonFileFormat.JsonCompression]
    JSON_COMPRESSION_UNSPECIFIED: JsonFileFormat.JsonCompression
    NO_COMPRESSION: JsonFileFormat.JsonCompression
    GZIP: JsonFileFormat.JsonCompression
    SCHEMA_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    schema_file_format: JsonFileFormat.SchemaFileFormat
    compression: JsonFileFormat.JsonCompression
    def __init__(self, schema_file_format: _Optional[_Union[JsonFileFormat.SchemaFileFormat, str]] = ..., compression: _Optional[_Union[JsonFileFormat.JsonCompression, str]] = ...) -> None: ...

class GcsDestinationConfig(_message.Message):
    __slots__ = ("path", "file_rotation_mb", "file_rotation_interval", "avro_file_format", "json_file_format")
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_ROTATION_MB_FIELD_NUMBER: _ClassVar[int]
    FILE_ROTATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AVRO_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    JSON_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    path: str
    file_rotation_mb: int
    file_rotation_interval: _duration_pb2.Duration
    avro_file_format: AvroFileFormat
    json_file_format: JsonFileFormat
    def __init__(self, path: _Optional[str] = ..., file_rotation_mb: _Optional[int] = ..., file_rotation_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., avro_file_format: _Optional[_Union[AvroFileFormat, _Mapping]] = ..., json_file_format: _Optional[_Union[JsonFileFormat, _Mapping]] = ...) -> None: ...

class BigQueryDestinationConfig(_message.Message):
    __slots__ = ("single_target_dataset", "source_hierarchy_datasets", "data_freshness", "merge", "append_only")
    class SingleTargetDataset(_message.Message):
        __slots__ = ("dataset_id",)
        DATASET_ID_FIELD_NUMBER: _ClassVar[int]
        dataset_id: str
        def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...
    class SourceHierarchyDatasets(_message.Message):
        __slots__ = ("dataset_template",)
        class DatasetTemplate(_message.Message):
            __slots__ = ("location", "dataset_id_prefix", "kms_key_name")
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            DATASET_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
            KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
            location: str
            dataset_id_prefix: str
            kms_key_name: str
            def __init__(self, location: _Optional[str] = ..., dataset_id_prefix: _Optional[str] = ..., kms_key_name: _Optional[str] = ...) -> None: ...
        DATASET_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        dataset_template: BigQueryDestinationConfig.SourceHierarchyDatasets.DatasetTemplate
        def __init__(self, dataset_template: _Optional[_Union[BigQueryDestinationConfig.SourceHierarchyDatasets.DatasetTemplate, _Mapping]] = ...) -> None: ...
    class AppendOnly(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Merge(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SINGLE_TARGET_DATASET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HIERARCHY_DATASETS_FIELD_NUMBER: _ClassVar[int]
    DATA_FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    MERGE_FIELD_NUMBER: _ClassVar[int]
    APPEND_ONLY_FIELD_NUMBER: _ClassVar[int]
    single_target_dataset: BigQueryDestinationConfig.SingleTargetDataset
    source_hierarchy_datasets: BigQueryDestinationConfig.SourceHierarchyDatasets
    data_freshness: _duration_pb2.Duration
    merge: BigQueryDestinationConfig.Merge
    append_only: BigQueryDestinationConfig.AppendOnly
    def __init__(self, single_target_dataset: _Optional[_Union[BigQueryDestinationConfig.SingleTargetDataset, _Mapping]] = ..., source_hierarchy_datasets: _Optional[_Union[BigQueryDestinationConfig.SourceHierarchyDatasets, _Mapping]] = ..., data_freshness: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., merge: _Optional[_Union[BigQueryDestinationConfig.Merge, _Mapping]] = ..., append_only: _Optional[_Union[BigQueryDestinationConfig.AppendOnly, _Mapping]] = ...) -> None: ...

class DestinationConfig(_message.Message):
    __slots__ = ("destination_connection_profile", "gcs_destination_config", "bigquery_destination_config")
    DESTINATION_CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    GCS_DESTINATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    destination_connection_profile: str
    gcs_destination_config: GcsDestinationConfig
    bigquery_destination_config: BigQueryDestinationConfig
    def __init__(self, destination_connection_profile: _Optional[str] = ..., gcs_destination_config: _Optional[_Union[GcsDestinationConfig, _Mapping]] = ..., bigquery_destination_config: _Optional[_Union[BigQueryDestinationConfig, _Mapping]] = ...) -> None: ...

class Stream(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "source_config", "destination_config", "state", "backfill_all", "backfill_none", "errors", "customer_managed_encryption_key", "last_recovery_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Stream.State]
        NOT_STARTED: _ClassVar[Stream.State]
        RUNNING: _ClassVar[Stream.State]
        PAUSED: _ClassVar[Stream.State]
        MAINTENANCE: _ClassVar[Stream.State]
        FAILED: _ClassVar[Stream.State]
        FAILED_PERMANENTLY: _ClassVar[Stream.State]
        STARTING: _ClassVar[Stream.State]
        DRAINING: _ClassVar[Stream.State]
    STATE_UNSPECIFIED: Stream.State
    NOT_STARTED: Stream.State
    RUNNING: Stream.State
    PAUSED: Stream.State
    MAINTENANCE: Stream.State
    FAILED: Stream.State
    FAILED_PERMANENTLY: Stream.State
    STARTING: Stream.State
    DRAINING: Stream.State
    class BackfillAllStrategy(_message.Message):
        __slots__ = ("oracle_excluded_objects", "mysql_excluded_objects", "postgresql_excluded_objects", "sql_server_excluded_objects")
        ORACLE_EXCLUDED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        MYSQL_EXCLUDED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        POSTGRESQL_EXCLUDED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        SQL_SERVER_EXCLUDED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        oracle_excluded_objects: OracleRdbms
        mysql_excluded_objects: MysqlRdbms
        postgresql_excluded_objects: PostgresqlRdbms
        sql_server_excluded_objects: SqlServerRdbms
        def __init__(self, oracle_excluded_objects: _Optional[_Union[OracleRdbms, _Mapping]] = ..., mysql_excluded_objects: _Optional[_Union[MysqlRdbms, _Mapping]] = ..., postgresql_excluded_objects: _Optional[_Union[PostgresqlRdbms, _Mapping]] = ..., sql_server_excluded_objects: _Optional[_Union[SqlServerRdbms, _Mapping]] = ...) -> None: ...
    class BackfillNoneStrategy(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_ALL_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_NONE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MANAGED_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_RECOVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    source_config: SourceConfig
    destination_config: DestinationConfig
    state: Stream.State
    backfill_all: Stream.BackfillAllStrategy
    backfill_none: Stream.BackfillNoneStrategy
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    customer_managed_encryption_key: str
    last_recovery_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., source_config: _Optional[_Union[SourceConfig, _Mapping]] = ..., destination_config: _Optional[_Union[DestinationConfig, _Mapping]] = ..., state: _Optional[_Union[Stream.State, str]] = ..., backfill_all: _Optional[_Union[Stream.BackfillAllStrategy, _Mapping]] = ..., backfill_none: _Optional[_Union[Stream.BackfillNoneStrategy, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ..., customer_managed_encryption_key: _Optional[str] = ..., last_recovery_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamObject(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "display_name", "errors", "backfill_job", "source_object")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_JOB_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    backfill_job: BackfillJob
    source_object: SourceObjectIdentifier
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_name: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ..., backfill_job: _Optional[_Union[BackfillJob, _Mapping]] = ..., source_object: _Optional[_Union[SourceObjectIdentifier, _Mapping]] = ...) -> None: ...

class SourceObjectIdentifier(_message.Message):
    __slots__ = ("oracle_identifier", "mysql_identifier", "postgresql_identifier", "sql_server_identifier")
    class OracleObjectIdentifier(_message.Message):
        __slots__ = ("schema", "table")
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        schema: str
        table: str
        def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...
    class PostgresqlObjectIdentifier(_message.Message):
        __slots__ = ("schema", "table")
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        schema: str
        table: str
        def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...
    class MysqlObjectIdentifier(_message.Message):
        __slots__ = ("database", "table")
        DATABASE_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        database: str
        table: str
        def __init__(self, database: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...
    class SqlServerObjectIdentifier(_message.Message):
        __slots__ = ("schema", "table")
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        schema: str
        table: str
        def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...
    ORACLE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MYSQL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    oracle_identifier: SourceObjectIdentifier.OracleObjectIdentifier
    mysql_identifier: SourceObjectIdentifier.MysqlObjectIdentifier
    postgresql_identifier: SourceObjectIdentifier.PostgresqlObjectIdentifier
    sql_server_identifier: SourceObjectIdentifier.SqlServerObjectIdentifier
    def __init__(self, oracle_identifier: _Optional[_Union[SourceObjectIdentifier.OracleObjectIdentifier, _Mapping]] = ..., mysql_identifier: _Optional[_Union[SourceObjectIdentifier.MysqlObjectIdentifier, _Mapping]] = ..., postgresql_identifier: _Optional[_Union[SourceObjectIdentifier.PostgresqlObjectIdentifier, _Mapping]] = ..., sql_server_identifier: _Optional[_Union[SourceObjectIdentifier.SqlServerObjectIdentifier, _Mapping]] = ...) -> None: ...

class BackfillJob(_message.Message):
    __slots__ = ("state", "trigger", "last_start_time", "last_end_time", "errors")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BackfillJob.State]
        NOT_STARTED: _ClassVar[BackfillJob.State]
        PENDING: _ClassVar[BackfillJob.State]
        ACTIVE: _ClassVar[BackfillJob.State]
        STOPPED: _ClassVar[BackfillJob.State]
        FAILED: _ClassVar[BackfillJob.State]
        COMPLETED: _ClassVar[BackfillJob.State]
        UNSUPPORTED: _ClassVar[BackfillJob.State]
    STATE_UNSPECIFIED: BackfillJob.State
    NOT_STARTED: BackfillJob.State
    PENDING: BackfillJob.State
    ACTIVE: BackfillJob.State
    STOPPED: BackfillJob.State
    FAILED: BackfillJob.State
    COMPLETED: BackfillJob.State
    UNSUPPORTED: BackfillJob.State
    class Trigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_UNSPECIFIED: _ClassVar[BackfillJob.Trigger]
        AUTOMATIC: _ClassVar[BackfillJob.Trigger]
        MANUAL: _ClassVar[BackfillJob.Trigger]
    TRIGGER_UNSPECIFIED: BackfillJob.Trigger
    AUTOMATIC: BackfillJob.Trigger
    MANUAL: BackfillJob.Trigger
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    LAST_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    state: BackfillJob.State
    trigger: BackfillJob.Trigger
    last_start_time: _timestamp_pb2.Timestamp
    last_end_time: _timestamp_pb2.Timestamp
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, state: _Optional[_Union[BackfillJob.State, str]] = ..., trigger: _Optional[_Union[BackfillJob.Trigger, str]] = ..., last_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("reason", "error_uuid", "message", "error_time", "details")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_UUID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_TIME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    reason: str
    error_uuid: str
    message: str
    error_time: _timestamp_pb2.Timestamp
    details: _containers.ScalarMap[str, str]
    def __init__(self, reason: _Optional[str] = ..., error_uuid: _Optional[str] = ..., message: _Optional[str] = ..., error_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ValidationResult(_message.Message):
    __slots__ = ("validations",)
    VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    validations: _containers.RepeatedCompositeFieldContainer[Validation]
    def __init__(self, validations: _Optional[_Iterable[_Union[Validation, _Mapping]]] = ...) -> None: ...

class Validation(_message.Message):
    __slots__ = ("description", "state", "message", "code")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Validation.State]
        NOT_EXECUTED: _ClassVar[Validation.State]
        FAILED: _ClassVar[Validation.State]
        PASSED: _ClassVar[Validation.State]
        WARNING: _ClassVar[Validation.State]
    STATE_UNSPECIFIED: Validation.State
    NOT_EXECUTED: Validation.State
    FAILED: Validation.State
    PASSED: Validation.State
    WARNING: Validation.State
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    description: str
    state: Validation.State
    message: _containers.RepeatedCompositeFieldContainer[ValidationMessage]
    code: str
    def __init__(self, description: _Optional[str] = ..., state: _Optional[_Union[Validation.State, str]] = ..., message: _Optional[_Iterable[_Union[ValidationMessage, _Mapping]]] = ..., code: _Optional[str] = ...) -> None: ...

class ValidationMessage(_message.Message):
    __slots__ = ("message", "level", "metadata", "code")
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEVEL_UNSPECIFIED: _ClassVar[ValidationMessage.Level]
        WARNING: _ClassVar[ValidationMessage.Level]
        ERROR: _ClassVar[ValidationMessage.Level]
    LEVEL_UNSPECIFIED: ValidationMessage.Level
    WARNING: ValidationMessage.Level
    ERROR: ValidationMessage.Level
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    level: ValidationMessage.Level
    metadata: _containers.ScalarMap[str, str]
    code: str
    def __init__(self, message: _Optional[str] = ..., level: _Optional[_Union[ValidationMessage.Level, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., code: _Optional[str] = ...) -> None: ...

class CdcStrategy(_message.Message):
    __slots__ = ("most_recent_start_position", "next_available_start_position", "specific_start_position")
    class MostRecentStartPosition(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class NextAvailableStartPosition(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SpecificStartPosition(_message.Message):
        __slots__ = ("mysql_log_position", "oracle_scn_position", "sql_server_lsn_position")
        MYSQL_LOG_POSITION_FIELD_NUMBER: _ClassVar[int]
        ORACLE_SCN_POSITION_FIELD_NUMBER: _ClassVar[int]
        SQL_SERVER_LSN_POSITION_FIELD_NUMBER: _ClassVar[int]
        mysql_log_position: MysqlLogPosition
        oracle_scn_position: OracleScnPosition
        sql_server_lsn_position: SqlServerLsnPosition
        def __init__(self, mysql_log_position: _Optional[_Union[MysqlLogPosition, _Mapping]] = ..., oracle_scn_position: _Optional[_Union[OracleScnPosition, _Mapping]] = ..., sql_server_lsn_position: _Optional[_Union[SqlServerLsnPosition, _Mapping]] = ...) -> None: ...
    MOST_RECENT_START_POSITION_FIELD_NUMBER: _ClassVar[int]
    NEXT_AVAILABLE_START_POSITION_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_START_POSITION_FIELD_NUMBER: _ClassVar[int]
    most_recent_start_position: CdcStrategy.MostRecentStartPosition
    next_available_start_position: CdcStrategy.NextAvailableStartPosition
    specific_start_position: CdcStrategy.SpecificStartPosition
    def __init__(self, most_recent_start_position: _Optional[_Union[CdcStrategy.MostRecentStartPosition, _Mapping]] = ..., next_available_start_position: _Optional[_Union[CdcStrategy.NextAvailableStartPosition, _Mapping]] = ..., specific_start_position: _Optional[_Union[CdcStrategy.SpecificStartPosition, _Mapping]] = ...) -> None: ...

class SqlServerLsnPosition(_message.Message):
    __slots__ = ("lsn",)
    LSN_FIELD_NUMBER: _ClassVar[int]
    lsn: str
    def __init__(self, lsn: _Optional[str] = ...) -> None: ...

class OracleScnPosition(_message.Message):
    __slots__ = ("scn",)
    SCN_FIELD_NUMBER: _ClassVar[int]
    scn: int
    def __init__(self, scn: _Optional[int] = ...) -> None: ...

class MysqlLogPosition(_message.Message):
    __slots__ = ("log_file", "log_position")
    LOG_FILE_FIELD_NUMBER: _ClassVar[int]
    LOG_POSITION_FIELD_NUMBER: _ClassVar[int]
    log_file: str
    log_position: int
    def __init__(self, log_file: _Optional[str] = ..., log_position: _Optional[int] = ...) -> None: ...
