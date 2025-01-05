from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GetServiceAccountRequest(_message.Message):
    __slots__ = ('project_id',)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str

    def __init__(self, project_id: _Optional[str]=...) -> None:
        ...

class GetServiceAccountResponse(_message.Message):
    __slots__ = ('kind', 'email')
    KIND_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    kind: str
    email: str

    def __init__(self, kind: _Optional[str]=..., email: _Optional[str]=...) -> None:
        ...