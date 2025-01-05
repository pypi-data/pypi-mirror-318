from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ('report_time', 'type', 'details')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[Event.EventType]
        IDLE: _ClassVar[Event.EventType]
        HEARTBEAT: _ClassVar[Event.EventType]
        HEALTH: _ClassVar[Event.EventType]
        MAINTENANCE: _ClassVar[Event.EventType]
        METADATA_CHANGE: _ClassVar[Event.EventType]
    EVENT_TYPE_UNSPECIFIED: Event.EventType
    IDLE: Event.EventType
    HEARTBEAT: Event.EventType
    HEALTH: Event.EventType
    MAINTENANCE: Event.EventType
    METADATA_CHANGE: Event.EventType

    class DetailsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    REPORT_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    report_time: _timestamp_pb2.Timestamp
    type: Event.EventType
    details: _containers.ScalarMap[str, str]

    def __init__(self, report_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[_Union[Event.EventType, str]]=..., details: _Optional[_Mapping[str, str]]=...) -> None:
        ...