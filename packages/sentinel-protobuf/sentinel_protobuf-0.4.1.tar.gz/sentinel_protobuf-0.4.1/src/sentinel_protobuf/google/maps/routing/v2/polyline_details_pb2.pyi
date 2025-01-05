from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolylineDetails(_message.Message):
    __slots__ = ("flyover_info", "narrow_road_info")
    class RoadFeatureState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROAD_FEATURE_STATE_UNSPECIFIED: _ClassVar[PolylineDetails.RoadFeatureState]
        EXISTS: _ClassVar[PolylineDetails.RoadFeatureState]
        DOES_NOT_EXIST: _ClassVar[PolylineDetails.RoadFeatureState]
    ROAD_FEATURE_STATE_UNSPECIFIED: PolylineDetails.RoadFeatureState
    EXISTS: PolylineDetails.RoadFeatureState
    DOES_NOT_EXIST: PolylineDetails.RoadFeatureState
    class PolylinePointIndex(_message.Message):
        __slots__ = ("start_index", "end_index")
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        END_INDEX_FIELD_NUMBER: _ClassVar[int]
        start_index: int
        end_index: int
        def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ...) -> None: ...
    class FlyoverInfo(_message.Message):
        __slots__ = ("flyover_presence", "polyline_point_index")
        FLYOVER_PRESENCE_FIELD_NUMBER: _ClassVar[int]
        POLYLINE_POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
        flyover_presence: PolylineDetails.RoadFeatureState
        polyline_point_index: PolylineDetails.PolylinePointIndex
        def __init__(self, flyover_presence: _Optional[_Union[PolylineDetails.RoadFeatureState, str]] = ..., polyline_point_index: _Optional[_Union[PolylineDetails.PolylinePointIndex, _Mapping]] = ...) -> None: ...
    class NarrowRoadInfo(_message.Message):
        __slots__ = ("narrow_road_presence", "polyline_point_index")
        NARROW_ROAD_PRESENCE_FIELD_NUMBER: _ClassVar[int]
        POLYLINE_POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
        narrow_road_presence: PolylineDetails.RoadFeatureState
        polyline_point_index: PolylineDetails.PolylinePointIndex
        def __init__(self, narrow_road_presence: _Optional[_Union[PolylineDetails.RoadFeatureState, str]] = ..., polyline_point_index: _Optional[_Union[PolylineDetails.PolylinePointIndex, _Mapping]] = ...) -> None: ...
    FLYOVER_INFO_FIELD_NUMBER: _ClassVar[int]
    NARROW_ROAD_INFO_FIELD_NUMBER: _ClassVar[int]
    flyover_info: _containers.RepeatedCompositeFieldContainer[PolylineDetails.FlyoverInfo]
    narrow_road_info: _containers.RepeatedCompositeFieldContainer[PolylineDetails.NarrowRoadInfo]
    def __init__(self, flyover_info: _Optional[_Iterable[_Union[PolylineDetails.FlyoverInfo, _Mapping]]] = ..., narrow_road_info: _Optional[_Iterable[_Union[PolylineDetails.NarrowRoadInfo, _Mapping]]] = ...) -> None: ...
