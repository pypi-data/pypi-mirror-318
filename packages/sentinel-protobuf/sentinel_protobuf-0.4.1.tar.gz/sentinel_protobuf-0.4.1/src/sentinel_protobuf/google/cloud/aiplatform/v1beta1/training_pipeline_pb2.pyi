from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import model_pb2 as _model_pb2
from google.cloud.aiplatform.v1beta1 import pipeline_state_pb2 as _pipeline_state_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrainingPipeline(_message.Message):
    __slots__ = ("name", "display_name", "input_data_config", "training_task_definition", "training_task_inputs", "training_task_metadata", "model_to_upload", "model_id", "parent_model", "state", "error", "create_time", "start_time", "end_time", "update_time", "labels", "encryption_spec")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRAINING_TASK_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    TRAINING_TASK_INPUTS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_TASK_METADATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_TO_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    input_data_config: InputDataConfig
    training_task_definition: str
    training_task_inputs: _struct_pb2.Value
    training_task_metadata: _struct_pb2.Value
    model_to_upload: _model_pb2.Model
    model_id: str
    parent_model: str
    state: _pipeline_state_pb2.PipelineState
    error: _status_pb2.Status
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., input_data_config: _Optional[_Union[InputDataConfig, _Mapping]] = ..., training_task_definition: _Optional[str] = ..., training_task_inputs: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., training_task_metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., model_to_upload: _Optional[_Union[_model_pb2.Model, _Mapping]] = ..., model_id: _Optional[str] = ..., parent_model: _Optional[str] = ..., state: _Optional[_Union[_pipeline_state_pb2.PipelineState, str]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]] = ...) -> None: ...

class InputDataConfig(_message.Message):
    __slots__ = ("fraction_split", "filter_split", "predefined_split", "timestamp_split", "stratified_split", "gcs_destination", "bigquery_destination", "dataset_id", "annotations_filter", "annotation_schema_uri", "saved_query_id", "persist_ml_use_assignment")
    FRACTION_SPLIT_FIELD_NUMBER: _ClassVar[int]
    FILTER_SPLIT_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_SPLIT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SPLIT_FIELD_NUMBER: _ClassVar[int]
    STRATIFIED_SPLIT_FIELD_NUMBER: _ClassVar[int]
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FILTER_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    SAVED_QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    PERSIST_ML_USE_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    fraction_split: FractionSplit
    filter_split: FilterSplit
    predefined_split: PredefinedSplit
    timestamp_split: TimestampSplit
    stratified_split: StratifiedSplit
    gcs_destination: _io_pb2.GcsDestination
    bigquery_destination: _io_pb2.BigQueryDestination
    dataset_id: str
    annotations_filter: str
    annotation_schema_uri: str
    saved_query_id: str
    persist_ml_use_assignment: bool
    def __init__(self, fraction_split: _Optional[_Union[FractionSplit, _Mapping]] = ..., filter_split: _Optional[_Union[FilterSplit, _Mapping]] = ..., predefined_split: _Optional[_Union[PredefinedSplit, _Mapping]] = ..., timestamp_split: _Optional[_Union[TimestampSplit, _Mapping]] = ..., stratified_split: _Optional[_Union[StratifiedSplit, _Mapping]] = ..., gcs_destination: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]] = ..., bigquery_destination: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]] = ..., dataset_id: _Optional[str] = ..., annotations_filter: _Optional[str] = ..., annotation_schema_uri: _Optional[str] = ..., saved_query_id: _Optional[str] = ..., persist_ml_use_assignment: bool = ...) -> None: ...

class FractionSplit(_message.Message):
    __slots__ = ("training_fraction", "validation_fraction", "test_fraction")
    TRAINING_FRACTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FRACTION_FIELD_NUMBER: _ClassVar[int]
    TEST_FRACTION_FIELD_NUMBER: _ClassVar[int]
    training_fraction: float
    validation_fraction: float
    test_fraction: float
    def __init__(self, training_fraction: _Optional[float] = ..., validation_fraction: _Optional[float] = ..., test_fraction: _Optional[float] = ...) -> None: ...

class FilterSplit(_message.Message):
    __slots__ = ("training_filter", "validation_filter", "test_filter")
    TRAINING_FILTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    TEST_FILTER_FIELD_NUMBER: _ClassVar[int]
    training_filter: str
    validation_filter: str
    test_filter: str
    def __init__(self, training_filter: _Optional[str] = ..., validation_filter: _Optional[str] = ..., test_filter: _Optional[str] = ...) -> None: ...

class PredefinedSplit(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class TimestampSplit(_message.Message):
    __slots__ = ("training_fraction", "validation_fraction", "test_fraction", "key")
    TRAINING_FRACTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FRACTION_FIELD_NUMBER: _ClassVar[int]
    TEST_FRACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    training_fraction: float
    validation_fraction: float
    test_fraction: float
    key: str
    def __init__(self, training_fraction: _Optional[float] = ..., validation_fraction: _Optional[float] = ..., test_fraction: _Optional[float] = ..., key: _Optional[str] = ...) -> None: ...

class StratifiedSplit(_message.Message):
    __slots__ = ("training_fraction", "validation_fraction", "test_fraction", "key")
    TRAINING_FRACTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FRACTION_FIELD_NUMBER: _ClassVar[int]
    TEST_FRACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    training_fraction: float
    validation_fraction: float
    test_fraction: float
    key: str
    def __init__(self, training_fraction: _Optional[float] = ..., validation_fraction: _Optional[float] = ..., test_fraction: _Optional[float] = ..., key: _Optional[str] = ...) -> None: ...
