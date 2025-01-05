from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TextSentimentPredictionResult(_message.Message):
    __slots__ = ('sentiment',)
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    sentiment: int

    def __init__(self, sentiment: _Optional[int]=...) -> None:
        ...