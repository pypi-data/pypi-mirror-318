from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SuggestionDenyListEntry(_message.Message):
    __slots__ = ('block_phrase', 'match_operator')

    class MatchOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MATCH_OPERATOR_UNSPECIFIED: _ClassVar[SuggestionDenyListEntry.MatchOperator]
        EXACT_MATCH: _ClassVar[SuggestionDenyListEntry.MatchOperator]
        CONTAINS: _ClassVar[SuggestionDenyListEntry.MatchOperator]
    MATCH_OPERATOR_UNSPECIFIED: SuggestionDenyListEntry.MatchOperator
    EXACT_MATCH: SuggestionDenyListEntry.MatchOperator
    CONTAINS: SuggestionDenyListEntry.MatchOperator
    BLOCK_PHRASE_FIELD_NUMBER: _ClassVar[int]
    MATCH_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    block_phrase: str
    match_operator: SuggestionDenyListEntry.MatchOperator

    def __init__(self, block_phrase: _Optional[str]=..., match_operator: _Optional[_Union[SuggestionDenyListEntry.MatchOperator, str]]=...) -> None:
        ...

class CompletionSuggestion(_message.Message):
    __slots__ = ('global_score', 'frequency', 'suggestion', 'language_code', 'group_id', 'group_score', 'alternative_phrases')
    GLOBAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SCORE_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_PHRASES_FIELD_NUMBER: _ClassVar[int]
    global_score: float
    frequency: int
    suggestion: str
    language_code: str
    group_id: str
    group_score: float
    alternative_phrases: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, global_score: _Optional[float]=..., frequency: _Optional[int]=..., suggestion: _Optional[str]=..., language_code: _Optional[str]=..., group_id: _Optional[str]=..., group_score: _Optional[float]=..., alternative_phrases: _Optional[_Iterable[str]]=...) -> None:
        ...