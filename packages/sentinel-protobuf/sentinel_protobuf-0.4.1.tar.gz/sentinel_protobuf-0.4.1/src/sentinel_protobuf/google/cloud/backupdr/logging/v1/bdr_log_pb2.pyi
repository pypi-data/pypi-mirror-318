from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BDRBackupRestoreJobLog(_message.Message):
    __slots__ = ("job_id", "job_category", "job_status", "source_resource_name", "source_resource_id", "restore_resource_name", "backup_name", "resource_type", "start_time", "end_time", "backup_plan_name", "backup_rule", "backup_vault_name", "incremental_backup_size_gib", "error_code", "error_type", "error_message", "backup_consistency_time", "source_resource_location", "restore_resource_location")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RULE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONSISTENCY_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_RESOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    job_category: str
    job_status: str
    source_resource_name: str
    source_resource_id: str
    restore_resource_name: str
    backup_name: str
    resource_type: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    backup_plan_name: str
    backup_rule: str
    backup_vault_name: str
    incremental_backup_size_gib: float
    error_code: int
    error_type: str
    error_message: str
    backup_consistency_time: _timestamp_pb2.Timestamp
    source_resource_location: str
    restore_resource_location: str
    def __init__(self, job_id: _Optional[str] = ..., job_category: _Optional[str] = ..., job_status: _Optional[str] = ..., source_resource_name: _Optional[str] = ..., source_resource_id: _Optional[str] = ..., restore_resource_name: _Optional[str] = ..., backup_name: _Optional[str] = ..., resource_type: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_plan_name: _Optional[str] = ..., backup_rule: _Optional[str] = ..., backup_vault_name: _Optional[str] = ..., incremental_backup_size_gib: _Optional[float] = ..., error_code: _Optional[int] = ..., error_type: _Optional[str] = ..., error_message: _Optional[str] = ..., backup_consistency_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_resource_location: _Optional[str] = ..., restore_resource_location: _Optional[str] = ...) -> None: ...

class BDRProtectedResourceLog(_message.Message):
    __slots__ = ("source_resource_name", "source_resource_id", "resource_type", "source_resource_data_size_gib", "current_backup_plan_name", "current_backup_rule_details", "last_protected_on", "current_backup_vault_name", "source_resource_location")
    SOURCE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_DATA_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BACKUP_PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BACKUP_RULE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LAST_PROTECTED_ON_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BACKUP_VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    source_resource_name: str
    source_resource_id: str
    resource_type: str
    source_resource_data_size_gib: float
    current_backup_plan_name: str
    current_backup_rule_details: _containers.RepeatedCompositeFieldContainer[BackupRuleDetail]
    last_protected_on: _timestamp_pb2.Timestamp
    current_backup_vault_name: str
    source_resource_location: str
    def __init__(self, source_resource_name: _Optional[str] = ..., source_resource_id: _Optional[str] = ..., resource_type: _Optional[str] = ..., source_resource_data_size_gib: _Optional[float] = ..., current_backup_plan_name: _Optional[str] = ..., current_backup_rule_details: _Optional[_Iterable[_Union[BackupRuleDetail, _Mapping]]] = ..., last_protected_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., current_backup_vault_name: _Optional[str] = ..., source_resource_location: _Optional[str] = ...) -> None: ...

class BackupRuleDetail(_message.Message):
    __slots__ = ("rule_name", "retention_days", "recurrence", "recurrence_schedule", "backup_window", "backup_window_timezone")
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    BACKUP_WINDOW_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    rule_name: str
    retention_days: int
    recurrence: str
    recurrence_schedule: str
    backup_window: str
    backup_window_timezone: str
    def __init__(self, rule_name: _Optional[str] = ..., retention_days: _Optional[int] = ..., recurrence: _Optional[str] = ..., recurrence_schedule: _Optional[str] = ..., backup_window: _Optional[str] = ..., backup_window_timezone: _Optional[str] = ...) -> None: ...

class BDRBackupVaultDetailsLog(_message.Message):
    __slots__ = ("backup_vault_name", "source_resource_name", "resource_type", "current_backup_plan_name", "first_available_restore_point", "last_available_restore_point", "stored_bytes_gib", "minimum_enforced_retention_days", "source_resource_location")
    BACKUP_VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BACKUP_PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_AVAILABLE_RESTORE_POINT_FIELD_NUMBER: _ClassVar[int]
    LAST_AVAILABLE_RESTORE_POINT_FIELD_NUMBER: _ClassVar[int]
    STORED_BYTES_GIB_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ENFORCED_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    backup_vault_name: str
    source_resource_name: str
    resource_type: str
    current_backup_plan_name: str
    first_available_restore_point: _timestamp_pb2.Timestamp
    last_available_restore_point: _timestamp_pb2.Timestamp
    stored_bytes_gib: float
    minimum_enforced_retention_days: int
    source_resource_location: str
    def __init__(self, backup_vault_name: _Optional[str] = ..., source_resource_name: _Optional[str] = ..., resource_type: _Optional[str] = ..., current_backup_plan_name: _Optional[str] = ..., first_available_restore_point: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_available_restore_point: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stored_bytes_gib: _Optional[float] = ..., minimum_enforced_retention_days: _Optional[int] = ..., source_resource_location: _Optional[str] = ...) -> None: ...
