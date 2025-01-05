from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NetworkArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_ARCHITECTURE_UNSPECIFIED: _ClassVar[NetworkArchitecture]
    NETWORK_ARCHITECTURE_OLD_CSQL_PRODUCER: _ClassVar[NetworkArchitecture]
    NETWORK_ARCHITECTURE_NEW_CSQL_PRODUCER: _ClassVar[NetworkArchitecture]

class DatabaseEngine(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_ENGINE_UNSPECIFIED: _ClassVar[DatabaseEngine]
    MYSQL: _ClassVar[DatabaseEngine]
    POSTGRESQL: _ClassVar[DatabaseEngine]
    ORACLE: _ClassVar[DatabaseEngine]

class DatabaseProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_PROVIDER_UNSPECIFIED: _ClassVar[DatabaseProvider]
    CLOUDSQL: _ClassVar[DatabaseProvider]
    RDS: _ClassVar[DatabaseProvider]
    AURORA: _ClassVar[DatabaseProvider]
    ALLOYDB: _ClassVar[DatabaseProvider]
NETWORK_ARCHITECTURE_UNSPECIFIED: NetworkArchitecture
NETWORK_ARCHITECTURE_OLD_CSQL_PRODUCER: NetworkArchitecture
NETWORK_ARCHITECTURE_NEW_CSQL_PRODUCER: NetworkArchitecture
DATABASE_ENGINE_UNSPECIFIED: DatabaseEngine
MYSQL: DatabaseEngine
POSTGRESQL: DatabaseEngine
ORACLE: DatabaseEngine
DATABASE_PROVIDER_UNSPECIFIED: DatabaseProvider
CLOUDSQL: DatabaseProvider
RDS: DatabaseProvider
AURORA: DatabaseProvider
ALLOYDB: DatabaseProvider

class SslConfig(_message.Message):
    __slots__ = ('type', 'client_key', 'client_certificate', 'ca_certificate')

    class SslType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SSL_TYPE_UNSPECIFIED: _ClassVar[SslConfig.SslType]
        SERVER_ONLY: _ClassVar[SslConfig.SslType]
        SERVER_CLIENT: _ClassVar[SslConfig.SslType]
    SSL_TYPE_UNSPECIFIED: SslConfig.SslType
    SERVER_ONLY: SslConfig.SslType
    SERVER_CLIENT: SslConfig.SslType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    type: SslConfig.SslType
    client_key: str
    client_certificate: str
    ca_certificate: str

    def __init__(self, type: _Optional[_Union[SslConfig.SslType, str]]=..., client_key: _Optional[str]=..., client_certificate: _Optional[str]=..., ca_certificate: _Optional[str]=...) -> None:
        ...

class MySqlConnectionProfile(_message.Message):
    __slots__ = ('host', 'port', 'username', 'password', 'password_set', 'ssl', 'cloud_sql_id')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
    SSL_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    username: str
    password: str
    password_set: bool
    ssl: SslConfig
    cloud_sql_id: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., username: _Optional[str]=..., password: _Optional[str]=..., password_set: bool=..., ssl: _Optional[_Union[SslConfig, _Mapping]]=..., cloud_sql_id: _Optional[str]=...) -> None:
        ...

class PostgreSqlConnectionProfile(_message.Message):
    __slots__ = ('host', 'port', 'username', 'password', 'password_set', 'ssl', 'cloud_sql_id', 'network_architecture', 'static_ip_connectivity', 'private_service_connect_connectivity')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
    SSL_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    STATIC_IP_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SERVICE_CONNECT_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    username: str
    password: str
    password_set: bool
    ssl: SslConfig
    cloud_sql_id: str
    network_architecture: NetworkArchitecture
    static_ip_connectivity: StaticIpConnectivity
    private_service_connect_connectivity: PrivateServiceConnectConnectivity

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., username: _Optional[str]=..., password: _Optional[str]=..., password_set: bool=..., ssl: _Optional[_Union[SslConfig, _Mapping]]=..., cloud_sql_id: _Optional[str]=..., network_architecture: _Optional[_Union[NetworkArchitecture, str]]=..., static_ip_connectivity: _Optional[_Union[StaticIpConnectivity, _Mapping]]=..., private_service_connect_connectivity: _Optional[_Union[PrivateServiceConnectConnectivity, _Mapping]]=...) -> None:
        ...

