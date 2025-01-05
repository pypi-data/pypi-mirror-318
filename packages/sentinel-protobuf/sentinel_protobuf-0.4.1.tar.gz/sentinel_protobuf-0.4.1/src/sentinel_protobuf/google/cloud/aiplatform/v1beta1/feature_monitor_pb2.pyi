from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureMonitor(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "etag", "labels", "description", "schedule_config", "feature_selection_config")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SELECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]
    description: str
    schedule_config: ScheduleConfig
    feature_selection_config: FeatureSelectionConfig
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., schedule_config: _Optional[_Union[ScheduleConfig, _Mapping]] = ..., feature_selection_config: _Optional[_Union[FeatureSelectionConfig, _Mapping]] = ...) -> None: ...

class ScheduleConfig(_message.Message):
    __slots__ = ("cron",)
    CRON_FIELD_NUMBER: _ClassVar[int]
    cron: str
    def __init__(self, cron: _Optional[str] = ...) -> None: ...

class FeatureSelectionConfig(_message.Message):
    __slots__ = ("feature_configs",)
    class FeatureConfig(_message.Message):
        __slots__ = ("feature_id", "drift_threshold")
        FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
        DRIFT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        feature_id: str
        drift_threshold: float
        def __init__(self, feature_id: _Optional[str] = ..., drift_threshold: _Optional[float] = ...) -> None: ...
    FEATURE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    feature_configs: _containers.RepeatedCompositeFieldContainer[FeatureSelectionConfig.FeatureConfig]
    def __init__(self, feature_configs: _Optional[_Iterable[_Union[FeatureSelectionConfig.FeatureConfig, _Mapping]]] = ...) -> None: ...

class FeatureStatsAndAnomaly(_message.Message):
    __slots__ = ("feature_id", "feature_stats", "distribution_deviation", "drift_detection_threshold", "drift_detected", "stats_time", "feature_monitor_job_id", "feature_monitor_id")
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_STATS_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    DRIFT_DETECTION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DRIFT_DETECTED_FIELD_NUMBER: _ClassVar[int]
    STATS_TIME_FIELD_NUMBER: _ClassVar[int]
    FEATURE_MONITOR_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_MONITOR_ID_FIELD_NUMBER: _ClassVar[int]
    feature_id: str
    feature_stats: _struct_pb2.Value
    distribution_deviation: float
    drift_detection_threshold: float
    drift_detected: bool
    stats_time: _timestamp_pb2.Timestamp
    feature_monitor_job_id: int
    feature_monitor_id: str
    def __init__(self, feature_id: _Optional[str] = ..., feature_stats: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., distribution_deviation: _Optional[float] = ..., drift_detection_threshold: _Optional[float] = ..., drift_detected: bool = ..., stats_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., feature_monitor_job_id: _Optional[int] = ..., feature_monitor_id: _Optional[str] = ...) -> None: ...

class FeatureStatsAndAnomalySpec(_message.Message):
    __slots__ = ("latest_stats_count", "stats_time_range")
    LATEST_STATS_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATS_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    latest_stats_count: int
    stats_time_range: _interval_pb2.Interval
    def __init__(self, latest_stats_count: _Optional[int] = ..., stats_time_range: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ...) -> None: ...
