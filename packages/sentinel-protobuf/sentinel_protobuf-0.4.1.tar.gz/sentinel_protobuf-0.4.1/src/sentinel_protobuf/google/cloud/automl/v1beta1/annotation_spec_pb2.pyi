from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationSpec(_message.Message):
    __slots__ = ('name', 'display_name', 'example_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    example_count: int

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., example_count: _Optional[int]=...) -> None:
        ...