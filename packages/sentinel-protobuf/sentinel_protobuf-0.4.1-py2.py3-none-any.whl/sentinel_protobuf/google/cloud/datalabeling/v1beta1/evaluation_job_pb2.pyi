from google.api import resource_pb2 as _resource_pb2
from google.cloud.datalabeling.v1beta1 import dataset_pb2 as _dataset_pb2
from google.cloud.datalabeling.v1beta1 import evaluation_pb2 as _evaluation_pb2
from google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as _human_annotation_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EvaluationJob(_message.Message):
    __slots__ = ('name', 'description', 'state', 'schedule', 'model_version', 'evaluation_job_config', 'annotation_spec_set', 'label_missing_ground_truth', 'attempts', 'create_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[EvaluationJob.State]
        SCHEDULED: _ClassVar[EvaluationJob.State]
        RUNNING: _ClassVar[EvaluationJob.State]
        PAUSED: _ClassVar[EvaluationJob.State]
        STOPPED: _ClassVar[EvaluationJob.State]
    STATE_UNSPECIFIED: EvaluationJob.State
    SCHEDULED: EvaluationJob.State
    RUNNING: EvaluationJob.State
    PAUSED: EvaluationJob.State
    STOPPED: EvaluationJob.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_JOB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    LABEL_MISSING_GROUND_TRUTH_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    state: EvaluationJob.State
    schedule: str
    model_version: str
    evaluation_job_config: EvaluationJobConfig
    annotation_spec_set: str
    label_missing_ground_truth: bool
    attempts: _containers.RepeatedCompositeFieldContainer[Attempt]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[EvaluationJob.State, str]]=..., schedule: _Optional[str]=..., model_version: _Optional[str]=..., evaluation_job_config: _Optional[_Union[EvaluationJobConfig, _Mapping]]=..., annotation_spec_set: _Optional[str]=..., label_missing_ground_truth: bool=..., attempts: _Optional[_Iterable[_Union[Attempt, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class EvaluationJobConfig(_message.Message):
    __slots__ = ('image_classification_config', 'bounding_poly_config', 'text_classification_config', 'input_config', 'evaluation_config', 'human_annotation_config', 'bigquery_import_keys', 'example_count', 'example_sample_percentage', 'evaluation_job_alert_config')

    class BigqueryImportKeysEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    IMAGE_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_POLY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HUMAN_ANNOTATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_IMPORT_KEYS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_SAMPLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_JOB_ALERT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    image_classification_config: _human_annotation_config_pb2.ImageClassificationConfig
    bounding_poly_config: _human_annotation_config_pb2.BoundingPolyConfig
    text_classification_config: _human_annotation_config_pb2.TextClassificationConfig
    input_config: _dataset_pb2.InputConfig
    evaluation_config: _evaluation_pb2.EvaluationConfig
    human_annotation_config: _human_annotation_config_pb2.HumanAnnotationConfig
    bigquery_import_keys: _containers.ScalarMap[str, str]
    example_count: int
    example_sample_percentage: float
    evaluation_job_alert_config: EvaluationJobAlertConfig

    def __init__(self, image_classification_config: _Optional[_Union[_human_annotation_config_pb2.ImageClassificationConfig, _Mapping]]=..., bounding_poly_config: _Optional[_Union[_human_annotation_config_pb2.BoundingPolyConfig, _Mapping]]=..., text_classification_config: _Optional[_Union[_human_annotation_config_pb2.TextClassificationConfig, _Mapping]]=..., input_config: _Optional[_Union[_dataset_pb2.InputConfig, _Mapping]]=..., evaluation_config: _Optional[_Union[_evaluation_pb2.EvaluationConfig, _Mapping]]=..., human_annotation_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=..., bigquery_import_keys: _Optional[_Mapping[str, str]]=..., example_count: _Optional[int]=..., example_sample_percentage: _Optional[float]=..., evaluation_job_alert_config: _Optional[_Union[EvaluationJobAlertConfig, _Mapping]]=...) -> None:
        ...

class EvaluationJobAlertConfig(_message.Message):
    __slots__ = ('email', 'min_acceptable_mean_average_precision')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MIN_ACCEPTABLE_MEAN_AVERAGE_PRECISION_FIELD_NUMBER: _ClassVar[int]
    email: str
    min_acceptable_mean_average_precision: float

    def __init__(self, email: _Optional[str]=..., min_acceptable_mean_average_precision: _Optional[float]=...) -> None:
        ...

class Attempt(_message.Message):
    __slots__ = ('attempt_time', 'partial_failures')
    ATTEMPT_TIME_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    attempt_time: _timestamp_pb2.Timestamp
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, attempt_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...