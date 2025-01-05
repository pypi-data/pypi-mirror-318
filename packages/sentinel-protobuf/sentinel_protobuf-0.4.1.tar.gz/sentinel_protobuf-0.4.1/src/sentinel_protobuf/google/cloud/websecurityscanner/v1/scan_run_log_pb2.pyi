from google.cloud.websecurityscanner.v1 import scan_run_pb2 as _scan_run_pb2
from google.cloud.websecurityscanner.v1 import scan_run_error_trace_pb2 as _scan_run_error_trace_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScanRunLog(_message.Message):
    __slots__ = ('summary', 'name', 'execution_state', 'result_state', 'urls_crawled_count', 'urls_tested_count', 'has_findings', 'error_trace')
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_STATE_FIELD_NUMBER: _ClassVar[int]
    URLS_CRAWLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    URLS_TESTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_TRACE_FIELD_NUMBER: _ClassVar[int]
    summary: str
    name: str
    execution_state: _scan_run_pb2.ScanRun.ExecutionState
    result_state: _scan_run_pb2.ScanRun.ResultState
    urls_crawled_count: int
    urls_tested_count: int
    has_findings: bool
    error_trace: _scan_run_error_trace_pb2.ScanRunErrorTrace

    def __init__(self, summary: _Optional[str]=..., name: _Optional[str]=..., execution_state: _Optional[_Union[_scan_run_pb2.ScanRun.ExecutionState, str]]=..., result_state: _Optional[_Union[_scan_run_pb2.ScanRun.ResultState, str]]=..., urls_crawled_count: _Optional[int]=..., urls_tested_count: _Optional[int]=..., has_findings: bool=..., error_trace: _Optional[_Union[_scan_run_error_trace_pb2.ScanRunErrorTrace, _Mapping]]=...) -> None:
        ...