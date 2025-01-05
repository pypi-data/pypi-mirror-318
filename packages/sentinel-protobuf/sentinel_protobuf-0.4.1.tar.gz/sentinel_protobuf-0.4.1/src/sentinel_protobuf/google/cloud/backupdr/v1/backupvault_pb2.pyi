from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.backupdr.v1 import backupvault_ba_pb2 as _backupvault_ba_pb2
from google.cloud.backupdr.v1 import backupvault_gce_pb2 as _backupvault_gce_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupConfigState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKUP_CONFIG_STATE_UNSPECIFIED: _ClassVar[BackupConfigState]
    ACTIVE: _ClassVar[BackupConfigState]
    PASSIVE: _ClassVar[BackupConfigState]

class BackupView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKUP_VIEW_UNSPECIFIED: _ClassVar[BackupView]
    BACKUP_VIEW_BASIC: _ClassVar[BackupView]
    BACKUP_VIEW_FULL: _ClassVar[BackupView]

class BackupVaultView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKUP_VAULT_VIEW_UNSPECIFIED: _ClassVar[BackupVaultView]
    BACKUP_VAULT_VIEW_BASIC: _ClassVar[BackupVaultView]
    BACKUP_VAULT_VIEW_FULL: _ClassVar[BackupVaultView]
BACKUP_CONFIG_STATE_UNSPECIFIED: BackupConfigState
ACTIVE: BackupConfigState
PASSIVE: BackupConfigState
BACKUP_VIEW_UNSPECIFIED: BackupView
BACKUP_VIEW_BASIC: BackupView
BACKUP_VIEW_FULL: BackupView
BACKUP_VAULT_VIEW_UNSPECIFIED: BackupVaultView
BACKUP_VAULT_VIEW_BASIC: BackupVaultView
BACKUP_VAULT_VIEW_FULL: BackupVaultView

class BackupVault(_message.Message):
    __slots__ = ("name", "description", "labels", "create_time", "update_time", "backup_minimum_enforced_retention_duration", "deletable", "etag", "state", "effective_time", "backup_count", "service_account", "total_stored_bytes", "uid", "annotations", "access_restriction")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BackupVault.State]
        CREATING: _ClassVar[BackupVault.State]
        ACTIVE: _ClassVar[BackupVault.State]
        DELETING: _ClassVar[BackupVault.State]
        ERROR: _ClassVar[BackupVault.State]
    STATE_UNSPECIFIED: BackupVault.State
    CREATING: BackupVault.State
    ACTIVE: BackupVault.State
    DELETING: BackupVault.State
    ERROR: BackupVault.State
    class AccessRestriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_RESTRICTION_UNSPECIFIED: _ClassVar[BackupVault.AccessRestriction]
        WITHIN_PROJECT: _ClassVar[BackupVault.AccessRestriction]
        WITHIN_ORGANIZATION: _ClassVar[BackupVault.AccessRestriction]
        UNRESTRICTED: _ClassVar[BackupVault.AccessRestriction]
    ACCESS_RESTRICTION_UNSPECIFIED: BackupVault.AccessRestriction
    WITHIN_PROJECT: BackupVault.AccessRestriction
    WITHIN_ORGANIZATION: BackupVault.AccessRestriction
    UNRESTRICTED: BackupVault.AccessRestriction
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_MINIMUM_ENFORCED_RETENTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    DELETABLE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STORED_BYTES_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    backup_minimum_enforced_retention_duration: _duration_pb2.Duration
    deletable: bool
    etag: str
    state: BackupVault.State
    effective_time: _timestamp_pb2.Timestamp
    backup_count: int
    service_account: str
    total_stored_bytes: int
    uid: str
    annotations: _containers.ScalarMap[str, str]
    access_restriction: BackupVault.AccessRestriction
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_minimum_enforced_retention_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., deletable: bool = ..., etag: _Optional[str] = ..., state: _Optional[_Union[BackupVault.State, str]] = ..., effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_count: _Optional[int] = ..., service_account: _Optional[str] = ..., total_stored_bytes: _Optional[int] = ..., uid: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., access_restriction: _Optional[_Union[BackupVault.AccessRestriction, str]] = ...) -> None: ...

