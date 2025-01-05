from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScanRun(_message.Message):
    __slots__ = ('name', 'execution_state', 'result_state', 'start_time', 'end_time', 'urls_crawled_count', 'urls_tested_count', 'has_vulnerabilities', 'progress_percent')

    class ExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXECUTION_STATE_UNSPECIFIED: _ClassVar[ScanRun.ExecutionState]
        QUEUED: _ClassVar[ScanRun.ExecutionState]
        SCANNING: _ClassVar[ScanRun.ExecutionState]
        FINISHED: _ClassVar[ScanRun.ExecutionState]
    EXECUTION_STATE_UNSPECIFIED: ScanRun.ExecutionState
    QUEUED: ScanRun.ExecutionState
    SCANNING: ScanRun.ExecutionState
    FINISHED: ScanRun.ExecutionState

    class ResultState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_STATE_UNSPECIFIED: _ClassVar[ScanRun.ResultState]
        SUCCESS: _ClassVar[ScanRun.ResultState]
        ERROR: _ClassVar[ScanRun.ResultState]
        KILLED: _ClassVar[ScanRun.ResultState]
    RESULT_STATE_UNSPECIFIED: ScanRun.ResultState
    SUCCESS: ScanRun.ResultState
    ERROR: ScanRun.ResultState
    KILLED: ScanRun.ResultState
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    URLS_CRAWLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    URLS_TESTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_VULNERABILITIES_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    execution_state: ScanRun.ExecutionState
    result_state: ScanRun.ResultState
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    urls_crawled_count: int
    urls_tested_count: int
    has_vulnerabilities: bool
    progress_percent: int

    def __init__(self, name: _Optional[str]=..., execution_state: _Optional[_Union[ScanRun.ExecutionState, str]]=..., result_state: _Optional[_Union[ScanRun.ResultState, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., urls_crawled_count: _Optional[int]=..., urls_tested_count: _Optional[int]=..., has_vulnerabilities: bool=..., progress_percent: _Optional[int]=...) -> None:
        ...