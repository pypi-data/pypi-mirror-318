from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataStoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_STORE_TYPE_UNSPECIFIED: _ClassVar[DataStoreType]
    PUBLIC_WEB: _ClassVar[DataStoreType]
    UNSTRUCTURED: _ClassVar[DataStoreType]
    STRUCTURED: _ClassVar[DataStoreType]
DATA_STORE_TYPE_UNSPECIFIED: DataStoreType
PUBLIC_WEB: DataStoreType
UNSTRUCTURED: DataStoreType
STRUCTURED: DataStoreType

class DataStoreConnection(_message.Message):
    __slots__ = ('data_store_type', 'data_store')
    DATA_STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    data_store_type: DataStoreType
    data_store: str

    def __init__(self, data_store_type: _Optional[_Union[DataStoreType, str]]=..., data_store: _Optional[str]=...) -> None:
        ...

class DataStoreConnectionSignals(_message.Message):
    __slots__ = ('rewriter_model_call_signals', 'rewritten_query', 'search_snippets', 'answer_generation_model_call_signals', 'answer', 'answer_parts', 'cited_snippets', 'grounding_signals', 'safety_signals')

    class RewriterModelCallSignals(_message.Message):
        __slots__ = ('rendered_prompt', 'model_output', 'model')
        RENDERED_PROMPT_FIELD_NUMBER: _ClassVar[int]
        MODEL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        rendered_prompt: str
        model_output: str
        model: str

        def __init__(self, rendered_prompt: _Optional[str]=..., model_output: _Optional[str]=..., model: _Optional[str]=...) -> None:
            ...

    class SearchSnippet(_message.Message):
        __slots__ = ('document_title', 'document_uri', 'text')
        DOCUMENT_TITLE_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_URI_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        document_title: str
        document_uri: str
        text: str

        def __init__(self, document_title: _Optional[str]=..., document_uri: _Optional[str]=..., text: _Optional[str]=...) -> None:
            ...

    class AnswerGenerationModelCallSignals(_message.Message):
        __slots__ = ('rendered_prompt', 'model_output', 'model')
        RENDERED_PROMPT_FIELD_NUMBER: _ClassVar[int]
        MODEL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        rendered_prompt: str
        model_output: str
        model: str

        def __init__(self, rendered_prompt: _Optional[str]=..., model_output: _Optional[str]=..., model: _Optional[str]=...) -> None:
            ...

    class AnswerPart(_message.Message):
        __slots__ = ('text', 'supporting_indices')
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SUPPORTING_INDICES_FIELD_NUMBER: _ClassVar[int]
        text: str
        supporting_indices: _containers.RepeatedScalarFieldContainer[int]

        def __init__(self, text: _Optional[str]=..., supporting_indices: _Optional[_Iterable[int]]=...) -> None:
            ...

    class CitedSnippet(_message.Message):
        __slots__ = ('search_snippet', 'snippet_index')
        SEARCH_SNIPPET_FIELD_NUMBER: _ClassVar[int]
        SNIPPET_INDEX_FIELD_NUMBER: _ClassVar[int]
        search_snippet: DataStoreConnectionSignals.SearchSnippet
        snippet_index: int

        def __init__(self, search_snippet: _Optional[_Union[DataStoreConnectionSignals.SearchSnippet, _Mapping]]=..., snippet_index: _Optional[int]=...) -> None:
            ...

    class GroundingSignals(_message.Message):
        __slots__ = ('decision', 'score')

        class GroundingDecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GROUNDING_DECISION_UNSPECIFIED: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingDecision]
            ACCEPTED_BY_GROUNDING: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingDecision]
            REJECTED_BY_GROUNDING: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingDecision]
        GROUNDING_DECISION_UNSPECIFIED: DataStoreConnectionSignals.GroundingSignals.GroundingDecision
        ACCEPTED_BY_GROUNDING: DataStoreConnectionSignals.GroundingSignals.GroundingDecision
        REJECTED_BY_GROUNDING: DataStoreConnectionSignals.GroundingSignals.GroundingDecision

        class GroundingScoreBucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GROUNDING_SCORE_BUCKET_UNSPECIFIED: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket]
            VERY_LOW: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket]
            LOW: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket]
            MEDIUM: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket]
            HIGH: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket]
            VERY_HIGH: _ClassVar[DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket]
        GROUNDING_SCORE_BUCKET_UNSPECIFIED: DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket
        VERY_LOW: DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket
        LOW: DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket
        MEDIUM: DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket
        HIGH: DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket
        VERY_HIGH: DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket
        DECISION_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        decision: DataStoreConnectionSignals.GroundingSignals.GroundingDecision
        score: DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket

        def __init__(self, decision: _Optional[_Union[DataStoreConnectionSignals.GroundingSignals.GroundingDecision, str]]=..., score: _Optional[_Union[DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket, str]]=...) -> None:
            ...

    class SafetySignals(_message.Message):
        __slots__ = ('decision', 'banned_phrase_match', 'matched_banned_phrase')

        class SafetyDecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SAFETY_DECISION_UNSPECIFIED: _ClassVar[DataStoreConnectionSignals.SafetySignals.SafetyDecision]
            ACCEPTED_BY_SAFETY_CHECK: _ClassVar[DataStoreConnectionSignals.SafetySignals.SafetyDecision]
            REJECTED_BY_SAFETY_CHECK: _ClassVar[DataStoreConnectionSignals.SafetySignals.SafetyDecision]
        SAFETY_DECISION_UNSPECIFIED: DataStoreConnectionSignals.SafetySignals.SafetyDecision
        ACCEPTED_BY_SAFETY_CHECK: DataStoreConnectionSignals.SafetySignals.SafetyDecision
        REJECTED_BY_SAFETY_CHECK: DataStoreConnectionSignals.SafetySignals.SafetyDecision

        class BannedPhraseMatch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BANNED_PHRASE_MATCH_UNSPECIFIED: _ClassVar[DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch]
            BANNED_PHRASE_MATCH_NONE: _ClassVar[DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch]
            BANNED_PHRASE_MATCH_QUERY: _ClassVar[DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch]
            BANNED_PHRASE_MATCH_RESPONSE: _ClassVar[DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch]
        BANNED_PHRASE_MATCH_UNSPECIFIED: DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch
        BANNED_PHRASE_MATCH_NONE: DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch
        BANNED_PHRASE_MATCH_QUERY: DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch
        BANNED_PHRASE_MATCH_RESPONSE: DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch
        DECISION_FIELD_NUMBER: _ClassVar[int]
        BANNED_PHRASE_MATCH_FIELD_NUMBER: _ClassVar[int]
        MATCHED_BANNED_PHRASE_FIELD_NUMBER: _ClassVar[int]
        decision: DataStoreConnectionSignals.SafetySignals.SafetyDecision
        banned_phrase_match: DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch
        matched_banned_phrase: str

        def __init__(self, decision: _Optional[_Union[DataStoreConnectionSignals.SafetySignals.SafetyDecision, str]]=..., banned_phrase_match: _Optional[_Union[DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch, str]]=..., matched_banned_phrase: _Optional[str]=...) -> None:
            ...
    REWRITER_MODEL_CALL_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    REWRITTEN_QUERY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SNIPPETS_FIELD_NUMBER: _ClassVar[int]
    ANSWER_GENERATION_MODEL_CALL_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    ANSWER_PARTS_FIELD_NUMBER: _ClassVar[int]
    CITED_SNIPPETS_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    SAFETY_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    rewriter_model_call_signals: DataStoreConnectionSignals.RewriterModelCallSignals
    rewritten_query: str
    search_snippets: _containers.RepeatedCompositeFieldContainer[DataStoreConnectionSignals.SearchSnippet]
    answer_generation_model_call_signals: DataStoreConnectionSignals.AnswerGenerationModelCallSignals
    answer: str
    answer_parts: _containers.RepeatedCompositeFieldContainer[DataStoreConnectionSignals.AnswerPart]
    cited_snippets: _containers.RepeatedCompositeFieldContainer[DataStoreConnectionSignals.CitedSnippet]
    grounding_signals: DataStoreConnectionSignals.GroundingSignals
    safety_signals: DataStoreConnectionSignals.SafetySignals

    def __init__(self, rewriter_model_call_signals: _Optional[_Union[DataStoreConnectionSignals.RewriterModelCallSignals, _Mapping]]=..., rewritten_query: _Optional[str]=..., search_snippets: _Optional[_Iterable[_Union[DataStoreConnectionSignals.SearchSnippet, _Mapping]]]=..., answer_generation_model_call_signals: _Optional[_Union[DataStoreConnectionSignals.AnswerGenerationModelCallSignals, _Mapping]]=..., answer: _Optional[str]=..., answer_parts: _Optional[_Iterable[_Union[DataStoreConnectionSignals.AnswerPart, _Mapping]]]=..., cited_snippets: _Optional[_Iterable[_Union[DataStoreConnectionSignals.CitedSnippet, _Mapping]]]=..., grounding_signals: _Optional[_Union[DataStoreConnectionSignals.GroundingSignals, _Mapping]]=..., safety_signals: _Optional[_Union[DataStoreConnectionSignals.SafetySignals, _Mapping]]=...) -> None:
        ...