from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.run.v2 import condition_pb2 as _condition_pb2
from google.cloud.run.v2.k8s import min_pb2 as _min_pb2
from google.cloud.run.v2 import vendor_settings_pb2 as _vendor_settings_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTaskRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListTasksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "show_deleted")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListTasksResponse(_message.Message):
    __slots__ = ("tasks", "next_page_token")
    TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    next_page_token: str
    def __init__(self, tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ("name", "uid", "generation", "labels", "annotations", "create_time", "scheduled_time", "start_time", "completion_time", "update_time", "delete_time", "expire_time", "job", "execution", "containers", "volumes", "max_retries", "timeout", "service_account", "execution_environment", "reconciling", "conditions", "observed_generation", "index", "retried", "last_attempt_result", "encryption_key", "vpc_access", "log_uri", "satisfies_pzs", "etag")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_GENERATION_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    RETRIED_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPT_RESULT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    VPC_ACCESS_FIELD_NUMBER: _ClassVar[int]
    LOG_URI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    generation: int
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    scheduled_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    completion_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    job: str
    execution: str
    containers: _containers.RepeatedCompositeFieldContainer[_min_pb2.Container]
    volumes: _containers.RepeatedCompositeFieldContainer[_min_pb2.Volume]
    max_retries: int
    timeout: _duration_pb2.Duration
    service_account: str
    execution_environment: _vendor_settings_pb2.ExecutionEnvironment
    reconciling: bool
    conditions: _containers.RepeatedCompositeFieldContainer[_condition_pb2.Condition]
    observed_generation: int
    index: int
    retried: int
    last_attempt_result: TaskAttemptResult
    encryption_key: str
    vpc_access: _vendor_settings_pb2.VpcAccess
    log_uri: str
    satisfies_pzs: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., generation: _Optional[int] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., job: _Optional[str] = ..., execution: _Optional[str] = ..., containers: _Optional[_Iterable[_Union[_min_pb2.Container, _Mapping]]] = ..., volumes: _Optional[_Iterable[_Union[_min_pb2.Volume, _Mapping]]] = ..., max_retries: _Optional[int] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., service_account: _Optional[str] = ..., execution_environment: _Optional[_Union[_vendor_settings_pb2.ExecutionEnvironment, str]] = ..., reconciling: bool = ..., conditions: _Optional[_Iterable[_Union[_condition_pb2.Condition, _Mapping]]] = ..., observed_generation: _Optional[int] = ..., index: _Optional[int] = ..., retried: _Optional[int] = ..., last_attempt_result: _Optional[_Union[TaskAttemptResult, _Mapping]] = ..., encryption_key: _Optional[str] = ..., vpc_access: _Optional[_Union[_vendor_settings_pb2.VpcAccess, _Mapping]] = ..., log_uri: _Optional[str] = ..., satisfies_pzs: bool = ..., etag: _Optional[str] = ...) -> None: ...

class TaskAttemptResult(_message.Message):
    __slots__ = ("status", "exit_code")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    exit_code: int
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., exit_code: _Optional[int] = ...) -> None: ...
