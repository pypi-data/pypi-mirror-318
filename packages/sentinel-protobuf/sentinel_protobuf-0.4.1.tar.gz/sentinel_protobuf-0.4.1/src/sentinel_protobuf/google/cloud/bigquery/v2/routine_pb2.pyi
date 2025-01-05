from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import routine_reference_pb2 as _routine_reference_pb2
from google.cloud.bigquery.v2 import standard_sql_pb2 as _standard_sql_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Routine(_message.Message):
    __slots__ = ('etag', 'routine_reference', 'routine_type', 'creation_time', 'last_modified_time', 'language', 'arguments', 'return_type', 'return_table_type', 'imported_libraries', 'definition_body', 'description', 'determinism_level', 'security_mode', 'strict_mode', 'remote_function_options', 'spark_options', 'data_governance_type')

    class RoutineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTINE_TYPE_UNSPECIFIED: _ClassVar[Routine.RoutineType]
        SCALAR_FUNCTION: _ClassVar[Routine.RoutineType]
        PROCEDURE: _ClassVar[Routine.RoutineType]
        TABLE_VALUED_FUNCTION: _ClassVar[Routine.RoutineType]
        AGGREGATE_FUNCTION: _ClassVar[Routine.RoutineType]
    ROUTINE_TYPE_UNSPECIFIED: Routine.RoutineType
    SCALAR_FUNCTION: Routine.RoutineType
    PROCEDURE: Routine.RoutineType
    TABLE_VALUED_FUNCTION: Routine.RoutineType
    AGGREGATE_FUNCTION: Routine.RoutineType

    class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LANGUAGE_UNSPECIFIED: _ClassVar[Routine.Language]
        SQL: _ClassVar[Routine.Language]
        JAVASCRIPT: _ClassVar[Routine.Language]
        PYTHON: _ClassVar[Routine.Language]
        JAVA: _ClassVar[Routine.Language]
        SCALA: _ClassVar[Routine.Language]
    LANGUAGE_UNSPECIFIED: Routine.Language
    SQL: Routine.Language
    JAVASCRIPT: Routine.Language
    PYTHON: Routine.Language
    JAVA: Routine.Language
    SCALA: Routine.Language

    class DeterminismLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETERMINISM_LEVEL_UNSPECIFIED: _ClassVar[Routine.DeterminismLevel]
        DETERMINISTIC: _ClassVar[Routine.DeterminismLevel]
        NOT_DETERMINISTIC: _ClassVar[Routine.DeterminismLevel]
    DETERMINISM_LEVEL_UNSPECIFIED: Routine.DeterminismLevel
    DETERMINISTIC: Routine.DeterminismLevel
    NOT_DETERMINISTIC: Routine.DeterminismLevel

    class SecurityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SECURITY_MODE_UNSPECIFIED: _ClassVar[Routine.SecurityMode]
        DEFINER: _ClassVar[Routine.SecurityMode]
        INVOKER: _ClassVar[Routine.SecurityMode]
    SECURITY_MODE_UNSPECIFIED: Routine.SecurityMode
    DEFINER: Routine.SecurityMode
    INVOKER: Routine.SecurityMode

    class DataGovernanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_GOVERNANCE_TYPE_UNSPECIFIED: _ClassVar[Routine.DataGovernanceType]
        DATA_MASKING: _ClassVar[Routine.DataGovernanceType]
    DATA_GOVERNANCE_TYPE_UNSPECIFIED: Routine.DataGovernanceType
    DATA_MASKING: Routine.DataGovernanceType

    class Argument(_message.Message):
        __slots__ = ('name', 'argument_kind', 'mode', 'data_type', 'is_aggregate')

        class ArgumentKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ARGUMENT_KIND_UNSPECIFIED: _ClassVar[Routine.Argument.ArgumentKind]
            FIXED_TYPE: _ClassVar[Routine.Argument.ArgumentKind]
            ANY_TYPE: _ClassVar[Routine.Argument.ArgumentKind]
        ARGUMENT_KIND_UNSPECIFIED: Routine.Argument.ArgumentKind
        FIXED_TYPE: Routine.Argument.ArgumentKind
        ANY_TYPE: Routine.Argument.ArgumentKind

        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[Routine.Argument.Mode]
            IN: _ClassVar[Routine.Argument.Mode]
            OUT: _ClassVar[Routine.Argument.Mode]
            INOUT: _ClassVar[Routine.Argument.Mode]
        MODE_UNSPECIFIED: Routine.Argument.Mode
        IN: Routine.Argument.Mode
        OUT: Routine.Argument.Mode
        INOUT: Routine.Argument.Mode
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
        name: str
        argument_kind: Routine.Argument.ArgumentKind
        mode: Routine.Argument.Mode
        data_type: _standard_sql_pb2.StandardSqlDataType
        is_aggregate: _wrappers_pb2.BoolValue

        def __init__(self, name: _Optional[str]=..., argument_kind: _Optional[_Union[Routine.Argument.ArgumentKind, str]]=..., mode: _Optional[_Union[Routine.Argument.Mode, str]]=..., data_type: _Optional[_Union[_standard_sql_pb2.StandardSqlDataType, _Mapping]]=..., is_aggregate: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=...) -> None:
            ...

    class RemoteFunctionOptions(_message.Message):
        __slots__ = ('endpoint', 'connection', 'user_defined_context', 'max_batching_rows')

        class UserDefinedContextEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FIELD_NUMBER: _ClassVar[int]
        USER_DEFINED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        MAX_BATCHING_ROWS_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        connection: str
        user_defined_context: _containers.ScalarMap[str, str]
        max_batching_rows: int

        def __init__(self, endpoint: _Optional[str]=..., connection: _Optional[str]=..., user_defined_context: _Optional[_Mapping[str, str]]=..., max_batching_rows: _Optional[int]=...) -> None:
            ...
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETURN_TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_BODY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DETERMINISM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MODE_FIELD_NUMBER: _ClassVar[int]
    STRICT_MODE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FUNCTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SPARK_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_GOVERNANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    etag: str
    routine_reference: _routine_reference_pb2.RoutineReference
    routine_type: Routine.RoutineType
    creation_time: int
    last_modified_time: int
    language: Routine.Language
    arguments: _containers.RepeatedCompositeFieldContainer[Routine.Argument]
    return_type: _standard_sql_pb2.StandardSqlDataType
    return_table_type: _standard_sql_pb2.StandardSqlTableType
    imported_libraries: _containers.RepeatedScalarFieldContainer[str]
    definition_body: str
    description: str
    determinism_level: Routine.DeterminismLevel
    security_mode: Routine.SecurityMode
    strict_mode: _wrappers_pb2.BoolValue
    remote_function_options: Routine.RemoteFunctionOptions
    spark_options: SparkOptions
    data_governance_type: Routine.DataGovernanceType

    def __init__(self, etag: _Optional[str]=..., routine_reference: _Optional[_Union[_routine_reference_pb2.RoutineReference, _Mapping]]=..., routine_type: _Optional[_Union[Routine.RoutineType, str]]=..., creation_time: _Optional[int]=..., last_modified_time: _Optional[int]=..., language: _Optional[_Union[Routine.Language, str]]=..., arguments: _Optional[_Iterable[_Union[Routine.Argument, _Mapping]]]=..., return_type: _Optional[_Union[_standard_sql_pb2.StandardSqlDataType, _Mapping]]=..., return_table_type: _Optional[_Union[_standard_sql_pb2.StandardSqlTableType, _Mapping]]=..., imported_libraries: _Optional[_Iterable[str]]=..., definition_body: _Optional[str]=..., description: _Optional[str]=..., determinism_level: _Optional[_Union[Routine.DeterminismLevel, str]]=..., security_mode: _Optional[_Union[Routine.SecurityMode, str]]=..., strict_mode: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., remote_function_options: _Optional[_Union[Routine.RemoteFunctionOptions, _Mapping]]=..., spark_options: _Optional[_Union[SparkOptions, _Mapping]]=..., data_governance_type: _Optional[_Union[Routine.DataGovernanceType, str]]=...) -> None:
        ...

