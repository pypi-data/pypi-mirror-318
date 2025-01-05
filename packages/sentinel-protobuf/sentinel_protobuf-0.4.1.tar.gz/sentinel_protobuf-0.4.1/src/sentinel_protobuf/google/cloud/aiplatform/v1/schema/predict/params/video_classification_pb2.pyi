from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class VideoClassificationPredictionParams(_message.Message):
    __slots__ = ('confidence_threshold', 'max_predictions', 'segment_classification', 'shot_classification', 'one_sec_interval_classification')
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    SHOT_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    ONE_SEC_INTERVAL_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    confidence_threshold: float
    max_predictions: int
    segment_classification: bool
    shot_classification: bool
    one_sec_interval_classification: bool

    def __init__(self, confidence_threshold: _Optional[float]=..., max_predictions: _Optional[int]=..., segment_classification: bool=..., shot_classification: bool=..., one_sec_interval_classification: bool=...) -> None:
        ...