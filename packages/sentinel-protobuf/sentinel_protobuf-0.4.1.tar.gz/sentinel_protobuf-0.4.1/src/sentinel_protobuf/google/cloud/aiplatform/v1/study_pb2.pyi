from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Study(_message.Message):
    __slots__ = ("name", "display_name", "study_spec", "state", "create_time", "inactive_reason")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Study.State]
        ACTIVE: _ClassVar[Study.State]
        INACTIVE: _ClassVar[Study.State]
        COMPLETED: _ClassVar[Study.State]
    STATE_UNSPECIFIED: Study.State
    ACTIVE: Study.State
    INACTIVE: Study.State
    COMPLETED: Study.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STUDY_SPEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    study_spec: StudySpec
    state: Study.State
    create_time: _timestamp_pb2.Timestamp
    inactive_reason: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., study_spec: _Optional[_Union[StudySpec, _Mapping]] = ..., state: _Optional[_Union[Study.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., inactive_reason: _Optional[str] = ...) -> None: ...

class Trial(_message.Message):
    __slots__ = ("name", "id", "state", "parameters", "final_measurement", "measurements", "start_time", "end_time", "client_id", "infeasible_reason", "custom_job", "web_access_uris")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Trial.State]
        REQUESTED: _ClassVar[Trial.State]
        ACTIVE: _ClassVar[Trial.State]
        STOPPING: _ClassVar[Trial.State]
        SUCCEEDED: _ClassVar[Trial.State]
        INFEASIBLE: _ClassVar[Trial.State]
    STATE_UNSPECIFIED: Trial.State
    REQUESTED: Trial.State
    ACTIVE: Trial.State
    STOPPING: Trial.State
    SUCCEEDED: Trial.State
    INFEASIBLE: Trial.State
    class Parameter(_message.Message):
        __slots__ = ("parameter_id", "value")
        PARAMETER_ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        parameter_id: str
        value: _struct_pb2.Value
        def __init__(self, parameter_id: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class WebAccessUrisEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    INFEASIBLE_REASON_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_JOB_FIELD_NUMBER: _ClassVar[int]
    WEB_ACCESS_URIS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    state: Trial.State
    parameters: _containers.RepeatedCompositeFieldContainer[Trial.Parameter]
    final_measurement: Measurement
    measurements: _containers.RepeatedCompositeFieldContainer[Measurement]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    client_id: str
    infeasible_reason: str
    custom_job: str
    web_access_uris: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., state: _Optional[_Union[Trial.State, str]] = ..., parameters: _Optional[_Iterable[_Union[Trial.Parameter, _Mapping]]] = ..., final_measurement: _Optional[_Union[Measurement, _Mapping]] = ..., measurements: _Optional[_Iterable[_Union[Measurement, _Mapping]]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., client_id: _Optional[str] = ..., infeasible_reason: _Optional[str] = ..., custom_job: _Optional[str] = ..., web_access_uris: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TrialContext(_message.Message):
    __slots__ = ("description", "parameters")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    description: str
    parameters: _containers.RepeatedCompositeFieldContainer[Trial.Parameter]
    def __init__(self, description: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[Trial.Parameter, _Mapping]]] = ...) -> None: ...

