from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ImageSegmentationPredictionResult(_message.Message):
    __slots__ = ('category_mask', 'confidence_mask')
    CATEGORY_MASK_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_MASK_FIELD_NUMBER: _ClassVar[int]
    category_mask: str
    confidence_mask: str

    def __init__(self, category_mask: _Optional[str]=..., confidence_mask: _Optional[str]=...) -> None:
        ...