from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.oracledatabase.v1 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERATE_TYPE_UNSPECIFIED: _ClassVar[GenerateType]
    ALL: _ClassVar[GenerateType]
    SINGLE: _ClassVar[GenerateType]

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    PROVISIONING: _ClassVar[State]
    AVAILABLE: _ClassVar[State]
    STOPPING: _ClassVar[State]
    STOPPED: _ClassVar[State]
    STARTING: _ClassVar[State]
    TERMINATING: _ClassVar[State]
    TERMINATED: _ClassVar[State]
    UNAVAILABLE: _ClassVar[State]
    RESTORE_IN_PROGRESS: _ClassVar[State]
    RESTORE_FAILED: _ClassVar[State]
    BACKUP_IN_PROGRESS: _ClassVar[State]
    SCALE_IN_PROGRESS: _ClassVar[State]
    AVAILABLE_NEEDS_ATTENTION: _ClassVar[State]
    UPDATING: _ClassVar[State]
    MAINTENANCE_IN_PROGRESS: _ClassVar[State]
    RESTARTING: _ClassVar[State]
    RECREATING: _ClassVar[State]
    ROLE_CHANGE_IN_PROGRESS: _ClassVar[State]
    UPGRADING: _ClassVar[State]
    INACCESSIBLE: _ClassVar[State]
    STANDBY: _ClassVar[State]

class OperationsInsightsState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATIONS_INSIGHTS_STATE_UNSPECIFIED: _ClassVar[OperationsInsightsState]
    ENABLING: _ClassVar[OperationsInsightsState]
    ENABLED: _ClassVar[OperationsInsightsState]
    DISABLING: _ClassVar[OperationsInsightsState]
    NOT_ENABLED: _ClassVar[OperationsInsightsState]
    FAILED_ENABLING: _ClassVar[OperationsInsightsState]
    FAILED_DISABLING: _ClassVar[OperationsInsightsState]

