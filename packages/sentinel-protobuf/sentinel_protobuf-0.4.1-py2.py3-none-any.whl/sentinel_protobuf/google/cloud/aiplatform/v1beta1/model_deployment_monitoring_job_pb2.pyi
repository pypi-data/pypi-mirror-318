from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import feature_monitoring_stats_pb2 as _feature_monitoring_stats_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import job_state_pb2 as _job_state_pb2
from google.cloud.aiplatform.v1beta1 import model_monitoring_pb2 as _model_monitoring_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ModelDeploymentMonitoringObjectiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED: _ClassVar[ModelDeploymentMonitoringObjectiveType]
    RAW_FEATURE_SKEW: _ClassVar[ModelDeploymentMonitoringObjectiveType]
    RAW_FEATURE_DRIFT: _ClassVar[ModelDeploymentMonitoringObjectiveType]
    FEATURE_ATTRIBUTION_SKEW: _ClassVar[ModelDeploymentMonitoringObjectiveType]
    FEATURE_ATTRIBUTION_DRIFT: _ClassVar[ModelDeploymentMonitoringObjectiveType]
MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED: ModelDeploymentMonitoringObjectiveType
RAW_FEATURE_SKEW: ModelDeploymentMonitoringObjectiveType
RAW_FEATURE_DRIFT: ModelDeploymentMonitoringObjectiveType
FEATURE_ATTRIBUTION_SKEW: ModelDeploymentMonitoringObjectiveType
FEATURE_ATTRIBUTION_DRIFT: ModelDeploymentMonitoringObjectiveType

