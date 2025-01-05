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

class SqlBackupRunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_BACKUP_RUN_STATUS_UNSPECIFIED: _ClassVar[SqlBackupRunStatus]
    ENQUEUED: _ClassVar[SqlBackupRunStatus]
    OVERDUE: _ClassVar[SqlBackupRunStatus]
    RUNNING: _ClassVar[SqlBackupRunStatus]
    FAILED: _ClassVar[SqlBackupRunStatus]
    SUCCESSFUL: _ClassVar[SqlBackupRunStatus]
    SKIPPED: _ClassVar[SqlBackupRunStatus]
    DELETION_PENDING: _ClassVar[SqlBackupRunStatus]
    DELETION_FAILED: _ClassVar[SqlBackupRunStatus]
    DELETED: _ClassVar[SqlBackupRunStatus]

class SqlBackupRunType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_BACKUP_RUN_TYPE_UNSPECIFIED: _ClassVar[SqlBackupRunType]
    AUTOMATED: _ClassVar[SqlBackupRunType]
    ON_DEMAND: _ClassVar[SqlBackupRunType]

class SqlBackupKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_BACKUP_KIND_UNSPECIFIED: _ClassVar[SqlBackupKind]
    SNAPSHOT: _ClassVar[SqlBackupKind]
    PHYSICAL: _ClassVar[SqlBackupKind]

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

class SqlInstanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_INSTANCE_TYPE_UNSPECIFIED: _ClassVar[SqlInstanceType]
    CLOUD_SQL_INSTANCE: _ClassVar[SqlInstanceType]
    ON_PREMISES_INSTANCE: _ClassVar[SqlInstanceType]
    READ_REPLICA_INSTANCE: _ClassVar[SqlInstanceType]

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

class SqlSuspensionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_SUSPENSION_REASON_UNSPECIFIED: _ClassVar[SqlSuspensionReason]
    BILLING_ISSUE: _ClassVar[SqlSuspensionReason]
    LEGAL_ISSUE: _ClassVar[SqlSuspensionReason]
    OPERATIONAL_ISSUE: _ClassVar[SqlSuspensionReason]
    KMS_KEY_ISSUE: _ClassVar[SqlSuspensionReason]

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

class SqlFlagType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_FLAG_TYPE_UNSPECIFIED: _ClassVar[SqlFlagType]
    BOOLEAN: _ClassVar[SqlFlagType]
    STRING: _ClassVar[SqlFlagType]
    INTEGER: _ClassVar[SqlFlagType]
    NONE: _ClassVar[SqlFlagType]
    MYSQL_TIMEZONE_OFFSET: _ClassVar[SqlFlagType]
    FLOAT: _ClassVar[SqlFlagType]
    REPEATED_STRING: _ClassVar[SqlFlagType]
SQL_FILE_TYPE_UNSPECIFIED: SqlFileType
SQL: SqlFileType
CSV: SqlFileType
BAK: SqlFileType
BAK_TYPE_UNSPECIFIED: BakType
FULL: BakType
DIFF: BakType
TLOG: BakType
SQL_BACKUP_RUN_STATUS_UNSPECIFIED: SqlBackupRunStatus
ENQUEUED: SqlBackupRunStatus
OVERDUE: SqlBackupRunStatus
RUNNING: SqlBackupRunStatus
FAILED: SqlBackupRunStatus
SUCCESSFUL: SqlBackupRunStatus
SKIPPED: SqlBackupRunStatus
DELETION_PENDING: SqlBackupRunStatus
DELETION_FAILED: SqlBackupRunStatus
DELETED: SqlBackupRunStatus
SQL_BACKUP_RUN_TYPE_UNSPECIFIED: SqlBackupRunType
AUTOMATED: SqlBackupRunType
ON_DEMAND: SqlBackupRunType
SQL_BACKUP_KIND_UNSPECIFIED: SqlBackupKind
SNAPSHOT: SqlBackupKind
PHYSICAL: SqlBackupKind
SQL_BACKEND_TYPE_UNSPECIFIED: SqlBackendType
FIRST_GEN: SqlBackendType
SECOND_GEN: SqlBackendType
EXTERNAL: SqlBackendType
SQL_IP_ADDRESS_TYPE_UNSPECIFIED: SqlIpAddressType
PRIMARY: SqlIpAddressType
OUTGOING: SqlIpAddressType
PRIVATE: SqlIpAddressType
MIGRATED_1ST_GEN: SqlIpAddressType
SQL_INSTANCE_TYPE_UNSPECIFIED: SqlInstanceType
CLOUD_SQL_INSTANCE: SqlInstanceType
ON_PREMISES_INSTANCE: SqlInstanceType
READ_REPLICA_INSTANCE: SqlInstanceType
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
SQL_SUSPENSION_REASON_UNSPECIFIED: SqlSuspensionReason
BILLING_ISSUE: SqlSuspensionReason
LEGAL_ISSUE: SqlSuspensionReason
OPERATIONAL_ISSUE: SqlSuspensionReason
KMS_KEY_ISSUE: SqlSuspensionReason
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
SQL_FLAG_TYPE_UNSPECIFIED: SqlFlagType
BOOLEAN: SqlFlagType
STRING: SqlFlagType
INTEGER: SqlFlagType
NONE: SqlFlagType
MYSQL_TIMEZONE_OFFSET: SqlFlagType
FLOAT: SqlFlagType
REPEATED_STRING: SqlFlagType

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
    __slots__ = ("start_time", "enabled", "kind", "binary_log_enabled", "replication_log_archiving_enabled", "location", "point_in_time_recovery_enabled", "transaction_log_retention_days", "backup_retention_settings", "transactional_log_storage_state")
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
    TRANSACTION_LOG_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RETENTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONAL_LOG_STORAGE_STATE_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    enabled: _wrappers_pb2.BoolValue
    kind: str
    binary_log_enabled: _wrappers_pb2.BoolValue
    replication_log_archiving_enabled: _wrappers_pb2.BoolValue
    location: str
    point_in_time_recovery_enabled: _wrappers_pb2.BoolValue
    transaction_log_retention_days: _wrappers_pb2.Int32Value
    backup_retention_settings: BackupRetentionSettings
    transactional_log_storage_state: BackupConfiguration.TransactionalLogStorageState
    def __init__(self, start_time: _Optional[str] = ..., enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., kind: _Optional[str] = ..., binary_log_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., replication_log_archiving_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., location: _Optional[str] = ..., point_in_time_recovery_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., transaction_log_retention_days: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., backup_retention_settings: _Optional[_Union[BackupRetentionSettings, _Mapping]] = ..., transactional_log_storage_state: _Optional[_Union[BackupConfiguration.TransactionalLogStorageState, str]] = ...) -> None: ...

