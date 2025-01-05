from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.datastream.v1 import datastream_resources_pb2 as _datastream_resources_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamActivityLogEntry(_message.Message):
    __slots__ = ("event_code", "event_message", "stream_state_change")
    class StreamStateChange(_message.Message):
        __slots__ = ("new_state",)
        NEW_STATE_FIELD_NUMBER: _ClassVar[int]
        new_state: _datastream_resources_pb2.Stream.State
        def __init__(self, new_state: _Optional[_Union[_datastream_resources_pb2.Stream.State, str]] = ...) -> None: ...
    EVENT_CODE_FIELD_NUMBER: _ClassVar[int]
    EVENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STREAM_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    event_code: str
    event_message: str
    stream_state_change: StreamActivityLogEntry.StreamStateChange
    def __init__(self, event_code: _Optional[str] = ..., event_message: _Optional[str] = ..., stream_state_change: _Optional[_Union[StreamActivityLogEntry.StreamStateChange, _Mapping]] = ...) -> None: ...
