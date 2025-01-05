from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import openapi_pb2 as _openapi_pb2
from google.cloud.aiplatform.v1beta1 import tool_pb2 as _tool_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HarmCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HARM_CATEGORY_UNSPECIFIED: _ClassVar[HarmCategory]
    HARM_CATEGORY_HATE_SPEECH: _ClassVar[HarmCategory]
    HARM_CATEGORY_DANGEROUS_CONTENT: _ClassVar[HarmCategory]
    HARM_CATEGORY_HARASSMENT: _ClassVar[HarmCategory]
    HARM_CATEGORY_SEXUALLY_EXPLICIT: _ClassVar[HarmCategory]
    HARM_CATEGORY_CIVIC_INTEGRITY: _ClassVar[HarmCategory]
HARM_CATEGORY_UNSPECIFIED: HarmCategory
HARM_CATEGORY_HATE_SPEECH: HarmCategory
HARM_CATEGORY_DANGEROUS_CONTENT: HarmCategory
HARM_CATEGORY_HARASSMENT: HarmCategory
HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmCategory
HARM_CATEGORY_CIVIC_INTEGRITY: HarmCategory

class Content(_message.Message):
    __slots__ = ("role", "parts")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    role: str
    parts: _containers.RepeatedCompositeFieldContainer[Part]
    def __init__(self, role: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[Part, _Mapping]]] = ...) -> None: ...

class Part(_message.Message):
    __slots__ = ("text", "inline_data", "file_data", "function_call", "function_response", "executable_code", "code_execution_result", "video_metadata", "thought")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_CALL_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_EXECUTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_METADATA_FIELD_NUMBER: _ClassVar[int]
    THOUGHT_FIELD_NUMBER: _ClassVar[int]
    text: str
    inline_data: Blob
    file_data: FileData
    function_call: _tool_pb2.FunctionCall
    function_response: _tool_pb2.FunctionResponse
    executable_code: _tool_pb2.ExecutableCode
    code_execution_result: _tool_pb2.CodeExecutionResult
    video_metadata: VideoMetadata
    thought: bool
    def __init__(self, text: _Optional[str] = ..., inline_data: _Optional[_Union[Blob, _Mapping]] = ..., file_data: _Optional[_Union[FileData, _Mapping]] = ..., function_call: _Optional[_Union[_tool_pb2.FunctionCall, _Mapping]] = ..., function_response: _Optional[_Union[_tool_pb2.FunctionResponse, _Mapping]] = ..., executable_code: _Optional[_Union[_tool_pb2.ExecutableCode, _Mapping]] = ..., code_execution_result: _Optional[_Union[_tool_pb2.CodeExecutionResult, _Mapping]] = ..., video_metadata: _Optional[_Union[VideoMetadata, _Mapping]] = ..., thought: bool = ...) -> None: ...