class OracleConnectionProfile(_message.Message):
    __slots__ = ('host', 'port', 'username', 'password', 'password_set', 'database_service', 'ssl', 'static_service_ip_connectivity', 'forward_ssh_connectivity', 'private_connectivity')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
    DATABASE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    SSL_FIELD_NUMBER: _ClassVar[int]
    STATIC_SERVICE_IP_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    FORWARD_SSH_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    username: str
    password: str
    password_set: bool
    database_service: str
    ssl: SslConfig
    static_service_ip_connectivity: StaticServiceIpConnectivity
    forward_ssh_connectivity: ForwardSshTunnelConnectivity
    private_connectivity: PrivateConnectivity

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., username: _Optional[str]=..., password: _Optional[str]=..., password_set: bool=..., database_service: _Optional[str]=..., ssl: _Optional[_Union[SslConfig, _Mapping]]=..., static_service_ip_connectivity: _Optional[_Union[StaticServiceIpConnectivity, _Mapping]]=..., forward_ssh_connectivity: _Optional[_Union[ForwardSshTunnelConnectivity, _Mapping]]=..., private_connectivity: _Optional[_Union[PrivateConnectivity, _Mapping]]=...) -> None:
        ...

class CloudSqlConnectionProfile(_message.Message):
    __slots__ = ('cloud_sql_id', 'settings', 'private_ip', 'public_ip', 'additional_public_ip')
    CLOUD_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    cloud_sql_id: str
    settings: CloudSqlSettings
    private_ip: str
    public_ip: str
    additional_public_ip: str

    def __init__(self, cloud_sql_id: _Optional[str]=..., settings: _Optional[_Union[CloudSqlSettings, _Mapping]]=..., private_ip: _Optional[str]=..., public_ip: _Optional[str]=..., additional_public_ip: _Optional[str]=...) -> None:
        ...

class AlloyDbConnectionProfile(_message.Message):
    __slots__ = ('cluster_id', 'settings')
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    settings: AlloyDbSettings

    def __init__(self, cluster_id: _Optional[str]=..., settings: _Optional[_Union[AlloyDbSettings, _Mapping]]=...) -> None:
        ...

class SqlAclEntry(_message.Message):
    __slots__ = ('value', 'expire_time', 'ttl', 'label')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    value: str
    expire_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    label: str

    def __init__(self, value: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., label: _Optional[str]=...) -> None:
        ...

class SqlIpConfig(_message.Message):
    __slots__ = ('enable_ipv4', 'private_network', 'allocated_ip_range', 'require_ssl', 'authorized_networks')
    ENABLE_IPV4_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SSL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    enable_ipv4: _wrappers_pb2.BoolValue
    private_network: str
    allocated_ip_range: str
    require_ssl: _wrappers_pb2.BoolValue
    authorized_networks: _containers.RepeatedCompositeFieldContainer[SqlAclEntry]

    def __init__(self, enable_ipv4: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., private_network: _Optional[str]=..., allocated_ip_range: _Optional[str]=..., require_ssl: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., authorized_networks: _Optional[_Iterable[_Union[SqlAclEntry, _Mapping]]]=...) -> None:
        ...

