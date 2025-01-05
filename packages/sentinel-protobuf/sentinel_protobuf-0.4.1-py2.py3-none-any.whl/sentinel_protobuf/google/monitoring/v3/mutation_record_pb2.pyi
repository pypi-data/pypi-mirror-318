from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MutationRecord(_message.Message):
    __slots__ = ('mutate_time', 'mutated_by')
    MUTATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MUTATED_BY_FIELD_NUMBER: _ClassVar[int]
    mutate_time: _timestamp_pb2.Timestamp
    mutated_by: str

    def __init__(self, mutate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., mutated_by: _Optional[str]=...) -> None:
        ...