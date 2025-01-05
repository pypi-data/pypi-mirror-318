from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoscalerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTOSCALER_STATE_UNSPECIFIED: _ClassVar[AutoscalerState]
    COOLDOWN: _ClassVar[AutoscalerState]
    RECOMMENDING: _ClassVar[AutoscalerState]
    SCALING: _ClassVar[AutoscalerState]
    STOPPED: _ClassVar[AutoscalerState]
    FAILED: _ClassVar[AutoscalerState]
    INITIALIZING: _ClassVar[AutoscalerState]

class ScalingDecisionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCALING_DECISION_TYPE_UNSPECIFIED: _ClassVar[ScalingDecisionType]
    SCALE_UP: _ClassVar[ScalingDecisionType]
    SCALE_DOWN: _ClassVar[ScalingDecisionType]
    NO_SCALE: _ClassVar[ScalingDecisionType]
    MIXED: _ClassVar[ScalingDecisionType]
    CANCEL: _ClassVar[ScalingDecisionType]
    DO_NOT_CANCEL: _ClassVar[ScalingDecisionType]

class ConstrainingFactor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSTRAINING_FACTOR_UNSPECIFIED: _ClassVar[ConstrainingFactor]
    SCALING_CAPPED_DUE_TO_LACK_OF_QUOTA: _ClassVar[ConstrainingFactor]
    REACHED_MAXIMUM_CLUSTER_SIZE: _ClassVar[ConstrainingFactor]
    REACHED_MINIMUM_CLUSTER_SIZE: _ClassVar[ConstrainingFactor]
    SECONDARY_SCALEDOWN_SINGLE_REQUEST_LIMIT_REACHED: _ClassVar[ConstrainingFactor]

class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_TYPE_UNSPECIFIED: _ClassVar[MetricType]
    YARN_MEMORY: _ClassVar[MetricType]
    YARN_CORES: _ClassVar[MetricType]
    SPARK_EXECUTORS: _ClassVar[MetricType]
AUTOSCALER_STATE_UNSPECIFIED: AutoscalerState
COOLDOWN: AutoscalerState
RECOMMENDING: AutoscalerState
SCALING: AutoscalerState
STOPPED: AutoscalerState
FAILED: AutoscalerState
INITIALIZING: AutoscalerState
SCALING_DECISION_TYPE_UNSPECIFIED: ScalingDecisionType
SCALE_UP: ScalingDecisionType
SCALE_DOWN: ScalingDecisionType
NO_SCALE: ScalingDecisionType
MIXED: ScalingDecisionType
CANCEL: ScalingDecisionType
DO_NOT_CANCEL: ScalingDecisionType
CONSTRAINING_FACTOR_UNSPECIFIED: ConstrainingFactor
SCALING_CAPPED_DUE_TO_LACK_OF_QUOTA: ConstrainingFactor
REACHED_MAXIMUM_CLUSTER_SIZE: ConstrainingFactor
REACHED_MINIMUM_CLUSTER_SIZE: ConstrainingFactor
SECONDARY_SCALEDOWN_SINGLE_REQUEST_LIMIT_REACHED: ConstrainingFactor
METRIC_TYPE_UNSPECIFIED: MetricType
YARN_MEMORY: MetricType
YARN_CORES: MetricType
SPARK_EXECUTORS: MetricType

class ClusterSize(_message.Message):
    __slots__ = ('primary_worker_count', 'secondary_worker_count')
    PRIMARY_WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    primary_worker_count: int
    secondary_worker_count: int

    def __init__(self, primary_worker_count: _Optional[int]=..., secondary_worker_count: _Optional[int]=...) -> None:
        ...

class AutoscalerLog(_message.Message):
    __slots__ = ('status', 'recommendation')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    status: AutoscalerStatus
    recommendation: AutoscalerRecommendation

    def __init__(self, status: _Optional[_Union[AutoscalerStatus, _Mapping]]=..., recommendation: _Optional[_Union[AutoscalerRecommendation, _Mapping]]=...) -> None:
        ...

class AutoscalerStatus(_message.Message):
    __slots__ = ('state', 'details', 'update_cluster_operation_id', 'error')
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CLUSTER_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: AutoscalerState
    details: str
    update_cluster_operation_id: str
    error: str

    def __init__(self, state: _Optional[_Union[AutoscalerState, str]]=..., details: _Optional[str]=..., update_cluster_operation_id: _Optional[str]=..., error: _Optional[str]=...) -> None:
        ...

class AutoscalerRecommendation(_message.Message):
    __slots__ = ('inputs', 'outputs')

    class Inputs(_message.Message):
        __slots__ = ('cluster_metrics', 'current_cluster_size', 'min_worker_counts', 'max_worker_counts')

        class ClusterMetricsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        CLUSTER_METRICS_FIELD_NUMBER: _ClassVar[int]
        CURRENT_CLUSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
        MIN_WORKER_COUNTS_FIELD_NUMBER: _ClassVar[int]
        MAX_WORKER_COUNTS_FIELD_NUMBER: _ClassVar[int]
        cluster_metrics: _containers.ScalarMap[str, str]
        current_cluster_size: ClusterSize
        min_worker_counts: ClusterSize
        max_worker_counts: ClusterSize

        def __init__(self, cluster_metrics: _Optional[_Mapping[str, str]]=..., current_cluster_size: _Optional[_Union[ClusterSize, _Mapping]]=..., min_worker_counts: _Optional[_Union[ClusterSize, _Mapping]]=..., max_worker_counts: _Optional[_Union[ClusterSize, _Mapping]]=...) -> None:
            ...

    class Outputs(_message.Message):
        __slots__ = ('decision', 'recommended_cluster_size', 'graceful_decommission_timeout', 'constraints_reached', 'additional_recommendation_details', 'recommendation_id', 'decision_metric')
        DECISION_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_CLUSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
        GRACEFUL_DECOMMISSION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        CONSTRAINTS_REACHED_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_RECOMMENDATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDATION_ID_FIELD_NUMBER: _ClassVar[int]
        DECISION_METRIC_FIELD_NUMBER: _ClassVar[int]
        decision: ScalingDecisionType
        recommended_cluster_size: ClusterSize
        graceful_decommission_timeout: _duration_pb2.Duration
        constraints_reached: _containers.RepeatedScalarFieldContainer[ConstrainingFactor]
        additional_recommendation_details: _containers.RepeatedScalarFieldContainer[str]
        recommendation_id: str
        decision_metric: MetricType

        def __init__(self, decision: _Optional[_Union[ScalingDecisionType, str]]=..., recommended_cluster_size: _Optional[_Union[ClusterSize, _Mapping]]=..., graceful_decommission_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., constraints_reached: _Optional[_Iterable[_Union[ConstrainingFactor, str]]]=..., additional_recommendation_details: _Optional[_Iterable[str]]=..., recommendation_id: _Optional[str]=..., decision_metric: _Optional[_Union[MetricType, str]]=...) -> None:
            ...
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoscalerRecommendation.Inputs
    outputs: AutoscalerRecommendation.Outputs

    def __init__(self, inputs: _Optional[_Union[AutoscalerRecommendation.Inputs, _Mapping]]=..., outputs: _Optional[_Union[AutoscalerRecommendation.Outputs, _Mapping]]=...) -> None:
        ...