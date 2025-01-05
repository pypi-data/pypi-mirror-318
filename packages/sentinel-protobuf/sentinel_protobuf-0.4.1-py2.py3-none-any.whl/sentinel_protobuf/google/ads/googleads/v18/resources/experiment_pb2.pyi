from google.ads.googleads.v18.common import metric_goal_pb2 as _metric_goal_pb2
from google.ads.googleads.v18.enums import async_action_status_pb2 as _async_action_status_pb2
from google.ads.googleads.v18.enums import experiment_status_pb2 as _experiment_status_pb2
from google.ads.googleads.v18.enums import experiment_type_pb2 as _experiment_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Experiment(_message.Message):
    __slots__ = ("resource_name", "experiment_id", "name", "description", "suffix", "type", "status", "start_date", "end_date", "goals", "long_running_operation", "promote_status", "sync_enabled")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    GOALS_FIELD_NUMBER: _ClassVar[int]
    LONG_RUNNING_OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SYNC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    experiment_id: int
    name: str
    description: str
    suffix: str
    type: _experiment_type_pb2.ExperimentTypeEnum.ExperimentType
    status: _experiment_status_pb2.ExperimentStatusEnum.ExperimentStatus
    start_date: str
    end_date: str
    goals: _containers.RepeatedCompositeFieldContainer[_metric_goal_pb2.MetricGoal]
    long_running_operation: str
    promote_status: _async_action_status_pb2.AsyncActionStatusEnum.AsyncActionStatus
    sync_enabled: bool
    def __init__(self, resource_name: _Optional[str] = ..., experiment_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., suffix: _Optional[str] = ..., type: _Optional[_Union[_experiment_type_pb2.ExperimentTypeEnum.ExperimentType, str]] = ..., status: _Optional[_Union[_experiment_status_pb2.ExperimentStatusEnum.ExperimentStatus, str]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., goals: _Optional[_Iterable[_Union[_metric_goal_pb2.MetricGoal, _Mapping]]] = ..., long_running_operation: _Optional[str] = ..., promote_status: _Optional[_Union[_async_action_status_pb2.AsyncActionStatusEnum.AsyncActionStatus, str]] = ..., sync_enabled: bool = ...) -> None: ...
