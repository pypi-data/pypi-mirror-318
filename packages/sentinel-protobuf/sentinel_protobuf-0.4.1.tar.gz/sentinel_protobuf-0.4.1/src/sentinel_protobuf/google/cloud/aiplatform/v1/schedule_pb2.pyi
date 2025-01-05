from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import notebook_service_pb2 as _notebook_service_pb2
from google.cloud.aiplatform.v1 import pipeline_service_pb2 as _pipeline_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Schedule(_message.Message):
    __slots__ = ("cron", "create_pipeline_job_request", "create_notebook_execution_job_request", "name", "display_name", "start_time", "end_time", "max_run_count", "started_run_count", "state", "create_time", "update_time", "next_run_time", "last_pause_time", "last_resume_time", "max_concurrent_run_count", "allow_queueing", "catch_up", "last_scheduled_run_response")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Schedule.State]
        ACTIVE: _ClassVar[Schedule.State]
        PAUSED: _ClassVar[Schedule.State]
        COMPLETED: _ClassVar[Schedule.State]
    STATE_UNSPECIFIED: Schedule.State
    ACTIVE: Schedule.State
    PAUSED: Schedule.State
    COMPLETED: Schedule.State
    class RunResponse(_message.Message):
        __slots__ = ("scheduled_run_time", "run_response")
        SCHEDULED_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
        RUN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        scheduled_run_time: _timestamp_pb2.Timestamp
        run_response: str
        def __init__(self, scheduled_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., run_response: _Optional[str] = ...) -> None: ...
    CRON_FIELD_NUMBER: _ClassVar[int]
    CREATE_PIPELINE_JOB_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATE_NOTEBOOK_EXECUTION_JOB_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    STARTED_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_RESUME_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_QUEUEING_FIELD_NUMBER: _ClassVar[int]
    CATCH_UP_FIELD_NUMBER: _ClassVar[int]
    LAST_SCHEDULED_RUN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    cron: str
    create_pipeline_job_request: _pipeline_service_pb2.CreatePipelineJobRequest
    create_notebook_execution_job_request: _notebook_service_pb2.CreateNotebookExecutionJobRequest
    name: str
    display_name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    max_run_count: int
    started_run_count: int
    state: Schedule.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    next_run_time: _timestamp_pb2.Timestamp
    last_pause_time: _timestamp_pb2.Timestamp
    last_resume_time: _timestamp_pb2.Timestamp
    max_concurrent_run_count: int
    allow_queueing: bool
    catch_up: bool
    last_scheduled_run_response: Schedule.RunResponse
    def __init__(self, cron: _Optional[str] = ..., create_pipeline_job_request: _Optional[_Union[_pipeline_service_pb2.CreatePipelineJobRequest, _Mapping]] = ..., create_notebook_execution_job_request: _Optional[_Union[_notebook_service_pb2.CreateNotebookExecutionJobRequest, _Mapping]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max_run_count: _Optional[int] = ..., started_run_count: _Optional[int] = ..., state: _Optional[_Union[Schedule.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_pause_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_resume_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max_concurrent_run_count: _Optional[int] = ..., allow_queueing: bool = ..., catch_up: bool = ..., last_scheduled_run_response: _Optional[_Union[Schedule.RunResponse, _Mapping]] = ...) -> None: ...
