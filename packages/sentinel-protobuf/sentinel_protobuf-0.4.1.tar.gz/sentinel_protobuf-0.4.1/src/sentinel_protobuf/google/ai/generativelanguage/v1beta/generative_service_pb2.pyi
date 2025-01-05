from google.ai.generativelanguage.v1beta import citation_pb2 as _citation_pb2
from google.ai.generativelanguage.v1beta import content_pb2 as _content_pb2
from google.ai.generativelanguage.v1beta import retriever_pb2 as _retriever_pb2
from google.ai.generativelanguage.v1beta import safety_pb2 as _safety_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_TYPE_UNSPECIFIED: _ClassVar[TaskType]
    RETRIEVAL_QUERY: _ClassVar[TaskType]
    RETRIEVAL_DOCUMENT: _ClassVar[TaskType]
    SEMANTIC_SIMILARITY: _ClassVar[TaskType]
    CLASSIFICATION: _ClassVar[TaskType]
    CLUSTERING: _ClassVar[TaskType]
    QUESTION_ANSWERING: _ClassVar[TaskType]
    FACT_VERIFICATION: _ClassVar[TaskType]
TASK_TYPE_UNSPECIFIED: TaskType
RETRIEVAL_QUERY: TaskType
RETRIEVAL_DOCUMENT: TaskType
SEMANTIC_SIMILARITY: TaskType
CLASSIFICATION: TaskType
CLUSTERING: TaskType
QUESTION_ANSWERING: TaskType
FACT_VERIFICATION: TaskType

class GenerateContentRequest(_message.Message):
    __slots__ = ("model", "system_instruction", "contents", "tools", "tool_config", "safety_settings", "generation_config", "cached_content")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SAFETY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GENERATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CACHED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    model: str
    system_instruction: _content_pb2.Content
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    tools: _containers.RepeatedCompositeFieldContainer[_content_pb2.Tool]
    tool_config: _content_pb2.ToolConfig
    safety_settings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetySetting]
    generation_config: GenerationConfig
    cached_content: str
    def __init__(self, model: _Optional[str] = ..., system_instruction: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[_content_pb2.Tool, _Mapping]]] = ..., tool_config: _Optional[_Union[_content_pb2.ToolConfig, _Mapping]] = ..., safety_settings: _Optional[_Iterable[_Union[_safety_pb2.SafetySetting, _Mapping]]] = ..., generation_config: _Optional[_Union[GenerationConfig, _Mapping]] = ..., cached_content: _Optional[str] = ...) -> None: ...

class GenerationConfig(_message.Message):
    __slots__ = ("candidate_count", "stop_sequences", "max_output_tokens", "temperature", "top_p", "top_k", "response_mime_type", "response_schema", "presence_penalty", "frequency_penalty", "response_logprobs", "logprobs")
    CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    STOP_SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    candidate_count: int
    stop_sequences: _containers.RepeatedScalarFieldContainer[str]
    max_output_tokens: int
    temperature: float
    top_p: float
    top_k: int
    response_mime_type: str
    response_schema: _content_pb2.Schema
    presence_penalty: float
    frequency_penalty: float
    response_logprobs: bool
    logprobs: int
    def __init__(self, candidate_count: _Optional[int] = ..., stop_sequences: _Optional[_Iterable[str]] = ..., max_output_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ..., response_mime_type: _Optional[str] = ..., response_schema: _Optional[_Union[_content_pb2.Schema, _Mapping]] = ..., presence_penalty: _Optional[float] = ..., frequency_penalty: _Optional[float] = ..., response_logprobs: bool = ..., logprobs: _Optional[int] = ...) -> None: ...

class SemanticRetrieverConfig(_message.Message):
    __slots__ = ("source", "query", "metadata_filters", "max_chunks_count", "minimum_relevance_score")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FILTERS_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNKS_COUNT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    source: str
    query: _content_pb2.Content
    metadata_filters: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.MetadataFilter]
    max_chunks_count: int
    minimum_relevance_score: float
    def __init__(self, source: _Optional[str] = ..., query: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., metadata_filters: _Optional[_Iterable[_Union[_retriever_pb2.MetadataFilter, _Mapping]]] = ..., max_chunks_count: _Optional[int] = ..., minimum_relevance_score: _Optional[float] = ...) -> None: ...

