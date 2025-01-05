from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.maps.fleetengine.delivery.v1 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryVehicle(_message.Message):
    __slots__ = ('name', 'last_location', 'navigation_status', 'current_route_segment', 'current_route_segment_end_point', 'remaining_distance_meters', 'remaining_duration', 'remaining_vehicle_journey_segments', 'attributes', 'type')

    class DeliveryVehicleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELIVERY_VEHICLE_TYPE_UNSPECIFIED: _ClassVar[DeliveryVehicle.DeliveryVehicleType]
        AUTO: _ClassVar[DeliveryVehicle.DeliveryVehicleType]
        TWO_WHEELER: _ClassVar[DeliveryVehicle.DeliveryVehicleType]
        BICYCLE: _ClassVar[DeliveryVehicle.DeliveryVehicleType]
        PEDESTRIAN: _ClassVar[DeliveryVehicle.DeliveryVehicleType]
    DELIVERY_VEHICLE_TYPE_UNSPECIFIED: DeliveryVehicle.DeliveryVehicleType
    AUTO: DeliveryVehicle.DeliveryVehicleType
    TWO_WHEELER: DeliveryVehicle.DeliveryVehicleType
    BICYCLE: DeliveryVehicle.DeliveryVehicleType
    PEDESTRIAN: DeliveryVehicle.DeliveryVehicleType
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ROUTE_SEGMENT_END_POINT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    REMAINING_DURATION_FIELD_NUMBER: _ClassVar[int]
    REMAINING_VEHICLE_JOURNEY_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    last_location: _common_pb2.DeliveryVehicleLocation
    navigation_status: _common_pb2.DeliveryVehicleNavigationStatus
    current_route_segment: bytes
    current_route_segment_end_point: _latlng_pb2.LatLng
    remaining_distance_meters: _wrappers_pb2.Int32Value
    remaining_duration: _duration_pb2.Duration
    remaining_vehicle_journey_segments: _containers.RepeatedCompositeFieldContainer[VehicleJourneySegment]
    attributes: _containers.RepeatedCompositeFieldContainer[_common_pb2.DeliveryVehicleAttribute]
    type: DeliveryVehicle.DeliveryVehicleType

    def __init__(self, name: _Optional[str]=..., last_location: _Optional[_Union[_common_pb2.DeliveryVehicleLocation, _Mapping]]=..., navigation_status: _Optional[_Union[_common_pb2.DeliveryVehicleNavigationStatus, str]]=..., current_route_segment: _Optional[bytes]=..., current_route_segment_end_point: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., remaining_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., remaining_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., remaining_vehicle_journey_segments: _Optional[_Iterable[_Union[VehicleJourneySegment, _Mapping]]]=..., attributes: _Optional[_Iterable[_Union[_common_pb2.DeliveryVehicleAttribute, _Mapping]]]=..., type: _Optional[_Union[DeliveryVehicle.DeliveryVehicleType, str]]=...) -> None:
        ...

class LocationInfo(_message.Message):
    __slots__ = ('point',)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _latlng_pb2.LatLng

    def __init__(self, point: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=...) -> None:
        ...

class VehicleJourneySegment(_message.Message):
    __slots__ = ('stop', 'driving_distance_meters', 'driving_duration', 'path')
    STOP_FIELD_NUMBER: _ClassVar[int]
    DRIVING_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    DRIVING_DURATION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    stop: VehicleStop
    driving_distance_meters: _wrappers_pb2.Int32Value
    driving_duration: _duration_pb2.Duration
    path: _containers.RepeatedCompositeFieldContainer[_latlng_pb2.LatLng]

    def __init__(self, stop: _Optional[_Union[VehicleStop, _Mapping]]=..., driving_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., driving_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., path: _Optional[_Iterable[_Union[_latlng_pb2.LatLng, _Mapping]]]=...) -> None:
        ...

class VehicleStop(_message.Message):
    __slots__ = ('planned_location', 'tasks', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[VehicleStop.State]
        NEW: _ClassVar[VehicleStop.State]
        ENROUTE: _ClassVar[VehicleStop.State]
        ARRIVED: _ClassVar[VehicleStop.State]
    STATE_UNSPECIFIED: VehicleStop.State
    NEW: VehicleStop.State
    ENROUTE: VehicleStop.State
    ARRIVED: VehicleStop.State

    class TaskInfo(_message.Message):
        __slots__ = ('task_id', 'task_duration', 'target_time_window')
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        TASK_DURATION_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
        task_id: str
        task_duration: _duration_pb2.Duration
        target_time_window: _common_pb2.TimeWindow

        def __init__(self, task_id: _Optional[str]=..., task_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., target_time_window: _Optional[_Union[_common_pb2.TimeWindow, _Mapping]]=...) -> None:
            ...
    PLANNED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    planned_location: LocationInfo
    tasks: _containers.RepeatedCompositeFieldContainer[VehicleStop.TaskInfo]
    state: VehicleStop.State

    def __init__(self, planned_location: _Optional[_Union[LocationInfo, _Mapping]]=..., tasks: _Optional[_Iterable[_Union[VehicleStop.TaskInfo, _Mapping]]]=..., state: _Optional[_Union[VehicleStop.State, str]]=...) -> None:
        ...