from google.ai.generativelanguage.v1beta3 import citation_pb2 as _citation_pb2
from google.ai.generativelanguage.v1beta3 import safety_pb2 as _safety_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateTextRequest(_message.Message):
    __slots__ = ("model", "prompt", "temperature", "candidate_count", "max_output_tokens", "top_p", "top_k", "safety_settings", "stop_sequences")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    SAFETY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STOP_SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    model: str
    prompt: TextPrompt
    temperature: float
    candidate_count: int
    max_output_tokens: int
    top_p: float
    top_k: int
    safety_settings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetySetting]
    stop_sequences: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model: _Optional[str] = ..., prompt: _Optional[_Union[TextPrompt, _Mapping]] = ..., temperature: _Optional[float] = ..., candidate_count: _Optional[int] = ..., max_output_tokens: _Optional[int] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ..., safety_settings: _Optional[_Iterable[_Union[_safety_pb2.SafetySetting, _Mapping]]] = ..., stop_sequences: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateTextResponse(_message.Message):
    __slots__ = ("candidates", "filters", "safety_feedback")
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SAFETY_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[TextCompletion]
    filters: _containers.RepeatedCompositeFieldContainer[_safety_pb2.ContentFilter]
    safety_feedback: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetyFeedback]
    def __init__(self, candidates: _Optional[_Iterable[_Union[TextCompletion, _Mapping]]] = ..., filters: _Optional[_Iterable[_Union[_safety_pb2.ContentFilter, _Mapping]]] = ..., safety_feedback: _Optional[_Iterable[_Union[_safety_pb2.SafetyFeedback, _Mapping]]] = ...) -> None: ...

class TextPrompt(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class TextCompletion(_message.Message):
    __slots__ = ("output", "safety_ratings", "citation_metadata")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RATINGS_FIELD_NUMBER: _ClassVar[int]
    CITATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    output: str
    safety_ratings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetyRating]
    citation_metadata: _citation_pb2.CitationMetadata
    def __init__(self, output: _Optional[str] = ..., safety_ratings: _Optional[_Iterable[_Union[_safety_pb2.SafetyRating, _Mapping]]] = ..., citation_metadata: _Optional[_Union[_citation_pb2.CitationMetadata, _Mapping]] = ...) -> None: ...

class EmbedTextRequest(_message.Message):
    __slots__ = ("model", "text")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    model: str
    text: str
    def __init__(self, model: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class EmbedTextResponse(_message.Message):
    __slots__ = ("embedding",)
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    embedding: Embedding
    def __init__(self, embedding: _Optional[_Union[Embedding, _Mapping]] = ...) -> None: ...

class BatchEmbedTextRequest(_message.Message):
    __slots__ = ("model", "texts")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TEXTS_FIELD_NUMBER: _ClassVar[int]
    model: str
    texts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model: _Optional[str] = ..., texts: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchEmbedTextResponse(_message.Message):
    __slots__ = ("embeddings",)
    EMBEDDINGS_FIELD_NUMBER: _ClassVar[int]
    embeddings: _containers.RepeatedCompositeFieldContainer[Embedding]
    def __init__(self, embeddings: _Optional[_Iterable[_Union[Embedding, _Mapping]]] = ...) -> None: ...

class Embedding(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...

class CountTextTokensRequest(_message.Message):
    __slots__ = ("model", "prompt")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    model: str
    prompt: TextPrompt
    def __init__(self, model: _Optional[str] = ..., prompt: _Optional[_Union[TextPrompt, _Mapping]] = ...) -> None: ...

class CountTextTokensResponse(_message.Message):
    __slots__ = ("token_count",)
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    token_count: int
    def __init__(self, token_count: _Optional[int] = ...) -> None: ...
