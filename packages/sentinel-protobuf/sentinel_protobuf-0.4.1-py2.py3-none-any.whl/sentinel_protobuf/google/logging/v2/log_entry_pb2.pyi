from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.api import resource_pb2 as _resource_pb2
from google.logging.type import http_request_pb2 as _http_request_pb2
from google.logging.type import log_severity_pb2 as _log_severity_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LogEntry(_message.Message):
    __slots__ = ('log_name', 'resource', 'proto_payload', 'text_payload', 'json_payload', 'timestamp', 'receive_timestamp', 'severity', 'insert_id', 'http_request', 'labels', 'operation', 'trace', 'span_id', 'trace_sampled', 'source_location', 'split')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    LOG_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PROTO_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TEXT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    JSON_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    INSERT_ID_FIELD_NUMBER: _ClassVar[int]
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TRACE_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_SAMPLED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    log_name: str
    resource: _monitored_resource_pb2.MonitoredResource
    proto_payload: _any_pb2.Any
    text_payload: str
    json_payload: _struct_pb2.Struct
    timestamp: _timestamp_pb2.Timestamp
    receive_timestamp: _timestamp_pb2.Timestamp
    severity: _log_severity_pb2.LogSeverity
    insert_id: str
    http_request: _http_request_pb2.HttpRequest
    labels: _containers.ScalarMap[str, str]
    operation: LogEntryOperation
    trace: str
    span_id: str
    trace_sampled: bool
    source_location: LogEntrySourceLocation
    split: LogSplit

    def __init__(self, log_name: _Optional[str]=..., resource: _Optional[_Union[_monitored_resource_pb2.MonitoredResource, _Mapping]]=..., proto_payload: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., text_payload: _Optional[str]=..., json_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., receive_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., severity: _Optional[_Union[_log_severity_pb2.LogSeverity, str]]=..., insert_id: _Optional[str]=..., http_request: _Optional[_Union[_http_request_pb2.HttpRequest, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., operation: _Optional[_Union[LogEntryOperation, _Mapping]]=..., trace: _Optional[str]=..., span_id: _Optional[str]=..., trace_sampled: bool=..., source_location: _Optional[_Union[LogEntrySourceLocation, _Mapping]]=..., split: _Optional[_Union[LogSplit, _Mapping]]=...) -> None:
        ...

class LogEntryOperation(_message.Message):
    __slots__ = ('id', 'producer', 'first', 'last')
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    id: str
    producer: str
    first: bool
    last: bool

    def __init__(self, id: _Optional[str]=..., producer: _Optional[str]=..., first: bool=..., last: bool=...) -> None:
        ...

class LogEntrySourceLocation(_message.Message):
    __slots__ = ('file', 'line', 'function')
    FILE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    file: str
    line: int
    function: str

    def __init__(self, file: _Optional[str]=..., line: _Optional[int]=..., function: _Optional[str]=...) -> None:
        ...

class LogSplit(_message.Message):
    __slots__ = ('uid', 'index', 'total_splits')
    UID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SPLITS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    index: int
    total_splits: int

    def __init__(self, uid: _Optional[str]=..., index: _Optional[int]=..., total_splits: _Optional[int]=...) -> None:
        ...