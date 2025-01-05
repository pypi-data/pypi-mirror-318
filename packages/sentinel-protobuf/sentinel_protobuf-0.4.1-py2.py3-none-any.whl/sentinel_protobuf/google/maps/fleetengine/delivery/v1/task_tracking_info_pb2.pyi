from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.maps.fleetengine.delivery.v1 import common_pb2 as _common_pb2
from google.maps.fleetengine.delivery.v1 import delivery_vehicles_pb2 as _delivery_vehicles_pb2
from google.maps.fleetengine.delivery.v1 import tasks_pb2 as _tasks_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TaskTrackingInfo(_message.Message):
    __slots__ = ('name', 'tracking_id', 'vehicle_location', 'route_polyline_points', 'remaining_stop_count', 'remaining_driving_distance_meters', 'estimated_arrival_time', 'estimated_task_completion_time', 'state', 'task_outcome', 'task_outcome_time', 'planned_location', 'target_time_window', 'attributes')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ROUTE_POLYLINE_POINTS_FIELD_NUMBER: _ClassVar[int]
    REMAINING_STOP_COUNT_FIELD_NUMBER: _ClassVar[int]
    REMAINING_DRIVING_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TASK_COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    TASK_OUTCOME_TIME_FIELD_NUMBER: _ClassVar[int]
    PLANNED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    tracking_id: str
    vehicle_location: _common_pb2.DeliveryVehicleLocation
    route_polyline_points: _containers.RepeatedCompositeFieldContainer[_latlng_pb2.LatLng]
    remaining_stop_count: _wrappers_pb2.Int32Value
    remaining_driving_distance_meters: _wrappers_pb2.Int32Value
    estimated_arrival_time: _timestamp_pb2.Timestamp
    estimated_task_completion_time: _timestamp_pb2.Timestamp
    state: _tasks_pb2.Task.State
    task_outcome: _tasks_pb2.Task.TaskOutcome
    task_outcome_time: _timestamp_pb2.Timestamp
    planned_location: _delivery_vehicles_pb2.LocationInfo
    target_time_window: _common_pb2.TimeWindow
    attributes: _containers.RepeatedCompositeFieldContainer[_common_pb2.TaskAttribute]

    def __init__(self, name: _Optional[str]=..., tracking_id: _Optional[str]=..., vehicle_location: _Optional[_Union[_common_pb2.DeliveryVehicleLocation, _Mapping]]=..., route_polyline_points: _Optional[_Iterable[_Union[_latlng_pb2.LatLng, _Mapping]]]=..., remaining_stop_count: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., remaining_driving_distance_meters: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., estimated_arrival_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., estimated_task_completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[_tasks_pb2.Task.State, str]]=..., task_outcome: _Optional[_Union[_tasks_pb2.Task.TaskOutcome, str]]=..., task_outcome_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., planned_location: _Optional[_Union[_delivery_vehicles_pb2.LocationInfo, _Mapping]]=..., target_time_window: _Optional[_Union[_common_pb2.TimeWindow, _Mapping]]=..., attributes: _Optional[_Iterable[_Union[_common_pb2.TaskAttribute, _Mapping]]]=...) -> None:
        ...