from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DataFormatOptions(_message.Message):
    __slots__ = ('use_int64_timestamp',)
    USE_INT64_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    use_int64_timestamp: bool

    def __init__(self, use_int64_timestamp: bool=...) -> None:
        ...