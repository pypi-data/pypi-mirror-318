from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpeedReadingInterval(_message.Message):
    __slots__ = ("start_polyline_point_index", "end_polyline_point_index", "speed")
    class Speed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEED_UNSPECIFIED: _ClassVar[SpeedReadingInterval.Speed]
        NORMAL: _ClassVar[SpeedReadingInterval.Speed]
        SLOW: _ClassVar[SpeedReadingInterval.Speed]
        TRAFFIC_JAM: _ClassVar[SpeedReadingInterval.Speed]
    SPEED_UNSPECIFIED: SpeedReadingInterval.Speed
    NORMAL: SpeedReadingInterval.Speed
    SLOW: SpeedReadingInterval.Speed
    TRAFFIC_JAM: SpeedReadingInterval.Speed
    START_POLYLINE_POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_POLYLINE_POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    start_polyline_point_index: int
    end_polyline_point_index: int
    speed: SpeedReadingInterval.Speed
    def __init__(self, start_polyline_point_index: _Optional[int] = ..., end_polyline_point_index: _Optional[int] = ..., speed: _Optional[_Union[SpeedReadingInterval.Speed, str]] = ...) -> None: ...
