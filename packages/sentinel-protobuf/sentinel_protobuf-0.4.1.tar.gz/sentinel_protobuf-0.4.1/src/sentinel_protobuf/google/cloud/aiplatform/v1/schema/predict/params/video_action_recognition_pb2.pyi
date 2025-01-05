from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class VideoActionRecognitionPredictionParams(_message.Message):
    __slots__ = ('confidence_threshold', 'max_predictions')
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    confidence_threshold: float
    max_predictions: int

    def __init__(self, confidence_threshold: _Optional[float]=..., max_predictions: _Optional[int]=...) -> None:
        ...