class BackupRun(_message.Message):
    __slots__ = ("kind", "status", "enqueued_time", "id", "start_time", "end_time", "error", "type", "description", "window_start_time", "instance", "self_link", "location", "disk_encryption_configuration", "disk_encryption_status", "backup_kind", "time_zone")
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENQUEUED_TIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_KIND_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    status: SqlBackupRunStatus
    enqueued_time: _timestamp_pb2.Timestamp
    id: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    error: OperationError
    type: SqlBackupRunType
    description: str
    window_start_time: _timestamp_pb2.Timestamp
    instance: str
    self_link: str
    location: str
    disk_encryption_configuration: DiskEncryptionConfiguration
    disk_encryption_status: DiskEncryptionStatus
    backup_kind: SqlBackupKind
    time_zone: str
    def __init__(self, kind: _Optional[str] = ..., status: _Optional[_Union[SqlBackupRunStatus, str]] = ..., enqueued_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., id: _Optional[int] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[OperationError, _Mapping]] = ..., type: _Optional[_Union[SqlBackupRunType, str]] = ..., description: _Optional[str] = ..., window_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instance: _Optional[str] = ..., self_link: _Optional[str] = ..., location: _Optional[str] = ..., disk_encryption_configuration: _Optional[_Union[DiskEncryptionConfiguration, _Mapping]] = ..., disk_encryption_status: _Optional[_Union[DiskEncryptionStatus, _Mapping]] = ..., backup_kind: _Optional[_Union[SqlBackupKind, str]] = ..., time_zone: _Optional[str] = ...) -> None: ...

