from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import common_pb2 as _common_pb2
from google.monitoring.v3 import mutation_record_pb2 as _mutation_record_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertPolicy(_message.Message):
    __slots__ = ("name", "display_name", "documentation", "user_labels", "conditions", "combiner", "enabled", "validity", "notification_channels", "creation_record", "mutation_record", "alert_strategy", "severity")
    class ConditionCombinerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMBINE_UNSPECIFIED: _ClassVar[AlertPolicy.ConditionCombinerType]
        AND: _ClassVar[AlertPolicy.ConditionCombinerType]
        OR: _ClassVar[AlertPolicy.ConditionCombinerType]
        AND_WITH_MATCHING_RESOURCE: _ClassVar[AlertPolicy.ConditionCombinerType]
    COMBINE_UNSPECIFIED: AlertPolicy.ConditionCombinerType
    AND: AlertPolicy.ConditionCombinerType
    OR: AlertPolicy.ConditionCombinerType
    AND_WITH_MATCHING_RESOURCE: AlertPolicy.ConditionCombinerType
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[AlertPolicy.Severity]
        CRITICAL: _ClassVar[AlertPolicy.Severity]
        ERROR: _ClassVar[AlertPolicy.Severity]
        WARNING: _ClassVar[AlertPolicy.Severity]
    SEVERITY_UNSPECIFIED: AlertPolicy.Severity
    CRITICAL: AlertPolicy.Severity
    ERROR: AlertPolicy.Severity
    WARNING: AlertPolicy.Severity
    class Documentation(_message.Message):
        __slots__ = ("content", "mime_type", "subject", "links")
        class Link(_message.Message):
            __slots__ = ("display_name", "url")
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            URL_FIELD_NUMBER: _ClassVar[int]
            display_name: str
            url: str
            def __init__(self, display_name: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        content: str
        mime_type: str
        subject: str
        links: _containers.RepeatedCompositeFieldContainer[AlertPolicy.Documentation.Link]
        def __init__(self, content: _Optional[str] = ..., mime_type: _Optional[str] = ..., subject: _Optional[str] = ..., links: _Optional[_Iterable[_Union[AlertPolicy.Documentation.Link, _Mapping]]] = ...) -> None: ...
    class Condition(_message.Message):
        __slots__ = ("name", "display_name", "condition_threshold", "condition_absent", "condition_matched_log", "condition_monitoring_query_language", "condition_prometheus_query_language", "condition_sql")
        class EvaluationMissingData(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EVALUATION_MISSING_DATA_UNSPECIFIED: _ClassVar[AlertPolicy.Condition.EvaluationMissingData]
            EVALUATION_MISSING_DATA_INACTIVE: _ClassVar[AlertPolicy.Condition.EvaluationMissingData]
            EVALUATION_MISSING_DATA_ACTIVE: _ClassVar[AlertPolicy.Condition.EvaluationMissingData]
            EVALUATION_MISSING_DATA_NO_OP: _ClassVar[AlertPolicy.Condition.EvaluationMissingData]
        EVALUATION_MISSING_DATA_UNSPECIFIED: AlertPolicy.Condition.EvaluationMissingData
        EVALUATION_MISSING_DATA_INACTIVE: AlertPolicy.Condition.EvaluationMissingData
        EVALUATION_MISSING_DATA_ACTIVE: AlertPolicy.Condition.EvaluationMissingData
        EVALUATION_MISSING_DATA_NO_OP: AlertPolicy.Condition.EvaluationMissingData
        class Trigger(_message.Message):
            __slots__ = ("count", "percent")
            COUNT_FIELD_NUMBER: _ClassVar[int]
            PERCENT_FIELD_NUMBER: _ClassVar[int]
            count: int
            percent: float
            def __init__(self, count: _Optional[int] = ..., percent: _Optional[float] = ...) -> None: ...
        class MetricThreshold(_message.Message):
            __slots__ = ("filter", "aggregations", "denominator_filter", "denominator_aggregations", "forecast_options", "comparison", "threshold_value", "duration", "trigger", "evaluation_missing_data")
            class ForecastOptions(_message.Message):
                __slots__ = ("forecast_horizon",)
                FORECAST_HORIZON_FIELD_NUMBER: _ClassVar[int]
                forecast_horizon: _duration_pb2.Duration
                def __init__(self, forecast_horizon: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            FILTER_FIELD_NUMBER: _ClassVar[int]
            AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
            DENOMINATOR_FILTER_FIELD_NUMBER: _ClassVar[int]
            DENOMINATOR_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
            FORECAST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
            COMPARISON_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            EVALUATION_MISSING_DATA_FIELD_NUMBER: _ClassVar[int]
            filter: str
            aggregations: _containers.RepeatedCompositeFieldContainer[_common_pb2.Aggregation]
            denominator_filter: str
            denominator_aggregations: _containers.RepeatedCompositeFieldContainer[_common_pb2.Aggregation]
            forecast_options: AlertPolicy.Condition.MetricThreshold.ForecastOptions
            comparison: _common_pb2.ComparisonType
            threshold_value: float
            duration: _duration_pb2.Duration
            trigger: AlertPolicy.Condition.Trigger
            evaluation_missing_data: AlertPolicy.Condition.EvaluationMissingData
            def __init__(self, filter: _Optional[str] = ..., aggregations: _Optional[_Iterable[_Union[_common_pb2.Aggregation, _Mapping]]] = ..., denominator_filter: _Optional[str] = ..., denominator_aggregations: _Optional[_Iterable[_Union[_common_pb2.Aggregation, _Mapping]]] = ..., forecast_options: _Optional[_Union[AlertPolicy.Condition.MetricThreshold.ForecastOptions, _Mapping]] = ..., comparison: _Optional[_Union[_common_pb2.ComparisonType, str]] = ..., threshold_value: _Optional[float] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., trigger: _Optional[_Union[AlertPolicy.Condition.Trigger, _Mapping]] = ..., evaluation_missing_data: _Optional[_Union[AlertPolicy.Condition.EvaluationMissingData, str]] = ...) -> None: ...
        class MetricAbsence(_message.Message):
            __slots__ = ("filter", "aggregations", "duration", "trigger")
            FILTER_FIELD_NUMBER: _ClassVar[int]
            AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            filter: str
            aggregations: _containers.RepeatedCompositeFieldContainer[_common_pb2.Aggregation]
            duration: _duration_pb2.Duration
            trigger: AlertPolicy.Condition.Trigger
            def __init__(self, filter: _Optional[str] = ..., aggregations: _Optional[_Iterable[_Union[_common_pb2.Aggregation, _Mapping]]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., trigger: _Optional[_Union[AlertPolicy.Condition.Trigger, _Mapping]] = ...) -> None: ...
        class LogMatch(_message.Message):
            __slots__ = ("filter", "label_extractors")
            class LabelExtractorsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            FILTER_FIELD_NUMBER: _ClassVar[int]
            LABEL_EXTRACTORS_FIELD_NUMBER: _ClassVar[int]
            filter: str
            label_extractors: _containers.ScalarMap[str, str]
            def __init__(self, filter: _Optional[str] = ..., label_extractors: _Optional[_Mapping[str, str]] = ...) -> None: ...
        class MonitoringQueryLanguageCondition(_message.Message):
            __slots__ = ("query", "duration", "trigger", "evaluation_missing_data")
            QUERY_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            EVALUATION_MISSING_DATA_FIELD_NUMBER: _ClassVar[int]
            query: str
            duration: _duration_pb2.Duration
            trigger: AlertPolicy.Condition.Trigger
            evaluation_missing_data: AlertPolicy.Condition.EvaluationMissingData
            def __init__(self, query: _Optional[str] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., trigger: _Optional[_Union[AlertPolicy.Condition.Trigger, _Mapping]] = ..., evaluation_missing_data: _Optional[_Union[AlertPolicy.Condition.EvaluationMissingData, str]] = ...) -> None: ...
        class PrometheusQueryLanguageCondition(_message.Message):
            __slots__ = ("query", "duration", "evaluation_interval", "labels", "rule_group", "alert_rule", "disable_metric_validation")
            class LabelsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            QUERY_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            EVALUATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
            LABELS_FIELD_NUMBER: _ClassVar[int]
            RULE_GROUP_FIELD_NUMBER: _ClassVar[int]
            ALERT_RULE_FIELD_NUMBER: _ClassVar[int]
            DISABLE_METRIC_VALIDATION_FIELD_NUMBER: _ClassVar[int]
            query: str
            duration: _duration_pb2.Duration
            evaluation_interval: _duration_pb2.Duration
            labels: _containers.ScalarMap[str, str]
            rule_group: str
            alert_rule: str
            disable_metric_validation: bool
            def __init__(self, query: _Optional[str] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., evaluation_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., rule_group: _Optional[str] = ..., alert_rule: _Optional[str] = ..., disable_metric_validation: bool = ...) -> None: ...
        class SqlCondition(_message.Message):
            __slots__ = ("query", "minutes", "hourly", "daily", "row_count_test", "boolean_test")
            class Minutes(_message.Message):
                __slots__ = ("periodicity",)
                PERIODICITY_FIELD_NUMBER: _ClassVar[int]
                periodicity: int
                def __init__(self, periodicity: _Optional[int] = ...) -> None: ...
            class Hourly(_message.Message):
                __slots__ = ("periodicity", "minute_offset")
                PERIODICITY_FIELD_NUMBER: _ClassVar[int]
                MINUTE_OFFSET_FIELD_NUMBER: _ClassVar[int]
                periodicity: int
                minute_offset: int
                def __init__(self, periodicity: _Optional[int] = ..., minute_offset: _Optional[int] = ...) -> None: ...
            class Daily(_message.Message):
                __slots__ = ("periodicity", "execution_time")
                PERIODICITY_FIELD_NUMBER: _ClassVar[int]
                EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
                periodicity: int
                execution_time: _timeofday_pb2.TimeOfDay
                def __init__(self, periodicity: _Optional[int] = ..., execution_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]] = ...) -> None: ...
            class RowCountTest(_message.Message):
                __slots__ = ("comparison", "threshold")
                COMPARISON_FIELD_NUMBER: _ClassVar[int]
                THRESHOLD_FIELD_NUMBER: _ClassVar[int]
                comparison: _common_pb2.ComparisonType
                threshold: int
                def __init__(self, comparison: _Optional[_Union[_common_pb2.ComparisonType, str]] = ..., threshold: _Optional[int] = ...) -> None: ...
            class BooleanTest(_message.Message):
                __slots__ = ("column",)
                COLUMN_FIELD_NUMBER: _ClassVar[int]
                column: str
                def __init__(self, column: _Optional[str] = ...) -> None: ...
            QUERY_FIELD_NUMBER: _ClassVar[int]
            MINUTES_FIELD_NUMBER: _ClassVar[int]
            HOURLY_FIELD_NUMBER: _ClassVar[int]
            DAILY_FIELD_NUMBER: _ClassVar[int]
            ROW_COUNT_TEST_FIELD_NUMBER: _ClassVar[int]
            BOOLEAN_TEST_FIELD_NUMBER: _ClassVar[int]
            query: str
            minutes: AlertPolicy.Condition.SqlCondition.Minutes
            hourly: AlertPolicy.Condition.SqlCondition.Hourly
            daily: AlertPolicy.Condition.SqlCondition.Daily
            row_count_test: AlertPolicy.Condition.SqlCondition.RowCountTest
            boolean_test: AlertPolicy.Condition.SqlCondition.BooleanTest
            def __init__(self, query: _Optional[str] = ..., minutes: _Optional[_Union[AlertPolicy.Condition.SqlCondition.Minutes, _Mapping]] = ..., hourly: _Optional[_Union[AlertPolicy.Condition.SqlCondition.Hourly, _Mapping]] = ..., daily: _Optional[_Union[AlertPolicy.Condition.SqlCondition.Daily, _Mapping]] = ..., row_count_test: _Optional[_Union[AlertPolicy.Condition.SqlCondition.RowCountTest, _Mapping]] = ..., boolean_test: _Optional[_Union[AlertPolicy.Condition.SqlCondition.BooleanTest, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CONDITION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        CONDITION_ABSENT_FIELD_NUMBER: _ClassVar[int]
        CONDITION_MATCHED_LOG_FIELD_NUMBER: _ClassVar[int]
        CONDITION_MONITORING_QUERY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        CONDITION_PROMETHEUS_QUERY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        CONDITION_SQL_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str
        condition_threshold: AlertPolicy.Condition.MetricThreshold
        condition_absent: AlertPolicy.Condition.MetricAbsence
        condition_matched_log: AlertPolicy.Condition.LogMatch
        condition_monitoring_query_language: AlertPolicy.Condition.MonitoringQueryLanguageCondition
        condition_prometheus_query_language: AlertPolicy.Condition.PrometheusQueryLanguageCondition
        condition_sql: AlertPolicy.Condition.SqlCondition
        def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., condition_threshold: _Optional[_Union[AlertPolicy.Condition.MetricThreshold, _Mapping]] = ..., condition_absent: _Optional[_Union[AlertPolicy.Condition.MetricAbsence, _Mapping]] = ..., condition_matched_log: _Optional[_Union[AlertPolicy.Condition.LogMatch, _Mapping]] = ..., condition_monitoring_query_language: _Optional[_Union[AlertPolicy.Condition.MonitoringQueryLanguageCondition, _Mapping]] = ..., condition_prometheus_query_language: _Optional[_Union[AlertPolicy.Condition.PrometheusQueryLanguageCondition, _Mapping]] = ..., condition_sql: _Optional[_Union[AlertPolicy.Condition.SqlCondition, _Mapping]] = ...) -> None: ...
    class AlertStrategy(_message.Message):
        __slots__ = ("notification_rate_limit", "notification_prompts", "auto_close", "notification_channel_strategy")
        class NotificationPrompt(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NOTIFICATION_PROMPT_UNSPECIFIED: _ClassVar[AlertPolicy.AlertStrategy.NotificationPrompt]
            OPENED: _ClassVar[AlertPolicy.AlertStrategy.NotificationPrompt]
            CLOSED: _ClassVar[AlertPolicy.AlertStrategy.NotificationPrompt]
        NOTIFICATION_PROMPT_UNSPECIFIED: AlertPolicy.AlertStrategy.NotificationPrompt
        OPENED: AlertPolicy.AlertStrategy.NotificationPrompt
        CLOSED: AlertPolicy.AlertStrategy.NotificationPrompt
        class NotificationRateLimit(_message.Message):
            __slots__ = ("period",)
            PERIOD_FIELD_NUMBER: _ClassVar[int]
            period: _duration_pb2.Duration
            def __init__(self, period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class NotificationChannelStrategy(_message.Message):
            __slots__ = ("notification_channel_names", "renotify_interval")
            NOTIFICATION_CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
            RENOTIFY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
            notification_channel_names: _containers.RepeatedScalarFieldContainer[str]
            renotify_interval: _duration_pb2.Duration
            def __init__(self, notification_channel_names: _Optional[_Iterable[str]] = ..., renotify_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        NOTIFICATION_RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_PROMPTS_FIELD_NUMBER: _ClassVar[int]
        AUTO_CLOSE_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_CHANNEL_STRATEGY_FIELD_NUMBER: _ClassVar[int]
        notification_rate_limit: AlertPolicy.AlertStrategy.NotificationRateLimit
        notification_prompts: _containers.RepeatedScalarFieldContainer[AlertPolicy.AlertStrategy.NotificationPrompt]
        auto_close: _duration_pb2.Duration
        notification_channel_strategy: _containers.RepeatedCompositeFieldContainer[AlertPolicy.AlertStrategy.NotificationChannelStrategy]
        def __init__(self, notification_rate_limit: _Optional[_Union[AlertPolicy.AlertStrategy.NotificationRateLimit, _Mapping]] = ..., notification_prompts: _Optional[_Iterable[_Union[AlertPolicy.AlertStrategy.NotificationPrompt, str]]] = ..., auto_close: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., notification_channel_strategy: _Optional[_Iterable[_Union[AlertPolicy.AlertStrategy.NotificationChannelStrategy, _Mapping]]] = ...) -> None: ...
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    COMBINER_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CREATION_RECORD_FIELD_NUMBER: _ClassVar[int]
    MUTATION_RECORD_FIELD_NUMBER: _ClassVar[int]
    ALERT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    documentation: AlertPolicy.Documentation
    user_labels: _containers.ScalarMap[str, str]
    conditions: _containers.RepeatedCompositeFieldContainer[AlertPolicy.Condition]
    combiner: AlertPolicy.ConditionCombinerType
    enabled: _wrappers_pb2.BoolValue
    validity: _status_pb2.Status
    notification_channels: _containers.RepeatedScalarFieldContainer[str]
    creation_record: _mutation_record_pb2.MutationRecord
    mutation_record: _mutation_record_pb2.MutationRecord
    alert_strategy: AlertPolicy.AlertStrategy
    severity: AlertPolicy.Severity
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., documentation: _Optional[_Union[AlertPolicy.Documentation, _Mapping]] = ..., user_labels: _Optional[_Mapping[str, str]] = ..., conditions: _Optional[_Iterable[_Union[AlertPolicy.Condition, _Mapping]]] = ..., combiner: _Optional[_Union[AlertPolicy.ConditionCombinerType, str]] = ..., enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., validity: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., notification_channels: _Optional[_Iterable[str]] = ..., creation_record: _Optional[_Union[_mutation_record_pb2.MutationRecord, _Mapping]] = ..., mutation_record: _Optional[_Union[_mutation_record_pb2.MutationRecord, _Mapping]] = ..., alert_strategy: _Optional[_Union[AlertPolicy.AlertStrategy, _Mapping]] = ..., severity: _Optional[_Union[AlertPolicy.Severity, str]] = ...) -> None: ...
