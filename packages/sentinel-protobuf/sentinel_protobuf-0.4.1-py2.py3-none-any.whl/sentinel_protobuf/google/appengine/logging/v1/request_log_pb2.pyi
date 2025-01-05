from google.logging.type import log_severity_pb2 as _log_severity_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LogLine(_message.Message):
    __slots__ = ('time', 'severity', 'log_message', 'source_location')
    TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    LOG_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    severity: _log_severity_pb2.LogSeverity
    log_message: str
    source_location: SourceLocation

    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., severity: _Optional[_Union[_log_severity_pb2.LogSeverity, str]]=..., log_message: _Optional[str]=..., source_location: _Optional[_Union[SourceLocation, _Mapping]]=...) -> None:
        ...

class SourceLocation(_message.Message):
    __slots__ = ('file', 'line', 'function_name')
    FILE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    file: str
    line: int
    function_name: str

    def __init__(self, file: _Optional[str]=..., line: _Optional[int]=..., function_name: _Optional[str]=...) -> None:
        ...

class SourceReference(_message.Message):
    __slots__ = ('repository', 'revision_id')
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    repository: str
    revision_id: str

    def __init__(self, repository: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
        ...

class RequestLog(_message.Message):
    __slots__ = ('app_id', 'module_id', 'version_id', 'request_id', 'ip', 'start_time', 'end_time', 'latency', 'mega_cycles', 'method', 'resource', 'http_version', 'status', 'response_size', 'referrer', 'user_agent', 'nickname', 'url_map_entry', 'host', 'cost', 'task_queue_name', 'task_name', 'was_loading_request', 'pending_time', 'instance_index', 'finished', 'first', 'instance_id', 'line', 'app_engine_release', 'trace_id', 'trace_sampled', 'source_reference')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    MEGA_CYCLES_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    HTTP_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_SIZE_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    URL_MAP_ENTRY_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TASK_QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    WAS_LOADING_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PENDING_TIME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_INDEX_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_RELEASE_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_SAMPLED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    module_id: str
    version_id: str
    request_id: str
    ip: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    latency: _duration_pb2.Duration
    mega_cycles: int
    method: str
    resource: str
    http_version: str
    status: int
    response_size: int
    referrer: str
    user_agent: str
    nickname: str
    url_map_entry: str
    host: str
    cost: float
    task_queue_name: str
    task_name: str
    was_loading_request: bool
    pending_time: _duration_pb2.Duration
    instance_index: int
    finished: bool
    first: bool
    instance_id: str
    line: _containers.RepeatedCompositeFieldContainer[LogLine]
    app_engine_release: str
    trace_id: str
    trace_sampled: bool
    source_reference: _containers.RepeatedCompositeFieldContainer[SourceReference]

    def __init__(self, app_id: _Optional[str]=..., module_id: _Optional[str]=..., version_id: _Optional[str]=..., request_id: _Optional[str]=..., ip: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., mega_cycles: _Optional[int]=..., method: _Optional[str]=..., resource: _Optional[str]=..., http_version: _Optional[str]=..., status: _Optional[int]=..., response_size: _Optional[int]=..., referrer: _Optional[str]=..., user_agent: _Optional[str]=..., nickname: _Optional[str]=..., url_map_entry: _Optional[str]=..., host: _Optional[str]=..., cost: _Optional[float]=..., task_queue_name: _Optional[str]=..., task_name: _Optional[str]=..., was_loading_request: bool=..., pending_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., instance_index: _Optional[int]=..., finished: bool=..., first: bool=..., instance_id: _Optional[str]=..., line: _Optional[_Iterable[_Union[LogLine, _Mapping]]]=..., app_engine_release: _Optional[str]=..., trace_id: _Optional[str]=..., trace_sampled: bool=..., source_reference: _Optional[_Iterable[_Union[SourceReference, _Mapping]]]=...) -> None:
        ...