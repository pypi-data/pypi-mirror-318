from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.v2 import dataset_reference_pb2 as _dataset_reference_pb2
from google.cloud.bigquery.v2 import model_pb2 as _model_pb2
from google.cloud.bigquery.v2 import query_parameter_pb2 as _query_parameter_pb2
from google.cloud.bigquery.v2 import routine_reference_pb2 as _routine_reference_pb2
from google.cloud.bigquery.v2 import row_access_policy_reference_pb2 as _row_access_policy_reference_pb2
from google.cloud.bigquery.v2 import session_info_pb2 as _session_info_pb2
from google.cloud.bigquery.v2 import table_reference_pb2 as _table_reference_pb2
from google.cloud.bigquery.v2 import table_schema_pb2 as _table_schema_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReservationEdition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESERVATION_EDITION_UNSPECIFIED: _ClassVar[ReservationEdition]
    STANDARD: _ClassVar[ReservationEdition]
    ENTERPRISE: _ClassVar[ReservationEdition]
    ENTERPRISE_PLUS: _ClassVar[ReservationEdition]
RESERVATION_EDITION_UNSPECIFIED: ReservationEdition
STANDARD: ReservationEdition
ENTERPRISE: ReservationEdition
ENTERPRISE_PLUS: ReservationEdition

class ExplainQueryStep(_message.Message):
    __slots__ = ("kind", "substeps")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SUBSTEPS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    substeps: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, kind: _Optional[str] = ..., substeps: _Optional[_Iterable[str]] = ...) -> None: ...

class ExplainQueryStage(_message.Message):
    __slots__ = ("name", "id", "start_ms", "end_ms", "input_stages", "wait_ratio_avg", "wait_ms_avg", "wait_ratio_max", "wait_ms_max", "read_ratio_avg", "read_ms_avg", "read_ratio_max", "read_ms_max", "compute_ratio_avg", "compute_ms_avg", "compute_ratio_max", "compute_ms_max", "write_ratio_avg", "write_ms_avg", "write_ratio_max", "write_ms_max", "shuffle_output_bytes", "shuffle_output_bytes_spilled", "records_read", "records_written", "parallel_inputs", "completed_parallel_inputs", "status", "steps", "slot_ms", "compute_mode")
    class ComputeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPUTE_MODE_UNSPECIFIED: _ClassVar[ExplainQueryStage.ComputeMode]
        BIGQUERY: _ClassVar[ExplainQueryStage.ComputeMode]
        BI_ENGINE: _ClassVar[ExplainQueryStage.ComputeMode]
    COMPUTE_MODE_UNSPECIFIED: ExplainQueryStage.ComputeMode
    BIGQUERY: ExplainQueryStage.ComputeMode
    BI_ENGINE: ExplainQueryStage.ComputeMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    START_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    INPUT_STAGES_FIELD_NUMBER: _ClassVar[int]
    WAIT_RATIO_AVG_FIELD_NUMBER: _ClassVar[int]
    WAIT_MS_AVG_FIELD_NUMBER: _ClassVar[int]
    WAIT_RATIO_MAX_FIELD_NUMBER: _ClassVar[int]
    WAIT_MS_MAX_FIELD_NUMBER: _ClassVar[int]
    READ_RATIO_AVG_FIELD_NUMBER: _ClassVar[int]
    READ_MS_AVG_FIELD_NUMBER: _ClassVar[int]
    READ_RATIO_MAX_FIELD_NUMBER: _ClassVar[int]
    READ_MS_MAX_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_RATIO_AVG_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_MS_AVG_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_RATIO_MAX_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_MS_MAX_FIELD_NUMBER: _ClassVar[int]
    WRITE_RATIO_AVG_FIELD_NUMBER: _ClassVar[int]
    WRITE_MS_AVG_FIELD_NUMBER: _ClassVar[int]
    WRITE_RATIO_MAX_FIELD_NUMBER: _ClassVar[int]
    WRITE_MS_MAX_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_OUTPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_OUTPUT_BYTES_SPILLED_FIELD_NUMBER: _ClassVar[int]
    RECORDS_READ_FIELD_NUMBER: _ClassVar[int]
    RECORDS_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_INPUTS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_PARALLEL_INPUTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    SLOT_MS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: _wrappers_pb2.Int64Value
    start_ms: int
    end_ms: int
    input_stages: _containers.RepeatedScalarFieldContainer[int]
    wait_ratio_avg: _wrappers_pb2.DoubleValue
    wait_ms_avg: _wrappers_pb2.Int64Value
    wait_ratio_max: _wrappers_pb2.DoubleValue
    wait_ms_max: _wrappers_pb2.Int64Value
    read_ratio_avg: _wrappers_pb2.DoubleValue
    read_ms_avg: _wrappers_pb2.Int64Value
    read_ratio_max: _wrappers_pb2.DoubleValue
    read_ms_max: _wrappers_pb2.Int64Value
    compute_ratio_avg: _wrappers_pb2.DoubleValue
    compute_ms_avg: _wrappers_pb2.Int64Value
    compute_ratio_max: _wrappers_pb2.DoubleValue
    compute_ms_max: _wrappers_pb2.Int64Value
    write_ratio_avg: _wrappers_pb2.DoubleValue
    write_ms_avg: _wrappers_pb2.Int64Value
    write_ratio_max: _wrappers_pb2.DoubleValue
    write_ms_max: _wrappers_pb2.Int64Value
    shuffle_output_bytes: _wrappers_pb2.Int64Value
    shuffle_output_bytes_spilled: _wrappers_pb2.Int64Value
    records_read: _wrappers_pb2.Int64Value
    records_written: _wrappers_pb2.Int64Value
    parallel_inputs: _wrappers_pb2.Int64Value
    completed_parallel_inputs: _wrappers_pb2.Int64Value
    status: str
    steps: _containers.RepeatedCompositeFieldContainer[ExplainQueryStep]
    slot_ms: _wrappers_pb2.Int64Value
    compute_mode: ExplainQueryStage.ComputeMode
    def __init__(self, name: _Optional[str] = ..., id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., start_ms: _Optional[int] = ..., end_ms: _Optional[int] = ..., input_stages: _Optional[_Iterable[int]] = ..., wait_ratio_avg: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., wait_ms_avg: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., wait_ratio_max: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., wait_ms_max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., read_ratio_avg: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., read_ms_avg: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., read_ratio_max: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., read_ms_max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., compute_ratio_avg: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., compute_ms_avg: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., compute_ratio_max: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., compute_ms_max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., write_ratio_avg: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., write_ms_avg: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., write_ratio_max: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., write_ms_max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., shuffle_output_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., shuffle_output_bytes_spilled: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., records_read: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., records_written: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., parallel_inputs: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., completed_parallel_inputs: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., status: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[ExplainQueryStep, _Mapping]]] = ..., slot_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., compute_mode: _Optional[_Union[ExplainQueryStage.ComputeMode, str]] = ...) -> None: ...

