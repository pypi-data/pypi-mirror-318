from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.maps.fleetengine.v1 import fleetengine_pb2 as _fleetengine_pb2
from google.maps.fleetengine.v1 import header_pb2 as _header_pb2
from google.maps.fleetengine.v1 import trips_pb2 as _trips_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateTripRequest(_message.Message):
    __slots__ = ('header', 'parent', 'trip_id', 'trip')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRIP_ID_FIELD_NUMBER: _ClassVar[int]
    TRIP_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    parent: str
    trip_id: str
    trip: _trips_pb2.Trip

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., parent: _Optional[str]=..., trip_id: _Optional[str]=..., trip: _Optional[_Union[_trips_pb2.Trip, _Mapping]]=...) -> None:
        ...

class GetTripRequest(_message.Message):
    __slots__ = ('header', 'name', 'view', 'current_route_segment_version', 'remaining_waypoints_version', 'route_format_type', 'current_route_segment_traffic_version', 'remaining_waypoints_route_version')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    REMAINING_WAYPOINTS_VERSION_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FORMAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_TRAFFIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    REMAINING_WAYPOINTS_ROUTE_VERSION_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    name: str
    view: _trips_pb2.TripView
    current_route_segment_version: _timestamp_pb2.Timestamp
    remaining_waypoints_version: _timestamp_pb2.Timestamp
    route_format_type: _fleetengine_pb2.PolylineFormatType
    current_route_segment_traffic_version: _timestamp_pb2.Timestamp
    remaining_waypoints_route_version: _timestamp_pb2.Timestamp

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., name: _Optional[str]=..., view: _Optional[_Union[_trips_pb2.TripView, str]]=..., current_route_segment_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., remaining_waypoints_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., route_format_type: _Optional[_Union[_fleetengine_pb2.PolylineFormatType, str]]=..., current_route_segment_traffic_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., remaining_waypoints_route_version: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ReportBillableTripRequest(_message.Message):
    __slots__ = ('name', 'country_code', 'platform', 'related_ids', 'solution_type')

    class SolutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOLUTION_TYPE_UNSPECIFIED: _ClassVar[ReportBillableTripRequest.SolutionType]
        ON_DEMAND_RIDESHARING_AND_DELIVERIES: _ClassVar[ReportBillableTripRequest.SolutionType]
    SOLUTION_TYPE_UNSPECIFIED: ReportBillableTripRequest.SolutionType
    ON_DEMAND_RIDESHARING_AND_DELIVERIES: ReportBillableTripRequest.SolutionType
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    RELATED_IDS_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    country_code: str
    platform: _trips_pb2.BillingPlatformIdentifier
    related_ids: _containers.RepeatedScalarFieldContainer[str]
    solution_type: ReportBillableTripRequest.SolutionType

    def __init__(self, name: _Optional[str]=..., country_code: _Optional[str]=..., platform: _Optional[_Union[_trips_pb2.BillingPlatformIdentifier, str]]=..., related_ids: _Optional[_Iterable[str]]=..., solution_type: _Optional[_Union[ReportBillableTripRequest.SolutionType, str]]=...) -> None:
        ...

class UpdateTripRequest(_message.Message):
    __slots__ = ('header', 'name', 'trip', 'update_mask')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRIP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    name: str
    trip: _trips_pb2.Trip
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., name: _Optional[str]=..., trip: _Optional[_Union[_trips_pb2.Trip, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class SearchTripsRequest(_message.Message):
    __slots__ = ('header', 'parent', 'vehicle_id', 'active_trips_only', 'page_size', 'page_token', 'minimum_staleness')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TRIPS_ONLY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_STALENESS_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.RequestHeader
    parent: str
    vehicle_id: str
    active_trips_only: bool
    page_size: int
    page_token: str
    minimum_staleness: _duration_pb2.Duration

    def __init__(self, header: _Optional[_Union[_header_pb2.RequestHeader, _Mapping]]=..., parent: _Optional[str]=..., vehicle_id: _Optional[str]=..., active_trips_only: bool=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., minimum_staleness: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class SearchTripsResponse(_message.Message):
    __slots__ = ('trips', 'next_page_token')
    TRIPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    trips: _containers.RepeatedCompositeFieldContainer[_trips_pb2.Trip]
    next_page_token: str

    def __init__(self, trips: _Optional[_Iterable[_Union[_trips_pb2.Trip, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...