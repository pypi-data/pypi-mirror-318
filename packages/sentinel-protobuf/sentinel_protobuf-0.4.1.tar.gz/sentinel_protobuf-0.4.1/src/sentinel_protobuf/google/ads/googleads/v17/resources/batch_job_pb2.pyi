from google.ads.googleads.v17.enums import batch_job_status_pb2 as _batch_job_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchJob(_message.Message):
    __slots__ = ("resource_name", "id", "next_add_sequence_token", "metadata", "status", "long_running_operation")
    class BatchJobMetadata(_message.Message):
        __slots__ = ("creation_date_time", "start_date_time", "completion_date_time", "estimated_completion_ratio", "operation_count", "executed_operation_count", "execution_limit_seconds")
        CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_COMPLETION_RATIO_FIELD_NUMBER: _ClassVar[int]
        OPERATION_COUNT_FIELD_NUMBER: _ClassVar[int]
        EXECUTED_OPERATION_COUNT_FIELD_NUMBER: _ClassVar[int]
        EXECUTION_LIMIT_SECONDS_FIELD_NUMBER: _ClassVar[int]
        creation_date_time: str
        start_date_time: str
        completion_date_time: str
        estimated_completion_ratio: float
        operation_count: int
        executed_operation_count: int
        execution_limit_seconds: int
        def __init__(self, creation_date_time: _Optional[str] = ..., start_date_time: _Optional[str] = ..., completion_date_time: _Optional[str] = ..., estimated_completion_ratio: _Optional[float] = ..., operation_count: _Optional[int] = ..., executed_operation_count: _Optional[int] = ..., execution_limit_seconds: _Optional[int] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_ADD_SEQUENCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LONG_RUNNING_OPERATION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    next_add_sequence_token: str
    metadata: BatchJob.BatchJobMetadata
    status: _batch_job_status_pb2.BatchJobStatusEnum.BatchJobStatus
    long_running_operation: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., next_add_sequence_token: _Optional[str] = ..., metadata: _Optional[_Union[BatchJob.BatchJobMetadata, _Mapping]] = ..., status: _Optional[_Union[_batch_job_status_pb2.BatchJobStatusEnum.BatchJobStatus, str]] = ..., long_running_operation: _Optional[str] = ...) -> None: ...
