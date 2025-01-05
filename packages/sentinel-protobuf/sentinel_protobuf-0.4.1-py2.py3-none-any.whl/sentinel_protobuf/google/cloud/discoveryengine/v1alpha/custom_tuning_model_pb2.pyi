from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomTuningModel(_message.Message):
    __slots__ = ('name', 'display_name', 'model_version', 'model_state', 'create_time', 'training_start_time', 'metrics')

    class ModelState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_STATE_UNSPECIFIED: _ClassVar[CustomTuningModel.ModelState]
        TRAINING_PAUSED: _ClassVar[CustomTuningModel.ModelState]
        TRAINING: _ClassVar[CustomTuningModel.ModelState]
        TRAINING_COMPLETE: _ClassVar[CustomTuningModel.ModelState]
        READY_FOR_SERVING: _ClassVar[CustomTuningModel.ModelState]
        TRAINING_FAILED: _ClassVar[CustomTuningModel.ModelState]
        NO_IMPROVEMENT: _ClassVar[CustomTuningModel.ModelState]
        INPUT_VALIDATION_FAILED: _ClassVar[CustomTuningModel.ModelState]
    MODEL_STATE_UNSPECIFIED: CustomTuningModel.ModelState
    TRAINING_PAUSED: CustomTuningModel.ModelState
    TRAINING: CustomTuningModel.ModelState
    TRAINING_COMPLETE: CustomTuningModel.ModelState
    READY_FOR_SERVING: CustomTuningModel.ModelState
    TRAINING_FAILED: CustomTuningModel.ModelState
    NO_IMPROVEMENT: CustomTuningModel.ModelState
    INPUT_VALIDATION_FAILED: CustomTuningModel.ModelState

    class MetricsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float

        def __init__(self, key: _Optional[str]=..., value: _Optional[float]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TRAINING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    model_version: int
    model_state: CustomTuningModel.ModelState
    create_time: _timestamp_pb2.Timestamp
    training_start_time: _timestamp_pb2.Timestamp
    metrics: _containers.ScalarMap[str, float]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., model_version: _Optional[int]=..., model_state: _Optional[_Union[CustomTuningModel.ModelState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., training_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., metrics: _Optional[_Mapping[str, float]]=...) -> None:
        ...