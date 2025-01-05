from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ReportPhishingRequest(_message.Message):
    __slots__ = ('parent', 'uri')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    parent: str
    uri: str

    def __init__(self, parent: _Optional[str]=..., uri: _Optional[str]=...) -> None:
        ...

class ReportPhishingResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...