from google.ads.googleads.v16.resources import keyword_theme_constant_pb2 as _keyword_theme_constant_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestKeywordThemeConstantsRequest(_message.Message):
    __slots__ = ("query_text", "country_code", "language_code")
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    query_text: str
    country_code: str
    language_code: str
    def __init__(self, query_text: _Optional[str] = ..., country_code: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class SuggestKeywordThemeConstantsResponse(_message.Message):
    __slots__ = ("keyword_theme_constants",)
    KEYWORD_THEME_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    keyword_theme_constants: _containers.RepeatedCompositeFieldContainer[_keyword_theme_constant_pb2.KeywordThemeConstant]
    def __init__(self, keyword_theme_constants: _Optional[_Iterable[_Union[_keyword_theme_constant_pb2.KeywordThemeConstant, _Mapping]]] = ...) -> None: ...
