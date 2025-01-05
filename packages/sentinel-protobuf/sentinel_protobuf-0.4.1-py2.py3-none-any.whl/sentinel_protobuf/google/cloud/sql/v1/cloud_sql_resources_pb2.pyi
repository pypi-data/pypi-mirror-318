from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_FILE_TYPE_UNSPECIFIED: _ClassVar[SqlFileType]
    SQL: _ClassVar[SqlFileType]
    CSV: _ClassVar[SqlFileType]
    BAK: _ClassVar[SqlFileType]

class BakType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BAK_TYPE_UNSPECIFIED: _ClassVar[BakType]
    FULL: _ClassVar[BakType]
    DIFF: _ClassVar[BakType]
    TLOG: _ClassVar[BakType]

class SqlBackendType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_BACKEND_TYPE_UNSPECIFIED: _ClassVar[SqlBackendType]
    FIRST_GEN: _ClassVar[SqlBackendType]
    SECOND_GEN: _ClassVar[SqlBackendType]
    EXTERNAL: _ClassVar[SqlBackendType]

class SqlIpAddressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_IP_ADDRESS_TYPE_UNSPECIFIED: _ClassVar[SqlIpAddressType]
    PRIMARY: _ClassVar[SqlIpAddressType]
    OUTGOING: _ClassVar[SqlIpAddressType]
    PRIVATE: _ClassVar[SqlIpAddressType]
    MIGRATED_1ST_GEN: _ClassVar[SqlIpAddressType]

class SqlDatabaseVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_DATABASE_VERSION_UNSPECIFIED: _ClassVar[SqlDatabaseVersion]
    MYSQL_5_1: _ClassVar[SqlDatabaseVersion]
    MYSQL_5_5: _ClassVar[SqlDatabaseVersion]
    MYSQL_5_6: _ClassVar[SqlDatabaseVersion]
    MYSQL_5_7: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2017_STANDARD: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2017_ENTERPRISE: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2017_EXPRESS: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2017_WEB: _ClassVar[SqlDatabaseVersion]
    POSTGRES_9_6: _ClassVar[SqlDatabaseVersion]
    POSTGRES_10: _ClassVar[SqlDatabaseVersion]
    POSTGRES_11: _ClassVar[SqlDatabaseVersion]
    POSTGRES_12: _ClassVar[SqlDatabaseVersion]
    POSTGRES_13: _ClassVar[SqlDatabaseVersion]
    POSTGRES_14: _ClassVar[SqlDatabaseVersion]
    POSTGRES_15: _ClassVar[SqlDatabaseVersion]
    POSTGRES_16: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_18: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_26: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_27: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_28: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_29: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_30: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_31: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_32: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_33: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_34: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_35: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_36: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_37: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_38: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_39: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_0_40: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_4: _ClassVar[SqlDatabaseVersion]
    MYSQL_8_4_0: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2019_STANDARD: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2019_ENTERPRISE: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2019_EXPRESS: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2019_WEB: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2022_STANDARD: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2022_ENTERPRISE: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2022_EXPRESS: _ClassVar[SqlDatabaseVersion]
    SQLSERVER_2022_WEB: _ClassVar[SqlDatabaseVersion]

