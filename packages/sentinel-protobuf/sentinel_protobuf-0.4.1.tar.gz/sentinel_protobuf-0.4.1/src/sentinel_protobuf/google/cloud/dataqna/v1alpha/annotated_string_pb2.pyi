from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnnotatedString(_message.Message):
    __slots__ = ('text_formatted', 'html_formatted', 'markups')

    class SemanticMarkupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MARKUP_TYPE_UNSPECIFIED: _ClassVar[AnnotatedString.SemanticMarkupType]
        METRIC: _ClassVar[AnnotatedString.SemanticMarkupType]
        DIMENSION: _ClassVar[AnnotatedString.SemanticMarkupType]
        FILTER: _ClassVar[AnnotatedString.SemanticMarkupType]
        UNUSED: _ClassVar[AnnotatedString.SemanticMarkupType]
        BLOCKED: _ClassVar[AnnotatedString.SemanticMarkupType]
        ROW: _ClassVar[AnnotatedString.SemanticMarkupType]
    MARKUP_TYPE_UNSPECIFIED: AnnotatedString.SemanticMarkupType
    METRIC: AnnotatedString.SemanticMarkupType
    DIMENSION: AnnotatedString.SemanticMarkupType
    FILTER: AnnotatedString.SemanticMarkupType
    UNUSED: AnnotatedString.SemanticMarkupType
    BLOCKED: AnnotatedString.SemanticMarkupType
    ROW: AnnotatedString.SemanticMarkupType

    class SemanticMarkup(_message.Message):
        __slots__ = ('type', 'start_char_index', 'length')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        START_CHAR_INDEX_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        type: AnnotatedString.SemanticMarkupType
        start_char_index: int
        length: int

        def __init__(self, type: _Optional[_Union[AnnotatedString.SemanticMarkupType, str]]=..., start_char_index: _Optional[int]=..., length: _Optional[int]=...) -> None:
            ...
    TEXT_FORMATTED_FIELD_NUMBER: _ClassVar[int]
    HTML_FORMATTED_FIELD_NUMBER: _ClassVar[int]
    MARKUPS_FIELD_NUMBER: _ClassVar[int]
    text_formatted: str
    html_formatted: str
    markups: _containers.RepeatedCompositeFieldContainer[AnnotatedString.SemanticMarkup]

    def __init__(self, text_formatted: _Optional[str]=..., html_formatted: _Optional[str]=..., markups: _Optional[_Iterable[_Union[AnnotatedString.SemanticMarkup, _Mapping]]]=...) -> None:
        ...