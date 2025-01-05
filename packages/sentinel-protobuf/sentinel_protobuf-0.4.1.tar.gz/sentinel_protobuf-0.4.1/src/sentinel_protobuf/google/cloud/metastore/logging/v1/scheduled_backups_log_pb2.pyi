from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScheduledBackupLogEntry(_message.Message):
    __slots__ = ('backup_id', 'service', 'start_time', 'end_time', 'state', 'backup_size_bytes', 'backup_location', 'message')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ScheduledBackupLogEntry.State]
        IN_PROGRESS: _ClassVar[ScheduledBackupLogEntry.State]
        SUCCEEDED: _ClassVar[ScheduledBackupLogEntry.State]
        FAILED: _ClassVar[ScheduledBackupLogEntry.State]
    STATE_UNSPECIFIED: ScheduledBackupLogEntry.State
    IN_PROGRESS: ScheduledBackupLogEntry.State
    SUCCEEDED: ScheduledBackupLogEntry.State
    FAILED: ScheduledBackupLogEntry.State
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    service: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: ScheduledBackupLogEntry.State
    backup_size_bytes: int
    backup_location: str
    message: str

    def __init__(self, backup_id: _Optional[str]=..., service: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ScheduledBackupLogEntry.State, str]]=..., backup_size_bytes: _Optional[int]=..., backup_location: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...