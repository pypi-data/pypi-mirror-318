from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class BackupRecoveryJobReportLog(_message.Message):
    __slots__ = ('job_name', 'job_category', 'job_type', 'log_backup', 'job_status', 'resource_name', 'resource_type', 'error_code', 'error_message', 'job_initiation_failure_reason', 'job_start_time', 'job_end_time', 'job_queued_time', 'job_duration_in_hours', 'hostname', 'appliance_name', 'backup_rule_policy_name', 'backup_plan_policy_template', 'backup_type', 'recovery_point', 'backup_consistency', 'target_host_name', 'target_appliance_name', 'target_pool_name', 'resource_data_size_in_gib', 'data_copied_in_gib', 'onvault_pool_storage_consumed_in_gib', 'pre_compress_in_gib', 'compression_ratio', 'data_change_rate', 'snapshot_disk_size_in_gib', 'data_written_in_gib', 'data_sent_in_gib', 'job_id', 'host_id', 'backup_rule_policy_id', 'resource_id', 'target_pool_id', 'target_host_id', 'target_appliance_id')
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    JOB_INITIATION_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_END_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_QUEUED_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_DURATION_IN_HOURS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RULE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_POLICY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_POINT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_POOL_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_DATA_SIZE_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    DATA_COPIED_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    ONVAULT_POOL_STORAGE_CONSUMED_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    PRE_COMPRESS_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_RATIO_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANGE_RATE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DISK_SIZE_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    DATA_SENT_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RULE_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    job_category: str
    job_type: str
    log_backup: str
    job_status: str
    resource_name: str
    resource_type: str
    error_code: int
    error_message: str
    job_initiation_failure_reason: str
    job_start_time: str
    job_end_time: str
    job_queued_time: str
    job_duration_in_hours: float
    hostname: str
    appliance_name: str
    backup_rule_policy_name: str
    backup_plan_policy_template: str
    backup_type: str
    recovery_point: str
    backup_consistency: str
    target_host_name: str
    target_appliance_name: str
    target_pool_name: str
    resource_data_size_in_gib: float
    data_copied_in_gib: float
    onvault_pool_storage_consumed_in_gib: float
    pre_compress_in_gib: float
    compression_ratio: float
    data_change_rate: float
    snapshot_disk_size_in_gib: float
    data_written_in_gib: float
    data_sent_in_gib: float
    job_id: str
    host_id: str
    backup_rule_policy_id: str
    resource_id: str
    target_pool_id: str
    target_host_id: str
    target_appliance_id: str

    def __init__(self, job_name: _Optional[str]=..., job_category: _Optional[str]=..., job_type: _Optional[str]=..., log_backup: _Optional[str]=..., job_status: _Optional[str]=..., resource_name: _Optional[str]=..., resource_type: _Optional[str]=..., error_code: _Optional[int]=..., error_message: _Optional[str]=..., job_initiation_failure_reason: _Optional[str]=..., job_start_time: _Optional[str]=..., job_end_time: _Optional[str]=..., job_queued_time: _Optional[str]=..., job_duration_in_hours: _Optional[float]=..., hostname: _Optional[str]=..., appliance_name: _Optional[str]=..., backup_rule_policy_name: _Optional[str]=..., backup_plan_policy_template: _Optional[str]=..., backup_type: _Optional[str]=..., recovery_point: _Optional[str]=..., backup_consistency: _Optional[str]=..., target_host_name: _Optional[str]=..., target_appliance_name: _Optional[str]=..., target_pool_name: _Optional[str]=..., resource_data_size_in_gib: _Optional[float]=..., data_copied_in_gib: _Optional[float]=..., onvault_pool_storage_consumed_in_gib: _Optional[float]=..., pre_compress_in_gib: _Optional[float]=..., compression_ratio: _Optional[float]=..., data_change_rate: _Optional[float]=..., snapshot_disk_size_in_gib: _Optional[float]=..., data_written_in_gib: _Optional[float]=..., data_sent_in_gib: _Optional[float]=..., job_id: _Optional[str]=..., host_id: _Optional[str]=..., backup_rule_policy_id: _Optional[str]=..., resource_id: _Optional[str]=..., target_pool_id: _Optional[str]=..., target_host_id: _Optional[str]=..., target_appliance_id: _Optional[str]=...) -> None:
        ...

