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

class GcsFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GCS_FILE_FORMAT_UNSPECIFIED: _ClassVar[GcsFileFormat]
    AVRO: _ClassVar[GcsFileFormat]

class SchemaFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEMA_FILE_FORMAT_UNSPECIFIED: _ClassVar[SchemaFileFormat]
    NO_SCHEMA_FILE: _ClassVar[SchemaFileFormat]
    AVRO_SCHEMA_FILE: _ClassVar[SchemaFileFormat]
GCS_FILE_FORMAT_UNSPECIFIED: GcsFileFormat
AVRO: GcsFileFormat
SCHEMA_FILE_FORMAT_UNSPECIFIED: SchemaFileFormat
NO_SCHEMA_FILE: SchemaFileFormat
AVRO_SCHEMA_FILE: SchemaFileFormat

class OracleProfile(_message.Message):
    __slots__ = ('hostname', 'port', 'username', 'password', 'database_service', 'connection_attributes')

    class ConnectionAttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    port: int
    username: str
    password: str
    database_service: str
    connection_attributes: _containers.ScalarMap[str, str]

    def __init__(self, hostname: _Optional[str]=..., port: _Optional[int]=..., username: _Optional[str]=..., password: _Optional[str]=..., database_service: _Optional[str]=..., connection_attributes: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class MysqlProfile(_message.Message):
    __slots__ = ('hostname', 'port', 'username', 'password', 'ssl_config')
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

    def __init__(self, hostname: _Optional[str]=..., port: _Optional[int]=..., username: _Optional[str]=..., password: _Optional[str]=..., ssl_config: _Optional[_Union[MysqlSslConfig, _Mapping]]=...) -> None:
        ...

class GcsProfile(_message.Message):
    __slots__ = ('bucket_name', 'root_path')
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    root_path: str

    def __init__(self, bucket_name: _Optional[str]=..., root_path: _Optional[str]=...) -> None:
        ...

class NoConnectivitySettings(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StaticServiceIpConnectivity(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ForwardSshTunnelConnectivity(_message.Message):
    __slots__ = ('hostname', 'username', 'port', 'password', 'private_key')
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

    def __init__(self, hostname: _Optional[str]=..., username: _Optional[str]=..., port: _Optional[int]=..., password: _Optional[str]=..., private_key: _Optional[str]=...) -> None:
        ...

class VpcPeeringConfig(_message.Message):
    __slots__ = ('vpc_name', 'subnet')
    VPC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    vpc_name: str
    subnet: str

    def __init__(self, vpc_name: _Optional[str]=..., subnet: _Optional[str]=...) -> None:
        ...

class PrivateConnection(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'state', 'error', 'vpc_peering_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PrivateConnection.State]
        CREATING: _ClassVar[PrivateConnection.State]
        CREATED: _ClassVar[PrivateConnection.State]
        FAILED: _ClassVar[PrivateConnection.State]
    STATE_UNSPECIFIED: PrivateConnection.State
    CREATING: PrivateConnection.State
    CREATED: PrivateConnection.State
    FAILED: PrivateConnection.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
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

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., state: _Optional[_Union[PrivateConnection.State, str]]=..., error: _Optional[_Union[Error, _Mapping]]=..., vpc_peering_config: _Optional[_Union[VpcPeeringConfig, _Mapping]]=...) -> None:
        ...

class PrivateConnectivity(_message.Message):
    __slots__ = ('private_connection_name',)
    PRIVATE_CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    private_connection_name: str

    def __init__(self, private_connection_name: _Optional[str]=...) -> None:
        ...

class Route(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'destination_address', 'destination_port')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
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

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., destination_address: _Optional[str]=..., destination_port: _Optional[int]=...) -> None:
        ...

class MysqlSslConfig(_message.Message):
    __slots__ = ('client_key', 'client_key_set', 'client_certificate', 'client_certificate_set', 'ca_certificate', 'ca_certificate_set')
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

    def __init__(self, client_key: _Optional[str]=..., client_key_set: bool=..., client_certificate: _Optional[str]=..., client_certificate_set: bool=..., ca_certificate: _Optional[str]=..., ca_certificate_set: bool=...) -> None:
        ...

class ConnectionProfile(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'oracle_profile', 'gcs_profile', 'mysql_profile', 'no_connectivity', 'static_service_ip_connectivity', 'forward_ssh_connectivity', 'private_connectivity')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    GCS_PROFILE_FIELD_NUMBER: _ClassVar[int]
    MYSQL_PROFILE_FIELD_NUMBER: _ClassVar[int]
    NO_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
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
    no_connectivity: NoConnectivitySettings
    static_service_ip_connectivity: StaticServiceIpConnectivity
    forward_ssh_connectivity: ForwardSshTunnelConnectivity
    private_connectivity: PrivateConnectivity

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., oracle_profile: _Optional[_Union[OracleProfile, _Mapping]]=..., gcs_profile: _Optional[_Union[GcsProfile, _Mapping]]=..., mysql_profile: _Optional[_Union[MysqlProfile, _Mapping]]=..., no_connectivity: _Optional[_Union[NoConnectivitySettings, _Mapping]]=..., static_service_ip_connectivity: _Optional[_Union[StaticServiceIpConnectivity, _Mapping]]=..., forward_ssh_connectivity: _Optional[_Union[ForwardSshTunnelConnectivity, _Mapping]]=..., private_connectivity: _Optional[_Union[PrivateConnectivity, _Mapping]]=...) -> None:
        ...

class OracleColumn(_message.Message):
    __slots__ = ('column_name', 'data_type', 'length', 'precision', 'scale', 'encoding', 'primary_key', 'nullable', 'ordinal_position')
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    data_type: str
    length: int
    precision: int
    scale: int
    encoding: str
    primary_key: bool
    nullable: bool
    ordinal_position: int

    def __init__(self, column_name: _Optional[str]=..., data_type: _Optional[str]=..., length: _Optional[int]=..., precision: _Optional[int]=..., scale: _Optional[int]=..., encoding: _Optional[str]=..., primary_key: bool=..., nullable: bool=..., ordinal_position: _Optional[int]=...) -> None:
        ...

class OracleTable(_message.Message):
    __slots__ = ('table_name', 'oracle_columns')
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    oracle_columns: _containers.RepeatedCompositeFieldContainer[OracleColumn]

    def __init__(self, table_name: _Optional[str]=..., oracle_columns: _Optional[_Iterable[_Union[OracleColumn, _Mapping]]]=...) -> None:
        ...

class OracleSchema(_message.Message):
    __slots__ = ('schema_name', 'oracle_tables')
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_TABLES_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    oracle_tables: _containers.RepeatedCompositeFieldContainer[OracleTable]

    def __init__(self, schema_name: _Optional[str]=..., oracle_tables: _Optional[_Iterable[_Union[OracleTable, _Mapping]]]=...) -> None:
        ...

class OracleRdbms(_message.Message):
    __slots__ = ('oracle_schemas',)
    ORACLE_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    oracle_schemas: _containers.RepeatedCompositeFieldContainer[OracleSchema]

    def __init__(self, oracle_schemas: _Optional[_Iterable[_Union[OracleSchema, _Mapping]]]=...) -> None:
        ...

class OracleSourceConfig(_message.Message):
    __slots__ = ('allowlist', 'rejectlist')
    ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    REJECTLIST_FIELD_NUMBER: _ClassVar[int]
    allowlist: OracleRdbms
    rejectlist: OracleRdbms

    def __init__(self, allowlist: _Optional[_Union[OracleRdbms, _Mapping]]=..., rejectlist: _Optional[_Union[OracleRdbms, _Mapping]]=...) -> None:
        ...

class MysqlColumn(_message.Message):
    __slots__ = ('column_name', 'data_type', 'length', 'collation', 'primary_key', 'nullable', 'ordinal_position')
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    data_type: str
    length: int
    collation: str
    primary_key: bool
    nullable: bool
    ordinal_position: int

    def __init__(self, column_name: _Optional[str]=..., data_type: _Optional[str]=..., length: _Optional[int]=..., collation: _Optional[str]=..., primary_key: bool=..., nullable: bool=..., ordinal_position: _Optional[int]=...) -> None:
        ...

class MysqlTable(_message.Message):
    __slots__ = ('table_name', 'mysql_columns')
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    MYSQL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    mysql_columns: _containers.RepeatedCompositeFieldContainer[MysqlColumn]

    def __init__(self, table_name: _Optional[str]=..., mysql_columns: _Optional[_Iterable[_Union[MysqlColumn, _Mapping]]]=...) -> None:
        ...

class MysqlDatabase(_message.Message):
    __slots__ = ('database_name', 'mysql_tables')
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    MYSQL_TABLES_FIELD_NUMBER: _ClassVar[int]
    database_name: str
    mysql_tables: _containers.RepeatedCompositeFieldContainer[MysqlTable]

    def __init__(self, database_name: _Optional[str]=..., mysql_tables: _Optional[_Iterable[_Union[MysqlTable, _Mapping]]]=...) -> None:
        ...

class MysqlRdbms(_message.Message):
    __slots__ = ('mysql_databases',)
    MYSQL_DATABASES_FIELD_NUMBER: _ClassVar[int]
    mysql_databases: _containers.RepeatedCompositeFieldContainer[MysqlDatabase]

    def __init__(self, mysql_databases: _Optional[_Iterable[_Union[MysqlDatabase, _Mapping]]]=...) -> None:
        ...

class MysqlSourceConfig(_message.Message):
    __slots__ = ('allowlist', 'rejectlist')
    ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    REJECTLIST_FIELD_NUMBER: _ClassVar[int]
    allowlist: MysqlRdbms
    rejectlist: MysqlRdbms

    def __init__(self, allowlist: _Optional[_Union[MysqlRdbms, _Mapping]]=..., rejectlist: _Optional[_Union[MysqlRdbms, _Mapping]]=...) -> None:
        ...

class SourceConfig(_message.Message):
    __slots__ = ('source_connection_profile_name', 'oracle_source_config', 'mysql_source_config')
    SOURCE_CONNECTION_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MYSQL_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    source_connection_profile_name: str
    oracle_source_config: OracleSourceConfig
    mysql_source_config: MysqlSourceConfig

    def __init__(self, source_connection_profile_name: _Optional[str]=..., oracle_source_config: _Optional[_Union[OracleSourceConfig, _Mapping]]=..., mysql_source_config: _Optional[_Union[MysqlSourceConfig, _Mapping]]=...) -> None:
        ...

class AvroFileFormat(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class JsonFileFormat(_message.Message):
    __slots__ = ('schema_file_format', 'compression')

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
    schema_file_format: SchemaFileFormat
    compression: JsonFileFormat.JsonCompression

    def __init__(self, schema_file_format: _Optional[_Union[SchemaFileFormat, str]]=..., compression: _Optional[_Union[JsonFileFormat.JsonCompression, str]]=...) -> None:
        ...

class GcsDestinationConfig(_message.Message):
    __slots__ = ('path', 'gcs_file_format', 'file_rotation_mb', 'file_rotation_interval', 'avro_file_format', 'json_file_format')
    PATH_FIELD_NUMBER: _ClassVar[int]
    GCS_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILE_ROTATION_MB_FIELD_NUMBER: _ClassVar[int]
    FILE_ROTATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AVRO_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    JSON_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    path: str
    gcs_file_format: GcsFileFormat
    file_rotation_mb: int
    file_rotation_interval: _duration_pb2.Duration
    avro_file_format: AvroFileFormat
    json_file_format: JsonFileFormat

    def __init__(self, path: _Optional[str]=..., gcs_file_format: _Optional[_Union[GcsFileFormat, str]]=..., file_rotation_mb: _Optional[int]=..., file_rotation_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., avro_file_format: _Optional[_Union[AvroFileFormat, _Mapping]]=..., json_file_format: _Optional[_Union[JsonFileFormat, _Mapping]]=...) -> None:
        ...

class DestinationConfig(_message.Message):
    __slots__ = ('destination_connection_profile_name', 'gcs_destination_config')
    DESTINATION_CONNECTION_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    GCS_DESTINATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    destination_connection_profile_name: str
    gcs_destination_config: GcsDestinationConfig

    def __init__(self, destination_connection_profile_name: _Optional[str]=..., gcs_destination_config: _Optional[_Union[GcsDestinationConfig, _Mapping]]=...) -> None:
        ...

class Stream(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'source_config', 'destination_config', 'state', 'backfill_all', 'backfill_none', 'errors')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Stream.State]
        CREATED: _ClassVar[Stream.State]
        RUNNING: _ClassVar[Stream.State]
        PAUSED: _ClassVar[Stream.State]
        MAINTENANCE: _ClassVar[Stream.State]
        FAILED: _ClassVar[Stream.State]
        FAILED_PERMANENTLY: _ClassVar[Stream.State]
        STARTING: _ClassVar[Stream.State]
        DRAINING: _ClassVar[Stream.State]
    STATE_UNSPECIFIED: Stream.State
    CREATED: Stream.State
    RUNNING: Stream.State
    PAUSED: Stream.State
    MAINTENANCE: Stream.State
    FAILED: Stream.State
    FAILED_PERMANENTLY: Stream.State
    STARTING: Stream.State
    DRAINING: Stream.State

    class BackfillAllStrategy(_message.Message):
        __slots__ = ('oracle_excluded_objects', 'mysql_excluded_objects')
        ORACLE_EXCLUDED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        MYSQL_EXCLUDED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        oracle_excluded_objects: OracleRdbms
        mysql_excluded_objects: MysqlRdbms

        def __init__(self, oracle_excluded_objects: _Optional[_Union[OracleRdbms, _Mapping]]=..., mysql_excluded_objects: _Optional[_Union[MysqlRdbms, _Mapping]]=...) -> None:
            ...

    class BackfillNoneStrategy(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
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

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., source_config: _Optional[_Union[SourceConfig, _Mapping]]=..., destination_config: _Optional[_Union[DestinationConfig, _Mapping]]=..., state: _Optional[_Union[Stream.State, str]]=..., backfill_all: _Optional[_Union[Stream.BackfillAllStrategy, _Mapping]]=..., backfill_none: _Optional[_Union[Stream.BackfillNoneStrategy, _Mapping]]=..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]]=...) -> None:
        ...