class CloudSqlSettings(_message.Message):
    __slots__ = ('database_version', 'user_labels', 'tier', 'storage_auto_resize_limit', 'activation_policy', 'ip_config', 'auto_storage_increase', 'database_flags', 'data_disk_type', 'data_disk_size_gb', 'zone', 'secondary_zone', 'source_id', 'root_password', 'root_password_set', 'collation', 'cmek_key_name', 'availability_type', 'edition')

    class SqlActivationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_ACTIVATION_POLICY_UNSPECIFIED: _ClassVar[CloudSqlSettings.SqlActivationPolicy]
        ALWAYS: _ClassVar[CloudSqlSettings.SqlActivationPolicy]
        NEVER: _ClassVar[CloudSqlSettings.SqlActivationPolicy]
    SQL_ACTIVATION_POLICY_UNSPECIFIED: CloudSqlSettings.SqlActivationPolicy
    ALWAYS: CloudSqlSettings.SqlActivationPolicy
    NEVER: CloudSqlSettings.SqlActivationPolicy

    class SqlDataDiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_DATA_DISK_TYPE_UNSPECIFIED: _ClassVar[CloudSqlSettings.SqlDataDiskType]
        PD_SSD: _ClassVar[CloudSqlSettings.SqlDataDiskType]
        PD_HDD: _ClassVar[CloudSqlSettings.SqlDataDiskType]
    SQL_DATA_DISK_TYPE_UNSPECIFIED: CloudSqlSettings.SqlDataDiskType
    PD_SSD: CloudSqlSettings.SqlDataDiskType
    PD_HDD: CloudSqlSettings.SqlDataDiskType

    class SqlDatabaseVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_DATABASE_VERSION_UNSPECIFIED: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        MYSQL_5_6: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        MYSQL_5_7: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        POSTGRES_9_6: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        POSTGRES_11: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        POSTGRES_10: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        MYSQL_8_0: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        POSTGRES_12: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        POSTGRES_13: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        POSTGRES_14: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
        POSTGRES_15: _ClassVar[CloudSqlSettings.SqlDatabaseVersion]
    SQL_DATABASE_VERSION_UNSPECIFIED: CloudSqlSettings.SqlDatabaseVersion
    MYSQL_5_6: CloudSqlSettings.SqlDatabaseVersion
    MYSQL_5_7: CloudSqlSettings.SqlDatabaseVersion
    POSTGRES_9_6: CloudSqlSettings.SqlDatabaseVersion
    POSTGRES_11: CloudSqlSettings.SqlDatabaseVersion
    POSTGRES_10: CloudSqlSettings.SqlDatabaseVersion
    MYSQL_8_0: CloudSqlSettings.SqlDatabaseVersion
    POSTGRES_12: CloudSqlSettings.SqlDatabaseVersion
    POSTGRES_13: CloudSqlSettings.SqlDatabaseVersion
    POSTGRES_14: CloudSqlSettings.SqlDatabaseVersion
    POSTGRES_15: CloudSqlSettings.SqlDatabaseVersion

    class SqlAvailabilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_AVAILABILITY_TYPE_UNSPECIFIED: _ClassVar[CloudSqlSettings.SqlAvailabilityType]
        ZONAL: _ClassVar[CloudSqlSettings.SqlAvailabilityType]
        REGIONAL: _ClassVar[CloudSqlSettings.SqlAvailabilityType]
    SQL_AVAILABILITY_TYPE_UNSPECIFIED: CloudSqlSettings.SqlAvailabilityType
    ZONAL: CloudSqlSettings.SqlAvailabilityType
    REGIONAL: CloudSqlSettings.SqlAvailabilityType

    class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EDITION_UNSPECIFIED: _ClassVar[CloudSqlSettings.Edition]
        ENTERPRISE: _ClassVar[CloudSqlSettings.Edition]
        ENTERPRISE_PLUS: _ClassVar[CloudSqlSettings.Edition]
    EDITION_UNSPECIFIED: CloudSqlSettings.Edition
    ENTERPRISE: CloudSqlSettings.Edition
    ENTERPRISE_PLUS: CloudSqlSettings.Edition

    class UserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class DatabaseFlagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_AUTO_RESIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTO_STORAGE_INCREASE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_ZONE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROOT_PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    CMEK_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    database_version: CloudSqlSettings.SqlDatabaseVersion
    user_labels: _containers.ScalarMap[str, str]
    tier: str
    storage_auto_resize_limit: _wrappers_pb2.Int64Value
    activation_policy: CloudSqlSettings.SqlActivationPolicy
    ip_config: SqlIpConfig
    auto_storage_increase: _wrappers_pb2.BoolValue
    database_flags: _containers.ScalarMap[str, str]
    data_disk_type: CloudSqlSettings.SqlDataDiskType
    data_disk_size_gb: _wrappers_pb2.Int64Value
    zone: str
    secondary_zone: str
    source_id: str
    root_password: str
    root_password_set: bool
    collation: str
    cmek_key_name: str
    availability_type: CloudSqlSettings.SqlAvailabilityType
    edition: CloudSqlSettings.Edition

    def __init__(self, database_version: _Optional[_Union[CloudSqlSettings.SqlDatabaseVersion, str]]=..., user_labels: _Optional[_Mapping[str, str]]=..., tier: _Optional[str]=..., storage_auto_resize_limit: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., activation_policy: _Optional[_Union[CloudSqlSettings.SqlActivationPolicy, str]]=..., ip_config: _Optional[_Union[SqlIpConfig, _Mapping]]=..., auto_storage_increase: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., database_flags: _Optional[_Mapping[str, str]]=..., data_disk_type: _Optional[_Union[CloudSqlSettings.SqlDataDiskType, str]]=..., data_disk_size_gb: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., zone: _Optional[str]=..., secondary_zone: _Optional[str]=..., source_id: _Optional[str]=..., root_password: _Optional[str]=..., root_password_set: bool=..., collation: _Optional[str]=..., cmek_key_name: _Optional[str]=..., availability_type: _Optional[_Union[CloudSqlSettings.SqlAvailabilityType, str]]=..., edition: _Optional[_Union[CloudSqlSettings.Edition, str]]=...) -> None:
        ...

