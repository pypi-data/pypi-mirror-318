from google.api import resource_pb2 as _resource_pb2
from google.cloud.datalabeling.v1beta1 import annotation_pb2 as _annotation_pb2
from google.cloud.datalabeling.v1beta1 import annotation_spec_set_pb2 as _annotation_spec_set_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Evaluation(_message.Message):
    __slots__ = ('name', 'config', 'evaluation_job_run_time', 'create_time', 'evaluation_metrics', 'annotation_type', 'evaluated_item_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_JOB_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: EvaluationConfig
    evaluation_job_run_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    evaluation_metrics: EvaluationMetrics
    annotation_type: _annotation_pb2.AnnotationType
    evaluated_item_count: int

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[EvaluationConfig, _Mapping]]=..., evaluation_job_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., evaluation_metrics: _Optional[_Union[EvaluationMetrics, _Mapping]]=..., annotation_type: _Optional[_Union[_annotation_pb2.AnnotationType, str]]=..., evaluated_item_count: _Optional[int]=...) -> None:
        ...

class EvaluationConfig(_message.Message):
    __slots__ = ('bounding_box_evaluation_options',)
    BOUNDING_BOX_EVALUATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    bounding_box_evaluation_options: BoundingBoxEvaluationOptions

    def __init__(self, bounding_box_evaluation_options: _Optional[_Union[BoundingBoxEvaluationOptions, _Mapping]]=...) -> None:
        ...

class BoundingBoxEvaluationOptions(_message.Message):
    __slots__ = ('iou_threshold',)
    IOU_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    iou_threshold: float

    def __init__(self, iou_threshold: _Optional[float]=...) -> None:
        ...

class EvaluationMetrics(_message.Message):
    __slots__ = ('classification_metrics', 'object_detection_metrics')
    CLASSIFICATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DETECTION_METRICS_FIELD_NUMBER: _ClassVar[int]
    classification_metrics: ClassificationMetrics
    object_detection_metrics: ObjectDetectionMetrics

    def __init__(self, classification_metrics: _Optional[_Union[ClassificationMetrics, _Mapping]]=..., object_detection_metrics: _Optional[_Union[ObjectDetectionMetrics, _Mapping]]=...) -> None:
        ...

class ClassificationMetrics(_message.Message):
    __slots__ = ('pr_curve', 'confusion_matrix')
    PR_CURVE_FIELD_NUMBER: _ClassVar[int]
    CONFUSION_MATRIX_FIELD_NUMBER: _ClassVar[int]
    pr_curve: PrCurve
    confusion_matrix: ConfusionMatrix

    def __init__(self, pr_curve: _Optional[_Union[PrCurve, _Mapping]]=..., confusion_matrix: _Optional[_Union[ConfusionMatrix, _Mapping]]=...) -> None:
        ...

class ObjectDetectionMetrics(_message.Message):
    __slots__ = ('pr_curve',)
    PR_CURVE_FIELD_NUMBER: _ClassVar[int]
    pr_curve: PrCurve

    def __init__(self, pr_curve: _Optional[_Union[PrCurve, _Mapping]]=...) -> None:
        ...

class PrCurve(_message.Message):
    __slots__ = ('annotation_spec', 'area_under_curve', 'confidence_metrics_entries', 'mean_average_precision')

    class ConfidenceMetricsEntry(_message.Message):
        __slots__ = ('confidence_threshold', 'recall', 'precision', 'f1_score', 'recall_at1', 'precision_at1', 'f1_score_at1', 'recall_at5', 'precision_at5', 'f1_score_at5')
        CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        RECALL_FIELD_NUMBER: _ClassVar[int]
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_FIELD_NUMBER: _ClassVar[int]
        RECALL_AT1_FIELD_NUMBER: _ClassVar[int]
        PRECISION_AT1_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_AT1_FIELD_NUMBER: _ClassVar[int]
        RECALL_AT5_FIELD_NUMBER: _ClassVar[int]
        PRECISION_AT5_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_AT5_FIELD_NUMBER: _ClassVar[int]
        confidence_threshold: float
        recall: float
        precision: float
        f1_score: float
        recall_at1: float
        precision_at1: float
        f1_score_at1: float
        recall_at5: float
        precision_at5: float
        f1_score_at5: float

        def __init__(self, confidence_threshold: _Optional[float]=..., recall: _Optional[float]=..., precision: _Optional[float]=..., f1_score: _Optional[float]=..., recall_at1: _Optional[float]=..., precision_at1: _Optional[float]=..., f1_score_at1: _Optional[float]=..., recall_at5: _Optional[float]=..., precision_at5: _Optional[float]=..., f1_score_at5: _Optional[float]=...) -> None:
            ...
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    AREA_UNDER_CURVE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_METRICS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MEAN_AVERAGE_PRECISION_FIELD_NUMBER: _ClassVar[int]
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec
    area_under_curve: float
    confidence_metrics_entries: _containers.RepeatedCompositeFieldContainer[PrCurve.ConfidenceMetricsEntry]
    mean_average_precision: float

    def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=..., area_under_curve: _Optional[float]=..., confidence_metrics_entries: _Optional[_Iterable[_Union[PrCurve.ConfidenceMetricsEntry, _Mapping]]]=..., mean_average_precision: _Optional[float]=...) -> None:
        ...

class ConfusionMatrix(_message.Message):
    __slots__ = ('row',)

    class ConfusionMatrixEntry(_message.Message):
        __slots__ = ('annotation_spec', 'item_count')
        ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
        ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
        annotation_spec: _annotation_spec_set_pb2.AnnotationSpec
        item_count: int

        def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=..., item_count: _Optional[int]=...) -> None:
            ...

    class Row(_message.Message):
        __slots__ = ('annotation_spec', 'entries')
        ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        annotation_spec: _annotation_spec_set_pb2.AnnotationSpec
        entries: _containers.RepeatedCompositeFieldContainer[ConfusionMatrix.ConfusionMatrixEntry]

        def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=..., entries: _Optional[_Iterable[_Union[ConfusionMatrix.ConfusionMatrixEntry, _Mapping]]]=...) -> None:
            ...
    ROW_FIELD_NUMBER: _ClassVar[int]
    row: _containers.RepeatedCompositeFieldContainer[ConfusionMatrix.Row]

    def __init__(self, row: _Optional[_Iterable[_Union[ConfusionMatrix.Row, _Mapping]]]=...) -> None:
        ...