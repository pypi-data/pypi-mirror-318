from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class InlineDestination(_message.Message):
    __slots__ = ('content',)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes

    def __init__(self, content: _Optional[bytes]=...) -> None:
        ...

class InlineSource(_message.Message):
    __slots__ = ('content',)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes

    def __init__(self, content: _Optional[bytes]=...) -> None:
        ...