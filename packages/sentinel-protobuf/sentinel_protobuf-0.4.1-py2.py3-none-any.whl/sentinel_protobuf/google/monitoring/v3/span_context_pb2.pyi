from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SpanContext(_message.Message):
    __slots__ = ('span_name',)
    SPAN_NAME_FIELD_NUMBER: _ClassVar[int]
    span_name: str

    def __init__(self, span_name: _Optional[str]=...) -> None:
        ...