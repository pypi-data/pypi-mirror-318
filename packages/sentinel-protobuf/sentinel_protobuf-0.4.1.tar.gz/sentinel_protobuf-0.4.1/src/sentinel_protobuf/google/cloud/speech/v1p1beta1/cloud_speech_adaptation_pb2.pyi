from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.speech.v1p1beta1 import resource_pb2 as _resource_pb2_1
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreatePhraseSetRequest(_message.Message):
    __slots__ = ('parent', 'phrase_set_id', 'phrase_set')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PHRASE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    PHRASE_SET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    phrase_set_id: str
    phrase_set: _resource_pb2_1.PhraseSet

    def __init__(self, parent: _Optional[str]=..., phrase_set_id: _Optional[str]=..., phrase_set: _Optional[_Union[_resource_pb2_1.PhraseSet, _Mapping]]=...) -> None:
        ...

class UpdatePhraseSetRequest(_message.Message):
    __slots__ = ('phrase_set', 'update_mask')
    PHRASE_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    phrase_set: _resource_pb2_1.PhraseSet
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, phrase_set: _Optional[_Union[_resource_pb2_1.PhraseSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetPhraseSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPhraseSetRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPhraseSetResponse(_message.Message):
    __slots__ = ('phrase_sets', 'next_page_token')
    PHRASE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    phrase_sets: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.PhraseSet]
    next_page_token: str

    def __init__(self, phrase_sets: _Optional[_Iterable[_Union[_resource_pb2_1.PhraseSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeletePhraseSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCustomClassRequest(_message.Message):
    __slots__ = ('parent', 'custom_class_id', 'custom_class')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_class_id: str
    custom_class: _resource_pb2_1.CustomClass

    def __init__(self, parent: _Optional[str]=..., custom_class_id: _Optional[str]=..., custom_class: _Optional[_Union[_resource_pb2_1.CustomClass, _Mapping]]=...) -> None:
        ...

class UpdateCustomClassRequest(_message.Message):
    __slots__ = ('custom_class', 'update_mask')
    CUSTOM_CLASS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    custom_class: _resource_pb2_1.CustomClass
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, custom_class: _Optional[_Union[_resource_pb2_1.CustomClass, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetCustomClassRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCustomClassesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCustomClassesResponse(_message.Message):
    __slots__ = ('custom_classes', 'next_page_token')
    CUSTOM_CLASSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    custom_classes: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.CustomClass]
    next_page_token: str

    def __init__(self, custom_classes: _Optional[_Iterable[_Union[_resource_pb2_1.CustomClass, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteCustomClassRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...