from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Range(_message.Message):
    __slots__ = ('reference_name', 'start', 'end')
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    reference_name: str
    start: int
    end: int

    def __init__(self, reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=...) -> None:
        ...