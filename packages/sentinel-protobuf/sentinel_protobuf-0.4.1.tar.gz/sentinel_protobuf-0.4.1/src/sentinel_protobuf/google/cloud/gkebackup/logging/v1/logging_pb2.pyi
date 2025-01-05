from google.cloud.gkebackup.logging.v1 import logged_backup_pb2 as _logged_backup_pb2
from google.cloud.gkebackup.logging.v1 import logged_backup_plan_pb2 as _logged_backup_plan_pb2
from google.cloud.gkebackup.logging.v1 import logged_restore_pb2 as _logged_restore_pb2
from google.cloud.gkebackup.logging.v1 import logged_restore_plan_pb2 as _logged_restore_plan_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANGE_TYPE_UNSPECIFIED: _ClassVar[ChangeType]
    CREATION: _ClassVar[ChangeType]
    UPDATE: _ClassVar[ChangeType]
    DELETION: _ClassVar[ChangeType]
CHANGE_TYPE_UNSPECIFIED: ChangeType
CREATION: ChangeType
UPDATE: ChangeType
DELETION: ChangeType

class BackupPlanChange(_message.Message):
    __slots__ = ('backup_plan', 'change_type', 'update_mask', 'input_backup_plan', 'error')
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INPUT_BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    backup_plan: str
    change_type: ChangeType
    update_mask: _field_mask_pb2.FieldMask
    input_backup_plan: _logged_backup_plan_pb2.LoggedBackupPlan
    error: _status_pb2.Status

    def __init__(self, backup_plan: _Optional[str]=..., change_type: _Optional[_Union[ChangeType, str]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., input_backup_plan: _Optional[_Union[_logged_backup_plan_pb2.LoggedBackupPlan, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class BackupChange(_message.Message):
    __slots__ = ('backup', 'change_type', 'scheduled', 'update_mask', 'input_backup', 'error')
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INPUT_BACKUP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    backup: str
    change_type: ChangeType
    scheduled: bool
    update_mask: _field_mask_pb2.FieldMask
    input_backup: _logged_backup_pb2.LoggedBackup
    error: _status_pb2.Status

    def __init__(self, backup: _Optional[str]=..., change_type: _Optional[_Union[ChangeType, str]]=..., scheduled: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., input_backup: _Optional[_Union[_logged_backup_pb2.LoggedBackup, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class RestorePlanChange(_message.Message):
    __slots__ = ('restore_plan', 'change_type', 'update_mask', 'input_restore_plan', 'error')
    RESTORE_PLAN_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INPUT_RESTORE_PLAN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    restore_plan: str
    change_type: ChangeType
    update_mask: _field_mask_pb2.FieldMask
    input_restore_plan: _logged_restore_plan_pb2.LoggedRestorePlan
    error: _status_pb2.Status

    def __init__(self, restore_plan: _Optional[str]=..., change_type: _Optional[_Union[ChangeType, str]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., input_restore_plan: _Optional[_Union[_logged_restore_plan_pb2.LoggedRestorePlan, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class RestoreChange(_message.Message):
    __slots__ = ('restore', 'change_type', 'update_mask', 'input_restore', 'error')
    RESTORE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INPUT_RESTORE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    restore: str
    change_type: ChangeType
    update_mask: _field_mask_pb2.FieldMask
    input_restore: _logged_restore_pb2.LoggedRestore
    error: _status_pb2.Status

    def __init__(self, restore: _Optional[str]=..., change_type: _Optional[_Union[ChangeType, str]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., input_restore: _Optional[_Union[_logged_restore_pb2.LoggedRestore, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...