from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import custom_tuning_model_pb2 as _custom_tuning_model_pb2
from google.cloud.discoveryengine.v1 import import_config_pb2 as _import_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCustomModelsRequest(_message.Message):
    __slots__ = ("data_store",)
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    data_store: str
    def __init__(self, data_store: _Optional[str] = ...) -> None: ...

class ListCustomModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_custom_tuning_model_pb2.CustomTuningModel]
    def __init__(self, models: _Optional[_Iterable[_Union[_custom_tuning_model_pb2.CustomTuningModel, _Mapping]]] = ...) -> None: ...

class TrainCustomModelRequest(_message.Message):
    __slots__ = ("gcs_training_input", "data_store", "model_type", "error_config", "model_id")
    class GcsTrainingInput(_message.Message):
        __slots__ = ("corpus_data_path", "query_data_path", "train_data_path", "test_data_path")
        CORPUS_DATA_PATH_FIELD_NUMBER: _ClassVar[int]
        QUERY_DATA_PATH_FIELD_NUMBER: _ClassVar[int]
        TRAIN_DATA_PATH_FIELD_NUMBER: _ClassVar[int]
        TEST_DATA_PATH_FIELD_NUMBER: _ClassVar[int]
        corpus_data_path: str
        query_data_path: str
        train_data_path: str
        test_data_path: str
        def __init__(self, corpus_data_path: _Optional[str] = ..., query_data_path: _Optional[str] = ..., train_data_path: _Optional[str] = ..., test_data_path: _Optional[str] = ...) -> None: ...
    GCS_TRAINING_INPUT_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    gcs_training_input: TrainCustomModelRequest.GcsTrainingInput
    data_store: str
    model_type: str
    error_config: _import_config_pb2.ImportErrorConfig
    model_id: str
    def __init__(self, gcs_training_input: _Optional[_Union[TrainCustomModelRequest.GcsTrainingInput, _Mapping]] = ..., data_store: _Optional[str] = ..., model_type: _Optional[str] = ..., error_config: _Optional[_Union[_import_config_pb2.ImportErrorConfig, _Mapping]] = ..., model_id: _Optional[str] = ...) -> None: ...

class TrainCustomModelResponse(_message.Message):
    __slots__ = ("error_samples", "error_config", "model_status", "metrics", "model_name")
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODEL_STATUS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    error_config: _import_config_pb2.ImportErrorConfig
    model_status: str
    metrics: _containers.ScalarMap[str, float]
    model_name: str
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., error_config: _Optional[_Union[_import_config_pb2.ImportErrorConfig, _Mapping]] = ..., model_status: _Optional[str] = ..., metrics: _Optional[_Mapping[str, float]] = ..., model_name: _Optional[str] = ...) -> None: ...

class TrainCustomModelMetadata(_message.Message):
    __slots__ = ("create_time", "update_time")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
