from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.spanner.admin.database.v1 import backup_pb2 as _backup_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BackupScheduleSpec(_message.Message):
    __slots__ = ('cron_spec',)
    CRON_SPEC_FIELD_NUMBER: _ClassVar[int]
    cron_spec: CrontabSpec

    def __init__(self, cron_spec: _Optional[_Union[CrontabSpec, _Mapping]]=...) -> None:
        ...

class BackupSchedule(_message.Message):
    __slots__ = ('name', 'spec', 'retention_duration', 'encryption_config', 'full_backup_spec', 'incremental_backup_spec', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_SPEC_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_SPEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    spec: BackupScheduleSpec
    retention_duration: _duration_pb2.Duration
    encryption_config: _backup_pb2.CreateBackupEncryptionConfig
    full_backup_spec: _backup_pb2.FullBackupSpec
    incremental_backup_spec: _backup_pb2.IncrementalBackupSpec
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., spec: _Optional[_Union[BackupScheduleSpec, _Mapping]]=..., retention_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., encryption_config: _Optional[_Union[_backup_pb2.CreateBackupEncryptionConfig, _Mapping]]=..., full_backup_spec: _Optional[_Union[_backup_pb2.FullBackupSpec, _Mapping]]=..., incremental_backup_spec: _Optional[_Union[_backup_pb2.IncrementalBackupSpec, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CrontabSpec(_message.Message):
    __slots__ = ('text', 'time_zone', 'creation_window')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CREATION_WINDOW_FIELD_NUMBER: _ClassVar[int]
    text: str
    time_zone: str
    creation_window: _duration_pb2.Duration

    def __init__(self, text: _Optional[str]=..., time_zone: _Optional[str]=..., creation_window: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class CreateBackupScheduleRequest(_message.Message):
    __slots__ = ('parent', 'backup_schedule_id', 'backup_schedule')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_schedule_id: str
    backup_schedule: BackupSchedule

    def __init__(self, parent: _Optional[str]=..., backup_schedule_id: _Optional[str]=..., backup_schedule: _Optional[_Union[BackupSchedule, _Mapping]]=...) -> None:
        ...

class GetBackupScheduleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteBackupScheduleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBackupSchedulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBackupSchedulesResponse(_message.Message):
    __slots__ = ('backup_schedules', 'next_page_token')
    BACKUP_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    backup_schedules: _containers.RepeatedCompositeFieldContainer[BackupSchedule]
    next_page_token: str

    def __init__(self, backup_schedules: _Optional[_Iterable[_Union[BackupSchedule, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateBackupScheduleRequest(_message.Message):
    __slots__ = ('backup_schedule', 'update_mask')
    BACKUP_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    backup_schedule: BackupSchedule
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, backup_schedule: _Optional[_Union[BackupSchedule, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...