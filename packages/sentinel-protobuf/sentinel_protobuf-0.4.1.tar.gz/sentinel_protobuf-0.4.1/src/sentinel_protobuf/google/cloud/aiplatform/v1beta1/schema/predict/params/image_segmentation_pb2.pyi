from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ImageSegmentationPredictionParams(_message.Message):
    __slots__ = ('confidence_threshold',)
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    confidence_threshold: float

    def __init__(self, confidence_threshold: _Optional[float]=...) -> None:
        ...