class UnprotectedResourceReportLog(_message.Message):
    __slots__ = ('host_name', 'resource_name', 'resource_type', 'instance_name', 'discovered_on', 'discovered_by', 'appliance_id', 'resource_id', 'host_id')
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_ON_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_BY_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    resource_name: str
    resource_type: str
    instance_name: str
    discovered_on: str
    discovered_by: str
    appliance_id: str
    resource_id: str
    host_id: str

    def __init__(self, host_name: _Optional[str]=..., resource_name: _Optional[str]=..., resource_type: _Optional[str]=..., instance_name: _Optional[str]=..., discovered_on: _Optional[str]=..., discovered_by: _Optional[str]=..., appliance_id: _Optional[str]=..., resource_id: _Optional[str]=..., host_id: _Optional[str]=...) -> None:
        ...

class DailyScheduleComplianceReportLog(_message.Message):
    __slots__ = ('resource_name', 'resource_type', 'backup_rule_policy_name', 'backup_plan_policy_template', 'host_name', 'appliance_name', 'date', 'backup_window_start_time', 'job_type', 'status', 'comment', 'resource_id', 'host_id', 'backup_plan_policy_template_id', 'backup_rule_policy_id', 'appliance_id')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RULE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_POLICY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_WINDOW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_POLICY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RULE_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    resource_type: str
    backup_rule_policy_name: str
    backup_plan_policy_template: str
    host_name: str
    appliance_name: str
    date: str
    backup_window_start_time: str
    job_type: str
    status: str
    comment: str
    resource_id: str
    host_id: str
    backup_plan_policy_template_id: str
    backup_rule_policy_id: str
    appliance_id: str

    def __init__(self, resource_name: _Optional[str]=..., resource_type: _Optional[str]=..., backup_rule_policy_name: _Optional[str]=..., backup_plan_policy_template: _Optional[str]=..., host_name: _Optional[str]=..., appliance_name: _Optional[str]=..., date: _Optional[str]=..., backup_window_start_time: _Optional[str]=..., job_type: _Optional[str]=..., status: _Optional[str]=..., comment: _Optional[str]=..., resource_id: _Optional[str]=..., host_id: _Optional[str]=..., backup_plan_policy_template_id: _Optional[str]=..., backup_rule_policy_id: _Optional[str]=..., appliance_id: _Optional[str]=...) -> None:
        ...

class BackupStorageUtilizationReportLog(_message.Message):
    __slots__ = ('appliance_name', 'storage_type', 'pool_name', 'total_capacity_in_gib', 'used_capacity_in_gib', 'utilization_percentage', 'appliance_id')
    APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CAPACITY_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    USED_CAPACITY_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    appliance_name: str
    storage_type: str
    pool_name: str
    total_capacity_in_gib: float
    used_capacity_in_gib: float
    utilization_percentage: float
    appliance_id: str

    def __init__(self, appliance_name: _Optional[str]=..., storage_type: _Optional[str]=..., pool_name: _Optional[str]=..., total_capacity_in_gib: _Optional[float]=..., used_capacity_in_gib: _Optional[float]=..., utilization_percentage: _Optional[float]=..., appliance_id: _Optional[str]=...) -> None:
        ...

class ProtectedResource(_message.Message):
    __slots__ = ('resource_name', 'resource_type', 'resource_id', 'backup_inclusion_or_exclusion', 'host_id', 'host_name', 'backup_plan_policy_template_id', 'backup_plan_policy_template', 'sla_id', 'backup_plan_restrictions', 'protected_on', 'policy_overrides', 'source_appliance', 'source_appliance_id', 'protected_data_in_gib', 'onvault_in_gib', 'appliance_name', 'appliance_id', 'remote_appliance', 'remote_appliance_id', 'recovery_point')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INCLUSION_OR_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_POLICY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_POLICY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SLA_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_ON_FIELD_NUMBER: _ClassVar[int]
    POLICY_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APPLIANCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_DATA_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    ONVAULT_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_APPLIANCE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_POINT_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    resource_type: str
    resource_id: str
    backup_inclusion_or_exclusion: str
    host_id: str
    host_name: str
    backup_plan_policy_template_id: str
    backup_plan_policy_template: str
    sla_id: str
    backup_plan_restrictions: str
    protected_on: str
    policy_overrides: str
    source_appliance: str
    source_appliance_id: str
    protected_data_in_gib: float
    onvault_in_gib: float
    appliance_name: str
    appliance_id: str
    remote_appliance: str
    remote_appliance_id: str
    recovery_point: str

    def __init__(self, resource_name: _Optional[str]=..., resource_type: _Optional[str]=..., resource_id: _Optional[str]=..., backup_inclusion_or_exclusion: _Optional[str]=..., host_id: _Optional[str]=..., host_name: _Optional[str]=..., backup_plan_policy_template_id: _Optional[str]=..., backup_plan_policy_template: _Optional[str]=..., sla_id: _Optional[str]=..., backup_plan_restrictions: _Optional[str]=..., protected_on: _Optional[str]=..., policy_overrides: _Optional[str]=..., source_appliance: _Optional[str]=..., source_appliance_id: _Optional[str]=..., protected_data_in_gib: _Optional[float]=..., onvault_in_gib: _Optional[float]=..., appliance_name: _Optional[str]=..., appliance_id: _Optional[str]=..., remote_appliance: _Optional[str]=..., remote_appliance_id: _Optional[str]=..., recovery_point: _Optional[str]=...) -> None:
        ...

