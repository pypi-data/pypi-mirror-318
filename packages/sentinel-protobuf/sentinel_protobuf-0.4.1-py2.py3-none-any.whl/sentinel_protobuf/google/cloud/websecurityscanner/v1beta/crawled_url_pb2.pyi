from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class CrawledUrl(_message.Message):
    __slots__ = ('http_method', 'url', 'body')
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    http_method: str
    url: str
    body: str

    def __init__(self, http_method: _Optional[str]=..., url: _Optional[str]=..., body: _Optional[str]=...) -> None:
        ...