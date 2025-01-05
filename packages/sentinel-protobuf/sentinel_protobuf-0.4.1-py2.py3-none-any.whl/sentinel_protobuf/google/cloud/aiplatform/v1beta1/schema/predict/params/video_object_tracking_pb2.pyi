from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class VideoObjectTrackingPredictionParams(_message.Message):
    __slots__ = ('confidence_threshold', 'max_predictions', 'min_bounding_box_size')
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    MIN_BOUNDING_BOX_SIZE_FIELD_NUMBER: _ClassVar[int]
    confidence_threshold: float
    max_predictions: int
    min_bounding_box_size: float

    def __init__(self, confidence_threshold: _Optional[float]=..., max_predictions: _Optional[int]=..., min_bounding_box_size: _Optional[float]=...) -> None:
        ...