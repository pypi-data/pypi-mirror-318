from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VideoClassificationPredictionResult(_message.Message):
    __slots__ = ('id', 'display_name', 'type', 'time_segment_start', 'time_segment_end', 'confidence')
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_START_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_END_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    type: str
    time_segment_start: _duration_pb2.Duration
    time_segment_end: _duration_pb2.Duration
    confidence: _wrappers_pb2.FloatValue

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[str]=..., time_segment_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., time_segment_end: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., confidence: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
        ...