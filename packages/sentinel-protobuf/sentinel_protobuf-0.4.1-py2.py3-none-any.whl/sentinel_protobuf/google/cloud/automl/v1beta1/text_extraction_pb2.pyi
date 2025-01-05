from google.cloud.automl.v1beta1 import text_segment_pb2 as _text_segment_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TextExtractionAnnotation(_message.Message):
    __slots__ = ('text_segment', 'score')
    TEXT_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    text_segment: _text_segment_pb2.TextSegment
    score: float

    def __init__(self, text_segment: _Optional[_Union[_text_segment_pb2.TextSegment, _Mapping]]=..., score: _Optional[float]=...) -> None:
        ...

class TextExtractionEvaluationMetrics(_message.Message):
    __slots__ = ('au_prc', 'confidence_metrics_entries')

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
    AU_PRC_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_METRICS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    au_prc: float
    confidence_metrics_entries: _containers.RepeatedCompositeFieldContainer[TextExtractionEvaluationMetrics.ConfidenceMetricsEntry]

    def __init__(self, au_prc: _Optional[float]=..., confidence_metrics_entries: _Optional[_Iterable[_Union[TextExtractionEvaluationMetrics.ConfidenceMetricsEntry, _Mapping]]]=...) -> None:
        ...