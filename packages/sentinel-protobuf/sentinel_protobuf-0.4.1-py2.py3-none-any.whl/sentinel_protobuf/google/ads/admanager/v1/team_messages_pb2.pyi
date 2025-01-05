from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ('name', 'team_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    team_id: int

    def __init__(self, name: _Optional[str]=..., team_id: _Optional[int]=...) -> None:
        ...