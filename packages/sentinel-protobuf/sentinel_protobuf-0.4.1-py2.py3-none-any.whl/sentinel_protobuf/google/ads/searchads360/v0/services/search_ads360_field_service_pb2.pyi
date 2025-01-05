from google.ads.searchads360.v0.resources import search_ads360_field_pb2 as _search_ads360_field_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSearchAds360FieldRequest(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class SearchSearchAds360FieldsRequest(_message.Message):
    __slots__ = ("query", "page_token", "page_size")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    query: str
    page_token: str
    page_size: int
    def __init__(self, query: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class SearchSearchAds360FieldsResponse(_message.Message):
    __slots__ = ("results", "next_page_token", "total_results_count")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_search_ads360_field_pb2.SearchAds360Field]
    next_page_token: str
    total_results_count: int
    def __init__(self, results: _Optional[_Iterable[_Union[_search_ads360_field_pb2.SearchAds360Field, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_results_count: _Optional[int] = ...) -> None: ...