class MountedImage(_message.Message):
    __slots__ = ('source_resource_name', 'source_resource_id', 'appliance_name', 'appliance_id', 'mounted_image_name', 'source_image_name', 'source_image_type', 'recovery_point_date', 'last_mount_date', 'resource_type', 'source_host_name', 'source_host_id', 'mounted_host_name', 'mounted_host_id', 'mounted_resource_name', 'resource_virtual_size_in_gib', 'storage_consumed_in_gib', 'mounted_resource_label', 'restorable_object', 'mounted_image_age_in_days', 'user_name', 'read_mode', 'resource_size_in_gib', 'image_expiration_date')
    SOURCE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_POINT_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_MOUNT_DATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HOST_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_HOST_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VIRTUAL_SIZE_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONSUMED_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_RESOURCE_LABEL_FIELD_NUMBER: _ClassVar[int]
    RESTORABLE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_IMAGE_AGE_IN_DAYS_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MODE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SIZE_IN_GIB_FIELD_NUMBER: _ClassVar[int]
    IMAGE_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    source_resource_name: str
    source_resource_id: str
    appliance_name: str
    appliance_id: str
    mounted_image_name: str
    source_image_name: str
    source_image_type: str
    recovery_point_date: str
    last_mount_date: str
    resource_type: str
    source_host_name: str
    source_host_id: str
    mounted_host_name: str
    mounted_host_id: str
    mounted_resource_name: str
    resource_virtual_size_in_gib: float
    storage_consumed_in_gib: float
    mounted_resource_label: str
    restorable_object: str
    mounted_image_age_in_days: int
    user_name: str
    read_mode: str
    resource_size_in_gib: float
    image_expiration_date: str

    def __init__(self, source_resource_name: _Optional[str]=..., source_resource_id: _Optional[str]=..., appliance_name: _Optional[str]=..., appliance_id: _Optional[str]=..., mounted_image_name: _Optional[str]=..., source_image_name: _Optional[str]=..., source_image_type: _Optional[str]=..., recovery_point_date: _Optional[str]=..., last_mount_date: _Optional[str]=..., resource_type: _Optional[str]=..., source_host_name: _Optional[str]=..., source_host_id: _Optional[str]=..., mounted_host_name: _Optional[str]=..., mounted_host_id: _Optional[str]=..., mounted_resource_name: _Optional[str]=..., resource_virtual_size_in_gib: _Optional[float]=..., storage_consumed_in_gib: _Optional[float]=..., mounted_resource_label: _Optional[str]=..., restorable_object: _Optional[str]=..., mounted_image_age_in_days: _Optional[int]=..., user_name: _Optional[str]=..., read_mode: _Optional[str]=..., resource_size_in_gib: _Optional[float]=..., image_expiration_date: _Optional[str]=...) -> None:
        ...

class ConnectorVersionReportLog(_message.Message):
    __slots__ = ('appliance_name', 'appliance_id', 'host_name', 'host_id', 'host_os_type', 'host_ip_address', 'db_authentication', 'installed_version', 'available_version', 'version_check', 'disk_preference', 'transport')
    APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DB_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_CHECK_FIELD_NUMBER: _ClassVar[int]
    DISK_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    appliance_name: str
    appliance_id: str
    host_name: str
    host_id: str
    host_os_type: str
    host_ip_address: str
    db_authentication: str
    installed_version: str
    available_version: str
    version_check: str
    disk_preference: str
    transport: str

    def __init__(self, appliance_name: _Optional[str]=..., appliance_id: _Optional[str]=..., host_name: _Optional[str]=..., host_id: _Optional[str]=..., host_os_type: _Optional[str]=..., host_ip_address: _Optional[str]=..., db_authentication: _Optional[str]=..., installed_version: _Optional[str]=..., available_version: _Optional[str]=..., version_check: _Optional[str]=..., disk_preference: _Optional[str]=..., transport: _Optional[str]=...) -> None:
        ...