class GenerateContentResponse(_message.Message):
    __slots__ = ("candidates", "prompt_feedback", "usage_metadata", "model_version")
    class PromptFeedback(_message.Message):
        __slots__ = ("block_reason", "safety_ratings")
        class BlockReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BLOCK_REASON_UNSPECIFIED: _ClassVar[GenerateContentResponse.PromptFeedback.BlockReason]
            SAFETY: _ClassVar[GenerateContentResponse.PromptFeedback.BlockReason]
            OTHER: _ClassVar[GenerateContentResponse.PromptFeedback.BlockReason]
            BLOCKLIST: _ClassVar[GenerateContentResponse.PromptFeedback.BlockReason]
            PROHIBITED_CONTENT: _ClassVar[GenerateContentResponse.PromptFeedback.BlockReason]
        BLOCK_REASON_UNSPECIFIED: GenerateContentResponse.PromptFeedback.BlockReason
        SAFETY: GenerateContentResponse.PromptFeedback.BlockReason
        OTHER: GenerateContentResponse.PromptFeedback.BlockReason
        BLOCKLIST: GenerateContentResponse.PromptFeedback.BlockReason
        PROHIBITED_CONTENT: GenerateContentResponse.PromptFeedback.BlockReason
        BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
        SAFETY_RATINGS_FIELD_NUMBER: _ClassVar[int]
        block_reason: GenerateContentResponse.PromptFeedback.BlockReason
        safety_ratings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetyRating]
        def __init__(self, block_reason: _Optional[_Union[GenerateContentResponse.PromptFeedback.BlockReason, str]] = ..., safety_ratings: _Optional[_Iterable[_Union[_safety_pb2.SafetyRating, _Mapping]]] = ...) -> None: ...
    class UsageMetadata(_message.Message):
        __slots__ = ("prompt_token_count", "cached_content_token_count", "candidates_token_count", "total_token_count")
        PROMPT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        CACHED_CONTENT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        CANDIDATES_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        prompt_token_count: int
        cached_content_token_count: int
        candidates_token_count: int
        total_token_count: int
        def __init__(self, prompt_token_count: _Optional[int] = ..., cached_content_token_count: _Optional[int] = ..., candidates_token_count: _Optional[int] = ..., total_token_count: _Optional[int] = ...) -> None: ...
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    USAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[Candidate]
    prompt_feedback: GenerateContentResponse.PromptFeedback
    usage_metadata: GenerateContentResponse.UsageMetadata
    model_version: str
    def __init__(self, candidates: _Optional[_Iterable[_Union[Candidate, _Mapping]]] = ..., prompt_feedback: _Optional[_Union[GenerateContentResponse.PromptFeedback, _Mapping]] = ..., usage_metadata: _Optional[_Union[GenerateContentResponse.UsageMetadata, _Mapping]] = ..., model_version: _Optional[str] = ...) -> None: ...

class Candidate(_message.Message):
    __slots__ = ("index", "content", "finish_reason", "safety_ratings", "citation_metadata", "token_count", "grounding_attributions", "grounding_metadata", "avg_logprobs", "logprobs_result")
    class FinishReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FINISH_REASON_UNSPECIFIED: _ClassVar[Candidate.FinishReason]
        STOP: _ClassVar[Candidate.FinishReason]
        MAX_TOKENS: _ClassVar[Candidate.FinishReason]
        SAFETY: _ClassVar[Candidate.FinishReason]
        RECITATION: _ClassVar[Candidate.FinishReason]
        LANGUAGE: _ClassVar[Candidate.FinishReason]
        OTHER: _ClassVar[Candidate.FinishReason]
        BLOCKLIST: _ClassVar[Candidate.FinishReason]
        PROHIBITED_CONTENT: _ClassVar[Candidate.FinishReason]
        SPII: _ClassVar[Candidate.FinishReason]
        MALFORMED_FUNCTION_CALL: _ClassVar[Candidate.FinishReason]
    FINISH_REASON_UNSPECIFIED: Candidate.FinishReason
    STOP: Candidate.FinishReason
    MAX_TOKENS: Candidate.FinishReason
    SAFETY: Candidate.FinishReason
    RECITATION: Candidate.FinishReason
    LANGUAGE: Candidate.FinishReason
    OTHER: Candidate.FinishReason
    BLOCKLIST: Candidate.FinishReason
    PROHIBITED_CONTENT: Candidate.FinishReason
    SPII: Candidate.FinishReason
    MALFORMED_FUNCTION_CALL: Candidate.FinishReason
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RATINGS_FIELD_NUMBER: _ClassVar[int]
    CITATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_ATTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_METADATA_FIELD_NUMBER: _ClassVar[int]
    AVG_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_RESULT_FIELD_NUMBER: _ClassVar[int]
    index: int
    content: _content_pb2.Content
    finish_reason: Candidate.FinishReason
    safety_ratings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetyRating]
    citation_metadata: _citation_pb2.CitationMetadata
    token_count: int
    grounding_attributions: _containers.RepeatedCompositeFieldContainer[GroundingAttribution]
    grounding_metadata: GroundingMetadata
    avg_logprobs: float
    logprobs_result: LogprobsResult
    def __init__(self, index: _Optional[int] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., finish_reason: _Optional[_Union[Candidate.FinishReason, str]] = ..., safety_ratings: _Optional[_Iterable[_Union[_safety_pb2.SafetyRating, _Mapping]]] = ..., citation_metadata: _Optional[_Union[_citation_pb2.CitationMetadata, _Mapping]] = ..., token_count: _Optional[int] = ..., grounding_attributions: _Optional[_Iterable[_Union[GroundingAttribution, _Mapping]]] = ..., grounding_metadata: _Optional[_Union[GroundingMetadata, _Mapping]] = ..., avg_logprobs: _Optional[float] = ..., logprobs_result: _Optional[_Union[LogprobsResult, _Mapping]] = ...) -> None: ...

