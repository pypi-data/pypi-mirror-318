from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.asset.v1p1beta1 import assets_pb2 as _assets_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SearchAllResourcesRequest(_message.Message):
    __slots__ = ('scope', 'query', 'asset_types', 'page_size', 'page_token', 'order_by')
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    scope: str
    query: str
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    order_by: str

    def __init__(self, scope: _Optional[str]=..., query: _Optional[str]=..., asset_types: _Optional[_Iterable[str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class SearchAllResourcesResponse(_message.Message):
    __slots__ = ('results', 'next_page_token')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_assets_pb2.StandardResourceMetadata]
    next_page_token: str

    def __init__(self, results: _Optional[_Iterable[_Union[_assets_pb2.StandardResourceMetadata, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchAllIamPoliciesRequest(_message.Message):
    __slots__ = ('scope', 'query', 'page_size', 'page_token')
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scope: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, scope: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchAllIamPoliciesResponse(_message.Message):
    __slots__ = ('results', 'next_page_token')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_assets_pb2.IamPolicySearchResult]
    next_page_token: str

    def __init__(self, results: _Optional[_Iterable[_Union[_assets_pb2.IamPolicySearchResult, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...