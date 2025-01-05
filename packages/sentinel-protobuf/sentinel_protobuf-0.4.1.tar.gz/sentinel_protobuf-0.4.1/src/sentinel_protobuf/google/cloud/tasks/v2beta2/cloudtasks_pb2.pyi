from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.tasks.v2beta2 import queue_pb2 as _queue_pb2
from google.cloud.tasks.v2beta2 import task_pb2 as _task_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListQueuesRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListQueuesResponse(_message.Message):
    __slots__ = ("queues", "next_page_token")
    QUEUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    queues: _containers.RepeatedCompositeFieldContainer[_queue_pb2.Queue]
    next_page_token: str
    def __init__(self, queues: _Optional[_Iterable[_Union[_queue_pb2.Queue, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetQueueRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateQueueRequest(_message.Message):
    __slots__ = ("parent", "queue")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    queue: _queue_pb2.Queue
    def __init__(self, parent: _Optional[str] = ..., queue: _Optional[_Union[_queue_pb2.Queue, _Mapping]] = ...) -> None: ...

class UpdateQueueRequest(_message.Message):
    __slots__ = ("queue", "update_mask")
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    queue: _queue_pb2.Queue
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, queue: _Optional[_Union[_queue_pb2.Queue, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteQueueRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PurgeQueueRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PauseQueueRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResumeQueueRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UploadQueueYamlRequest(_message.Message):
    __slots__ = ("app_id", "http_body")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    HTTP_BODY_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    http_body: _httpbody_pb2.HttpBody
    def __init__(self, app_id: _Optional[str] = ..., http_body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]] = ...) -> None: ...

class ListTasksRequest(_message.Message):
    __slots__ = ("parent", "response_view", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    response_view: _task_pb2.Task.View
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., response_view: _Optional[_Union[_task_pb2.Task.View, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTasksResponse(_message.Message):
    __slots__ = ("tasks", "next_page_token")
    TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_task_pb2.Task]
    next_page_token: str
    def __init__(self, tasks: _Optional[_Iterable[_Union[_task_pb2.Task, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("name", "response_view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    response_view: _task_pb2.Task.View
    def __init__(self, name: _Optional[str] = ..., response_view: _Optional[_Union[_task_pb2.Task.View, str]] = ...) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ("parent", "task", "response_view")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    task: _task_pb2.Task
    response_view: _task_pb2.Task.View
    def __init__(self, parent: _Optional[str] = ..., task: _Optional[_Union[_task_pb2.Task, _Mapping]] = ..., response_view: _Optional[_Union[_task_pb2.Task.View, str]] = ...) -> None: ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LeaseTasksRequest(_message.Message):
    __slots__ = ("parent", "max_tasks", "lease_duration", "response_view", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MAX_TASKS_FIELD_NUMBER: _ClassVar[int]
    LEASE_DURATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    max_tasks: int
    lease_duration: _duration_pb2.Duration
    response_view: _task_pb2.Task.View
    filter: str
    def __init__(self, parent: _Optional[str] = ..., max_tasks: _Optional[int] = ..., lease_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., response_view: _Optional[_Union[_task_pb2.Task.View, str]] = ..., filter: _Optional[str] = ...) -> None: ...

class LeaseTasksResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_task_pb2.Task]
    def __init__(self, tasks: _Optional[_Iterable[_Union[_task_pb2.Task, _Mapping]]] = ...) -> None: ...

class AcknowledgeTaskRequest(_message.Message):
    __slots__ = ("name", "schedule_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    schedule_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RenewLeaseRequest(_message.Message):
    __slots__ = ("name", "schedule_time", "lease_duration", "response_view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    LEASE_DURATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    schedule_time: _timestamp_pb2.Timestamp
    lease_duration: _duration_pb2.Duration
    response_view: _task_pb2.Task.View
    def __init__(self, name: _Optional[str] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lease_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., response_view: _Optional[_Union[_task_pb2.Task.View, str]] = ...) -> None: ...

class CancelLeaseRequest(_message.Message):
    __slots__ = ("name", "schedule_time", "response_view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    schedule_time: _timestamp_pb2.Timestamp
    response_view: _task_pb2.Task.View
    def __init__(self, name: _Optional[str] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., response_view: _Optional[_Union[_task_pb2.Task.View, str]] = ...) -> None: ...

class RunTaskRequest(_message.Message):
    __slots__ = ("name", "response_view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    response_view: _task_pb2.Task.View
    def __init__(self, name: _Optional[str] = ..., response_view: _Optional[_Union[_task_pb2.Task.View, str]] = ...) -> None: ...
