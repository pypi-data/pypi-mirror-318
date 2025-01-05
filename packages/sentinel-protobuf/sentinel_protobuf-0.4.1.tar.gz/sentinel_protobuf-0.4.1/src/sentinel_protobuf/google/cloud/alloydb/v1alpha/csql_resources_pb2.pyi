from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class CloudSQLBackupRunSource(_message.Message):
    __slots__ = ('project', 'instance_id', 'backup_run_id')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    project: str
    instance_id: str
    backup_run_id: int

    def __init__(self, project: _Optional[str]=..., instance_id: _Optional[str]=..., backup_run_id: _Optional[int]=...) -> None:
        ...