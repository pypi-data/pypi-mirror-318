from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSet(_message.Message):
    __slots__ = ('id', 'resource_name')
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    resource_name: str

    def __init__(self, id: _Optional[int]=..., resource_name: _Optional[str]=...) -> None:
        ...