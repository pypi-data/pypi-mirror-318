from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlTextSentiment(_message.Message):
    __slots__ = ('inputs',)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlTextSentimentInputs

    def __init__(self, inputs: _Optional[_Union[AutoMlTextSentimentInputs, _Mapping]]=...) -> None:
        ...

class AutoMlTextSentimentInputs(_message.Message):
    __slots__ = ('sentiment_max',)
    SENTIMENT_MAX_FIELD_NUMBER: _ClassVar[int]
    sentiment_max: int

    def __init__(self, sentiment_max: _Optional[int]=...) -> None:
        ...