class DataSource(_message.Message):
    __slots__ = ("name", "state", "labels", "create_time", "update_time", "backup_count", "etag", "total_stored_bytes", "config_state", "backup_config_info", "data_source_gcp_resource", "data_source_backup_appliance_application")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DataSource.State]
        CREATING: _ClassVar[DataSource.State]
        ACTIVE: _ClassVar[DataSource.State]
        DELETING: _ClassVar[DataSource.State]
        ERROR: _ClassVar[DataSource.State]
    STATE_UNSPECIFIED: DataSource.State
    CREATING: DataSource.State
    ACTIVE: DataSource.State
    DELETING: DataSource.State
    ERROR: DataSource.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STORED_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_GCP_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_BACKUP_APPLIANCE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: DataSource.State
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    backup_count: int
    etag: str
    total_stored_bytes: int
    config_state: BackupConfigState
    backup_config_info: BackupConfigInfo
    data_source_gcp_resource: DataSourceGcpResource
    data_source_backup_appliance_application: DataSourceBackupApplianceApplication
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[DataSource.State, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_count: _Optional[int] = ..., etag: _Optional[str] = ..., total_stored_bytes: _Optional[int] = ..., config_state: _Optional[_Union[BackupConfigState, str]] = ..., backup_config_info: _Optional[_Union[BackupConfigInfo, _Mapping]] = ..., data_source_gcp_resource: _Optional[_Union[DataSourceGcpResource, _Mapping]] = ..., data_source_backup_appliance_application: _Optional[_Union[DataSourceBackupApplianceApplication, _Mapping]] = ...) -> None: ...

class BackupConfigInfo(_message.Message):
    __slots__ = ("last_backup_state", "last_successful_backup_consistency_time", "last_backup_error", "gcp_backup_config", "backup_appliance_backup_config")
    class LastBackupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAST_BACKUP_STATE_UNSPECIFIED: _ClassVar[BackupConfigInfo.LastBackupState]
        FIRST_BACKUP_PENDING: _ClassVar[BackupConfigInfo.LastBackupState]
        SUCCEEDED: _ClassVar[BackupConfigInfo.LastBackupState]
        FAILED: _ClassVar[BackupConfigInfo.LastBackupState]
        PERMISSION_DENIED: _ClassVar[BackupConfigInfo.LastBackupState]
    LAST_BACKUP_STATE_UNSPECIFIED: BackupConfigInfo.LastBackupState
    FIRST_BACKUP_PENDING: BackupConfigInfo.LastBackupState
    SUCCEEDED: BackupConfigInfo.LastBackupState
    FAILED: BackupConfigInfo.LastBackupState
    PERMISSION_DENIED: BackupConfigInfo.LastBackupState
    LAST_BACKUP_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_BACKUP_CONSISTENCY_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    GCP_BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APPLIANCE_BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    last_backup_state: BackupConfigInfo.LastBackupState
    last_successful_backup_consistency_time: _timestamp_pb2.Timestamp
    last_backup_error: _status_pb2.Status
    gcp_backup_config: GcpBackupConfig
    backup_appliance_backup_config: BackupApplianceBackupConfig
    def __init__(self, last_backup_state: _Optional[_Union[BackupConfigInfo.LastBackupState, str]] = ..., last_successful_backup_consistency_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_backup_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., gcp_backup_config: _Optional[_Union[GcpBackupConfig, _Mapping]] = ..., backup_appliance_backup_config: _Optional[_Union[BackupApplianceBackupConfig, _Mapping]] = ...) -> None: ...