class StudyTimeConstraint(_message.Message):
    __slots__ = ("max_duration", "end_time")
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    max_duration: _duration_pb2.Duration
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StudySpec(_message.Message):
    __slots__ = ("decay_curve_stopping_spec", "median_automated_stopping_spec", "convex_automated_stopping_spec", "metrics", "parameters", "algorithm", "observation_noise", "measurement_selection_type", "study_stopping_config")
    class Algorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALGORITHM_UNSPECIFIED: _ClassVar[StudySpec.Algorithm]
        GRID_SEARCH: _ClassVar[StudySpec.Algorithm]
        RANDOM_SEARCH: _ClassVar[StudySpec.Algorithm]
    ALGORITHM_UNSPECIFIED: StudySpec.Algorithm
    GRID_SEARCH: StudySpec.Algorithm
    RANDOM_SEARCH: StudySpec.Algorithm
    class ObservationNoise(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OBSERVATION_NOISE_UNSPECIFIED: _ClassVar[StudySpec.ObservationNoise]
        LOW: _ClassVar[StudySpec.ObservationNoise]
        HIGH: _ClassVar[StudySpec.ObservationNoise]
    OBSERVATION_NOISE_UNSPECIFIED: StudySpec.ObservationNoise
    LOW: StudySpec.ObservationNoise
    HIGH: StudySpec.ObservationNoise
    class MeasurementSelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEASUREMENT_SELECTION_TYPE_UNSPECIFIED: _ClassVar[StudySpec.MeasurementSelectionType]
        LAST_MEASUREMENT: _ClassVar[StudySpec.MeasurementSelectionType]
        BEST_MEASUREMENT: _ClassVar[StudySpec.MeasurementSelectionType]
    MEASUREMENT_SELECTION_TYPE_UNSPECIFIED: StudySpec.MeasurementSelectionType
    LAST_MEASUREMENT: StudySpec.MeasurementSelectionType
    BEST_MEASUREMENT: StudySpec.MeasurementSelectionType
    class MetricSpec(_message.Message):
        __slots__ = ("metric_id", "goal", "safety_config")
        class GoalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GOAL_TYPE_UNSPECIFIED: _ClassVar[StudySpec.MetricSpec.GoalType]
            MAXIMIZE: _ClassVar[StudySpec.MetricSpec.GoalType]
            MINIMIZE: _ClassVar[StudySpec.MetricSpec.GoalType]
        GOAL_TYPE_UNSPECIFIED: StudySpec.MetricSpec.GoalType
        MAXIMIZE: StudySpec.MetricSpec.GoalType
        MINIMIZE: StudySpec.MetricSpec.GoalType
        class SafetyMetricConfig(_message.Message):
            __slots__ = ("safety_threshold", "desired_min_safe_trials_fraction")
            SAFETY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            DESIRED_MIN_SAFE_TRIALS_FRACTION_FIELD_NUMBER: _ClassVar[int]
            safety_threshold: float
            desired_min_safe_trials_fraction: float
            def __init__(self, safety_threshold: _Optional[float] = ..., desired_min_safe_trials_fraction: _Optional[float] = ...) -> None: ...
        METRIC_ID_FIELD_NUMBER: _ClassVar[int]
        GOAL_FIELD_NUMBER: _ClassVar[int]
        SAFETY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        metric_id: str
        goal: StudySpec.MetricSpec.GoalType
        safety_config: StudySpec.MetricSpec.SafetyMetricConfig
        def __init__(self, metric_id: _Optional[str] = ..., goal: _Optional[_Union[StudySpec.MetricSpec.GoalType, str]] = ..., safety_config: _Optional[_Union[StudySpec.MetricSpec.SafetyMetricConfig, _Mapping]] = ...) -> None: ...
    class ParameterSpec(_message.Message):
        __slots__ = ("double_value_spec", "integer_value_spec", "categorical_value_spec", "discrete_value_spec", "parameter_id", "scale_type", "conditional_parameter_specs")
        class ScaleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_TYPE_UNSPECIFIED: _ClassVar[StudySpec.ParameterSpec.ScaleType]
            UNIT_LINEAR_SCALE: _ClassVar[StudySpec.ParameterSpec.ScaleType]
            UNIT_LOG_SCALE: _ClassVar[StudySpec.ParameterSpec.ScaleType]
            UNIT_REVERSE_LOG_SCALE: _ClassVar[StudySpec.ParameterSpec.ScaleType]
        SCALE_TYPE_UNSPECIFIED: StudySpec.ParameterSpec.ScaleType
        UNIT_LINEAR_SCALE: StudySpec.ParameterSpec.ScaleType
        UNIT_LOG_SCALE: StudySpec.ParameterSpec.ScaleType
        UNIT_REVERSE_LOG_SCALE: StudySpec.ParameterSpec.ScaleType
        class DoubleValueSpec(_message.Message):
            __slots__ = ("min_value", "max_value", "default_value")
            MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
            MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            min_value: float
            max_value: float
            default_value: float
            def __init__(self, min_value: _Optional[float] = ..., max_value: _Optional[float] = ..., default_value: _Optional[float] = ...) -> None: ...
        class IntegerValueSpec(_message.Message):
            __slots__ = ("min_value", "max_value", "default_value")
            MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
            MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            min_value: int
            max_value: int
            default_value: int
            def __init__(self, min_value: _Optional[int] = ..., max_value: _Optional[int] = ..., default_value: _Optional[int] = ...) -> None: ...
        class CategoricalValueSpec(_message.Message):
            __slots__ = ("values", "default_value")
            VALUES_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[str]
            default_value: str
            def __init__(self, values: _Optional[_Iterable[str]] = ..., default_value: _Optional[str] = ...) -> None: ...
        class DiscreteValueSpec(_message.Message):
            __slots__ = ("values", "default_value")
            VALUES_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[float]
            default_value: float
            def __init__(self, values: _Optional[_Iterable[float]] = ..., default_value: _Optional[float] = ...) -> None: ...
        class ConditionalParameterSpec(_message.Message):
            __slots__ = ("parent_discrete_values", "parent_int_values", "parent_categorical_values", "parameter_spec")
            class DiscreteValueCondition(_message.Message):
                __slots__ = ("values",)
                VALUES_FIELD_NUMBER: _ClassVar[int]
                values: _containers.RepeatedScalarFieldContainer[float]
                def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...
            class IntValueCondition(_message.Message):
                __slots__ = ("values",)
                VALUES_FIELD_NUMBER: _ClassVar[int]
                values: _containers.RepeatedScalarFieldContainer[int]
                def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...
            class CategoricalValueCondition(_message.Message):
                __slots__ = ("values",)
                VALUES_FIELD_NUMBER: _ClassVar[int]
                values: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
            PARENT_DISCRETE_VALUES_FIELD_NUMBER: _ClassVar[int]
            PARENT_INT_VALUES_FIELD_NUMBER: _ClassVar[int]
            PARENT_CATEGORICAL_VALUES_FIELD_NUMBER: _ClassVar[int]
            PARAMETER_SPEC_FIELD_NUMBER: _ClassVar[int]
            parent_discrete_values: StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition
            parent_int_values: StudySpec.ParameterSpec.ConditionalParameterSpec.IntValueCondition
            parent_categorical_values: StudySpec.ParameterSpec.ConditionalParameterSpec.CategoricalValueCondition
            parameter_spec: StudySpec.ParameterSpec
            def __init__(self, parent_discrete_values: _Optional[_Union[StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition, _Mapping]] = ..., parent_int_values: _Optional[_Union[StudySpec.ParameterSpec.ConditionalParameterSpec.IntValueCondition, _Mapping]] = ..., parent_categorical_values: _Optional[_Union[StudySpec.ParameterSpec.ConditionalParameterSpec.CategoricalValueCondition, _Mapping]] = ..., parameter_spec: _Optional[_Union[StudySpec.ParameterSpec, _Mapping]] = ...) -> None: ...
        DOUBLE_VALUE_SPEC_FIELD_NUMBER: _ClassVar[int]
        INTEGER_VALUE_SPEC_FIELD_NUMBER: _ClassVar[int]
        CATEGORICAL_VALUE_SPEC_FIELD_NUMBER: _ClassVar[int]
        DISCRETE_VALUE_SPEC_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_ID_FIELD_NUMBER: _ClassVar[int]
        SCALE_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONDITIONAL_PARAMETER_SPECS_FIELD_NUMBER: _ClassVar[int]
        double_value_spec: StudySpec.ParameterSpec.DoubleValueSpec
        integer_value_spec: StudySpec.ParameterSpec.IntegerValueSpec
        categorical_value_spec: StudySpec.ParameterSpec.CategoricalValueSpec
        discrete_value_spec: StudySpec.ParameterSpec.DiscreteValueSpec
        parameter_id: str
        scale_type: StudySpec.ParameterSpec.ScaleType
        conditional_parameter_specs: _containers.RepeatedCompositeFieldContainer[StudySpec.ParameterSpec.ConditionalParameterSpec]
        def __init__(self, double_value_spec: _Optional[_Union[StudySpec.ParameterSpec.DoubleValueSpec, _Mapping]] = ..., integer_value_spec: _Optional[_Union[StudySpec.ParameterSpec.IntegerValueSpec, _Mapping]] = ..., categorical_value_spec: _Optional[_Union[StudySpec.ParameterSpec.CategoricalValueSpec, _Mapping]] = ..., discrete_value_spec: _Optional[_Union[StudySpec.ParameterSpec.DiscreteValueSpec, _Mapping]] = ..., parameter_id: _Optional[str] = ..., scale_type: _Optional[_Union[StudySpec.ParameterSpec.ScaleType, str]] = ..., conditional_parameter_specs: _Optional[_Iterable[_Union[StudySpec.ParameterSpec.ConditionalParameterSpec, _Mapping]]] = ...) -> None: ...
    class DecayCurveAutomatedStoppingSpec(_message.Message):
        __slots__ = ("use_elapsed_duration",)
        USE_ELAPSED_DURATION_FIELD_NUMBER: _ClassVar[int]
        use_elapsed_duration: bool
        def __init__(self, use_elapsed_duration: bool = ...) -> None: ...
    class MedianAutomatedStoppingSpec(_message.Message):
        __slots__ = ("use_elapsed_duration",)
        USE_ELAPSED_DURATION_FIELD_NUMBER: _ClassVar[int]
        use_elapsed_duration: bool
        def __init__(self, use_elapsed_duration: bool = ...) -> None: ...
    class ConvexAutomatedStoppingSpec(_message.Message):
        __slots__ = ("max_step_count", "min_step_count", "min_measurement_count", "learning_rate_parameter_name", "use_elapsed_duration", "update_all_stopped_trials")
        MAX_STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
        MIN_STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
        MIN_MEASUREMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        LEARNING_RATE_PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
        USE_ELAPSED_DURATION_FIELD_NUMBER: _ClassVar[int]
        UPDATE_ALL_STOPPED_TRIALS_FIELD_NUMBER: _ClassVar[int]
        max_step_count: int
        min_step_count: int
        min_measurement_count: int
        learning_rate_parameter_name: str
        use_elapsed_duration: bool
        update_all_stopped_trials: bool
        def __init__(self, max_step_count: _Optional[int] = ..., min_step_count: _Optional[int] = ..., min_measurement_count: _Optional[int] = ..., learning_rate_parameter_name: _Optional[str] = ..., use_elapsed_duration: bool = ..., update_all_stopped_trials: bool = ...) -> None: ...
    class StudyStoppingConfig(_message.Message):
        __slots__ = ("should_stop_asap", "minimum_runtime_constraint", "maximum_runtime_constraint", "min_num_trials", "max_num_trials", "max_num_trials_no_progress", "max_duration_no_progress")
        SHOULD_STOP_ASAP_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_RUNTIME_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_RUNTIME_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
        MIN_NUM_TRIALS_FIELD_NUMBER: _ClassVar[int]
        MAX_NUM_TRIALS_FIELD_NUMBER: _ClassVar[int]
        MAX_NUM_TRIALS_NO_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        MAX_DURATION_NO_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        should_stop_asap: _wrappers_pb2.BoolValue
        minimum_runtime_constraint: StudyTimeConstraint
        maximum_runtime_constraint: StudyTimeConstraint
        min_num_trials: _wrappers_pb2.Int32Value
        max_num_trials: _wrappers_pb2.Int32Value
        max_num_trials_no_progress: _wrappers_pb2.Int32Value
        max_duration_no_progress: _duration_pb2.Duration
        def __init__(self, should_stop_asap: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., minimum_runtime_constraint: _Optional[_Union[StudyTimeConstraint, _Mapping]] = ..., maximum_runtime_constraint: _Optional[_Union[StudyTimeConstraint, _Mapping]] = ..., min_num_trials: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., max_num_trials: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., max_num_trials_no_progress: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., max_duration_no_progress: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    DECAY_CURVE_STOPPING_SPEC_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_AUTOMATED_STOPPING_SPEC_FIELD_NUMBER: _ClassVar[int]
    CONVEX_AUTOMATED_STOPPING_SPEC_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_NOISE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_SELECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STUDY_STOPPING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    decay_curve_stopping_spec: StudySpec.DecayCurveAutomatedStoppingSpec
    median_automated_stopping_spec: StudySpec.MedianAutomatedStoppingSpec
    convex_automated_stopping_spec: StudySpec.ConvexAutomatedStoppingSpec
    metrics: _containers.RepeatedCompositeFieldContainer[StudySpec.MetricSpec]
    parameters: _containers.RepeatedCompositeFieldContainer[StudySpec.ParameterSpec]
    algorithm: StudySpec.Algorithm
    observation_noise: StudySpec.ObservationNoise
    measurement_selection_type: StudySpec.MeasurementSelectionType
    study_stopping_config: StudySpec.StudyStoppingConfig
    def __init__(self, decay_curve_stopping_spec: _Optional[_Union[StudySpec.DecayCurveAutomatedStoppingSpec, _Mapping]] = ..., median_automated_stopping_spec: _Optional[_Union[StudySpec.MedianAutomatedStoppingSpec, _Mapping]] = ..., convex_automated_stopping_spec: _Optional[_Union[StudySpec.ConvexAutomatedStoppingSpec, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[StudySpec.MetricSpec, _Mapping]]] = ..., parameters: _Optional[_Iterable[_Union[StudySpec.ParameterSpec, _Mapping]]] = ..., algorithm: _Optional[_Union[StudySpec.Algorithm, str]] = ..., observation_noise: _Optional[_Union[StudySpec.ObservationNoise, str]] = ..., measurement_selection_type: _Optional[_Union[StudySpec.MeasurementSelectionType, str]] = ..., study_stopping_config: _Optional[_Union[StudySpec.StudyStoppingConfig, _Mapping]] = ...) -> None: ...

class Measurement(_message.Message):
    __slots__ = ("elapsed_duration", "step_count", "metrics")
    class Metric(_message.Message):
        __slots__ = ("metric_id", "value")
        METRIC_ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        metric_id: str
        value: float
        def __init__(self, metric_id: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    ELAPSED_DURATION_FIELD_NUMBER: _ClassVar[int]
    STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    elapsed_duration: _duration_pb2.Duration
    step_count: int
    metrics: _containers.RepeatedCompositeFieldContainer[Measurement.Metric]
    def __init__(self, elapsed_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., step_count: _Optional[int] = ..., metrics: _Optional[_Iterable[_Union[Measurement.Metric, _Mapping]]] = ...) -> None: ...