class SparkOptions(_message.Message):
    __slots__ = ('connection', 'runtime_version', 'container_image', 'properties', 'main_file_uri', 'py_file_uris', 'jar_uris', 'file_uris', 'archive_uris', 'main_class')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MAIN_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    PY_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    JAR_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    connection: str
    runtime_version: str
    container_image: str
    properties: _containers.ScalarMap[str, str]
    main_file_uri: str
    py_file_uris: _containers.RepeatedScalarFieldContainer[str]
    jar_uris: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]
    main_class: str

    def __init__(self, connection: _Optional[str]=..., runtime_version: _Optional[str]=..., container_image: _Optional[str]=..., properties: _Optional[_Mapping[str, str]]=..., main_file_uri: _Optional[str]=..., py_file_uris: _Optional[_Iterable[str]]=..., jar_uris: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=..., main_class: _Optional[str]=...) -> None:
        ...

class GetRoutineRequest(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'routine_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    routine_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., routine_id: _Optional[str]=...) -> None:
        ...

class InsertRoutineRequest(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'routine')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    routine: Routine

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., routine: _Optional[_Union[Routine, _Mapping]]=...) -> None:
        ...

class UpdateRoutineRequest(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'routine_id', 'routine')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    routine_id: str
    routine: Routine

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., routine_id: _Optional[str]=..., routine: _Optional[_Union[Routine, _Mapping]]=...) -> None:
        ...

class PatchRoutineRequest(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'routine_id', 'routine', 'field_mask')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    routine_id: str
    routine: Routine
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., routine_id: _Optional[str]=..., routine: _Optional[_Union[Routine, _Mapping]]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRoutineRequest(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'routine_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    routine_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., routine_id: _Optional[str]=...) -> None:
        ...

class ListRoutinesRequest(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'max_results', 'page_token', 'filter')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    max_results: _wrappers_pb2.UInt32Value
    page_token: str
    filter: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., max_results: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRoutinesResponse(_message.Message):
    __slots__ = ('routines', 'next_page_token')
    ROUTINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    routines: _containers.RepeatedCompositeFieldContainer[Routine]
    next_page_token: str

    def __init__(self, routines: _Optional[_Iterable[_Union[Routine, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...