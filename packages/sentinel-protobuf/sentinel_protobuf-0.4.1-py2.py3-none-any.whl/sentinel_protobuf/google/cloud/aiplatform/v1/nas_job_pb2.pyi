from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import custom_job_pb2 as _custom_job_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as _job_state_pb2
from google.cloud.aiplatform.v1 import study_pb2 as _study_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NasJob(_message.Message):
    __slots__ = ("name", "display_name", "nas_job_spec", "nas_job_output", "state", "create_time", "start_time", "end_time", "update_time", "error", "labels", "encryption_spec", "enable_restricted_image_training", "satisfies_pzs", "satisfies_pzi")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAS_JOB_SPEC_FIELD_NUMBER: _ClassVar[int]
    NAS_JOB_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RESTRICTED_IMAGE_TRAINING_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    nas_job_spec: NasJobSpec
    nas_job_output: NasJobOutput
    state: _job_state_pb2.JobState
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    labels: _containers.ScalarMap[str, str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    enable_restricted_image_training: bool
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., nas_job_spec: _Optional[_Union[NasJobSpec, _Mapping]] = ..., nas_job_output: _Optional[_Union[NasJobOutput, _Mapping]] = ..., state: _Optional[_Union[_job_state_pb2.JobState, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]] = ..., enable_restricted_image_training: bool = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class NasTrialDetail(_message.Message):
    __slots__ = ("name", "parameters", "search_trial", "train_trial")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TRIAL_FIELD_NUMBER: _ClassVar[int]
    TRAIN_TRIAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameters: str
    search_trial: NasTrial
    train_trial: NasTrial
    def __init__(self, name: _Optional[str] = ..., parameters: _Optional[str] = ..., search_trial: _Optional[_Union[NasTrial, _Mapping]] = ..., train_trial: _Optional[_Union[NasTrial, _Mapping]] = ...) -> None: ...

class NasJobSpec(_message.Message):
    __slots__ = ("multi_trial_algorithm_spec", "resume_nas_job_id", "search_space_spec")
    class MultiTrialAlgorithmSpec(_message.Message):
        __slots__ = ("multi_trial_algorithm", "metric", "search_trial_spec", "train_trial_spec")
        class MultiTrialAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MULTI_TRIAL_ALGORITHM_UNSPECIFIED: _ClassVar[NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm]
            REINFORCEMENT_LEARNING: _ClassVar[NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm]
            GRID_SEARCH: _ClassVar[NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm]
        MULTI_TRIAL_ALGORITHM_UNSPECIFIED: NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm
        REINFORCEMENT_LEARNING: NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm
        GRID_SEARCH: NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm
        class MetricSpec(_message.Message):
            __slots__ = ("metric_id", "goal")
            class GoalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                GOAL_TYPE_UNSPECIFIED: _ClassVar[NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType]
                MAXIMIZE: _ClassVar[NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType]
                MINIMIZE: _ClassVar[NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType]
            GOAL_TYPE_UNSPECIFIED: NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType
            MAXIMIZE: NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType
            MINIMIZE: NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType
            METRIC_ID_FIELD_NUMBER: _ClassVar[int]
            GOAL_FIELD_NUMBER: _ClassVar[int]
            metric_id: str
            goal: NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType
            def __init__(self, metric_id: _Optional[str] = ..., goal: _Optional[_Union[NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalType, str]] = ...) -> None: ...
        class SearchTrialSpec(_message.Message):
            __slots__ = ("search_trial_job_spec", "max_trial_count", "max_parallel_trial_count", "max_failed_trial_count")
            SEARCH_TRIAL_JOB_SPEC_FIELD_NUMBER: _ClassVar[int]
            MAX_TRIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
            MAX_PARALLEL_TRIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
            MAX_FAILED_TRIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
            search_trial_job_spec: _custom_job_pb2.CustomJobSpec
            max_trial_count: int
            max_parallel_trial_count: int
            max_failed_trial_count: int
            def __init__(self, search_trial_job_spec: _Optional[_Union[_custom_job_pb2.CustomJobSpec, _Mapping]] = ..., max_trial_count: _Optional[int] = ..., max_parallel_trial_count: _Optional[int] = ..., max_failed_trial_count: _Optional[int] = ...) -> None: ...
        class TrainTrialSpec(_message.Message):
            __slots__ = ("train_trial_job_spec", "max_parallel_trial_count", "frequency")
            TRAIN_TRIAL_JOB_SPEC_FIELD_NUMBER: _ClassVar[int]
            MAX_PARALLEL_TRIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
            FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            train_trial_job_spec: _custom_job_pb2.CustomJobSpec
            max_parallel_trial_count: int
            frequency: int
            def __init__(self, train_trial_job_spec: _Optional[_Union[_custom_job_pb2.CustomJobSpec, _Mapping]] = ..., max_parallel_trial_count: _Optional[int] = ..., frequency: _Optional[int] = ...) -> None: ...
        MULTI_TRIAL_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        METRIC_FIELD_NUMBER: _ClassVar[int]
        SEARCH_TRIAL_SPEC_FIELD_NUMBER: _ClassVar[int]
        TRAIN_TRIAL_SPEC_FIELD_NUMBER: _ClassVar[int]
        multi_trial_algorithm: NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm
        metric: NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec
        search_trial_spec: NasJobSpec.MultiTrialAlgorithmSpec.SearchTrialSpec
        train_trial_spec: NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec
        def __init__(self, multi_trial_algorithm: _Optional[_Union[NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm, str]] = ..., metric: _Optional[_Union[NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec, _Mapping]] = ..., search_trial_spec: _Optional[_Union[NasJobSpec.MultiTrialAlgorithmSpec.SearchTrialSpec, _Mapping]] = ..., train_trial_spec: _Optional[_Union[NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec, _Mapping]] = ...) -> None: ...
    MULTI_TRIAL_ALGORITHM_SPEC_FIELD_NUMBER: _ClassVar[int]
    RESUME_NAS_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SPACE_SPEC_FIELD_NUMBER: _ClassVar[int]
    multi_trial_algorithm_spec: NasJobSpec.MultiTrialAlgorithmSpec
    resume_nas_job_id: str
    search_space_spec: str
    def __init__(self, multi_trial_algorithm_spec: _Optional[_Union[NasJobSpec.MultiTrialAlgorithmSpec, _Mapping]] = ..., resume_nas_job_id: _Optional[str] = ..., search_space_spec: _Optional[str] = ...) -> None: ...

class NasJobOutput(_message.Message):
    __slots__ = ("multi_trial_job_output",)
    class MultiTrialJobOutput(_message.Message):
        __slots__ = ("search_trials", "train_trials")
        SEARCH_TRIALS_FIELD_NUMBER: _ClassVar[int]
        TRAIN_TRIALS_FIELD_NUMBER: _ClassVar[int]
        search_trials: _containers.RepeatedCompositeFieldContainer[NasTrial]
        train_trials: _containers.RepeatedCompositeFieldContainer[NasTrial]
        def __init__(self, search_trials: _Optional[_Iterable[_Union[NasTrial, _Mapping]]] = ..., train_trials: _Optional[_Iterable[_Union[NasTrial, _Mapping]]] = ...) -> None: ...
    MULTI_TRIAL_JOB_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    multi_trial_job_output: NasJobOutput.MultiTrialJobOutput
    def __init__(self, multi_trial_job_output: _Optional[_Union[NasJobOutput.MultiTrialJobOutput, _Mapping]] = ...) -> None: ...

class NasTrial(_message.Message):
    __slots__ = ("id", "state", "final_measurement", "start_time", "end_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[NasTrial.State]
        REQUESTED: _ClassVar[NasTrial.State]
        ACTIVE: _ClassVar[NasTrial.State]
        STOPPING: _ClassVar[NasTrial.State]
        SUCCEEDED: _ClassVar[NasTrial.State]
        INFEASIBLE: _ClassVar[NasTrial.State]
    STATE_UNSPECIFIED: NasTrial.State
    REQUESTED: NasTrial.State
    ACTIVE: NasTrial.State
    STOPPING: NasTrial.State
    SUCCEEDED: NasTrial.State
    INFEASIBLE: NasTrial.State
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FINAL_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    state: NasTrial.State
    final_measurement: _study_pb2.Measurement
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., state: _Optional[_Union[NasTrial.State, str]] = ..., final_measurement: _Optional[_Union[_study_pb2.Measurement, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