class AlloyDbSettings(_message.Message):
    __slots__ = ('initial_user', 'vpc_network', 'labels', 'primary_instance_settings', 'encryption_config')

    class UserPassword(_message.Message):
        __slots__ = ('user', 'password', 'password_set')
        USER_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
        user: str
        password: str
        password_set: bool

        def __init__(self, user: _Optional[str]=..., password: _Optional[str]=..., password_set: bool=...) -> None:
            ...

    class PrimaryInstanceSettings(_message.Message):
        __slots__ = ('id', 'machine_config', 'database_flags', 'labels', 'private_ip')

        class MachineConfig(_message.Message):
            __slots__ = ('cpu_count',)
            CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
            cpu_count: int

            def __init__(self, cpu_count: _Optional[int]=...) -> None:
                ...

        class DatabaseFlagsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...

        class LabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ID_FIELD_NUMBER: _ClassVar[int]
        MACHINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        DATABASE_FLAGS_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_IP_FIELD_NUMBER: _ClassVar[int]
        id: str
        machine_config: AlloyDbSettings.PrimaryInstanceSettings.MachineConfig
        database_flags: _containers.ScalarMap[str, str]
        labels: _containers.ScalarMap[str, str]
        private_ip: str

        def __init__(self, id: _Optional[str]=..., machine_config: _Optional[_Union[AlloyDbSettings.PrimaryInstanceSettings.MachineConfig, _Mapping]]=..., database_flags: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., private_ip: _Optional[str]=...) -> None:
            ...

    class EncryptionConfig(_message.Message):
        __slots__ = ('kms_key_name',)
        KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        kms_key_name: str

        def __init__(self, kms_key_name: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    INITIAL_USER_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INSTANCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    initial_user: AlloyDbSettings.UserPassword
    vpc_network: str
    labels: _containers.ScalarMap[str, str]
    primary_instance_settings: AlloyDbSettings.PrimaryInstanceSettings
    encryption_config: AlloyDbSettings.EncryptionConfig

    def __init__(self, initial_user: _Optional[_Union[AlloyDbSettings.UserPassword, _Mapping]]=..., vpc_network: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., primary_instance_settings: _Optional[_Union[AlloyDbSettings.PrimaryInstanceSettings, _Mapping]]=..., encryption_config: _Optional[_Union[AlloyDbSettings.EncryptionConfig, _Mapping]]=...) -> None:
        ...

class StaticIpConnectivity(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PrivateServiceConnectConnectivity(_message.Message):
    __slots__ = ('service_attachment',)
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    service_attachment: str

    def __init__(self, service_attachment: _Optional[str]=...) -> None:
        ...

class ReverseSshConnectivity(_message.Message):
    __slots__ = ('vm_ip', 'vm_port', 'vm', 'vpc')
    VM_IP_FIELD_NUMBER: _ClassVar[int]
    VM_PORT_FIELD_NUMBER: _ClassVar[int]
    VM_FIELD_NUMBER: _ClassVar[int]
    VPC_FIELD_NUMBER: _ClassVar[int]
    vm_ip: str
    vm_port: int
    vm: str
    vpc: str

    def __init__(self, vm_ip: _Optional[str]=..., vm_port: _Optional[int]=..., vm: _Optional[str]=..., vpc: _Optional[str]=...) -> None:
        ...

class VpcPeeringConnectivity(_message.Message):
    __slots__ = ('vpc',)
    VPC_FIELD_NUMBER: _ClassVar[int]
    vpc: str

    def __init__(self, vpc: _Optional[str]=...) -> None:
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

class StaticServiceIpConnectivity(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PrivateConnectivity(_message.Message):
    __slots__ = ('private_connection',)
    PRIVATE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    private_connection: str

    def __init__(self, private_connection: _Optional[str]=...) -> None:
        ...

class DatabaseType(_message.Message):
    __slots__ = ('provider', 'engine')
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    provider: DatabaseProvider
    engine: DatabaseEngine

    def __init__(self, provider: _Optional[_Union[DatabaseProvider, str]]=..., engine: _Optional[_Union[DatabaseEngine, str]]=...) -> None:
        ...

class MigrationJob(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'state', 'phase', 'type', 'dump_path', 'dump_flags', 'source', 'destination', 'reverse_ssh_connectivity', 'vpc_peering_connectivity', 'static_ip_connectivity', 'duration', 'error', 'source_database', 'destination_database', 'end_time', 'conversion_workspace', 'filter', 'cmek_key_name', 'performance_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MigrationJob.State]
        MAINTENANCE: _ClassVar[MigrationJob.State]
        DRAFT: _ClassVar[MigrationJob.State]
        CREATING: _ClassVar[MigrationJob.State]
        NOT_STARTED: _ClassVar[MigrationJob.State]
        RUNNING: _ClassVar[MigrationJob.State]
        FAILED: _ClassVar[MigrationJob.State]
        COMPLETED: _ClassVar[MigrationJob.State]
        DELETING: _ClassVar[MigrationJob.State]
        STOPPING: _ClassVar[MigrationJob.State]
        STOPPED: _ClassVar[MigrationJob.State]
        DELETED: _ClassVar[MigrationJob.State]
        UPDATING: _ClassVar[MigrationJob.State]
        STARTING: _ClassVar[MigrationJob.State]
        RESTARTING: _ClassVar[MigrationJob.State]
        RESUMING: _ClassVar[MigrationJob.State]
    STATE_UNSPECIFIED: MigrationJob.State
    MAINTENANCE: MigrationJob.State
    DRAFT: MigrationJob.State
    CREATING: MigrationJob.State
    NOT_STARTED: MigrationJob.State
    RUNNING: MigrationJob.State
    FAILED: MigrationJob.State
    COMPLETED: MigrationJob.State
    DELETING: MigrationJob.State
    STOPPING: MigrationJob.State
    STOPPED: MigrationJob.State
    DELETED: MigrationJob.State
    UPDATING: MigrationJob.State
    STARTING: MigrationJob.State
    RESTARTING: MigrationJob.State
    RESUMING: MigrationJob.State

    class Phase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHASE_UNSPECIFIED: _ClassVar[MigrationJob.Phase]
        FULL_DUMP: _ClassVar[MigrationJob.Phase]
        CDC: _ClassVar[MigrationJob.Phase]
        PROMOTE_IN_PROGRESS: _ClassVar[MigrationJob.Phase]
        WAITING_FOR_SOURCE_WRITES_TO_STOP: _ClassVar[MigrationJob.Phase]
        PREPARING_THE_DUMP: _ClassVar[MigrationJob.Phase]
    PHASE_UNSPECIFIED: MigrationJob.Phase
    FULL_DUMP: MigrationJob.Phase
    CDC: MigrationJob.Phase
    PROMOTE_IN_PROGRESS: MigrationJob.Phase
    WAITING_FOR_SOURCE_WRITES_TO_STOP: MigrationJob.Phase
    PREPARING_THE_DUMP: MigrationJob.Phase

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[MigrationJob.Type]
        ONE_TIME: _ClassVar[MigrationJob.Type]
        CONTINUOUS: _ClassVar[MigrationJob.Type]
    TYPE_UNSPECIFIED: MigrationJob.Type
    ONE_TIME: MigrationJob.Type
    CONTINUOUS: MigrationJob.Type

    class DumpFlag(_message.Message):
        __slots__ = ('name', 'value')
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str

        def __init__(self, name: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class DumpFlags(_message.Message):
        __slots__ = ('dump_flags',)
        DUMP_FLAGS_FIELD_NUMBER: _ClassVar[int]
        dump_flags: _containers.RepeatedCompositeFieldContainer[MigrationJob.DumpFlag]

        def __init__(self, dump_flags: _Optional[_Iterable[_Union[MigrationJob.DumpFlag, _Mapping]]]=...) -> None:
            ...

    class PerformanceConfig(_message.Message):
        __slots__ = ('dump_parallel_level',)

        class DumpParallelLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DUMP_PARALLEL_LEVEL_UNSPECIFIED: _ClassVar[MigrationJob.PerformanceConfig.DumpParallelLevel]
            MIN: _ClassVar[MigrationJob.PerformanceConfig.DumpParallelLevel]
            OPTIMAL: _ClassVar[MigrationJob.PerformanceConfig.DumpParallelLevel]
            MAX: _ClassVar[MigrationJob.PerformanceConfig.DumpParallelLevel]
        DUMP_PARALLEL_LEVEL_UNSPECIFIED: MigrationJob.PerformanceConfig.DumpParallelLevel
        MIN: MigrationJob.PerformanceConfig.DumpParallelLevel
        OPTIMAL: MigrationJob.PerformanceConfig.DumpParallelLevel
        MAX: MigrationJob.PerformanceConfig.DumpParallelLevel
        DUMP_PARALLEL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        dump_parallel_level: MigrationJob.PerformanceConfig.DumpParallelLevel

        def __init__(self, dump_parallel_level: _Optional[_Union[MigrationJob.PerformanceConfig.DumpParallelLevel, str]]=...) -> None:
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
    STATE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DUMP_PATH_FIELD_NUMBER: _ClassVar[int]
    DUMP_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    REVERSE_SSH_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    VPC_PEERING_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    STATIC_IP_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DATABASE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CMEK_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    state: MigrationJob.State
    phase: MigrationJob.Phase
    type: MigrationJob.Type
    dump_path: str
    dump_flags: MigrationJob.DumpFlags
    source: str
    destination: str
    reverse_ssh_connectivity: ReverseSshConnectivity
    vpc_peering_connectivity: VpcPeeringConnectivity
    static_ip_connectivity: StaticIpConnectivity
    duration: _duration_pb2.Duration
    error: _status_pb2.Status
    source_database: DatabaseType
    destination_database: DatabaseType
    end_time: _timestamp_pb2.Timestamp
    conversion_workspace: ConversionWorkspaceInfo
    filter: str
    cmek_key_name: str
    performance_config: MigrationJob.PerformanceConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., state: _Optional[_Union[MigrationJob.State, str]]=..., phase: _Optional[_Union[MigrationJob.Phase, str]]=..., type: _Optional[_Union[MigrationJob.Type, str]]=..., dump_path: _Optional[str]=..., dump_flags: _Optional[_Union[MigrationJob.DumpFlags, _Mapping]]=..., source: _Optional[str]=..., destination: _Optional[str]=..., reverse_ssh_connectivity: _Optional[_Union[ReverseSshConnectivity, _Mapping]]=..., vpc_peering_connectivity: _Optional[_Union[VpcPeeringConnectivity, _Mapping]]=..., static_ip_connectivity: _Optional[_Union[StaticIpConnectivity, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., source_database: _Optional[_Union[DatabaseType, _Mapping]]=..., destination_database: _Optional[_Union[DatabaseType, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., conversion_workspace: _Optional[_Union[ConversionWorkspaceInfo, _Mapping]]=..., filter: _Optional[str]=..., cmek_key_name: _Optional[str]=..., performance_config: _Optional[_Union[MigrationJob.PerformanceConfig, _Mapping]]=...) -> None:
        ...

class ConversionWorkspaceInfo(_message.Message):
    __slots__ = ('name', 'commit_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    commit_id: str

    def __init__(self, name: _Optional[str]=..., commit_id: _Optional[str]=...) -> None:
        ...

class ConnectionProfile(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'state', 'display_name', 'mysql', 'postgresql', 'oracle', 'cloudsql', 'alloydb', 'error', 'provider')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ConnectionProfile.State]
        DRAFT: _ClassVar[ConnectionProfile.State]
        CREATING: _ClassVar[ConnectionProfile.State]
        READY: _ClassVar[ConnectionProfile.State]
        UPDATING: _ClassVar[ConnectionProfile.State]
        DELETING: _ClassVar[ConnectionProfile.State]
        DELETED: _ClassVar[ConnectionProfile.State]
        FAILED: _ClassVar[ConnectionProfile.State]
    STATE_UNSPECIFIED: ConnectionProfile.State
    DRAFT: ConnectionProfile.State
    CREATING: ConnectionProfile.State
    READY: ConnectionProfile.State
    UPDATING: ConnectionProfile.State
    DELETING: ConnectionProfile.State
    DELETED: ConnectionProfile.State
    FAILED: ConnectionProfile.State

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
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MYSQL_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_FIELD_NUMBER: _ClassVar[int]
    ORACLE_FIELD_NUMBER: _ClassVar[int]
    CLOUDSQL_FIELD_NUMBER: _ClassVar[int]
    ALLOYDB_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: ConnectionProfile.State
    display_name: str
    mysql: MySqlConnectionProfile
    postgresql: PostgreSqlConnectionProfile
    oracle: OracleConnectionProfile
    cloudsql: CloudSqlConnectionProfile
    alloydb: AlloyDbConnectionProfile
    error: _status_pb2.Status
    provider: DatabaseProvider

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[ConnectionProfile.State, str]]=..., display_name: _Optional[str]=..., mysql: _Optional[_Union[MySqlConnectionProfile, _Mapping]]=..., postgresql: _Optional[_Union[PostgreSqlConnectionProfile, _Mapping]]=..., oracle: _Optional[_Union[OracleConnectionProfile, _Mapping]]=..., cloudsql: _Optional[_Union[CloudSqlConnectionProfile, _Mapping]]=..., alloydb: _Optional[_Union[AlloyDbConnectionProfile, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., provider: _Optional[_Union[DatabaseProvider, str]]=...) -> None:
        ...

class MigrationJobVerificationError(_message.Message):
    __slots__ = ('error_code', 'error_message', 'error_detail_message')

    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[MigrationJobVerificationError.ErrorCode]
        CONNECTION_FAILURE: _ClassVar[MigrationJobVerificationError.ErrorCode]
        AUTHENTICATION_FAILURE: _ClassVar[MigrationJobVerificationError.ErrorCode]
        INVALID_CONNECTION_PROFILE_CONFIG: _ClassVar[MigrationJobVerificationError.ErrorCode]
        VERSION_INCOMPATIBILITY: _ClassVar[MigrationJobVerificationError.ErrorCode]
        CONNECTION_PROFILE_TYPES_INCOMPATIBILITY: _ClassVar[MigrationJobVerificationError.ErrorCode]
        NO_PGLOGICAL_INSTALLED: _ClassVar[MigrationJobVerificationError.ErrorCode]
        PGLOGICAL_NODE_ALREADY_EXISTS: _ClassVar[MigrationJobVerificationError.ErrorCode]
        INVALID_WAL_LEVEL: _ClassVar[MigrationJobVerificationError.ErrorCode]
        INVALID_SHARED_PRELOAD_LIBRARY: _ClassVar[MigrationJobVerificationError.ErrorCode]
        INSUFFICIENT_MAX_REPLICATION_SLOTS: _ClassVar[MigrationJobVerificationError.ErrorCode]
        INSUFFICIENT_MAX_WAL_SENDERS: _ClassVar[MigrationJobVerificationError.ErrorCode]
        INSUFFICIENT_MAX_WORKER_PROCESSES: _ClassVar[MigrationJobVerificationError.ErrorCode]
        UNSUPPORTED_EXTENSIONS: _ClassVar[MigrationJobVerificationError.ErrorCode]
        UNSUPPORTED_MIGRATION_TYPE: _ClassVar[MigrationJobVerificationError.ErrorCode]
        INVALID_RDS_LOGICAL_REPLICATION: _ClassVar[MigrationJobVerificationError.ErrorCode]
        UNSUPPORTED_GTID_MODE: _ClassVar[MigrationJobVerificationError.ErrorCode]
        UNSUPPORTED_TABLE_DEFINITION: _ClassVar[MigrationJobVerificationError.ErrorCode]
        UNSUPPORTED_DEFINER: _ClassVar[MigrationJobVerificationError.ErrorCode]
        CANT_RESTART_RUNNING_MIGRATION: _ClassVar[MigrationJobVerificationError.ErrorCode]
        SOURCE_ALREADY_SETUP: _ClassVar[MigrationJobVerificationError.ErrorCode]
        TABLES_WITH_LIMITED_SUPPORT: _ClassVar[MigrationJobVerificationError.ErrorCode]
        UNSUPPORTED_DATABASE_LOCALE: _ClassVar[MigrationJobVerificationError.ErrorCode]
        UNSUPPORTED_DATABASE_FDW_CONFIG: _ClassVar[MigrationJobVerificationError.ErrorCode]
        ERROR_RDBMS: _ClassVar[MigrationJobVerificationError.ErrorCode]
        SOURCE_SIZE_EXCEEDS_THRESHOLD: _ClassVar[MigrationJobVerificationError.ErrorCode]
        EXISTING_CONFLICTING_DATABASES: _ClassVar[MigrationJobVerificationError.ErrorCode]
        PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE: _ClassVar[MigrationJobVerificationError.ErrorCode]
    ERROR_CODE_UNSPECIFIED: MigrationJobVerificationError.ErrorCode
    CONNECTION_FAILURE: MigrationJobVerificationError.ErrorCode
    AUTHENTICATION_FAILURE: MigrationJobVerificationError.ErrorCode
    INVALID_CONNECTION_PROFILE_CONFIG: MigrationJobVerificationError.ErrorCode
    VERSION_INCOMPATIBILITY: MigrationJobVerificationError.ErrorCode
    CONNECTION_PROFILE_TYPES_INCOMPATIBILITY: MigrationJobVerificationError.ErrorCode
    NO_PGLOGICAL_INSTALLED: MigrationJobVerificationError.ErrorCode
    PGLOGICAL_NODE_ALREADY_EXISTS: MigrationJobVerificationError.ErrorCode
    INVALID_WAL_LEVEL: MigrationJobVerificationError.ErrorCode
    INVALID_SHARED_PRELOAD_LIBRARY: MigrationJobVerificationError.ErrorCode
    INSUFFICIENT_MAX_REPLICATION_SLOTS: MigrationJobVerificationError.ErrorCode
    INSUFFICIENT_MAX_WAL_SENDERS: MigrationJobVerificationError.ErrorCode
    INSUFFICIENT_MAX_WORKER_PROCESSES: MigrationJobVerificationError.ErrorCode
    UNSUPPORTED_EXTENSIONS: MigrationJobVerificationError.ErrorCode
    UNSUPPORTED_MIGRATION_TYPE: MigrationJobVerificationError.ErrorCode
    INVALID_RDS_LOGICAL_REPLICATION: MigrationJobVerificationError.ErrorCode
    UNSUPPORTED_GTID_MODE: MigrationJobVerificationError.ErrorCode
    UNSUPPORTED_TABLE_DEFINITION: MigrationJobVerificationError.ErrorCode
    UNSUPPORTED_DEFINER: MigrationJobVerificationError.ErrorCode
    CANT_RESTART_RUNNING_MIGRATION: MigrationJobVerificationError.ErrorCode
    SOURCE_ALREADY_SETUP: MigrationJobVerificationError.ErrorCode
    TABLES_WITH_LIMITED_SUPPORT: MigrationJobVerificationError.ErrorCode
    UNSUPPORTED_DATABASE_LOCALE: MigrationJobVerificationError.ErrorCode
    UNSUPPORTED_DATABASE_FDW_CONFIG: MigrationJobVerificationError.ErrorCode
    ERROR_RDBMS: MigrationJobVerificationError.ErrorCode
    SOURCE_SIZE_EXCEEDS_THRESHOLD: MigrationJobVerificationError.ErrorCode
    EXISTING_CONFLICTING_DATABASES: MigrationJobVerificationError.ErrorCode
    PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE: MigrationJobVerificationError.ErrorCode
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_code: MigrationJobVerificationError.ErrorCode
    error_message: str
    error_detail_message: str

    def __init__(self, error_code: _Optional[_Union[MigrationJobVerificationError.ErrorCode, str]]=..., error_message: _Optional[str]=..., error_detail_message: _Optional[str]=...) -> None:
        ...

class PrivateConnection(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'state', 'error', 'vpc_peering_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PrivateConnection.State]
        CREATING: _ClassVar[PrivateConnection.State]
        CREATED: _ClassVar[PrivateConnection.State]
        FAILED: _ClassVar[PrivateConnection.State]
        DELETING: _ClassVar[PrivateConnection.State]
        FAILED_TO_DELETE: _ClassVar[PrivateConnection.State]
        DELETED: _ClassVar[PrivateConnection.State]
    STATE_UNSPECIFIED: PrivateConnection.State
    CREATING: PrivateConnection.State
    CREATED: PrivateConnection.State
    FAILED: PrivateConnection.State
    DELETING: PrivateConnection.State
    FAILED_TO_DELETE: PrivateConnection.State
    DELETED: PrivateConnection.State

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
    error: _status_pb2.Status
    vpc_peering_config: VpcPeeringConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., state: _Optional[_Union[PrivateConnection.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., vpc_peering_config: _Optional[_Union[VpcPeeringConfig, _Mapping]]=...) -> None:
        ...

class VpcPeeringConfig(_message.Message):
    __slots__ = ('vpc_name', 'subnet')
    VPC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    vpc_name: str
    subnet: str

    def __init__(self, vpc_name: _Optional[str]=..., subnet: _Optional[str]=...) -> None:
        ...