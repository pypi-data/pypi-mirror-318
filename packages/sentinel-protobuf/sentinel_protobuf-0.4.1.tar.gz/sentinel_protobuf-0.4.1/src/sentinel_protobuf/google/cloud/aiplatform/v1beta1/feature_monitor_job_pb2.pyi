from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import feature_monitor_pb2 as _feature_monitor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureMonitorJob(_message.Message):
    __slots__ = ("name", "create_time", "final_status", "job_summary", "labels", "description", "drift_base_feature_monitor_job_id", "drift_base_snapshot_time", "feature_selection_config", "trigger_type")
    class FeatureMonitorJobTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_MONITOR_JOB_TRIGGER_UNSPECIFIED: _ClassVar[FeatureMonitorJob.FeatureMonitorJobTrigger]
        FEATURE_MONITOR_JOB_TRIGGER_PERIODIC: _ClassVar[FeatureMonitorJob.FeatureMonitorJobTrigger]
        FEATURE_MONITOR_JOB_TRIGGER_ON_DEMAND: _ClassVar[FeatureMonitorJob.FeatureMonitorJobTrigger]
    FEATURE_MONITOR_JOB_TRIGGER_UNSPECIFIED: FeatureMonitorJob.FeatureMonitorJobTrigger
    FEATURE_MONITOR_JOB_TRIGGER_PERIODIC: FeatureMonitorJob.FeatureMonitorJobTrigger
    FEATURE_MONITOR_JOB_TRIGGER_ON_DEMAND: FeatureMonitorJob.FeatureMonitorJobTrigger
    class JobSummary(_message.Message):
        __slots__ = ("total_slot_ms", "feature_stats_and_anomalies")
        TOTAL_SLOT_MS_FIELD_NUMBER: _ClassVar[int]
        FEATURE_STATS_AND_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
        total_slot_ms: int
        feature_stats_and_anomalies: _containers.RepeatedCompositeFieldContainer[_feature_monitor_pb2.FeatureStatsAndAnomaly]
        def __init__(self, total_slot_ms: _Optional[int] = ..., feature_stats_and_anomalies: _Optional[_Iterable[_Union[_feature_monitor_pb2.FeatureStatsAndAnomaly, _Mapping]]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FINAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DRIFT_BASE_FEATURE_MONITOR_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DRIFT_BASE_SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SELECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    final_status: _status_pb2.Status
    job_summary: FeatureMonitorJob.JobSummary
    labels: _containers.ScalarMap[str, str]
    description: str
    drift_base_feature_monitor_job_id: int
    drift_base_snapshot_time: _timestamp_pb2.Timestamp
    feature_selection_config: _feature_monitor_pb2.FeatureSelectionConfig
    trigger_type: FeatureMonitorJob.FeatureMonitorJobTrigger
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., final_status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., job_summary: _Optional[_Union[FeatureMonitorJob.JobSummary, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., drift_base_feature_monitor_job_id: _Optional[int] = ..., drift_base_snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., feature_selection_config: _Optional[_Union[_feature_monitor_pb2.FeatureSelectionConfig, _Mapping]] = ..., trigger_type: _Optional[_Union[FeatureMonitorJob.FeatureMonitorJobTrigger, str]] = ...) -> None: ...
