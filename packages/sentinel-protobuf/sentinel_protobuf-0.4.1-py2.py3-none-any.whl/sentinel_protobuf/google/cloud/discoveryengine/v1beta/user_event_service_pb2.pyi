from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import import_config_pb2 as _import_config_pb2
from google.cloud.discoveryengine.v1beta import purge_config_pb2 as _purge_config_pb2
from google.cloud.discoveryengine.v1beta import user_event_pb2 as _user_event_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WriteUserEventRequest(_message.Message):
    __slots__ = ("parent", "user_event", "write_async")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    WRITE_ASYNC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_event: _user_event_pb2.UserEvent
    write_async: bool
    def __init__(self, parent: _Optional[str] = ..., user_event: _Optional[_Union[_user_event_pb2.UserEvent, _Mapping]] = ..., write_async: bool = ...) -> None: ...

class CollectUserEventRequest(_message.Message):
    __slots__ = ("parent", "user_event", "uri", "ets")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ETS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_event: str
    uri: str
    ets: int
    def __init__(self, parent: _Optional[str] = ..., user_event: _Optional[str] = ..., uri: _Optional[str] = ..., ets: _Optional[int] = ...) -> None: ...
