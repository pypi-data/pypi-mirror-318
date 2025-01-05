from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LineCoverageSummary(_message.Message):
    __slots__ = ('instrumented_line_count', 'executed_line_count')
    INSTRUMENTED_LINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_LINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    instrumented_line_count: int
    executed_line_count: int

    def __init__(self, instrumented_line_count: _Optional[int]=..., executed_line_count: _Optional[int]=...) -> None:
        ...

class BranchCoverageSummary(_message.Message):
    __slots__ = ('total_branch_count', 'executed_branch_count', 'taken_branch_count')
    TOTAL_BRANCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_BRANCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    TAKEN_BRANCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    total_branch_count: int
    executed_branch_count: int
    taken_branch_count: int

    def __init__(self, total_branch_count: _Optional[int]=..., executed_branch_count: _Optional[int]=..., taken_branch_count: _Optional[int]=...) -> None:
        ...

class LanguageCoverageSummary(_message.Message):
    __slots__ = ('language', 'line_summary', 'branch_summary')
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LINE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    BRANCH_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    language: _common_pb2.Language
    line_summary: LineCoverageSummary
    branch_summary: BranchCoverageSummary

    def __init__(self, language: _Optional[_Union[_common_pb2.Language, str]]=..., line_summary: _Optional[_Union[LineCoverageSummary, _Mapping]]=..., branch_summary: _Optional[_Union[BranchCoverageSummary, _Mapping]]=...) -> None:
        ...