class LogprobsResult(_message.Message):
    __slots__ = ("top_candidates", "chosen_candidates")
    class Candidate(_message.Message):
        __slots__ = ("token", "token_id", "log_probability")
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        LOG_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
        token: str
        token_id: int
        log_probability: float
        def __init__(self, token: _Optional[str] = ..., token_id: _Optional[int] = ..., log_probability: _Optional[float] = ...) -> None: ...
    class TopCandidates(_message.Message):
        __slots__ = ("candidates",)
        CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        candidates: _containers.RepeatedCompositeFieldContainer[LogprobsResult.Candidate]
        def __init__(self, candidates: _Optional[_Iterable[_Union[LogprobsResult.Candidate, _Mapping]]] = ...) -> None: ...
    TOP_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    top_candidates: _containers.RepeatedCompositeFieldContainer[LogprobsResult.TopCandidates]
    chosen_candidates: _containers.RepeatedCompositeFieldContainer[LogprobsResult.Candidate]
    def __init__(self, top_candidates: _Optional[_Iterable[_Union[LogprobsResult.TopCandidates, _Mapping]]] = ..., chosen_candidates: _Optional[_Iterable[_Union[LogprobsResult.Candidate, _Mapping]]] = ...) -> None: ...

class AttributionSourceId(_message.Message):
    __slots__ = ("grounding_passage", "semantic_retriever_chunk")
    class GroundingPassageId(_message.Message):
        __slots__ = ("passage_id", "part_index")
        PASSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        PART_INDEX_FIELD_NUMBER: _ClassVar[int]
        passage_id: str
        part_index: int
        def __init__(self, passage_id: _Optional[str] = ..., part_index: _Optional[int] = ...) -> None: ...
    class SemanticRetrieverChunk(_message.Message):
        __slots__ = ("source", "chunk")
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        source: str
        chunk: str
        def __init__(self, source: _Optional[str] = ..., chunk: _Optional[str] = ...) -> None: ...
    GROUNDING_PASSAGE_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_RETRIEVER_CHUNK_FIELD_NUMBER: _ClassVar[int]
    grounding_passage: AttributionSourceId.GroundingPassageId
    semantic_retriever_chunk: AttributionSourceId.SemanticRetrieverChunk
    def __init__(self, grounding_passage: _Optional[_Union[AttributionSourceId.GroundingPassageId, _Mapping]] = ..., semantic_retriever_chunk: _Optional[_Union[AttributionSourceId.SemanticRetrieverChunk, _Mapping]] = ...) -> None: ...