class Error(_message.Message):
    __slots__ = ('reason', 'error_uuid', 'message', 'error_time', 'details')

    class DetailsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
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

    def __init__(self, reason: _Optional[str]=..., error_uuid: _Optional[str]=..., message: _Optional[str]=..., error_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., details: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ValidationResult(_message.Message):
    __slots__ = ('validations',)
    VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    validations: _containers.RepeatedCompositeFieldContainer[Validation]

    def __init__(self, validations: _Optional[_Iterable[_Union[Validation, _Mapping]]]=...) -> None:
        ...

class Validation(_message.Message):
    __slots__ = ('description', 'status', 'message', 'code')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[Validation.Status]
        NOT_EXECUTED: _ClassVar[Validation.Status]
        FAILED: _ClassVar[Validation.Status]
        PASSED: _ClassVar[Validation.Status]
    STATUS_UNSPECIFIED: Validation.Status
    NOT_EXECUTED: Validation.Status
    FAILED: Validation.Status
    PASSED: Validation.Status
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    description: str
    status: Validation.Status
    message: _containers.RepeatedCompositeFieldContainer[ValidationMessage]
    code: str

    def __init__(self, description: _Optional[str]=..., status: _Optional[_Union[Validation.Status, str]]=..., message: _Optional[_Iterable[_Union[ValidationMessage, _Mapping]]]=..., code: _Optional[str]=...) -> None:
        ...

class ValidationMessage(_message.Message):
    __slots__ = ('message', 'level', 'metadata', 'code')

    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEVEL_UNSPECIFIED: _ClassVar[ValidationMessage.Level]
        WARNING: _ClassVar[ValidationMessage.Level]
        ERROR: _ClassVar[ValidationMessage.Level]
    LEVEL_UNSPECIFIED: ValidationMessage.Level
    WARNING: ValidationMessage.Level
    ERROR: ValidationMessage.Level

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    level: ValidationMessage.Level
    metadata: _containers.ScalarMap[str, str]
    code: str

    def __init__(self, message: _Optional[str]=..., level: _Optional[_Union[ValidationMessage.Level, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., code: _Optional[str]=...) -> None:
        ...