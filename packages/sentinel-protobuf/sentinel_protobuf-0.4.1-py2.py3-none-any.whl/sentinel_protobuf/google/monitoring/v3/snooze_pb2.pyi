from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Snooze(_message.Message):
    __slots__ = ('name', 'criteria', 'interval', 'display_name')

    class Criteria(_message.Message):
        __slots__ = ('policies',)
        POLICIES_FIELD_NUMBER: _ClassVar[int]
        policies: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, policies: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    criteria: Snooze.Criteria
    interval: _common_pb2.TimeInterval
    display_name: str

    def __init__(self, name: _Optional[str]=..., criteria: _Optional[_Union[Snooze.Criteria, _Mapping]]=..., interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]]=..., display_name: _Optional[str]=...) -> None:
        ...