from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class VideoActionRecognitionPredictionInstance(_message.Message):
    __slots__ = ('content', 'mime_type', 'time_segment_start', 'time_segment_end')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_START_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_END_FIELD_NUMBER: _ClassVar[int]
    content: str
    mime_type: str
    time_segment_start: str
    time_segment_end: str

    def __init__(self, content: _Optional[str]=..., mime_type: _Optional[str]=..., time_segment_start: _Optional[str]=..., time_segment_end: _Optional[str]=...) -> None:
        ...