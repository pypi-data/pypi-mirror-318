from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImageObjectDetectionPredictionResult(_message.Message):
    __slots__ = ('ids', 'display_names', 'confidences', 'bboxes')
    IDS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCES_FIELD_NUMBER: _ClassVar[int]
    BBOXES_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    display_names: _containers.RepeatedScalarFieldContainer[str]
    confidences: _containers.RepeatedScalarFieldContainer[float]
    bboxes: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]

    def __init__(self, ids: _Optional[_Iterable[int]]=..., display_names: _Optional[_Iterable[str]]=..., confidences: _Optional[_Iterable[float]]=..., bboxes: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]]=...) -> None:
        ...