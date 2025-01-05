from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import io_pb2 as _io_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ModelMonitoringObjectiveConfig(_message.Message):
    __slots__ = ('training_dataset', 'training_prediction_skew_detection_config', 'prediction_drift_detection_config', 'explanation_config')

    class TrainingDataset(_message.Message):
        __slots__ = ('dataset', 'gcs_source', 'bigquery_source', 'data_format', 'target_field', 'logging_sampling_strategy')
        DATASET_FIELD_NUMBER: _ClassVar[int]
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
        TARGET_FIELD_FIELD_NUMBER: _ClassVar[int]
        LOGGING_SAMPLING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        gcs_source: _io_pb2.GcsSource
        bigquery_source: _io_pb2.BigQuerySource
        data_format: str
        target_field: str
        logging_sampling_strategy: SamplingStrategy

        def __init__(self, dataset: _Optional[str]=..., gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]]=..., bigquery_source: _Optional[_Union[_io_pb2.BigQuerySource, _Mapping]]=..., data_format: _Optional[str]=..., target_field: _Optional[str]=..., logging_sampling_strategy: _Optional[_Union[SamplingStrategy, _Mapping]]=...) -> None:
            ...

    class TrainingPredictionSkewDetectionConfig(_message.Message):
        __slots__ = ('skew_thresholds', 'attribution_score_skew_thresholds', 'default_skew_threshold')

        class SkewThresholdsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ThresholdConfig

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ThresholdConfig, _Mapping]]=...) -> None:
                ...

        class AttributionScoreSkewThresholdsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ThresholdConfig

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ThresholdConfig, _Mapping]]=...) -> None:
                ...
        SKEW_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTION_SCORE_SKEW_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_SKEW_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        skew_thresholds: _containers.MessageMap[str, ThresholdConfig]
        attribution_score_skew_thresholds: _containers.MessageMap[str, ThresholdConfig]
        default_skew_threshold: ThresholdConfig

        def __init__(self, skew_thresholds: _Optional[_Mapping[str, ThresholdConfig]]=..., attribution_score_skew_thresholds: _Optional[_Mapping[str, ThresholdConfig]]=..., default_skew_threshold: _Optional[_Union[ThresholdConfig, _Mapping]]=...) -> None:
            ...

    class PredictionDriftDetectionConfig(_message.Message):
        __slots__ = ('drift_thresholds', 'attribution_score_drift_thresholds', 'default_drift_threshold')

        class DriftThresholdsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ThresholdConfig

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ThresholdConfig, _Mapping]]=...) -> None:
                ...

        class AttributionScoreDriftThresholdsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ThresholdConfig

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ThresholdConfig, _Mapping]]=...) -> None:
                ...
        DRIFT_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTION_SCORE_DRIFT_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_DRIFT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        drift_thresholds: _containers.MessageMap[str, ThresholdConfig]
        attribution_score_drift_thresholds: _containers.MessageMap[str, ThresholdConfig]
        default_drift_threshold: ThresholdConfig

        def __init__(self, drift_thresholds: _Optional[_Mapping[str, ThresholdConfig]]=..., attribution_score_drift_thresholds: _Optional[_Mapping[str, ThresholdConfig]]=..., default_drift_threshold: _Optional[_Union[ThresholdConfig, _Mapping]]=...) -> None:
            ...

    class ExplanationConfig(_message.Message):
        __slots__ = ('enable_feature_attributes', 'explanation_baseline')

        class ExplanationBaseline(_message.Message):
            __slots__ = ('gcs', 'bigquery', 'prediction_format')

            class PredictionFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PREDICTION_FORMAT_UNSPECIFIED: _ClassVar[ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat]
                JSONL: _ClassVar[ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat]
                BIGQUERY: _ClassVar[ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat]
            PREDICTION_FORMAT_UNSPECIFIED: ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat
            JSONL: ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat
            BIGQUERY: ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat
            GCS_FIELD_NUMBER: _ClassVar[int]
            BIGQUERY_FIELD_NUMBER: _ClassVar[int]
            PREDICTION_FORMAT_FIELD_NUMBER: _ClassVar[int]
            gcs: _io_pb2.GcsDestination
            bigquery: _io_pb2.BigQueryDestination
            prediction_format: ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat

            def __init__(self, gcs: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=..., bigquery: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]]=..., prediction_format: _Optional[_Union[ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat, str]]=...) -> None:
                ...
        ENABLE_FEATURE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        EXPLANATION_BASELINE_FIELD_NUMBER: _ClassVar[int]
        enable_feature_attributes: bool
        explanation_baseline: ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline

        def __init__(self, enable_feature_attributes: bool=..., explanation_baseline: _Optional[_Union[ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline, _Mapping]]=...) -> None:
            ...
    TRAINING_DATASET_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PREDICTION_SKEW_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_DRIFT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    training_dataset: ModelMonitoringObjectiveConfig.TrainingDataset
    training_prediction_skew_detection_config: ModelMonitoringObjectiveConfig.TrainingPredictionSkewDetectionConfig
    prediction_drift_detection_config: ModelMonitoringObjectiveConfig.PredictionDriftDetectionConfig
    explanation_config: ModelMonitoringObjectiveConfig.ExplanationConfig

    def __init__(self, training_dataset: _Optional[_Union[ModelMonitoringObjectiveConfig.TrainingDataset, _Mapping]]=..., training_prediction_skew_detection_config: _Optional[_Union[ModelMonitoringObjectiveConfig.TrainingPredictionSkewDetectionConfig, _Mapping]]=..., prediction_drift_detection_config: _Optional[_Union[ModelMonitoringObjectiveConfig.PredictionDriftDetectionConfig, _Mapping]]=..., explanation_config: _Optional[_Union[ModelMonitoringObjectiveConfig.ExplanationConfig, _Mapping]]=...) -> None:
        ...

class ModelMonitoringAlertConfig(_message.Message):
    __slots__ = ('email_alert_config', 'enable_logging', 'notification_channels')

    class EmailAlertConfig(_message.Message):
        __slots__ = ('user_emails',)
        USER_EMAILS_FIELD_NUMBER: _ClassVar[int]
        user_emails: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, user_emails: _Optional[_Iterable[str]]=...) -> None:
            ...
    EMAIL_ALERT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LOGGING_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    email_alert_config: ModelMonitoringAlertConfig.EmailAlertConfig
    enable_logging: bool
    notification_channels: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email_alert_config: _Optional[_Union[ModelMonitoringAlertConfig.EmailAlertConfig, _Mapping]]=..., enable_logging: bool=..., notification_channels: _Optional[_Iterable[str]]=...) -> None:
        ...

class ThresholdConfig(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float

    def __init__(self, value: _Optional[float]=...) -> None:
        ...

class SamplingStrategy(_message.Message):
    __slots__ = ('random_sample_config',)

    class RandomSampleConfig(_message.Message):
        __slots__ = ('sample_rate',)
        SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
        sample_rate: float

        def __init__(self, sample_rate: _Optional[float]=...) -> None:
            ...
    RANDOM_SAMPLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    random_sample_config: SamplingStrategy.RandomSampleConfig

    def __init__(self, random_sample_config: _Optional[_Union[SamplingStrategy.RandomSampleConfig, _Mapping]]=...) -> None:
        ...