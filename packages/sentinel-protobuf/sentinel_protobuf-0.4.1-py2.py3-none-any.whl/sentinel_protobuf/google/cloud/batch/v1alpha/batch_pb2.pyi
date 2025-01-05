from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.batch.v1alpha import job_pb2 as _job_pb2
from google.cloud.batch.v1alpha import resource_allowance_pb2 as _resource_allowance_pb2
from google.cloud.batch.v1alpha import task_pb2 as _task_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateJobRequest(_message.Message):
    __slots__ = ("parent", "job_id", "job", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    job_id: str
    job: _job_pb2.Job
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., job_id: _Optional[str] = ..., job: _Optional[_Union[_job_pb2.Job, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteJobRequest(_message.Message):
    __slots__ = ("name", "reason", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., reason: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class CancelJobRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class CancelJobResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateJobRequest(_message.Message):
    __slots__ = ("job", "update_mask", "request_id")
    JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    job: _job_pb2.Job
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, job: _Optional[_Union[_job_pb2.Job, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListJobsRequest(_message.Message):
    __slots__ = ("parent", "filter", "order_by", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    order_by: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListJobsResponse(_message.Message):
    __slots__ = ("jobs", "next_page_token", "unreachable")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_job_pb2.Job]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, jobs: _Optional[_Iterable[_Union[_job_pb2.Job, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class ListTasksRequest(_message.Message):
    __slots__ = ("parent", "filter", "order_by", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    order_by: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTasksResponse(_message.Message):
    __slots__ = ("tasks", "next_page_token", "unreachable")
    TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_task_pb2.Task]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tasks: _Optional[_Iterable[_Union[_task_pb2.Task, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateResourceAllowanceRequest(_message.Message):
    __slots__ = ("parent", "resource_allowance_id", "resource_allowance", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ALLOWANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    resource_allowance_id: str
    resource_allowance: _resource_allowance_pb2.ResourceAllowance
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., resource_allowance_id: _Optional[str] = ..., resource_allowance: _Optional[_Union[_resource_allowance_pb2.ResourceAllowance, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetResourceAllowanceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteResourceAllowanceRequest(_message.Message):
    __slots__ = ("name", "reason", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., reason: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListResourceAllowancesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListResourceAllowancesResponse(_message.Message):
    __slots__ = ("resource_allowances", "next_page_token", "unreachable")
    RESOURCE_ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    resource_allowances: _containers.RepeatedCompositeFieldContainer[_resource_allowance_pb2.ResourceAllowance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resource_allowances: _Optional[_Iterable[_Union[_resource_allowance_pb2.ResourceAllowance, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateResourceAllowanceRequest(_message.Message):
    __slots__ = ("resource_allowance", "update_mask", "request_id")
    RESOURCE_ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    resource_allowance: _resource_allowance_pb2.ResourceAllowance
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, resource_allowance: _Optional[_Union[_resource_allowance_pb2.ResourceAllowance, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...
