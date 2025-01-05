from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureStatsAnomaly(_message.Message):
    __slots__ = ('score', 'stats_uri', 'anomaly_uri', 'distribution_deviation', 'anomaly_detection_threshold', 'start_time', 'end_time')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATS_URI_FIELD_NUMBER: _ClassVar[int]
    ANOMALY_URI_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    ANOMALY_DETECTION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    score: float
    stats_uri: str
    anomaly_uri: str
    distribution_deviation: float
    anomaly_detection_threshold: float
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, score: _Optional[float]=..., stats_uri: _Optional[str]=..., anomaly_uri: _Optional[str]=..., distribution_deviation: _Optional[float]=..., anomaly_detection_threshold: _Optional[float]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...