from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceAccessSpec(_message.Message):
    __slots__ = ('readers', 'writers', 'owners')
    READERS_FIELD_NUMBER: _ClassVar[int]
    WRITERS_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    readers: _containers.RepeatedScalarFieldContainer[str]
    writers: _containers.RepeatedScalarFieldContainer[str]
    owners: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, readers: _Optional[_Iterable[str]]=..., writers: _Optional[_Iterable[str]]=..., owners: _Optional[_Iterable[str]]=...) -> None:
        ...

class DataAccessSpec(_message.Message):
    __slots__ = ('readers',)
    READERS_FIELD_NUMBER: _ClassVar[int]
    readers: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, readers: _Optional[_Iterable[str]]=...) -> None:
        ...