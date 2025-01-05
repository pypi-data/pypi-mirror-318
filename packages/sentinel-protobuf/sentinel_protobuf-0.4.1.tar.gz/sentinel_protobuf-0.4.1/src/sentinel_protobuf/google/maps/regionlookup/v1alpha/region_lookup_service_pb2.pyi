from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.maps.regionlookup.v1alpha import region_identifier_pb2 as _region_identifier_pb2
from google.maps.regionlookup.v1alpha import region_match_pb2 as _region_match_pb2
from google.maps.regionlookup.v1alpha import region_search_values_pb2 as _region_search_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LookupRegionRequest(_message.Message):
    __slots__ = ('identifiers', 'page_size', 'page_token')
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedCompositeFieldContainer[_region_identifier_pb2.RegionIdentifier]
    page_size: int
    page_token: str

    def __init__(self, identifiers: _Optional[_Iterable[_Union[_region_identifier_pb2.RegionIdentifier, _Mapping]]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class LookupRegionResponse(_message.Message):
    __slots__ = ('matches', 'next_page_token')
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[_region_match_pb2.RegionMatch]
    next_page_token: str

    def __init__(self, matches: _Optional[_Iterable[_Union[_region_match_pb2.RegionMatch, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchRegionRequest(_message.Message):
    __slots__ = ('search_values', 'page_size', 'page_token')
    SEARCH_VALUES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_values: _containers.RepeatedCompositeFieldContainer[_region_search_values_pb2.RegionSearchValue]
    page_size: int
    page_token: str

    def __init__(self, search_values: _Optional[_Iterable[_Union[_region_search_values_pb2.RegionSearchValue, _Mapping]]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchRegionResponse(_message.Message):
    __slots__ = ('matches', 'next_page_token')
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[_region_match_pb2.RegionMatch]
    next_page_token: str

    def __init__(self, matches: _Optional[_Iterable[_Union[_region_match_pb2.RegionMatch, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...