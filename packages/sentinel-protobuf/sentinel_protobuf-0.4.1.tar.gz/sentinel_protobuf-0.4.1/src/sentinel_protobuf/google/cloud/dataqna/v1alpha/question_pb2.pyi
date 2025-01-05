from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataqna.v1alpha import annotated_string_pb2 as _annotated_string_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InterpretEntity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERPRET_ENTITY_UNSPECIFIED: _ClassVar[InterpretEntity]
    DIMENSION: _ClassVar[InterpretEntity]
    METRIC: _ClassVar[InterpretEntity]
INTERPRET_ENTITY_UNSPECIFIED: InterpretEntity
DIMENSION: InterpretEntity
METRIC: InterpretEntity

class Question(_message.Message):
    __slots__ = ('name', 'scopes', 'query', 'data_source_annotations', 'interpret_error', 'interpretations', 'create_time', 'user_email', 'debug_flags', 'debug_info')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    INTERPRET_ERROR_FIELD_NUMBER: _ClassVar[int]
    INTERPRETATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    query: str
    data_source_annotations: _containers.RepeatedScalarFieldContainer[str]
    interpret_error: InterpretError
    interpretations: _containers.RepeatedCompositeFieldContainer[Interpretation]
    create_time: _timestamp_pb2.Timestamp
    user_email: str
    debug_flags: DebugFlags
    debug_info: _any_pb2.Any

    def __init__(self, name: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=..., query: _Optional[str]=..., data_source_annotations: _Optional[_Iterable[str]]=..., interpret_error: _Optional[_Union[InterpretError, _Mapping]]=..., interpretations: _Optional[_Iterable[_Union[Interpretation, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., user_email: _Optional[str]=..., debug_flags: _Optional[_Union[DebugFlags, _Mapping]]=..., debug_info: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
        ...

class InterpretError(_message.Message):
    __slots__ = ('message', 'code', 'details')

    class InterpretErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERPRET_ERROR_CODE_UNSPECIFIED: _ClassVar[InterpretError.InterpretErrorCode]
        INVALID_QUERY: _ClassVar[InterpretError.InterpretErrorCode]
        FAILED_TO_UNDERSTAND: _ClassVar[InterpretError.InterpretErrorCode]
        FAILED_TO_ANSWER: _ClassVar[InterpretError.InterpretErrorCode]
    INTERPRET_ERROR_CODE_UNSPECIFIED: InterpretError.InterpretErrorCode
    INVALID_QUERY: InterpretError.InterpretErrorCode
    FAILED_TO_UNDERSTAND: InterpretError.InterpretErrorCode
    FAILED_TO_ANSWER: InterpretError.InterpretErrorCode

    class InterpretErrorDetails(_message.Message):
        __slots__ = ('unsupported_details', 'incomplete_query_details', 'ambiguity_details')
        UNSUPPORTED_DETAILS_FIELD_NUMBER: _ClassVar[int]
        INCOMPLETE_QUERY_DETAILS_FIELD_NUMBER: _ClassVar[int]
        AMBIGUITY_DETAILS_FIELD_NUMBER: _ClassVar[int]
        unsupported_details: InterpretError.InterpretUnsupportedDetails
        incomplete_query_details: InterpretError.InterpretIncompleteQueryDetails
        ambiguity_details: InterpretError.InterpretAmbiguityDetails

        def __init__(self, unsupported_details: _Optional[_Union[InterpretError.InterpretUnsupportedDetails, _Mapping]]=..., incomplete_query_details: _Optional[_Union[InterpretError.InterpretIncompleteQueryDetails, _Mapping]]=..., ambiguity_details: _Optional[_Union[InterpretError.InterpretAmbiguityDetails, _Mapping]]=...) -> None:
            ...

    class InterpretUnsupportedDetails(_message.Message):
        __slots__ = ('operators', 'intent')
        OPERATORS_FIELD_NUMBER: _ClassVar[int]
        INTENT_FIELD_NUMBER: _ClassVar[int]
        operators: _containers.RepeatedScalarFieldContainer[str]
        intent: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, operators: _Optional[_Iterable[str]]=..., intent: _Optional[_Iterable[str]]=...) -> None:
            ...

    class InterpretIncompleteQueryDetails(_message.Message):
        __slots__ = ('entities',)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedScalarFieldContainer[InterpretEntity]

        def __init__(self, entities: _Optional[_Iterable[_Union[InterpretEntity, str]]]=...) -> None:
            ...

    class InterpretAmbiguityDetails(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    message: str
    code: InterpretError.InterpretErrorCode
    details: InterpretError.InterpretErrorDetails

    def __init__(self, message: _Optional[str]=..., code: _Optional[_Union[InterpretError.InterpretErrorCode, str]]=..., details: _Optional[_Union[InterpretError.InterpretErrorDetails, _Mapping]]=...) -> None:
        ...

class ExecutionInfo(_message.Message):
    __slots__ = ('job_creation_status', 'job_execution_state', 'create_time', 'bigquery_job')

    class JobExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_EXECUTION_STATE_UNSPECIFIED: _ClassVar[ExecutionInfo.JobExecutionState]
        NOT_EXECUTED: _ClassVar[ExecutionInfo.JobExecutionState]
        RUNNING: _ClassVar[ExecutionInfo.JobExecutionState]
        SUCCEEDED: _ClassVar[ExecutionInfo.JobExecutionState]
        FAILED: _ClassVar[ExecutionInfo.JobExecutionState]
    JOB_EXECUTION_STATE_UNSPECIFIED: ExecutionInfo.JobExecutionState
    NOT_EXECUTED: ExecutionInfo.JobExecutionState
    RUNNING: ExecutionInfo.JobExecutionState
    SUCCEEDED: ExecutionInfo.JobExecutionState
    FAILED: ExecutionInfo.JobExecutionState
    JOB_CREATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_JOB_FIELD_NUMBER: _ClassVar[int]
    job_creation_status: _status_pb2.Status
    job_execution_state: ExecutionInfo.JobExecutionState
    create_time: _timestamp_pb2.Timestamp
    bigquery_job: BigQueryJob

    def __init__(self, job_creation_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., job_execution_state: _Optional[_Union[ExecutionInfo.JobExecutionState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., bigquery_job: _Optional[_Union[BigQueryJob, _Mapping]]=...) -> None:
        ...

class BigQueryJob(_message.Message):
    __slots__ = ('job_id', 'project_id', 'location')
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    project_id: str
    location: str

    def __init__(self, job_id: _Optional[str]=..., project_id: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class Interpretation(_message.Message):
    __slots__ = ('data_sources', 'confidence', 'unused_phrases', 'human_readable', 'interpretation_structure', 'data_query', 'execution_info')
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    UNUSED_PHRASES_FIELD_NUMBER: _ClassVar[int]
    HUMAN_READABLE_FIELD_NUMBER: _ClassVar[int]
    INTERPRETATION_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    DATA_QUERY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    data_sources: _containers.RepeatedScalarFieldContainer[str]
    confidence: float
    unused_phrases: _containers.RepeatedScalarFieldContainer[str]
    human_readable: HumanReadable
    interpretation_structure: InterpretationStructure
    data_query: DataQuery
    execution_info: ExecutionInfo

    def __init__(self, data_sources: _Optional[_Iterable[str]]=..., confidence: _Optional[float]=..., unused_phrases: _Optional[_Iterable[str]]=..., human_readable: _Optional[_Union[HumanReadable, _Mapping]]=..., interpretation_structure: _Optional[_Union[InterpretationStructure, _Mapping]]=..., data_query: _Optional[_Union[DataQuery, _Mapping]]=..., execution_info: _Optional[_Union[ExecutionInfo, _Mapping]]=...) -> None:
        ...

class DataQuery(_message.Message):
    __slots__ = ('sql',)
    SQL_FIELD_NUMBER: _ClassVar[int]
    sql: str

    def __init__(self, sql: _Optional[str]=...) -> None:
        ...

class HumanReadable(_message.Message):
    __slots__ = ('generated_interpretation', 'original_question')
    GENERATED_INTERPRETATION_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_QUESTION_FIELD_NUMBER: _ClassVar[int]
    generated_interpretation: _annotated_string_pb2.AnnotatedString
    original_question: _annotated_string_pb2.AnnotatedString

    def __init__(self, generated_interpretation: _Optional[_Union[_annotated_string_pb2.AnnotatedString, _Mapping]]=..., original_question: _Optional[_Union[_annotated_string_pb2.AnnotatedString, _Mapping]]=...) -> None:
        ...

class InterpretationStructure(_message.Message):
    __slots__ = ('visualization_types', 'column_info')

    class VisualizationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VISUALIZATION_TYPE_UNSPECIFIED: _ClassVar[InterpretationStructure.VisualizationType]
        TABLE: _ClassVar[InterpretationStructure.VisualizationType]
        BAR_CHART: _ClassVar[InterpretationStructure.VisualizationType]
        COLUMN_CHART: _ClassVar[InterpretationStructure.VisualizationType]
        TIMELINE: _ClassVar[InterpretationStructure.VisualizationType]
        SCATTER_PLOT: _ClassVar[InterpretationStructure.VisualizationType]
        PIE_CHART: _ClassVar[InterpretationStructure.VisualizationType]
        LINE_CHART: _ClassVar[InterpretationStructure.VisualizationType]
        AREA_CHART: _ClassVar[InterpretationStructure.VisualizationType]
        COMBO_CHART: _ClassVar[InterpretationStructure.VisualizationType]
        HISTOGRAM: _ClassVar[InterpretationStructure.VisualizationType]
        GENERIC_CHART: _ClassVar[InterpretationStructure.VisualizationType]
        CHART_NOT_UNDERSTOOD: _ClassVar[InterpretationStructure.VisualizationType]
    VISUALIZATION_TYPE_UNSPECIFIED: InterpretationStructure.VisualizationType
    TABLE: InterpretationStructure.VisualizationType
    BAR_CHART: InterpretationStructure.VisualizationType
    COLUMN_CHART: InterpretationStructure.VisualizationType
    TIMELINE: InterpretationStructure.VisualizationType
    SCATTER_PLOT: InterpretationStructure.VisualizationType
    PIE_CHART: InterpretationStructure.VisualizationType
    LINE_CHART: InterpretationStructure.VisualizationType
    AREA_CHART: InterpretationStructure.VisualizationType
    COMBO_CHART: InterpretationStructure.VisualizationType
    HISTOGRAM: InterpretationStructure.VisualizationType
    GENERIC_CHART: InterpretationStructure.VisualizationType
    CHART_NOT_UNDERSTOOD: InterpretationStructure.VisualizationType

    class ColumnInfo(_message.Message):
        __slots__ = ('output_alias', 'display_name')
        OUTPUT_ALIAS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        output_alias: str
        display_name: str

        def __init__(self, output_alias: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
            ...
    VISUALIZATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    visualization_types: _containers.RepeatedScalarFieldContainer[InterpretationStructure.VisualizationType]
    column_info: _containers.RepeatedCompositeFieldContainer[InterpretationStructure.ColumnInfo]

    def __init__(self, visualization_types: _Optional[_Iterable[_Union[InterpretationStructure.VisualizationType, str]]]=..., column_info: _Optional[_Iterable[_Union[InterpretationStructure.ColumnInfo, _Mapping]]]=...) -> None:
        ...

class DebugFlags(_message.Message):
    __slots__ = ('include_va_query', 'include_nested_va_query', 'include_human_interpretation', 'include_aqua_debug_response', 'time_override', 'is_internal_google_user', 'ignore_cache', 'include_search_entities_rpc', 'include_list_column_annotations_rpc', 'include_virtual_analyst_entities', 'include_table_list', 'include_domain_list')
    INCLUDE_VA_QUERY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NESTED_VA_QUERY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HUMAN_INTERPRETATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_AQUA_DEBUG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TIME_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_GOOGLE_USER_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CACHE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SEARCH_ENTITIES_RPC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LIST_COLUMN_ANNOTATIONS_RPC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VIRTUAL_ANALYST_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DOMAIN_LIST_FIELD_NUMBER: _ClassVar[int]
    include_va_query: bool
    include_nested_va_query: bool
    include_human_interpretation: bool
    include_aqua_debug_response: bool
    time_override: int
    is_internal_google_user: bool
    ignore_cache: bool
    include_search_entities_rpc: bool
    include_list_column_annotations_rpc: bool
    include_virtual_analyst_entities: bool
    include_table_list: bool
    include_domain_list: bool

    def __init__(self, include_va_query: bool=..., include_nested_va_query: bool=..., include_human_interpretation: bool=..., include_aqua_debug_response: bool=..., time_override: _Optional[int]=..., is_internal_google_user: bool=..., ignore_cache: bool=..., include_search_entities_rpc: bool=..., include_list_column_annotations_rpc: bool=..., include_virtual_analyst_entities: bool=..., include_table_list: bool=..., include_domain_list: bool=...) -> None:
        ...