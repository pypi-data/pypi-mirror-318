from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VideoObjectTrackingPredictionResult(_message.Message):
    __slots__ = ('id', 'display_name', 'time_segment_start', 'time_segment_end', 'confidence', 'frames')

    class Frame(_message.Message):
        __slots__ = ('time_offset', 'x_min', 'x_max', 'y_min', 'y_max')
        TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        X_MIN_FIELD_NUMBER: _ClassVar[int]
        X_MAX_FIELD_NUMBER: _ClassVar[int]
        Y_MIN_FIELD_NUMBER: _ClassVar[int]
        Y_MAX_FIELD_NUMBER: _ClassVar[int]
        time_offset: _duration_pb2.Duration
        x_min: _wrappers_pb2.FloatValue
        x_max: _wrappers_pb2.FloatValue
        y_min: _wrappers_pb2.FloatValue
        y_max: _wrappers_pb2.FloatValue

        def __init__(self, time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., x_min: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., x_max: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., y_min: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., y_max: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_START_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_END_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    time_segment_start: _duration_pb2.Duration
    time_segment_end: _duration_pb2.Duration
    confidence: _wrappers_pb2.FloatValue
    frames: _containers.RepeatedCompositeFieldContainer[VideoObjectTrackingPredictionResult.Frame]

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., time_segment_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., time_segment_end: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., confidence: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]]=..., frames: _Optional[_Iterable[_Union[VideoObjectTrackingPredictionResult.Frame, _Mapping]]]=...) -> None:
        ...