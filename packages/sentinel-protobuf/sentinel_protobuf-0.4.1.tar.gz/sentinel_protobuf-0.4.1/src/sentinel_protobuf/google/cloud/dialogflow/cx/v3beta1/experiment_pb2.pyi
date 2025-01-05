from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Experiment(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'state', 'definition', 'rollout_config', 'rollout_state', 'rollout_failure_reason', 'result', 'create_time', 'start_time', 'end_time', 'last_update_time', 'experiment_length', 'variants_history')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Experiment.State]
        DRAFT: _ClassVar[Experiment.State]
        RUNNING: _ClassVar[Experiment.State]
        DONE: _ClassVar[Experiment.State]
        ROLLOUT_FAILED: _ClassVar[Experiment.State]
    STATE_UNSPECIFIED: Experiment.State
    DRAFT: Experiment.State
    RUNNING: Experiment.State
    DONE: Experiment.State
    ROLLOUT_FAILED: Experiment.State

    class Definition(_message.Message):
        __slots__ = ('condition', 'version_variants')
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        VERSION_VARIANTS_FIELD_NUMBER: _ClassVar[int]
        condition: str
        version_variants: VersionVariants

        def __init__(self, condition: _Optional[str]=..., version_variants: _Optional[_Union[VersionVariants, _Mapping]]=...) -> None:
            ...

    class Result(_message.Message):
        __slots__ = ('version_metrics', 'last_update_time')

        class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METRIC_UNSPECIFIED: _ClassVar[Experiment.Result.MetricType]
            CONTAINED_SESSION_NO_CALLBACK_RATE: _ClassVar[Experiment.Result.MetricType]
            LIVE_AGENT_HANDOFF_RATE: _ClassVar[Experiment.Result.MetricType]
            CALLBACK_SESSION_RATE: _ClassVar[Experiment.Result.MetricType]
            ABANDONED_SESSION_RATE: _ClassVar[Experiment.Result.MetricType]
            SESSION_END_RATE: _ClassVar[Experiment.Result.MetricType]
        METRIC_UNSPECIFIED: Experiment.Result.MetricType
        CONTAINED_SESSION_NO_CALLBACK_RATE: Experiment.Result.MetricType
        LIVE_AGENT_HANDOFF_RATE: Experiment.Result.MetricType
        CALLBACK_SESSION_RATE: Experiment.Result.MetricType
        ABANDONED_SESSION_RATE: Experiment.Result.MetricType
        SESSION_END_RATE: Experiment.Result.MetricType

        class CountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            COUNT_TYPE_UNSPECIFIED: _ClassVar[Experiment.Result.CountType]
            TOTAL_NO_MATCH_COUNT: _ClassVar[Experiment.Result.CountType]
            TOTAL_TURN_COUNT: _ClassVar[Experiment.Result.CountType]
            AVERAGE_TURN_COUNT: _ClassVar[Experiment.Result.CountType]
        COUNT_TYPE_UNSPECIFIED: Experiment.Result.CountType
        TOTAL_NO_MATCH_COUNT: Experiment.Result.CountType
        TOTAL_TURN_COUNT: Experiment.Result.CountType
        AVERAGE_TURN_COUNT: Experiment.Result.CountType

        class ConfidenceInterval(_message.Message):
            __slots__ = ('confidence_level', 'ratio', 'lower_bound', 'upper_bound')
            CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
            RATIO_FIELD_NUMBER: _ClassVar[int]
            LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
            UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
            confidence_level: float
            ratio: float
            lower_bound: float
            upper_bound: float

            def __init__(self, confidence_level: _Optional[float]=..., ratio: _Optional[float]=..., lower_bound: _Optional[float]=..., upper_bound: _Optional[float]=...) -> None:
                ...

        class Metric(_message.Message):
            __slots__ = ('type', 'count_type', 'ratio', 'count', 'confidence_interval')
            TYPE_FIELD_NUMBER: _ClassVar[int]
            COUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
            RATIO_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            CONFIDENCE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
            type: Experiment.Result.MetricType
            count_type: Experiment.Result.CountType
            ratio: float
            count: float
            confidence_interval: Experiment.Result.ConfidenceInterval

            def __init__(self, type: _Optional[_Union[Experiment.Result.MetricType, str]]=..., count_type: _Optional[_Union[Experiment.Result.CountType, str]]=..., ratio: _Optional[float]=..., count: _Optional[float]=..., confidence_interval: _Optional[_Union[Experiment.Result.ConfidenceInterval, _Mapping]]=...) -> None:
                ...

        class VersionMetrics(_message.Message):
            __slots__ = ('version', 'metrics', 'session_count')
            VERSION_FIELD_NUMBER: _ClassVar[int]
            METRICS_FIELD_NUMBER: _ClassVar[int]
            SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
            version: str
            metrics: _containers.RepeatedCompositeFieldContainer[Experiment.Result.Metric]
            session_count: int

            def __init__(self, version: _Optional[str]=..., metrics: _Optional[_Iterable[_Union[Experiment.Result.Metric, _Mapping]]]=..., session_count: _Optional[int]=...) -> None:
                ...
        VERSION_METRICS_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        version_metrics: _containers.RepeatedCompositeFieldContainer[Experiment.Result.VersionMetrics]
        last_update_time: _timestamp_pb2.Timestamp

        def __init__(self, version_metrics: _Optional[_Iterable[_Union[Experiment.Result.VersionMetrics, _Mapping]]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_STATE_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    state: Experiment.State
    definition: Experiment.Definition
    rollout_config: RolloutConfig
    rollout_state: RolloutState
    rollout_failure_reason: str
    result: Experiment.Result
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    experiment_length: _duration_pb2.Duration
    variants_history: _containers.RepeatedCompositeFieldContainer[VariantsHistory]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[Experiment.State, str]]=..., definition: _Optional[_Union[Experiment.Definition, _Mapping]]=..., rollout_config: _Optional[_Union[RolloutConfig, _Mapping]]=..., rollout_state: _Optional[_Union[RolloutState, _Mapping]]=..., rollout_failure_reason: _Optional[str]=..., result: _Optional[_Union[Experiment.Result, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., experiment_length: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., variants_history: _Optional[_Iterable[_Union[VariantsHistory, _Mapping]]]=...) -> None:
        ...

class VersionVariants(_message.Message):
    __slots__ = ('variants',)

    class Variant(_message.Message):
        __slots__ = ('version', 'traffic_allocation', 'is_control_group')
        VERSION_FIELD_NUMBER: _ClassVar[int]
        TRAFFIC_ALLOCATION_FIELD_NUMBER: _ClassVar[int]
        IS_CONTROL_GROUP_FIELD_NUMBER: _ClassVar[int]
        version: str
        traffic_allocation: float
        is_control_group: bool

        def __init__(self, version: _Optional[str]=..., traffic_allocation: _Optional[float]=..., is_control_group: bool=...) -> None:
            ...
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    variants: _containers.RepeatedCompositeFieldContainer[VersionVariants.Variant]

    def __init__(self, variants: _Optional[_Iterable[_Union[VersionVariants.Variant, _Mapping]]]=...) -> None:
        ...

class RolloutConfig(_message.Message):
    __slots__ = ('rollout_steps', 'rollout_condition', 'failure_condition')

    class RolloutStep(_message.Message):
        __slots__ = ('display_name', 'traffic_percent', 'min_duration')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        TRAFFIC_PERCENT_FIELD_NUMBER: _ClassVar[int]
        MIN_DURATION_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        traffic_percent: int
        min_duration: _duration_pb2.Duration

        def __init__(self, display_name: _Optional[str]=..., traffic_percent: _Optional[int]=..., min_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    ROLLOUT_STEPS_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    rollout_steps: _containers.RepeatedCompositeFieldContainer[RolloutConfig.RolloutStep]
    rollout_condition: str
    failure_condition: str

    def __init__(self, rollout_steps: _Optional[_Iterable[_Union[RolloutConfig.RolloutStep, _Mapping]]]=..., rollout_condition: _Optional[str]=..., failure_condition: _Optional[str]=...) -> None:
        ...

class RolloutState(_message.Message):
    __slots__ = ('step', 'step_index', 'start_time')
    STEP_FIELD_NUMBER: _ClassVar[int]
    STEP_INDEX_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    step: str
    step_index: int
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, step: _Optional[str]=..., step_index: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class VariantsHistory(_message.Message):
    __slots__ = ('version_variants', 'update_time')
    VERSION_VARIANTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    version_variants: VersionVariants
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, version_variants: _Optional[_Union[VersionVariants, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListExperimentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListExperimentsResponse(_message.Message):
    __slots__ = ('experiments', 'next_page_token')
    EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    experiments: _containers.RepeatedCompositeFieldContainer[Experiment]
    next_page_token: str

    def __init__(self, experiments: _Optional[_Iterable[_Union[Experiment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetExperimentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateExperimentRequest(_message.Message):
    __slots__ = ('parent', 'experiment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    experiment: Experiment

    def __init__(self, parent: _Optional[str]=..., experiment: _Optional[_Union[Experiment, _Mapping]]=...) -> None:
        ...

class UpdateExperimentRequest(_message.Message):
    __slots__ = ('experiment', 'update_mask')
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    experiment: Experiment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, experiment: _Optional[_Union[Experiment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteExperimentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartExperimentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StopExperimentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...