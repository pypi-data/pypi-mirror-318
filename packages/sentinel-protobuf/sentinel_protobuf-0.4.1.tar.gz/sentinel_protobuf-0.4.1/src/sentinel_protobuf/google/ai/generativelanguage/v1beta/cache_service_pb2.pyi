from google.ai.generativelanguage.v1beta import cached_content_pb2 as _cached_content_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCachedContentsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCachedContentsResponse(_message.Message):
    __slots__ = ("cached_contents", "next_page_token")
    CACHED_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cached_contents: _containers.RepeatedCompositeFieldContainer[_cached_content_pb2.CachedContent]
    next_page_token: str
    def __init__(self, cached_contents: _Optional[_Iterable[_Union[_cached_content_pb2.CachedContent, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateCachedContentRequest(_message.Message):
    __slots__ = ("cached_content",)
    CACHED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    cached_content: _cached_content_pb2.CachedContent
    def __init__(self, cached_content: _Optional[_Union[_cached_content_pb2.CachedContent, _Mapping]] = ...) -> None: ...

class GetCachedContentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateCachedContentRequest(_message.Message):
    __slots__ = ("cached_content", "update_mask")
    CACHED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    cached_content: _cached_content_pb2.CachedContent
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, cached_content: _Optional[_Union[_cached_content_pb2.CachedContent, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteCachedContentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