class BackupRunsListResponse(_message.Message):
    __slots__ = ("kind", "items", "next_page_token")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[BackupRun]
    next_page_token: str
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[BackupRun, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class BinLogCoordinates(_message.Message):
    __slots__ = ("bin_log_file_name", "bin_log_position", "kind")
    BIN_LOG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    BIN_LOG_POSITION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    bin_log_file_name: str
    bin_log_position: int
    kind: str
    def __init__(self, bin_log_file_name: _Optional[str] = ..., bin_log_position: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class BackupContext(_message.Message):
    __slots__ = ("backup_id", "kind")
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    backup_id: int
    kind: str
    def __init__(self, backup_id: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class CloneContext(_message.Message):
    __slots__ = ("kind", "pitr_timestamp_ms", "destination_instance_name", "bin_log_coordinates", "point_in_time", "allocated_ip_range", "database_names", "preferred_zone", "preferred_secondary_zone")
    KIND_FIELD_NUMBER: _ClassVar[int]
    PITR_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BIN_LOG_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAMES_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_ZONE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_SECONDARY_ZONE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    pitr_timestamp_ms: int
    destination_instance_name: str
    bin_log_coordinates: BinLogCoordinates
    point_in_time: _timestamp_pb2.Timestamp
    allocated_ip_range: str
    database_names: _containers.RepeatedScalarFieldContainer[str]
    preferred_zone: str
    preferred_secondary_zone: str
    def __init__(self, kind: _Optional[str] = ..., pitr_timestamp_ms: _Optional[int] = ..., destination_instance_name: _Optional[str] = ..., bin_log_coordinates: _Optional[_Union[BinLogCoordinates, _Mapping]] = ..., point_in_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allocated_ip_range: _Optional[str] = ..., database_names: _Optional[_Iterable[str]] = ..., preferred_zone: _Optional[str] = ..., preferred_secondary_zone: _Optional[str] = ...) -> None: ...

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

class DatabaseInstance(_message.Message):
    __slots__ = ("kind", "state", "database_version", "settings", "etag", "failover_replica", "master_instance_name", "replica_names", "max_disk_size", "current_disk_size", "ip_addresses", "server_ca_cert", "instance_type", "project", "ipv6_address", "service_account_email_address", "on_premises_configuration", "replica_configuration", "backend_type", "self_link", "suspension_reason", "connection_name", "name", "region", "gce_zone", "secondary_gce_zone", "disk_encryption_configuration", "disk_encryption_status", "root_password", "scheduled_maintenance", "satisfies_pzs", "database_installed_version", "out_of_disk_report", "create_time", "available_maintenance_versions", "maintenance_version", "upgradable_database_versions", "sql_network_architecture", "psc_service_attachment_link", "dns_name", "primary_dns_name", "write_endpoint", "replication_cluster", "gemini_config")
    class SqlInstanceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_INSTANCE_STATE_UNSPECIFIED: _ClassVar[DatabaseInstance.SqlInstanceState]
        RUNNABLE: _ClassVar[DatabaseInstance.SqlInstanceState]
        SUSPENDED: _ClassVar[DatabaseInstance.SqlInstanceState]
        PENDING_DELETE: _ClassVar[DatabaseInstance.SqlInstanceState]
        PENDING_CREATE: _ClassVar[DatabaseInstance.SqlInstanceState]
        MAINTENANCE: _ClassVar[DatabaseInstance.SqlInstanceState]
        FAILED: _ClassVar[DatabaseInstance.SqlInstanceState]
        ONLINE_MAINTENANCE: _ClassVar[DatabaseInstance.SqlInstanceState]
    SQL_INSTANCE_STATE_UNSPECIFIED: DatabaseInstance.SqlInstanceState
    RUNNABLE: DatabaseInstance.SqlInstanceState
    SUSPENDED: DatabaseInstance.SqlInstanceState
    PENDING_DELETE: DatabaseInstance.SqlInstanceState
    PENDING_CREATE: DatabaseInstance.SqlInstanceState
    MAINTENANCE: DatabaseInstance.SqlInstanceState
    FAILED: DatabaseInstance.SqlInstanceState
    ONLINE_MAINTENANCE: DatabaseInstance.SqlInstanceState
    class SqlNetworkArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_NETWORK_ARCHITECTURE_UNSPECIFIED: _ClassVar[DatabaseInstance.SqlNetworkArchitecture]
        NEW_NETWORK_ARCHITECTURE: _ClassVar[DatabaseInstance.SqlNetworkArchitecture]
        OLD_NETWORK_ARCHITECTURE: _ClassVar[DatabaseInstance.SqlNetworkArchitecture]
    SQL_NETWORK_ARCHITECTURE_UNSPECIFIED: DatabaseInstance.SqlNetworkArchitecture
    NEW_NETWORK_ARCHITECTURE: DatabaseInstance.SqlNetworkArchitecture
    OLD_NETWORK_ARCHITECTURE: DatabaseInstance.SqlNetworkArchitecture
    class SqlFailoverReplica(_message.Message):
        __slots__ = ("name", "available")
        NAME_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        name: str
        available: _wrappers_pb2.BoolValue
        def __init__(self, name: _Optional[str] = ..., available: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class SqlScheduledMaintenance(_message.Message):
        __slots__ = ("start_time", "can_defer", "can_reschedule", "schedule_deadline_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        CAN_DEFER_FIELD_NUMBER: _ClassVar[int]
        CAN_RESCHEDULE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_DEADLINE_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        can_defer: bool
        can_reschedule: bool
        schedule_deadline_time: _timestamp_pb2.Timestamp
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., can_defer: bool = ..., can_reschedule: bool = ..., schedule_deadline_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class SqlOutOfDiskReport(_message.Message):
        __slots__ = ("sql_out_of_disk_state", "sql_min_recommended_increase_size_gb")
        class SqlOutOfDiskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SQL_OUT_OF_DISK_STATE_UNSPECIFIED: _ClassVar[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState]
            NORMAL: _ClassVar[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState]
            SOFT_SHUTDOWN: _ClassVar[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState]
        SQL_OUT_OF_DISK_STATE_UNSPECIFIED: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        NORMAL: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        SOFT_SHUTDOWN: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        SQL_OUT_OF_DISK_STATE_FIELD_NUMBER: _ClassVar[int]
        SQL_MIN_RECOMMENDED_INCREASE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        sql_out_of_disk_state: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        sql_min_recommended_increase_size_gb: int
        def __init__(self, sql_out_of_disk_state: _Optional[_Union[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState, str]] = ..., sql_min_recommended_increase_size_gb: _Optional[int] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_REPLICA_FIELD_NUMBER: _ClassVar[int]
    MASTER_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NAMES_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    IPV6_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ON_PREMISES_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    BACKEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_REASON_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    GCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_GCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ROOT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_DISK_REPORT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MAINTENANCE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPGRADABLE_DATABASE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SQL_NETWORK_ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    PSC_SERVICE_ATTACHMENT_LINK_FIELD_NUMBER: _ClassVar[int]
    DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    WRITE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    GEMINI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    kind: str
    state: DatabaseInstance.SqlInstanceState
    database_version: SqlDatabaseVersion
    settings: Settings
    etag: str
    failover_replica: DatabaseInstance.SqlFailoverReplica
    master_instance_name: str
    replica_names: _containers.RepeatedScalarFieldContainer[str]
    max_disk_size: _wrappers_pb2.Int64Value
    current_disk_size: _wrappers_pb2.Int64Value
    ip_addresses: _containers.RepeatedCompositeFieldContainer[IpMapping]
    server_ca_cert: SslCert
    instance_type: SqlInstanceType
    project: str
    ipv6_address: str
    service_account_email_address: str
    on_premises_configuration: OnPremisesConfiguration
    replica_configuration: ReplicaConfiguration
    backend_type: SqlBackendType
    self_link: str
    suspension_reason: _containers.RepeatedScalarFieldContainer[SqlSuspensionReason]
    connection_name: str
    name: str
    region: str
    gce_zone: str
    secondary_gce_zone: str
    disk_encryption_configuration: DiskEncryptionConfiguration
    disk_encryption_status: DiskEncryptionStatus
    root_password: str
    scheduled_maintenance: DatabaseInstance.SqlScheduledMaintenance
    satisfies_pzs: _wrappers_pb2.BoolValue
    database_installed_version: str
    out_of_disk_report: DatabaseInstance.SqlOutOfDiskReport
    create_time: _timestamp_pb2.Timestamp
    available_maintenance_versions: _containers.RepeatedScalarFieldContainer[str]
    maintenance_version: str
    upgradable_database_versions: _containers.RepeatedCompositeFieldContainer[AvailableDatabaseVersion]
    sql_network_architecture: DatabaseInstance.SqlNetworkArchitecture
    psc_service_attachment_link: str
    dns_name: str
    primary_dns_name: str
    write_endpoint: str
    replication_cluster: ReplicationCluster
    gemini_config: GeminiInstanceConfig
    def __init__(self, kind: _Optional[str] = ..., state: _Optional[_Union[DatabaseInstance.SqlInstanceState, str]] = ..., database_version: _Optional[_Union[SqlDatabaseVersion, str]] = ..., settings: _Optional[_Union[Settings, _Mapping]] = ..., etag: _Optional[str] = ..., failover_replica: _Optional[_Union[DatabaseInstance.SqlFailoverReplica, _Mapping]] = ..., master_instance_name: _Optional[str] = ..., replica_names: _Optional[_Iterable[str]] = ..., max_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., current_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., ip_addresses: _Optional[_Iterable[_Union[IpMapping, _Mapping]]] = ..., server_ca_cert: _Optional[_Union[SslCert, _Mapping]] = ..., instance_type: _Optional[_Union[SqlInstanceType, str]] = ..., project: _Optional[str] = ..., ipv6_address: _Optional[str] = ..., service_account_email_address: _Optional[str] = ..., on_premises_configuration: _Optional[_Union[OnPremisesConfiguration, _Mapping]] = ..., replica_configuration: _Optional[_Union[ReplicaConfiguration, _Mapping]] = ..., backend_type: _Optional[_Union[SqlBackendType, str]] = ..., self_link: _Optional[str] = ..., suspension_reason: _Optional[_Iterable[_Union[SqlSuspensionReason, str]]] = ..., connection_name: _Optional[str] = ..., name: _Optional[str] = ..., region: _Optional[str] = ..., gce_zone: _Optional[str] = ..., secondary_gce_zone: _Optional[str] = ..., disk_encryption_configuration: _Optional[_Union[DiskEncryptionConfiguration, _Mapping]] = ..., disk_encryption_status: _Optional[_Union[DiskEncryptionStatus, _Mapping]] = ..., root_password: _Optional[str] = ..., scheduled_maintenance: _Optional[_Union[DatabaseInstance.SqlScheduledMaintenance, _Mapping]] = ..., satisfies_pzs: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., database_installed_version: _Optional[str] = ..., out_of_disk_report: _Optional[_Union[DatabaseInstance.SqlOutOfDiskReport, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., available_maintenance_versions: _Optional[_Iterable[str]] = ..., maintenance_version: _Optional[str] = ..., upgradable_database_versions: _Optional[_Iterable[_Union[AvailableDatabaseVersion, _Mapping]]] = ..., sql_network_architecture: _Optional[_Union[DatabaseInstance.SqlNetworkArchitecture, str]] = ..., psc_service_attachment_link: _Optional[str] = ..., dns_name: _Optional[str] = ..., primary_dns_name: _Optional[str] = ..., write_endpoint: _Optional[str] = ..., replication_cluster: _Optional[_Union[ReplicationCluster, _Mapping]] = ..., gemini_config: _Optional[_Union[GeminiInstanceConfig, _Mapping]] = ...) -> None: ...

class GeminiInstanceConfig(_message.Message):
    __slots__ = ("entitled", "google_vacuum_mgmt_enabled", "oom_session_cancel_enabled", "active_query_enabled", "index_advisor_enabled", "flag_recommender_enabled")
    ENTITLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_VACUUM_MGMT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OOM_SESSION_CANCEL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_QUERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INDEX_ADVISOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FLAG_RECOMMENDER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    entitled: bool
    google_vacuum_mgmt_enabled: bool
    oom_session_cancel_enabled: bool
    active_query_enabled: bool
    index_advisor_enabled: bool
    flag_recommender_enabled: bool
    def __init__(self, entitled: bool = ..., google_vacuum_mgmt_enabled: bool = ..., oom_session_cancel_enabled: bool = ..., active_query_enabled: bool = ..., index_advisor_enabled: bool = ..., flag_recommender_enabled: bool = ...) -> None: ...

class ReplicationCluster(_message.Message):
    __slots__ = ("psa_write_endpoint", "failover_dr_replica_name", "dr_replica")
    PSA_WRITE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_DR_REPLICA_NAME_FIELD_NUMBER: _ClassVar[int]
    DR_REPLICA_FIELD_NUMBER: _ClassVar[int]
    psa_write_endpoint: str
    failover_dr_replica_name: str
    dr_replica: bool
    def __init__(self, psa_write_endpoint: _Optional[str] = ..., failover_dr_replica_name: _Optional[str] = ..., dr_replica: bool = ...) -> None: ...

class AvailableDatabaseVersion(_message.Message):
    __slots__ = ("major_version", "name", "display_name")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    major_version: str
    name: str
    display_name: str
    def __init__(self, major_version: _Optional[str] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class DatabasesListResponse(_message.Message):
    __slots__ = ("kind", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[Database]
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Database, _Mapping]]] = ...) -> None: ...

class DemoteMasterConfiguration(_message.Message):
    __slots__ = ("kind", "mysql_replica_configuration")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MYSQL_REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    mysql_replica_configuration: DemoteMasterMySqlReplicaConfiguration
    def __init__(self, kind: _Optional[str] = ..., mysql_replica_configuration: _Optional[_Union[DemoteMasterMySqlReplicaConfiguration, _Mapping]] = ...) -> None: ...

class DemoteMasterContext(_message.Message):
    __slots__ = ("kind", "verify_gtid_consistency", "master_instance_name", "replica_configuration", "skip_replication_setup")
    KIND_FIELD_NUMBER: _ClassVar[int]
    VERIFY_GTID_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    MASTER_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_REPLICATION_SETUP_FIELD_NUMBER: _ClassVar[int]
    kind: str
    verify_gtid_consistency: _wrappers_pb2.BoolValue
    master_instance_name: str
    replica_configuration: DemoteMasterConfiguration
    skip_replication_setup: bool
    def __init__(self, kind: _Optional[str] = ..., verify_gtid_consistency: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., master_instance_name: _Optional[str] = ..., replica_configuration: _Optional[_Union[DemoteMasterConfiguration, _Mapping]] = ..., skip_replication_setup: bool = ...) -> None: ...

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

class DemoteContext(_message.Message):
    __slots__ = ("kind", "source_representative_instance_name")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REPRESENTATIVE_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    kind: str
    source_representative_instance_name: str
    def __init__(self, kind: _Optional[str] = ..., source_representative_instance_name: _Optional[str] = ...) -> None: ...

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
        __slots__ = ("tables", "schema_only", "mysql_export_options", "threads", "parallel")
        class MysqlExportOptions(_message.Message):
            __slots__ = ("master_data",)
            MASTER_DATA_FIELD_NUMBER: _ClassVar[int]
            master_data: _wrappers_pb2.Int32Value
            def __init__(self, master_data: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        TABLES_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_ONLY_FIELD_NUMBER: _ClassVar[int]
        MYSQL_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        THREADS_FIELD_NUMBER: _ClassVar[int]
        PARALLEL_FIELD_NUMBER: _ClassVar[int]
        tables: _containers.RepeatedScalarFieldContainer[str]
        schema_only: _wrappers_pb2.BoolValue
        mysql_export_options: ExportContext.SqlExportOptions.MysqlExportOptions
        threads: _wrappers_pb2.Int32Value
        parallel: _wrappers_pb2.BoolValue
        def __init__(self, tables: _Optional[_Iterable[str]] = ..., schema_only: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., mysql_export_options: _Optional[_Union[ExportContext.SqlExportOptions.MysqlExportOptions, _Mapping]] = ..., threads: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., parallel: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
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

class FailoverContext(_message.Message):
    __slots__ = ("settings_version", "kind")
    SETTINGS_VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    settings_version: int
    kind: str
    def __init__(self, settings_version: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class Flag(_message.Message):
    __slots__ = ("name", "type", "applies_to", "allowed_string_values", "min_value", "max_value", "requires_restart", "kind", "in_beta", "allowed_int_values")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLIES_TO_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_RESTART_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    IN_BETA_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_INT_VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: SqlFlagType
    applies_to: _containers.RepeatedScalarFieldContainer[SqlDatabaseVersion]
    allowed_string_values: _containers.RepeatedScalarFieldContainer[str]
    min_value: _wrappers_pb2.Int64Value
    max_value: _wrappers_pb2.Int64Value
    requires_restart: _wrappers_pb2.BoolValue
    kind: str
    in_beta: _wrappers_pb2.BoolValue
    allowed_int_values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[SqlFlagType, str]] = ..., applies_to: _Optional[_Iterable[_Union[SqlDatabaseVersion, str]]] = ..., allowed_string_values: _Optional[_Iterable[str]] = ..., min_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., requires_restart: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., kind: _Optional[str] = ..., in_beta: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., allowed_int_values: _Optional[_Iterable[int]] = ...) -> None: ...

class FlagsListResponse(_message.Message):
    __slots__ = ("kind", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[Flag]
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Flag, _Mapping]]] = ...) -> None: ...

class ImportContext(_message.Message):
    __slots__ = ("uri", "database", "kind", "file_type", "csv_import_options", "import_user", "bak_import_options", "sql_import_options")
    class SqlImportOptions(_message.Message):
        __slots__ = ("threads", "parallel")
        THREADS_FIELD_NUMBER: _ClassVar[int]
        PARALLEL_FIELD_NUMBER: _ClassVar[int]
        threads: _wrappers_pb2.Int32Value
        parallel: _wrappers_pb2.BoolValue
        def __init__(self, threads: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., parallel: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
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

class InstancesCloneRequest(_message.Message):
    __slots__ = ("clone_context",)
    CLONE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    clone_context: CloneContext
    def __init__(self, clone_context: _Optional[_Union[CloneContext, _Mapping]] = ...) -> None: ...

class InstancesDemoteMasterRequest(_message.Message):
    __slots__ = ("demote_master_context",)
    DEMOTE_MASTER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    demote_master_context: DemoteMasterContext
    def __init__(self, demote_master_context: _Optional[_Union[DemoteMasterContext, _Mapping]] = ...) -> None: ...

class InstancesDemoteRequest(_message.Message):
    __slots__ = ("demote_context",)
    DEMOTE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    demote_context: DemoteContext
    def __init__(self, demote_context: _Optional[_Union[DemoteContext, _Mapping]] = ...) -> None: ...

class InstancesExportRequest(_message.Message):
    __slots__ = ("export_context",)
    EXPORT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    export_context: ExportContext
    def __init__(self, export_context: _Optional[_Union[ExportContext, _Mapping]] = ...) -> None: ...

class InstancesFailoverRequest(_message.Message):
    __slots__ = ("failover_context",)
    FAILOVER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    failover_context: FailoverContext
    def __init__(self, failover_context: _Optional[_Union[FailoverContext, _Mapping]] = ...) -> None: ...

class InstancesImportRequest(_message.Message):
    __slots__ = ("import_context",)
    IMPORT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    import_context: ImportContext
    def __init__(self, import_context: _Optional[_Union[ImportContext, _Mapping]] = ...) -> None: ...

class MySqlSyncConfig(_message.Message):
    __slots__ = ("initial_sync_flags",)
    INITIAL_SYNC_FLAGS_FIELD_NUMBER: _ClassVar[int]
    initial_sync_flags: _containers.RepeatedCompositeFieldContainer[SyncFlags]
    def __init__(self, initial_sync_flags: _Optional[_Iterable[_Union[SyncFlags, _Mapping]]] = ...) -> None: ...

class InstancesListResponse(_message.Message):
    __slots__ = ("kind", "warnings", "items", "next_page_token")
    KIND_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    warnings: _containers.RepeatedCompositeFieldContainer[ApiWarning]
    items: _containers.RepeatedCompositeFieldContainer[DatabaseInstance]
    next_page_token: str
    def __init__(self, kind: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[ApiWarning, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[DatabaseInstance, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class InstancesListServerCasResponse(_message.Message):
    __slots__ = ("certs", "active_version", "kind")
    CERTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    certs: _containers.RepeatedCompositeFieldContainer[SslCert]
    active_version: str
    kind: str
    def __init__(self, certs: _Optional[_Iterable[_Union[SslCert, _Mapping]]] = ..., active_version: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class InstancesRestoreBackupRequest(_message.Message):
    __slots__ = ("restore_backup_context",)
    RESTORE_BACKUP_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    restore_backup_context: RestoreBackupContext
    def __init__(self, restore_backup_context: _Optional[_Union[RestoreBackupContext, _Mapping]] = ...) -> None: ...

class InstancesRotateServerCaRequest(_message.Message):
    __slots__ = ("rotate_server_ca_context",)
    ROTATE_SERVER_CA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    rotate_server_ca_context: RotateServerCaContext
    def __init__(self, rotate_server_ca_context: _Optional[_Union[RotateServerCaContext, _Mapping]] = ...) -> None: ...

class InstancesTruncateLogRequest(_message.Message):
    __slots__ = ("truncate_log_context",)
    TRUNCATE_LOG_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    truncate_log_context: TruncateLogContext
    def __init__(self, truncate_log_context: _Optional[_Union[TruncateLogContext, _Mapping]] = ...) -> None: ...

class InstancesAcquireSsrsLeaseRequest(_message.Message):
    __slots__ = ("acquire_ssrs_lease_context",)
    ACQUIRE_SSRS_LEASE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    acquire_ssrs_lease_context: AcquireSsrsLeaseContext
    def __init__(self, acquire_ssrs_lease_context: _Optional[_Union[AcquireSsrsLeaseContext, _Mapping]] = ...) -> None: ...

class PerformDiskShrinkContext(_message.Message):
    __slots__ = ("target_size_gb",)
    TARGET_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    target_size_gb: int
    def __init__(self, target_size_gb: _Optional[int] = ...) -> None: ...

class SqlInstancesGetDiskShrinkConfigResponse(_message.Message):
    __slots__ = ("kind", "minimal_target_size_gb", "message")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MINIMAL_TARGET_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    minimal_target_size_gb: int
    message: str
    def __init__(self, kind: _Optional[str] = ..., minimal_target_size_gb: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class SqlInstancesVerifyExternalSyncSettingsResponse(_message.Message):
    __slots__ = ("kind", "errors", "warnings")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    errors: _containers.RepeatedCompositeFieldContainer[SqlExternalSyncSettingError]
    warnings: _containers.RepeatedCompositeFieldContainer[SqlExternalSyncSettingError]
    def __init__(self, kind: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[SqlExternalSyncSettingError, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[SqlExternalSyncSettingError, _Mapping]]] = ...) -> None: ...

class SqlExternalSyncSettingError(_message.Message):
    __slots__ = ("kind", "type", "detail")
    class SqlExternalSyncSettingErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        CONNECTION_FAILURE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        BINLOG_NOT_ENABLED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INCOMPATIBLE_DATABASE_VERSION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        REPLICA_ALREADY_SETUP: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_PRIVILEGE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_MIGRATION_TYPE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        NO_PGLOGICAL_INSTALLED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PGLOGICAL_NODE_ALREADY_EXISTS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_WAL_LEVEL: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_SHARED_PRELOAD_LIBRARY: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MAX_REPLICATION_SLOTS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MAX_WAL_SENDERS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MAX_WORKER_PROCESSES: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_EXTENSIONS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_RDS_LOGICAL_REPLICATION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_LOGGING_SETUP: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_DB_PARAM: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_GTID_MODE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SQLSERVER_AGENT_NOT_RUNNING: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_TABLE_DEFINITION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_DEFINER: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SQLSERVER_SERVERNAME_MISMATCH: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PRIMARY_ALREADY_SETUP: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_BINLOG_FORMAT: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        BINLOG_RETENTION_SETTING: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_STORAGE_ENGINE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        LIMITED_SUPPORT_TABLES: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        EXISTING_DATA_IN_REPLICA: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        MISSING_OPTIONAL_PRIVILEGES: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        RISKY_BACKUP_ADMIN_PRIVILEGE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_GCS_PERMISSIONS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_FILE_INFO: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_DATABASE_SETTINGS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        LOCAL_INFILE_OFF: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        TURN_ON_PITR_AFTER_PROMOTE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INCOMPATIBLE_DATABASE_MINOR_VERSION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SOURCE_MAX_SUBSCRIPTIONS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNABLE_TO_VERIFY_DEFINERS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SUBSCRIPTION_CALCULATION_STATUS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PG_SUBSCRIPTION_COUNT: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PG_SYNC_PARALLEL_LEVEL: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_DISK_SIZE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MACHINE_TIER: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_EXTENSIONS_NOT_MIGRATED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        EXTENSIONS_NOT_MIGRATED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PG_CRON_FLAG_ENABLED_IN_REPLICA: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        EXTENSIONS_NOT_ENABLED_IN_REPLICA: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
    SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    CONNECTION_FAILURE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    BINLOG_NOT_ENABLED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INCOMPATIBLE_DATABASE_VERSION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    REPLICA_ALREADY_SETUP: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_PRIVILEGE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_MIGRATION_TYPE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    NO_PGLOGICAL_INSTALLED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PGLOGICAL_NODE_ALREADY_EXISTS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_WAL_LEVEL: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_SHARED_PRELOAD_LIBRARY: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MAX_REPLICATION_SLOTS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MAX_WAL_SENDERS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MAX_WORKER_PROCESSES: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_EXTENSIONS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_RDS_LOGICAL_REPLICATION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_LOGGING_SETUP: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_DB_PARAM: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_GTID_MODE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SQLSERVER_AGENT_NOT_RUNNING: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_TABLE_DEFINITION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_DEFINER: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SQLSERVER_SERVERNAME_MISMATCH: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PRIMARY_ALREADY_SETUP: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_BINLOG_FORMAT: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    BINLOG_RETENTION_SETTING: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_STORAGE_ENGINE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    LIMITED_SUPPORT_TABLES: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    EXISTING_DATA_IN_REPLICA: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    MISSING_OPTIONAL_PRIVILEGES: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    RISKY_BACKUP_ADMIN_PRIVILEGE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_GCS_PERMISSIONS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_FILE_INFO: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_DATABASE_SETTINGS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    LOCAL_INFILE_OFF: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    TURN_ON_PITR_AFTER_PROMOTE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INCOMPATIBLE_DATABASE_MINOR_VERSION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SOURCE_MAX_SUBSCRIPTIONS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNABLE_TO_VERIFY_DEFINERS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SUBSCRIPTION_CALCULATION_STATUS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PG_SUBSCRIPTION_COUNT: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PG_SYNC_PARALLEL_LEVEL: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_DISK_SIZE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MACHINE_TIER: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_EXTENSIONS_NOT_MIGRATED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    EXTENSIONS_NOT_MIGRATED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PG_CRON_FLAG_ENABLED_IN_REPLICA: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    EXTENSIONS_NOT_ENABLED_IN_REPLICA: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    KIND_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    kind: str
    type: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    detail: str
    def __init__(self, kind: _Optional[str] = ..., type: _Optional[_Union[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class IpConfiguration(_message.Message):
    __slots__ = ("ipv4_enabled", "private_network", "require_ssl", "authorized_networks", "allocated_ip_range", "enable_private_path_for_google_cloud_services", "ssl_mode", "psc_config")
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
    IPV4_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SSL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATE_PATH_FOR_GOOGLE_CLOUD_SERVICES_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ipv4_enabled: _wrappers_pb2.BoolValue
    private_network: str
    require_ssl: _wrappers_pb2.BoolValue
    authorized_networks: _containers.RepeatedCompositeFieldContainer[AclEntry]
    allocated_ip_range: str
    enable_private_path_for_google_cloud_services: _wrappers_pb2.BoolValue
    ssl_mode: IpConfiguration.SslMode
    psc_config: PscConfig
    def __init__(self, ipv4_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., private_network: _Optional[str] = ..., require_ssl: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., authorized_networks: _Optional[_Iterable[_Union[AclEntry, _Mapping]]] = ..., allocated_ip_range: _Optional[str] = ..., enable_private_path_for_google_cloud_services: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., ssl_mode: _Optional[_Union[IpConfiguration.SslMode, str]] = ..., psc_config: _Optional[_Union[PscConfig, _Mapping]] = ...) -> None: ...

class PscConfig(_message.Message):
    __slots__ = ("psc_enabled", "allowed_consumer_projects")
    PSC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONSUMER_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    psc_enabled: bool
    allowed_consumer_projects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, psc_enabled: bool = ..., allowed_consumer_projects: _Optional[_Iterable[str]] = ...) -> None: ...

class IpMapping(_message.Message):
    __slots__ = ("type", "ip_address", "time_to_retire")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_RETIRE_FIELD_NUMBER: _ClassVar[int]
    type: SqlIpAddressType
    ip_address: str
    time_to_retire: _timestamp_pb2.Timestamp
    def __init__(self, type: _Optional[_Union[SqlIpAddressType, str]] = ..., ip_address: _Optional[str] = ..., time_to_retire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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

class OnPremisesConfiguration(_message.Message):
    __slots__ = ("host_port", "kind", "username", "password", "ca_certificate", "client_certificate", "client_key", "dump_file_path", "source_instance")
    HOST_PORT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    DUMP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    host_port: str
    kind: str
    username: str
    password: str
    ca_certificate: str
    client_certificate: str
    client_key: str
    dump_file_path: str
    source_instance: InstanceReference
    def __init__(self, host_port: _Optional[str] = ..., kind: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., ca_certificate: _Optional[str] = ..., client_certificate: _Optional[str] = ..., client_key: _Optional[str] = ..., dump_file_path: _Optional[str] = ..., source_instance: _Optional[_Union[InstanceReference, _Mapping]] = ...) -> None: ...

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

class OperationsListResponse(_message.Message):
    __slots__ = ("kind", "items", "next_page_token")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[Operation]
    next_page_token: str
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Operation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReplicaConfiguration(_message.Message):
    __slots__ = ("kind", "mysql_replica_configuration", "failover_target", "cascadable_replica")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MYSQL_REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_TARGET_FIELD_NUMBER: _ClassVar[int]
    CASCADABLE_REPLICA_FIELD_NUMBER: _ClassVar[int]
    kind: str
    mysql_replica_configuration: MySqlReplicaConfiguration
    failover_target: _wrappers_pb2.BoolValue
    cascadable_replica: _wrappers_pb2.BoolValue
    def __init__(self, kind: _Optional[str] = ..., mysql_replica_configuration: _Optional[_Union[MySqlReplicaConfiguration, _Mapping]] = ..., failover_target: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., cascadable_replica: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class RestoreBackupContext(_message.Message):
    __slots__ = ("kind", "backup_run_id", "instance_id", "project")
    KIND_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    kind: str
    backup_run_id: int
    instance_id: str
    project: str
    def __init__(self, kind: _Optional[str] = ..., backup_run_id: _Optional[int] = ..., instance_id: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class RotateServerCaContext(_message.Message):
    __slots__ = ("kind", "next_version")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NEXT_VERSION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    next_version: str
    def __init__(self, kind: _Optional[str] = ..., next_version: _Optional[str] = ...) -> None: ...

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

class SslCertsCreateEphemeralRequest(_message.Message):
    __slots__ = ("public_key", "access_token")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    access_token: str
    def __init__(self, public_key: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class SslCertsInsertRequest(_message.Message):
    __slots__ = ("common_name",)
    COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
    common_name: str
    def __init__(self, common_name: _Optional[str] = ...) -> None: ...

class SqlInstancesRescheduleMaintenanceRequestBody(_message.Message):
    __slots__ = ("reschedule",)
    class RescheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESCHEDULE_TYPE_UNSPECIFIED: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
        IMMEDIATE: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
        NEXT_AVAILABLE_WINDOW: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
        SPECIFIC_TIME: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
    RESCHEDULE_TYPE_UNSPECIFIED: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    IMMEDIATE: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    NEXT_AVAILABLE_WINDOW: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    SPECIFIC_TIME: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    class Reschedule(_message.Message):
        __slots__ = ("reschedule_type", "schedule_time")
        RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
        reschedule_type: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
        schedule_time: _timestamp_pb2.Timestamp
        def __init__(self, reschedule_type: _Optional[_Union[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType, str]] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    RESCHEDULE_FIELD_NUMBER: _ClassVar[int]
    reschedule: SqlInstancesRescheduleMaintenanceRequestBody.Reschedule
    def __init__(self, reschedule: _Optional[_Union[SqlInstancesRescheduleMaintenanceRequestBody.Reschedule, _Mapping]] = ...) -> None: ...

class SslCertsInsertResponse(_message.Message):
    __slots__ = ("kind", "operation", "server_ca_cert", "client_cert")
    KIND_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
    kind: str
    operation: Operation
    server_ca_cert: SslCert
    client_cert: SslCertDetail
    def __init__(self, kind: _Optional[str] = ..., operation: _Optional[_Union[Operation, _Mapping]] = ..., server_ca_cert: _Optional[_Union[SslCert, _Mapping]] = ..., client_cert: _Optional[_Union[SslCertDetail, _Mapping]] = ...) -> None: ...

class SslCertsListResponse(_message.Message):
    __slots__ = ("kind", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[SslCert]
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[SslCert, _Mapping]]] = ...) -> None: ...

class TruncateLogContext(_message.Message):
    __slots__ = ("kind", "log_type")
    KIND_FIELD_NUMBER: _ClassVar[int]
    LOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    log_type: str
    def __init__(self, kind: _Optional[str] = ..., log_type: _Optional[str] = ...) -> None: ...

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
