from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class CollapsibleGroup(_message.Message):
    __slots__ = ('collapsed',)
    COLLAPSED_FIELD_NUMBER: _ClassVar[int]
    collapsed: bool

    def __init__(self, collapsed: bool=...) -> None:
        ...