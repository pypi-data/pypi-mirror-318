from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.talent.v4 import event_pb2 as _event_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateClientEventRequest(_message.Message):
    __slots__ = ('parent', 'client_event')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    client_event: _event_pb2.ClientEvent

    def __init__(self, parent: _Optional[str]=..., client_event: _Optional[_Union[_event_pb2.ClientEvent, _Mapping]]=...) -> None:
        ...