class ModelDeploymentMonitoringJob(_message.Message):
    __slots__ = ('name', 'display_name', 'endpoint', 'state', 'schedule_state', 'latest_monitoring_pipeline_metadata', 'model_deployment_monitoring_objective_configs', 'model_deployment_monitoring_schedule_config', 'logging_sampling_strategy', 'model_monitoring_alert_config', 'predict_instance_schema_uri', 'sample_predict_instance', 'analysis_instance_schema_uri', 'bigquery_tables', 'log_ttl', 'labels', 'create_time', 'update_time', 'next_schedule_time', 'stats_anomalies_base_directory', 'encryption_spec', 'enable_monitoring_pipeline_logs', 'error', 'satisfies_pzs', 'satisfies_pzi')

    class MonitoringScheduleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MONITORING_SCHEDULE_STATE_UNSPECIFIED: _ClassVar[ModelDeploymentMonitoringJob.MonitoringScheduleState]
        PENDING: _ClassVar[ModelDeploymentMonitoringJob.MonitoringScheduleState]
        OFFLINE: _ClassVar[ModelDeploymentMonitoringJob.MonitoringScheduleState]
        RUNNING: _ClassVar[ModelDeploymentMonitoringJob.MonitoringScheduleState]
    MONITORING_SCHEDULE_STATE_UNSPECIFIED: ModelDeploymentMonitoringJob.MonitoringScheduleState
    PENDING: ModelDeploymentMonitoringJob.MonitoringScheduleState
    OFFLINE: ModelDeploymentMonitoringJob.MonitoringScheduleState
    RUNNING: ModelDeploymentMonitoringJob.MonitoringScheduleState

    class LatestMonitoringPipelineMetadata(_message.Message):
        __slots__ = ('run_time', 'status')
        RUN_TIME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        run_time: _timestamp_pb2.Timestamp
        status: _status_pb2.Status

        def __init__(self, run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_STATE_FIELD_NUMBER: _ClassVar[int]
    LATEST_MONITORING_PIPELINE_METADATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    MODEL_DEPLOYMENT_MONITORING_SCHEDULE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOGGING_SAMPLING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_ALERT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PREDICT_INSTANCE_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_PREDICT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_INSTANCE_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_TABLES_FIELD_NUMBER: _ClassVar[int]
    LOG_TTL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATS_ANOMALIES_BASE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MONITORING_PIPELINE_LOGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    endpoint: str
    state: _job_state_pb2.JobState
    schedule_state: ModelDeploymentMonitoringJob.MonitoringScheduleState
    latest_monitoring_pipeline_metadata: ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata
    model_deployment_monitoring_objective_configs: _containers.RepeatedCompositeFieldContainer[ModelDeploymentMonitoringObjectiveConfig]
    model_deployment_monitoring_schedule_config: ModelDeploymentMonitoringScheduleConfig
    logging_sampling_strategy: _model_monitoring_pb2.SamplingStrategy
    model_monitoring_alert_config: _model_monitoring_pb2.ModelMonitoringAlertConfig
    predict_instance_schema_uri: str
    sample_predict_instance: _struct_pb2.Value
    analysis_instance_schema_uri: str
    bigquery_tables: _containers.RepeatedCompositeFieldContainer[ModelDeploymentMonitoringBigQueryTable]
    log_ttl: _duration_pb2.Duration
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    next_schedule_time: _timestamp_pb2.Timestamp
    stats_anomalies_base_directory: _io_pb2.GcsDestination
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    enable_monitoring_pipeline_logs: bool
    error: _status_pb2.Status
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., endpoint: _Optional[str]=..., state: _Optional[_Union[_job_state_pb2.JobState, str]]=..., schedule_state: _Optional[_Union[ModelDeploymentMonitoringJob.MonitoringScheduleState, str]]=..., latest_monitoring_pipeline_metadata: _Optional[_Union[ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadata, _Mapping]]=..., model_deployment_monitoring_objective_configs: _Optional[_Iterable[_Union[ModelDeploymentMonitoringObjectiveConfig, _Mapping]]]=..., model_deployment_monitoring_schedule_config: _Optional[_Union[ModelDeploymentMonitoringScheduleConfig, _Mapping]]=..., logging_sampling_strategy: _Optional[_Union[_model_monitoring_pb2.SamplingStrategy, _Mapping]]=..., model_monitoring_alert_config: _Optional[_Union[_model_monitoring_pb2.ModelMonitoringAlertConfig, _Mapping]]=..., predict_instance_schema_uri: _Optional[str]=..., sample_predict_instance: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., analysis_instance_schema_uri: _Optional[str]=..., bigquery_tables: _Optional[_Iterable[_Union[ModelDeploymentMonitoringBigQueryTable, _Mapping]]]=..., log_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., stats_anomalies_base_directory: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., enable_monitoring_pipeline_logs: bool=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...

class ModelDeploymentMonitoringBigQueryTable(_message.Message):
    __slots__ = ('log_source', 'log_type', 'bigquery_table_path', 'request_response_logging_schema_version')

    class LogSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOG_SOURCE_UNSPECIFIED: _ClassVar[ModelDeploymentMonitoringBigQueryTable.LogSource]
        TRAINING: _ClassVar[ModelDeploymentMonitoringBigQueryTable.LogSource]
        SERVING: _ClassVar[ModelDeploymentMonitoringBigQueryTable.LogSource]
    LOG_SOURCE_UNSPECIFIED: ModelDeploymentMonitoringBigQueryTable.LogSource
    TRAINING: ModelDeploymentMonitoringBigQueryTable.LogSource
    SERVING: ModelDeploymentMonitoringBigQueryTable.LogSource

    class LogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOG_TYPE_UNSPECIFIED: _ClassVar[ModelDeploymentMonitoringBigQueryTable.LogType]
        PREDICT: _ClassVar[ModelDeploymentMonitoringBigQueryTable.LogType]
        EXPLAIN: _ClassVar[ModelDeploymentMonitoringBigQueryTable.LogType]
    LOG_TYPE_UNSPECIFIED: ModelDeploymentMonitoringBigQueryTable.LogType
    PREDICT: ModelDeploymentMonitoringBigQueryTable.LogType
    EXPLAIN: ModelDeploymentMonitoringBigQueryTable.LogType
    LOG_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_TABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_RESPONSE_LOGGING_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    log_source: ModelDeploymentMonitoringBigQueryTable.LogSource
    log_type: ModelDeploymentMonitoringBigQueryTable.LogType
    bigquery_table_path: str
    request_response_logging_schema_version: str

    def __init__(self, log_source: _Optional[_Union[ModelDeploymentMonitoringBigQueryTable.LogSource, str]]=..., log_type: _Optional[_Union[ModelDeploymentMonitoringBigQueryTable.LogType, str]]=..., bigquery_table_path: _Optional[str]=..., request_response_logging_schema_version: _Optional[str]=...) -> None:
        ...

class ModelDeploymentMonitoringObjectiveConfig(_message.Message):
    __slots__ = ('deployed_model_id', 'objective_config')
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    deployed_model_id: str
    objective_config: _model_monitoring_pb2.ModelMonitoringObjectiveConfig

    def __init__(self, deployed_model_id: _Optional[str]=..., objective_config: _Optional[_Union[_model_monitoring_pb2.ModelMonitoringObjectiveConfig, _Mapping]]=...) -> None:
        ...

class ModelDeploymentMonitoringScheduleConfig(_message.Message):
    __slots__ = ('monitor_interval', 'monitor_window')
    MONITOR_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MONITOR_WINDOW_FIELD_NUMBER: _ClassVar[int]
    monitor_interval: _duration_pb2.Duration
    monitor_window: _duration_pb2.Duration

    def __init__(self, monitor_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., monitor_window: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ModelMonitoringStatsAnomalies(_message.Message):
    __slots__ = ('objective', 'deployed_model_id', 'anomaly_count', 'feature_stats')

    class FeatureHistoricStatsAnomalies(_message.Message):
        __slots__ = ('feature_display_name', 'threshold', 'training_stats', 'prediction_stats')
        FEATURE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        TRAINING_STATS_FIELD_NUMBER: _ClassVar[int]
        PREDICTION_STATS_FIELD_NUMBER: _ClassVar[int]
        feature_display_name: str
        threshold: _model_monitoring_pb2.ThresholdConfig
        training_stats: _feature_monitoring_stats_pb2.FeatureStatsAnomaly
        prediction_stats: _containers.RepeatedCompositeFieldContainer[_feature_monitoring_stats_pb2.FeatureStatsAnomaly]

        def __init__(self, feature_display_name: _Optional[str]=..., threshold: _Optional[_Union[_model_monitoring_pb2.ThresholdConfig, _Mapping]]=..., training_stats: _Optional[_Union[_feature_monitoring_stats_pb2.FeatureStatsAnomaly, _Mapping]]=..., prediction_stats: _Optional[_Iterable[_Union[_feature_monitoring_stats_pb2.FeatureStatsAnomaly, _Mapping]]]=...) -> None:
            ...
    OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ANOMALY_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_STATS_FIELD_NUMBER: _ClassVar[int]
    objective: ModelDeploymentMonitoringObjectiveType
    deployed_model_id: str
    anomaly_count: int
    feature_stats: _containers.RepeatedCompositeFieldContainer[ModelMonitoringStatsAnomalies.FeatureHistoricStatsAnomalies]

    def __init__(self, objective: _Optional[_Union[ModelDeploymentMonitoringObjectiveType, str]]=..., deployed_model_id: _Optional[str]=..., anomaly_count: _Optional[int]=..., feature_stats: _Optional[_Iterable[_Union[ModelMonitoringStatsAnomalies.FeatureHistoricStatsAnomalies, _Mapping]]]=...) -> None:
        ...