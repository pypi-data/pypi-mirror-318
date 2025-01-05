from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as _job_state_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataLabelingJob(_message.Message):
    __slots__ = ('name', 'display_name', 'datasets', 'annotation_labels', 'labeler_count', 'instruction_uri', 'inputs_schema_uri', 'inputs', 'state', 'labeling_progress', 'current_spend', 'create_time', 'update_time', 'error', 'labels', 'specialist_pools', 'encryption_spec', 'active_learning_config')

    class AnnotationLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_LABELS_FIELD_NUMBER: _ClassVar[int]
    LABELER_COUNT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_URI_FIELD_NUMBER: _ClassVar[int]
    INPUTS_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELING_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SPEND_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SPECIALIST_POOLS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_LEARNING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    datasets: _containers.RepeatedScalarFieldContainer[str]
    annotation_labels: _containers.ScalarMap[str, str]
    labeler_count: int
    instruction_uri: str
    inputs_schema_uri: str
    inputs: _struct_pb2.Value
    state: _job_state_pb2.JobState
    labeling_progress: int
    current_spend: _money_pb2.Money
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    labels: _containers.ScalarMap[str, str]
    specialist_pools: _containers.RepeatedScalarFieldContainer[str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    active_learning_config: ActiveLearningConfig

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., datasets: _Optional[_Iterable[str]]=..., annotation_labels: _Optional[_Mapping[str, str]]=..., labeler_count: _Optional[int]=..., instruction_uri: _Optional[str]=..., inputs_schema_uri: _Optional[str]=..., inputs: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., state: _Optional[_Union[_job_state_pb2.JobState, str]]=..., labeling_progress: _Optional[int]=..., current_spend: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., specialist_pools: _Optional[_Iterable[str]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., active_learning_config: _Optional[_Union[ActiveLearningConfig, _Mapping]]=...) -> None:
        ...

class ActiveLearningConfig(_message.Message):
    __slots__ = ('max_data_item_count', 'max_data_item_percentage', 'sample_config', 'training_config')
    MAX_DATA_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_DATA_ITEM_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRAINING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    max_data_item_count: int
    max_data_item_percentage: int
    sample_config: SampleConfig
    training_config: TrainingConfig

    def __init__(self, max_data_item_count: _Optional[int]=..., max_data_item_percentage: _Optional[int]=..., sample_config: _Optional[_Union[SampleConfig, _Mapping]]=..., training_config: _Optional[_Union[TrainingConfig, _Mapping]]=...) -> None:
        ...

class SampleConfig(_message.Message):
    __slots__ = ('initial_batch_sample_percentage', 'following_batch_sample_percentage', 'sample_strategy')

    class SampleStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAMPLE_STRATEGY_UNSPECIFIED: _ClassVar[SampleConfig.SampleStrategy]
        UNCERTAINTY: _ClassVar[SampleConfig.SampleStrategy]
    SAMPLE_STRATEGY_UNSPECIFIED: SampleConfig.SampleStrategy
    UNCERTAINTY: SampleConfig.SampleStrategy
    INITIAL_BATCH_SAMPLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_BATCH_SAMPLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    initial_batch_sample_percentage: int
    following_batch_sample_percentage: int
    sample_strategy: SampleConfig.SampleStrategy

    def __init__(self, initial_batch_sample_percentage: _Optional[int]=..., following_batch_sample_percentage: _Optional[int]=..., sample_strategy: _Optional[_Union[SampleConfig.SampleStrategy, str]]=...) -> None:
        ...

class TrainingConfig(_message.Message):
    __slots__ = ('timeout_training_milli_hours',)
    TIMEOUT_TRAINING_MILLI_HOURS_FIELD_NUMBER: _ClassVar[int]
    timeout_training_milli_hours: int

    def __init__(self, timeout_training_milli_hours: _Optional[int]=...) -> None:
        ...