from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UrlCollection(_message.Message):
    __slots__ = ("url_collection_id", "final_urls", "final_mobile_urls", "tracking_url_template")
    URL_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    url_collection_id: str
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    def __init__(self, url_collection_id: _Optional[str] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ..., tracking_url_template: _Optional[str] = ...) -> None: ...
