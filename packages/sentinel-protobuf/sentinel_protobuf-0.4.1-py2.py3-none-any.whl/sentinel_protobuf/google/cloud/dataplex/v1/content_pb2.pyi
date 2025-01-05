from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import analyze_pb2 as _analyze_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateContentRequest(_message.Message):
    __slots__ = ('parent', 'content', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    content: _analyze_pb2.Content
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., content: _Optional[_Union[_analyze_pb2.Content, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateContentRequest(_message.Message):
    __slots__ = ('update_mask', 'content', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    content: _analyze_pb2.Content
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., content: _Optional[_Union[_analyze_pb2.Content, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteContentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListContentRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListContentResponse(_message.Message):
    __slots__ = ('content', 'next_page_token')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[_analyze_pb2.Content]
    next_page_token: str

    def __init__(self, content: _Optional[_Iterable[_Union[_analyze_pb2.Content, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetContentRequest(_message.Message):
    __slots__ = ('name', 'view')

    class ContentView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_VIEW_UNSPECIFIED: _ClassVar[GetContentRequest.ContentView]
        BASIC: _ClassVar[GetContentRequest.ContentView]
        FULL: _ClassVar[GetContentRequest.ContentView]
    CONTENT_VIEW_UNSPECIFIED: GetContentRequest.ContentView
    BASIC: GetContentRequest.ContentView
    FULL: GetContentRequest.ContentView
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: GetContentRequest.ContentView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[GetContentRequest.ContentView, str]]=...) -> None:
        ...