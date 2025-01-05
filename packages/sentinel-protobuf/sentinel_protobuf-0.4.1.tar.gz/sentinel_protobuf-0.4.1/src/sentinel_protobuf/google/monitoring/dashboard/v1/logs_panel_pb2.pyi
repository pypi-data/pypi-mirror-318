from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class LogsPanel(_message.Message):
    __slots__ = ('filter', 'resource_names')
    FILTER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    filter: str
    resource_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, filter: _Optional[str]=..., resource_names: _Optional[_Iterable[str]]=...) -> None:
        ...