class Blob(_message.Message):
    __slots__ = ("mime_type", "data")
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    data: bytes
    def __init__(self, mime_type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class FileData(_message.Message):
    __slots__ = ("mime_type", "file_uri")
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_URI_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    file_uri: str
    def __init__(self, mime_type: _Optional[str] = ..., file_uri: _Optional[str] = ...) -> None: ...

class VideoMetadata(_message.Message):
    __slots__ = ("start_offset", "end_offset")
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_offset: _duration_pb2.Duration
    end_offset: _duration_pb2.Duration
    def __init__(self, start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PrebuiltVoiceConfig(_message.Message):
    __slots__ = ("voice_name",)
    VOICE_NAME_FIELD_NUMBER: _ClassVar[int]
    voice_name: str
    def __init__(self, voice_name: _Optional[str] = ...) -> None: ...

class VoiceConfig(_message.Message):
    __slots__ = ("prebuilt_voice_config",)
    PREBUILT_VOICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    prebuilt_voice_config: PrebuiltVoiceConfig
    def __init__(self, prebuilt_voice_config: _Optional[_Union[PrebuiltVoiceConfig, _Mapping]] = ...) -> None: ...

class SpeechConfig(_message.Message):
    __slots__ = ("voice_config",)
    VOICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    voice_config: VoiceConfig
    def __init__(self, voice_config: _Optional[_Union[VoiceConfig, _Mapping]] = ...) -> None: ...

class GenerationConfig(_message.Message):
    __slots__ = ("temperature", "top_p", "top_k", "candidate_count", "max_output_tokens", "stop_sequences", "response_logprobs", "logprobs", "presence_penalty", "frequency_penalty", "seed", "response_mime_type", "response_schema", "routing_config", "audio_timestamp", "response_modalities", "media_resolution", "speech_config")
    class Modality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODALITY_UNSPECIFIED: _ClassVar[GenerationConfig.Modality]
        TEXT: _ClassVar[GenerationConfig.Modality]
        IMAGE: _ClassVar[GenerationConfig.Modality]
        AUDIO: _ClassVar[GenerationConfig.Modality]
    MODALITY_UNSPECIFIED: GenerationConfig.Modality
    TEXT: GenerationConfig.Modality
    IMAGE: GenerationConfig.Modality
    AUDIO: GenerationConfig.Modality
    class MediaResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEDIA_RESOLUTION_UNSPECIFIED: _ClassVar[GenerationConfig.MediaResolution]
        MEDIA_RESOLUTION_LOW: _ClassVar[GenerationConfig.MediaResolution]
        MEDIA_RESOLUTION_MEDIUM: _ClassVar[GenerationConfig.MediaResolution]
        MEDIA_RESOLUTION_HIGH: _ClassVar[GenerationConfig.MediaResolution]
    MEDIA_RESOLUTION_UNSPECIFIED: GenerationConfig.MediaResolution
    MEDIA_RESOLUTION_LOW: GenerationConfig.MediaResolution
    MEDIA_RESOLUTION_MEDIUM: GenerationConfig.MediaResolution
    MEDIA_RESOLUTION_HIGH: GenerationConfig.MediaResolution
    class RoutingConfig(_message.Message):
        __slots__ = ("auto_mode", "manual_mode")
        class AutoRoutingMode(_message.Message):
            __slots__ = ("model_routing_preference",)
            class ModelRoutingPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN: _ClassVar[GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference]
                PRIORITIZE_QUALITY: _ClassVar[GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference]
                BALANCED: _ClassVar[GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference]
                PRIORITIZE_COST: _ClassVar[GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference]
            UNKNOWN: GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference
            PRIORITIZE_QUALITY: GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference
            BALANCED: GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference
            PRIORITIZE_COST: GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference
            MODEL_ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
            model_routing_preference: GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference
            def __init__(self, model_routing_preference: _Optional[_Union[GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference, str]] = ...) -> None: ...
        class ManualRoutingMode(_message.Message):
            __slots__ = ("model_name",)
            MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
            model_name: str
            def __init__(self, model_name: _Optional[str] = ...) -> None: ...
        AUTO_MODE_FIELD_NUMBER: _ClassVar[int]
        MANUAL_MODE_FIELD_NUMBER: _ClassVar[int]
        auto_mode: GenerationConfig.RoutingConfig.AutoRoutingMode
        manual_mode: GenerationConfig.RoutingConfig.ManualRoutingMode
        def __init__(self, auto_mode: _Optional[_Union[GenerationConfig.RoutingConfig.AutoRoutingMode, _Mapping]] = ..., manual_mode: _Optional[_Union[GenerationConfig.RoutingConfig.ManualRoutingMode, _Mapping]] = ...) -> None: ...
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    STOP_SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ROUTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MODALITIES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    temperature: float
    top_p: float
    top_k: float
    candidate_count: int
    max_output_tokens: int
    stop_sequences: _containers.RepeatedScalarFieldContainer[str]
    response_logprobs: bool
    logprobs: int
    presence_penalty: float
    frequency_penalty: float
    seed: int
    response_mime_type: str
    response_schema: _openapi_pb2.Schema
    routing_config: GenerationConfig.RoutingConfig
    audio_timestamp: bool
    response_modalities: _containers.RepeatedScalarFieldContainer[GenerationConfig.Modality]
    media_resolution: GenerationConfig.MediaResolution
    speech_config: SpeechConfig
    def __init__(self, temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., top_k: _Optional[float] = ..., candidate_count: _Optional[int] = ..., max_output_tokens: _Optional[int] = ..., stop_sequences: _Optional[_Iterable[str]] = ..., response_logprobs: bool = ..., logprobs: _Optional[int] = ..., presence_penalty: _Optional[float] = ..., frequency_penalty: _Optional[float] = ..., seed: _Optional[int] = ..., response_mime_type: _Optional[str] = ..., response_schema: _Optional[_Union[_openapi_pb2.Schema, _Mapping]] = ..., routing_config: _Optional[_Union[GenerationConfig.RoutingConfig, _Mapping]] = ..., audio_timestamp: bool = ..., response_modalities: _Optional[_Iterable[_Union[GenerationConfig.Modality, str]]] = ..., media_resolution: _Optional[_Union[GenerationConfig.MediaResolution, str]] = ..., speech_config: _Optional[_Union[SpeechConfig, _Mapping]] = ...) -> None: ...

class SafetySetting(_message.Message):
    __slots__ = ("category", "threshold", "method")
    class HarmBlockThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_BLOCK_THRESHOLD_UNSPECIFIED: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_LOW_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_MEDIUM_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_ONLY_HIGH: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_NONE: _ClassVar[SafetySetting.HarmBlockThreshold]
        OFF: _ClassVar[SafetySetting.HarmBlockThreshold]
    HARM_BLOCK_THRESHOLD_UNSPECIFIED: SafetySetting.HarmBlockThreshold
    BLOCK_LOW_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_MEDIUM_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_ONLY_HIGH: SafetySetting.HarmBlockThreshold
    BLOCK_NONE: SafetySetting.HarmBlockThreshold
    OFF: SafetySetting.HarmBlockThreshold
    class HarmBlockMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_BLOCK_METHOD_UNSPECIFIED: _ClassVar[SafetySetting.HarmBlockMethod]
        SEVERITY: _ClassVar[SafetySetting.HarmBlockMethod]
        PROBABILITY: _ClassVar[SafetySetting.HarmBlockMethod]
    HARM_BLOCK_METHOD_UNSPECIFIED: SafetySetting.HarmBlockMethod
    SEVERITY: SafetySetting.HarmBlockMethod
    PROBABILITY: SafetySetting.HarmBlockMethod
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    category: HarmCategory
    threshold: SafetySetting.HarmBlockThreshold
    method: SafetySetting.HarmBlockMethod
    def __init__(self, category: _Optional[_Union[HarmCategory, str]] = ..., threshold: _Optional[_Union[SafetySetting.HarmBlockThreshold, str]] = ..., method: _Optional[_Union[SafetySetting.HarmBlockMethod, str]] = ...) -> None: ...

class SafetyRating(_message.Message):
    __slots__ = ("category", "probability", "probability_score", "severity", "severity_score", "blocked")
    class HarmProbability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_PROBABILITY_UNSPECIFIED: _ClassVar[SafetyRating.HarmProbability]
        NEGLIGIBLE: _ClassVar[SafetyRating.HarmProbability]
        LOW: _ClassVar[SafetyRating.HarmProbability]
        MEDIUM: _ClassVar[SafetyRating.HarmProbability]
        HIGH: _ClassVar[SafetyRating.HarmProbability]
    HARM_PROBABILITY_UNSPECIFIED: SafetyRating.HarmProbability
    NEGLIGIBLE: SafetyRating.HarmProbability
    LOW: SafetyRating.HarmProbability
    MEDIUM: SafetyRating.HarmProbability
    HIGH: SafetyRating.HarmProbability
    class HarmSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_SEVERITY_UNSPECIFIED: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_NEGLIGIBLE: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_LOW: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_MEDIUM: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_HIGH: _ClassVar[SafetyRating.HarmSeverity]
    HARM_SEVERITY_UNSPECIFIED: SafetyRating.HarmSeverity
    HARM_SEVERITY_NEGLIGIBLE: SafetyRating.HarmSeverity
    HARM_SEVERITY_LOW: SafetyRating.HarmSeverity
    HARM_SEVERITY_MEDIUM: SafetyRating.HarmSeverity
    HARM_SEVERITY_HIGH: SafetyRating.HarmSeverity
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    category: HarmCategory
    probability: SafetyRating.HarmProbability
    probability_score: float
    severity: SafetyRating.HarmSeverity
    severity_score: float
    blocked: bool
    def __init__(self, category: _Optional[_Union[HarmCategory, str]] = ..., probability: _Optional[_Union[SafetyRating.HarmProbability, str]] = ..., probability_score: _Optional[float] = ..., severity: _Optional[_Union[SafetyRating.HarmSeverity, str]] = ..., severity_score: _Optional[float] = ..., blocked: bool = ...) -> None: ...

class CitationMetadata(_message.Message):
    __slots__ = ("citations",)
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    citations: _containers.RepeatedCompositeFieldContainer[Citation]
    def __init__(self, citations: _Optional[_Iterable[_Union[Citation, _Mapping]]] = ...) -> None: ...

class Citation(_message.Message):
    __slots__ = ("start_index", "end_index", "uri", "title", "license", "publication_date")
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_INDEX_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    start_index: int
    end_index: int
    uri: str
    title: str
    license: str
    publication_date: _date_pb2.Date
    def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ..., uri: _Optional[str] = ..., title: _Optional[str] = ..., license: _Optional[str] = ..., publication_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class Candidate(_message.Message):
    __slots__ = ("index", "content", "avg_logprobs", "logprobs_result", "finish_reason", "safety_ratings", "finish_message", "citation_metadata", "grounding_metadata")
    class FinishReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FINISH_REASON_UNSPECIFIED: _ClassVar[Candidate.FinishReason]
        STOP: _ClassVar[Candidate.FinishReason]
        MAX_TOKENS: _ClassVar[Candidate.FinishReason]
        SAFETY: _ClassVar[Candidate.FinishReason]
        RECITATION: _ClassVar[Candidate.FinishReason]
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
    OTHER: Candidate.FinishReason
    BLOCKLIST: Candidate.FinishReason
    PROHIBITED_CONTENT: Candidate.FinishReason
    SPII: Candidate.FinishReason
    MALFORMED_FUNCTION_CALL: Candidate.FinishReason
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AVG_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_RESULT_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RATINGS_FIELD_NUMBER: _ClassVar[int]
    FINISH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CITATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_METADATA_FIELD_NUMBER: _ClassVar[int]
    index: int
    content: Content
    avg_logprobs: float
    logprobs_result: LogprobsResult
    finish_reason: Candidate.FinishReason
    safety_ratings: _containers.RepeatedCompositeFieldContainer[SafetyRating]
    finish_message: str
    citation_metadata: CitationMetadata
    grounding_metadata: GroundingMetadata
    def __init__(self, index: _Optional[int] = ..., content: _Optional[_Union[Content, _Mapping]] = ..., avg_logprobs: _Optional[float] = ..., logprobs_result: _Optional[_Union[LogprobsResult, _Mapping]] = ..., finish_reason: _Optional[_Union[Candidate.FinishReason, str]] = ..., safety_ratings: _Optional[_Iterable[_Union[SafetyRating, _Mapping]]] = ..., finish_message: _Optional[str] = ..., citation_metadata: _Optional[_Union[CitationMetadata, _Mapping]] = ..., grounding_metadata: _Optional[_Union[GroundingMetadata, _Mapping]] = ...) -> None: ...

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

class GroundingChunk(_message.Message):
    __slots__ = ("web", "retrieved_context")
    class Web(_message.Message):
        __slots__ = ("uri", "title")
        URI_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        uri: str
        title: str
        def __init__(self, uri: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
    class RetrievedContext(_message.Message):
        __slots__ = ("uri", "title", "text")
        URI_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        uri: str
        title: str
        text: str
        def __init__(self, uri: _Optional[str] = ..., title: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    WEB_FIELD_NUMBER: _ClassVar[int]
    RETRIEVED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    web: GroundingChunk.Web
    retrieved_context: GroundingChunk.RetrievedContext
    def __init__(self, web: _Optional[_Union[GroundingChunk.Web, _Mapping]] = ..., retrieved_context: _Optional[_Union[GroundingChunk.RetrievedContext, _Mapping]] = ...) -> None: ...

class GroundingSupport(_message.Message):
    __slots__ = ("segment", "grounding_chunk_indices", "confidence_scores")
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_CHUNK_INDICES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORES_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    grounding_chunk_indices: _containers.RepeatedScalarFieldContainer[int]
    confidence_scores: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ..., grounding_chunk_indices: _Optional[_Iterable[int]] = ..., confidence_scores: _Optional[_Iterable[float]] = ...) -> None: ...

class GroundingMetadata(_message.Message):
    __slots__ = ("web_search_queries", "search_entry_point", "retrieval_queries", "grounding_chunks", "grounding_supports", "retrieval_metadata")
    WEB_SEARCH_QUERIES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_QUERIES_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_SUPPORTS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    web_search_queries: _containers.RepeatedScalarFieldContainer[str]
    search_entry_point: SearchEntryPoint
    retrieval_queries: _containers.RepeatedScalarFieldContainer[str]
    grounding_chunks: _containers.RepeatedCompositeFieldContainer[GroundingChunk]
    grounding_supports: _containers.RepeatedCompositeFieldContainer[GroundingSupport]
    retrieval_metadata: RetrievalMetadata
    def __init__(self, web_search_queries: _Optional[_Iterable[str]] = ..., search_entry_point: _Optional[_Union[SearchEntryPoint, _Mapping]] = ..., retrieval_queries: _Optional[_Iterable[str]] = ..., grounding_chunks: _Optional[_Iterable[_Union[GroundingChunk, _Mapping]]] = ..., grounding_supports: _Optional[_Iterable[_Union[GroundingSupport, _Mapping]]] = ..., retrieval_metadata: _Optional[_Union[RetrievalMetadata, _Mapping]] = ...) -> None: ...

class SearchEntryPoint(_message.Message):
    __slots__ = ("rendered_content", "sdk_blob")
    RENDERED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    SDK_BLOB_FIELD_NUMBER: _ClassVar[int]
    rendered_content: str
    sdk_blob: bytes
    def __init__(self, rendered_content: _Optional[str] = ..., sdk_blob: _Optional[bytes] = ...) -> None: ...

class RetrievalMetadata(_message.Message):
    __slots__ = ("google_search_dynamic_retrieval_score",)
    GOOGLE_SEARCH_DYNAMIC_RETRIEVAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    google_search_dynamic_retrieval_score: float
    def __init__(self, google_search_dynamic_retrieval_score: _Optional[float] = ...) -> None: ...
