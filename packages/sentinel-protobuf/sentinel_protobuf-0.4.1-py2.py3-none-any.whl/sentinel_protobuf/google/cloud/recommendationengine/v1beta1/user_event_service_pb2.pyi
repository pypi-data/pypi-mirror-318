from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.recommendationengine.v1beta1 import import_pb2 as _import_pb2
from google.cloud.recommendationengine.v1beta1 import user_event_pb2 as _user_event_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PurgeUserEventsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'force')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    force: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., force: bool=...) -> None:
        ...

class PurgeUserEventsMetadata(_message.Message):
    __slots__ = ('operation_name', 'create_time')
    OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    operation_name: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, operation_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PurgeUserEventsResponse(_message.Message):
    __slots__ = ('purged_events_count', 'user_events_sample')
    PURGED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENTS_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    purged_events_count: int
    user_events_sample: _containers.RepeatedCompositeFieldContainer[_user_event_pb2.UserEvent]

    def __init__(self, purged_events_count: _Optional[int]=..., user_events_sample: _Optional[_Iterable[_Union[_user_event_pb2.UserEvent, _Mapping]]]=...) -> None:
        ...

class WriteUserEventRequest(_message.Message):
    __slots__ = ('parent', 'user_event')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_event: _user_event_pb2.UserEvent

    def __init__(self, parent: _Optional[str]=..., user_event: _Optional[_Union[_user_event_pb2.UserEvent, _Mapping]]=...) -> None:
        ...

class CollectUserEventRequest(_message.Message):
    __slots__ = ('parent', 'user_event', 'uri', 'ets')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ETS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_event: str
    uri: str
    ets: int

    def __init__(self, parent: _Optional[str]=..., user_event: _Optional[str]=..., uri: _Optional[str]=..., ets: _Optional[int]=...) -> None:
        ...

class ListUserEventsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListUserEventsResponse(_message.Message):
    __slots__ = ('user_events', 'next_page_token')
    USER_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_events: _containers.RepeatedCompositeFieldContainer[_user_event_pb2.UserEvent]
    next_page_token: str

    def __init__(self, user_events: _Optional[_Iterable[_Union[_user_event_pb2.UserEvent, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...