class GcpBackupConfig(_message.Message):
    __slots__ = ("backup_plan", "backup_plan_description", "backup_plan_association", "backup_plan_rules")
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_RULES_FIELD_NUMBER: _ClassVar[int]
    backup_plan: str
    backup_plan_description: str
    backup_plan_association: str
    backup_plan_rules: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backup_plan: _Optional[str] = ..., backup_plan_description: _Optional[str] = ..., backup_plan_association: _Optional[str] = ..., backup_plan_rules: _Optional[_Iterable[str]] = ...) -> None: ...

class BackupApplianceBackupConfig(_message.Message):
    __slots__ = ("backup_appliance_name", "backup_appliance_id", "sla_id", "application_name", "host_name", "slt_name", "slp_name")
    BACKUP_APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SLA_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    SLT_NAME_FIELD_NUMBER: _ClassVar[int]
    SLP_NAME_FIELD_NUMBER: _ClassVar[int]
    backup_appliance_name: str
    backup_appliance_id: int
    sla_id: int
    application_name: str
    host_name: str
    slt_name: str
    slp_name: str
    def __init__(self, backup_appliance_name: _Optional[str] = ..., backup_appliance_id: _Optional[int] = ..., sla_id: _Optional[int] = ..., application_name: _Optional[str] = ..., host_name: _Optional[str] = ..., slt_name: _Optional[str] = ..., slp_name: _Optional[str] = ...) -> None: ...

class DataSourceGcpResource(_message.Message):
    __slots__ = ("gcp_resourcename", "location", "type", "compute_instance_datasource_properties")
    GCP_RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_INSTANCE_DATASOURCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    gcp_resourcename: str
    location: str
    type: str
    compute_instance_datasource_properties: _backupvault_gce_pb2.ComputeInstanceDataSourceProperties
    def __init__(self, gcp_resourcename: _Optional[str] = ..., location: _Optional[str] = ..., type: _Optional[str] = ..., compute_instance_datasource_properties: _Optional[_Union[_backupvault_gce_pb2.ComputeInstanceDataSourceProperties, _Mapping]] = ...) -> None: ...

class DataSourceBackupApplianceApplication(_message.Message):
    __slots__ = ("application_name", "backup_appliance", "appliance_id", "type", "application_id", "hostname", "host_id")
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APPLIANCE_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    application_name: str
    backup_appliance: str
    appliance_id: int
    type: str
    application_id: int
    hostname: str
    host_id: int
    def __init__(self, application_name: _Optional[str] = ..., backup_appliance: _Optional[str] = ..., appliance_id: _Optional[int] = ..., type: _Optional[str] = ..., application_id: _Optional[int] = ..., hostname: _Optional[str] = ..., host_id: _Optional[int] = ...) -> None: ...

class ServiceLockInfo(_message.Message):
    __slots__ = ("operation",)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: str
    def __init__(self, operation: _Optional[str] = ...) -> None: ...

class BackupApplianceLockInfo(_message.Message):
    __slots__ = ("backup_appliance_id", "backup_appliance_name", "lock_reason", "job_name", "backup_image", "sla_id")
    BACKUP_APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCK_REASON_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_IMAGE_FIELD_NUMBER: _ClassVar[int]
    SLA_ID_FIELD_NUMBER: _ClassVar[int]
    backup_appliance_id: int
    backup_appliance_name: str
    lock_reason: str
    job_name: str
    backup_image: str
    sla_id: int
    def __init__(self, backup_appliance_id: _Optional[int] = ..., backup_appliance_name: _Optional[str] = ..., lock_reason: _Optional[str] = ..., job_name: _Optional[str] = ..., backup_image: _Optional[str] = ..., sla_id: _Optional[int] = ...) -> None: ...

class BackupLock(_message.Message):
    __slots__ = ("lock_until_time", "backup_appliance_lock_info", "service_lock_info")
    LOCK_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APPLIANCE_LOCK_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LOCK_INFO_FIELD_NUMBER: _ClassVar[int]
    lock_until_time: _timestamp_pb2.Timestamp
    backup_appliance_lock_info: BackupApplianceLockInfo
    service_lock_info: ServiceLockInfo
    def __init__(self, lock_until_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_appliance_lock_info: _Optional[_Union[BackupApplianceLockInfo, _Mapping]] = ..., service_lock_info: _Optional[_Union[ServiceLockInfo, _Mapping]] = ...) -> None: ...

