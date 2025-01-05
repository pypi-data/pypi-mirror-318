from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TextSegment(_message.Message):
    __slots__ = ('content', 'start_offset', 'end_offset')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    content: str
    start_offset: int
    end_offset: int

    def __init__(self, content: _Optional[str]=..., start_offset: _Optional[int]=..., end_offset: _Optional[int]=...) -> None:
        ...