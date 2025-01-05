from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OSImage(_message.Message):
    __slots__ = ('name', 'code', 'description', 'applicable_instance_types', 'supported_network_templates')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPLICABLE_INSTANCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_NETWORK_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    description: str
    applicable_instance_types: _containers.RepeatedScalarFieldContainer[str]
    supported_network_templates: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., code: _Optional[str]=..., description: _Optional[str]=..., applicable_instance_types: _Optional[_Iterable[str]]=..., supported_network_templates: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListOSImagesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOSImagesResponse(_message.Message):
    __slots__ = ('os_images', 'next_page_token')
    OS_IMAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    os_images: _containers.RepeatedCompositeFieldContainer[OSImage]
    next_page_token: str

    def __init__(self, os_images: _Optional[_Iterable[_Union[OSImage, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...