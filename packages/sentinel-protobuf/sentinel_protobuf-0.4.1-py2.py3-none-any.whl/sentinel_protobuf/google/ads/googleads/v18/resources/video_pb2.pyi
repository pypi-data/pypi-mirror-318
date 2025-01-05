from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Video(_message.Message):
    __slots__ = ("resource_name", "id", "channel_id", "duration_millis", "title")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MILLIS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: str
    channel_id: str
    duration_millis: int
    title: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[str] = ..., channel_id: _Optional[str] = ..., duration_millis: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...
