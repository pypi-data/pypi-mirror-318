from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ThirdPartyAppAnalyticsLink(_message.Message):
    __slots__ = ("resource_name", "shareable_link_id")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHAREABLE_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    shareable_link_id: str
    def __init__(self, resource_name: _Optional[str] = ..., shareable_link_id: _Optional[str] = ...) -> None: ...
