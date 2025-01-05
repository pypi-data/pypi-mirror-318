from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ClassificationPredictionResult(_message.Message):
    __slots__ = ('ids', 'display_names', 'confidences')
    IDS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCES_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    display_names: _containers.RepeatedScalarFieldContainer[str]
    confidences: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, ids: _Optional[_Iterable[int]]=..., display_names: _Optional[_Iterable[str]]=..., confidences: _Optional[_Iterable[float]]=...) -> None:
        ...