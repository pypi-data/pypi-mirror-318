from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import processing_pb2 as _processing_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataQualitySpec(_message.Message):
    __slots__ = ("rules", "sampling_percent", "row_filter", "post_scan_actions")
    class PostScanActions(_message.Message):
        __slots__ = ("bigquery_export", "notification_report")
        class BigQueryExport(_message.Message):
            __slots__ = ("results_table",)
            RESULTS_TABLE_FIELD_NUMBER: _ClassVar[int]
            results_table: str
            def __init__(self, results_table: _Optional[str] = ...) -> None: ...
        class Recipients(_message.Message):
            __slots__ = ("emails",)
            EMAILS_FIELD_NUMBER: _ClassVar[int]
            emails: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, emails: _Optional[_Iterable[str]] = ...) -> None: ...
        class ScoreThresholdTrigger(_message.Message):
            __slots__ = ("score_threshold",)
            SCORE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            score_threshold: float
            def __init__(self, score_threshold: _Optional[float] = ...) -> None: ...
        class JobFailureTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class JobEndTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class NotificationReport(_message.Message):
            __slots__ = ("recipients", "score_threshold_trigger", "job_failure_trigger", "job_end_trigger")
            RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
            SCORE_THRESHOLD_TRIGGER_FIELD_NUMBER: _ClassVar[int]
            JOB_FAILURE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
            JOB_END_TRIGGER_FIELD_NUMBER: _ClassVar[int]
            recipients: DataQualitySpec.PostScanActions.Recipients
            score_threshold_trigger: DataQualitySpec.PostScanActions.ScoreThresholdTrigger
            job_failure_trigger: DataQualitySpec.PostScanActions.JobFailureTrigger
            job_end_trigger: DataQualitySpec.PostScanActions.JobEndTrigger
            def __init__(self, recipients: _Optional[_Union[DataQualitySpec.PostScanActions.Recipients, _Mapping]] = ..., score_threshold_trigger: _Optional[_Union[DataQualitySpec.PostScanActions.ScoreThresholdTrigger, _Mapping]] = ..., job_failure_trigger: _Optional[_Union[DataQualitySpec.PostScanActions.JobFailureTrigger, _Mapping]] = ..., job_end_trigger: _Optional[_Union[DataQualitySpec.PostScanActions.JobEndTrigger, _Mapping]] = ...) -> None: ...
        BIGQUERY_EXPORT_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_REPORT_FIELD_NUMBER: _ClassVar[int]
        bigquery_export: DataQualitySpec.PostScanActions.BigQueryExport
        notification_report: DataQualitySpec.PostScanActions.NotificationReport
        def __init__(self, bigquery_export: _Optional[_Union[DataQualitySpec.PostScanActions.BigQueryExport, _Mapping]] = ..., notification_report: _Optional[_Union[DataQualitySpec.PostScanActions.NotificationReport, _Mapping]] = ...) -> None: ...
    RULES_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ROW_FILTER_FIELD_NUMBER: _ClassVar[int]
    POST_SCAN_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[DataQualityRule]
    sampling_percent: float
    row_filter: str
    post_scan_actions: DataQualitySpec.PostScanActions
    def __init__(self, rules: _Optional[_Iterable[_Union[DataQualityRule, _Mapping]]] = ..., sampling_percent: _Optional[float] = ..., row_filter: _Optional[str] = ..., post_scan_actions: _Optional[_Union[DataQualitySpec.PostScanActions, _Mapping]] = ...) -> None: ...

