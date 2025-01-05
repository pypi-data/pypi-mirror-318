from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupApplianceBackupProperties(_message.Message):
    __slots__ = ("generation_id", "finalize_time", "recovery_range_start_time", "recovery_range_end_time")
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_RANGE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_RANGE_END_TIME_FIELD_NUMBER: _ClassVar[int]
    generation_id: int
    finalize_time: _timestamp_pb2.Timestamp
    recovery_range_start_time: _timestamp_pb2.Timestamp
    recovery_range_end_time: _timestamp_pb2.Timestamp
    def __init__(self, generation_id: _Optional[int] = ..., finalize_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., recovery_range_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., recovery_range_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
