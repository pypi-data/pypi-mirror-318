from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StringAggregationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRING_AGGREGATION_TYPE_UNSPECIFIED: _ClassVar[StringAggregationType]
    MAJORITY_VOTE: _ClassVar[StringAggregationType]
    UNANIMOUS_VOTE: _ClassVar[StringAggregationType]
    NO_AGGREGATION: _ClassVar[StringAggregationType]
STRING_AGGREGATION_TYPE_UNSPECIFIED: StringAggregationType
MAJORITY_VOTE: StringAggregationType
UNANIMOUS_VOTE: StringAggregationType
NO_AGGREGATION: StringAggregationType

class HumanAnnotationConfig(_message.Message):
    __slots__ = ('instruction', 'annotated_dataset_display_name', 'annotated_dataset_description', 'label_group', 'language_code', 'replica_count', 'question_duration', 'contributor_emails', 'user_email_address')
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_DATASET_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_DATASET_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTOR_EMAILS_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    instruction: str
    annotated_dataset_display_name: str
    annotated_dataset_description: str
    label_group: str
    language_code: str
    replica_count: int
    question_duration: _duration_pb2.Duration
    contributor_emails: _containers.RepeatedScalarFieldContainer[str]
    user_email_address: str

    def __init__(self, instruction: _Optional[str]=..., annotated_dataset_display_name: _Optional[str]=..., annotated_dataset_description: _Optional[str]=..., label_group: _Optional[str]=..., language_code: _Optional[str]=..., replica_count: _Optional[int]=..., question_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., contributor_emails: _Optional[_Iterable[str]]=..., user_email_address: _Optional[str]=...) -> None:
        ...

class ImageClassificationConfig(_message.Message):
    __slots__ = ('annotation_spec_set', 'allow_multi_label', 'answer_aggregation_type')
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MULTI_LABEL_FIELD_NUMBER: _ClassVar[int]
    ANSWER_AGGREGATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set: str
    allow_multi_label: bool
    answer_aggregation_type: StringAggregationType

    def __init__(self, annotation_spec_set: _Optional[str]=..., allow_multi_label: bool=..., answer_aggregation_type: _Optional[_Union[StringAggregationType, str]]=...) -> None:
        ...

class BoundingPolyConfig(_message.Message):
    __slots__ = ('annotation_spec_set', 'instruction_message')
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set: str
    instruction_message: str

    def __init__(self, annotation_spec_set: _Optional[str]=..., instruction_message: _Optional[str]=...) -> None:
        ...

class PolylineConfig(_message.Message):
    __slots__ = ('annotation_spec_set', 'instruction_message')
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set: str
    instruction_message: str

    def __init__(self, annotation_spec_set: _Optional[str]=..., instruction_message: _Optional[str]=...) -> None:
        ...

class SegmentationConfig(_message.Message):
    __slots__ = ('annotation_spec_set', 'instruction_message')
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set: str
    instruction_message: str

    def __init__(self, annotation_spec_set: _Optional[str]=..., instruction_message: _Optional[str]=...) -> None:
        ...

class VideoClassificationConfig(_message.Message):
    __slots__ = ('annotation_spec_set_configs', 'apply_shot_detection')

    class AnnotationSpecSetConfig(_message.Message):
        __slots__ = ('annotation_spec_set', 'allow_multi_label')
        ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MULTI_LABEL_FIELD_NUMBER: _ClassVar[int]
        annotation_spec_set: str
        allow_multi_label: bool

        def __init__(self, annotation_spec_set: _Optional[str]=..., allow_multi_label: bool=...) -> None:
            ...
    ANNOTATION_SPEC_SET_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    APPLY_SHOT_DETECTION_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set_configs: _containers.RepeatedCompositeFieldContainer[VideoClassificationConfig.AnnotationSpecSetConfig]
    apply_shot_detection: bool

    def __init__(self, annotation_spec_set_configs: _Optional[_Iterable[_Union[VideoClassificationConfig.AnnotationSpecSetConfig, _Mapping]]]=..., apply_shot_detection: bool=...) -> None:
        ...

class ObjectDetectionConfig(_message.Message):
    __slots__ = ('annotation_spec_set', 'extraction_frame_rate')
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    EXTRACTION_FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set: str
    extraction_frame_rate: float

    def __init__(self, annotation_spec_set: _Optional[str]=..., extraction_frame_rate: _Optional[float]=...) -> None:
        ...

class ObjectTrackingConfig(_message.Message):
    __slots__ = ('annotation_spec_set',)
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set: str

    def __init__(self, annotation_spec_set: _Optional[str]=...) -> None:
        ...

class EventConfig(_message.Message):
    __slots__ = ('annotation_spec_sets',)
    ANNOTATION_SPEC_SETS_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_sets: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, annotation_spec_sets: _Optional[_Iterable[str]]=...) -> None:
        ...

class TextClassificationConfig(_message.Message):
    __slots__ = ('allow_multi_label', 'annotation_spec_set', 'sentiment_config')
    ALLOW_MULTI_LABEL_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    allow_multi_label: bool
    annotation_spec_set: str
    sentiment_config: SentimentConfig

    def __init__(self, allow_multi_label: bool=..., annotation_spec_set: _Optional[str]=..., sentiment_config: _Optional[_Union[SentimentConfig, _Mapping]]=...) -> None:
        ...

class SentimentConfig(_message.Message):
    __slots__ = ('enable_label_sentiment_selection',)
    ENABLE_LABEL_SENTIMENT_SELECTION_FIELD_NUMBER: _ClassVar[int]
    enable_label_sentiment_selection: bool

    def __init__(self, enable_label_sentiment_selection: bool=...) -> None:
        ...

class TextEntityExtractionConfig(_message.Message):
    __slots__ = ('annotation_spec_set',)
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_set: str

    def __init__(self, annotation_spec_set: _Optional[str]=...) -> None:
        ...