from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ExternalDatasetReference(_message.Message):
    __slots__ = ('external_source', 'connection')
    EXTERNAL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    external_source: str
    connection: str

    def __init__(self, external_source: _Optional[str]=..., connection: _Optional[str]=...) -> None:
        ...