from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Position(_message.Message):
    __slots__ = ('reference_name', 'position', 'reverse_strand')
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    REVERSE_STRAND_FIELD_NUMBER: _ClassVar[int]
    reference_name: str
    position: int
    reverse_strand: bool

    def __init__(self, reference_name: _Optional[str]=..., position: _Optional[int]=..., reverse_strand: bool=...) -> None:
        ...