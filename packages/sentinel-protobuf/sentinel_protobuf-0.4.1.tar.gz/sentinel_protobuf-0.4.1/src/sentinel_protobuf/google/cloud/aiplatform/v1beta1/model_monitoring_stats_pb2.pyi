from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ModelMonitoringStats(_message.Message):
    __slots__ = ('tabular_stats',)
    TABULAR_STATS_FIELD_NUMBER: _ClassVar[int]
    tabular_stats: ModelMonitoringTabularStats

    def __init__(self, tabular_stats: _Optional[_Union[ModelMonitoringTabularStats, _Mapping]]=...) -> None:
        ...

class ModelMonitoringStatsDataPoint(_message.Message):
    __slots__ = ('current_stats', 'baseline_stats', 'threshold_value', 'has_anomaly', 'model_monitoring_job', 'schedule', 'create_time', 'algorithm')

    class TypedValue(_message.Message):
        __slots__ = ('double_value', 'distribution_value')

        class DistributionDataValue(_message.Message):
            __slots__ = ('distribution', 'distribution_deviation')
            DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
            DISTRIBUTION_DEVIATION_FIELD_NUMBER: _ClassVar[int]
            distribution: _struct_pb2.Value
            distribution_deviation: float

            def __init__(self, distribution: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., distribution_deviation: _Optional[float]=...) -> None:
                ...
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        DISTRIBUTION_VALUE_FIELD_NUMBER: _ClassVar[int]
        double_value: float
        distribution_value: ModelMonitoringStatsDataPoint.TypedValue.DistributionDataValue

        def __init__(self, double_value: _Optional[float]=..., distribution_value: _Optional[_Union[ModelMonitoringStatsDataPoint.TypedValue.DistributionDataValue, _Mapping]]=...) -> None:
            ...
    CURRENT_STATS_FIELD_NUMBER: _ClassVar[int]
    BASELINE_STATS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    HAS_ANOMALY_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    current_stats: ModelMonitoringStatsDataPoint.TypedValue
    baseline_stats: ModelMonitoringStatsDataPoint.TypedValue
    threshold_value: float
    has_anomaly: bool
    model_monitoring_job: str
    schedule: str
    create_time: _timestamp_pb2.Timestamp
    algorithm: str

    def __init__(self, current_stats: _Optional[_Union[ModelMonitoringStatsDataPoint.TypedValue, _Mapping]]=..., baseline_stats: _Optional[_Union[ModelMonitoringStatsDataPoint.TypedValue, _Mapping]]=..., threshold_value: _Optional[float]=..., has_anomaly: bool=..., model_monitoring_job: _Optional[str]=..., schedule: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., algorithm: _Optional[str]=...) -> None:
        ...

class ModelMonitoringTabularStats(_message.Message):
    __slots__ = ('stats_name', 'objective_type', 'data_points')
    STATS_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    stats_name: str
    objective_type: str
    data_points: _containers.RepeatedCompositeFieldContainer[ModelMonitoringStatsDataPoint]

    def __init__(self, stats_name: _Optional[str]=..., objective_type: _Optional[str]=..., data_points: _Optional[_Iterable[_Union[ModelMonitoringStatsDataPoint, _Mapping]]]=...) -> None:
        ...

class SearchModelMonitoringStatsFilter(_message.Message):
    __slots__ = ('tabular_stats_filter',)

    class TabularStatsFilter(_message.Message):
        __slots__ = ('stats_name', 'objective_type', 'model_monitoring_job', 'model_monitoring_schedule', 'algorithm')
        STATS_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECTIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        MODEL_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
        MODEL_MONITORING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        stats_name: str
        objective_type: str
        model_monitoring_job: str
        model_monitoring_schedule: str
        algorithm: str

        def __init__(self, stats_name: _Optional[str]=..., objective_type: _Optional[str]=..., model_monitoring_job: _Optional[str]=..., model_monitoring_schedule: _Optional[str]=..., algorithm: _Optional[str]=...) -> None:
            ...
    TABULAR_STATS_FILTER_FIELD_NUMBER: _ClassVar[int]
    tabular_stats_filter: SearchModelMonitoringStatsFilter.TabularStatsFilter

    def __init__(self, tabular_stats_filter: _Optional[_Union[SearchModelMonitoringStatsFilter.TabularStatsFilter, _Mapping]]=...) -> None:
        ...