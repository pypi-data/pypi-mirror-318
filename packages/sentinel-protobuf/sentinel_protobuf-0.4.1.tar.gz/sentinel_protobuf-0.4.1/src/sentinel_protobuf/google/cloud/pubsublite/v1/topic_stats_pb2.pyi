from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.pubsublite.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeMessageStatsRequest(_message.Message):
    __slots__ = ('topic', 'partition', 'start_cursor', 'end_cursor')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    START_CURSOR_FIELD_NUMBER: _ClassVar[int]
    END_CURSOR_FIELD_NUMBER: _ClassVar[int]
    topic: str
    partition: int
    start_cursor: _common_pb2.Cursor
    end_cursor: _common_pb2.Cursor

    def __init__(self, topic: _Optional[str]=..., partition: _Optional[int]=..., start_cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=..., end_cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class ComputeMessageStatsResponse(_message.Message):
    __slots__ = ('message_count', 'message_bytes', 'minimum_publish_time', 'minimum_event_time')
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    message_count: int
    message_bytes: int
    minimum_publish_time: _timestamp_pb2.Timestamp
    minimum_event_time: _timestamp_pb2.Timestamp

    def __init__(self, message_count: _Optional[int]=..., message_bytes: _Optional[int]=..., minimum_publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., minimum_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ComputeHeadCursorRequest(_message.Message):
    __slots__ = ('topic', 'partition')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    topic: str
    partition: int

    def __init__(self, topic: _Optional[str]=..., partition: _Optional[int]=...) -> None:
        ...

class ComputeHeadCursorResponse(_message.Message):
    __slots__ = ('head_cursor',)
    HEAD_CURSOR_FIELD_NUMBER: _ClassVar[int]
    head_cursor: _common_pb2.Cursor

    def __init__(self, head_cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class ComputeTimeCursorRequest(_message.Message):
    __slots__ = ('topic', 'partition', 'target')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    topic: str
    partition: int
    target: _common_pb2.TimeTarget

    def __init__(self, topic: _Optional[str]=..., partition: _Optional[int]=..., target: _Optional[_Union[_common_pb2.TimeTarget, _Mapping]]=...) -> None:
        ...

class ComputeTimeCursorResponse(_message.Message):
    __slots__ = ('cursor',)
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    cursor: _common_pb2.Cursor

    def __init__(self, cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...