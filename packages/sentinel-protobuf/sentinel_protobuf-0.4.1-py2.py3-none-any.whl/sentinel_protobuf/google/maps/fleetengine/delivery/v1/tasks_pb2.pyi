from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.maps.fleetengine.delivery.v1 import common_pb2 as _common_pb2
from google.maps.fleetengine.delivery.v1 import delivery_vehicles_pb2 as _delivery_vehicles_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ('name', 'type', 'state', 'task_outcome', 'task_outcome_time', 'task_outcome_location', 'task_outcome_location_source', 'tracking_id', 'delivery_vehicle_id', 'planned_location', 'task_duration', 'target_time_window', 'journey_sharing_info', 'task_tracking_view_config', 'attributes')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Task.Type]
        PICKUP: _ClassVar[Task.Type]
        DELIVERY: _ClassVar[Task.Type]
        SCHEDULED_STOP: _ClassVar[Task.Type]
        UNAVAILABLE: _ClassVar[Task.Type]
    TYPE_UNSPECIFIED: Task.Type
    PICKUP: Task.Type
    DELIVERY: Task.Type
    SCHEDULED_STOP: Task.Type
    UNAVAILABLE: Task.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Task.State]
        OPEN: _ClassVar[Task.State]
        CLOSED: _ClassVar[Task.State]
    STATE_UNSPECIFIED: Task.State
    OPEN: Task.State
    CLOSED: Task.State

    class TaskOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TASK_OUTCOME_UNSPECIFIED: _ClassVar[Task.TaskOutcome]
        SUCCEEDED: _ClassVar[Task.TaskOutcome]
        FAILED: _ClassVar[Task.TaskOutcome]
    TASK_OUTCOME_UNSPECIFIED: Task.TaskOutcome
    SUCCEEDED: Task.TaskOutcome
    FAILED: Task.TaskOutcome

    class TaskOutcomeLocationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TASK_OUTCOME_LOCATION_SOURCE_UNSPECIFIED: _ClassVar[Task.TaskOutcomeLocationSource]
        PROVIDER: _ClassVar[Task.TaskOutcomeLocationSource]
        LAST_VEHICLE_LOCATION: _ClassVar[Task.TaskOutcomeLocationSource]
    TASK_OUTCOME_LOCATION_SOURCE_UNSPECIFIED: Task.TaskOutcomeLocationSource
    PROVIDER: Task.TaskOutcomeLocationSource
    LAST_VEHICLE_LOCATION: Task.TaskOutcomeLocationSource

    class JourneySharingInfo(_message.Message):
        __slots__ = ('remaining_vehicle_journey_segments', 'last_location', 'last_location_snappable')
        REMAINING_VEHICLE_JOURNEY_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        LAST_LOCATION_FIELD_NUMBER: _ClassVar[int]
        LAST_LOCATION_SNAPPABLE_FIELD_NUMBER: _ClassVar[int]
        remaining_vehicle_journey_segments: _containers.RepeatedCompositeFieldContainer[_delivery_vehicles_pb2.VehicleJourneySegment]
        last_location: _common_pb2.DeliveryVehicleLocation
        last_location_snappable: bool

        def __init__(self, remaining_vehicle_journey_segments: _Optional[_Iterable[_Union[_delivery_vehicles_pb2.VehicleJourneySegment, _Mapping]]]=..., last_location: _Optional[_Union[_common_pb2.DeliveryVehicleLocation, _Mapping]]=..., last_location_snappable: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    TASK_OUTCOME_TIME_FIELD_NUMBER: _ClassVar[int]
    TASK_OUTCOME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TASK_OUTCOME_LOCATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    PLANNED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TASK_DURATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_SHARING_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_TRACKING_VIEW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: Task.Type
    state: Task.State
    task_outcome: Task.TaskOutcome
    task_outcome_time: _timestamp_pb2.Timestamp
    task_outcome_location: _delivery_vehicles_pb2.LocationInfo
    task_outcome_location_source: Task.TaskOutcomeLocationSource
    tracking_id: str
    delivery_vehicle_id: str
    planned_location: _delivery_vehicles_pb2.LocationInfo
    task_duration: _duration_pb2.Duration
    target_time_window: _common_pb2.TimeWindow
    journey_sharing_info: Task.JourneySharingInfo
    task_tracking_view_config: TaskTrackingViewConfig
    attributes: _containers.RepeatedCompositeFieldContainer[_common_pb2.TaskAttribute]

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Task.Type, str]]=..., state: _Optional[_Union[Task.State, str]]=..., task_outcome: _Optional[_Union[Task.TaskOutcome, str]]=..., task_outcome_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., task_outcome_location: _Optional[_Union[_delivery_vehicles_pb2.LocationInfo, _Mapping]]=..., task_outcome_location_source: _Optional[_Union[Task.TaskOutcomeLocationSource, str]]=..., tracking_id: _Optional[str]=..., delivery_vehicle_id: _Optional[str]=..., planned_location: _Optional[_Union[_delivery_vehicles_pb2.LocationInfo, _Mapping]]=..., task_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., target_time_window: _Optional[_Union[_common_pb2.TimeWindow, _Mapping]]=..., journey_sharing_info: _Optional[_Union[Task.JourneySharingInfo, _Mapping]]=..., task_tracking_view_config: _Optional[_Union[TaskTrackingViewConfig, _Mapping]]=..., attributes: _Optional[_Iterable[_Union[_common_pb2.TaskAttribute, _Mapping]]]=...) -> None:
        ...

