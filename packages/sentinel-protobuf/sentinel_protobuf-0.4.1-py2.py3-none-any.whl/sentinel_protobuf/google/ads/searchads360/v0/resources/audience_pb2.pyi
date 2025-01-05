from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Audience(_message.Message):
    __slots__ = ('resource_name', 'id', 'name', 'description')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    description: str

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...