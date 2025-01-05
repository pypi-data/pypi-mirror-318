from google.ads.googleads.v16.enums import experiment_metric_pb2 as _experiment_metric_pb2
from google.ads.googleads.v16.enums import experiment_metric_direction_pb2 as _experiment_metric_direction_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MetricGoal(_message.Message):
    __slots__ = ('metric', 'direction')
    METRIC_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    metric: _experiment_metric_pb2.ExperimentMetricEnum.ExperimentMetric
    direction: _experiment_metric_direction_pb2.ExperimentMetricDirectionEnum.ExperimentMetricDirection

    def __init__(self, metric: _Optional[_Union[_experiment_metric_pb2.ExperimentMetricEnum.ExperimentMetric, str]]=..., direction: _Optional[_Union[_experiment_metric_direction_pb2.ExperimentMetricDirectionEnum.ExperimentMetricDirection, str]]=...) -> None:
        ...