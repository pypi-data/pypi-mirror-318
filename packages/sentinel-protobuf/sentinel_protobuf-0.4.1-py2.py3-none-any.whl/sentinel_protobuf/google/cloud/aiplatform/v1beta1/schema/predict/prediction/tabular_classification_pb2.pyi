from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TabularClassificationPredictionResult(_message.Message):
    __slots__ = ('classes', 'scores')
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedScalarFieldContainer[str]
    scores: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, classes: _Optional[_Iterable[str]]=..., scores: _Optional[_Iterable[float]]=...) -> None:
        ...