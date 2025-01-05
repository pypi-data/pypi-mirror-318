from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkebackup.v1 import backup_pb2 as _backup_pb2
from google.cloud.gkebackup.v1 import backup_plan_pb2 as _backup_plan_pb2
from google.cloud.gkebackup.v1 import restore_pb2 as _restore_pb2
from google.cloud.gkebackup.v1 import restore_plan_pb2 as _restore_plan_pb2
from google.cloud.gkebackup.v1 import volume_pb2 as _volume_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class CreateBackupPlanRequest(_message.Message):
    __slots__ = ('parent', 'backup_plan', 'backup_plan_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_plan: _backup_plan_pb2.BackupPlan
    backup_plan_id: str

    def __init__(self, parent: _Optional[str]=..., backup_plan: _Optional[_Union[_backup_plan_pb2.BackupPlan, _Mapping]]=..., backup_plan_id: _Optional[str]=...) -> None:
        ...

class ListBackupPlansRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListBackupPlansResponse(_message.Message):
    __slots__ = ('backup_plans', 'next_page_token', 'unreachable')
    BACKUP_PLANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_plans: _containers.RepeatedCompositeFieldContainer[_backup_plan_pb2.BackupPlan]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backup_plans: _Optional[_Iterable[_Union[_backup_plan_pb2.BackupPlan, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetBackupPlanRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateBackupPlanRequest(_message.Message):
    __slots__ = ('backup_plan', 'update_mask')
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    backup_plan: _backup_plan_pb2.BackupPlan
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, backup_plan: _Optional[_Union[_backup_plan_pb2.BackupPlan, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteBackupPlanRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class CreateBackupRequest(_message.Message):
    __slots__ = ('parent', 'backup', 'backup_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup: _backup_pb2.Backup
    backup_id: str

    def __init__(self, parent: _Optional[str]=..., backup: _Optional[_Union[_backup_pb2.Backup, _Mapping]]=..., backup_id: _Optional[str]=...) -> None:
        ...

class ListBackupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListBackupsResponse(_message.Message):
    __slots__ = ('backups', 'next_page_token')
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[_backup_pb2.Backup]
    next_page_token: str

    def __init__(self, backups: _Optional[_Iterable[_Union[_backup_pb2.Backup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateBackupRequest(_message.Message):
    __slots__ = ('backup', 'update_mask')
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    backup: _backup_pb2.Backup
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, backup: _Optional[_Union[_backup_pb2.Backup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ('name', 'etag', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    force: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListVolumeBackupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListVolumeBackupsResponse(_message.Message):
    __slots__ = ('volume_backups', 'next_page_token')
    VOLUME_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    volume_backups: _containers.RepeatedCompositeFieldContainer[_volume_pb2.VolumeBackup]
    next_page_token: str

    def __init__(self, volume_backups: _Optional[_Iterable[_Union[_volume_pb2.VolumeBackup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetVolumeBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRestorePlanRequest(_message.Message):
    __slots__ = ('parent', 'restore_plan', 'restore_plan_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PLAN_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    restore_plan: _restore_plan_pb2.RestorePlan
    restore_plan_id: str

    def __init__(self, parent: _Optional[str]=..., restore_plan: _Optional[_Union[_restore_plan_pb2.RestorePlan, _Mapping]]=..., restore_plan_id: _Optional[str]=...) -> None:
        ...

class ListRestorePlansRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListRestorePlansResponse(_message.Message):
    __slots__ = ('restore_plans', 'next_page_token', 'unreachable')
    RESTORE_PLANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    restore_plans: _containers.RepeatedCompositeFieldContainer[_restore_plan_pb2.RestorePlan]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, restore_plans: _Optional[_Iterable[_Union[_restore_plan_pb2.RestorePlan, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRestorePlanRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateRestorePlanRequest(_message.Message):
    __slots__ = ('restore_plan', 'update_mask')
    RESTORE_PLAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    restore_plan: _restore_plan_pb2.RestorePlan
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, restore_plan: _Optional[_Union[_restore_plan_pb2.RestorePlan, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRestorePlanRequest(_message.Message):
    __slots__ = ('name', 'etag', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    force: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., force: bool=...) -> None:
        ...

class CreateRestoreRequest(_message.Message):
    __slots__ = ('parent', 'restore', 'restore_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    restore: _restore_pb2.Restore
    restore_id: str

    def __init__(self, parent: _Optional[str]=..., restore: _Optional[_Union[_restore_pb2.Restore, _Mapping]]=..., restore_id: _Optional[str]=...) -> None:
        ...

class ListRestoresRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListRestoresResponse(_message.Message):
    __slots__ = ('restores', 'next_page_token', 'unreachable')
    RESTORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    restores: _containers.RepeatedCompositeFieldContainer[_restore_pb2.Restore]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, restores: _Optional[_Iterable[_Union[_restore_pb2.Restore, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRestoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateRestoreRequest(_message.Message):
    __slots__ = ('restore', 'update_mask')
    RESTORE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    restore: _restore_pb2.Restore
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, restore: _Optional[_Union[_restore_pb2.Restore, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRestoreRequest(_message.Message):
    __slots__ = ('name', 'etag', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    force: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListVolumeRestoresRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListVolumeRestoresResponse(_message.Message):
    __slots__ = ('volume_restores', 'next_page_token')
    VOLUME_RESTORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    volume_restores: _containers.RepeatedCompositeFieldContainer[_volume_pb2.VolumeRestore]
    next_page_token: str

    def __init__(self, volume_restores: _Optional[_Iterable[_Union[_volume_pb2.VolumeRestore, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetVolumeRestoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetBackupIndexDownloadUrlRequest(_message.Message):
    __slots__ = ('backup',)
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    backup: str

    def __init__(self, backup: _Optional[str]=...) -> None:
        ...

class GetBackupIndexDownloadUrlResponse(_message.Message):
    __slots__ = ('signed_url',)
    SIGNED_URL_FIELD_NUMBER: _ClassVar[int]
    signed_url: str

    def __init__(self, signed_url: _Optional[str]=...) -> None:
        ...