class Backup(_message.Message):
    __slots__ = ("name", "description", "create_time", "update_time", "labels", "enforced_retention_end_time", "expire_time", "consistency_time", "etag", "state", "service_locks", "backup_appliance_locks", "compute_instance_backup_properties", "backup_appliance_backup_properties", "backup_type", "gcp_backup_plan_info", "resource_size_bytes")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        ACTIVE: _ClassVar[Backup.State]
        DELETING: _ClassVar[Backup.State]
        ERROR: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    ACTIVE: Backup.State
    DELETING: Backup.State
    ERROR: Backup.State
    class BackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BACKUP_TYPE_UNSPECIFIED: _ClassVar[Backup.BackupType]
        SCHEDULED: _ClassVar[Backup.BackupType]
        ON_DEMAND: _ClassVar[Backup.BackupType]
    BACKUP_TYPE_UNSPECIFIED: Backup.BackupType
    SCHEDULED: Backup.BackupType
    ON_DEMAND: Backup.BackupType
    class GCPBackupPlanInfo(_message.Message):
        __slots__ = ("backup_plan", "backup_plan_rule_id")
        BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
        BACKUP_PLAN_RULE_ID_FIELD_NUMBER: _ClassVar[int]
        backup_plan: str
        backup_plan_rule_id: str
        def __init__(self, backup_plan: _Optional[str] = ..., backup_plan_rule_id: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENFORCED_RETENTION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LOCKS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APPLIANCE_LOCKS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_INSTANCE_BACKUP_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APPLIANCE_BACKUP_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GCP_BACKUP_PLAN_INFO_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    enforced_retention_end_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    consistency_time: _timestamp_pb2.Timestamp
    etag: str
    state: Backup.State
    service_locks: _containers.RepeatedCompositeFieldContainer[BackupLock]
    backup_appliance_locks: _containers.RepeatedCompositeFieldContainer[BackupLock]
    compute_instance_backup_properties: _backupvault_gce_pb2.ComputeInstanceBackupProperties
    backup_appliance_backup_properties: _backupvault_ba_pb2.BackupApplianceBackupProperties
    backup_type: Backup.BackupType
    gcp_backup_plan_info: Backup.GCPBackupPlanInfo
    resource_size_bytes: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., enforced_retention_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., consistency_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., state: _Optional[_Union[Backup.State, str]] = ..., service_locks: _Optional[_Iterable[_Union[BackupLock, _Mapping]]] = ..., backup_appliance_locks: _Optional[_Iterable[_Union[BackupLock, _Mapping]]] = ..., compute_instance_backup_properties: _Optional[_Union[_backupvault_gce_pb2.ComputeInstanceBackupProperties, _Mapping]] = ..., backup_appliance_backup_properties: _Optional[_Union[_backupvault_ba_pb2.BackupApplianceBackupProperties, _Mapping]] = ..., backup_type: _Optional[_Union[Backup.BackupType, str]] = ..., gcp_backup_plan_info: _Optional[_Union[Backup.GCPBackupPlanInfo, _Mapping]] = ..., resource_size_bytes: _Optional[int] = ...) -> None: ...

