from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ListAccessibleCustomersRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListAccessibleCustomersResponse(_message.Message):
    __slots__ = ('resource_names',)
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    resource_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, resource_names: _Optional[_Iterable[str]]=...) -> None:
        ...