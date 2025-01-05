from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ClassReference(_message.Message):
    __slots__ = ('name', 'list')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    name: str
    list: bool

    def __init__(self, name: _Optional[str]=..., list: bool=...) -> None:
        ...