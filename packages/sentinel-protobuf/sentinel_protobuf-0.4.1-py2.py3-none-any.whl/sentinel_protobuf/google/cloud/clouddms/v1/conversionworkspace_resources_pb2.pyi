from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.clouddms.v1 import clouddms_resources_pb2 as _clouddms_resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValuePresentInList(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_PRESENT_IN_LIST_UNSPECIFIED: _ClassVar[ValuePresentInList]
    VALUE_PRESENT_IN_LIST_IF_VALUE_LIST: _ClassVar[ValuePresentInList]
    VALUE_PRESENT_IN_LIST_IF_VALUE_NOT_LIST: _ClassVar[ValuePresentInList]

class DatabaseEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_ENTITY_TYPE_UNSPECIFIED: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_SCHEMA: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_TABLE: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_COLUMN: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_CONSTRAINT: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_INDEX: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_TRIGGER: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_VIEW: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_SEQUENCE: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_STORED_PROCEDURE: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_FUNCTION: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_SYNONYM: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_DATABASE_PACKAGE: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_UDT: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW: _ClassVar[DatabaseEntityType]
    DATABASE_ENTITY_TYPE_DATABASE: _ClassVar[DatabaseEntityType]

class EntityNameTransformation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTITY_NAME_TRANSFORMATION_UNSPECIFIED: _ClassVar[EntityNameTransformation]
    ENTITY_NAME_TRANSFORMATION_NO_TRANSFORMATION: _ClassVar[EntityNameTransformation]
    ENTITY_NAME_TRANSFORMATION_LOWER_CASE: _ClassVar[EntityNameTransformation]
    ENTITY_NAME_TRANSFORMATION_UPPER_CASE: _ClassVar[EntityNameTransformation]
    ENTITY_NAME_TRANSFORMATION_CAPITALIZED_CASE: _ClassVar[EntityNameTransformation]

class BackgroundJobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_JOB_TYPE_UNSPECIFIED: _ClassVar[BackgroundJobType]
    BACKGROUND_JOB_TYPE_SOURCE_SEED: _ClassVar[BackgroundJobType]
    BACKGROUND_JOB_TYPE_CONVERT: _ClassVar[BackgroundJobType]
    BACKGROUND_JOB_TYPE_APPLY_DESTINATION: _ClassVar[BackgroundJobType]
    BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE: _ClassVar[BackgroundJobType]

class ImportRulesFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORT_RULES_FILE_FORMAT_UNSPECIFIED: _ClassVar[ImportRulesFileFormat]
    IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE: _ClassVar[ImportRulesFileFormat]
    IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE: _ClassVar[ImportRulesFileFormat]

class ValueComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_COMPARISON_UNSPECIFIED: _ClassVar[ValueComparison]
    VALUE_COMPARISON_IF_VALUE_SMALLER_THAN: _ClassVar[ValueComparison]
    VALUE_COMPARISON_IF_VALUE_SMALLER_EQUAL_THAN: _ClassVar[ValueComparison]
    VALUE_COMPARISON_IF_VALUE_LARGER_THAN: _ClassVar[ValueComparison]
    VALUE_COMPARISON_IF_VALUE_LARGER_EQUAL_THAN: _ClassVar[ValueComparison]

class NumericFilterOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NUMERIC_FILTER_OPTION_UNSPECIFIED: _ClassVar[NumericFilterOption]
    NUMERIC_FILTER_OPTION_ALL: _ClassVar[NumericFilterOption]
    NUMERIC_FILTER_OPTION_LIMIT: _ClassVar[NumericFilterOption]
    NUMERIC_FILTER_OPTION_LIMITLESS: _ClassVar[NumericFilterOption]
VALUE_PRESENT_IN_LIST_UNSPECIFIED: ValuePresentInList
VALUE_PRESENT_IN_LIST_IF_VALUE_LIST: ValuePresentInList
VALUE_PRESENT_IN_LIST_IF_VALUE_NOT_LIST: ValuePresentInList
DATABASE_ENTITY_TYPE_UNSPECIFIED: DatabaseEntityType
DATABASE_ENTITY_TYPE_SCHEMA: DatabaseEntityType
DATABASE_ENTITY_TYPE_TABLE: DatabaseEntityType
DATABASE_ENTITY_TYPE_COLUMN: DatabaseEntityType
DATABASE_ENTITY_TYPE_CONSTRAINT: DatabaseEntityType
DATABASE_ENTITY_TYPE_INDEX: DatabaseEntityType
DATABASE_ENTITY_TYPE_TRIGGER: DatabaseEntityType
DATABASE_ENTITY_TYPE_VIEW: DatabaseEntityType
DATABASE_ENTITY_TYPE_SEQUENCE: DatabaseEntityType
DATABASE_ENTITY_TYPE_STORED_PROCEDURE: DatabaseEntityType
DATABASE_ENTITY_TYPE_FUNCTION: DatabaseEntityType
DATABASE_ENTITY_TYPE_SYNONYM: DatabaseEntityType
DATABASE_ENTITY_TYPE_DATABASE_PACKAGE: DatabaseEntityType
DATABASE_ENTITY_TYPE_UDT: DatabaseEntityType
DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW: DatabaseEntityType
DATABASE_ENTITY_TYPE_DATABASE: DatabaseEntityType
ENTITY_NAME_TRANSFORMATION_UNSPECIFIED: EntityNameTransformation
ENTITY_NAME_TRANSFORMATION_NO_TRANSFORMATION: EntityNameTransformation
ENTITY_NAME_TRANSFORMATION_LOWER_CASE: EntityNameTransformation
ENTITY_NAME_TRANSFORMATION_UPPER_CASE: EntityNameTransformation
ENTITY_NAME_TRANSFORMATION_CAPITALIZED_CASE: EntityNameTransformation
BACKGROUND_JOB_TYPE_UNSPECIFIED: BackgroundJobType
BACKGROUND_JOB_TYPE_SOURCE_SEED: BackgroundJobType
BACKGROUND_JOB_TYPE_CONVERT: BackgroundJobType
BACKGROUND_JOB_TYPE_APPLY_DESTINATION: BackgroundJobType
BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE: BackgroundJobType
IMPORT_RULES_FILE_FORMAT_UNSPECIFIED: ImportRulesFileFormat
IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE: ImportRulesFileFormat
IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE: ImportRulesFileFormat
VALUE_COMPARISON_UNSPECIFIED: ValueComparison
VALUE_COMPARISON_IF_VALUE_SMALLER_THAN: ValueComparison
VALUE_COMPARISON_IF_VALUE_SMALLER_EQUAL_THAN: ValueComparison
VALUE_COMPARISON_IF_VALUE_LARGER_THAN: ValueComparison
VALUE_COMPARISON_IF_VALUE_LARGER_EQUAL_THAN: ValueComparison
NUMERIC_FILTER_OPTION_UNSPECIFIED: NumericFilterOption
NUMERIC_FILTER_OPTION_ALL: NumericFilterOption
NUMERIC_FILTER_OPTION_LIMIT: NumericFilterOption
NUMERIC_FILTER_OPTION_LIMITLESS: NumericFilterOption

class DatabaseEngineInfo(_message.Message):
    __slots__ = ("engine", "version")
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    engine: _clouddms_resources_pb2.DatabaseEngine
    version: str
    def __init__(self, engine: _Optional[_Union[_clouddms_resources_pb2.DatabaseEngine, str]] = ..., version: _Optional[str] = ...) -> None: ...

class ConversionWorkspace(_message.Message):
    __slots__ = ("name", "source", "destination", "global_settings", "has_uncommitted_changes", "latest_commit_id", "latest_commit_time", "create_time", "update_time", "display_name")
    class GlobalSettingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    HAS_UNCOMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    LATEST_COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_COMMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    source: DatabaseEngineInfo
    destination: DatabaseEngineInfo
    global_settings: _containers.ScalarMap[str, str]
    has_uncommitted_changes: bool
    latest_commit_id: str
    latest_commit_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    def __init__(self, name: _Optional[str] = ..., source: _Optional[_Union[DatabaseEngineInfo, _Mapping]] = ..., destination: _Optional[_Union[DatabaseEngineInfo, _Mapping]] = ..., global_settings: _Optional[_Mapping[str, str]] = ..., has_uncommitted_changes: bool = ..., latest_commit_id: _Optional[str] = ..., latest_commit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_name: _Optional[str] = ...) -> None: ...

class BackgroundJobLogEntry(_message.Message):
    __slots__ = ("id", "job_type", "start_time", "finish_time", "completion_state", "completion_comment", "request_autocommit", "seed_job_details", "import_rules_job_details", "convert_job_details", "apply_job_details")
    class JobCompletionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_COMPLETION_STATE_UNSPECIFIED: _ClassVar[BackgroundJobLogEntry.JobCompletionState]
        SUCCEEDED: _ClassVar[BackgroundJobLogEntry.JobCompletionState]
        FAILED: _ClassVar[BackgroundJobLogEntry.JobCompletionState]
    JOB_COMPLETION_STATE_UNSPECIFIED: BackgroundJobLogEntry.JobCompletionState
    SUCCEEDED: BackgroundJobLogEntry.JobCompletionState
    FAILED: BackgroundJobLogEntry.JobCompletionState
    class SeedJobDetails(_message.Message):
        __slots__ = ("connection_profile",)
        CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
        connection_profile: str
        def __init__(self, connection_profile: _Optional[str] = ...) -> None: ...
    class ImportRulesJobDetails(_message.Message):
        __slots__ = ("files", "file_format")
        FILES_FIELD_NUMBER: _ClassVar[int]
        FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
        files: _containers.RepeatedScalarFieldContainer[str]
        file_format: ImportRulesFileFormat
        def __init__(self, files: _Optional[_Iterable[str]] = ..., file_format: _Optional[_Union[ImportRulesFileFormat, str]] = ...) -> None: ...
    class ConvertJobDetails(_message.Message):
        __slots__ = ("filter",)
        FILTER_FIELD_NUMBER: _ClassVar[int]
        filter: str
        def __init__(self, filter: _Optional[str] = ...) -> None: ...
    class ApplyJobDetails(_message.Message):
        __slots__ = ("connection_profile", "filter")
        CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        connection_profile: str
        filter: str
        def __init__(self, connection_profile: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_STATE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_COMMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_AUTOCOMMIT_FIELD_NUMBER: _ClassVar[int]
    SEED_JOB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_RULES_JOB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONVERT_JOB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    APPLY_JOB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    job_type: BackgroundJobType
    start_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    completion_state: BackgroundJobLogEntry.JobCompletionState
    completion_comment: str
    request_autocommit: bool
    seed_job_details: BackgroundJobLogEntry.SeedJobDetails
    import_rules_job_details: BackgroundJobLogEntry.ImportRulesJobDetails
    convert_job_details: BackgroundJobLogEntry.ConvertJobDetails
    apply_job_details: BackgroundJobLogEntry.ApplyJobDetails
    def __init__(self, id: _Optional[str] = ..., job_type: _Optional[_Union[BackgroundJobType, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_state: _Optional[_Union[BackgroundJobLogEntry.JobCompletionState, str]] = ..., completion_comment: _Optional[str] = ..., request_autocommit: bool = ..., seed_job_details: _Optional[_Union[BackgroundJobLogEntry.SeedJobDetails, _Mapping]] = ..., import_rules_job_details: _Optional[_Union[BackgroundJobLogEntry.ImportRulesJobDetails, _Mapping]] = ..., convert_job_details: _Optional[_Union[BackgroundJobLogEntry.ConvertJobDetails, _Mapping]] = ..., apply_job_details: _Optional[_Union[BackgroundJobLogEntry.ApplyJobDetails, _Mapping]] = ...) -> None: ...

class MappingRuleFilter(_message.Message):
    __slots__ = ("parent_entity", "entity_name_prefix", "entity_name_suffix", "entity_name_contains", "entities")
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    parent_entity: str
    entity_name_prefix: str
    entity_name_suffix: str
    entity_name_contains: str
    entities: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent_entity: _Optional[str] = ..., entity_name_prefix: _Optional[str] = ..., entity_name_suffix: _Optional[str] = ..., entity_name_contains: _Optional[str] = ..., entities: _Optional[_Iterable[str]] = ...) -> None: ...

class MappingRule(_message.Message):
    __slots__ = ("name", "display_name", "state", "rule_scope", "filter", "rule_order", "revision_id", "revision_create_time", "single_entity_rename", "multi_entity_rename", "entity_move", "single_column_change", "multi_column_data_type_change", "conditional_column_set_value", "convert_rowid_column", "set_table_primary_key", "single_package_change", "source_sql_change", "filter_table_columns")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MappingRule.State]
        ENABLED: _ClassVar[MappingRule.State]
        DISABLED: _ClassVar[MappingRule.State]
        DELETED: _ClassVar[MappingRule.State]
    STATE_UNSPECIFIED: MappingRule.State
    ENABLED: MappingRule.State
    DISABLED: MappingRule.State
    DELETED: MappingRule.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RULE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    RULE_ORDER_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SINGLE_ENTITY_RENAME_FIELD_NUMBER: _ClassVar[int]
    MULTI_ENTITY_RENAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MOVE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_COLUMN_CHANGE_FIELD_NUMBER: _ClassVar[int]
    MULTI_COLUMN_DATA_TYPE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_COLUMN_SET_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONVERT_ROWID_COLUMN_FIELD_NUMBER: _ClassVar[int]
    SET_TABLE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    SINGLE_PACKAGE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SQL_CHANGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: MappingRule.State
    rule_scope: DatabaseEntityType
    filter: MappingRuleFilter
    rule_order: int
    revision_id: str
    revision_create_time: _timestamp_pb2.Timestamp
    single_entity_rename: SingleEntityRename
    multi_entity_rename: MultiEntityRename
    entity_move: EntityMove
    single_column_change: SingleColumnChange
    multi_column_data_type_change: MultiColumnDatatypeChange
    conditional_column_set_value: ConditionalColumnSetValue
    convert_rowid_column: ConvertRowIdToColumn
    set_table_primary_key: SetTablePrimaryKey
    single_package_change: SinglePackageChange
    source_sql_change: SourceSqlChange
    filter_table_columns: FilterTableColumns
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., state: _Optional[_Union[MappingRule.State, str]] = ..., rule_scope: _Optional[_Union[DatabaseEntityType, str]] = ..., filter: _Optional[_Union[MappingRuleFilter, _Mapping]] = ..., rule_order: _Optional[int] = ..., revision_id: _Optional[str] = ..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., single_entity_rename: _Optional[_Union[SingleEntityRename, _Mapping]] = ..., multi_entity_rename: _Optional[_Union[MultiEntityRename, _Mapping]] = ..., entity_move: _Optional[_Union[EntityMove, _Mapping]] = ..., single_column_change: _Optional[_Union[SingleColumnChange, _Mapping]] = ..., multi_column_data_type_change: _Optional[_Union[MultiColumnDatatypeChange, _Mapping]] = ..., conditional_column_set_value: _Optional[_Union[ConditionalColumnSetValue, _Mapping]] = ..., convert_rowid_column: _Optional[_Union[ConvertRowIdToColumn, _Mapping]] = ..., set_table_primary_key: _Optional[_Union[SetTablePrimaryKey, _Mapping]] = ..., single_package_change: _Optional[_Union[SinglePackageChange, _Mapping]] = ..., source_sql_change: _Optional[_Union[SourceSqlChange, _Mapping]] = ..., filter_table_columns: _Optional[_Union[FilterTableColumns, _Mapping]] = ...) -> None: ...

class SingleEntityRename(_message.Message):
    __slots__ = ("new_name",)
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    new_name: str
    def __init__(self, new_name: _Optional[str] = ...) -> None: ...

class MultiEntityRename(_message.Message):
    __slots__ = ("new_name_pattern", "source_name_transformation")
    NEW_NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NAME_TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
    new_name_pattern: str
    source_name_transformation: EntityNameTransformation
    def __init__(self, new_name_pattern: _Optional[str] = ..., source_name_transformation: _Optional[_Union[EntityNameTransformation, str]] = ...) -> None: ...

class EntityMove(_message.Message):
    __slots__ = ("new_schema",)
    NEW_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    new_schema: str
    def __init__(self, new_schema: _Optional[str] = ...) -> None: ...

class SingleColumnChange(_message.Message):
    __slots__ = ("data_type", "charset", "collation", "length", "precision", "scale", "fractional_seconds_precision", "array", "array_length", "nullable", "auto_generated", "udt", "custom_features", "set_values", "comment")
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHARSET_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    FRACTIONAL_SECONDS_PRECISION_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    ARRAY_LENGTH_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    AUTO_GENERATED_FIELD_NUMBER: _ClassVar[int]
    UDT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SET_VALUES_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    data_type: str
    charset: str
    collation: str
    length: int
    precision: int
    scale: int
    fractional_seconds_precision: int
    array: bool
    array_length: int
    nullable: bool
    auto_generated: bool
    udt: bool
    custom_features: _struct_pb2.Struct
    set_values: _containers.RepeatedScalarFieldContainer[str]
    comment: str
    def __init__(self, data_type: _Optional[str] = ..., charset: _Optional[str] = ..., collation: _Optional[str] = ..., length: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ..., fractional_seconds_precision: _Optional[int] = ..., array: bool = ..., array_length: _Optional[int] = ..., nullable: bool = ..., auto_generated: bool = ..., udt: bool = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., set_values: _Optional[_Iterable[str]] = ..., comment: _Optional[str] = ...) -> None: ...

class MultiColumnDatatypeChange(_message.Message):
    __slots__ = ("source_data_type_filter", "source_text_filter", "source_numeric_filter", "new_data_type", "override_length", "override_scale", "override_precision", "override_fractional_seconds_precision", "custom_features")
    SOURCE_DATA_TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TEXT_FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    NEW_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_SCALE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_PRECISION_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FRACTIONAL_SECONDS_PRECISION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    source_data_type_filter: str
    source_text_filter: SourceTextFilter
    source_numeric_filter: SourceNumericFilter
    new_data_type: str
    override_length: int
    override_scale: int
    override_precision: int
    override_fractional_seconds_precision: int
    custom_features: _struct_pb2.Struct
    def __init__(self, source_data_type_filter: _Optional[str] = ..., source_text_filter: _Optional[_Union[SourceTextFilter, _Mapping]] = ..., source_numeric_filter: _Optional[_Union[SourceNumericFilter, _Mapping]] = ..., new_data_type: _Optional[str] = ..., override_length: _Optional[int] = ..., override_scale: _Optional[int] = ..., override_precision: _Optional[int] = ..., override_fractional_seconds_precision: _Optional[int] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SourceTextFilter(_message.Message):
    __slots__ = ("source_min_length_filter", "source_max_length_filter")
    SOURCE_MIN_LENGTH_FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MAX_LENGTH_FILTER_FIELD_NUMBER: _ClassVar[int]
    source_min_length_filter: int
    source_max_length_filter: int
    def __init__(self, source_min_length_filter: _Optional[int] = ..., source_max_length_filter: _Optional[int] = ...) -> None: ...

class SourceNumericFilter(_message.Message):
    __slots__ = ("source_min_scale_filter", "source_max_scale_filter", "source_min_precision_filter", "source_max_precision_filter", "numeric_filter_option")
    SOURCE_MIN_SCALE_FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MAX_SCALE_FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MIN_PRECISION_FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MAX_PRECISION_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_OPTION_FIELD_NUMBER: _ClassVar[int]
    source_min_scale_filter: int
    source_max_scale_filter: int
    source_min_precision_filter: int
    source_max_precision_filter: int
    numeric_filter_option: NumericFilterOption
    def __init__(self, source_min_scale_filter: _Optional[int] = ..., source_max_scale_filter: _Optional[int] = ..., source_min_precision_filter: _Optional[int] = ..., source_max_precision_filter: _Optional[int] = ..., numeric_filter_option: _Optional[_Union[NumericFilterOption, str]] = ...) -> None: ...

class ConditionalColumnSetValue(_message.Message):
    __slots__ = ("source_text_filter", "source_numeric_filter", "value_transformation", "custom_features")
    SOURCE_TEXT_FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    VALUE_TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    source_text_filter: SourceTextFilter
    source_numeric_filter: SourceNumericFilter
    value_transformation: ValueTransformation
    custom_features: _struct_pb2.Struct
    def __init__(self, source_text_filter: _Optional[_Union[SourceTextFilter, _Mapping]] = ..., source_numeric_filter: _Optional[_Union[SourceNumericFilter, _Mapping]] = ..., value_transformation: _Optional[_Union[ValueTransformation, _Mapping]] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ValueTransformation(_message.Message):
    __slots__ = ("is_null", "value_list", "int_comparison", "double_comparison", "assign_null", "assign_specific_value", "assign_min_value", "assign_max_value", "round_scale", "apply_hash")
    IS_NULL_FIELD_NUMBER: _ClassVar[int]
    VALUE_LIST_FIELD_NUMBER: _ClassVar[int]
    INT_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_NULL_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_SPECIFIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    ROUND_SCALE_FIELD_NUMBER: _ClassVar[int]
    APPLY_HASH_FIELD_NUMBER: _ClassVar[int]
    is_null: _empty_pb2.Empty
    value_list: ValueListFilter
    int_comparison: IntComparisonFilter
    double_comparison: DoubleComparisonFilter
    assign_null: _empty_pb2.Empty
    assign_specific_value: AssignSpecificValue
    assign_min_value: _empty_pb2.Empty
    assign_max_value: _empty_pb2.Empty
    round_scale: RoundToScale
    apply_hash: ApplyHash
    def __init__(self, is_null: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., value_list: _Optional[_Union[ValueListFilter, _Mapping]] = ..., int_comparison: _Optional[_Union[IntComparisonFilter, _Mapping]] = ..., double_comparison: _Optional[_Union[DoubleComparisonFilter, _Mapping]] = ..., assign_null: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., assign_specific_value: _Optional[_Union[AssignSpecificValue, _Mapping]] = ..., assign_min_value: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., assign_max_value: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., round_scale: _Optional[_Union[RoundToScale, _Mapping]] = ..., apply_hash: _Optional[_Union[ApplyHash, _Mapping]] = ...) -> None: ...

class ConvertRowIdToColumn(_message.Message):
    __slots__ = ("only_if_no_primary_key",)
    ONLY_IF_NO_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    only_if_no_primary_key: bool
    def __init__(self, only_if_no_primary_key: bool = ...) -> None: ...

class SetTablePrimaryKey(_message.Message):
    __slots__ = ("primary_key_columns", "primary_key")
    PRIMARY_KEY_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    primary_key_columns: _containers.RepeatedScalarFieldContainer[str]
    primary_key: str
    def __init__(self, primary_key_columns: _Optional[_Iterable[str]] = ..., primary_key: _Optional[str] = ...) -> None: ...

class SinglePackageChange(_message.Message):
    __slots__ = ("package_description", "package_body")
    PACKAGE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    package_description: str
    package_body: str
    def __init__(self, package_description: _Optional[str] = ..., package_body: _Optional[str] = ...) -> None: ...

class SourceSqlChange(_message.Message):
    __slots__ = ("sql_code",)
    SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    sql_code: str
    def __init__(self, sql_code: _Optional[str] = ...) -> None: ...

class FilterTableColumns(_message.Message):
    __slots__ = ("include_columns", "exclude_columns")
    INCLUDE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    include_columns: _containers.RepeatedScalarFieldContainer[str]
    exclude_columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, include_columns: _Optional[_Iterable[str]] = ..., exclude_columns: _Optional[_Iterable[str]] = ...) -> None: ...

class ValueListFilter(_message.Message):
    __slots__ = ("value_present_list", "values", "ignore_case")
    VALUE_PRESENT_LIST_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CASE_FIELD_NUMBER: _ClassVar[int]
    value_present_list: ValuePresentInList
    values: _containers.RepeatedScalarFieldContainer[str]
    ignore_case: bool
    def __init__(self, value_present_list: _Optional[_Union[ValuePresentInList, str]] = ..., values: _Optional[_Iterable[str]] = ..., ignore_case: bool = ...) -> None: ...

class IntComparisonFilter(_message.Message):
    __slots__ = ("value_comparison", "value")
    VALUE_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value_comparison: ValueComparison
    value: int
    def __init__(self, value_comparison: _Optional[_Union[ValueComparison, str]] = ..., value: _Optional[int] = ...) -> None: ...

class DoubleComparisonFilter(_message.Message):
    __slots__ = ("value_comparison", "value")
    VALUE_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value_comparison: ValueComparison
    value: float
    def __init__(self, value_comparison: _Optional[_Union[ValueComparison, str]] = ..., value: _Optional[float] = ...) -> None: ...

class AssignSpecificValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ApplyHash(_message.Message):
    __slots__ = ("uuid_from_bytes",)
    UUID_FROM_BYTES_FIELD_NUMBER: _ClassVar[int]
    uuid_from_bytes: _empty_pb2.Empty
    def __init__(self, uuid_from_bytes: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class RoundToScale(_message.Message):
    __slots__ = ("scale",)
    SCALE_FIELD_NUMBER: _ClassVar[int]
    scale: int
    def __init__(self, scale: _Optional[int] = ...) -> None: ...

class DatabaseEntity(_message.Message):
    __slots__ = ("short_name", "parent_entity", "tree", "entity_type", "mappings", "entity_ddl", "issues", "database", "schema", "table", "view", "sequence", "stored_procedure", "database_function", "synonym", "database_package", "udt", "materialized_view")
    class TreeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TREE_TYPE_UNSPECIFIED: _ClassVar[DatabaseEntity.TreeType]
        SOURCE: _ClassVar[DatabaseEntity.TreeType]
        DRAFT: _ClassVar[DatabaseEntity.TreeType]
        DESTINATION: _ClassVar[DatabaseEntity.TreeType]
    TREE_TYPE_UNSPECIFIED: DatabaseEntity.TreeType
    SOURCE: DatabaseEntity.TreeType
    DRAFT: DatabaseEntity.TreeType
    DESTINATION: DatabaseEntity.TreeType
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TREE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DDL_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    STORED_PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    SYNONYM_FIELD_NUMBER: _ClassVar[int]
    DATABASE_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UDT_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZED_VIEW_FIELD_NUMBER: _ClassVar[int]
    short_name: str
    parent_entity: str
    tree: DatabaseEntity.TreeType
    entity_type: DatabaseEntityType
    mappings: _containers.RepeatedCompositeFieldContainer[EntityMapping]
    entity_ddl: _containers.RepeatedCompositeFieldContainer[EntityDdl]
    issues: _containers.RepeatedCompositeFieldContainer[EntityIssue]
    database: DatabaseInstanceEntity
    schema: SchemaEntity
    table: TableEntity
    view: ViewEntity
    sequence: SequenceEntity
    stored_procedure: StoredProcedureEntity
    database_function: FunctionEntity
    synonym: SynonymEntity
    database_package: PackageEntity
    udt: UDTEntity
    materialized_view: MaterializedViewEntity
    def __init__(self, short_name: _Optional[str] = ..., parent_entity: _Optional[str] = ..., tree: _Optional[_Union[DatabaseEntity.TreeType, str]] = ..., entity_type: _Optional[_Union[DatabaseEntityType, str]] = ..., mappings: _Optional[_Iterable[_Union[EntityMapping, _Mapping]]] = ..., entity_ddl: _Optional[_Iterable[_Union[EntityDdl, _Mapping]]] = ..., issues: _Optional[_Iterable[_Union[EntityIssue, _Mapping]]] = ..., database: _Optional[_Union[DatabaseInstanceEntity, _Mapping]] = ..., schema: _Optional[_Union[SchemaEntity, _Mapping]] = ..., table: _Optional[_Union[TableEntity, _Mapping]] = ..., view: _Optional[_Union[ViewEntity, _Mapping]] = ..., sequence: _Optional[_Union[SequenceEntity, _Mapping]] = ..., stored_procedure: _Optional[_Union[StoredProcedureEntity, _Mapping]] = ..., database_function: _Optional[_Union[FunctionEntity, _Mapping]] = ..., synonym: _Optional[_Union[SynonymEntity, _Mapping]] = ..., database_package: _Optional[_Union[PackageEntity, _Mapping]] = ..., udt: _Optional[_Union[UDTEntity, _Mapping]] = ..., materialized_view: _Optional[_Union[MaterializedViewEntity, _Mapping]] = ...) -> None: ...

class DatabaseInstanceEntity(_message.Message):
    __slots__ = ("custom_features",)
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    custom_features: _struct_pb2.Struct
    def __init__(self, custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SchemaEntity(_message.Message):
    __slots__ = ("custom_features",)
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    custom_features: _struct_pb2.Struct
    def __init__(self, custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class TableEntity(_message.Message):
    __slots__ = ("columns", "constraints", "indices", "triggers", "custom_features", "comment")
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    INDICES_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[ColumnEntity]
    constraints: _containers.RepeatedCompositeFieldContainer[ConstraintEntity]
    indices: _containers.RepeatedCompositeFieldContainer[IndexEntity]
    triggers: _containers.RepeatedCompositeFieldContainer[TriggerEntity]
    custom_features: _struct_pb2.Struct
    comment: str
    def __init__(self, columns: _Optional[_Iterable[_Union[ColumnEntity, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[ConstraintEntity, _Mapping]]] = ..., indices: _Optional[_Iterable[_Union[IndexEntity, _Mapping]]] = ..., triggers: _Optional[_Iterable[_Union[TriggerEntity, _Mapping]]] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., comment: _Optional[str] = ...) -> None: ...

class ColumnEntity(_message.Message):
    __slots__ = ("name", "data_type", "charset", "collation", "length", "precision", "scale", "fractional_seconds_precision", "array", "array_length", "nullable", "auto_generated", "udt", "custom_features", "set_values", "comment", "ordinal_position", "default_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHARSET_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    FRACTIONAL_SECONDS_PRECISION_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    ARRAY_LENGTH_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    AUTO_GENERATED_FIELD_NUMBER: _ClassVar[int]
    UDT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SET_VALUES_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_type: str
    charset: str
    collation: str
    length: int
    precision: int
    scale: int
    fractional_seconds_precision: int
    array: bool
    array_length: int
    nullable: bool
    auto_generated: bool
    udt: bool
    custom_features: _struct_pb2.Struct
    set_values: _containers.RepeatedScalarFieldContainer[str]
    comment: str
    ordinal_position: int
    default_value: str
    def __init__(self, name: _Optional[str] = ..., data_type: _Optional[str] = ..., charset: _Optional[str] = ..., collation: _Optional[str] = ..., length: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ..., fractional_seconds_precision: _Optional[int] = ..., array: bool = ..., array_length: _Optional[int] = ..., nullable: bool = ..., auto_generated: bool = ..., udt: bool = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., set_values: _Optional[_Iterable[str]] = ..., comment: _Optional[str] = ..., ordinal_position: _Optional[int] = ..., default_value: _Optional[str] = ...) -> None: ...

class ConstraintEntity(_message.Message):
    __slots__ = ("name", "type", "table_columns", "custom_features", "reference_columns", "reference_table", "table_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    table_columns: _containers.RepeatedScalarFieldContainer[str]
    custom_features: _struct_pb2.Struct
    reference_columns: _containers.RepeatedScalarFieldContainer[str]
    reference_table: str
    table_name: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., table_columns: _Optional[_Iterable[str]] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., reference_columns: _Optional[_Iterable[str]] = ..., reference_table: _Optional[str] = ..., table_name: _Optional[str] = ...) -> None: ...

class IndexEntity(_message.Message):
    __slots__ = ("name", "type", "table_columns", "unique", "custom_features")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    table_columns: _containers.RepeatedScalarFieldContainer[str]
    unique: bool
    custom_features: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., table_columns: _Optional[_Iterable[str]] = ..., unique: bool = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class TriggerEntity(_message.Message):
    __slots__ = ("name", "triggering_events", "trigger_type", "sql_code", "custom_features")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGERING_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    name: str
    triggering_events: _containers.RepeatedScalarFieldContainer[str]
    trigger_type: str
    sql_code: str
    custom_features: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., triggering_events: _Optional[_Iterable[str]] = ..., trigger_type: _Optional[str] = ..., sql_code: _Optional[str] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ViewEntity(_message.Message):
    __slots__ = ("sql_code", "custom_features", "constraints")
    SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    sql_code: str
    custom_features: _struct_pb2.Struct
    constraints: _containers.RepeatedCompositeFieldContainer[ConstraintEntity]
    def __init__(self, sql_code: _Optional[str] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., constraints: _Optional[_Iterable[_Union[ConstraintEntity, _Mapping]]] = ...) -> None: ...

class SequenceEntity(_message.Message):
    __slots__ = ("increment", "start_value", "max_value", "min_value", "cycle", "cache", "custom_features")
    INCREMENT_FIELD_NUMBER: _ClassVar[int]
    START_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    CYCLE_FIELD_NUMBER: _ClassVar[int]
    CACHE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    increment: int
    start_value: bytes
    max_value: bytes
    min_value: bytes
    cycle: bool
    cache: int
    custom_features: _struct_pb2.Struct
    def __init__(self, increment: _Optional[int] = ..., start_value: _Optional[bytes] = ..., max_value: _Optional[bytes] = ..., min_value: _Optional[bytes] = ..., cycle: bool = ..., cache: _Optional[int] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class StoredProcedureEntity(_message.Message):
    __slots__ = ("sql_code", "custom_features")
    SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    sql_code: str
    custom_features: _struct_pb2.Struct
    def __init__(self, sql_code: _Optional[str] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class FunctionEntity(_message.Message):
    __slots__ = ("sql_code", "custom_features")
    SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    sql_code: str
    custom_features: _struct_pb2.Struct
    def __init__(self, sql_code: _Optional[str] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class MaterializedViewEntity(_message.Message):
    __slots__ = ("sql_code", "custom_features")
    SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    sql_code: str
    custom_features: _struct_pb2.Struct
    def __init__(self, sql_code: _Optional[str] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SynonymEntity(_message.Message):
    __slots__ = ("source_entity", "source_type", "custom_features")
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    source_entity: str
    source_type: DatabaseEntityType
    custom_features: _struct_pb2.Struct
    def __init__(self, source_entity: _Optional[str] = ..., source_type: _Optional[_Union[DatabaseEntityType, str]] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class PackageEntity(_message.Message):
    __slots__ = ("package_sql_code", "package_body", "custom_features")
    PACKAGE_SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    package_sql_code: str
    package_body: str
    custom_features: _struct_pb2.Struct
    def __init__(self, package_sql_code: _Optional[str] = ..., package_body: _Optional[str] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UDTEntity(_message.Message):
    __slots__ = ("udt_sql_code", "udt_body", "custom_features")
    UDT_SQL_CODE_FIELD_NUMBER: _ClassVar[int]
    UDT_BODY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    udt_sql_code: str
    udt_body: str
    custom_features: _struct_pb2.Struct
    def __init__(self, udt_sql_code: _Optional[str] = ..., udt_body: _Optional[str] = ..., custom_features: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class EntityMapping(_message.Message):
    __slots__ = ("source_entity", "draft_entity", "source_type", "draft_type", "mapping_log")
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DRAFT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAPPING_LOG_FIELD_NUMBER: _ClassVar[int]
    source_entity: str
    draft_entity: str
    source_type: DatabaseEntityType
    draft_type: DatabaseEntityType
    mapping_log: _containers.RepeatedCompositeFieldContainer[EntityMappingLogEntry]
    def __init__(self, source_entity: _Optional[str] = ..., draft_entity: _Optional[str] = ..., source_type: _Optional[_Union[DatabaseEntityType, str]] = ..., draft_type: _Optional[_Union[DatabaseEntityType, str]] = ..., mapping_log: _Optional[_Iterable[_Union[EntityMappingLogEntry, _Mapping]]] = ...) -> None: ...

class EntityMappingLogEntry(_message.Message):
    __slots__ = ("rule_id", "rule_revision_id", "mapping_comment")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPING_COMMENT_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    rule_revision_id: str
    mapping_comment: str
    def __init__(self, rule_id: _Optional[str] = ..., rule_revision_id: _Optional[str] = ..., mapping_comment: _Optional[str] = ...) -> None: ...

class EntityDdl(_message.Message):
    __slots__ = ("ddl_type", "entity", "ddl", "entity_type", "issue_id")
    DDL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    DDL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    ddl_type: str
    entity: str
    ddl: str
    entity_type: DatabaseEntityType
    issue_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ddl_type: _Optional[str] = ..., entity: _Optional[str] = ..., ddl: _Optional[str] = ..., entity_type: _Optional[_Union[DatabaseEntityType, str]] = ..., issue_id: _Optional[_Iterable[str]] = ...) -> None: ...

class EntityIssue(_message.Message):
    __slots__ = ("id", "type", "severity", "message", "code", "ddl", "position", "entity_type")
    class IssueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ISSUE_TYPE_UNSPECIFIED: _ClassVar[EntityIssue.IssueType]
        ISSUE_TYPE_DDL: _ClassVar[EntityIssue.IssueType]
        ISSUE_TYPE_APPLY: _ClassVar[EntityIssue.IssueType]
        ISSUE_TYPE_CONVERT: _ClassVar[EntityIssue.IssueType]
    ISSUE_TYPE_UNSPECIFIED: EntityIssue.IssueType
    ISSUE_TYPE_DDL: EntityIssue.IssueType
    ISSUE_TYPE_APPLY: EntityIssue.IssueType
    ISSUE_TYPE_CONVERT: EntityIssue.IssueType
    class IssueSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ISSUE_SEVERITY_UNSPECIFIED: _ClassVar[EntityIssue.IssueSeverity]
        ISSUE_SEVERITY_INFO: _ClassVar[EntityIssue.IssueSeverity]
        ISSUE_SEVERITY_WARNING: _ClassVar[EntityIssue.IssueSeverity]
        ISSUE_SEVERITY_ERROR: _ClassVar[EntityIssue.IssueSeverity]
    ISSUE_SEVERITY_UNSPECIFIED: EntityIssue.IssueSeverity
    ISSUE_SEVERITY_INFO: EntityIssue.IssueSeverity
    ISSUE_SEVERITY_WARNING: EntityIssue.IssueSeverity
    ISSUE_SEVERITY_ERROR: EntityIssue.IssueSeverity
    class Position(_message.Message):
        __slots__ = ("line", "column", "offset", "length")
        LINE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        line: int
        column: int
        offset: int
        length: int
        def __init__(self, line: _Optional[int] = ..., column: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DDL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: EntityIssue.IssueType
    severity: EntityIssue.IssueSeverity
    message: str
    code: str
    ddl: str
    position: EntityIssue.Position
    entity_type: DatabaseEntityType
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[EntityIssue.IssueType, str]] = ..., severity: _Optional[_Union[EntityIssue.IssueSeverity, str]] = ..., message: _Optional[str] = ..., code: _Optional[str] = ..., ddl: _Optional[str] = ..., position: _Optional[_Union[EntityIssue.Position, _Mapping]] = ..., entity_type: _Optional[_Union[DatabaseEntityType, str]] = ...) -> None: ...
