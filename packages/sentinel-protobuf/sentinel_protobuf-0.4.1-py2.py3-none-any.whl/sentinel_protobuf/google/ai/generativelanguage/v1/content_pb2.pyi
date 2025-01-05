from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Content(_message.Message):
    __slots__ = ('parts', 'role')
    PARTS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[Part]
    role: str

    def __init__(self, parts: _Optional[_Iterable[_Union[Part, _Mapping]]]=..., role: _Optional[str]=...) -> None:
        ...

class Part(_message.Message):
    __slots__ = ('text', 'inline_data')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    text: str
    inline_data: Blob

    def __init__(self, text: _Optional[str]=..., inline_data: _Optional[_Union[Blob, _Mapping]]=...) -> None:
        ...

class Blob(_message.Message):
    __slots__ = ('mime_type', 'data')
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    data: bytes

    def __init__(self, mime_type: _Optional[str]=..., data: _Optional[bytes]=...) -> None:
        ...