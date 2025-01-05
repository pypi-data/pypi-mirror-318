from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import explanation_pb2 as _explanation_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1beta1 import model_monitoring_alert_pb2 as _model_monitoring_alert_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelMonitoringSpec(_message.Message):
    __slots__ = ("objective_spec", "notification_spec", "output_spec")
    OBJECTIVE_SPEC_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SPEC_FIELD_NUMBER: _ClassVar[int]
    objective_spec: ModelMonitoringObjectiveSpec
    notification_spec: ModelMonitoringNotificationSpec
    output_spec: ModelMonitoringOutputSpec
    def __init__(self, objective_spec: _Optional[_Union[ModelMonitoringObjectiveSpec, _Mapping]] = ..., notification_spec: _Optional[_Union[ModelMonitoringNotificationSpec, _Mapping]] = ..., output_spec: _Optional[_Union[ModelMonitoringOutputSpec, _Mapping]] = ...) -> None: ...

class ModelMonitoringObjectiveSpec(_message.Message):
    __slots__ = ("tabular_objective", "explanation_spec", "baseline_dataset", "target_dataset")
    class DataDriftSpec(_message.Message):
        __slots__ = ("features", "categorical_metric_type", "numeric_metric_type", "default_categorical_alert_condition", "default_numeric_alert_condition", "feature_alert_conditions")
        class FeatureAlertConditionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _model_monitoring_alert_pb2.ModelMonitoringAlertCondition
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_monitoring_alert_pb2.ModelMonitoringAlertCondition, _Mapping]] = ...) -> None: ...
        FEATURES_FIELD_NUMBER: _ClassVar[int]
        CATEGORICAL_METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
        NUMERIC_METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_CATEGORICAL_ALERT_CONDITION_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_NUMERIC_ALERT_CONDITION_FIELD_NUMBER: _ClassVar[int]
        FEATURE_ALERT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        features: _containers.RepeatedScalarFieldContainer[str]
        categorical_metric_type: str
        numeric_metric_type: str
        default_categorical_alert_condition: _model_monitoring_alert_pb2.ModelMonitoringAlertCondition
        default_numeric_alert_condition: _model_monitoring_alert_pb2.ModelMonitoringAlertCondition
        feature_alert_conditions: _containers.MessageMap[str, _model_monitoring_alert_pb2.ModelMonitoringAlertCondition]
        def __init__(self, features: _Optional[_Iterable[str]] = ..., categorical_metric_type: _Optional[str] = ..., numeric_metric_type: _Optional[str] = ..., default_categorical_alert_condition: _Optional[_Union[_model_monitoring_alert_pb2.ModelMonitoringAlertCondition, _Mapping]] = ..., default_numeric_alert_condition: _Optional[_Union[_model_monitoring_alert_pb2.ModelMonitoringAlertCondition, _Mapping]] = ..., feature_alert_conditions: _Optional[_Mapping[str, _model_monitoring_alert_pb2.ModelMonitoringAlertCondition]] = ...) -> None: ...
    class FeatureAttributionSpec(_message.Message):
        __slots__ = ("features", "default_alert_condition", "feature_alert_conditions", "batch_explanation_dedicated_resources")
        class FeatureAlertConditionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _model_monitoring_alert_pb2.ModelMonitoringAlertCondition
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_monitoring_alert_pb2.ModelMonitoringAlertCondition, _Mapping]] = ...) -> None: ...
        FEATURES_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_ALERT_CONDITION_FIELD_NUMBER: _ClassVar[int]
        FEATURE_ALERT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        BATCH_EXPLANATION_DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        features: _containers.RepeatedScalarFieldContainer[str]
        default_alert_condition: _model_monitoring_alert_pb2.ModelMonitoringAlertCondition
        feature_alert_conditions: _containers.MessageMap[str, _model_monitoring_alert_pb2.ModelMonitoringAlertCondition]
        batch_explanation_dedicated_resources: _machine_resources_pb2.BatchDedicatedResources
        def __init__(self, features: _Optional[_Iterable[str]] = ..., default_alert_condition: _Optional[_Union[_model_monitoring_alert_pb2.ModelMonitoringAlertCondition, _Mapping]] = ..., feature_alert_conditions: _Optional[_Mapping[str, _model_monitoring_alert_pb2.ModelMonitoringAlertCondition]] = ..., batch_explanation_dedicated_resources: _Optional[_Union[_machine_resources_pb2.BatchDedicatedResources, _Mapping]] = ...) -> None: ...
    class TabularObjective(_message.Message):
        __slots__ = ("feature_drift_spec", "prediction_output_drift_spec", "feature_attribution_spec")
        FEATURE_DRIFT_SPEC_FIELD_NUMBER: _ClassVar[int]
        PREDICTION_OUTPUT_DRIFT_SPEC_FIELD_NUMBER: _ClassVar[int]
        FEATURE_ATTRIBUTION_SPEC_FIELD_NUMBER: _ClassVar[int]
        feature_drift_spec: ModelMonitoringObjectiveSpec.DataDriftSpec
        prediction_output_drift_spec: ModelMonitoringObjectiveSpec.DataDriftSpec
        feature_attribution_spec: ModelMonitoringObjectiveSpec.FeatureAttributionSpec
        def __init__(self, feature_drift_spec: _Optional[_Union[ModelMonitoringObjectiveSpec.DataDriftSpec, _Mapping]] = ..., prediction_output_drift_spec: _Optional[_Union[ModelMonitoringObjectiveSpec.DataDriftSpec, _Mapping]] = ..., feature_attribution_spec: _Optional[_Union[ModelMonitoringObjectiveSpec.FeatureAttributionSpec, _Mapping]] = ...) -> None: ...
    TABULAR_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    BASELINE_DATASET_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATASET_FIELD_NUMBER: _ClassVar[int]
    tabular_objective: ModelMonitoringObjectiveSpec.TabularObjective
    explanation_spec: _explanation_pb2.ExplanationSpec
    baseline_dataset: ModelMonitoringInput
    target_dataset: ModelMonitoringInput
    def __init__(self, tabular_objective: _Optional[_Union[ModelMonitoringObjectiveSpec.TabularObjective, _Mapping]] = ..., explanation_spec: _Optional[_Union[_explanation_pb2.ExplanationSpec, _Mapping]] = ..., baseline_dataset: _Optional[_Union[ModelMonitoringInput, _Mapping]] = ..., target_dataset: _Optional[_Union[ModelMonitoringInput, _Mapping]] = ...) -> None: ...

