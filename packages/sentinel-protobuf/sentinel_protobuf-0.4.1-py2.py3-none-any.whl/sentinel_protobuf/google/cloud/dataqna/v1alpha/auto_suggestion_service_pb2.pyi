from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataqna.v1alpha import annotated_string_pb2 as _annotated_string_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SuggestionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUGGESTION_TYPE_UNSPECIFIED: _ClassVar[SuggestionType]
    ENTITY: _ClassVar[SuggestionType]
    TEMPLATE: _ClassVar[SuggestionType]
SUGGESTION_TYPE_UNSPECIFIED: SuggestionType
ENTITY: SuggestionType
TEMPLATE: SuggestionType

class SuggestQueriesRequest(_message.Message):
    __slots__ = ('parent', 'scopes', 'query', 'suggestion_types')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    query: str
    suggestion_types: _containers.RepeatedScalarFieldContainer[SuggestionType]

    def __init__(self, parent: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=..., query: _Optional[str]=..., suggestion_types: _Optional[_Iterable[_Union[SuggestionType, str]]]=...) -> None:
        ...

class Suggestion(_message.Message):
    __slots__ = ('suggestion_info', 'ranking_score', 'suggestion_type')
    SUGGESTION_INFO_FIELD_NUMBER: _ClassVar[int]
    RANKING_SCORE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    suggestion_info: SuggestionInfo
    ranking_score: float
    suggestion_type: SuggestionType

    def __init__(self, suggestion_info: _Optional[_Union[SuggestionInfo, _Mapping]]=..., ranking_score: _Optional[float]=..., suggestion_type: _Optional[_Union[SuggestionType, str]]=...) -> None:
        ...

class SuggestionInfo(_message.Message):
    __slots__ = ('annotated_suggestion', 'query_matches')

    class MatchInfo(_message.Message):
        __slots__ = ('start_char_index', 'length')
        START_CHAR_INDEX_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        start_char_index: int
        length: int

        def __init__(self, start_char_index: _Optional[int]=..., length: _Optional[int]=...) -> None:
            ...
    ANNOTATED_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    QUERY_MATCHES_FIELD_NUMBER: _ClassVar[int]
    annotated_suggestion: _annotated_string_pb2.AnnotatedString
    query_matches: _containers.RepeatedCompositeFieldContainer[SuggestionInfo.MatchInfo]

    def __init__(self, annotated_suggestion: _Optional[_Union[_annotated_string_pb2.AnnotatedString, _Mapping]]=..., query_matches: _Optional[_Iterable[_Union[SuggestionInfo.MatchInfo, _Mapping]]]=...) -> None:
        ...

class SuggestQueriesResponse(_message.Message):
    __slots__ = ('suggestions',)
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    suggestions: _containers.RepeatedCompositeFieldContainer[Suggestion]

    def __init__(self, suggestions: _Optional[_Iterable[_Union[Suggestion, _Mapping]]]=...) -> None:
        ...