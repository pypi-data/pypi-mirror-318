from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TunedModel(_message.Message):
    __slots__ = ("tuned_model_source", "base_model", "name", "display_name", "description", "temperature", "top_p", "top_k", "state", "create_time", "update_time", "tuning_task", "reader_project_numbers")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[TunedModel.State]
        CREATING: _ClassVar[TunedModel.State]
        ACTIVE: _ClassVar[TunedModel.State]
        FAILED: _ClassVar[TunedModel.State]
    STATE_UNSPECIFIED: TunedModel.State
    CREATING: TunedModel.State
    ACTIVE: TunedModel.State
    FAILED: TunedModel.State
    TUNED_MODEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TUNING_TASK_FIELD_NUMBER: _ClassVar[int]
    READER_PROJECT_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    tuned_model_source: TunedModelSource
    base_model: str
    name: str
    display_name: str
    description: str
    temperature: float
    top_p: float
    top_k: int
    state: TunedModel.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    tuning_task: TuningTask
    reader_project_numbers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tuned_model_source: _Optional[_Union[TunedModelSource, _Mapping]] = ..., base_model: _Optional[str] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ..., state: _Optional[_Union[TunedModel.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tuning_task: _Optional[_Union[TuningTask, _Mapping]] = ..., reader_project_numbers: _Optional[_Iterable[int]] = ...) -> None: ...

class TunedModelSource(_message.Message):
    __slots__ = ("tuned_model", "base_model")
    TUNED_MODEL_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    tuned_model: str
    base_model: str
    def __init__(self, tuned_model: _Optional[str] = ..., base_model: _Optional[str] = ...) -> None: ...

class TuningTask(_message.Message):
    __slots__ = ("start_time", "complete_time", "snapshots", "training_data", "hyperparameters")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DATA_FIELD_NUMBER: _ClassVar[int]
    HYPERPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    complete_time: _timestamp_pb2.Timestamp
    snapshots: _containers.RepeatedCompositeFieldContainer[TuningSnapshot]
    training_data: Dataset
    hyperparameters: Hyperparameters
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., snapshots: _Optional[_Iterable[_Union[TuningSnapshot, _Mapping]]] = ..., training_data: _Optional[_Union[Dataset, _Mapping]] = ..., hyperparameters: _Optional[_Union[Hyperparameters, _Mapping]] = ...) -> None: ...

class Hyperparameters(_message.Message):
    __slots__ = ("learning_rate", "learning_rate_multiplier", "epoch_count", "batch_size")
    LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    EPOCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    learning_rate: float
    learning_rate_multiplier: float
    epoch_count: int
    batch_size: int
    def __init__(self, learning_rate: _Optional[float] = ..., learning_rate_multiplier: _Optional[float] = ..., epoch_count: _Optional[int] = ..., batch_size: _Optional[int] = ...) -> None: ...

class Dataset(_message.Message):
    __slots__ = ("examples",)
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: TuningExamples
    def __init__(self, examples: _Optional[_Union[TuningExamples, _Mapping]] = ...) -> None: ...

class TuningExamples(_message.Message):
    __slots__ = ("examples",)
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[TuningExample]
    def __init__(self, examples: _Optional[_Iterable[_Union[TuningExample, _Mapping]]] = ...) -> None: ...

class TuningExample(_message.Message):
    __slots__ = ("text_input", "output")
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    text_input: str
    output: str
    def __init__(self, text_input: _Optional[str] = ..., output: _Optional[str] = ...) -> None: ...

class TuningSnapshot(_message.Message):
    __slots__ = ("step", "epoch", "mean_loss", "compute_time")
    STEP_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    MEAN_LOSS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    step: int
    epoch: int
    mean_loss: float
    compute_time: _timestamp_pb2.Timestamp
    def __init__(self, step: _Optional[int] = ..., epoch: _Optional[int] = ..., mean_loss: _Optional[float] = ..., compute_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
