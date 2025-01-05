from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.devtools.build.v1 import build_events_pb2 as _build_events_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PublishLifecycleEventRequest(_message.Message):
    __slots__ = ('service_level', 'build_event', 'stream_timeout', 'notification_keywords', 'project_id', 'check_preceding_lifecycle_events_present')

    class ServiceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONINTERACTIVE: _ClassVar[PublishLifecycleEventRequest.ServiceLevel]
        INTERACTIVE: _ClassVar[PublishLifecycleEventRequest.ServiceLevel]
    NONINTERACTIVE: PublishLifecycleEventRequest.ServiceLevel
    INTERACTIVE: PublishLifecycleEventRequest.ServiceLevel
    SERVICE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BUILD_EVENT_FIELD_NUMBER: _ClassVar[int]
    STREAM_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_PRECEDING_LIFECYCLE_EVENTS_PRESENT_FIELD_NUMBER: _ClassVar[int]
    service_level: PublishLifecycleEventRequest.ServiceLevel
    build_event: OrderedBuildEvent
    stream_timeout: _duration_pb2.Duration
    notification_keywords: _containers.RepeatedScalarFieldContainer[str]
    project_id: str
    check_preceding_lifecycle_events_present: bool

    def __init__(self, service_level: _Optional[_Union[PublishLifecycleEventRequest.ServiceLevel, str]]=..., build_event: _Optional[_Union[OrderedBuildEvent, _Mapping]]=..., stream_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., notification_keywords: _Optional[_Iterable[str]]=..., project_id: _Optional[str]=..., check_preceding_lifecycle_events_present: bool=...) -> None:
        ...

class PublishBuildToolEventStreamResponse(_message.Message):
    __slots__ = ('stream_id', 'sequence_number')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    stream_id: _build_events_pb2.StreamId
    sequence_number: int

    def __init__(self, stream_id: _Optional[_Union[_build_events_pb2.StreamId, _Mapping]]=..., sequence_number: _Optional[int]=...) -> None:
        ...

class OrderedBuildEvent(_message.Message):
    __slots__ = ('stream_id', 'sequence_number', 'event')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    stream_id: _build_events_pb2.StreamId
    sequence_number: int
    event: _build_events_pb2.BuildEvent

    def __init__(self, stream_id: _Optional[_Union[_build_events_pb2.StreamId, _Mapping]]=..., sequence_number: _Optional[int]=..., event: _Optional[_Union[_build_events_pb2.BuildEvent, _Mapping]]=...) -> None:
        ...

class PublishBuildToolEventStreamRequest(_message.Message):
    __slots__ = ('ordered_build_event', 'notification_keywords', 'project_id', 'check_preceding_lifecycle_events_present')
    ORDERED_BUILD_EVENT_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_PRECEDING_LIFECYCLE_EVENTS_PRESENT_FIELD_NUMBER: _ClassVar[int]
    ordered_build_event: OrderedBuildEvent
    notification_keywords: _containers.RepeatedScalarFieldContainer[str]
    project_id: str
    check_preceding_lifecycle_events_present: bool

    def __init__(self, ordered_build_event: _Optional[_Union[OrderedBuildEvent, _Mapping]]=..., notification_keywords: _Optional[_Iterable[str]]=..., project_id: _Optional[str]=..., check_preceding_lifecycle_events_present: bool=...) -> None:
        ...