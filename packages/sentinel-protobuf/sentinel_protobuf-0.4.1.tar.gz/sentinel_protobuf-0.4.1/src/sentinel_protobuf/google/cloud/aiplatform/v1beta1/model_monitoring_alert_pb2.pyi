from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ModelMonitoringAlertCondition(_message.Message):
    __slots__ = ('threshold',)
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    threshold: float

    def __init__(self, threshold: _Optional[float]=...) -> None:
        ...

class ModelMonitoringAnomaly(_message.Message):
    __slots__ = ('tabular_anomaly', 'model_monitoring_job', 'algorithm')

    class TabularAnomaly(_message.Message):
        __slots__ = ('anomaly_uri', 'summary', 'anomaly', 'trigger_time', 'condition')
        ANOMALY_URI_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        ANOMALY_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        anomaly_uri: str
        summary: str
        anomaly: _struct_pb2.Value
        trigger_time: _timestamp_pb2.Timestamp
        condition: ModelMonitoringAlertCondition

        def __init__(self, anomaly_uri: _Optional[str]=..., summary: _Optional[str]=..., anomaly: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., trigger_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., condition: _Optional[_Union[ModelMonitoringAlertCondition, _Mapping]]=...) -> None:
            ...
    TABULAR_ANOMALY_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    tabular_anomaly: ModelMonitoringAnomaly.TabularAnomaly
    model_monitoring_job: str
    algorithm: str

    def __init__(self, tabular_anomaly: _Optional[_Union[ModelMonitoringAnomaly.TabularAnomaly, _Mapping]]=..., model_monitoring_job: _Optional[str]=..., algorithm: _Optional[str]=...) -> None:
        ...

class ModelMonitoringAlert(_message.Message):
    __slots__ = ('stats_name', 'objective_type', 'alert_time', 'anomaly')
    STATS_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALERT_TIME_FIELD_NUMBER: _ClassVar[int]
    ANOMALY_FIELD_NUMBER: _ClassVar[int]
    stats_name: str
    objective_type: str
    alert_time: _timestamp_pb2.Timestamp
    anomaly: ModelMonitoringAnomaly

    def __init__(self, stats_name: _Optional[str]=..., objective_type: _Optional[str]=..., alert_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., anomaly: _Optional[_Union[ModelMonitoringAnomaly, _Mapping]]=...) -> None:
        ...