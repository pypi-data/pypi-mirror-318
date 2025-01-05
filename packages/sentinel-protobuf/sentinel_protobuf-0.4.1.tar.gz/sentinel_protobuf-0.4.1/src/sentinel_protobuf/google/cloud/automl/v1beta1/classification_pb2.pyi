from google.cloud.automl.v1beta1 import temporal_pb2 as _temporal_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ClassificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLASSIFICATION_TYPE_UNSPECIFIED: _ClassVar[ClassificationType]
    MULTICLASS: _ClassVar[ClassificationType]
    MULTILABEL: _ClassVar[ClassificationType]
CLASSIFICATION_TYPE_UNSPECIFIED: ClassificationType
MULTICLASS: ClassificationType
MULTILABEL: ClassificationType

class ClassificationAnnotation(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class VideoClassificationAnnotation(_message.Message):
    __slots__ = ('type', 'classification_annotation', 'time_segment')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    type: str
    classification_annotation: ClassificationAnnotation
    time_segment: _temporal_pb2.TimeSegment

    def __init__(self, type: _Optional[str]=..., classification_annotation: _Optional[_Union[ClassificationAnnotation, _Mapping]]=..., time_segment: _Optional[_Union[_temporal_pb2.TimeSegment, _Mapping]]=...) -> None:
        ...

class ClassificationEvaluationMetrics(_message.Message):
    __slots__ = ('au_prc', 'base_au_prc', 'au_roc', 'log_loss', 'confidence_metrics_entry', 'confusion_matrix', 'annotation_spec_id')

    class ConfidenceMetricsEntry(_message.Message):
        __slots__ = ('confidence_threshold', 'position_threshold', 'recall', 'precision', 'false_positive_rate', 'f1_score', 'recall_at1', 'precision_at1', 'false_positive_rate_at1', 'f1_score_at1', 'true_positive_count', 'false_positive_count', 'false_negative_count', 'true_negative_count')
        CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        POSITION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        RECALL_FIELD_NUMBER: _ClassVar[int]
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        FALSE_POSITIVE_RATE_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_FIELD_NUMBER: _ClassVar[int]
        RECALL_AT1_FIELD_NUMBER: _ClassVar[int]
        PRECISION_AT1_FIELD_NUMBER: _ClassVar[int]
        FALSE_POSITIVE_RATE_AT1_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_AT1_FIELD_NUMBER: _ClassVar[int]
        TRUE_POSITIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        FALSE_POSITIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        FALSE_NEGATIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        TRUE_NEGATIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        confidence_threshold: float
        position_threshold: int
        recall: float
        precision: float
        false_positive_rate: float
        f1_score: float
        recall_at1: float
        precision_at1: float
        false_positive_rate_at1: float
        f1_score_at1: float
        true_positive_count: int
        false_positive_count: int
        false_negative_count: int
        true_negative_count: int

        def __init__(self, confidence_threshold: _Optional[float]=..., position_threshold: _Optional[int]=..., recall: _Optional[float]=..., precision: _Optional[float]=..., false_positive_rate: _Optional[float]=..., f1_score: _Optional[float]=..., recall_at1: _Optional[float]=..., precision_at1: _Optional[float]=..., false_positive_rate_at1: _Optional[float]=..., f1_score_at1: _Optional[float]=..., true_positive_count: _Optional[int]=..., false_positive_count: _Optional[int]=..., false_negative_count: _Optional[int]=..., true_negative_count: _Optional[int]=...) -> None:
            ...

    class ConfusionMatrix(_message.Message):
        __slots__ = ('annotation_spec_id', 'display_name', 'row')

        class Row(_message.Message):
            __slots__ = ('example_count',)
            EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
            example_count: _containers.RepeatedScalarFieldContainer[int]

            def __init__(self, example_count: _Optional[_Iterable[int]]=...) -> None:
                ...
        ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        ROW_FIELD_NUMBER: _ClassVar[int]
        annotation_spec_id: _containers.RepeatedScalarFieldContainer[str]
        display_name: _containers.RepeatedScalarFieldContainer[str]
        row: _containers.RepeatedCompositeFieldContainer[ClassificationEvaluationMetrics.ConfusionMatrix.Row]

        def __init__(self, annotation_spec_id: _Optional[_Iterable[str]]=..., display_name: _Optional[_Iterable[str]]=..., row: _Optional[_Iterable[_Union[ClassificationEvaluationMetrics.ConfusionMatrix.Row, _Mapping]]]=...) -> None:
            ...
    AU_PRC_FIELD_NUMBER: _ClassVar[int]
    BASE_AU_PRC_FIELD_NUMBER: _ClassVar[int]
    AU_ROC_FIELD_NUMBER: _ClassVar[int]
    LOG_LOSS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_METRICS_ENTRY_FIELD_NUMBER: _ClassVar[int]
    CONFUSION_MATRIX_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    au_prc: float
    base_au_prc: float
    au_roc: float
    log_loss: float
    confidence_metrics_entry: _containers.RepeatedCompositeFieldContainer[ClassificationEvaluationMetrics.ConfidenceMetricsEntry]
    confusion_matrix: ClassificationEvaluationMetrics.ConfusionMatrix
    annotation_spec_id: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, au_prc: _Optional[float]=..., base_au_prc: _Optional[float]=..., au_roc: _Optional[float]=..., log_loss: _Optional[float]=..., confidence_metrics_entry: _Optional[_Iterable[_Union[ClassificationEvaluationMetrics.ConfidenceMetricsEntry, _Mapping]]]=..., confusion_matrix: _Optional[_Union[ClassificationEvaluationMetrics.ConfusionMatrix, _Mapping]]=..., annotation_spec_id: _Optional[_Iterable[str]]=...) -> None:
        ...