class DataQualityResult(_message.Message):
    __slots__ = ("passed", "score", "dimensions", "columns", "rules", "row_count", "scanned_data", "post_scan_actions_result")
    class PostScanActionsResult(_message.Message):
        __slots__ = ("bigquery_export_result",)
        class BigQueryExportResult(_message.Message):
            __slots__ = ("state", "message")
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[DataQualityResult.PostScanActionsResult.BigQueryExportResult.State]
                SUCCEEDED: _ClassVar[DataQualityResult.PostScanActionsResult.BigQueryExportResult.State]
                FAILED: _ClassVar[DataQualityResult.PostScanActionsResult.BigQueryExportResult.State]
                SKIPPED: _ClassVar[DataQualityResult.PostScanActionsResult.BigQueryExportResult.State]
            STATE_UNSPECIFIED: DataQualityResult.PostScanActionsResult.BigQueryExportResult.State
            SUCCEEDED: DataQualityResult.PostScanActionsResult.BigQueryExportResult.State
            FAILED: DataQualityResult.PostScanActionsResult.BigQueryExportResult.State
            SKIPPED: DataQualityResult.PostScanActionsResult.BigQueryExportResult.State
            STATE_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            state: DataQualityResult.PostScanActionsResult.BigQueryExportResult.State
            message: str
            def __init__(self, state: _Optional[_Union[DataQualityResult.PostScanActionsResult.BigQueryExportResult.State, str]] = ..., message: _Optional[str] = ...) -> None: ...
        BIGQUERY_EXPORT_RESULT_FIELD_NUMBER: _ClassVar[int]
        bigquery_export_result: DataQualityResult.PostScanActionsResult.BigQueryExportResult
        def __init__(self, bigquery_export_result: _Optional[_Union[DataQualityResult.PostScanActionsResult.BigQueryExportResult, _Mapping]] = ...) -> None: ...
    PASSED_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCANNED_DATA_FIELD_NUMBER: _ClassVar[int]
    POST_SCAN_ACTIONS_RESULT_FIELD_NUMBER: _ClassVar[int]
    passed: bool
    score: float
    dimensions: _containers.RepeatedCompositeFieldContainer[DataQualityDimensionResult]
    columns: _containers.RepeatedCompositeFieldContainer[DataQualityColumnResult]
    rules: _containers.RepeatedCompositeFieldContainer[DataQualityRuleResult]
    row_count: int
    scanned_data: _processing_pb2.ScannedData
    post_scan_actions_result: DataQualityResult.PostScanActionsResult
    def __init__(self, passed: bool = ..., score: _Optional[float] = ..., dimensions: _Optional[_Iterable[_Union[DataQualityDimensionResult, _Mapping]]] = ..., columns: _Optional[_Iterable[_Union[DataQualityColumnResult, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[DataQualityRuleResult, _Mapping]]] = ..., row_count: _Optional[int] = ..., scanned_data: _Optional[_Union[_processing_pb2.ScannedData, _Mapping]] = ..., post_scan_actions_result: _Optional[_Union[DataQualityResult.PostScanActionsResult, _Mapping]] = ...) -> None: ...

class DataQualityRuleResult(_message.Message):
    __slots__ = ("rule", "passed", "evaluated_count", "passed_count", "null_count", "pass_ratio", "failing_rows_query", "assertion_row_count")
    RULE_FIELD_NUMBER: _ClassVar[int]
    PASSED_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    PASSED_COUNT_FIELD_NUMBER: _ClassVar[int]
    NULL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PASS_RATIO_FIELD_NUMBER: _ClassVar[int]
    FAILING_ROWS_QUERY_FIELD_NUMBER: _ClassVar[int]
    ASSERTION_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    rule: DataQualityRule
    passed: bool
    evaluated_count: int
    passed_count: int
    null_count: int
    pass_ratio: float
    failing_rows_query: str
    assertion_row_count: int
    def __init__(self, rule: _Optional[_Union[DataQualityRule, _Mapping]] = ..., passed: bool = ..., evaluated_count: _Optional[int] = ..., passed_count: _Optional[int] = ..., null_count: _Optional[int] = ..., pass_ratio: _Optional[float] = ..., failing_rows_query: _Optional[str] = ..., assertion_row_count: _Optional[int] = ...) -> None: ...

class DataQualityDimensionResult(_message.Message):
    __slots__ = ("dimension", "passed", "score")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    PASSED_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    dimension: DataQualityDimension
    passed: bool
    score: float
    def __init__(self, dimension: _Optional[_Union[DataQualityDimension, _Mapping]] = ..., passed: bool = ..., score: _Optional[float] = ...) -> None: ...

class DataQualityDimension(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DataQualityRule(_message.Message):
    __slots__ = ("range_expectation", "non_null_expectation", "set_expectation", "regex_expectation", "uniqueness_expectation", "statistic_range_expectation", "row_condition_expectation", "table_condition_expectation", "sql_assertion", "column", "ignore_null", "dimension", "threshold", "name", "description", "suspended")
    class RangeExpectation(_message.Message):
        __slots__ = ("min_value", "max_value", "strict_min_enabled", "strict_max_enabled")
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRICT_MIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
        STRICT_MAX_ENABLED_FIELD_NUMBER: _ClassVar[int]
        min_value: str
        max_value: str
        strict_min_enabled: bool
        strict_max_enabled: bool
        def __init__(self, min_value: _Optional[str] = ..., max_value: _Optional[str] = ..., strict_min_enabled: bool = ..., strict_max_enabled: bool = ...) -> None: ...
    class NonNullExpectation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SetExpectation(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    class RegexExpectation(_message.Message):
        __slots__ = ("regex",)
        REGEX_FIELD_NUMBER: _ClassVar[int]
        regex: str
        def __init__(self, regex: _Optional[str] = ...) -> None: ...
    class UniquenessExpectation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StatisticRangeExpectation(_message.Message):
        __slots__ = ("statistic", "min_value", "max_value", "strict_min_enabled", "strict_max_enabled")
        class ColumnStatistic(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATISTIC_UNDEFINED: _ClassVar[DataQualityRule.StatisticRangeExpectation.ColumnStatistic]
            MEAN: _ClassVar[DataQualityRule.StatisticRangeExpectation.ColumnStatistic]
            MIN: _ClassVar[DataQualityRule.StatisticRangeExpectation.ColumnStatistic]
            MAX: _ClassVar[DataQualityRule.StatisticRangeExpectation.ColumnStatistic]
        STATISTIC_UNDEFINED: DataQualityRule.StatisticRangeExpectation.ColumnStatistic
        MEAN: DataQualityRule.StatisticRangeExpectation.ColumnStatistic
        MIN: DataQualityRule.StatisticRangeExpectation.ColumnStatistic
        MAX: DataQualityRule.StatisticRangeExpectation.ColumnStatistic
        STATISTIC_FIELD_NUMBER: _ClassVar[int]
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRICT_MIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
        STRICT_MAX_ENABLED_FIELD_NUMBER: _ClassVar[int]
        statistic: DataQualityRule.StatisticRangeExpectation.ColumnStatistic
        min_value: str
        max_value: str
        strict_min_enabled: bool
        strict_max_enabled: bool
        def __init__(self, statistic: _Optional[_Union[DataQualityRule.StatisticRangeExpectation.ColumnStatistic, str]] = ..., min_value: _Optional[str] = ..., max_value: _Optional[str] = ..., strict_min_enabled: bool = ..., strict_max_enabled: bool = ...) -> None: ...
    class RowConditionExpectation(_message.Message):
        __slots__ = ("sql_expression",)
        SQL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        sql_expression: str
        def __init__(self, sql_expression: _Optional[str] = ...) -> None: ...
    class TableConditionExpectation(_message.Message):
        __slots__ = ("sql_expression",)
        SQL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        sql_expression: str
        def __init__(self, sql_expression: _Optional[str] = ...) -> None: ...
    class SqlAssertion(_message.Message):
        __slots__ = ("sql_statement",)
        SQL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
        sql_statement: str
        def __init__(self, sql_statement: _Optional[str] = ...) -> None: ...
    RANGE_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    NON_NULL_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    SET_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    REGEX_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    UNIQUENESS_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    STATISTIC_RANGE_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    ROW_CONDITION_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    TABLE_CONDITION_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
    SQL_ASSERTION_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    IGNORE_NULL_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    range_expectation: DataQualityRule.RangeExpectation
    non_null_expectation: DataQualityRule.NonNullExpectation
    set_expectation: DataQualityRule.SetExpectation
    regex_expectation: DataQualityRule.RegexExpectation
    uniqueness_expectation: DataQualityRule.UniquenessExpectation
    statistic_range_expectation: DataQualityRule.StatisticRangeExpectation
    row_condition_expectation: DataQualityRule.RowConditionExpectation
    table_condition_expectation: DataQualityRule.TableConditionExpectation
    sql_assertion: DataQualityRule.SqlAssertion
    column: str
    ignore_null: bool
    dimension: str
    threshold: float
    name: str
    description: str
    suspended: bool
    def __init__(self, range_expectation: _Optional[_Union[DataQualityRule.RangeExpectation, _Mapping]] = ..., non_null_expectation: _Optional[_Union[DataQualityRule.NonNullExpectation, _Mapping]] = ..., set_expectation: _Optional[_Union[DataQualityRule.SetExpectation, _Mapping]] = ..., regex_expectation: _Optional[_Union[DataQualityRule.RegexExpectation, _Mapping]] = ..., uniqueness_expectation: _Optional[_Union[DataQualityRule.UniquenessExpectation, _Mapping]] = ..., statistic_range_expectation: _Optional[_Union[DataQualityRule.StatisticRangeExpectation, _Mapping]] = ..., row_condition_expectation: _Optional[_Union[DataQualityRule.RowConditionExpectation, _Mapping]] = ..., table_condition_expectation: _Optional[_Union[DataQualityRule.TableConditionExpectation, _Mapping]] = ..., sql_assertion: _Optional[_Union[DataQualityRule.SqlAssertion, _Mapping]] = ..., column: _Optional[str] = ..., ignore_null: bool = ..., dimension: _Optional[str] = ..., threshold: _Optional[float] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., suspended: bool = ...) -> None: ...

class DataQualityColumnResult(_message.Message):
    __slots__ = ("column", "score")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    column: str
    score: float
    def __init__(self, column: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...
