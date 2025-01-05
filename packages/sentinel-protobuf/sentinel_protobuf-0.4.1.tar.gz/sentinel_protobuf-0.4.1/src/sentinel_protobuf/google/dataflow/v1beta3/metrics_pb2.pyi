from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_STATE_UNKNOWN: _ClassVar[ExecutionState]
    EXECUTION_STATE_NOT_STARTED: _ClassVar[ExecutionState]
    EXECUTION_STATE_RUNNING: _ClassVar[ExecutionState]
    EXECUTION_STATE_SUCCEEDED: _ClassVar[ExecutionState]
    EXECUTION_STATE_FAILED: _ClassVar[ExecutionState]
    EXECUTION_STATE_CANCELLED: _ClassVar[ExecutionState]
EXECUTION_STATE_UNKNOWN: ExecutionState
EXECUTION_STATE_NOT_STARTED: ExecutionState
EXECUTION_STATE_RUNNING: ExecutionState
EXECUTION_STATE_SUCCEEDED: ExecutionState
EXECUTION_STATE_FAILED: ExecutionState
EXECUTION_STATE_CANCELLED: ExecutionState

class MetricStructuredName(_message.Message):
    __slots__ = ('origin', 'name', 'context')

    class ContextEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    origin: str
    name: str
    context: _containers.ScalarMap[str, str]

    def __init__(self, origin: _Optional[str]=..., name: _Optional[str]=..., context: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class MetricUpdate(_message.Message):
    __slots__ = ('name', 'kind', 'cumulative', 'scalar', 'mean_sum', 'mean_count', 'set', 'distribution', 'gauge', 'internal', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_FIELD_NUMBER: _ClassVar[int]
    SCALAR_FIELD_NUMBER: _ClassVar[int]
    MEAN_SUM_FIELD_NUMBER: _ClassVar[int]
    MEAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    GAUGE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: MetricStructuredName
    kind: str
    cumulative: bool
    scalar: _struct_pb2.Value
    mean_sum: _struct_pb2.Value
    mean_count: _struct_pb2.Value
    set: _struct_pb2.Value
    distribution: _struct_pb2.Value
    gauge: _struct_pb2.Value
    internal: _struct_pb2.Value
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[_Union[MetricStructuredName, _Mapping]]=..., kind: _Optional[str]=..., cumulative: bool=..., scalar: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., mean_sum: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., mean_count: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., set: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., distribution: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., gauge: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., internal: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetJobMetricsRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'start_time', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    start_time: _timestamp_pb2.Timestamp
    location: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., location: _Optional[str]=...) -> None:
        ...

class JobMetrics(_message.Message):
    __slots__ = ('metric_time', 'metrics')
    METRIC_TIME_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metric_time: _timestamp_pb2.Timestamp
    metrics: _containers.RepeatedCompositeFieldContainer[MetricUpdate]

    def __init__(self, metric_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., metrics: _Optional[_Iterable[_Union[MetricUpdate, _Mapping]]]=...) -> None:
        ...

class GetJobExecutionDetailsRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'location', 'page_size', 'page_token')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str
    page_size: int
    page_token: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., location: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ProgressTimeseries(_message.Message):
    __slots__ = ('current_progress', 'data_points')

    class Point(_message.Message):
        __slots__ = ('time', 'value')
        TIME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        time: _timestamp_pb2.Timestamp
        value: float

        def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., value: _Optional[float]=...) -> None:
            ...
    CURRENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    current_progress: float
    data_points: _containers.RepeatedCompositeFieldContainer[ProgressTimeseries.Point]

    def __init__(self, current_progress: _Optional[float]=..., data_points: _Optional[_Iterable[_Union[ProgressTimeseries.Point, _Mapping]]]=...) -> None:
        ...

class StageSummary(_message.Message):
    __slots__ = ('stage_id', 'state', 'start_time', 'end_time', 'progress', 'metrics')
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    stage_id: str
    state: ExecutionState
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    progress: ProgressTimeseries
    metrics: _containers.RepeatedCompositeFieldContainer[MetricUpdate]

    def __init__(self, stage_id: _Optional[str]=..., state: _Optional[_Union[ExecutionState, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., progress: _Optional[_Union[ProgressTimeseries, _Mapping]]=..., metrics: _Optional[_Iterable[_Union[MetricUpdate, _Mapping]]]=...) -> None:
        ...

class JobExecutionDetails(_message.Message):
    __slots__ = ('stages', 'next_page_token')
    STAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    stages: _containers.RepeatedCompositeFieldContainer[StageSummary]
    next_page_token: str

    def __init__(self, stages: _Optional[_Iterable[_Union[StageSummary, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetStageExecutionDetailsRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'location', 'stage_id', 'page_size', 'page_token', 'start_time', 'end_time')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str
    stage_id: str
    page_size: int
    page_token: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., location: _Optional[str]=..., stage_id: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class WorkItemDetails(_message.Message):
    __slots__ = ('task_id', 'attempt_id', 'start_time', 'end_time', 'state', 'progress', 'metrics')
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    attempt_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: ExecutionState
    progress: ProgressTimeseries
    metrics: _containers.RepeatedCompositeFieldContainer[MetricUpdate]

    def __init__(self, task_id: _Optional[str]=..., attempt_id: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ExecutionState, str]]=..., progress: _Optional[_Union[ProgressTimeseries, _Mapping]]=..., metrics: _Optional[_Iterable[_Union[MetricUpdate, _Mapping]]]=...) -> None:
        ...

class WorkerDetails(_message.Message):
    __slots__ = ('worker_name', 'work_items')
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    WORK_ITEMS_FIELD_NUMBER: _ClassVar[int]
    worker_name: str
    work_items: _containers.RepeatedCompositeFieldContainer[WorkItemDetails]

    def __init__(self, worker_name: _Optional[str]=..., work_items: _Optional[_Iterable[_Union[WorkItemDetails, _Mapping]]]=...) -> None:
        ...

class StageExecutionDetails(_message.Message):
    __slots__ = ('workers', 'next_page_token')
    WORKERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workers: _containers.RepeatedCompositeFieldContainer[WorkerDetails]
    next_page_token: str

    def __init__(self, workers: _Optional[_Iterable[_Union[WorkerDetails, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...