class GroundingAttribution(_message.Message):
    __slots__ = ("source_id", "content")
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    source_id: AttributionSourceId
    content: _content_pb2.Content
    def __init__(self, source_id: _Optional[_Union[AttributionSourceId, _Mapping]] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class RetrievalMetadata(_message.Message):
    __slots__ = ("google_search_dynamic_retrieval_score",)
    GOOGLE_SEARCH_DYNAMIC_RETRIEVAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    google_search_dynamic_retrieval_score: float
    def __init__(self, google_search_dynamic_retrieval_score: _Optional[float] = ...) -> None: ...

class GroundingMetadata(_message.Message):
    __slots__ = ("search_entry_point", "grounding_chunks", "grounding_supports", "retrieval_metadata", "web_search_queries")
    SEARCH_ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_SUPPORTS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_QUERIES_FIELD_NUMBER: _ClassVar[int]
    search_entry_point: SearchEntryPoint
    grounding_chunks: _containers.RepeatedCompositeFieldContainer[GroundingChunk]
    grounding_supports: _containers.RepeatedCompositeFieldContainer[GroundingSupport]
    retrieval_metadata: RetrievalMetadata
    web_search_queries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, search_entry_point: _Optional[_Union[SearchEntryPoint, _Mapping]] = ..., grounding_chunks: _Optional[_Iterable[_Union[GroundingChunk, _Mapping]]] = ..., grounding_supports: _Optional[_Iterable[_Union[GroundingSupport, _Mapping]]] = ..., retrieval_metadata: _Optional[_Union[RetrievalMetadata, _Mapping]] = ..., web_search_queries: _Optional[_Iterable[str]] = ...) -> None: ...

class SearchEntryPoint(_message.Message):
    __slots__ = ("rendered_content", "sdk_blob")
    RENDERED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    SDK_BLOB_FIELD_NUMBER: _ClassVar[int]
    rendered_content: str
    sdk_blob: bytes
    def __init__(self, rendered_content: _Optional[str] = ..., sdk_blob: _Optional[bytes] = ...) -> None: ...

class GroundingChunk(_message.Message):
    __slots__ = ("web",)
    class Web(_message.Message):
        __slots__ = ("uri", "title")
        URI_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        uri: str
        title: str
        def __init__(self, uri: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
    WEB_FIELD_NUMBER: _ClassVar[int]
    web: GroundingChunk.Web
    def __init__(self, web: _Optional[_Union[GroundingChunk.Web, _Mapping]] = ...) -> None: ...

class Segment(_message.Message):
    __slots__ = ("part_index", "start_index", "end_index", "text")
    PART_INDEX_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_INDEX_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    part_index: int
    start_index: int
    end_index: int
    text: str
    def __init__(self, part_index: _Optional[int] = ..., start_index: _Optional[int] = ..., end_index: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class GroundingSupport(_message.Message):
    __slots__ = ("segment", "grounding_chunk_indices", "confidence_scores")
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_CHUNK_INDICES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORES_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    grounding_chunk_indices: _containers.RepeatedScalarFieldContainer[int]
    confidence_scores: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ..., grounding_chunk_indices: _Optional[_Iterable[int]] = ..., confidence_scores: _Optional[_Iterable[float]] = ...) -> None: ...

class GenerateAnswerRequest(_message.Message):
    __slots__ = ("inline_passages", "semantic_retriever", "model", "contents", "answer_style", "safety_settings", "temperature")
    class AnswerStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANSWER_STYLE_UNSPECIFIED: _ClassVar[GenerateAnswerRequest.AnswerStyle]
        ABSTRACTIVE: _ClassVar[GenerateAnswerRequest.AnswerStyle]
        EXTRACTIVE: _ClassVar[GenerateAnswerRequest.AnswerStyle]
        VERBOSE: _ClassVar[GenerateAnswerRequest.AnswerStyle]
    ANSWER_STYLE_UNSPECIFIED: GenerateAnswerRequest.AnswerStyle
    ABSTRACTIVE: GenerateAnswerRequest.AnswerStyle
    EXTRACTIVE: GenerateAnswerRequest.AnswerStyle
    VERBOSE: GenerateAnswerRequest.AnswerStyle
    INLINE_PASSAGES_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_RETRIEVER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ANSWER_STYLE_FIELD_NUMBER: _ClassVar[int]
    SAFETY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    inline_passages: _content_pb2.GroundingPassages
    semantic_retriever: SemanticRetrieverConfig
    model: str
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    answer_style: GenerateAnswerRequest.AnswerStyle
    safety_settings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetySetting]
    temperature: float
    def __init__(self, inline_passages: _Optional[_Union[_content_pb2.GroundingPassages, _Mapping]] = ..., semantic_retriever: _Optional[_Union[SemanticRetrieverConfig, _Mapping]] = ..., model: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ..., answer_style: _Optional[_Union[GenerateAnswerRequest.AnswerStyle, str]] = ..., safety_settings: _Optional[_Iterable[_Union[_safety_pb2.SafetySetting, _Mapping]]] = ..., temperature: _Optional[float] = ...) -> None: ...

