from google.maps.routes.v1 import fallback_info_pb2 as _fallback_info_pb2
from google.maps.routes.v1 import route_pb2 as _route_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RouteMatrixElementCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED: _ClassVar[RouteMatrixElementCondition]
    ROUTE_EXISTS: _ClassVar[RouteMatrixElementCondition]
    ROUTE_NOT_FOUND: _ClassVar[RouteMatrixElementCondition]
ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED: RouteMatrixElementCondition
ROUTE_EXISTS: RouteMatrixElementCondition
ROUTE_NOT_FOUND: RouteMatrixElementCondition

class RouteMatrixElement(_message.Message):
    __slots__ = ('origin_index', 'destination_index', 'status', 'condition', 'distance_meters', 'duration', 'static_duration', 'travel_advisory', 'fallback_info')
    ORIGIN_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_ADVISORY_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_INFO_FIELD_NUMBER: _ClassVar[int]
    origin_index: int
    destination_index: int
    status: _status_pb2.Status
    condition: RouteMatrixElementCondition
    distance_meters: int
    duration: _duration_pb2.Duration
    static_duration: _duration_pb2.Duration
    travel_advisory: _route_pb2.RouteTravelAdvisory
    fallback_info: _fallback_info_pb2.FallbackInfo

    def __init__(self, origin_index: _Optional[int]=..., destination_index: _Optional[int]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., condition: _Optional[_Union[RouteMatrixElementCondition, str]]=..., distance_meters: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., travel_advisory: _Optional[_Union[_route_pb2.RouteTravelAdvisory, _Mapping]]=..., fallback_info: _Optional[_Union[_fallback_info_pb2.FallbackInfo, _Mapping]]=...) -> None:
        ...