from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkebackup.v1 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BackupPlan(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'cluster', 'retention_policy', 'labels', 'backup_schedule', 'etag', 'deactivated', 'backup_config', 'protected_pod_count', 'state', 'state_reason', 'rpo_risk_level', 'rpo_risk_reason')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BackupPlan.State]
        CLUSTER_PENDING: _ClassVar[BackupPlan.State]
        PROVISIONING: _ClassVar[BackupPlan.State]
        READY: _ClassVar[BackupPlan.State]
        FAILED: _ClassVar[BackupPlan.State]
        DEACTIVATED: _ClassVar[BackupPlan.State]
        DELETING: _ClassVar[BackupPlan.State]
    STATE_UNSPECIFIED: BackupPlan.State
    CLUSTER_PENDING: BackupPlan.State
    PROVISIONING: BackupPlan.State
    READY: BackupPlan.State
    FAILED: BackupPlan.State
    DEACTIVATED: BackupPlan.State
    DELETING: BackupPlan.State

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
        __slots__ = ('cron_schedule', 'paused', 'rpo_config', 'next_scheduled_backup_time')
        CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        PAUSED_FIELD_NUMBER: _ClassVar[int]
        RPO_CONFIG_FIELD_NUMBER: _ClassVar[int]
        NEXT_SCHEDULED_BACKUP_TIME_FIELD_NUMBER: _ClassVar[int]
        cron_schedule: str
        paused: bool
        rpo_config: RpoConfig
        next_scheduled_backup_time: _timestamp_pb2.Timestamp

        def __init__(self, cron_schedule: _Optional[str]=..., paused: bool=..., rpo_config: _Optional[_Union[RpoConfig, _Mapping]]=..., next_scheduled_backup_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class BackupConfig(_message.Message):
        __slots__ = ('all_namespaces', 'selected_namespaces', 'selected_applications', 'include_volume_data', 'include_secrets', 'encryption_key', 'permissive_mode')
        ALL_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
        SELECTED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
        SELECTED_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_VOLUME_DATA_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_SECRETS_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        PERMISSIVE_MODE_FIELD_NUMBER: _ClassVar[int]
        all_namespaces: bool
        selected_namespaces: _common_pb2.Namespaces
        selected_applications: _common_pb2.NamespacedNames
        include_volume_data: bool
        include_secrets: bool
        encryption_key: _common_pb2.EncryptionKey
        permissive_mode: bool

        def __init__(self, all_namespaces: bool=..., selected_namespaces: _Optional[_Union[_common_pb2.Namespaces, _Mapping]]=..., selected_applications: _Optional[_Union[_common_pb2.NamespacedNames, _Mapping]]=..., include_volume_data: bool=..., include_secrets: bool=..., encryption_key: _Optional[_Union[_common_pb2.EncryptionKey, _Mapping]]=..., permissive_mode: bool=...) -> None:
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
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_POD_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    RPO_RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RPO_RISK_REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    cluster: str
    retention_policy: BackupPlan.RetentionPolicy
    labels: _containers.ScalarMap[str, str]
    backup_schedule: BackupPlan.Schedule
    etag: str
    deactivated: bool
    backup_config: BackupPlan.BackupConfig
    protected_pod_count: int
    state: BackupPlan.State
    state_reason: str
    rpo_risk_level: int
    rpo_risk_reason: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., cluster: _Optional[str]=..., retention_policy: _Optional[_Union[BackupPlan.RetentionPolicy, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., backup_schedule: _Optional[_Union[BackupPlan.Schedule, _Mapping]]=..., etag: _Optional[str]=..., deactivated: bool=..., backup_config: _Optional[_Union[BackupPlan.BackupConfig, _Mapping]]=..., protected_pod_count: _Optional[int]=..., state: _Optional[_Union[BackupPlan.State, str]]=..., state_reason: _Optional[str]=..., rpo_risk_level: _Optional[int]=..., rpo_risk_reason: _Optional[str]=...) -> None:
        ...

class RpoConfig(_message.Message):
    __slots__ = ('target_rpo_minutes', 'exclusion_windows')
    TARGET_RPO_MINUTES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    target_rpo_minutes: int
    exclusion_windows: _containers.RepeatedCompositeFieldContainer[ExclusionWindow]

    def __init__(self, target_rpo_minutes: _Optional[int]=..., exclusion_windows: _Optional[_Iterable[_Union[ExclusionWindow, _Mapping]]]=...) -> None:
        ...

class ExclusionWindow(_message.Message):
    __slots__ = ('start_time', 'duration', 'single_occurrence_date', 'daily', 'days_of_week')

    class DayOfWeekList(_message.Message):
        __slots__ = ('days_of_week',)
        DAYS_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
        days_of_week: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]

        def __init__(self, days_of_week: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]]=...) -> None:
            ...
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SINGLE_OCCURRENCE_DATE_FIELD_NUMBER: _ClassVar[int]
    DAILY_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    start_time: _timeofday_pb2.TimeOfDay
    duration: _duration_pb2.Duration
    single_occurrence_date: _date_pb2.Date
    daily: bool
    days_of_week: ExclusionWindow.DayOfWeekList

    def __init__(self, start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., single_occurrence_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., daily: bool=..., days_of_week: _Optional[_Union[ExclusionWindow.DayOfWeekList, _Mapping]]=...) -> None:
        ...