class TaskTrackingViewConfig(_message.Message):
    __slots__ = ('route_polyline_points_visibility', 'estimated_arrival_time_visibility', 'estimated_task_completion_time_visibility', 'remaining_driving_distance_visibility', 'remaining_stop_count_visibility', 'vehicle_location_visibility')

    class VisibilityOption(_message.Message):
        __slots__ = ('remaining_stop_count_threshold', 'duration_until_estimated_arrival_time_threshold', 'remaining_driving_distance_meters_threshold', 'always', 'never')
        REMAINING_STOP_COUNT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        DURATION_UNTIL_ESTIMATED_ARRIVAL_TIME_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        REMAINING_DRIVING_DISTANCE_METERS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_FIELD_NUMBER: _ClassVar[int]
        NEVER_FIELD_NUMBER: _ClassVar[int]
        remaining_stop_count_threshold: int
        duration_until_estimated_arrival_time_threshold: _duration_pb2.Duration
        remaining_driving_distance_meters_threshold: int
        always: bool
        never: bool

        def __init__(self, remaining_stop_count_threshold: _Optional[int]=..., duration_until_estimated_arrival_time_threshold: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., remaining_driving_distance_meters_threshold: _Optional[int]=..., always: bool=..., never: bool=...) -> None:
            ...
    ROUTE_POLYLINE_POINTS_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_ARRIVAL_TIME_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TASK_COMPLETION_TIME_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    REMAINING_DRIVING_DISTANCE_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    REMAINING_STOP_COUNT_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_LOCATION_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    route_polyline_points_visibility: TaskTrackingViewConfig.VisibilityOption
    estimated_arrival_time_visibility: TaskTrackingViewConfig.VisibilityOption
    estimated_task_completion_time_visibility: TaskTrackingViewConfig.VisibilityOption
    remaining_driving_distance_visibility: TaskTrackingViewConfig.VisibilityOption
    remaining_stop_count_visibility: TaskTrackingViewConfig.VisibilityOption
    vehicle_location_visibility: TaskTrackingViewConfig.VisibilityOption

    def __init__(self, route_polyline_points_visibility: _Optional[_Union[TaskTrackingViewConfig.VisibilityOption, _Mapping]]=..., estimated_arrival_time_visibility: _Optional[_Union[TaskTrackingViewConfig.VisibilityOption, _Mapping]]=..., estimated_task_completion_time_visibility: _Optional[_Union[TaskTrackingViewConfig.VisibilityOption, _Mapping]]=..., remaining_driving_distance_visibility: _Optional[_Union[TaskTrackingViewConfig.VisibilityOption, _Mapping]]=..., remaining_stop_count_visibility: _Optional[_Union[TaskTrackingViewConfig.VisibilityOption, _Mapping]]=..., vehicle_location_visibility: _Optional[_Union[TaskTrackingViewConfig.VisibilityOption, _Mapping]]=...) -> None:
        ...