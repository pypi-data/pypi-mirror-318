from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.geo.type import viewport_pb2 as _viewport_pb2
from google.maps.fleetengine.delivery.v1 import delivery_vehicles_pb2 as _delivery_vehicles_pb2
from google.maps.fleetengine.delivery.v1 import header_pb2 as _header_pb2
from google.maps.fleetengine.delivery.v1 import task_tracking_info_pb2 as _task_tracking_info_pb2
from google.maps.fleetengine.delivery.v1 import tasks_pb2 as _tasks_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDeliveryVehicleRequest(_message.Message):
    __slots__ = ('header', 'parent', 'delivery_vehicle_id', 'delivery_vehicle')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_VEHICLE_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    parent: str
    delivery_vehicle_id: str
    delivery_vehicle: _delivery_vehicles_pb2.DeliveryVehicle

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., parent: _Optional[str]=..., delivery_vehicle_id: _Optional[str]=..., delivery_vehicle: _Optional[_Union[_delivery_vehicles_pb2.DeliveryVehicle, _Mapping]]=...) -> None:
        ...

class GetDeliveryVehicleRequest(_message.Message):
    __slots__ = ('header', 'name')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    name: str

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class ListDeliveryVehiclesRequest(_message.Message):
    __slots__ = ('header', 'parent', 'page_size', 'page_token', 'filter', 'viewport')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    parent: str
    page_size: int
    page_token: str
    filter: str
    viewport: _viewport_pb2.Viewport

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., viewport: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]]=...) -> None:
        ...

class ListDeliveryVehiclesResponse(_message.Message):
    __slots__ = ('delivery_vehicles', 'next_page_token', 'total_size')
    DELIVERY_VEHICLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    delivery_vehicles: _containers.RepeatedCompositeFieldContainer[_delivery_vehicles_pb2.DeliveryVehicle]
    next_page_token: str
    total_size: int

    def __init__(self, delivery_vehicles: _Optional[_Iterable[_Union[_delivery_vehicles_pb2.DeliveryVehicle, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class UpdateDeliveryVehicleRequest(_message.Message):
    __slots__ = ('header', 'delivery_vehicle', 'update_mask')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_VEHICLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    delivery_vehicle: _delivery_vehicles_pb2.DeliveryVehicle
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., delivery_vehicle: _Optional[_Union[_delivery_vehicles_pb2.DeliveryVehicle, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class BatchCreateTasksRequest(_message.Message):
    __slots__ = ('header', 'parent', 'requests')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateTaskRequest]

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateTaskRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateTasksResponse(_message.Message):
    __slots__ = ('tasks',)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_tasks_pb2.Task]

    def __init__(self, tasks: _Optional[_Iterable[_Union[_tasks_pb2.Task, _Mapping]]]=...) -> None:
        ...

class CreateTaskRequest(_message.Message):
    __slots__ = ('header', 'parent', 'task_id', 'task')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    parent: str
    task_id: str
    task: _tasks_pb2.Task

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., parent: _Optional[str]=..., task_id: _Optional[str]=..., task: _Optional[_Union[_tasks_pb2.Task, _Mapping]]=...) -> None:
        ...

class GetTaskRequest(_message.Message):
    __slots__ = ('header', 'name')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    name: str

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class UpdateTaskRequest(_message.Message):
    __slots__ = ('header', 'task', 'update_mask')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    task: _tasks_pb2.Task
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., task: _Optional[_Union[_tasks_pb2.Task, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListTasksRequest(_message.Message):
    __slots__ = ('header', 'parent', 'page_size', 'page_token', 'filter')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListTasksResponse(_message.Message):
    __slots__ = ('tasks', 'next_page_token', 'total_size')
    TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_tasks_pb2.Task]
    next_page_token: str
    total_size: int

    def __init__(self, tasks: _Optional[_Iterable[_Union[_tasks_pb2.Task, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GetTaskTrackingInfoRequest(_message.Message):
    __slots__ = ('header', 'name')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    header: _header_pb2.DeliveryRequestHeader
    name: str

    def __init__(self, header: _Optional[_Union[_header_pb2.DeliveryRequestHeader, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...