class GenerateAnswerResponse(_message.Message):
    __slots__ = ("answer", "answerable_probability", "input_feedback")
    class InputFeedback(_message.Message):
        __slots__ = ("block_reason", "safety_ratings")
        class BlockReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BLOCK_REASON_UNSPECIFIED: _ClassVar[GenerateAnswerResponse.InputFeedback.BlockReason]
            SAFETY: _ClassVar[GenerateAnswerResponse.InputFeedback.BlockReason]
            OTHER: _ClassVar[GenerateAnswerResponse.InputFeedback.BlockReason]
        BLOCK_REASON_UNSPECIFIED: GenerateAnswerResponse.InputFeedback.BlockReason
        SAFETY: GenerateAnswerResponse.InputFeedback.BlockReason
        OTHER: GenerateAnswerResponse.InputFeedback.BlockReason
        BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
        SAFETY_RATINGS_FIELD_NUMBER: _ClassVar[int]
        block_reason: GenerateAnswerResponse.InputFeedback.BlockReason
        safety_ratings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetyRating]
        def __init__(self, block_reason: _Optional[_Union[GenerateAnswerResponse.InputFeedback.BlockReason, str]] = ..., safety_ratings: _Optional[_Iterable[_Union[_safety_pb2.SafetyRating, _Mapping]]] = ...) -> None: ...
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    ANSWERABLE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    INPUT_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    answer: Candidate
    answerable_probability: float
    input_feedback: GenerateAnswerResponse.InputFeedback
    def __init__(self, answer: _Optional[_Union[Candidate, _Mapping]] = ..., answerable_probability: _Optional[float] = ..., input_feedback: _Optional[_Union[GenerateAnswerResponse.InputFeedback, _Mapping]] = ...) -> None: ...

class EmbedContentRequest(_message.Message):
    __slots__ = ("model", "content", "task_type", "title", "output_dimensionality")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DIMENSIONALITY_FIELD_NUMBER: _ClassVar[int]
    model: str
    content: _content_pb2.Content
    task_type: TaskType
    title: str
    output_dimensionality: int
    def __init__(self, model: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., task_type: _Optional[_Union[TaskType, str]] = ..., title: _Optional[str] = ..., output_dimensionality: _Optional[int] = ...) -> None: ...

class ContentEmbedding(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class EmbedContentResponse(_message.Message):
    __slots__ = ("embedding",)
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    embedding: ContentEmbedding
    def __init__(self, embedding: _Optional[_Union[ContentEmbedding, _Mapping]] = ...) -> None: ...

class BatchEmbedContentsRequest(_message.Message):
    __slots__ = ("model", "requests")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    model: str
    requests: _containers.RepeatedCompositeFieldContainer[EmbedContentRequest]
    def __init__(self, model: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[EmbedContentRequest, _Mapping]]] = ...) -> None: ...

class BatchEmbedContentsResponse(_message.Message):
    __slots__ = ("embeddings",)
    EMBEDDINGS_FIELD_NUMBER: _ClassVar[int]
    embeddings: _containers.RepeatedCompositeFieldContainer[ContentEmbedding]
    def __init__(self, embeddings: _Optional[_Iterable[_Union[ContentEmbedding, _Mapping]]] = ...) -> None: ...

class CountTokensRequest(_message.Message):
    __slots__ = ("model", "contents", "generate_content_request")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    GENERATE_CONTENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    model: str
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    generate_content_request: GenerateContentRequest
    def __init__(self, model: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ..., generate_content_request: _Optional[_Union[GenerateContentRequest, _Mapping]] = ...) -> None: ...

class CountTokensResponse(_message.Message):
    __slots__ = ("total_tokens", "cached_content_token_count")
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHED_CONTENT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    total_tokens: int
    cached_content_token_count: int
    def __init__(self, total_tokens: _Optional[int] = ..., cached_content_token_count: _Optional[int] = ...) -> None: ...