class CreateBackupVaultRequest(_message.Message):
    __slots__ = ("parent", "backup_vault_id", "backup_vault", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_vault_id: str
    backup_vault: BackupVault
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., backup_vault_id: _Optional[str] = ..., backup_vault: _Optional[_Union[BackupVault, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class ListBackupVaultsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "view")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: BackupVaultView
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., view: _Optional[_Union[BackupVaultView, str]] = ...) -> None: ...

class ListBackupVaultsResponse(_message.Message):
    __slots__ = ("backup_vaults", "next_page_token", "unreachable")
    BACKUP_VAULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_vaults: _containers.RepeatedCompositeFieldContainer[BackupVault]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backup_vaults: _Optional[_Iterable[_Union[BackupVault, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchUsableBackupVaultsRequest(_message.Message):
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

class FetchUsableBackupVaultsResponse(_message.Message):
    __slots__ = ("backup_vaults", "next_page_token", "unreachable")
    BACKUP_VAULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_vaults: _containers.RepeatedCompositeFieldContainer[BackupVault]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backup_vaults: _Optional[_Iterable[_Union[BackupVault, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBackupVaultRequest(_message.Message):
    __slots__ = ("name", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: BackupVaultView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[BackupVaultView, str]] = ...) -> None: ...

class UpdateBackupVaultRequest(_message.Message):
    __slots__ = ("update_mask", "backup_vault", "request_id", "validate_only", "force")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    backup_vault: BackupVault
    request_id: str
    validate_only: bool
    force: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., backup_vault: _Optional[_Union[BackupVault, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., force: bool = ...) -> None: ...

class DeleteBackupVaultRequest(_message.Message):
    __slots__ = ("name", "request_id", "force", "etag", "validate_only", "allow_missing")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    etag: str
    validate_only: bool
    allow_missing: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ..., etag: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ...) -> None: ...

class ListDataSourcesRequest(_message.Message):
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

class ListDataSourcesResponse(_message.Message):
    __slots__ = ("data_sources", "next_page_token", "unreachable")
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDataSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateDataSourceRequest(_message.Message):
    __slots__ = ("update_mask", "data_source", "request_id", "allow_missing")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    data_source: DataSource
    request_id: str
    allow_missing: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., data_source: _Optional[_Union[DataSource, _Mapping]] = ..., request_id: _Optional[str] = ..., allow_missing: bool = ...) -> None: ...

class ListBackupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "view")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: BackupView
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., view: _Optional[_Union[BackupView, str]] = ...) -> None: ...

class ListBackupsResponse(_message.Message):
    __slots__ = ("backups", "next_page_token", "unreachable")
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[Backup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backups: _Optional[_Iterable[_Union[Backup, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBackupRequest(_message.Message):
    __slots__ = ("name", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: BackupView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[BackupView, str]] = ...) -> None: ...

class UpdateBackupRequest(_message.Message):
    __slots__ = ("update_mask", "backup", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    backup: Backup
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., backup: _Optional[_Union[Backup, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class RestoreBackupRequest(_message.Message):
    __slots__ = ("name", "request_id", "compute_instance_target_environment", "compute_instance_restore_properties")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_INSTANCE_TARGET_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_INSTANCE_RESTORE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    compute_instance_target_environment: _backupvault_gce_pb2.ComputeInstanceTargetEnvironment
    compute_instance_restore_properties: _backupvault_gce_pb2.ComputeInstanceRestoreProperties
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., compute_instance_target_environment: _Optional[_Union[_backupvault_gce_pb2.ComputeInstanceTargetEnvironment, _Mapping]] = ..., compute_instance_restore_properties: _Optional[_Union[_backupvault_gce_pb2.ComputeInstanceRestoreProperties, _Mapping]] = ...) -> None: ...

class RestoreBackupResponse(_message.Message):
    __slots__ = ("target_resource",)
    TARGET_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    target_resource: TargetResource
    def __init__(self, target_resource: _Optional[_Union[TargetResource, _Mapping]] = ...) -> None: ...

class TargetResource(_message.Message):
    __slots__ = ("gcp_resource",)
    GCP_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    gcp_resource: GcpResource
    def __init__(self, gcp_resource: _Optional[_Union[GcpResource, _Mapping]] = ...) -> None: ...

class GcpResource(_message.Message):
    __slots__ = ("gcp_resourcename", "location", "type")
    GCP_RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    gcp_resourcename: str
    location: str
    type: str
    def __init__(self, gcp_resourcename: _Optional[str] = ..., location: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
