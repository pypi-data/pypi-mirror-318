from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TimeRange(_message.Message):
    __slots__ = ('start_time', 'end_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Group(_message.Message):
    __slots__ = ('email', 'title')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    email: str
    title: str

    def __init__(self, email: _Optional[str]=..., title: _Optional[str]=...) -> None:
        ...

class Domain(_message.Message):
    __slots__ = ('name', 'legacy_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEGACY_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    legacy_id: str

    def __init__(self, name: _Optional[str]=..., legacy_id: _Optional[str]=...) -> None:
        ...