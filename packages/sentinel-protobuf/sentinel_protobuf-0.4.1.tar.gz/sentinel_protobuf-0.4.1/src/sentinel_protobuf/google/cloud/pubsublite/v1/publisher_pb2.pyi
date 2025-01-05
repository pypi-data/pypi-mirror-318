from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.cloud.pubsublite.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InitialPublishRequest(_message.Message):
    __slots__ = ('topic', 'partition', 'client_id')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    topic: str
    partition: int
    client_id: bytes

    def __init__(self, topic: _Optional[str]=..., partition: _Optional[int]=..., client_id: _Optional[bytes]=...) -> None:
        ...

class InitialPublishResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MessagePublishRequest(_message.Message):
    __slots__ = ('messages', 'first_sequence_number')
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_common_pb2.PubSubMessage]
    first_sequence_number: int

    def __init__(self, messages: _Optional[_Iterable[_Union[_common_pb2.PubSubMessage, _Mapping]]]=..., first_sequence_number: _Optional[int]=...) -> None:
        ...

class MessagePublishResponse(_message.Message):
    __slots__ = ('start_cursor', 'cursor_ranges')

    class CursorRange(_message.Message):
        __slots__ = ('start_cursor', 'start_index', 'end_index')
        START_CURSOR_FIELD_NUMBER: _ClassVar[int]
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        END_INDEX_FIELD_NUMBER: _ClassVar[int]
        start_cursor: _common_pb2.Cursor
        start_index: int
        end_index: int

        def __init__(self, start_cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=..., start_index: _Optional[int]=..., end_index: _Optional[int]=...) -> None:
            ...
    START_CURSOR_FIELD_NUMBER: _ClassVar[int]
    CURSOR_RANGES_FIELD_NUMBER: _ClassVar[int]
    start_cursor: _common_pb2.Cursor
    cursor_ranges: _containers.RepeatedCompositeFieldContainer[MessagePublishResponse.CursorRange]

    def __init__(self, start_cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=..., cursor_ranges: _Optional[_Iterable[_Union[MessagePublishResponse.CursorRange, _Mapping]]]=...) -> None:
        ...

class PublishRequest(_message.Message):
    __slots__ = ('initial_request', 'message_publish_request')
    INITIAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_PUBLISH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    initial_request: InitialPublishRequest
    message_publish_request: MessagePublishRequest

    def __init__(self, initial_request: _Optional[_Union[InitialPublishRequest, _Mapping]]=..., message_publish_request: _Optional[_Union[MessagePublishRequest, _Mapping]]=...) -> None:
        ...

class PublishResponse(_message.Message):
    __slots__ = ('initial_response', 'message_response')
    INITIAL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    initial_response: InitialPublishResponse
    message_response: MessagePublishResponse

    def __init__(self, initial_response: _Optional[_Union[InitialPublishResponse, _Mapping]]=..., message_response: _Optional[_Union[MessagePublishResponse, _Mapping]]=...) -> None:
        ...