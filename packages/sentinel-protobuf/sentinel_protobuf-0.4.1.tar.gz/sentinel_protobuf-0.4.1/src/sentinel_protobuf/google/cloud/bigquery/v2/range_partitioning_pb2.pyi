from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RangePartitioning(_message.Message):
    __slots__ = ('field', 'range')

    class Range(_message.Message):
        __slots__ = ('start', 'end', 'interval')
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_FIELD_NUMBER: _ClassVar[int]
        start: str
        end: str
        interval: str

        def __init__(self, start: _Optional[str]=..., end: _Optional[str]=..., interval: _Optional[str]=...) -> None:
            ...
    FIELD_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    field: str
    range: RangePartitioning.Range

    def __init__(self, field: _Optional[str]=..., range: _Optional[_Union[RangePartitioning.Range, _Mapping]]=...) -> None:
        ...