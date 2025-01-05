from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ('type', 'uri', 'id', 'offset')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[Event.EventType]
        CREATIVE_VIEW: _ClassVar[Event.EventType]
        START: _ClassVar[Event.EventType]
        BREAK_START: _ClassVar[Event.EventType]
        BREAK_END: _ClassVar[Event.EventType]
        IMPRESSION: _ClassVar[Event.EventType]
        FIRST_QUARTILE: _ClassVar[Event.EventType]
        MIDPOINT: _ClassVar[Event.EventType]
        THIRD_QUARTILE: _ClassVar[Event.EventType]
        COMPLETE: _ClassVar[Event.EventType]
        PROGRESS: _ClassVar[Event.EventType]
        MUTE: _ClassVar[Event.EventType]
        UNMUTE: _ClassVar[Event.EventType]
        PAUSE: _ClassVar[Event.EventType]
        CLICK: _ClassVar[Event.EventType]
        CLICK_THROUGH: _ClassVar[Event.EventType]
        REWIND: _ClassVar[Event.EventType]
        RESUME: _ClassVar[Event.EventType]
        ERROR: _ClassVar[Event.EventType]
        EXPAND: _ClassVar[Event.EventType]
        COLLAPSE: _ClassVar[Event.EventType]
        CLOSE: _ClassVar[Event.EventType]
        CLOSE_LINEAR: _ClassVar[Event.EventType]
        SKIP: _ClassVar[Event.EventType]
        ACCEPT_INVITATION: _ClassVar[Event.EventType]
    EVENT_TYPE_UNSPECIFIED: Event.EventType
    CREATIVE_VIEW: Event.EventType
    START: Event.EventType
    BREAK_START: Event.EventType
    BREAK_END: Event.EventType
    IMPRESSION: Event.EventType
    FIRST_QUARTILE: Event.EventType
    MIDPOINT: Event.EventType
    THIRD_QUARTILE: Event.EventType
    COMPLETE: Event.EventType
    PROGRESS: Event.EventType
    MUTE: Event.EventType
    UNMUTE: Event.EventType
    PAUSE: Event.EventType
    CLICK: Event.EventType
    CLICK_THROUGH: Event.EventType
    REWIND: Event.EventType
    RESUME: Event.EventType
    ERROR: Event.EventType
    EXPAND: Event.EventType
    COLLAPSE: Event.EventType
    CLOSE: Event.EventType
    CLOSE_LINEAR: Event.EventType
    SKIP: Event.EventType
    ACCEPT_INVITATION: Event.EventType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    type: Event.EventType
    uri: str
    id: str
    offset: _duration_pb2.Duration

    def __init__(self, type: _Optional[_Union[Event.EventType, str]]=..., uri: _Optional[str]=..., id: _Optional[str]=..., offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ProgressEvent(_message.Message):
    __slots__ = ('time_offset', 'events')
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    time_offset: _duration_pb2.Duration
    events: _containers.RepeatedCompositeFieldContainer[Event]

    def __init__(self, time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., events: _Optional[_Iterable[_Union[Event, _Mapping]]]=...) -> None:
        ...