from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import grounding_pb2 as _grounding_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroundedGenerationContent(_message.Message):
    __slots__ = ("role", "parts")
    class Part(_message.Message):
        __slots__ = ("text",)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    role: str
    parts: _containers.RepeatedCompositeFieldContainer[GroundedGenerationContent.Part]
    def __init__(self, role: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[GroundedGenerationContent.Part, _Mapping]]] = ...) -> None: ...

class GenerateGroundedContentRequest(_message.Message):
    __slots__ = ("location", "system_instruction", "contents", "generation_spec", "grounding_spec", "user_labels")
    class GenerationSpec(_message.Message):
        __slots__ = ("model_id", "language_code", "temperature", "top_p", "top_k", "frequency_penalty", "presence_penalty", "max_output_tokens")
        MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        TOP_P_FIELD_NUMBER: _ClassVar[int]
        TOP_K_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
        PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
        MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
        model_id: str
        language_code: str
        temperature: float
        top_p: float
        top_k: int
        frequency_penalty: float
        presence_penalty: float
        max_output_tokens: int
        def __init__(self, model_id: _Optional[str] = ..., language_code: _Optional[str] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ..., frequency_penalty: _Optional[float] = ..., presence_penalty: _Optional[float] = ..., max_output_tokens: _Optional[int] = ...) -> None: ...
    class DynamicRetrievalConfiguration(_message.Message):
        __slots__ = ("predictor",)
        class DynamicRetrievalPredictor(_message.Message):
            __slots__ = ("version", "threshold")
            class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                VERSION_UNSPECIFIED: _ClassVar[GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version]
                V1_INDEPENDENT: _ClassVar[GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version]
            VERSION_UNSPECIFIED: GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version
            V1_INDEPENDENT: GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version
            VERSION_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            version: GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version
            threshold: float
            def __init__(self, version: _Optional[_Union[GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version, str]] = ..., threshold: _Optional[float] = ...) -> None: ...
        PREDICTOR_FIELD_NUMBER: _ClassVar[int]
        predictor: GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor
        def __init__(self, predictor: _Optional[_Union[GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor, _Mapping]] = ...) -> None: ...
    class GroundingSource(_message.Message):
        __slots__ = ("inline_source", "search_source", "google_search_source")
        class InlineSource(_message.Message):
            __slots__ = ("grounding_facts", "attributes")
            class AttributesEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            GROUNDING_FACTS_FIELD_NUMBER: _ClassVar[int]
            ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
            grounding_facts: _containers.RepeatedCompositeFieldContainer[_grounding_pb2.GroundingFact]
            attributes: _containers.ScalarMap[str, str]
            def __init__(self, grounding_facts: _Optional[_Iterable[_Union[_grounding_pb2.GroundingFact, _Mapping]]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...
        class SearchSource(_message.Message):
            __slots__ = ("serving_config", "max_result_count", "filter", "safe_search")
            SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
            MAX_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
            FILTER_FIELD_NUMBER: _ClassVar[int]
            SAFE_SEARCH_FIELD_NUMBER: _ClassVar[int]
            serving_config: str
            max_result_count: int
            filter: str
            safe_search: bool
            def __init__(self, serving_config: _Optional[str] = ..., max_result_count: _Optional[int] = ..., filter: _Optional[str] = ..., safe_search: bool = ...) -> None: ...
        class GoogleSearchSource(_message.Message):
            __slots__ = ("dynamic_retrieval_config",)
            DYNAMIC_RETRIEVAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
            dynamic_retrieval_config: GenerateGroundedContentRequest.DynamicRetrievalConfiguration
            def __init__(self, dynamic_retrieval_config: _Optional[_Union[GenerateGroundedContentRequest.DynamicRetrievalConfiguration, _Mapping]] = ...) -> None: ...
        INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
        SEARCH_SOURCE_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_SEARCH_SOURCE_FIELD_NUMBER: _ClassVar[int]
        inline_source: GenerateGroundedContentRequest.GroundingSource.InlineSource
        search_source: GenerateGroundedContentRequest.GroundingSource.SearchSource
        google_search_source: GenerateGroundedContentRequest.GroundingSource.GoogleSearchSource
        def __init__(self, inline_source: _Optional[_Union[GenerateGroundedContentRequest.GroundingSource.InlineSource, _Mapping]] = ..., search_source: _Optional[_Union[GenerateGroundedContentRequest.GroundingSource.SearchSource, _Mapping]] = ..., google_search_source: _Optional[_Union[GenerateGroundedContentRequest.GroundingSource.GoogleSearchSource, _Mapping]] = ...) -> None: ...
    class GroundingSpec(_message.Message):
        __slots__ = ("grounding_sources",)
        GROUNDING_SOURCES_FIELD_NUMBER: _ClassVar[int]
        grounding_sources: _containers.RepeatedCompositeFieldContainer[GenerateGroundedContentRequest.GroundingSource]
        def __init__(self, grounding_sources: _Optional[_Iterable[_Union[GenerateGroundedContentRequest.GroundingSource, _Mapping]]] = ...) -> None: ...
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    GENERATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_SPEC_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    location: str
    system_instruction: GroundedGenerationContent
    contents: _containers.RepeatedCompositeFieldContainer[GroundedGenerationContent]
    generation_spec: GenerateGroundedContentRequest.GenerationSpec
    grounding_spec: GenerateGroundedContentRequest.GroundingSpec
    user_labels: _containers.ScalarMap[str, str]
    def __init__(self, location: _Optional[str] = ..., system_instruction: _Optional[_Union[GroundedGenerationContent, _Mapping]] = ..., contents: _Optional[_Iterable[_Union[GroundedGenerationContent, _Mapping]]] = ..., generation_spec: _Optional[_Union[GenerateGroundedContentRequest.GenerationSpec, _Mapping]] = ..., grounding_spec: _Optional[_Union[GenerateGroundedContentRequest.GroundingSpec, _Mapping]] = ..., user_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GenerateGroundedContentResponse(_message.Message):
    __slots__ = ("candidates",)
    class Candidate(_message.Message):
        __slots__ = ("index", "content", "grounding_score", "grounding_metadata")
        class GroundingMetadata(_message.Message):
            __slots__ = ("retrieval_metadata", "support_chunks", "web_search_queries", "search_entry_point", "grounding_support")
            class RetrievalMetadata(_message.Message):
                __slots__ = ("source", "dynamic_retrieval_metadata")
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNSPECIFIED: _ClassVar[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source]
                    VERTEX_AI_SEARCH: _ClassVar[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source]
                    GOOGLE_SEARCH: _ClassVar[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source]
                    INLINE_CONTENT: _ClassVar[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source]
                    GOOGLE_MAPS: _ClassVar[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source]
                SOURCE_UNSPECIFIED: GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source
                VERTEX_AI_SEARCH: GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source
                GOOGLE_SEARCH: GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source
                INLINE_CONTENT: GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source
                GOOGLE_MAPS: GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                DYNAMIC_RETRIEVAL_METADATA_FIELD_NUMBER: _ClassVar[int]
                source: GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source
                dynamic_retrieval_metadata: GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalMetadata
                def __init__(self, source: _Optional[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source, str]] = ..., dynamic_retrieval_metadata: _Optional[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalMetadata, _Mapping]] = ...) -> None: ...
            class DynamicRetrievalMetadata(_message.Message):
                __slots__ = ("predictor_metadata",)
                PREDICTOR_METADATA_FIELD_NUMBER: _ClassVar[int]
                predictor_metadata: GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata
                def __init__(self, predictor_metadata: _Optional[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata, _Mapping]] = ...) -> None: ...
            class DynamicRetrievalPredictorMetadata(_message.Message):
                __slots__ = ("version", "prediction")
                class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    VERSION_UNSPECIFIED: _ClassVar[GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version]
                    V1_INDEPENDENT: _ClassVar[GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version]
                VERSION_UNSPECIFIED: GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version
                V1_INDEPENDENT: GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version
                VERSION_FIELD_NUMBER: _ClassVar[int]
                PREDICTION_FIELD_NUMBER: _ClassVar[int]
                version: GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version
                prediction: float
                def __init__(self, version: _Optional[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version, str]] = ..., prediction: _Optional[float] = ...) -> None: ...
            class SearchEntryPoint(_message.Message):
                __slots__ = ("rendered_content", "sdk_blob")
                RENDERED_CONTENT_FIELD_NUMBER: _ClassVar[int]
                SDK_BLOB_FIELD_NUMBER: _ClassVar[int]
                rendered_content: str
                sdk_blob: bytes
                def __init__(self, rendered_content: _Optional[str] = ..., sdk_blob: _Optional[bytes] = ...) -> None: ...
            class GroundingSupport(_message.Message):
                __slots__ = ("claim_text", "support_chunk_indices", "support_score")
                CLAIM_TEXT_FIELD_NUMBER: _ClassVar[int]
                SUPPORT_CHUNK_INDICES_FIELD_NUMBER: _ClassVar[int]
                SUPPORT_SCORE_FIELD_NUMBER: _ClassVar[int]
                claim_text: str
                support_chunk_indices: _containers.RepeatedScalarFieldContainer[int]
                support_score: float
                def __init__(self, claim_text: _Optional[str] = ..., support_chunk_indices: _Optional[_Iterable[int]] = ..., support_score: _Optional[float] = ...) -> None: ...
            RETRIEVAL_METADATA_FIELD_NUMBER: _ClassVar[int]
            SUPPORT_CHUNKS_FIELD_NUMBER: _ClassVar[int]
            WEB_SEARCH_QUERIES_FIELD_NUMBER: _ClassVar[int]
            SEARCH_ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
            GROUNDING_SUPPORT_FIELD_NUMBER: _ClassVar[int]
            retrieval_metadata: _containers.RepeatedCompositeFieldContainer[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata]
            support_chunks: _containers.RepeatedCompositeFieldContainer[_grounding_pb2.FactChunk]
            web_search_queries: _containers.RepeatedScalarFieldContainer[str]
            search_entry_point: GenerateGroundedContentResponse.Candidate.GroundingMetadata.SearchEntryPoint
            grounding_support: _containers.RepeatedCompositeFieldContainer[GenerateGroundedContentResponse.Candidate.GroundingMetadata.GroundingSupport]
            def __init__(self, retrieval_metadata: _Optional[_Iterable[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata, _Mapping]]] = ..., support_chunks: _Optional[_Iterable[_Union[_grounding_pb2.FactChunk, _Mapping]]] = ..., web_search_queries: _Optional[_Iterable[str]] = ..., search_entry_point: _Optional[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata.SearchEntryPoint, _Mapping]] = ..., grounding_support: _Optional[_Iterable[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata.GroundingSupport, _Mapping]]] = ...) -> None: ...
        INDEX_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        GROUNDING_SCORE_FIELD_NUMBER: _ClassVar[int]
        GROUNDING_METADATA_FIELD_NUMBER: _ClassVar[int]
        index: int
        content: GroundedGenerationContent
        grounding_score: float
        grounding_metadata: GenerateGroundedContentResponse.Candidate.GroundingMetadata
        def __init__(self, index: _Optional[int] = ..., content: _Optional[_Union[GroundedGenerationContent, _Mapping]] = ..., grounding_score: _Optional[float] = ..., grounding_metadata: _Optional[_Union[GenerateGroundedContentResponse.Candidate.GroundingMetadata, _Mapping]] = ...) -> None: ...
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[GenerateGroundedContentResponse.Candidate]
    def __init__(self, candidates: _Optional[_Iterable[_Union[GenerateGroundedContentResponse.Candidate, _Mapping]]] = ...) -> None: ...

