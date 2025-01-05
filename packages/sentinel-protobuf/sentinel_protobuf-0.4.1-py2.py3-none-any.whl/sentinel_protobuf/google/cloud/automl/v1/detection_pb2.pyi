from google.cloud.automl.v1 import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImageObjectDetectionAnnotation(_message.Message):
    __slots__ = ('bounding_box', 'score')
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    bounding_box: _geometry_pb2.BoundingPoly
    score: float

    def __init__(self, bounding_box: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., score: _Optional[float]=...) -> None:
        ...

class BoundingBoxMetricsEntry(_message.Message):
    __slots__ = ('iou_threshold', 'mean_average_precision', 'confidence_metrics_entries')

    class ConfidenceMetricsEntry(_message.Message):
        __slots__ = ('confidence_threshold', 'recall', 'precision', 'f1_score')
        CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        RECALL_FIELD_NUMBER: _ClassVar[int]
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_FIELD_NUMBER: _ClassVar[int]
        confidence_threshold: float
        recall: float
        precision: float
        f1_score: float

        def __init__(self, confidence_threshold: _Optional[float]=..., recall: _Optional[float]=..., precision: _Optional[float]=..., f1_score: _Optional[float]=...) -> None:
            ...
    IOU_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MEAN_AVERAGE_PRECISION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_METRICS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    iou_threshold: float
    mean_average_precision: float
    confidence_metrics_entries: _containers.RepeatedCompositeFieldContainer[BoundingBoxMetricsEntry.ConfidenceMetricsEntry]

    def __init__(self, iou_threshold: _Optional[float]=..., mean_average_precision: _Optional[float]=..., confidence_metrics_entries: _Optional[_Iterable[_Union[BoundingBoxMetricsEntry.ConfidenceMetricsEntry, _Mapping]]]=...) -> None:
        ...

class ImageObjectDetectionEvaluationMetrics(_message.Message):
    __slots__ = ('evaluated_bounding_box_count', 'bounding_box_metrics_entries', 'bounding_box_mean_average_precision')
    EVALUATED_BOUNDING_BOX_COUNT_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_METRICS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_MEAN_AVERAGE_PRECISION_FIELD_NUMBER: _ClassVar[int]
    evaluated_bounding_box_count: int
    bounding_box_metrics_entries: _containers.RepeatedCompositeFieldContainer[BoundingBoxMetricsEntry]
    bounding_box_mean_average_precision: float

    def __init__(self, evaluated_bounding_box_count: _Optional[int]=..., bounding_box_metrics_entries: _Optional[_Iterable[_Union[BoundingBoxMetricsEntry, _Mapping]]]=..., bounding_box_mean_average_precision: _Optional[float]=...) -> None:
        ...