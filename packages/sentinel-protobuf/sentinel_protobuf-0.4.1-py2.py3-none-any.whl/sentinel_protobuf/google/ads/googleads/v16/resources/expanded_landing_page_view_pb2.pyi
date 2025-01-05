from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExpandedLandingPageView(_message.Message):
    __slots__ = ("resource_name", "expanded_final_url")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_FINAL_URL_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    expanded_final_url: str
    def __init__(self, resource_name: _Optional[str] = ..., expanded_final_url: _Optional[str] = ...) -> None: ...
