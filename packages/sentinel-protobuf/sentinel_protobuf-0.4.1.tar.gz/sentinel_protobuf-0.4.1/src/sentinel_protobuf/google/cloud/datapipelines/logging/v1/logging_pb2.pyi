from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RequestLogEntry(_message.Message):
    __slots__ = ('request_type', 'status', 'error_cause')

    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUEST_TYPE_UNSPECIFIED: _ClassVar[RequestLogEntry.RequestType]
        CREATE_PIPELINE: _ClassVar[RequestLogEntry.RequestType]
        UPDATE_PIPELINE: _ClassVar[RequestLogEntry.RequestType]
        DELETE_PIPELINE: _ClassVar[RequestLogEntry.RequestType]
        LIST_PIPELINES: _ClassVar[RequestLogEntry.RequestType]
        GET_PIPELINE: _ClassVar[RequestLogEntry.RequestType]
        STOP_PIPELINE: _ClassVar[RequestLogEntry.RequestType]
        RUN_PIPELINE: _ClassVar[RequestLogEntry.RequestType]
        LIST_JOBS: _ClassVar[RequestLogEntry.RequestType]
    REQUEST_TYPE_UNSPECIFIED: RequestLogEntry.RequestType
    CREATE_PIPELINE: RequestLogEntry.RequestType
    UPDATE_PIPELINE: RequestLogEntry.RequestType
    DELETE_PIPELINE: RequestLogEntry.RequestType
    LIST_PIPELINES: RequestLogEntry.RequestType
    GET_PIPELINE: RequestLogEntry.RequestType
    STOP_PIPELINE: RequestLogEntry.RequestType
    RUN_PIPELINE: RequestLogEntry.RequestType
    LIST_JOBS: RequestLogEntry.RequestType

    class ErrorCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CAUSE_UNSPECIFIED: _ClassVar[RequestLogEntry.ErrorCause]
        INVALID_REQUEST: _ClassVar[RequestLogEntry.ErrorCause]
        PROJECT_NUMBER_NOT_FOUND: _ClassVar[RequestLogEntry.ErrorCause]
        PIPELINE_ID_ALREADY_EXISTS: _ClassVar[RequestLogEntry.ErrorCause]
        PIPELINE_QUOTA_ALLOCATION_FAILED: _ClassVar[RequestLogEntry.ErrorCause]
        PIPELINE_NOT_FOUND: _ClassVar[RequestLogEntry.ErrorCause]
        INVALID_PIPELINE_WORKLOAD: _ClassVar[RequestLogEntry.ErrorCause]
        DATAFLOW_WORKER_SERVICE_ACCOUNT_PERMISSION_DENIED: _ClassVar[RequestLogEntry.ErrorCause]
        CLOUD_SCHEDULER_SERVICE_ACCOUNT_PERMISSION_DENIED: _ClassVar[RequestLogEntry.ErrorCause]
        INTERNAL_DATA_PIPELINES_SERVICE_ACCOUNT_ISSUE: _ClassVar[RequestLogEntry.ErrorCause]
        CLOUD_SCHEDULER_INVALID_ARGUMENT: _ClassVar[RequestLogEntry.ErrorCause]
        CLOUD_SCHEDULER_RESOURCE_EXHAUSTED: _ClassVar[RequestLogEntry.ErrorCause]
        CLOUD_SCHEDULER_JOB_NOT_FOUND: _ClassVar[RequestLogEntry.ErrorCause]
        OTHER_CLOUD_SCHEDULER_ISSUE: _ClassVar[RequestLogEntry.ErrorCause]
        DATAFLOW_JOB_ALREADY_EXISTS: _ClassVar[RequestLogEntry.ErrorCause]
        DATAFLOW_INVALID_ARGUMENT: _ClassVar[RequestLogEntry.ErrorCause]
        DATAFLOW_RESOURCE_EXHAUSTED: _ClassVar[RequestLogEntry.ErrorCause]
        DATAFLOW_JOB_NOT_FOUND: _ClassVar[RequestLogEntry.ErrorCause]
        OTHER_DATAFLOW_ISSUE: _ClassVar[RequestLogEntry.ErrorCause]
        DATABASE_ERROR: _ClassVar[RequestLogEntry.ErrorCause]
        WRONG_PIPELINE_TYPE: _ClassVar[RequestLogEntry.ErrorCause]
        INTERNAL_ERROR: _ClassVar[RequestLogEntry.ErrorCause]
        PIPELINE_OR_PROJECT_NOT_FOUND: _ClassVar[RequestLogEntry.ErrorCause]
    ERROR_CAUSE_UNSPECIFIED: RequestLogEntry.ErrorCause
    INVALID_REQUEST: RequestLogEntry.ErrorCause
    PROJECT_NUMBER_NOT_FOUND: RequestLogEntry.ErrorCause
    PIPELINE_ID_ALREADY_EXISTS: RequestLogEntry.ErrorCause
    PIPELINE_QUOTA_ALLOCATION_FAILED: RequestLogEntry.ErrorCause
    PIPELINE_NOT_FOUND: RequestLogEntry.ErrorCause
    INVALID_PIPELINE_WORKLOAD: RequestLogEntry.ErrorCause
    DATAFLOW_WORKER_SERVICE_ACCOUNT_PERMISSION_DENIED: RequestLogEntry.ErrorCause
    CLOUD_SCHEDULER_SERVICE_ACCOUNT_PERMISSION_DENIED: RequestLogEntry.ErrorCause
    INTERNAL_DATA_PIPELINES_SERVICE_ACCOUNT_ISSUE: RequestLogEntry.ErrorCause
    CLOUD_SCHEDULER_INVALID_ARGUMENT: RequestLogEntry.ErrorCause
    CLOUD_SCHEDULER_RESOURCE_EXHAUSTED: RequestLogEntry.ErrorCause
    CLOUD_SCHEDULER_JOB_NOT_FOUND: RequestLogEntry.ErrorCause
    OTHER_CLOUD_SCHEDULER_ISSUE: RequestLogEntry.ErrorCause
    DATAFLOW_JOB_ALREADY_EXISTS: RequestLogEntry.ErrorCause
    DATAFLOW_INVALID_ARGUMENT: RequestLogEntry.ErrorCause
    DATAFLOW_RESOURCE_EXHAUSTED: RequestLogEntry.ErrorCause
    DATAFLOW_JOB_NOT_FOUND: RequestLogEntry.ErrorCause
    OTHER_DATAFLOW_ISSUE: RequestLogEntry.ErrorCause
    DATABASE_ERROR: RequestLogEntry.ErrorCause
    WRONG_PIPELINE_TYPE: RequestLogEntry.ErrorCause
    INTERNAL_ERROR: RequestLogEntry.ErrorCause
    PIPELINE_OR_PROJECT_NOT_FOUND: RequestLogEntry.ErrorCause
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
    request_type: RequestLogEntry.RequestType
    status: _status_pb2.Status
    error_cause: RequestLogEntry.ErrorCause

    def __init__(self, request_type: _Optional[_Union[RequestLogEntry.RequestType, str]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., error_cause: _Optional[_Union[RequestLogEntry.ErrorCause, str]]=...) -> None:
        ...