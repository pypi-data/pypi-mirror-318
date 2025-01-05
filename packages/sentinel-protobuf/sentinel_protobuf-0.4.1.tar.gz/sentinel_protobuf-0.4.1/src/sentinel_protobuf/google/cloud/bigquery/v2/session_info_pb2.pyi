from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SessionInfo(_message.Message):
    __slots__ = ('session_id',)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str

    def __init__(self, session_id: _Optional[str]=...) -> None:
        ...