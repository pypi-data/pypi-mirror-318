from google.cloud.gkebackup.logging.v1 import logged_common_pb2 as _logged_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LoggedBackupPlan(_message.Message):
    __slots__ = ('description', 'cluster', 'retention_policy', 'labels', 'backup_schedule', 'deactivated', 'backup_config', 'rpo_risk_level')

    class RetentionPolicy(_message.Message):
        __slots__ = ('backup_delete_lock_days', 'backup_retain_days', 'locked')
        BACKUP_DELETE_LOCK_DAYS_FIELD_NUMBER: _ClassVar[int]
        BACKUP_RETAIN_DAYS_FIELD_NUMBER: _ClassVar[int]
        LOCKED_FIELD_NUMBER: _ClassVar[int]
        backup_delete_lock_days: int
        backup_retain_days: int
        locked: bool

        def __init__(self, backup_delete_lock_days: _Optional[int]=..., backup_retain_days: _Optional[int]=..., locked: bool=...) -> None:
            ...

    class Schedule(_message.Message):
        __slots__ = ('cron_schedule', 'paused')
        CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        PAUSED_FIELD_NUMBER: _ClassVar[int]
        cron_schedule: str
        paused: bool

        def __init__(self, cron_schedule: _Optional[str]=..., paused: bool=...) -> None:
            ...

    class BackupConfig(_message.Message):
        __slots__ = ('all_namespaces', 'selected_namespaces', 'selected_applications', 'include_volume_data', 'include_secrets', 'encryption_key')
        ALL_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
        SELECTED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
        SELECTED_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_VOLUME_DATA_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_SECRETS_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        all_namespaces: bool
        selected_namespaces: _logged_common_pb2.Namespaces
        selected_applications: _logged_common_pb2.NamespacedNames
        include_volume_data: bool
        include_secrets: bool
        encryption_key: _logged_common_pb2.EncryptionKey

        def __init__(self, all_namespaces: bool=..., selected_namespaces: _Optional[_Union[_logged_common_pb2.Namespaces, _Mapping]]=..., selected_applications: _Optional[_Union[_logged_common_pb2.NamespacedNames, _Mapping]]=..., include_volume_data: bool=..., include_secrets: bool=..., encryption_key: _Optional[_Union[_logged_common_pb2.EncryptionKey, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RPO_RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    description: str
    cluster: str
    retention_policy: LoggedBackupPlan.RetentionPolicy
    labels: _containers.ScalarMap[str, str]
    backup_schedule: LoggedBackupPlan.Schedule
    deactivated: bool
    backup_config: LoggedBackupPlan.BackupConfig
    rpo_risk_level: int

    def __init__(self, description: _Optional[str]=..., cluster: _Optional[str]=..., retention_policy: _Optional[_Union[LoggedBackupPlan.RetentionPolicy, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., backup_schedule: _Optional[_Union[LoggedBackupPlan.Schedule, _Mapping]]=..., deactivated: bool=..., backup_config: _Optional[_Union[LoggedBackupPlan.BackupConfig, _Mapping]]=..., rpo_risk_level: _Optional[int]=...) -> None:
        ...