from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationSpecSet(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'annotation_specs', 'blocking_resources')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPECS_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    annotation_specs: _containers.RepeatedCompositeFieldContainer[AnnotationSpec]
    blocking_resources: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., annotation_specs: _Optional[_Iterable[_Union[AnnotationSpec, _Mapping]]]=..., blocking_resources: _Optional[_Iterable[str]]=...) -> None:
        ...

class AnnotationSpec(_message.Message):
    __slots__ = ('display_name', 'description')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str

    def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...