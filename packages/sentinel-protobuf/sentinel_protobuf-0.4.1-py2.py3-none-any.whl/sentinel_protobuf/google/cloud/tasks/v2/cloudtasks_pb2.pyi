from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.tasks.v2 import queue_pb2 as _queue_pb2
from google.cloud.tasks.v2 import task_pb2 as _task_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListQueuesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListQueuesResponse(_message.Message):
    __slots__ = ('queues', 'next_page_token')
    QUEUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    queues: _containers.RepeatedCompositeFieldContainer[_queue_pb2.Queue]
    next_page_token: str

    def __init__(self, queues: _Optional[_Iterable[_Union[_queue_pb2.Queue, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetQueueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateQueueRequest(_message.Message):
    __slots__ = ('parent', 'queue')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    queue: _queue_pb2.Queue

    def __init__(self, parent: _Optional[str]=..., queue: _Optional[_Union[_queue_pb2.Queue, _Mapping]]=...) -> None:
        ...

class UpdateQueueRequest(_message.Message):
    __slots__ = ('queue', 'update_mask')
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    queue: _queue_pb2.Queue
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, queue: _Optional[_Union[_queue_pb2.Queue, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteQueueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PurgeQueueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PauseQueueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResumeQueueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTasksRequest(_message.Message):
    __slots__ = ('parent', 'response_view', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    response_view: _task_pb2.Task.View
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., response_view: _Optional[_Union[_task_pb2.Task.View, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTasksResponse(_message.Message):
    __slots__ = ('tasks', 'next_page_token')
    TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_task_pb2.Task]
    next_page_token: str

    def __init__(self, tasks: _Optional[_Iterable[_Union[_task_pb2.Task, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTaskRequest(_message.Message):
    __slots__ = ('name', 'response_view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    response_view: _task_pb2.Task.View

    def __init__(self, name: _Optional[str]=..., response_view: _Optional[_Union[_task_pb2.Task.View, str]]=...) -> None:
        ...

class CreateTaskRequest(_message.Message):
    __slots__ = ('parent', 'task', 'response_view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    task: _task_pb2.Task
    response_view: _task_pb2.Task.View

    def __init__(self, parent: _Optional[str]=..., task: _Optional[_Union[_task_pb2.Task, _Mapping]]=..., response_view: _Optional[_Union[_task_pb2.Task.View, str]]=...) -> None:
        ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RunTaskRequest(_message.Message):
    __slots__ = ('name', 'response_view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    response_view: _task_pb2.Task.View

    def __init__(self, name: _Optional[str]=..., response_view: _Optional[_Union[_task_pb2.Task.View, str]]=...) -> None:
        ...