class SqlPricingPlan(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_PRICING_PLAN_UNSPECIFIED: _ClassVar[SqlPricingPlan]
    PACKAGE: _ClassVar[SqlPricingPlan]
    PER_USE: _ClassVar[SqlPricingPlan]

class SqlReplicationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_REPLICATION_TYPE_UNSPECIFIED: _ClassVar[SqlReplicationType]
    SYNCHRONOUS: _ClassVar[SqlReplicationType]
    ASYNCHRONOUS: _ClassVar[SqlReplicationType]

class SqlDataDiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_DATA_DISK_TYPE_UNSPECIFIED: _ClassVar[SqlDataDiskType]
    PD_SSD: _ClassVar[SqlDataDiskType]
    PD_HDD: _ClassVar[SqlDataDiskType]
    OBSOLETE_LOCAL_SSD: _ClassVar[SqlDataDiskType]

class SqlAvailabilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_AVAILABILITY_TYPE_UNSPECIFIED: _ClassVar[SqlAvailabilityType]
    ZONAL: _ClassVar[SqlAvailabilityType]
    REGIONAL: _ClassVar[SqlAvailabilityType]

class SqlUpdateTrack(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_UPDATE_TRACK_UNSPECIFIED: _ClassVar[SqlUpdateTrack]
    canary: _ClassVar[SqlUpdateTrack]
    stable: _ClassVar[SqlUpdateTrack]
    week5: _ClassVar[SqlUpdateTrack]
SQL_FILE_TYPE_UNSPECIFIED: SqlFileType
SQL: SqlFileType
CSV: SqlFileType
BAK: SqlFileType
BAK_TYPE_UNSPECIFIED: BakType
FULL: BakType
DIFF: BakType
TLOG: BakType
SQL_BACKEND_TYPE_UNSPECIFIED: SqlBackendType
FIRST_GEN: SqlBackendType
SECOND_GEN: SqlBackendType
EXTERNAL: SqlBackendType
SQL_IP_ADDRESS_TYPE_UNSPECIFIED: SqlIpAddressType
PRIMARY: SqlIpAddressType
OUTGOING: SqlIpAddressType
PRIVATE: SqlIpAddressType
MIGRATED_1ST_GEN: SqlIpAddressType
SQL_DATABASE_VERSION_UNSPECIFIED: SqlDatabaseVersion
MYSQL_5_1: SqlDatabaseVersion
MYSQL_5_5: SqlDatabaseVersion
MYSQL_5_6: SqlDatabaseVersion
MYSQL_5_7: SqlDatabaseVersion
SQLSERVER_2017_STANDARD: SqlDatabaseVersion
SQLSERVER_2017_ENTERPRISE: SqlDatabaseVersion
SQLSERVER_2017_EXPRESS: SqlDatabaseVersion
SQLSERVER_2017_WEB: SqlDatabaseVersion
POSTGRES_9_6: SqlDatabaseVersion
POSTGRES_10: SqlDatabaseVersion
POSTGRES_11: SqlDatabaseVersion
POSTGRES_12: SqlDatabaseVersion
POSTGRES_13: SqlDatabaseVersion
POSTGRES_14: SqlDatabaseVersion
POSTGRES_15: SqlDatabaseVersion
POSTGRES_16: SqlDatabaseVersion
MYSQL_8_0: SqlDatabaseVersion
MYSQL_8_0_18: SqlDatabaseVersion
MYSQL_8_0_26: SqlDatabaseVersion
MYSQL_8_0_27: SqlDatabaseVersion
MYSQL_8_0_28: SqlDatabaseVersion
MYSQL_8_0_29: SqlDatabaseVersion
MYSQL_8_0_30: SqlDatabaseVersion
MYSQL_8_0_31: SqlDatabaseVersion
MYSQL_8_0_32: SqlDatabaseVersion
MYSQL_8_0_33: SqlDatabaseVersion
MYSQL_8_0_34: SqlDatabaseVersion
MYSQL_8_0_35: SqlDatabaseVersion
MYSQL_8_0_36: SqlDatabaseVersion
MYSQL_8_0_37: SqlDatabaseVersion
MYSQL_8_0_38: SqlDatabaseVersion
MYSQL_8_0_39: SqlDatabaseVersion
MYSQL_8_0_40: SqlDatabaseVersion
MYSQL_8_4: SqlDatabaseVersion
MYSQL_8_4_0: SqlDatabaseVersion
SQLSERVER_2019_STANDARD: SqlDatabaseVersion
SQLSERVER_2019_ENTERPRISE: SqlDatabaseVersion
SQLSERVER_2019_EXPRESS: SqlDatabaseVersion
SQLSERVER_2019_WEB: SqlDatabaseVersion
SQLSERVER_2022_STANDARD: SqlDatabaseVersion
SQLSERVER_2022_ENTERPRISE: SqlDatabaseVersion
SQLSERVER_2022_EXPRESS: SqlDatabaseVersion
SQLSERVER_2022_WEB: SqlDatabaseVersion
SQL_PRICING_PLAN_UNSPECIFIED: SqlPricingPlan
PACKAGE: SqlPricingPlan
PER_USE: SqlPricingPlan
SQL_REPLICATION_TYPE_UNSPECIFIED: SqlReplicationType
SYNCHRONOUS: SqlReplicationType
ASYNCHRONOUS: SqlReplicationType
SQL_DATA_DISK_TYPE_UNSPECIFIED: SqlDataDiskType
PD_SSD: SqlDataDiskType
PD_HDD: SqlDataDiskType
OBSOLETE_LOCAL_SSD: SqlDataDiskType
SQL_AVAILABILITY_TYPE_UNSPECIFIED: SqlAvailabilityType
ZONAL: SqlAvailabilityType
REGIONAL: SqlAvailabilityType
SQL_UPDATE_TRACK_UNSPECIFIED: SqlUpdateTrack
canary: SqlUpdateTrack
stable: SqlUpdateTrack
week5: SqlUpdateTrack

class AclEntry(_message.Message):
    __slots__ = ("value", "expiration_time", "name", "kind")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    value: str
    expiration_time: _timestamp_pb2.Timestamp
    name: str
    kind: str
    def __init__(self, value: _Optional[str] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class ApiWarning(_message.Message):
    __slots__ = ("code", "message", "region")
    class SqlApiWarningCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_API_WARNING_CODE_UNSPECIFIED: _ClassVar[ApiWarning.SqlApiWarningCode]
        REGION_UNREACHABLE: _ClassVar[ApiWarning.SqlApiWarningCode]
        MAX_RESULTS_EXCEEDS_LIMIT: _ClassVar[ApiWarning.SqlApiWarningCode]
        COMPROMISED_CREDENTIALS: _ClassVar[ApiWarning.SqlApiWarningCode]
        INTERNAL_STATE_FAILURE: _ClassVar[ApiWarning.SqlApiWarningCode]
    SQL_API_WARNING_CODE_UNSPECIFIED: ApiWarning.SqlApiWarningCode
    REGION_UNREACHABLE: ApiWarning.SqlApiWarningCode
    MAX_RESULTS_EXCEEDS_LIMIT: ApiWarning.SqlApiWarningCode
    COMPROMISED_CREDENTIALS: ApiWarning.SqlApiWarningCode
    INTERNAL_STATE_FAILURE: ApiWarning.SqlApiWarningCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    code: ApiWarning.SqlApiWarningCode
    message: str
    region: str
    def __init__(self, code: _Optional[_Union[ApiWarning.SqlApiWarningCode, str]] = ..., message: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class BackupRetentionSettings(_message.Message):
    __slots__ = ("retention_unit", "retained_backups")
    class RetentionUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETENTION_UNIT_UNSPECIFIED: _ClassVar[BackupRetentionSettings.RetentionUnit]
        COUNT: _ClassVar[BackupRetentionSettings.RetentionUnit]
    RETENTION_UNIT_UNSPECIFIED: BackupRetentionSettings.RetentionUnit
    COUNT: BackupRetentionSettings.RetentionUnit
    RETENTION_UNIT_FIELD_NUMBER: _ClassVar[int]
    RETAINED_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    retention_unit: BackupRetentionSettings.RetentionUnit
    retained_backups: _wrappers_pb2.Int32Value
    def __init__(self, retention_unit: _Optional[_Union[BackupRetentionSettings.RetentionUnit, str]] = ..., retained_backups: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class BackupConfiguration(_message.Message):
    __slots__ = ("start_time", "enabled", "kind", "binary_log_enabled", "replication_log_archiving_enabled", "location", "point_in_time_recovery_enabled", "backup_retention_settings", "transaction_log_retention_days", "transactional_log_storage_state")
    class TransactionalLogStorageState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSACTIONAL_LOG_STORAGE_STATE_UNSPECIFIED: _ClassVar[BackupConfiguration.TransactionalLogStorageState]
        DISK: _ClassVar[BackupConfiguration.TransactionalLogStorageState]
        SWITCHING_TO_CLOUD_STORAGE: _ClassVar[BackupConfiguration.TransactionalLogStorageState]
        SWITCHED_TO_CLOUD_STORAGE: _ClassVar[BackupConfiguration.TransactionalLogStorageState]
        CLOUD_STORAGE: _ClassVar[BackupConfiguration.TransactionalLogStorageState]
    TRANSACTIONAL_LOG_STORAGE_STATE_UNSPECIFIED: BackupConfiguration.TransactionalLogStorageState
    DISK: BackupConfiguration.TransactionalLogStorageState
    SWITCHING_TO_CLOUD_STORAGE: BackupConfiguration.TransactionalLogStorageState
    SWITCHED_TO_CLOUD_STORAGE: BackupConfiguration.TransactionalLogStorageState
    CLOUD_STORAGE: BackupConfiguration.TransactionalLogStorageState
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    BINARY_LOG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_LOG_ARCHIVING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_RECOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RETENTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_LOG_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONAL_LOG_STORAGE_STATE_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    enabled: _wrappers_pb2.BoolValue
    kind: str
    binary_log_enabled: _wrappers_pb2.BoolValue
    replication_log_archiving_enabled: _wrappers_pb2.BoolValue
    location: str
    point_in_time_recovery_enabled: _wrappers_pb2.BoolValue
    backup_retention_settings: BackupRetentionSettings
    transaction_log_retention_days: _wrappers_pb2.Int32Value
    transactional_log_storage_state: BackupConfiguration.TransactionalLogStorageState
    def __init__(self, start_time: _Optional[str] = ..., enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., kind: _Optional[str] = ..., binary_log_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., replication_log_archiving_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., location: _Optional[str] = ..., point_in_time_recovery_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., backup_retention_settings: _Optional[_Union[BackupRetentionSettings, _Mapping]] = ..., transaction_log_retention_days: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., transactional_log_storage_state: _Optional[_Union[BackupConfiguration.TransactionalLogStorageState, str]] = ...) -> None: ...

class PerformDiskShrinkContext(_message.Message):
    __slots__ = ("target_size_gb",)
    TARGET_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    target_size_gb: int
    def __init__(self, target_size_gb: _Optional[int] = ...) -> None: ...

class BackupContext(_message.Message):
    __slots__ = ("backup_id", "kind")
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    backup_id: int
    kind: str
    def __init__(self, backup_id: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class Database(_message.Message):
    __slots__ = ("kind", "charset", "collation", "etag", "name", "instance", "self_link", "project", "sqlserver_database_details")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CHARSET_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SQLSERVER_DATABASE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    charset: str
    collation: str
    etag: str
    name: str
    instance: str
    self_link: str
    project: str
    sqlserver_database_details: SqlServerDatabaseDetails
    def __init__(self, kind: _Optional[str] = ..., charset: _Optional[str] = ..., collation: _Optional[str] = ..., etag: _Optional[str] = ..., name: _Optional[str] = ..., instance: _Optional[str] = ..., self_link: _Optional[str] = ..., project: _Optional[str] = ..., sqlserver_database_details: _Optional[_Union[SqlServerDatabaseDetails, _Mapping]] = ...) -> None: ...

class SqlServerDatabaseDetails(_message.Message):
    __slots__ = ("compatibility_level", "recovery_model")
    COMPATIBILITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_MODEL_FIELD_NUMBER: _ClassVar[int]
    compatibility_level: int
    recovery_model: str
    def __init__(self, compatibility_level: _Optional[int] = ..., recovery_model: _Optional[str] = ...) -> None: ...

class DatabaseFlags(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class MySqlSyncConfig(_message.Message):
    __slots__ = ("initial_sync_flags",)
    INITIAL_SYNC_FLAGS_FIELD_NUMBER: _ClassVar[int]
    initial_sync_flags: _containers.RepeatedCompositeFieldContainer[SyncFlags]
    def __init__(self, initial_sync_flags: _Optional[_Iterable[_Union[SyncFlags, _Mapping]]] = ...) -> None: ...

class SyncFlags(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class InstanceReference(_message.Message):
    __slots__ = ("name", "region", "project")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    region: str
    project: str
    def __init__(self, name: _Optional[str] = ..., region: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class DemoteMasterConfiguration(_message.Message):
    __slots__ = ("kind", "mysql_replica_configuration")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MYSQL_REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    mysql_replica_configuration: DemoteMasterMySqlReplicaConfiguration
    def __init__(self, kind: _Optional[str] = ..., mysql_replica_configuration: _Optional[_Union[DemoteMasterMySqlReplicaConfiguration, _Mapping]] = ...) -> None: ...

class DemoteMasterMySqlReplicaConfiguration(_message.Message):
    __slots__ = ("kind", "username", "password", "client_key", "client_certificate", "ca_certificate")
    KIND_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    username: str
    password: str
    client_key: str
    client_certificate: str
    ca_certificate: str
    def __init__(self, kind: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., client_key: _Optional[str] = ..., client_certificate: _Optional[str] = ..., ca_certificate: _Optional[str] = ...) -> None: ...

class ExportContext(_message.Message):
    __slots__ = ("uri", "databases", "kind", "sql_export_options", "csv_export_options", "file_type", "offload", "bak_export_options")
    class SqlCsvExportOptions(_message.Message):
        __slots__ = ("select_query", "escape_character", "quote_character", "fields_terminated_by", "lines_terminated_by")
        SELECT_QUERY_FIELD_NUMBER: _ClassVar[int]
        ESCAPE_CHARACTER_FIELD_NUMBER: _ClassVar[int]
        QUOTE_CHARACTER_FIELD_NUMBER: _ClassVar[int]
        FIELDS_TERMINATED_BY_FIELD_NUMBER: _ClassVar[int]
        LINES_TERMINATED_BY_FIELD_NUMBER: _ClassVar[int]
        select_query: str
        escape_character: str
        quote_character: str
        fields_terminated_by: str
        lines_terminated_by: str
        def __init__(self, select_query: _Optional[str] = ..., escape_character: _Optional[str] = ..., quote_character: _Optional[str] = ..., fields_terminated_by: _Optional[str] = ..., lines_terminated_by: _Optional[str] = ...) -> None: ...
    class SqlExportOptions(_message.Message):
        __slots__ = ("tables", "schema_only", "mysql_export_options", "threads", "parallel", "postgres_export_options")
        class MysqlExportOptions(_message.Message):
            __slots__ = ("master_data",)
            MASTER_DATA_FIELD_NUMBER: _ClassVar[int]
            master_data: _wrappers_pb2.Int32Value
            def __init__(self, master_data: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        class PostgresExportOptions(_message.Message):
            __slots__ = ("clean", "if_exists")
            CLEAN_FIELD_NUMBER: _ClassVar[int]
            IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
            clean: _wrappers_pb2.BoolValue
            if_exists: _wrappers_pb2.BoolValue
            def __init__(self, clean: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., if_exists: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
        TABLES_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_ONLY_FIELD_NUMBER: _ClassVar[int]
        MYSQL_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        THREADS_FIELD_NUMBER: _ClassVar[int]
        PARALLEL_FIELD_NUMBER: _ClassVar[int]
        POSTGRES_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[str]
        schema_only: _wrappers_pb2.BoolValue
        mysql_export_options: ExportContext.SqlExportOptions.MysqlExportOptions
        threads: _wrappers_pb2.Int32Value
        parallel: _wrappers_pb2.BoolValue
        postgres_export_options: ExportContext.SqlExportOptions.PostgresExportOptions
        def __init__(self, tables: _Optional[_Iterable[str]] = ..., schema_only: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., mysql_export_options: _Optional[_Union[ExportContext.SqlExportOptions.MysqlExportOptions, _Mapping]] = ..., threads: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., parallel: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., postgres_export_options: _Optional[_Union[ExportContext.SqlExportOptions.PostgresExportOptions, _Mapping]] = ...) -> None: ...
    class SqlBakExportOptions(_message.Message):
        __slots__ = ("striped", "stripe_count", "bak_type", "copy_only", "differential_base")
        STRIPED_FIELD_NUMBER: _ClassVar[int]
        STRIPE_COUNT_FIELD_NUMBER: _ClassVar[int]
        BAK_TYPE_FIELD_NUMBER: _ClassVar[int]
        COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
        DIFFERENTIAL_BASE_FIELD_NUMBER: _ClassVar[int]
        striped: _wrappers_pb2.BoolValue
        stripe_count: _wrappers_pb2.Int32Value
        bak_type: BakType
        copy_only: _wrappers_pb2.BoolValue
        differential_base: _wrappers_pb2.BoolValue
        def __init__(self, striped: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., stripe_count: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., bak_type: _Optional[_Union[BakType, str]] = ..., copy_only: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., differential_base: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    URI_FIELD_NUMBER: _ClassVar[int]
    DATABASES_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SQL_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CSV_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFLOAD_FIELD_NUMBER: _ClassVar[int]
    BAK_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    databases: _containers.RepeatedScalarFieldContainer[str]
    kind: str
    sql_export_options: ExportContext.SqlExportOptions
    csv_export_options: ExportContext.SqlCsvExportOptions
    file_type: SqlFileType
    offload: _wrappers_pb2.BoolValue
    bak_export_options: ExportContext.SqlBakExportOptions
    def __init__(self, uri: _Optional[str] = ..., databases: _Optional[_Iterable[str]] = ..., kind: _Optional[str] = ..., sql_export_options: _Optional[_Union[ExportContext.SqlExportOptions, _Mapping]] = ..., csv_export_options: _Optional[_Union[ExportContext.SqlCsvExportOptions, _Mapping]] = ..., file_type: _Optional[_Union[SqlFileType, str]] = ..., offload: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., bak_export_options: _Optional[_Union[ExportContext.SqlBakExportOptions, _Mapping]] = ...) -> None: ...

class ImportContext(_message.Message):
    __slots__ = ("uri", "database", "kind", "file_type", "csv_import_options", "import_user", "bak_import_options", "sql_import_options")
    class SqlImportOptions(_message.Message):
        __slots__ = ("threads", "parallel", "postgres_import_options")
        class PostgresImportOptions(_message.Message):
            __slots__ = ("clean", "if_exists")
            CLEAN_FIELD_NUMBER: _ClassVar[int]
            IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
            clean: _wrappers_pb2.BoolValue
            if_exists: _wrappers_pb2.BoolValue
            def __init__(self, clean: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., if_exists: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
        THREADS_FIELD_NUMBER: _ClassVar[int]
        PARALLEL_FIELD_NUMBER: _ClassVar[int]
        POSTGRES_IMPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        threads: _wrappers_pb2.Int32Value
        parallel: _wrappers_pb2.BoolValue
        postgres_import_options: ImportContext.SqlImportOptions.PostgresImportOptions
        def __init__(self, threads: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., parallel: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., postgres_import_options: _Optional[_Union[ImportContext.SqlImportOptions.PostgresImportOptions, _Mapping]] = ...) -> None: ...
    class SqlCsvImportOptions(_message.Message):
        __slots__ = ("table", "columns", "escape_character", "quote_character", "fields_terminated_by", "lines_terminated_by")
        TABLE_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        ESCAPE_CHARACTER_FIELD_NUMBER: _ClassVar[int]
        QUOTE_CHARACTER_FIELD_NUMBER: _ClassVar[int]
        FIELDS_TERMINATED_BY_FIELD_NUMBER: _ClassVar[int]
        LINES_TERMINATED_BY_FIELD_NUMBER: _ClassVar[int]
        table: str
        columns: _containers.RepeatedScalarFieldContainer[str]
        escape_character: str
        quote_character: str
        fields_terminated_by: str
        lines_terminated_by: str
        def __init__(self, table: _Optional[str] = ..., columns: _Optional[_Iterable[str]] = ..., escape_character: _Optional[str] = ..., quote_character: _Optional[str] = ..., fields_terminated_by: _Optional[str] = ..., lines_terminated_by: _Optional[str] = ...) -> None: ...
    class SqlBakImportOptions(_message.Message):
        __slots__ = ("encryption_options", "striped", "no_recovery", "recovery_only", "bak_type", "stop_at", "stop_at_mark")
        class EncryptionOptions(_message.Message):
            __slots__ = ("cert_path", "pvk_path", "pvk_password")
            CERT_PATH_FIELD_NUMBER: _ClassVar[int]
            PVK_PATH_FIELD_NUMBER: _ClassVar[int]
            PVK_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            cert_path: str
            pvk_path: str
            pvk_password: str
            def __init__(self, cert_path: _Optional[str] = ..., pvk_path: _Optional[str] = ..., pvk_password: _Optional[str] = ...) -> None: ...
        ENCRYPTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        STRIPED_FIELD_NUMBER: _ClassVar[int]
        NO_RECOVERY_FIELD_NUMBER: _ClassVar[int]
        RECOVERY_ONLY_FIELD_NUMBER: _ClassVar[int]
        BAK_TYPE_FIELD_NUMBER: _ClassVar[int]
        STOP_AT_FIELD_NUMBER: _ClassVar[int]
        STOP_AT_MARK_FIELD_NUMBER: _ClassVar[int]
        encryption_options: ImportContext.SqlBakImportOptions.EncryptionOptions
        striped: _wrappers_pb2.BoolValue
        no_recovery: _wrappers_pb2.BoolValue
        recovery_only: _wrappers_pb2.BoolValue
        bak_type: BakType
        stop_at: _timestamp_pb2.Timestamp
        stop_at_mark: str
        def __init__(self, encryption_options: _Optional[_Union[ImportContext.SqlBakImportOptions.EncryptionOptions, _Mapping]] = ..., striped: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., no_recovery: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., recovery_only: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., bak_type: _Optional[_Union[BakType, str]] = ..., stop_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stop_at_mark: _Optional[str] = ...) -> None: ...
    URI_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CSV_IMPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_USER_FIELD_NUMBER: _ClassVar[int]
    BAK_IMPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SQL_IMPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    database: str
    kind: str
    file_type: SqlFileType
    csv_import_options: ImportContext.SqlCsvImportOptions
    import_user: str
    bak_import_options: ImportContext.SqlBakImportOptions
    sql_import_options: ImportContext.SqlImportOptions
    def __init__(self, uri: _Optional[str] = ..., database: _Optional[str] = ..., kind: _Optional[str] = ..., file_type: _Optional[_Union[SqlFileType, str]] = ..., csv_import_options: _Optional[_Union[ImportContext.SqlCsvImportOptions, _Mapping]] = ..., import_user: _Optional[str] = ..., bak_import_options: _Optional[_Union[ImportContext.SqlBakImportOptions, _Mapping]] = ..., sql_import_options: _Optional[_Union[ImportContext.SqlImportOptions, _Mapping]] = ...) -> None: ...

class IpConfiguration(_message.Message):
    __slots__ = ("ipv4_enabled", "private_network", "require_ssl", "authorized_networks", "allocated_ip_range", "enable_private_path_for_google_cloud_services", "ssl_mode", "psc_config", "server_ca_mode")
    class SslMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SSL_MODE_UNSPECIFIED: _ClassVar[IpConfiguration.SslMode]
        ALLOW_UNENCRYPTED_AND_ENCRYPTED: _ClassVar[IpConfiguration.SslMode]
        ENCRYPTED_ONLY: _ClassVar[IpConfiguration.SslMode]
        TRUSTED_CLIENT_CERTIFICATE_REQUIRED: _ClassVar[IpConfiguration.SslMode]
    SSL_MODE_UNSPECIFIED: IpConfiguration.SslMode
    ALLOW_UNENCRYPTED_AND_ENCRYPTED: IpConfiguration.SslMode
    ENCRYPTED_ONLY: IpConfiguration.SslMode
    TRUSTED_CLIENT_CERTIFICATE_REQUIRED: IpConfiguration.SslMode
    class CaMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CA_MODE_UNSPECIFIED: _ClassVar[IpConfiguration.CaMode]
        GOOGLE_MANAGED_INTERNAL_CA: _ClassVar[IpConfiguration.CaMode]
        GOOGLE_MANAGED_CAS_CA: _ClassVar[IpConfiguration.CaMode]
    CA_MODE_UNSPECIFIED: IpConfiguration.CaMode
    GOOGLE_MANAGED_INTERNAL_CA: IpConfiguration.CaMode
    GOOGLE_MANAGED_CAS_CA: IpConfiguration.CaMode
    IPV4_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SSL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATE_PATH_FOR_GOOGLE_CLOUD_SERVICES_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_MODE_FIELD_NUMBER: _ClassVar[int]
    ipv4_enabled: _wrappers_pb2.BoolValue
    private_network: str
    require_ssl: _wrappers_pb2.BoolValue
    authorized_networks: _containers.RepeatedCompositeFieldContainer[AclEntry]
    allocated_ip_range: str
    enable_private_path_for_google_cloud_services: _wrappers_pb2.BoolValue
    ssl_mode: IpConfiguration.SslMode
    psc_config: PscConfig
    server_ca_mode: IpConfiguration.CaMode
    def __init__(self, ipv4_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., private_network: _Optional[str] = ..., require_ssl: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., authorized_networks: _Optional[_Iterable[_Union[AclEntry, _Mapping]]] = ..., allocated_ip_range: _Optional[str] = ..., enable_private_path_for_google_cloud_services: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., ssl_mode: _Optional[_Union[IpConfiguration.SslMode, str]] = ..., psc_config: _Optional[_Union[PscConfig, _Mapping]] = ..., server_ca_mode: _Optional[_Union[IpConfiguration.CaMode, str]] = ...) -> None: ...

class PscConfig(_message.Message):
    __slots__ = ("psc_enabled", "allowed_consumer_projects")
    PSC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONSUMER_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    psc_enabled: bool
    allowed_consumer_projects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, psc_enabled: bool = ..., allowed_consumer_projects: _Optional[_Iterable[str]] = ...) -> None: ...

class LocationPreference(_message.Message):
    __slots__ = ("follow_gae_application", "zone", "secondary_zone", "kind")
    FOLLOW_GAE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_ZONE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    follow_gae_application: str
    zone: str
    secondary_zone: str
    kind: str
    def __init__(self, follow_gae_application: _Optional[str] = ..., zone: _Optional[str] = ..., secondary_zone: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class MaintenanceWindow(_message.Message):
    __slots__ = ("hour", "day", "update_track", "kind")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TRACK_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    hour: _wrappers_pb2.Int32Value
    day: _wrappers_pb2.Int32Value
    update_track: SqlUpdateTrack
    kind: str
    def __init__(self, hour: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., update_track: _Optional[_Union[SqlUpdateTrack, str]] = ..., kind: _Optional[str] = ...) -> None: ...

class DenyMaintenancePeriod(_message.Message):
    __slots__ = ("start_date", "end_date", "time")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    time: str
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., time: _Optional[str] = ...) -> None: ...

class InsightsConfig(_message.Message):
    __slots__ = ("query_insights_enabled", "record_client_address", "record_application_tags", "query_string_length", "query_plans_per_minute")
    QUERY_INSIGHTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RECORD_CLIENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RECORD_APPLICATION_TAGS_FIELD_NUMBER: _ClassVar[int]
    QUERY_STRING_LENGTH_FIELD_NUMBER: _ClassVar[int]
    QUERY_PLANS_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    query_insights_enabled: bool
    record_client_address: bool
    record_application_tags: bool
    query_string_length: _wrappers_pb2.Int32Value
    query_plans_per_minute: _wrappers_pb2.Int32Value
    def __init__(self, query_insights_enabled: bool = ..., record_client_address: bool = ..., record_application_tags: bool = ..., query_string_length: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., query_plans_per_minute: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class MySqlReplicaConfiguration(_message.Message):
    __slots__ = ("dump_file_path", "username", "password", "connect_retry_interval", "master_heartbeat_period", "ca_certificate", "client_certificate", "client_key", "ssl_cipher", "verify_server_certificate", "kind")
    DUMP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CONNECT_RETRY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MASTER_HEARTBEAT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    SSL_CIPHER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SERVER_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    dump_file_path: str
    username: str
    password: str
    connect_retry_interval: _wrappers_pb2.Int32Value
    master_heartbeat_period: _wrappers_pb2.Int64Value
    ca_certificate: str
    client_certificate: str
    client_key: str
    ssl_cipher: str
    verify_server_certificate: _wrappers_pb2.BoolValue
    kind: str
    def __init__(self, dump_file_path: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., connect_retry_interval: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., master_heartbeat_period: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., ca_certificate: _Optional[str] = ..., client_certificate: _Optional[str] = ..., client_key: _Optional[str] = ..., ssl_cipher: _Optional[str] = ..., verify_server_certificate: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., kind: _Optional[str] = ...) -> None: ...

class DiskEncryptionConfiguration(_message.Message):
    __slots__ = ("kms_key_name", "kind")
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str
    kind: str
    def __init__(self, kms_key_name: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class DiskEncryptionStatus(_message.Message):
    __slots__ = ("kms_key_version_name", "kind")
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    kms_key_version_name: str
    kind: str
    def __init__(self, kms_key_version_name: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class IpMapping(_message.Message):
    __slots__ = ("type", "ip_address", "time_to_retire")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_RETIRE_FIELD_NUMBER: _ClassVar[int]
    type: SqlIpAddressType
    ip_address: str
    time_to_retire: _timestamp_pb2.Timestamp
    def __init__(self, type: _Optional[_Union[SqlIpAddressType, str]] = ..., ip_address: _Optional[str] = ..., time_to_retire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Operation(_message.Message):
    __slots__ = ("kind", "target_link", "status", "user", "insert_time", "start_time", "end_time", "error", "api_warning", "operation_type", "import_context", "export_context", "backup_context", "name", "target_id", "self_link", "target_project", "acquire_ssrs_lease_context")
    class SqlOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_OPERATION_TYPE_UNSPECIFIED: _ClassVar[Operation.SqlOperationType]
        IMPORT: _ClassVar[Operation.SqlOperationType]
        EXPORT: _ClassVar[Operation.SqlOperationType]
        CREATE: _ClassVar[Operation.SqlOperationType]
        UPDATE: _ClassVar[Operation.SqlOperationType]
        DELETE: _ClassVar[Operation.SqlOperationType]
        RESTART: _ClassVar[Operation.SqlOperationType]
        BACKUP: _ClassVar[Operation.SqlOperationType]
        SNAPSHOT: _ClassVar[Operation.SqlOperationType]
        BACKUP_VOLUME: _ClassVar[Operation.SqlOperationType]
        DELETE_VOLUME: _ClassVar[Operation.SqlOperationType]
        RESTORE_VOLUME: _ClassVar[Operation.SqlOperationType]
        INJECT_USER: _ClassVar[Operation.SqlOperationType]
        CLONE: _ClassVar[Operation.SqlOperationType]
        STOP_REPLICA: _ClassVar[Operation.SqlOperationType]
        START_REPLICA: _ClassVar[Operation.SqlOperationType]
        PROMOTE_REPLICA: _ClassVar[Operation.SqlOperationType]
        CREATE_REPLICA: _ClassVar[Operation.SqlOperationType]
        CREATE_USER: _ClassVar[Operation.SqlOperationType]
        DELETE_USER: _ClassVar[Operation.SqlOperationType]
        UPDATE_USER: _ClassVar[Operation.SqlOperationType]
        CREATE_DATABASE: _ClassVar[Operation.SqlOperationType]
        DELETE_DATABASE: _ClassVar[Operation.SqlOperationType]
        UPDATE_DATABASE: _ClassVar[Operation.SqlOperationType]
        FAILOVER: _ClassVar[Operation.SqlOperationType]
        DELETE_BACKUP: _ClassVar[Operation.SqlOperationType]
        RECREATE_REPLICA: _ClassVar[Operation.SqlOperationType]
        TRUNCATE_LOG: _ClassVar[Operation.SqlOperationType]
        DEMOTE_MASTER: _ClassVar[Operation.SqlOperationType]
        MAINTENANCE: _ClassVar[Operation.SqlOperationType]
        ENABLE_PRIVATE_IP: _ClassVar[Operation.SqlOperationType]
        DEFER_MAINTENANCE: _ClassVar[Operation.SqlOperationType]
        CREATE_CLONE: _ClassVar[Operation.SqlOperationType]
        RESCHEDULE_MAINTENANCE: _ClassVar[Operation.SqlOperationType]
        START_EXTERNAL_SYNC: _ClassVar[Operation.SqlOperationType]
        LOG_CLEANUP: _ClassVar[Operation.SqlOperationType]
        AUTO_RESTART: _ClassVar[Operation.SqlOperationType]
        REENCRYPT: _ClassVar[Operation.SqlOperationType]
        SWITCHOVER: _ClassVar[Operation.SqlOperationType]
        ACQUIRE_SSRS_LEASE: _ClassVar[Operation.SqlOperationType]
        RELEASE_SSRS_LEASE: _ClassVar[Operation.SqlOperationType]
        RECONFIGURE_OLD_PRIMARY: _ClassVar[Operation.SqlOperationType]
        CLUSTER_MAINTENANCE: _ClassVar[Operation.SqlOperationType]
        SELF_SERVICE_MAINTENANCE: _ClassVar[Operation.SqlOperationType]
        SWITCHOVER_TO_REPLICA: _ClassVar[Operation.SqlOperationType]
        MAJOR_VERSION_UPGRADE: _ClassVar[Operation.SqlOperationType]
    SQL_OPERATION_TYPE_UNSPECIFIED: Operation.SqlOperationType
    IMPORT: Operation.SqlOperationType
    EXPORT: Operation.SqlOperationType
    CREATE: Operation.SqlOperationType
    UPDATE: Operation.SqlOperationType
    DELETE: Operation.SqlOperationType
    RESTART: Operation.SqlOperationType
    BACKUP: Operation.SqlOperationType
    SNAPSHOT: Operation.SqlOperationType
    BACKUP_VOLUME: Operation.SqlOperationType
    DELETE_VOLUME: Operation.SqlOperationType
    RESTORE_VOLUME: Operation.SqlOperationType
    INJECT_USER: Operation.SqlOperationType
    CLONE: Operation.SqlOperationType
    STOP_REPLICA: Operation.SqlOperationType
    START_REPLICA: Operation.SqlOperationType
    PROMOTE_REPLICA: Operation.SqlOperationType
    CREATE_REPLICA: Operation.SqlOperationType
    CREATE_USER: Operation.SqlOperationType
    DELETE_USER: Operation.SqlOperationType
    UPDATE_USER: Operation.SqlOperationType
    CREATE_DATABASE: Operation.SqlOperationType
    DELETE_DATABASE: Operation.SqlOperationType
    UPDATE_DATABASE: Operation.SqlOperationType
    FAILOVER: Operation.SqlOperationType
    DELETE_BACKUP: Operation.SqlOperationType
    RECREATE_REPLICA: Operation.SqlOperationType
    TRUNCATE_LOG: Operation.SqlOperationType
    DEMOTE_MASTER: Operation.SqlOperationType
    MAINTENANCE: Operation.SqlOperationType
    ENABLE_PRIVATE_IP: Operation.SqlOperationType
    DEFER_MAINTENANCE: Operation.SqlOperationType
    CREATE_CLONE: Operation.SqlOperationType
    RESCHEDULE_MAINTENANCE: Operation.SqlOperationType
    START_EXTERNAL_SYNC: Operation.SqlOperationType
    LOG_CLEANUP: Operation.SqlOperationType
    AUTO_RESTART: Operation.SqlOperationType
    REENCRYPT: Operation.SqlOperationType
    SWITCHOVER: Operation.SqlOperationType
    ACQUIRE_SSRS_LEASE: Operation.SqlOperationType
    RELEASE_SSRS_LEASE: Operation.SqlOperationType
    RECONFIGURE_OLD_PRIMARY: Operation.SqlOperationType
    CLUSTER_MAINTENANCE: Operation.SqlOperationType
    SELF_SERVICE_MAINTENANCE: Operation.SqlOperationType
    SWITCHOVER_TO_REPLICA: Operation.SqlOperationType
    MAJOR_VERSION_UPGRADE: Operation.SqlOperationType
    class SqlOperationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_OPERATION_STATUS_UNSPECIFIED: _ClassVar[Operation.SqlOperationStatus]
        PENDING: _ClassVar[Operation.SqlOperationStatus]
        RUNNING: _ClassVar[Operation.SqlOperationStatus]
        DONE: _ClassVar[Operation.SqlOperationStatus]
    SQL_OPERATION_STATUS_UNSPECIFIED: Operation.SqlOperationStatus
    PENDING: Operation.SqlOperationStatus
    RUNNING: Operation.SqlOperationStatus
    DONE: Operation.SqlOperationStatus
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_LINK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    INSERT_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    API_WARNING_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_SSRS_LEASE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    kind: str
    target_link: str
    status: Operation.SqlOperationStatus
    user: str
    insert_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    error: OperationErrors
    api_warning: ApiWarning
    operation_type: Operation.SqlOperationType
    import_context: ImportContext
    export_context: ExportContext
    backup_context: BackupContext
    name: str
    target_id: str
    self_link: str
    target_project: str
    acquire_ssrs_lease_context: AcquireSsrsLeaseContext
    def __init__(self, kind: _Optional[str] = ..., target_link: _Optional[str] = ..., status: _Optional[_Union[Operation.SqlOperationStatus, str]] = ..., user: _Optional[str] = ..., insert_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[OperationErrors, _Mapping]] = ..., api_warning: _Optional[_Union[ApiWarning, _Mapping]] = ..., operation_type: _Optional[_Union[Operation.SqlOperationType, str]] = ..., import_context: _Optional[_Union[ImportContext, _Mapping]] = ..., export_context: _Optional[_Union[ExportContext, _Mapping]] = ..., backup_context: _Optional[_Union[BackupContext, _Mapping]] = ..., name: _Optional[str] = ..., target_id: _Optional[str] = ..., self_link: _Optional[str] = ..., target_project: _Optional[str] = ..., acquire_ssrs_lease_context: _Optional[_Union[AcquireSsrsLeaseContext, _Mapping]] = ...) -> None: ...

class OperationError(_message.Message):
    __slots__ = ("kind", "code", "message")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    code: str
    message: str
    def __init__(self, kind: _Optional[str] = ..., code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class OperationErrors(_message.Message):
    __slots__ = ("kind", "errors")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    errors: _containers.RepeatedCompositeFieldContainer[OperationError]
    def __init__(self, kind: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[OperationError, _Mapping]]] = ...) -> None: ...

class PasswordValidationPolicy(_message.Message):
    __slots__ = ("min_length", "complexity", "reuse_interval", "disallow_username_substring", "password_change_interval", "enable_password_policy", "disallow_compromised_credentials")
    class Complexity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLEXITY_UNSPECIFIED: _ClassVar[PasswordValidationPolicy.Complexity]
        COMPLEXITY_DEFAULT: _ClassVar[PasswordValidationPolicy.Complexity]
    COMPLEXITY_UNSPECIFIED: PasswordValidationPolicy.Complexity
    COMPLEXITY_DEFAULT: PasswordValidationPolicy.Complexity
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    COMPLEXITY_FIELD_NUMBER: _ClassVar[int]
    REUSE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DISALLOW_USERNAME_SUBSTRING_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_CHANGE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PASSWORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    DISALLOW_COMPROMISED_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    min_length: _wrappers_pb2.Int32Value
    complexity: PasswordValidationPolicy.Complexity
    reuse_interval: _wrappers_pb2.Int32Value
    disallow_username_substring: _wrappers_pb2.BoolValue
    password_change_interval: _duration_pb2.Duration
    enable_password_policy: _wrappers_pb2.BoolValue
    disallow_compromised_credentials: _wrappers_pb2.BoolValue
    def __init__(self, min_length: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., complexity: _Optional[_Union[PasswordValidationPolicy.Complexity, str]] = ..., reuse_interval: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., disallow_username_substring: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., password_change_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., enable_password_policy: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., disallow_compromised_credentials: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class DataCacheConfig(_message.Message):
    __slots__ = ("data_cache_enabled",)
    DATA_CACHE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    data_cache_enabled: bool
    def __init__(self, data_cache_enabled: bool = ...) -> None: ...

class Settings(_message.Message):
    __slots__ = ("settings_version", "authorized_gae_applications", "tier", "kind", "user_labels", "availability_type", "pricing_plan", "replication_type", "storage_auto_resize_limit", "activation_policy", "ip_configuration", "storage_auto_resize", "location_preference", "database_flags", "data_disk_type", "maintenance_window", "backup_configuration", "database_replication_enabled", "crash_safe_replication_enabled", "data_disk_size_gb", "active_directory_config", "collation", "deny_maintenance_periods", "insights_config", "password_validation_policy", "sql_server_audit_config", "edition", "connector_enforcement", "deletion_protection_enabled", "time_zone", "advanced_machine_features", "data_cache_config", "enable_google_ml_integration", "enable_dataplex_integration")
    class SqlActivationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_ACTIVATION_POLICY_UNSPECIFIED: _ClassVar[Settings.SqlActivationPolicy]
        ALWAYS: _ClassVar[Settings.SqlActivationPolicy]
        NEVER: _ClassVar[Settings.SqlActivationPolicy]
        ON_DEMAND: _ClassVar[Settings.SqlActivationPolicy]
    SQL_ACTIVATION_POLICY_UNSPECIFIED: Settings.SqlActivationPolicy
    ALWAYS: Settings.SqlActivationPolicy
    NEVER: Settings.SqlActivationPolicy
    ON_DEMAND: Settings.SqlActivationPolicy
    class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EDITION_UNSPECIFIED: _ClassVar[Settings.Edition]
        ENTERPRISE: _ClassVar[Settings.Edition]
        ENTERPRISE_PLUS: _ClassVar[Settings.Edition]
    EDITION_UNSPECIFIED: Settings.Edition
    ENTERPRISE: Settings.Edition
    ENTERPRISE_PLUS: Settings.Edition
    class ConnectorEnforcement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTOR_ENFORCEMENT_UNSPECIFIED: _ClassVar[Settings.ConnectorEnforcement]
        NOT_REQUIRED: _ClassVar[Settings.ConnectorEnforcement]
        REQUIRED: _ClassVar[Settings.ConnectorEnforcement]
    CONNECTOR_ENFORCEMENT_UNSPECIFIED: Settings.ConnectorEnforcement
    NOT_REQUIRED: Settings.ConnectorEnforcement
    REQUIRED: Settings.ConnectorEnforcement
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SETTINGS_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_GAE_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICING_PLAN_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_AUTO_RESIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_AUTO_RESIZE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_REPLICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRASH_SAFE_REPLICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    DENY_MAINTENANCE_PERIODS_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_VALIDATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_AUDIT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_MACHINE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    DATA_CACHE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_GOOGLE_ML_INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DATAPLEX_INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    settings_version: _wrappers_pb2.Int64Value
    authorized_gae_applications: _containers.RepeatedScalarFieldContainer[str]
    tier: str
    kind: str
    user_labels: _containers.ScalarMap[str, str]
    availability_type: SqlAvailabilityType
    pricing_plan: SqlPricingPlan
    replication_type: SqlReplicationType
    storage_auto_resize_limit: _wrappers_pb2.Int64Value
    activation_policy: Settings.SqlActivationPolicy
    ip_configuration: IpConfiguration
    storage_auto_resize: _wrappers_pb2.BoolValue
    location_preference: LocationPreference
    database_flags: _containers.RepeatedCompositeFieldContainer[DatabaseFlags]
    data_disk_type: SqlDataDiskType
    maintenance_window: MaintenanceWindow
    backup_configuration: BackupConfiguration
    database_replication_enabled: _wrappers_pb2.BoolValue
    crash_safe_replication_enabled: _wrappers_pb2.BoolValue
    data_disk_size_gb: _wrappers_pb2.Int64Value
    active_directory_config: SqlActiveDirectoryConfig
    collation: str
    deny_maintenance_periods: _containers.RepeatedCompositeFieldContainer[DenyMaintenancePeriod]
    insights_config: InsightsConfig
    password_validation_policy: PasswordValidationPolicy
    sql_server_audit_config: SqlServerAuditConfig
    edition: Settings.Edition
    connector_enforcement: Settings.ConnectorEnforcement
    deletion_protection_enabled: _wrappers_pb2.BoolValue
    time_zone: str
    advanced_machine_features: AdvancedMachineFeatures
    data_cache_config: DataCacheConfig
    enable_google_ml_integration: _wrappers_pb2.BoolValue
    enable_dataplex_integration: _wrappers_pb2.BoolValue
    def __init__(self, settings_version: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., authorized_gae_applications: _Optional[_Iterable[str]] = ..., tier: _Optional[str] = ..., kind: _Optional[str] = ..., user_labels: _Optional[_Mapping[str, str]] = ..., availability_type: _Optional[_Union[SqlAvailabilityType, str]] = ..., pricing_plan: _Optional[_Union[SqlPricingPlan, str]] = ..., replication_type: _Optional[_Union[SqlReplicationType, str]] = ..., storage_auto_resize_limit: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., activation_policy: _Optional[_Union[Settings.SqlActivationPolicy, str]] = ..., ip_configuration: _Optional[_Union[IpConfiguration, _Mapping]] = ..., storage_auto_resize: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., location_preference: _Optional[_Union[LocationPreference, _Mapping]] = ..., database_flags: _Optional[_Iterable[_Union[DatabaseFlags, _Mapping]]] = ..., data_disk_type: _Optional[_Union[SqlDataDiskType, str]] = ..., maintenance_window: _Optional[_Union[MaintenanceWindow, _Mapping]] = ..., backup_configuration: _Optional[_Union[BackupConfiguration, _Mapping]] = ..., database_replication_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., crash_safe_replication_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., data_disk_size_gb: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., active_directory_config: _Optional[_Union[SqlActiveDirectoryConfig, _Mapping]] = ..., collation: _Optional[str] = ..., deny_maintenance_periods: _Optional[_Iterable[_Union[DenyMaintenancePeriod, _Mapping]]] = ..., insights_config: _Optional[_Union[InsightsConfig, _Mapping]] = ..., password_validation_policy: _Optional[_Union[PasswordValidationPolicy, _Mapping]] = ..., sql_server_audit_config: _Optional[_Union[SqlServerAuditConfig, _Mapping]] = ..., edition: _Optional[_Union[Settings.Edition, str]] = ..., connector_enforcement: _Optional[_Union[Settings.ConnectorEnforcement, str]] = ..., deletion_protection_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., time_zone: _Optional[str] = ..., advanced_machine_features: _Optional[_Union[AdvancedMachineFeatures, _Mapping]] = ..., data_cache_config: _Optional[_Union[DataCacheConfig, _Mapping]] = ..., enable_google_ml_integration: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., enable_dataplex_integration: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class AdvancedMachineFeatures(_message.Message):
    __slots__ = ("threads_per_core",)
    THREADS_PER_CORE_FIELD_NUMBER: _ClassVar[int]
    threads_per_core: int
    def __init__(self, threads_per_core: _Optional[int] = ...) -> None: ...

class SslCert(_message.Message):
    __slots__ = ("kind", "cert_serial_number", "cert", "create_time", "common_name", "expiration_time", "sha1_fingerprint", "instance", "self_link")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CERT_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CERT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SHA1_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    kind: str
    cert_serial_number: str
    cert: str
    create_time: _timestamp_pb2.Timestamp
    common_name: str
    expiration_time: _timestamp_pb2.Timestamp
    sha1_fingerprint: str
    instance: str
    self_link: str
    def __init__(self, kind: _Optional[str] = ..., cert_serial_number: _Optional[str] = ..., cert: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., common_name: _Optional[str] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sha1_fingerprint: _Optional[str] = ..., instance: _Optional[str] = ..., self_link: _Optional[str] = ...) -> None: ...

class SslCertDetail(_message.Message):
    __slots__ = ("cert_info", "cert_private_key")
    CERT_INFO_FIELD_NUMBER: _ClassVar[int]
    CERT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    cert_info: SslCert
    cert_private_key: str
    def __init__(self, cert_info: _Optional[_Union[SslCert, _Mapping]] = ..., cert_private_key: _Optional[str] = ...) -> None: ...

class SqlActiveDirectoryConfig(_message.Message):
    __slots__ = ("kind", "domain")
    KIND_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    domain: str
    def __init__(self, kind: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class SqlServerAuditConfig(_message.Message):
    __slots__ = ("kind", "bucket", "retention_interval", "upload_interval")
    KIND_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    RETENTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    kind: str
    bucket: str
    retention_interval: _duration_pb2.Duration
    upload_interval: _duration_pb2.Duration
    def __init__(self, kind: _Optional[str] = ..., bucket: _Optional[str] = ..., retention_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., upload_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class AcquireSsrsLeaseContext(_message.Message):
    __slots__ = ("setup_login", "service_login", "report_database", "duration")
    SETUP_LOGIN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LOGIN_FIELD_NUMBER: _ClassVar[int]
    REPORT_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    setup_login: str
    service_login: str
    report_database: str
    duration: _duration_pb2.Duration
    def __init__(self, setup_login: _Optional[str] = ..., service_login: _Optional[str] = ..., report_database: _Optional[str] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
