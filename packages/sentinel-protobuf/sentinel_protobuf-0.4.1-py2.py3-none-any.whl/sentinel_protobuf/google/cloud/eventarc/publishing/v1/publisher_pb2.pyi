from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.cloud.eventarc.publishing.v1 import cloud_event_pb2 as _cloud_event_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PublishChannelConnectionEventsRequest(_message.Message):
    __slots__ = ('channel_connection', 'events', 'text_events')
    CHANNEL_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TEXT_EVENTS_FIELD_NUMBER: _ClassVar[int]
    channel_connection: str
    events: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    text_events: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, channel_connection: _Optional[str]=..., events: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=..., text_events: _Optional[_Iterable[str]]=...) -> None:
        ...

class PublishChannelConnectionEventsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PublishEventsRequest(_message.Message):
    __slots__ = ('channel', 'events', 'text_events')
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TEXT_EVENTS_FIELD_NUMBER: _ClassVar[int]
    channel: str
    events: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    text_events: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, channel: _Optional[str]=..., events: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=..., text_events: _Optional[_Iterable[str]]=...) -> None:
        ...

class PublishEventsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PublishRequest(_message.Message):
    __slots__ = ('message_bus', 'proto_message', 'json_message', 'avro_message')
    MESSAGE_BUS_FIELD_NUMBER: _ClassVar[int]
    PROTO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    JSON_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AVRO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_bus: str
    proto_message: _cloud_event_pb2.CloudEvent
    json_message: str
    avro_message: bytes

    def __init__(self, message_bus: _Optional[str]=..., proto_message: _Optional[_Union[_cloud_event_pb2.CloudEvent, _Mapping]]=..., json_message: _Optional[str]=..., avro_message: _Optional[bytes]=...) -> None:
        ...

class PublishResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...