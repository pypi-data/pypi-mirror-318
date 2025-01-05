from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ('artifact', 'execution', 'event_time', 'type', 'labels')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Event.Type]
        INPUT: _ClassVar[Event.Type]
        OUTPUT: _ClassVar[Event.Type]
    TYPE_UNSPECIFIED: Event.Type
    INPUT: Event.Type
    OUTPUT: Event.Type

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    artifact: str
    execution: str
    event_time: _timestamp_pb2.Timestamp
    type: Event.Type
    labels: _containers.ScalarMap[str, str]

    def __init__(self, artifact: _Optional[str]=..., execution: _Optional[str]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[_Union[Event.Type, str]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...