class DBWorkload(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DB_WORKLOAD_UNSPECIFIED: _ClassVar[DBWorkload]
    OLTP: _ClassVar[DBWorkload]
    DW: _ClassVar[DBWorkload]
    AJD: _ClassVar[DBWorkload]
    APEX: _ClassVar[DBWorkload]
GENERATE_TYPE_UNSPECIFIED: GenerateType
ALL: GenerateType
SINGLE: GenerateType
STATE_UNSPECIFIED: State
PROVISIONING: State
AVAILABLE: State
STOPPING: State
STOPPED: State
STARTING: State
TERMINATING: State
TERMINATED: State
UNAVAILABLE: State
RESTORE_IN_PROGRESS: State
RESTORE_FAILED: State
BACKUP_IN_PROGRESS: State
SCALE_IN_PROGRESS: State
AVAILABLE_NEEDS_ATTENTION: State
UPDATING: State
MAINTENANCE_IN_PROGRESS: State
RESTARTING: State
RECREATING: State
ROLE_CHANGE_IN_PROGRESS: State
UPGRADING: State
INACCESSIBLE: State
STANDBY: State
OPERATIONS_INSIGHTS_STATE_UNSPECIFIED: OperationsInsightsState
ENABLING: OperationsInsightsState
ENABLED: OperationsInsightsState
DISABLING: OperationsInsightsState
NOT_ENABLED: OperationsInsightsState
FAILED_ENABLING: OperationsInsightsState
FAILED_DISABLING: OperationsInsightsState
DB_WORKLOAD_UNSPECIFIED: DBWorkload
OLTP: DBWorkload
DW: DBWorkload
AJD: DBWorkload
APEX: DBWorkload

class AutonomousDatabase(_message.Message):
    __slots__ = ("name", "database", "display_name", "entitlement_id", "admin_password", "properties", "labels", "network", "cidr", "create_time")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    database: str
    display_name: str
    entitlement_id: str
    admin_password: str
    properties: AutonomousDatabaseProperties
    labels: _containers.ScalarMap[str, str]
    network: str
    cidr: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., database: _Optional[str] = ..., display_name: _Optional[str] = ..., entitlement_id: _Optional[str] = ..., admin_password: _Optional[str] = ..., properties: _Optional[_Union[AutonomousDatabaseProperties, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., network: _Optional[str] = ..., cidr: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AutonomousDatabaseProperties(_message.Message):
    __slots__ = ("ocid", "compute_count", "cpu_core_count", "data_storage_size_tb", "data_storage_size_gb", "db_workload", "db_edition", "character_set", "n_character_set", "private_endpoint_ip", "private_endpoint_label", "db_version", "is_auto_scaling_enabled", "is_storage_auto_scaling_enabled", "license_type", "customer_contacts", "secret_id", "vault_id", "maintenance_schedule_type", "mtls_connection_required", "backup_retention_period_days", "actual_used_data_storage_size_tb", "allocated_storage_size_tb", "apex_details", "are_primary_allowlisted_ips_used", "lifecycle_details", "state", "autonomous_container_database_id", "available_upgrade_versions", "connection_strings", "connection_urls", "failed_data_recovery_duration", "memory_table_gbs", "is_local_data_guard_enabled", "local_adg_auto_failover_max_data_loss_limit", "local_standby_db", "memory_per_oracle_compute_unit_gbs", "local_disaster_recovery_type", "data_safe_state", "database_management_state", "open_mode", "operations_insights_state", "peer_db_ids", "permission_level", "private_endpoint", "refreshable_mode", "refreshable_state", "role", "scheduled_operation_details", "sql_web_developer_url", "supported_clone_regions", "used_data_storage_size_tbs", "oci_url", "total_auto_backup_storage_size_gbs", "next_long_term_backup_time", "maintenance_begin_time", "maintenance_end_time")
    class DatabaseEdition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_EDITION_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.DatabaseEdition]
        STANDARD_EDITION: _ClassVar[AutonomousDatabaseProperties.DatabaseEdition]
        ENTERPRISE_EDITION: _ClassVar[AutonomousDatabaseProperties.DatabaseEdition]
    DATABASE_EDITION_UNSPECIFIED: AutonomousDatabaseProperties.DatabaseEdition
    STANDARD_EDITION: AutonomousDatabaseProperties.DatabaseEdition
    ENTERPRISE_EDITION: AutonomousDatabaseProperties.DatabaseEdition
    class LicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LICENSE_TYPE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.LicenseType]
        LICENSE_INCLUDED: _ClassVar[AutonomousDatabaseProperties.LicenseType]
        BRING_YOUR_OWN_LICENSE: _ClassVar[AutonomousDatabaseProperties.LicenseType]
    LICENSE_TYPE_UNSPECIFIED: AutonomousDatabaseProperties.LicenseType
    LICENSE_INCLUDED: AutonomousDatabaseProperties.LicenseType
    BRING_YOUR_OWN_LICENSE: AutonomousDatabaseProperties.LicenseType
    class MaintenanceScheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MAINTENANCE_SCHEDULE_TYPE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.MaintenanceScheduleType]
        EARLY: _ClassVar[AutonomousDatabaseProperties.MaintenanceScheduleType]
        REGULAR: _ClassVar[AutonomousDatabaseProperties.MaintenanceScheduleType]
    MAINTENANCE_SCHEDULE_TYPE_UNSPECIFIED: AutonomousDatabaseProperties.MaintenanceScheduleType
    EARLY: AutonomousDatabaseProperties.MaintenanceScheduleType
    REGULAR: AutonomousDatabaseProperties.MaintenanceScheduleType
    class LocalDisasterRecoveryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCAL_DISASTER_RECOVERY_TYPE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.LocalDisasterRecoveryType]
        ADG: _ClassVar[AutonomousDatabaseProperties.LocalDisasterRecoveryType]
        BACKUP_BASED: _ClassVar[AutonomousDatabaseProperties.LocalDisasterRecoveryType]
    LOCAL_DISASTER_RECOVERY_TYPE_UNSPECIFIED: AutonomousDatabaseProperties.LocalDisasterRecoveryType
    ADG: AutonomousDatabaseProperties.LocalDisasterRecoveryType
    BACKUP_BASED: AutonomousDatabaseProperties.LocalDisasterRecoveryType
    class DataSafeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_SAFE_STATE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.DataSafeState]
        REGISTERING: _ClassVar[AutonomousDatabaseProperties.DataSafeState]
        REGISTERED: _ClassVar[AutonomousDatabaseProperties.DataSafeState]
        DEREGISTERING: _ClassVar[AutonomousDatabaseProperties.DataSafeState]
        NOT_REGISTERED: _ClassVar[AutonomousDatabaseProperties.DataSafeState]
        FAILED: _ClassVar[AutonomousDatabaseProperties.DataSafeState]
    DATA_SAFE_STATE_UNSPECIFIED: AutonomousDatabaseProperties.DataSafeState
    REGISTERING: AutonomousDatabaseProperties.DataSafeState
    REGISTERED: AutonomousDatabaseProperties.DataSafeState
    DEREGISTERING: AutonomousDatabaseProperties.DataSafeState
    NOT_REGISTERED: AutonomousDatabaseProperties.DataSafeState
    FAILED: AutonomousDatabaseProperties.DataSafeState
    class DatabaseManagementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_MANAGEMENT_STATE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.DatabaseManagementState]
        ENABLING: _ClassVar[AutonomousDatabaseProperties.DatabaseManagementState]
        ENABLED: _ClassVar[AutonomousDatabaseProperties.DatabaseManagementState]
        DISABLING: _ClassVar[AutonomousDatabaseProperties.DatabaseManagementState]
        NOT_ENABLED: _ClassVar[AutonomousDatabaseProperties.DatabaseManagementState]
        FAILED_ENABLING: _ClassVar[AutonomousDatabaseProperties.DatabaseManagementState]
        FAILED_DISABLING: _ClassVar[AutonomousDatabaseProperties.DatabaseManagementState]
    DATABASE_MANAGEMENT_STATE_UNSPECIFIED: AutonomousDatabaseProperties.DatabaseManagementState
    ENABLING: AutonomousDatabaseProperties.DatabaseManagementState
    ENABLED: AutonomousDatabaseProperties.DatabaseManagementState
    DISABLING: AutonomousDatabaseProperties.DatabaseManagementState
    NOT_ENABLED: AutonomousDatabaseProperties.DatabaseManagementState
    FAILED_ENABLING: AutonomousDatabaseProperties.DatabaseManagementState
    FAILED_DISABLING: AutonomousDatabaseProperties.DatabaseManagementState
    class OpenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPEN_MODE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.OpenMode]
        READ_ONLY: _ClassVar[AutonomousDatabaseProperties.OpenMode]
        READ_WRITE: _ClassVar[AutonomousDatabaseProperties.OpenMode]
    OPEN_MODE_UNSPECIFIED: AutonomousDatabaseProperties.OpenMode
    READ_ONLY: AutonomousDatabaseProperties.OpenMode
    READ_WRITE: AutonomousDatabaseProperties.OpenMode
    class PermissionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSION_LEVEL_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.PermissionLevel]
        RESTRICTED: _ClassVar[AutonomousDatabaseProperties.PermissionLevel]
        UNRESTRICTED: _ClassVar[AutonomousDatabaseProperties.PermissionLevel]
    PERMISSION_LEVEL_UNSPECIFIED: AutonomousDatabaseProperties.PermissionLevel
    RESTRICTED: AutonomousDatabaseProperties.PermissionLevel
    UNRESTRICTED: AutonomousDatabaseProperties.PermissionLevel
    class RefreshableMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REFRESHABLE_MODE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.RefreshableMode]
        AUTOMATIC: _ClassVar[AutonomousDatabaseProperties.RefreshableMode]
        MANUAL: _ClassVar[AutonomousDatabaseProperties.RefreshableMode]
    REFRESHABLE_MODE_UNSPECIFIED: AutonomousDatabaseProperties.RefreshableMode
    AUTOMATIC: AutonomousDatabaseProperties.RefreshableMode
    MANUAL: AutonomousDatabaseProperties.RefreshableMode
    class RefreshableState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REFRESHABLE_STATE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.RefreshableState]
        REFRESHING: _ClassVar[AutonomousDatabaseProperties.RefreshableState]
        NOT_REFRESHING: _ClassVar[AutonomousDatabaseProperties.RefreshableState]
    REFRESHABLE_STATE_UNSPECIFIED: AutonomousDatabaseProperties.RefreshableState
    REFRESHING: AutonomousDatabaseProperties.RefreshableState
    NOT_REFRESHING: AutonomousDatabaseProperties.RefreshableState
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[AutonomousDatabaseProperties.Role]
        PRIMARY: _ClassVar[AutonomousDatabaseProperties.Role]
        STANDBY: _ClassVar[AutonomousDatabaseProperties.Role]
        DISABLED_STANDBY: _ClassVar[AutonomousDatabaseProperties.Role]
        BACKUP_COPY: _ClassVar[AutonomousDatabaseProperties.Role]
        SNAPSHOT_STANDBY: _ClassVar[AutonomousDatabaseProperties.Role]
    ROLE_UNSPECIFIED: AutonomousDatabaseProperties.Role
    PRIMARY: AutonomousDatabaseProperties.Role
    STANDBY: AutonomousDatabaseProperties.Role
    DISABLED_STANDBY: AutonomousDatabaseProperties.Role
    BACKUP_COPY: AutonomousDatabaseProperties.Role
    SNAPSHOT_STANDBY: AutonomousDatabaseProperties.Role
    OCID_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CPU_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_STORAGE_SIZE_TB_FIELD_NUMBER: _ClassVar[int]
    DATA_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DB_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    DB_EDITION_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_SET_FIELD_NUMBER: _ClassVar[int]
    N_CHARACTER_SET_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_IP_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_LABEL_FIELD_NUMBER: _ClassVar[int]
    DB_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_SCALING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_STORAGE_AUTO_SCALING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CONTACTS_FIELD_NUMBER: _ClassVar[int]
    SECRET_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MTLS_CONNECTION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_USED_DATA_STORAGE_SIZE_TB_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_STORAGE_SIZE_TB_FIELD_NUMBER: _ClassVar[int]
    APEX_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ARE_PRIMARY_ALLOWLISTED_IPS_USED_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AUTONOMOUS_CONTAINER_DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_UPGRADE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STRINGS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_URLS_FIELD_NUMBER: _ClassVar[int]
    FAILED_DATA_RECOVERY_DURATION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_TABLE_GBS_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_DATA_GUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADG_AUTO_FAILOVER_MAX_DATA_LOSS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_STANDBY_DB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_PER_ORACLE_COMPUTE_UNIT_GBS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DISASTER_RECOVERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_SAFE_STATE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_MANAGEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_INSIGHTS_STATE_FIELD_NUMBER: _ClassVar[int]
    PEER_DB_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REFRESHABLE_MODE_FIELD_NUMBER: _ClassVar[int]
    REFRESHABLE_STATE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_OPERATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SQL_WEB_DEVELOPER_URL_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLONE_REGIONS_FIELD_NUMBER: _ClassVar[int]
    USED_DATA_STORAGE_SIZE_TBS_FIELD_NUMBER: _ClassVar[int]
    OCI_URL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AUTO_BACKUP_STORAGE_SIZE_GBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_LONG_TERM_BACKUP_TIME_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_END_TIME_FIELD_NUMBER: _ClassVar[int]
    ocid: str
    compute_count: float
    cpu_core_count: int
    data_storage_size_tb: int
    data_storage_size_gb: int
    db_workload: DBWorkload
    db_edition: AutonomousDatabaseProperties.DatabaseEdition
    character_set: str
    n_character_set: str
    private_endpoint_ip: str
    private_endpoint_label: str
    db_version: str
    is_auto_scaling_enabled: bool
    is_storage_auto_scaling_enabled: bool
    license_type: AutonomousDatabaseProperties.LicenseType
    customer_contacts: _containers.RepeatedCompositeFieldContainer[_common_pb2.CustomerContact]
    secret_id: str
    vault_id: str
    maintenance_schedule_type: AutonomousDatabaseProperties.MaintenanceScheduleType
    mtls_connection_required: bool
    backup_retention_period_days: int
    actual_used_data_storage_size_tb: float
    allocated_storage_size_tb: float
    apex_details: AutonomousDatabaseApex
    are_primary_allowlisted_ips_used: bool
    lifecycle_details: str
    state: State
    autonomous_container_database_id: str
    available_upgrade_versions: _containers.RepeatedScalarFieldContainer[str]
    connection_strings: AutonomousDatabaseConnectionStrings
    connection_urls: AutonomousDatabaseConnectionUrls
    failed_data_recovery_duration: _duration_pb2.Duration
    memory_table_gbs: int
    is_local_data_guard_enabled: bool
    local_adg_auto_failover_max_data_loss_limit: int
    local_standby_db: AutonomousDatabaseStandbySummary
    memory_per_oracle_compute_unit_gbs: int
    local_disaster_recovery_type: AutonomousDatabaseProperties.LocalDisasterRecoveryType
    data_safe_state: AutonomousDatabaseProperties.DataSafeState
    database_management_state: AutonomousDatabaseProperties.DatabaseManagementState
    open_mode: AutonomousDatabaseProperties.OpenMode
    operations_insights_state: OperationsInsightsState
    peer_db_ids: _containers.RepeatedScalarFieldContainer[str]
    permission_level: AutonomousDatabaseProperties.PermissionLevel
    private_endpoint: str
    refreshable_mode: AutonomousDatabaseProperties.RefreshableMode
    refreshable_state: AutonomousDatabaseProperties.RefreshableState
    role: AutonomousDatabaseProperties.Role
    scheduled_operation_details: _containers.RepeatedCompositeFieldContainer[ScheduledOperationDetails]
    sql_web_developer_url: str
    supported_clone_regions: _containers.RepeatedScalarFieldContainer[str]
    used_data_storage_size_tbs: int
    oci_url: str
    total_auto_backup_storage_size_gbs: float
    next_long_term_backup_time: _timestamp_pb2.Timestamp
    maintenance_begin_time: _timestamp_pb2.Timestamp
    maintenance_end_time: _timestamp_pb2.Timestamp
    def __init__(self, ocid: _Optional[str] = ..., compute_count: _Optional[float] = ..., cpu_core_count: _Optional[int] = ..., data_storage_size_tb: _Optional[int] = ..., data_storage_size_gb: _Optional[int] = ..., db_workload: _Optional[_Union[DBWorkload, str]] = ..., db_edition: _Optional[_Union[AutonomousDatabaseProperties.DatabaseEdition, str]] = ..., character_set: _Optional[str] = ..., n_character_set: _Optional[str] = ..., private_endpoint_ip: _Optional[str] = ..., private_endpoint_label: _Optional[str] = ..., db_version: _Optional[str] = ..., is_auto_scaling_enabled: bool = ..., is_storage_auto_scaling_enabled: bool = ..., license_type: _Optional[_Union[AutonomousDatabaseProperties.LicenseType, str]] = ..., customer_contacts: _Optional[_Iterable[_Union[_common_pb2.CustomerContact, _Mapping]]] = ..., secret_id: _Optional[str] = ..., vault_id: _Optional[str] = ..., maintenance_schedule_type: _Optional[_Union[AutonomousDatabaseProperties.MaintenanceScheduleType, str]] = ..., mtls_connection_required: bool = ..., backup_retention_period_days: _Optional[int] = ..., actual_used_data_storage_size_tb: _Optional[float] = ..., allocated_storage_size_tb: _Optional[float] = ..., apex_details: _Optional[_Union[AutonomousDatabaseApex, _Mapping]] = ..., are_primary_allowlisted_ips_used: bool = ..., lifecycle_details: _Optional[str] = ..., state: _Optional[_Union[State, str]] = ..., autonomous_container_database_id: _Optional[str] = ..., available_upgrade_versions: _Optional[_Iterable[str]] = ..., connection_strings: _Optional[_Union[AutonomousDatabaseConnectionStrings, _Mapping]] = ..., connection_urls: _Optional[_Union[AutonomousDatabaseConnectionUrls, _Mapping]] = ..., failed_data_recovery_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., memory_table_gbs: _Optional[int] = ..., is_local_data_guard_enabled: bool = ..., local_adg_auto_failover_max_data_loss_limit: _Optional[int] = ..., local_standby_db: _Optional[_Union[AutonomousDatabaseStandbySummary, _Mapping]] = ..., memory_per_oracle_compute_unit_gbs: _Optional[int] = ..., local_disaster_recovery_type: _Optional[_Union[AutonomousDatabaseProperties.LocalDisasterRecoveryType, str]] = ..., data_safe_state: _Optional[_Union[AutonomousDatabaseProperties.DataSafeState, str]] = ..., database_management_state: _Optional[_Union[AutonomousDatabaseProperties.DatabaseManagementState, str]] = ..., open_mode: _Optional[_Union[AutonomousDatabaseProperties.OpenMode, str]] = ..., operations_insights_state: _Optional[_Union[OperationsInsightsState, str]] = ..., peer_db_ids: _Optional[_Iterable[str]] = ..., permission_level: _Optional[_Union[AutonomousDatabaseProperties.PermissionLevel, str]] = ..., private_endpoint: _Optional[str] = ..., refreshable_mode: _Optional[_Union[AutonomousDatabaseProperties.RefreshableMode, str]] = ..., refreshable_state: _Optional[_Union[AutonomousDatabaseProperties.RefreshableState, str]] = ..., role: _Optional[_Union[AutonomousDatabaseProperties.Role, str]] = ..., scheduled_operation_details: _Optional[_Iterable[_Union[ScheduledOperationDetails, _Mapping]]] = ..., sql_web_developer_url: _Optional[str] = ..., supported_clone_regions: _Optional[_Iterable[str]] = ..., used_data_storage_size_tbs: _Optional[int] = ..., oci_url: _Optional[str] = ..., total_auto_backup_storage_size_gbs: _Optional[float] = ..., next_long_term_backup_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., maintenance_begin_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., maintenance_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AutonomousDatabaseApex(_message.Message):
    __slots__ = ("apex_version", "ords_version")
    APEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    ORDS_VERSION_FIELD_NUMBER: _ClassVar[int]
    apex_version: str
    ords_version: str
    def __init__(self, apex_version: _Optional[str] = ..., ords_version: _Optional[str] = ...) -> None: ...

class AutonomousDatabaseConnectionStrings(_message.Message):
    __slots__ = ("all_connection_strings", "dedicated", "high", "low", "medium", "profiles")
    ALL_CONNECTION_STRINGS_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    all_connection_strings: AllConnectionStrings
    dedicated: str
    high: str
    low: str
    medium: str
    profiles: _containers.RepeatedCompositeFieldContainer[DatabaseConnectionStringProfile]
    def __init__(self, all_connection_strings: _Optional[_Union[AllConnectionStrings, _Mapping]] = ..., dedicated: _Optional[str] = ..., high: _Optional[str] = ..., low: _Optional[str] = ..., medium: _Optional[str] = ..., profiles: _Optional[_Iterable[_Union[DatabaseConnectionStringProfile, _Mapping]]] = ...) -> None: ...

class DatabaseConnectionStringProfile(_message.Message):
    __slots__ = ("consumer_group", "display_name", "host_format", "is_regional", "protocol", "session_mode", "syntax_format", "tls_authentication", "value")
    class ConsumerGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONSUMER_GROUP_UNSPECIFIED: _ClassVar[DatabaseConnectionStringProfile.ConsumerGroup]
        HIGH: _ClassVar[DatabaseConnectionStringProfile.ConsumerGroup]
        MEDIUM: _ClassVar[DatabaseConnectionStringProfile.ConsumerGroup]
        LOW: _ClassVar[DatabaseConnectionStringProfile.ConsumerGroup]
        TP: _ClassVar[DatabaseConnectionStringProfile.ConsumerGroup]
        TPURGENT: _ClassVar[DatabaseConnectionStringProfile.ConsumerGroup]
    CONSUMER_GROUP_UNSPECIFIED: DatabaseConnectionStringProfile.ConsumerGroup
    HIGH: DatabaseConnectionStringProfile.ConsumerGroup
    MEDIUM: DatabaseConnectionStringProfile.ConsumerGroup
    LOW: DatabaseConnectionStringProfile.ConsumerGroup
    TP: DatabaseConnectionStringProfile.ConsumerGroup
    TPURGENT: DatabaseConnectionStringProfile.ConsumerGroup
    class HostFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HOST_FORMAT_UNSPECIFIED: _ClassVar[DatabaseConnectionStringProfile.HostFormat]
        FQDN: _ClassVar[DatabaseConnectionStringProfile.HostFormat]
        IP: _ClassVar[DatabaseConnectionStringProfile.HostFormat]
    HOST_FORMAT_UNSPECIFIED: DatabaseConnectionStringProfile.HostFormat
    FQDN: DatabaseConnectionStringProfile.HostFormat
    IP: DatabaseConnectionStringProfile.HostFormat
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROTOCOL_UNSPECIFIED: _ClassVar[DatabaseConnectionStringProfile.Protocol]
        TCP: _ClassVar[DatabaseConnectionStringProfile.Protocol]
        TCPS: _ClassVar[DatabaseConnectionStringProfile.Protocol]
    PROTOCOL_UNSPECIFIED: DatabaseConnectionStringProfile.Protocol
    TCP: DatabaseConnectionStringProfile.Protocol
    TCPS: DatabaseConnectionStringProfile.Protocol
    class SessionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SESSION_MODE_UNSPECIFIED: _ClassVar[DatabaseConnectionStringProfile.SessionMode]
        DIRECT: _ClassVar[DatabaseConnectionStringProfile.SessionMode]
        INDIRECT: _ClassVar[DatabaseConnectionStringProfile.SessionMode]
    SESSION_MODE_UNSPECIFIED: DatabaseConnectionStringProfile.SessionMode
    DIRECT: DatabaseConnectionStringProfile.SessionMode
    INDIRECT: DatabaseConnectionStringProfile.SessionMode
    class SyntaxFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYNTAX_FORMAT_UNSPECIFIED: _ClassVar[DatabaseConnectionStringProfile.SyntaxFormat]
        LONG: _ClassVar[DatabaseConnectionStringProfile.SyntaxFormat]
        EZCONNECT: _ClassVar[DatabaseConnectionStringProfile.SyntaxFormat]
        EZCONNECTPLUS: _ClassVar[DatabaseConnectionStringProfile.SyntaxFormat]
    SYNTAX_FORMAT_UNSPECIFIED: DatabaseConnectionStringProfile.SyntaxFormat
    LONG: DatabaseConnectionStringProfile.SyntaxFormat
    EZCONNECT: DatabaseConnectionStringProfile.SyntaxFormat
    EZCONNECTPLUS: DatabaseConnectionStringProfile.SyntaxFormat
    class TLSAuthentication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TLS_AUTHENTICATION_UNSPECIFIED: _ClassVar[DatabaseConnectionStringProfile.TLSAuthentication]
        SERVER: _ClassVar[DatabaseConnectionStringProfile.TLSAuthentication]
        MUTUAL: _ClassVar[DatabaseConnectionStringProfile.TLSAuthentication]
    TLS_AUTHENTICATION_UNSPECIFIED: DatabaseConnectionStringProfile.TLSAuthentication
    SERVER: DatabaseConnectionStringProfile.TLSAuthentication
    MUTUAL: DatabaseConnectionStringProfile.TLSAuthentication
    CONSUMER_GROUP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_FORMAT_FIELD_NUMBER: _ClassVar[int]
    IS_REGIONAL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SESSION_MODE_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TLS_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    consumer_group: DatabaseConnectionStringProfile.ConsumerGroup
    display_name: str
    host_format: DatabaseConnectionStringProfile.HostFormat
    is_regional: bool
    protocol: DatabaseConnectionStringProfile.Protocol
    session_mode: DatabaseConnectionStringProfile.SessionMode
    syntax_format: DatabaseConnectionStringProfile.SyntaxFormat
    tls_authentication: DatabaseConnectionStringProfile.TLSAuthentication
    value: str
    def __init__(self, consumer_group: _Optional[_Union[DatabaseConnectionStringProfile.ConsumerGroup, str]] = ..., display_name: _Optional[str] = ..., host_format: _Optional[_Union[DatabaseConnectionStringProfile.HostFormat, str]] = ..., is_regional: bool = ..., protocol: _Optional[_Union[DatabaseConnectionStringProfile.Protocol, str]] = ..., session_mode: _Optional[_Union[DatabaseConnectionStringProfile.SessionMode, str]] = ..., syntax_format: _Optional[_Union[DatabaseConnectionStringProfile.SyntaxFormat, str]] = ..., tls_authentication: _Optional[_Union[DatabaseConnectionStringProfile.TLSAuthentication, str]] = ..., value: _Optional[str] = ...) -> None: ...

class AllConnectionStrings(_message.Message):
    __slots__ = ("high", "low", "medium")
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    high: str
    low: str
    medium: str
    def __init__(self, high: _Optional[str] = ..., low: _Optional[str] = ..., medium: _Optional[str] = ...) -> None: ...

class AutonomousDatabaseConnectionUrls(_message.Message):
    __slots__ = ("apex_uri", "database_transforms_uri", "graph_studio_uri", "machine_learning_notebook_uri", "machine_learning_user_management_uri", "mongo_db_uri", "ords_uri", "sql_dev_web_uri")
    APEX_URI_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TRANSFORMS_URI_FIELD_NUMBER: _ClassVar[int]
    GRAPH_STUDIO_URI_FIELD_NUMBER: _ClassVar[int]
    MACHINE_LEARNING_NOTEBOOK_URI_FIELD_NUMBER: _ClassVar[int]
    MACHINE_LEARNING_USER_MANAGEMENT_URI_FIELD_NUMBER: _ClassVar[int]
    MONGO_DB_URI_FIELD_NUMBER: _ClassVar[int]
    ORDS_URI_FIELD_NUMBER: _ClassVar[int]
    SQL_DEV_WEB_URI_FIELD_NUMBER: _ClassVar[int]
    apex_uri: str
    database_transforms_uri: str
    graph_studio_uri: str
    machine_learning_notebook_uri: str
    machine_learning_user_management_uri: str
    mongo_db_uri: str
    ords_uri: str
    sql_dev_web_uri: str
    def __init__(self, apex_uri: _Optional[str] = ..., database_transforms_uri: _Optional[str] = ..., graph_studio_uri: _Optional[str] = ..., machine_learning_notebook_uri: _Optional[str] = ..., machine_learning_user_management_uri: _Optional[str] = ..., mongo_db_uri: _Optional[str] = ..., ords_uri: _Optional[str] = ..., sql_dev_web_uri: _Optional[str] = ...) -> None: ...

class AutonomousDatabaseStandbySummary(_message.Message):
    __slots__ = ("lag_time_duration", "lifecycle_details", "state", "data_guard_role_changed_time", "disaster_recovery_role_changed_time")
    LAG_TIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATA_GUARD_ROLE_CHANGED_TIME_FIELD_NUMBER: _ClassVar[int]
    DISASTER_RECOVERY_ROLE_CHANGED_TIME_FIELD_NUMBER: _ClassVar[int]
    lag_time_duration: _duration_pb2.Duration
    lifecycle_details: str
    state: State
    data_guard_role_changed_time: _timestamp_pb2.Timestamp
    disaster_recovery_role_changed_time: _timestamp_pb2.Timestamp
    def __init__(self, lag_time_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lifecycle_details: _Optional[str] = ..., state: _Optional[_Union[State, str]] = ..., data_guard_role_changed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disaster_recovery_role_changed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScheduledOperationDetails(_message.Message):
    __slots__ = ("day_of_week", "start_time", "stop_time")
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    day_of_week: _dayofweek_pb2.DayOfWeek
    start_time: _timeofday_pb2.TimeOfDay
    stop_time: _timeofday_pb2.TimeOfDay
    def __init__(self, day_of_week: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]] = ..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]] = ..., stop_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]] = ...) -> None: ...