class QueryTimelineSample(_message.Message):
    __slots__ = ("elapsed_ms", "total_slot_ms", "pending_units", "completed_units", "active_units", "estimated_runnable_units")
    ELAPSED_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SLOT_MS_FIELD_NUMBER: _ClassVar[int]
    PENDING_UNITS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_UNITS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_UNITS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_RUNNABLE_UNITS_FIELD_NUMBER: _ClassVar[int]
    elapsed_ms: _wrappers_pb2.Int64Value
    total_slot_ms: _wrappers_pb2.Int64Value
    pending_units: _wrappers_pb2.Int64Value
    completed_units: _wrappers_pb2.Int64Value
    active_units: _wrappers_pb2.Int64Value
    estimated_runnable_units: _wrappers_pb2.Int64Value
    def __init__(self, elapsed_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., total_slot_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., pending_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., completed_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., active_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., estimated_runnable_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class ExternalServiceCost(_message.Message):
    __slots__ = ("external_service", "bytes_processed", "bytes_billed", "slot_ms", "reserved_slot_count")
    EXTERNAL_SERVICE_FIELD_NUMBER: _ClassVar[int]
    BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    BYTES_BILLED_FIELD_NUMBER: _ClassVar[int]
    SLOT_MS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_SLOT_COUNT_FIELD_NUMBER: _ClassVar[int]
    external_service: str
    bytes_processed: _wrappers_pb2.Int64Value
    bytes_billed: _wrappers_pb2.Int64Value
    slot_ms: _wrappers_pb2.Int64Value
    reserved_slot_count: int
    def __init__(self, external_service: _Optional[str] = ..., bytes_processed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., bytes_billed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., slot_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., reserved_slot_count: _Optional[int] = ...) -> None: ...

class ExportDataStatistics(_message.Message):
    __slots__ = ("file_count", "row_count")
    FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    file_count: _wrappers_pb2.Int64Value
    row_count: _wrappers_pb2.Int64Value
    def __init__(self, file_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., row_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class BiEngineReason(_message.Message):
    __slots__ = ("code", "message")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[BiEngineReason.Code]
        NO_RESERVATION: _ClassVar[BiEngineReason.Code]
        INSUFFICIENT_RESERVATION: _ClassVar[BiEngineReason.Code]
        UNSUPPORTED_SQL_TEXT: _ClassVar[BiEngineReason.Code]
        INPUT_TOO_LARGE: _ClassVar[BiEngineReason.Code]
        OTHER_REASON: _ClassVar[BiEngineReason.Code]
        TABLE_EXCLUDED: _ClassVar[BiEngineReason.Code]
    CODE_UNSPECIFIED: BiEngineReason.Code
    NO_RESERVATION: BiEngineReason.Code
    INSUFFICIENT_RESERVATION: BiEngineReason.Code
    UNSUPPORTED_SQL_TEXT: BiEngineReason.Code
    INPUT_TOO_LARGE: BiEngineReason.Code
    OTHER_REASON: BiEngineReason.Code
    TABLE_EXCLUDED: BiEngineReason.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: BiEngineReason.Code
    message: str
    def __init__(self, code: _Optional[_Union[BiEngineReason.Code, str]] = ..., message: _Optional[str] = ...) -> None: ...

class BiEngineStatistics(_message.Message):
    __slots__ = ("bi_engine_mode", "acceleration_mode", "bi_engine_reasons")
    class BiEngineMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCELERATION_MODE_UNSPECIFIED: _ClassVar[BiEngineStatistics.BiEngineMode]
        DISABLED: _ClassVar[BiEngineStatistics.BiEngineMode]
        PARTIAL: _ClassVar[BiEngineStatistics.BiEngineMode]
        FULL: _ClassVar[BiEngineStatistics.BiEngineMode]
    ACCELERATION_MODE_UNSPECIFIED: BiEngineStatistics.BiEngineMode
    DISABLED: BiEngineStatistics.BiEngineMode
    PARTIAL: BiEngineStatistics.BiEngineMode
    FULL: BiEngineStatistics.BiEngineMode
    class BiEngineAccelerationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED: _ClassVar[BiEngineStatistics.BiEngineAccelerationMode]
        BI_ENGINE_DISABLED: _ClassVar[BiEngineStatistics.BiEngineAccelerationMode]
        PARTIAL_INPUT: _ClassVar[BiEngineStatistics.BiEngineAccelerationMode]
        FULL_INPUT: _ClassVar[BiEngineStatistics.BiEngineAccelerationMode]
        FULL_QUERY: _ClassVar[BiEngineStatistics.BiEngineAccelerationMode]
    BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED: BiEngineStatistics.BiEngineAccelerationMode
    BI_ENGINE_DISABLED: BiEngineStatistics.BiEngineAccelerationMode
    PARTIAL_INPUT: BiEngineStatistics.BiEngineAccelerationMode
    FULL_INPUT: BiEngineStatistics.BiEngineAccelerationMode
    FULL_QUERY: BiEngineStatistics.BiEngineAccelerationMode
    BI_ENGINE_MODE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATION_MODE_FIELD_NUMBER: _ClassVar[int]
    BI_ENGINE_REASONS_FIELD_NUMBER: _ClassVar[int]
    bi_engine_mode: BiEngineStatistics.BiEngineMode
    acceleration_mode: BiEngineStatistics.BiEngineAccelerationMode
    bi_engine_reasons: _containers.RepeatedCompositeFieldContainer[BiEngineReason]
    def __init__(self, bi_engine_mode: _Optional[_Union[BiEngineStatistics.BiEngineMode, str]] = ..., acceleration_mode: _Optional[_Union[BiEngineStatistics.BiEngineAccelerationMode, str]] = ..., bi_engine_reasons: _Optional[_Iterable[_Union[BiEngineReason, _Mapping]]] = ...) -> None: ...

class IndexUnusedReason(_message.Message):
    __slots__ = ("code", "message", "base_table", "index_name")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[IndexUnusedReason.Code]
        INDEX_CONFIG_NOT_AVAILABLE: _ClassVar[IndexUnusedReason.Code]
        PENDING_INDEX_CREATION: _ClassVar[IndexUnusedReason.Code]
        BASE_TABLE_TRUNCATED: _ClassVar[IndexUnusedReason.Code]
        INDEX_CONFIG_MODIFIED: _ClassVar[IndexUnusedReason.Code]
        TIME_TRAVEL_QUERY: _ClassVar[IndexUnusedReason.Code]
        NO_PRUNING_POWER: _ClassVar[IndexUnusedReason.Code]
        UNINDEXED_SEARCH_FIELDS: _ClassVar[IndexUnusedReason.Code]
        UNSUPPORTED_SEARCH_PATTERN: _ClassVar[IndexUnusedReason.Code]
        OPTIMIZED_WITH_MATERIALIZED_VIEW: _ClassVar[IndexUnusedReason.Code]
        SECURED_BY_DATA_MASKING: _ClassVar[IndexUnusedReason.Code]
        MISMATCHED_TEXT_ANALYZER: _ClassVar[IndexUnusedReason.Code]
        BASE_TABLE_TOO_SMALL: _ClassVar[IndexUnusedReason.Code]
        BASE_TABLE_TOO_LARGE: _ClassVar[IndexUnusedReason.Code]
        ESTIMATED_PERFORMANCE_GAIN_TOO_LOW: _ClassVar[IndexUnusedReason.Code]
        NOT_SUPPORTED_IN_STANDARD_EDITION: _ClassVar[IndexUnusedReason.Code]
        INDEX_SUPPRESSED_BY_FUNCTION_OPTION: _ClassVar[IndexUnusedReason.Code]
        QUERY_CACHE_HIT: _ClassVar[IndexUnusedReason.Code]
        STALE_INDEX: _ClassVar[IndexUnusedReason.Code]
        INTERNAL_ERROR: _ClassVar[IndexUnusedReason.Code]
        OTHER_REASON: _ClassVar[IndexUnusedReason.Code]
    CODE_UNSPECIFIED: IndexUnusedReason.Code
    INDEX_CONFIG_NOT_AVAILABLE: IndexUnusedReason.Code
    PENDING_INDEX_CREATION: IndexUnusedReason.Code
    BASE_TABLE_TRUNCATED: IndexUnusedReason.Code
    INDEX_CONFIG_MODIFIED: IndexUnusedReason.Code
    TIME_TRAVEL_QUERY: IndexUnusedReason.Code
    NO_PRUNING_POWER: IndexUnusedReason.Code
    UNINDEXED_SEARCH_FIELDS: IndexUnusedReason.Code
    UNSUPPORTED_SEARCH_PATTERN: IndexUnusedReason.Code
    OPTIMIZED_WITH_MATERIALIZED_VIEW: IndexUnusedReason.Code
    SECURED_BY_DATA_MASKING: IndexUnusedReason.Code
    MISMATCHED_TEXT_ANALYZER: IndexUnusedReason.Code
    BASE_TABLE_TOO_SMALL: IndexUnusedReason.Code
    BASE_TABLE_TOO_LARGE: IndexUnusedReason.Code
    ESTIMATED_PERFORMANCE_GAIN_TOO_LOW: IndexUnusedReason.Code
    NOT_SUPPORTED_IN_STANDARD_EDITION: IndexUnusedReason.Code
    INDEX_SUPPRESSED_BY_FUNCTION_OPTION: IndexUnusedReason.Code
    QUERY_CACHE_HIT: IndexUnusedReason.Code
    STALE_INDEX: IndexUnusedReason.Code
    INTERNAL_ERROR: IndexUnusedReason.Code
    OTHER_REASON: IndexUnusedReason.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BASE_TABLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    code: IndexUnusedReason.Code
    message: str
    base_table: _table_reference_pb2.TableReference
    index_name: str
    def __init__(self, code: _Optional[_Union[IndexUnusedReason.Code, str]] = ..., message: _Optional[str] = ..., base_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., index_name: _Optional[str] = ...) -> None: ...

class SearchStatistics(_message.Message):
    __slots__ = ("index_usage_mode", "index_unused_reasons")
    class IndexUsageMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEX_USAGE_MODE_UNSPECIFIED: _ClassVar[SearchStatistics.IndexUsageMode]
        UNUSED: _ClassVar[SearchStatistics.IndexUsageMode]
        PARTIALLY_USED: _ClassVar[SearchStatistics.IndexUsageMode]
        FULLY_USED: _ClassVar[SearchStatistics.IndexUsageMode]
    INDEX_USAGE_MODE_UNSPECIFIED: SearchStatistics.IndexUsageMode
    UNUSED: SearchStatistics.IndexUsageMode
    PARTIALLY_USED: SearchStatistics.IndexUsageMode
    FULLY_USED: SearchStatistics.IndexUsageMode
    INDEX_USAGE_MODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_UNUSED_REASONS_FIELD_NUMBER: _ClassVar[int]
    index_usage_mode: SearchStatistics.IndexUsageMode
    index_unused_reasons: _containers.RepeatedCompositeFieldContainer[IndexUnusedReason]
    def __init__(self, index_usage_mode: _Optional[_Union[SearchStatistics.IndexUsageMode, str]] = ..., index_unused_reasons: _Optional[_Iterable[_Union[IndexUnusedReason, _Mapping]]] = ...) -> None: ...

class VectorSearchStatistics(_message.Message):
    __slots__ = ("index_usage_mode", "index_unused_reasons")
    class IndexUsageMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEX_USAGE_MODE_UNSPECIFIED: _ClassVar[VectorSearchStatistics.IndexUsageMode]
        UNUSED: _ClassVar[VectorSearchStatistics.IndexUsageMode]
        PARTIALLY_USED: _ClassVar[VectorSearchStatistics.IndexUsageMode]
        FULLY_USED: _ClassVar[VectorSearchStatistics.IndexUsageMode]
    INDEX_USAGE_MODE_UNSPECIFIED: VectorSearchStatistics.IndexUsageMode
    UNUSED: VectorSearchStatistics.IndexUsageMode
    PARTIALLY_USED: VectorSearchStatistics.IndexUsageMode
    FULLY_USED: VectorSearchStatistics.IndexUsageMode
    INDEX_USAGE_MODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_UNUSED_REASONS_FIELD_NUMBER: _ClassVar[int]
    index_usage_mode: VectorSearchStatistics.IndexUsageMode
    index_unused_reasons: _containers.RepeatedCompositeFieldContainer[IndexUnusedReason]
    def __init__(self, index_usage_mode: _Optional[_Union[VectorSearchStatistics.IndexUsageMode, str]] = ..., index_unused_reasons: _Optional[_Iterable[_Union[IndexUnusedReason, _Mapping]]] = ...) -> None: ...

class QueryInfo(_message.Message):
    __slots__ = ("optimization_details",)
    OPTIMIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    optimization_details: _struct_pb2.Struct
    def __init__(self, optimization_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class LoadQueryStatistics(_message.Message):
    __slots__ = ("input_files", "input_file_bytes", "output_rows", "output_bytes", "bad_records")
    INPUT_FILES_FIELD_NUMBER: _ClassVar[int]
    INPUT_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ROWS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    BAD_RECORDS_FIELD_NUMBER: _ClassVar[int]
    input_files: _wrappers_pb2.Int64Value
    input_file_bytes: _wrappers_pb2.Int64Value
    output_rows: _wrappers_pb2.Int64Value
    output_bytes: _wrappers_pb2.Int64Value
    bad_records: _wrappers_pb2.Int64Value
    def __init__(self, input_files: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., input_file_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., output_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., output_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., bad_records: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class JobStatistics2(_message.Message):
    __slots__ = ("query_plan", "estimated_bytes_processed", "timeline", "total_partitions_processed", "total_bytes_processed", "total_bytes_processed_accuracy", "total_bytes_billed", "billing_tier", "total_slot_ms", "cache_hit", "referenced_tables", "referenced_routines", "schema", "num_dml_affected_rows", "dml_stats", "undeclared_query_parameters", "statement_type", "ddl_operation_performed", "ddl_target_table", "ddl_destination_table", "ddl_target_row_access_policy", "ddl_affected_row_access_policy_count", "ddl_target_routine", "ddl_target_dataset", "ml_statistics", "export_data_statistics", "external_service_costs", "bi_engine_statistics", "load_query_statistics", "dcl_target_table", "dcl_target_view", "dcl_target_dataset", "search_statistics", "vector_search_statistics", "performance_insights", "query_info", "spark_statistics", "transferred_bytes", "materialized_view_statistics", "metadata_cache_statistics")
    QUERY_PLAN_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PARTITIONS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PROCESSED_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_BILLED_FIELD_NUMBER: _ClassVar[int]
    BILLING_TIER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SLOT_MS_FIELD_NUMBER: _ClassVar[int]
    CACHE_HIT_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_TABLES_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_ROUTINES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NUM_DML_AFFECTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    DML_STATS_FIELD_NUMBER: _ClassVar[int]
    UNDECLARED_QUERY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DDL_OPERATION_PERFORMED_FIELD_NUMBER: _ClassVar[int]
    DDL_TARGET_TABLE_FIELD_NUMBER: _ClassVar[int]
    DDL_DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
    DDL_TARGET_ROW_ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
    DDL_AFFECTED_ROW_ACCESS_POLICY_COUNT_FIELD_NUMBER: _ClassVar[int]
    DDL_TARGET_ROUTINE_FIELD_NUMBER: _ClassVar[int]
    DDL_TARGET_DATASET_FIELD_NUMBER: _ClassVar[int]
    ML_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DATA_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SERVICE_COSTS_FIELD_NUMBER: _ClassVar[int]
    BI_ENGINE_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    LOAD_QUERY_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    DCL_TARGET_TABLE_FIELD_NUMBER: _ClassVar[int]
    DCL_TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
    DCL_TARGET_DATASET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    VECTOR_SEARCH_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INFO_FIELD_NUMBER: _ClassVar[int]
    SPARK_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_BYTES_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZED_VIEW_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    METADATA_CACHE_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    query_plan: _containers.RepeatedCompositeFieldContainer[ExplainQueryStage]
    estimated_bytes_processed: _wrappers_pb2.Int64Value
    timeline: _containers.RepeatedCompositeFieldContainer[QueryTimelineSample]
    total_partitions_processed: _wrappers_pb2.Int64Value
    total_bytes_processed: _wrappers_pb2.Int64Value
    total_bytes_processed_accuracy: str
    total_bytes_billed: _wrappers_pb2.Int64Value
    billing_tier: _wrappers_pb2.Int32Value
    total_slot_ms: _wrappers_pb2.Int64Value
    cache_hit: _wrappers_pb2.BoolValue
    referenced_tables: _containers.RepeatedCompositeFieldContainer[_table_reference_pb2.TableReference]
    referenced_routines: _containers.RepeatedCompositeFieldContainer[_routine_reference_pb2.RoutineReference]
    schema: _table_schema_pb2.TableSchema
    num_dml_affected_rows: _wrappers_pb2.Int64Value
    dml_stats: DmlStats
    undeclared_query_parameters: _containers.RepeatedCompositeFieldContainer[_query_parameter_pb2.QueryParameter]
    statement_type: str
    ddl_operation_performed: str
    ddl_target_table: _table_reference_pb2.TableReference
    ddl_destination_table: _table_reference_pb2.TableReference
    ddl_target_row_access_policy: _row_access_policy_reference_pb2.RowAccessPolicyReference
    ddl_affected_row_access_policy_count: _wrappers_pb2.Int64Value
    ddl_target_routine: _routine_reference_pb2.RoutineReference
    ddl_target_dataset: _dataset_reference_pb2.DatasetReference
    ml_statistics: MlStatistics
    export_data_statistics: ExportDataStatistics
    external_service_costs: _containers.RepeatedCompositeFieldContainer[ExternalServiceCost]
    bi_engine_statistics: BiEngineStatistics
    load_query_statistics: LoadQueryStatistics
    dcl_target_table: _table_reference_pb2.TableReference
    dcl_target_view: _table_reference_pb2.TableReference
    dcl_target_dataset: _dataset_reference_pb2.DatasetReference
    search_statistics: SearchStatistics
    vector_search_statistics: VectorSearchStatistics
    performance_insights: PerformanceInsights
    query_info: QueryInfo
    spark_statistics: SparkStatistics
    transferred_bytes: _wrappers_pb2.Int64Value
    materialized_view_statistics: MaterializedViewStatistics
    metadata_cache_statistics: MetadataCacheStatistics
    def __init__(self, query_plan: _Optional[_Iterable[_Union[ExplainQueryStage, _Mapping]]] = ..., estimated_bytes_processed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., timeline: _Optional[_Iterable[_Union[QueryTimelineSample, _Mapping]]] = ..., total_partitions_processed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., total_bytes_processed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., total_bytes_processed_accuracy: _Optional[str] = ..., total_bytes_billed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., billing_tier: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., total_slot_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., cache_hit: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., referenced_tables: _Optional[_Iterable[_Union[_table_reference_pb2.TableReference, _Mapping]]] = ..., referenced_routines: _Optional[_Iterable[_Union[_routine_reference_pb2.RoutineReference, _Mapping]]] = ..., schema: _Optional[_Union[_table_schema_pb2.TableSchema, _Mapping]] = ..., num_dml_affected_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., dml_stats: _Optional[_Union[DmlStats, _Mapping]] = ..., undeclared_query_parameters: _Optional[_Iterable[_Union[_query_parameter_pb2.QueryParameter, _Mapping]]] = ..., statement_type: _Optional[str] = ..., ddl_operation_performed: _Optional[str] = ..., ddl_target_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., ddl_destination_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., ddl_target_row_access_policy: _Optional[_Union[_row_access_policy_reference_pb2.RowAccessPolicyReference, _Mapping]] = ..., ddl_affected_row_access_policy_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., ddl_target_routine: _Optional[_Union[_routine_reference_pb2.RoutineReference, _Mapping]] = ..., ddl_target_dataset: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ..., ml_statistics: _Optional[_Union[MlStatistics, _Mapping]] = ..., export_data_statistics: _Optional[_Union[ExportDataStatistics, _Mapping]] = ..., external_service_costs: _Optional[_Iterable[_Union[ExternalServiceCost, _Mapping]]] = ..., bi_engine_statistics: _Optional[_Union[BiEngineStatistics, _Mapping]] = ..., load_query_statistics: _Optional[_Union[LoadQueryStatistics, _Mapping]] = ..., dcl_target_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., dcl_target_view: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., dcl_target_dataset: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ..., search_statistics: _Optional[_Union[SearchStatistics, _Mapping]] = ..., vector_search_statistics: _Optional[_Union[VectorSearchStatistics, _Mapping]] = ..., performance_insights: _Optional[_Union[PerformanceInsights, _Mapping]] = ..., query_info: _Optional[_Union[QueryInfo, _Mapping]] = ..., spark_statistics: _Optional[_Union[SparkStatistics, _Mapping]] = ..., transferred_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., materialized_view_statistics: _Optional[_Union[MaterializedViewStatistics, _Mapping]] = ..., metadata_cache_statistics: _Optional[_Union[MetadataCacheStatistics, _Mapping]] = ...) -> None: ...

class JobStatistics3(_message.Message):
    __slots__ = ("input_files", "input_file_bytes", "output_rows", "output_bytes", "bad_records", "timeline")
    INPUT_FILES_FIELD_NUMBER: _ClassVar[int]
    INPUT_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ROWS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    BAD_RECORDS_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    input_files: _wrappers_pb2.Int64Value
    input_file_bytes: _wrappers_pb2.Int64Value
    output_rows: _wrappers_pb2.Int64Value
    output_bytes: _wrappers_pb2.Int64Value
    bad_records: _wrappers_pb2.Int64Value
    timeline: _containers.RepeatedCompositeFieldContainer[QueryTimelineSample]
    def __init__(self, input_files: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., input_file_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., output_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., output_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., bad_records: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., timeline: _Optional[_Iterable[_Union[QueryTimelineSample, _Mapping]]] = ...) -> None: ...

class JobStatistics4(_message.Message):
    __slots__ = ("destination_uri_file_counts", "input_bytes", "timeline")
    DESTINATION_URI_FILE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    destination_uri_file_counts: _containers.RepeatedScalarFieldContainer[int]
    input_bytes: _wrappers_pb2.Int64Value
    timeline: _containers.RepeatedCompositeFieldContainer[QueryTimelineSample]
    def __init__(self, destination_uri_file_counts: _Optional[_Iterable[int]] = ..., input_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., timeline: _Optional[_Iterable[_Union[QueryTimelineSample, _Mapping]]] = ...) -> None: ...

class CopyJobStatistics(_message.Message):
    __slots__ = ("copied_rows", "copied_logical_bytes")
    COPIED_ROWS_FIELD_NUMBER: _ClassVar[int]
    COPIED_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    copied_rows: _wrappers_pb2.Int64Value
    copied_logical_bytes: _wrappers_pb2.Int64Value
    def __init__(self, copied_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., copied_logical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class MlStatistics(_message.Message):
    __slots__ = ("max_iterations", "iteration_results", "model_type", "training_type", "hparam_trials")
    class TrainingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRAINING_TYPE_UNSPECIFIED: _ClassVar[MlStatistics.TrainingType]
        SINGLE_TRAINING: _ClassVar[MlStatistics.TrainingType]
        HPARAM_TUNING: _ClassVar[MlStatistics.TrainingType]
    TRAINING_TYPE_UNSPECIFIED: MlStatistics.TrainingType
    SINGLE_TRAINING: MlStatistics.TrainingType
    HPARAM_TUNING: MlStatistics.TrainingType
    MAX_ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    ITERATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRAINING_TYPE_FIELD_NUMBER: _ClassVar[int]
    HPARAM_TRIALS_FIELD_NUMBER: _ClassVar[int]
    max_iterations: int
    iteration_results: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model.TrainingRun.IterationResult]
    model_type: _model_pb2.Model.ModelType
    training_type: MlStatistics.TrainingType
    hparam_trials: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model.HparamTuningTrial]
    def __init__(self, max_iterations: _Optional[int] = ..., iteration_results: _Optional[_Iterable[_Union[_model_pb2.Model.TrainingRun.IterationResult, _Mapping]]] = ..., model_type: _Optional[_Union[_model_pb2.Model.ModelType, str]] = ..., training_type: _Optional[_Union[MlStatistics.TrainingType, str]] = ..., hparam_trials: _Optional[_Iterable[_Union[_model_pb2.Model.HparamTuningTrial, _Mapping]]] = ...) -> None: ...

class ScriptStatistics(_message.Message):
    __slots__ = ("evaluation_kind", "stack_frames")
    class EvaluationKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATION_KIND_UNSPECIFIED: _ClassVar[ScriptStatistics.EvaluationKind]
        STATEMENT: _ClassVar[ScriptStatistics.EvaluationKind]
        EXPRESSION: _ClassVar[ScriptStatistics.EvaluationKind]
    EVALUATION_KIND_UNSPECIFIED: ScriptStatistics.EvaluationKind
    STATEMENT: ScriptStatistics.EvaluationKind
    EXPRESSION: ScriptStatistics.EvaluationKind
    class ScriptStackFrame(_message.Message):
        __slots__ = ("start_line", "start_column", "end_line", "end_column", "procedure_id", "text")
        START_LINE_FIELD_NUMBER: _ClassVar[int]
        START_COLUMN_FIELD_NUMBER: _ClassVar[int]
        END_LINE_FIELD_NUMBER: _ClassVar[int]
        END_COLUMN_FIELD_NUMBER: _ClassVar[int]
        PROCEDURE_ID_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        start_line: int
        start_column: int
        end_line: int
        end_column: int
        procedure_id: str
        text: str
        def __init__(self, start_line: _Optional[int] = ..., start_column: _Optional[int] = ..., end_line: _Optional[int] = ..., end_column: _Optional[int] = ..., procedure_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    EVALUATION_KIND_FIELD_NUMBER: _ClassVar[int]
    STACK_FRAMES_FIELD_NUMBER: _ClassVar[int]
    evaluation_kind: ScriptStatistics.EvaluationKind
    stack_frames: _containers.RepeatedCompositeFieldContainer[ScriptStatistics.ScriptStackFrame]
    def __init__(self, evaluation_kind: _Optional[_Union[ScriptStatistics.EvaluationKind, str]] = ..., stack_frames: _Optional[_Iterable[_Union[ScriptStatistics.ScriptStackFrame, _Mapping]]] = ...) -> None: ...

class RowLevelSecurityStatistics(_message.Message):
    __slots__ = ("row_level_security_applied",)
    ROW_LEVEL_SECURITY_APPLIED_FIELD_NUMBER: _ClassVar[int]
    row_level_security_applied: bool
    def __init__(self, row_level_security_applied: bool = ...) -> None: ...

class DataMaskingStatistics(_message.Message):
    __slots__ = ("data_masking_applied",)
    DATA_MASKING_APPLIED_FIELD_NUMBER: _ClassVar[int]
    data_masking_applied: bool
    def __init__(self, data_masking_applied: bool = ...) -> None: ...

class JobStatistics(_message.Message):
    __slots__ = ("creation_time", "start_time", "end_time", "total_bytes_processed", "completion_ratio", "quota_deferments", "query", "load", "extract", "copy", "total_slot_ms", "reservation_id", "num_child_jobs", "parent_job_id", "script_statistics", "row_level_security_statistics", "data_masking_statistics", "transaction_info", "session_info", "final_execution_duration_ms", "edition")
    class TransactionInfo(_message.Message):
        __slots__ = ("transaction_id",)
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        transaction_id: str
        def __init__(self, transaction_id: _Optional[str] = ...) -> None: ...
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_RATIO_FIELD_NUMBER: _ClassVar[int]
    QUOTA_DEFERMENTS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_FIELD_NUMBER: _ClassVar[int]
    COPY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SLOT_MS_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_CHILD_JOBS_FIELD_NUMBER: _ClassVar[int]
    PARENT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    ROW_LEVEL_SECURITY_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    DATA_MASKING_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    FINAL_EXECUTION_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    creation_time: int
    start_time: int
    end_time: int
    total_bytes_processed: _wrappers_pb2.Int64Value
    completion_ratio: _wrappers_pb2.DoubleValue
    quota_deferments: _containers.RepeatedScalarFieldContainer[str]
    query: JobStatistics2
    load: JobStatistics3
    extract: JobStatistics4
    copy: CopyJobStatistics
    total_slot_ms: _wrappers_pb2.Int64Value
    reservation_id: str
    num_child_jobs: int
    parent_job_id: str
    script_statistics: ScriptStatistics
    row_level_security_statistics: RowLevelSecurityStatistics
    data_masking_statistics: DataMaskingStatistics
    transaction_info: JobStatistics.TransactionInfo
    session_info: _session_info_pb2.SessionInfo
    final_execution_duration_ms: int
    edition: ReservationEdition
    def __init__(self, creation_time: _Optional[int] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., total_bytes_processed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., completion_ratio: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., quota_deferments: _Optional[_Iterable[str]] = ..., query: _Optional[_Union[JobStatistics2, _Mapping]] = ..., load: _Optional[_Union[JobStatistics3, _Mapping]] = ..., extract: _Optional[_Union[JobStatistics4, _Mapping]] = ..., copy: _Optional[_Union[CopyJobStatistics, _Mapping]] = ..., total_slot_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., reservation_id: _Optional[str] = ..., num_child_jobs: _Optional[int] = ..., parent_job_id: _Optional[str] = ..., script_statistics: _Optional[_Union[ScriptStatistics, _Mapping]] = ..., row_level_security_statistics: _Optional[_Union[RowLevelSecurityStatistics, _Mapping]] = ..., data_masking_statistics: _Optional[_Union[DataMaskingStatistics, _Mapping]] = ..., transaction_info: _Optional[_Union[JobStatistics.TransactionInfo, _Mapping]] = ..., session_info: _Optional[_Union[_session_info_pb2.SessionInfo, _Mapping]] = ..., final_execution_duration_ms: _Optional[int] = ..., edition: _Optional[_Union[ReservationEdition, str]] = ...) -> None: ...

class DmlStats(_message.Message):
    __slots__ = ("inserted_row_count", "deleted_row_count", "updated_row_count")
    INSERTED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    inserted_row_count: _wrappers_pb2.Int64Value
    deleted_row_count: _wrappers_pb2.Int64Value
    updated_row_count: _wrappers_pb2.Int64Value
    def __init__(self, inserted_row_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., deleted_row_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., updated_row_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class PerformanceInsights(_message.Message):
    __slots__ = ("avg_previous_execution_ms", "stage_performance_standalone_insights", "stage_performance_change_insights")
    AVG_PREVIOUS_EXECUTION_MS_FIELD_NUMBER: _ClassVar[int]
    STAGE_PERFORMANCE_STANDALONE_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    STAGE_PERFORMANCE_CHANGE_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    avg_previous_execution_ms: int
    stage_performance_standalone_insights: _containers.RepeatedCompositeFieldContainer[StagePerformanceStandaloneInsight]
    stage_performance_change_insights: _containers.RepeatedCompositeFieldContainer[StagePerformanceChangeInsight]
    def __init__(self, avg_previous_execution_ms: _Optional[int] = ..., stage_performance_standalone_insights: _Optional[_Iterable[_Union[StagePerformanceStandaloneInsight, _Mapping]]] = ..., stage_performance_change_insights: _Optional[_Iterable[_Union[StagePerformanceChangeInsight, _Mapping]]] = ...) -> None: ...

class StagePerformanceChangeInsight(_message.Message):
    __slots__ = ("stage_id", "input_data_change")
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_CHANGE_FIELD_NUMBER: _ClassVar[int]
    stage_id: int
    input_data_change: InputDataChange
    def __init__(self, stage_id: _Optional[int] = ..., input_data_change: _Optional[_Union[InputDataChange, _Mapping]] = ...) -> None: ...

class InputDataChange(_message.Message):
    __slots__ = ("records_read_diff_percentage",)
    RECORDS_READ_DIFF_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    records_read_diff_percentage: float
    def __init__(self, records_read_diff_percentage: _Optional[float] = ...) -> None: ...

class StagePerformanceStandaloneInsight(_message.Message):
    __slots__ = ("stage_id", "slot_contention", "insufficient_shuffle_quota", "bi_engine_reasons", "high_cardinality_joins", "partition_skew")
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_CONTENTION_FIELD_NUMBER: _ClassVar[int]
    INSUFFICIENT_SHUFFLE_QUOTA_FIELD_NUMBER: _ClassVar[int]
    BI_ENGINE_REASONS_FIELD_NUMBER: _ClassVar[int]
    HIGH_CARDINALITY_JOINS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_SKEW_FIELD_NUMBER: _ClassVar[int]
    stage_id: int
    slot_contention: bool
    insufficient_shuffle_quota: bool
    bi_engine_reasons: _containers.RepeatedCompositeFieldContainer[BiEngineReason]
    high_cardinality_joins: _containers.RepeatedCompositeFieldContainer[HighCardinalityJoin]
    partition_skew: PartitionSkew
    def __init__(self, stage_id: _Optional[int] = ..., slot_contention: bool = ..., insufficient_shuffle_quota: bool = ..., bi_engine_reasons: _Optional[_Iterable[_Union[BiEngineReason, _Mapping]]] = ..., high_cardinality_joins: _Optional[_Iterable[_Union[HighCardinalityJoin, _Mapping]]] = ..., partition_skew: _Optional[_Union[PartitionSkew, _Mapping]] = ...) -> None: ...

class HighCardinalityJoin(_message.Message):
    __slots__ = ("left_rows", "right_rows", "output_rows", "step_index")
    LEFT_ROWS_FIELD_NUMBER: _ClassVar[int]
    RIGHT_ROWS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ROWS_FIELD_NUMBER: _ClassVar[int]
    STEP_INDEX_FIELD_NUMBER: _ClassVar[int]
    left_rows: int
    right_rows: int
    output_rows: int
    step_index: int
    def __init__(self, left_rows: _Optional[int] = ..., right_rows: _Optional[int] = ..., output_rows: _Optional[int] = ..., step_index: _Optional[int] = ...) -> None: ...

class PartitionSkew(_message.Message):
    __slots__ = ("skew_sources",)
    class SkewSource(_message.Message):
        __slots__ = ("stage_id",)
        STAGE_ID_FIELD_NUMBER: _ClassVar[int]
        stage_id: int
        def __init__(self, stage_id: _Optional[int] = ...) -> None: ...
    SKEW_SOURCES_FIELD_NUMBER: _ClassVar[int]
    skew_sources: _containers.RepeatedCompositeFieldContainer[PartitionSkew.SkewSource]
    def __init__(self, skew_sources: _Optional[_Iterable[_Union[PartitionSkew.SkewSource, _Mapping]]] = ...) -> None: ...

class SparkStatistics(_message.Message):
    __slots__ = ("spark_job_id", "spark_job_location", "endpoints", "logging_info", "kms_key_name", "gcs_staging_bucket")
    class LoggingInfo(_message.Message):
        __slots__ = ("resource_type", "project_id")
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        resource_type: str
        project_id: str
        def __init__(self, resource_type: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...
    class EndpointsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SPARK_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SPARK_JOB_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    LOGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    GCS_STAGING_BUCKET_FIELD_NUMBER: _ClassVar[int]
    spark_job_id: str
    spark_job_location: str
    endpoints: _containers.ScalarMap[str, str]
    logging_info: SparkStatistics.LoggingInfo
    kms_key_name: str
    gcs_staging_bucket: str
    def __init__(self, spark_job_id: _Optional[str] = ..., spark_job_location: _Optional[str] = ..., endpoints: _Optional[_Mapping[str, str]] = ..., logging_info: _Optional[_Union[SparkStatistics.LoggingInfo, _Mapping]] = ..., kms_key_name: _Optional[str] = ..., gcs_staging_bucket: _Optional[str] = ...) -> None: ...

class MaterializedViewStatistics(_message.Message):
    __slots__ = ("materialized_view",)
    MATERIALIZED_VIEW_FIELD_NUMBER: _ClassVar[int]
    materialized_view: _containers.RepeatedCompositeFieldContainer[MaterializedView]
    def __init__(self, materialized_view: _Optional[_Iterable[_Union[MaterializedView, _Mapping]]] = ...) -> None: ...

class MaterializedView(_message.Message):
    __slots__ = ("table_reference", "chosen", "estimated_bytes_saved", "rejected_reason")
    class RejectedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REJECTED_REASON_UNSPECIFIED: _ClassVar[MaterializedView.RejectedReason]
        NO_DATA: _ClassVar[MaterializedView.RejectedReason]
        COST: _ClassVar[MaterializedView.RejectedReason]
        BASE_TABLE_TRUNCATED: _ClassVar[MaterializedView.RejectedReason]
        BASE_TABLE_DATA_CHANGE: _ClassVar[MaterializedView.RejectedReason]
        BASE_TABLE_PARTITION_EXPIRATION_CHANGE: _ClassVar[MaterializedView.RejectedReason]
        BASE_TABLE_EXPIRED_PARTITION: _ClassVar[MaterializedView.RejectedReason]
        BASE_TABLE_INCOMPATIBLE_METADATA_CHANGE: _ClassVar[MaterializedView.RejectedReason]
        TIME_ZONE: _ClassVar[MaterializedView.RejectedReason]
        OUT_OF_TIME_TRAVEL_WINDOW: _ClassVar[MaterializedView.RejectedReason]
        BASE_TABLE_FINE_GRAINED_SECURITY_POLICY: _ClassVar[MaterializedView.RejectedReason]
        BASE_TABLE_TOO_STALE: _ClassVar[MaterializedView.RejectedReason]
    REJECTED_REASON_UNSPECIFIED: MaterializedView.RejectedReason
    NO_DATA: MaterializedView.RejectedReason
    COST: MaterializedView.RejectedReason
    BASE_TABLE_TRUNCATED: MaterializedView.RejectedReason
    BASE_TABLE_DATA_CHANGE: MaterializedView.RejectedReason
    BASE_TABLE_PARTITION_EXPIRATION_CHANGE: MaterializedView.RejectedReason
    BASE_TABLE_EXPIRED_PARTITION: MaterializedView.RejectedReason
    BASE_TABLE_INCOMPATIBLE_METADATA_CHANGE: MaterializedView.RejectedReason
    TIME_ZONE: MaterializedView.RejectedReason
    OUT_OF_TIME_TRAVEL_WINDOW: MaterializedView.RejectedReason
    BASE_TABLE_FINE_GRAINED_SECURITY_POLICY: MaterializedView.RejectedReason
    BASE_TABLE_TOO_STALE: MaterializedView.RejectedReason
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_BYTES_SAVED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_REASON_FIELD_NUMBER: _ClassVar[int]
    table_reference: _table_reference_pb2.TableReference
    chosen: bool
    estimated_bytes_saved: int
    rejected_reason: MaterializedView.RejectedReason
    def __init__(self, table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., chosen: bool = ..., estimated_bytes_saved: _Optional[int] = ..., rejected_reason: _Optional[_Union[MaterializedView.RejectedReason, str]] = ...) -> None: ...

class TableMetadataCacheUsage(_message.Message):
    __slots__ = ("table_reference", "unused_reason", "explanation", "staleness", "table_type")
    class UnusedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNUSED_REASON_UNSPECIFIED: _ClassVar[TableMetadataCacheUsage.UnusedReason]
        EXCEEDED_MAX_STALENESS: _ClassVar[TableMetadataCacheUsage.UnusedReason]
        METADATA_CACHING_NOT_ENABLED: _ClassVar[TableMetadataCacheUsage.UnusedReason]
        OTHER_REASON: _ClassVar[TableMetadataCacheUsage.UnusedReason]
    UNUSED_REASON_UNSPECIFIED: TableMetadataCacheUsage.UnusedReason
    EXCEEDED_MAX_STALENESS: TableMetadataCacheUsage.UnusedReason
    METADATA_CACHING_NOT_ENABLED: TableMetadataCacheUsage.UnusedReason
    OTHER_REASON: TableMetadataCacheUsage.UnusedReason
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    UNUSED_REASON_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    STALENESS_FIELD_NUMBER: _ClassVar[int]
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    table_reference: _table_reference_pb2.TableReference
    unused_reason: TableMetadataCacheUsage.UnusedReason
    explanation: str
    staleness: _duration_pb2.Duration
    table_type: str
    def __init__(self, table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., unused_reason: _Optional[_Union[TableMetadataCacheUsage.UnusedReason, str]] = ..., explanation: _Optional[str] = ..., staleness: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., table_type: _Optional[str] = ...) -> None: ...

class MetadataCacheStatistics(_message.Message):
    __slots__ = ("table_metadata_cache_usage",)
    TABLE_METADATA_CACHE_USAGE_FIELD_NUMBER: _ClassVar[int]
    table_metadata_cache_usage: _containers.RepeatedCompositeFieldContainer[TableMetadataCacheUsage]
    def __init__(self, table_metadata_cache_usage: _Optional[_Iterable[_Union[TableMetadataCacheUsage, _Mapping]]] = ...) -> None: ...