class CheckGroundingSpec(_message.Message):
    __slots__ = ("citation_threshold",)
    CITATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    citation_threshold: float
    def __init__(self, citation_threshold: _Optional[float] = ...) -> None: ...

class CheckGroundingRequest(_message.Message):
    __slots__ = ("grounding_config", "answer_candidate", "facts", "grounding_spec", "user_labels")
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GROUNDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANSWER_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_SPEC_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    grounding_config: str
    answer_candidate: str
    facts: _containers.RepeatedCompositeFieldContainer[_grounding_pb2.GroundingFact]
    grounding_spec: CheckGroundingSpec
    user_labels: _containers.ScalarMap[str, str]
    def __init__(self, grounding_config: _Optional[str] = ..., answer_candidate: _Optional[str] = ..., facts: _Optional[_Iterable[_Union[_grounding_pb2.GroundingFact, _Mapping]]] = ..., grounding_spec: _Optional[_Union[CheckGroundingSpec, _Mapping]] = ..., user_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CheckGroundingResponse(_message.Message):
    __slots__ = ("support_score", "cited_chunks", "cited_facts", "claims")
    class CheckGroundingFactChunk(_message.Message):
        __slots__ = ("chunk_text",)
        CHUNK_TEXT_FIELD_NUMBER: _ClassVar[int]
        chunk_text: str
        def __init__(self, chunk_text: _Optional[str] = ...) -> None: ...
    class Claim(_message.Message):
        __slots__ = ("start_pos", "end_pos", "claim_text", "citation_indices", "grounding_check_required")
        START_POS_FIELD_NUMBER: _ClassVar[int]
        END_POS_FIELD_NUMBER: _ClassVar[int]
        CLAIM_TEXT_FIELD_NUMBER: _ClassVar[int]
        CITATION_INDICES_FIELD_NUMBER: _ClassVar[int]
        GROUNDING_CHECK_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        start_pos: int
        end_pos: int
        claim_text: str
        citation_indices: _containers.RepeatedScalarFieldContainer[int]
        grounding_check_required: bool
        def __init__(self, start_pos: _Optional[int] = ..., end_pos: _Optional[int] = ..., claim_text: _Optional[str] = ..., citation_indices: _Optional[_Iterable[int]] = ..., grounding_check_required: bool = ...) -> None: ...
    SUPPORT_SCORE_FIELD_NUMBER: _ClassVar[int]
    CITED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    CITED_FACTS_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    support_score: float
    cited_chunks: _containers.RepeatedCompositeFieldContainer[_grounding_pb2.FactChunk]
    cited_facts: _containers.RepeatedCompositeFieldContainer[CheckGroundingResponse.CheckGroundingFactChunk]
    claims: _containers.RepeatedCompositeFieldContainer[CheckGroundingResponse.Claim]
    def __init__(self, support_score: _Optional[float] = ..., cited_chunks: _Optional[_Iterable[_Union[_grounding_pb2.FactChunk, _Mapping]]] = ..., cited_facts: _Optional[_Iterable[_Union[CheckGroundingResponse.CheckGroundingFactChunk, _Mapping]]] = ..., claims: _Optional[_Iterable[_Union[CheckGroundingResponse.Claim, _Mapping]]] = ...) -> None: ...
