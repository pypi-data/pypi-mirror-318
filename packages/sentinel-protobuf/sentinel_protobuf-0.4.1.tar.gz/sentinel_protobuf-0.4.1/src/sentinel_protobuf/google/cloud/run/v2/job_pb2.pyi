from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import launch_stage_pb2 as _launch_stage_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.cloud.run.v2 import condition_pb2 as _condition_pb2
from google.cloud.run.v2 import execution_pb2 as _execution_pb2
from google.cloud.run.v2 import execution_template_pb2 as _execution_template_pb2
from google.cloud.run.v2.k8s import min_pb2 as _min_pb2
from google.cloud.run.v2 import vendor_settings_pb2 as _vendor_settings_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateJobRequest(_message.Message):
    __slots__ = ("parent", "job", "job_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    job: Job
    job_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., job: _Optional[_Union[Job, _Mapping]] = ..., job_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class GetJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateJobRequest(_message.Message):
    __slots__ = ("job", "validate_only", "allow_missing")
    JOB_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    job: Job
    validate_only: bool
    allow_missing: bool
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ..., validate_only: bool = ..., allow_missing: bool = ...) -> None: ...

class ListJobsRequest(_message.Message):
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

class ListJobsResponse(_message.Message):
    __slots__ = ("jobs", "next_page_token")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    next_page_token: str
    def __init__(self, jobs: _Optional[_Iterable[_Union[Job, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteJobRequest(_message.Message):
    __slots__ = ("name", "validate_only", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., etag: _Optional[str] = ...) -> None: ...

class RunJobRequest(_message.Message):
    __slots__ = ("name", "validate_only", "etag", "overrides")
    class Overrides(_message.Message):
        __slots__ = ("container_overrides", "task_count", "timeout")
        class ContainerOverride(_message.Message):
            __slots__ = ("name", "args", "env", "clear_args")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ARGS_FIELD_NUMBER: _ClassVar[int]
            ENV_FIELD_NUMBER: _ClassVar[int]
            CLEAR_ARGS_FIELD_NUMBER: _ClassVar[int]
            name: str
            args: _containers.RepeatedScalarFieldContainer[str]
            env: _containers.RepeatedCompositeFieldContainer[_min_pb2.EnvVar]
            clear_args: bool
            def __init__(self, name: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ..., env: _Optional[_Iterable[_Union[_min_pb2.EnvVar, _Mapping]]] = ..., clear_args: bool = ...) -> None: ...
        CONTAINER_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
        TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        container_overrides: _containers.RepeatedCompositeFieldContainer[RunJobRequest.Overrides.ContainerOverride]
        task_count: int
        timeout: _duration_pb2.Duration
        def __init__(self, container_overrides: _Optional[_Iterable[_Union[RunJobRequest.Overrides.ContainerOverride, _Mapping]]] = ..., task_count: _Optional[int] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str
    overrides: RunJobRequest.Overrides
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., etag: _Optional[str] = ..., overrides: _Optional[_Union[RunJobRequest.Overrides, _Mapping]] = ...) -> None: ...

class Job(_message.Message):
    __slots__ = ("name", "uid", "generation", "labels", "annotations", "create_time", "update_time", "delete_time", "expire_time", "creator", "last_modifier", "client", "client_version", "launch_stage", "binary_authorization", "template", "observed_generation", "terminal_condition", "conditions", "execution_count", "latest_created_execution", "reconciling", "satisfies_pzs", "start_execution_token", "run_execution_token", "etag")
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
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    BINARY_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_GENERATION_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_CONDITION_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    LATEST_CREATED_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    START_EXECUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RUN_EXECUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    generation: int
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    creator: str
    last_modifier: str
    client: str
    client_version: str
    launch_stage: _launch_stage_pb2.LaunchStage
    binary_authorization: _vendor_settings_pb2.BinaryAuthorization
    template: _execution_template_pb2.ExecutionTemplate
    observed_generation: int
    terminal_condition: _condition_pb2.Condition
    conditions: _containers.RepeatedCompositeFieldContainer[_condition_pb2.Condition]
    execution_count: int
    latest_created_execution: ExecutionReference
    reconciling: bool
    satisfies_pzs: bool
    start_execution_token: str
    run_execution_token: str
    etag: str
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., generation: _Optional[int] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creator: _Optional[str] = ..., last_modifier: _Optional[str] = ..., client: _Optional[str] = ..., client_version: _Optional[str] = ..., launch_stage: _Optional[_Union[_launch_stage_pb2.LaunchStage, str]] = ..., binary_authorization: _Optional[_Union[_vendor_settings_pb2.BinaryAuthorization, _Mapping]] = ..., template: _Optional[_Union[_execution_template_pb2.ExecutionTemplate, _Mapping]] = ..., observed_generation: _Optional[int] = ..., terminal_condition: _Optional[_Union[_condition_pb2.Condition, _Mapping]] = ..., conditions: _Optional[_Iterable[_Union[_condition_pb2.Condition, _Mapping]]] = ..., execution_count: _Optional[int] = ..., latest_created_execution: _Optional[_Union[ExecutionReference, _Mapping]] = ..., reconciling: bool = ..., satisfies_pzs: bool = ..., start_execution_token: _Optional[str] = ..., run_execution_token: _Optional[str] = ..., etag: _Optional[str] = ...) -> None: ...

class ExecutionReference(_message.Message):
    __slots__ = ("name", "create_time", "completion_time", "delete_time", "completion_status")
    class CompletionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETION_STATUS_UNSPECIFIED: _ClassVar[ExecutionReference.CompletionStatus]
        EXECUTION_SUCCEEDED: _ClassVar[ExecutionReference.CompletionStatus]
        EXECUTION_FAILED: _ClassVar[ExecutionReference.CompletionStatus]
        EXECUTION_RUNNING: _ClassVar[ExecutionReference.CompletionStatus]
        EXECUTION_PENDING: _ClassVar[ExecutionReference.CompletionStatus]
        EXECUTION_CANCELLED: _ClassVar[ExecutionReference.CompletionStatus]
    COMPLETION_STATUS_UNSPECIFIED: ExecutionReference.CompletionStatus
    EXECUTION_SUCCEEDED: ExecutionReference.CompletionStatus
    EXECUTION_FAILED: ExecutionReference.CompletionStatus
    EXECUTION_RUNNING: ExecutionReference.CompletionStatus
    EXECUTION_PENDING: ExecutionReference.CompletionStatus
    EXECUTION_CANCELLED: ExecutionReference.CompletionStatus
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    completion_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    completion_status: ExecutionReference.CompletionStatus
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_status: _Optional[_Union[ExecutionReference.CompletionStatus, str]] = ...) -> None: ...
