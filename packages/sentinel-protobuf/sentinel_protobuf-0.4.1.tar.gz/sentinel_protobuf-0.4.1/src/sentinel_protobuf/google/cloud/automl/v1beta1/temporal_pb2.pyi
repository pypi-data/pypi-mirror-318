from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TimeSegment(_message.Message):
    __slots__ = ('start_time_offset', 'end_time_offset')
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_time_offset: _duration_pb2.Duration
    end_time_offset: _duration_pb2.Duration

    def __init__(self, start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...