class ModelMonitoringOutputSpec(_message.Message):
    __slots__ = ("gcs_base_directory",)
    GCS_BASE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    gcs_base_directory: _io_pb2.GcsDestination
    def __init__(self, gcs_base_directory: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]] = ...) -> None: ...

class ModelMonitoringInput(_message.Message):
    __slots__ = ("columnized_dataset", "batch_prediction_output", "vertex_endpoint_logs", "time_interval", "time_offset")
    class ModelMonitoringDataset(_message.Message):
        __slots__ = ("vertex_dataset", "gcs_source", "bigquery_source", "timestamp_field")
        class ModelMonitoringGcsSource(_message.Message):
            __slots__ = ("gcs_uri", "format")
            class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                DATA_FORMAT_UNSPECIFIED: _ClassVar[ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat]
                CSV: _ClassVar[ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat]
                TF_RECORD: _ClassVar[ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat]
                JSONL: _ClassVar[ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat]
            DATA_FORMAT_UNSPECIFIED: ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat
            CSV: ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat
            TF_RECORD: ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat
            JSONL: ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat
            GCS_URI_FIELD_NUMBER: _ClassVar[int]
            FORMAT_FIELD_NUMBER: _ClassVar[int]
            gcs_uri: str
            format: ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat
            def __init__(self, gcs_uri: _Optional[str] = ..., format: _Optional[_Union[ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat, str]] = ...) -> None: ...
        class ModelMonitoringBigQuerySource(_message.Message):
            __slots__ = ("table_uri", "query")
            TABLE_URI_FIELD_NUMBER: _ClassVar[int]
            QUERY_FIELD_NUMBER: _ClassVar[int]
            table_uri: str
            query: str
            def __init__(self, table_uri: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...
        VERTEX_DATASET_FIELD_NUMBER: _ClassVar[int]
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_FIELD_NUMBER: _ClassVar[int]
        vertex_dataset: str
        gcs_source: ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource
        bigquery_source: ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringBigQuerySource
        timestamp_field: str
        def __init__(self, vertex_dataset: _Optional[str] = ..., gcs_source: _Optional[_Union[ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource, _Mapping]] = ..., bigquery_source: _Optional[_Union[ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringBigQuerySource, _Mapping]] = ..., timestamp_field: _Optional[str] = ...) -> None: ...
    class BatchPredictionOutput(_message.Message):
        __slots__ = ("batch_prediction_job",)
        BATCH_PREDICTION_JOB_FIELD_NUMBER: _ClassVar[int]
        batch_prediction_job: str
        def __init__(self, batch_prediction_job: _Optional[str] = ...) -> None: ...
    class VertexEndpointLogs(_message.Message):
        __slots__ = ("endpoints",)
        ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        endpoints: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, endpoints: _Optional[_Iterable[str]] = ...) -> None: ...
    class TimeOffset(_message.Message):
        __slots__ = ("offset", "window")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        WINDOW_FIELD_NUMBER: _ClassVar[int]
        offset: str
        window: str
        def __init__(self, offset: _Optional[str] = ..., window: _Optional[str] = ...) -> None: ...
    COLUMNIZED_DATASET_FIELD_NUMBER: _ClassVar[int]
    BATCH_PREDICTION_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_ENDPOINT_LOGS_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    columnized_dataset: ModelMonitoringInput.ModelMonitoringDataset
    batch_prediction_output: ModelMonitoringInput.BatchPredictionOutput
    vertex_endpoint_logs: ModelMonitoringInput.VertexEndpointLogs
    time_interval: _interval_pb2.Interval
    time_offset: ModelMonitoringInput.TimeOffset
    def __init__(self, columnized_dataset: _Optional[_Union[ModelMonitoringInput.ModelMonitoringDataset, _Mapping]] = ..., batch_prediction_output: _Optional[_Union[ModelMonitoringInput.BatchPredictionOutput, _Mapping]] = ..., vertex_endpoint_logs: _Optional[_Union[ModelMonitoringInput.VertexEndpointLogs, _Mapping]] = ..., time_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., time_offset: _Optional[_Union[ModelMonitoringInput.TimeOffset, _Mapping]] = ...) -> None: ...

class ModelMonitoringNotificationSpec(_message.Message):
    __slots__ = ("email_config", "enable_cloud_logging", "notification_channel_configs")
    class EmailConfig(_message.Message):
        __slots__ = ("user_emails",)
        USER_EMAILS_FIELD_NUMBER: _ClassVar[int]
        user_emails: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, user_emails: _Optional[_Iterable[str]] = ...) -> None: ...
    class NotificationChannelConfig(_message.Message):
        __slots__ = ("notification_channel",)
        NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        notification_channel: str
        def __init__(self, notification_channel: _Optional[str] = ...) -> None: ...
    EMAIL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CLOUD_LOGGING_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNEL_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    email_config: ModelMonitoringNotificationSpec.EmailConfig
    enable_cloud_logging: bool
    notification_channel_configs: _containers.RepeatedCompositeFieldContainer[ModelMonitoringNotificationSpec.NotificationChannelConfig]
    def __init__(self, email_config: _Optional[_Union[ModelMonitoringNotificationSpec.EmailConfig, _Mapping]] = ..., enable_cloud_logging: bool = ..., notification_channel_configs: _Optional[_Iterable[_Union[ModelMonitoringNotificationSpec.NotificationChannelConfig, _Mapping]]] = ...) -> None: ...
