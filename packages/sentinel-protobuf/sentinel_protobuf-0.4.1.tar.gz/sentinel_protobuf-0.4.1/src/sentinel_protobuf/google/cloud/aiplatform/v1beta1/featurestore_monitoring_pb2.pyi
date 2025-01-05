from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeaturestoreMonitoringConfig(_message.Message):
    __slots__ = ('snapshot_analysis', 'import_features_analysis', 'numerical_threshold_config', 'categorical_threshold_config')

    class SnapshotAnalysis(_message.Message):
        __slots__ = ('disabled', 'monitoring_interval', 'monitoring_interval_days', 'staleness_days')
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        MONITORING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        MONITORING_INTERVAL_DAYS_FIELD_NUMBER: _ClassVar[int]
        STALENESS_DAYS_FIELD_NUMBER: _ClassVar[int]
        disabled: bool
        monitoring_interval: _duration_pb2.Duration
        monitoring_interval_days: int
        staleness_days: int

        def __init__(self, disabled: bool=..., monitoring_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., monitoring_interval_days: _Optional[int]=..., staleness_days: _Optional[int]=...) -> None:
            ...

    class ImportFeaturesAnalysis(_message.Message):
        __slots__ = ('state', 'anomaly_detection_baseline')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State]
            DEFAULT: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State]
            ENABLED: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State]
            DISABLED: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State]
        STATE_UNSPECIFIED: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State
        DEFAULT: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State
        ENABLED: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State
        DISABLED: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State

        class Baseline(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BASELINE_UNSPECIFIED: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline]
            LATEST_STATS: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline]
            MOST_RECENT_SNAPSHOT_STATS: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline]
            PREVIOUS_IMPORT_FEATURES_STATS: _ClassVar[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline]
        BASELINE_UNSPECIFIED: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline
        LATEST_STATS: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline
        MOST_RECENT_SNAPSHOT_STATS: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline
        PREVIOUS_IMPORT_FEATURES_STATS: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline
        STATE_FIELD_NUMBER: _ClassVar[int]
        ANOMALY_DETECTION_BASELINE_FIELD_NUMBER: _ClassVar[int]
        state: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State
        anomaly_detection_baseline: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline

        def __init__(self, state: _Optional[_Union[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State, str]]=..., anomaly_detection_baseline: _Optional[_Union[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline, str]]=...) -> None:
            ...

    class ThresholdConfig(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float

        def __init__(self, value: _Optional[float]=...) -> None:
            ...
    SNAPSHOT_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FEATURES_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    NUMERICAL_THRESHOLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CATEGORICAL_THRESHOLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    snapshot_analysis: FeaturestoreMonitoringConfig.SnapshotAnalysis
    import_features_analysis: FeaturestoreMonitoringConfig.ImportFeaturesAnalysis
    numerical_threshold_config: FeaturestoreMonitoringConfig.ThresholdConfig
    categorical_threshold_config: FeaturestoreMonitoringConfig.ThresholdConfig

    def __init__(self, snapshot_analysis: _Optional[_Union[FeaturestoreMonitoringConfig.SnapshotAnalysis, _Mapping]]=..., import_features_analysis: _Optional[_Union[FeaturestoreMonitoringConfig.ImportFeaturesAnalysis, _Mapping]]=..., numerical_threshold_config: _Optional[_Union[FeaturestoreMonitoringConfig.ThresholdConfig, _Mapping]]=..., categorical_threshold_config: _Optional[_Union[FeaturestoreMonitoringConfig.ThresholdConfig, _Mapping]]=...) -> None:
        ...