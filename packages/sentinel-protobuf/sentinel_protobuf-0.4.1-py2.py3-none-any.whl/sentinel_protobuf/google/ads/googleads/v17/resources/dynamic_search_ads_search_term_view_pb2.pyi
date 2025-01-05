from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DynamicSearchAdsSearchTermView(_message.Message):
    __slots__ = ("resource_name", "search_term", "headline", "landing_page", "page_url", "has_negative_keyword", "has_matching_keyword", "has_negative_url")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    LANDING_PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    HAS_NEGATIVE_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    HAS_MATCHING_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    HAS_NEGATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    search_term: str
    headline: str
    landing_page: str
    page_url: str
    has_negative_keyword: bool
    has_matching_keyword: bool
    has_negative_url: bool
    def __init__(self, resource_name: _Optional[str] = ..., search_term: _Optional[str] = ..., headline: _Optional[str] = ..., landing_page: _Optional[str] = ..., page_url: _Optional[str] = ..., has_negative_keyword: bool = ..., has_matching_keyword: bool = ..., has_negative_url: bool = ...) -> None: ...
