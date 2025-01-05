from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeocodingResults(_message.Message):
    __slots__ = ("origin", "destination", "intermediates")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATES_FIELD_NUMBER: _ClassVar[int]
    origin: GeocodedWaypoint
    destination: GeocodedWaypoint
    intermediates: _containers.RepeatedCompositeFieldContainer[GeocodedWaypoint]
    def __init__(self, origin: _Optional[_Union[GeocodedWaypoint, _Mapping]] = ..., destination: _Optional[_Union[GeocodedWaypoint, _Mapping]] = ..., intermediates: _Optional[_Iterable[_Union[GeocodedWaypoint, _Mapping]]] = ...) -> None: ...

class GeocodedWaypoint(_message.Message):
    __slots__ = ("geocoder_status", "intermediate_waypoint_request_index", "type", "partial_match", "place_id")
    GEOCODER_STATUS_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_WAYPOINT_REQUEST_INDEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_MATCH_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    geocoder_status: _status_pb2.Status
    intermediate_waypoint_request_index: int
    type: _containers.RepeatedScalarFieldContainer[str]
    partial_match: bool
    place_id: str
    def __init__(self, geocoder_status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., intermediate_waypoint_request_index: _Optional[int] = ..., type: _Optional[_Iterable[str]] = ..., partial_match: bool = ..., place_id: _Optional[str] = ...) -> None: ...
