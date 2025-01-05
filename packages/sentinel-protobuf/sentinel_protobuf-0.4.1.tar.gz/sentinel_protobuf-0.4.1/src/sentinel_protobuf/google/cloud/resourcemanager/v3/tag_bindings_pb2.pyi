from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TagBinding(_message.Message):
    __slots__ = ('name', 'parent', 'tag_value', 'tag_value_namespaced_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_NAMESPACED_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    tag_value: str
    tag_value_namespaced_name: str

    def __init__(self, name: _Optional[str]=..., parent: _Optional[str]=..., tag_value: _Optional[str]=..., tag_value_namespaced_name: _Optional[str]=...) -> None:
        ...

class CreateTagBindingMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateTagBindingRequest(_message.Message):
    __slots__ = ('tag_binding', 'validate_only')
    TAG_BINDING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    tag_binding: TagBinding
    validate_only: bool

    def __init__(self, tag_binding: _Optional[_Union[TagBinding, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteTagBindingMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteTagBindingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTagBindingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTagBindingsResponse(_message.Message):
    __slots__ = ('tag_bindings', 'next_page_token')
    TAG_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tag_bindings: _containers.RepeatedCompositeFieldContainer[TagBinding]
    next_page_token: str

    def __init__(self, tag_bindings: _Optional[_Iterable[_Union[TagBinding, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListEffectiveTagsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEffectiveTagsResponse(_message.Message):
    __slots__ = ('effective_tags', 'next_page_token')
    EFFECTIVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    effective_tags: _containers.RepeatedCompositeFieldContainer[EffectiveTag]
    next_page_token: str

    def __init__(self, effective_tags: _Optional[_Iterable[_Union[EffectiveTag, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class EffectiveTag(_message.Message):
    __slots__ = ('tag_value', 'namespaced_tag_value', 'tag_key', 'namespaced_tag_key', 'tag_key_parent_name', 'inherited')
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACED_TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    TAG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACED_TAG_KEY_FIELD_NUMBER: _ClassVar[int]
    TAG_KEY_PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
    INHERITED_FIELD_NUMBER: _ClassVar[int]
    tag_value: str
    namespaced_tag_value: str
    tag_key: str
    namespaced_tag_key: str
    tag_key_parent_name: str
    inherited: bool

    def __init__(self, tag_value: _Optional[str]=..., namespaced_tag_value: _Optional[str]=..., tag_key: _Optional[str]=..., namespaced_tag_key: _Optional[str]=..., tag_key_parent_name: _Optional[str]=..., inherited: bool=...) -> None:
        ...