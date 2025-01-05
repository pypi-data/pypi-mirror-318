from google.cloud.automl.v1beta1 import classification_pb2 as _classification_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TextSentimentAnnotation(_message.Message):
    __slots__ = ('sentiment',)
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    sentiment: int

    def __init__(self, sentiment: _Optional[int]=...) -> None:
        ...

class TextSentimentEvaluationMetrics(_message.Message):
    __slots__ = ('precision', 'recall', 'f1_score', 'mean_absolute_error', 'mean_squared_error', 'linear_kappa', 'quadratic_kappa', 'confusion_matrix', 'annotation_spec_id')
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    RECALL_FIELD_NUMBER: _ClassVar[int]
    F1_SCORE_FIELD_NUMBER: _ClassVar[int]
    MEAN_ABSOLUTE_ERROR_FIELD_NUMBER: _ClassVar[int]
    MEAN_SQUARED_ERROR_FIELD_NUMBER: _ClassVar[int]
    LINEAR_KAPPA_FIELD_NUMBER: _ClassVar[int]
    QUADRATIC_KAPPA_FIELD_NUMBER: _ClassVar[int]
    CONFUSION_MATRIX_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    precision: float
    recall: float
    f1_score: float
    mean_absolute_error: float
    mean_squared_error: float
    linear_kappa: float
    quadratic_kappa: float
    confusion_matrix: _classification_pb2.ClassificationEvaluationMetrics.ConfusionMatrix
    annotation_spec_id: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, precision: _Optional[float]=..., recall: _Optional[float]=..., f1_score: _Optional[float]=..., mean_absolute_error: _Optional[float]=..., mean_squared_error: _Optional[float]=..., linear_kappa: _Optional[float]=..., quadratic_kappa: _Optional[float]=..., confusion_matrix: _Optional[_Union[_classification_pb2.ClassificationEvaluationMetrics.ConfusionMatrix, _Mapping]]=..., annotation_spec_id: _Optional[_Iterable[str]]=...) -> None:
        ...