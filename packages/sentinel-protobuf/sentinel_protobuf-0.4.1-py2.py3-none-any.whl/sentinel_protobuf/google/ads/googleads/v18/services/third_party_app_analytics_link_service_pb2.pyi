from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class RegenerateShareableLinkIdRequest(_message.Message):
    __slots__ = ('resource_name',)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str

    def __init__(self, resource_name: _Optional[str]=...) -> None:
        ...

class RegenerateShareableLinkIdResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...