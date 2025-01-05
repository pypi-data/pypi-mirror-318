from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ReleaseChannel(_message.Message):
    __slots__ = ('name', 'current_version', 'pending_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PENDING_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    current_version: str
    pending_version: str

    def __init__(self, name: _Optional[str]=..., current_version: _Optional[str]=..., pending_version: _Optional[str]=...) -> None:
        ...