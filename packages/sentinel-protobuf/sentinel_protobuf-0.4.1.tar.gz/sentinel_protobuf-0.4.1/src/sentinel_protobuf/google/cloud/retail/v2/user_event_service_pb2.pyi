from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import import_config_pb2 as _import_config_pb2
from google.cloud.retail.v2 import purge_config_pb2 as _purge_config_pb2
from google.cloud.retail.v2 import user_event_pb2 as _user_event_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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
    __slots__ = ("prebuilt_rule", "parent", "user_event", "uri", "ets", "raw_json")
    PREBUILT_RULE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ETS_FIELD_NUMBER: _ClassVar[int]
    RAW_JSON_FIELD_NUMBER: _ClassVar[int]
    prebuilt_rule: str
    parent: str
    user_event: str
    uri: str
    ets: int
    raw_json: str
    def __init__(self, prebuilt_rule: _Optional[str] = ..., parent: _Optional[str] = ..., user_event: _Optional[str] = ..., uri: _Optional[str] = ..., ets: _Optional[int] = ..., raw_json: _Optional[str] = ...) -> None: ...

class RejoinUserEventsRequest(_message.Message):
    __slots__ = ("parent", "user_event_rejoin_scope")
    class UserEventRejoinScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_EVENT_REJOIN_SCOPE_UNSPECIFIED: _ClassVar[RejoinUserEventsRequest.UserEventRejoinScope]
        JOINED_EVENTS: _ClassVar[RejoinUserEventsRequest.UserEventRejoinScope]
        UNJOINED_EVENTS: _ClassVar[RejoinUserEventsRequest.UserEventRejoinScope]
    USER_EVENT_REJOIN_SCOPE_UNSPECIFIED: RejoinUserEventsRequest.UserEventRejoinScope
    JOINED_EVENTS: RejoinUserEventsRequest.UserEventRejoinScope
    UNJOINED_EVENTS: RejoinUserEventsRequest.UserEventRejoinScope
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_REJOIN_SCOPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_event_rejoin_scope: RejoinUserEventsRequest.UserEventRejoinScope
    def __init__(self, parent: _Optional[str] = ..., user_event_rejoin_scope: _Optional[_Union[RejoinUserEventsRequest.UserEventRejoinScope, str]] = ...) -> None: ...

class RejoinUserEventsResponse(_message.Message):
    __slots__ = ("rejoined_user_events_count",)
    REJOINED_USER_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    rejoined_user_events_count: int
    def __init__(self, rejoined_user_events_count: _Optional[int] = ...) -> None: ...

class RejoinUserEventsMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
