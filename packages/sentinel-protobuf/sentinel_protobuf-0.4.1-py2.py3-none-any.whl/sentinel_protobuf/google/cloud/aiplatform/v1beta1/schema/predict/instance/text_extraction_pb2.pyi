from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TextExtractionPredictionInstance(_message.Message):
    __slots__ = ('content', 'mime_type', 'key')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    content: str
    mime_type: str
    key: str

    def __init__(self, content: _Optional[str]=..., mime_type: _Optional[str]=..., key: _Optional[str]=...) -> None:
        ...