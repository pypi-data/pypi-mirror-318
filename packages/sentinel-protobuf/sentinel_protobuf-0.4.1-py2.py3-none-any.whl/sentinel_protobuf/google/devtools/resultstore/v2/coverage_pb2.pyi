from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LineCoverage(_message.Message):
    __slots__ = ('instrumented_lines', 'executed_lines')
    INSTRUMENTED_LINES_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_LINES_FIELD_NUMBER: _ClassVar[int]
    instrumented_lines: bytes
    executed_lines: bytes

    def __init__(self, instrumented_lines: _Optional[bytes]=..., executed_lines: _Optional[bytes]=...) -> None:
        ...

class BranchCoverage(_message.Message):
    __slots__ = ('branch_present', 'branches_in_line', 'executed', 'taken')
    BRANCH_PRESENT_FIELD_NUMBER: _ClassVar[int]
    BRANCHES_IN_LINE_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_FIELD_NUMBER: _ClassVar[int]
    TAKEN_FIELD_NUMBER: _ClassVar[int]
    branch_present: bytes
    branches_in_line: _containers.RepeatedScalarFieldContainer[int]
    executed: bytes
    taken: bytes

    def __init__(self, branch_present: _Optional[bytes]=..., branches_in_line: _Optional[_Iterable[int]]=..., executed: _Optional[bytes]=..., taken: _Optional[bytes]=...) -> None:
        ...

class FileCoverage(_message.Message):
    __slots__ = ('path', 'line_coverage', 'branch_coverage')
    PATH_FIELD_NUMBER: _ClassVar[int]
    LINE_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    BRANCH_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    line_coverage: LineCoverage
    branch_coverage: BranchCoverage

    def __init__(self, path: _Optional[str]=..., line_coverage: _Optional[_Union[LineCoverage, _Mapping]]=..., branch_coverage: _Optional[_Union[BranchCoverage, _Mapping]]=...) -> None:
        ...

class ActionCoverage(_message.Message):
    __slots__ = ('file_coverages',)
    FILE_COVERAGES_FIELD_NUMBER: _ClassVar[int]
    file_coverages: _containers.RepeatedCompositeFieldContainer[FileCoverage]

    def __init__(self, file_coverages: _Optional[_Iterable[_Union[FileCoverage, _Mapping]]]=...) -> None:
        ...

class AggregateCoverage(_message.Message):
    __slots__ = ('file_coverages',)
    FILE_COVERAGES_FIELD_NUMBER: _ClassVar[int]
    file_coverages: _containers.RepeatedCompositeFieldContainer[FileCoverage]

    def __init__(self, file_coverages: _Optional[_Iterable[_Union[FileCoverage, _Mapping]]]=...) -> None:
        ...