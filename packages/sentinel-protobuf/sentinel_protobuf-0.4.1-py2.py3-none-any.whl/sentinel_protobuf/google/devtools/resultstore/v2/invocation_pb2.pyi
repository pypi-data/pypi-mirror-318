from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.devtools.resultstore.v2 import coverage_pb2 as _coverage_pb2
from google.devtools.resultstore.v2 import coverage_summary_pb2 as _coverage_summary_pb2
from google.devtools.resultstore.v2 import file_pb2 as _file_pb2
from google.devtools.resultstore.v2 import file_processing_error_pb2 as _file_processing_error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Invocation(_message.Message):
    __slots__ = ('name', 'id', 'status_attributes', 'timing', 'invocation_attributes', 'workspace_info', 'properties', 'files', 'coverage_summaries', 'aggregate_coverage', 'file_processing_errors')

    class Id(_message.Message):
        __slots__ = ('invocation_id',)
        INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        invocation_id: str

        def __init__(self, invocation_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_PROCESSING_ERRORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: Invocation.Id
    status_attributes: _common_pb2.StatusAttributes
    timing: _common_pb2.Timing
    invocation_attributes: InvocationAttributes
    workspace_info: WorkspaceInfo
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.Property]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    coverage_summaries: _containers.RepeatedCompositeFieldContainer[_coverage_summary_pb2.LanguageCoverageSummary]
    aggregate_coverage: _coverage_pb2.AggregateCoverage
    file_processing_errors: _containers.RepeatedCompositeFieldContainer[_file_processing_error_pb2.FileProcessingErrors]

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[Invocation.Id, _Mapping]]=..., status_attributes: _Optional[_Union[_common_pb2.StatusAttributes, _Mapping]]=..., timing: _Optional[_Union[_common_pb2.Timing, _Mapping]]=..., invocation_attributes: _Optional[_Union[InvocationAttributes, _Mapping]]=..., workspace_info: _Optional[_Union[WorkspaceInfo, _Mapping]]=..., properties: _Optional[_Iterable[_Union[_common_pb2.Property, _Mapping]]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=..., coverage_summaries: _Optional[_Iterable[_Union[_coverage_summary_pb2.LanguageCoverageSummary, _Mapping]]]=..., aggregate_coverage: _Optional[_Union[_coverage_pb2.AggregateCoverage, _Mapping]]=..., file_processing_errors: _Optional[_Iterable[_Union[_file_processing_error_pb2.FileProcessingErrors, _Mapping]]]=...) -> None:
        ...

class WorkspaceContext(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WorkspaceInfo(_message.Message):
    __slots__ = ('workspace_context', 'hostname', 'working_directory', 'tool_tag', 'command_lines')
    WORKSPACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    TOOL_TAG_FIELD_NUMBER: _ClassVar[int]
    COMMAND_LINES_FIELD_NUMBER: _ClassVar[int]
    workspace_context: WorkspaceContext
    hostname: str
    working_directory: str
    tool_tag: str
    command_lines: _containers.RepeatedCompositeFieldContainer[CommandLine]

    def __init__(self, workspace_context: _Optional[_Union[WorkspaceContext, _Mapping]]=..., hostname: _Optional[str]=..., working_directory: _Optional[str]=..., tool_tag: _Optional[str]=..., command_lines: _Optional[_Iterable[_Union[CommandLine, _Mapping]]]=...) -> None:
        ...

class CommandLine(_message.Message):
    __slots__ = ('label', 'tool', 'args', 'command')
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    label: str
    tool: str
    args: _containers.RepeatedScalarFieldContainer[str]
    command: str

    def __init__(self, label: _Optional[str]=..., tool: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., command: _Optional[str]=...) -> None:
        ...

class InvocationAttributes(_message.Message):
    __slots__ = ('project_id', 'users', 'labels', 'description', 'invocation_contexts', 'exit_code')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    users: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.RepeatedScalarFieldContainer[str]
    description: str
    invocation_contexts: _containers.RepeatedCompositeFieldContainer[InvocationContext]
    exit_code: int

    def __init__(self, project_id: _Optional[str]=..., users: _Optional[_Iterable[str]]=..., labels: _Optional[_Iterable[str]]=..., description: _Optional[str]=..., invocation_contexts: _Optional[_Iterable[_Union[InvocationContext, _Mapping]]]=..., exit_code: _Optional[int]=...) -> None:
        ...

class InvocationContext(_message.Message):
    __slots__ = ('display_name', 'url')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    url: str

    def __init__(self, display_name: _Optional[str]=..., url: _Optional[str]=...) -> None:
        ...