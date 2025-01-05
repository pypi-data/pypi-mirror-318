from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1 import schedule_pb2 as _schedule_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScheduleRequest(_message.Message):
    __slots__ = ("parent", "schedule")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    schedule: _schedule_pb2.Schedule
    def __init__(self, parent: _Optional[str] = ..., schedule: _Optional[_Union[_schedule_pb2.Schedule, _Mapping]] = ...) -> None: ...

class GetScheduleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSchedulesRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListSchedulesResponse(_message.Message):
    __slots__ = ("schedules", "next_page_token")
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    schedules: _containers.RepeatedCompositeFieldContainer[_schedule_pb2.Schedule]
    next_page_token: str
    def __init__(self, schedules: _Optional[_Iterable[_Union[_schedule_pb2.Schedule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteScheduleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PauseScheduleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResumeScheduleRequest(_message.Message):
    __slots__ = ("name", "catch_up")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATCH_UP_FIELD_NUMBER: _ClassVar[int]
    name: str
    catch_up: bool
    def __init__(self, name: _Optional[str] = ..., catch_up: bool = ...) -> None: ...

class UpdateScheduleRequest(_message.Message):
    __slots__ = ("schedule", "update_mask")
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    schedule: _schedule_pb2.Schedule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, schedule: _Optional[_Union[_schedule_pb2.Schedule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
