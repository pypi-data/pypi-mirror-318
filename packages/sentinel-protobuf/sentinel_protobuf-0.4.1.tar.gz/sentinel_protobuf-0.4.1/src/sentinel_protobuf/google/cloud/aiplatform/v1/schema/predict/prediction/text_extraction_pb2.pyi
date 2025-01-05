from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TextExtractionPredictionResult(_message.Message):
    __slots__ = ('ids', 'display_names', 'text_segment_start_offsets', 'text_segment_end_offsets', 'confidences')
    IDS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
    TEXT_SEGMENT_START_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    TEXT_SEGMENT_END_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCES_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    display_names: _containers.RepeatedScalarFieldContainer[str]
    text_segment_start_offsets: _containers.RepeatedScalarFieldContainer[int]
    text_segment_end_offsets: _containers.RepeatedScalarFieldContainer[int]
    confidences: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, ids: _Optional[_Iterable[int]]=..., display_names: _Optional[_Iterable[str]]=..., text_segment_start_offsets: _Optional[_Iterable[int]]=..., text_segment_end_offsets: _Optional[_Iterable[int]]=..., confidences: _Optional[_Iterable[float]]=...) -> None:
        ...