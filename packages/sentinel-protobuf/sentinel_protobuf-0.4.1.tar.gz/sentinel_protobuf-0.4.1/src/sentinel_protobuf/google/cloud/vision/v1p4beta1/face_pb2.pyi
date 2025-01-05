from google.cloud.vision.v1p4beta1 import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FaceRecognitionParams(_message.Message):
    __slots__ = ('celebrity_set',)
    CELEBRITY_SET_FIELD_NUMBER: _ClassVar[int]
    celebrity_set: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, celebrity_set: _Optional[_Iterable[str]]=...) -> None:
        ...

class Celebrity(_message.Message):
    __slots__ = ('name', 'display_name', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class FaceRecognitionResult(_message.Message):
    __slots__ = ('celebrity', 'confidence')
    CELEBRITY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    celebrity: Celebrity
    confidence: float

    def __init__(self, celebrity: _Optional[_Union[Celebrity, _Mapping]]=..., confidence: _Optional[float]=...) -> None:
        ...