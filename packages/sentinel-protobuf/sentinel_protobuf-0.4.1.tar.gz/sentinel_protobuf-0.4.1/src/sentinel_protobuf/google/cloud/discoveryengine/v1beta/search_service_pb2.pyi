from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import chunk_pb2 as _chunk_pb2
from google.cloud.discoveryengine.v1beta import common_pb2 as _common_pb2
from google.cloud.discoveryengine.v1beta import document_pb2 as _document_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchRequest(_message.Message):
    __slots__ = ("serving_config", "branch", "query", "image_query", "page_size", "page_token", "offset", "one_box_page_size", "data_store_specs", "filter", "canonical_filter", "order_by", "user_info", "language_code", "region_code", "facet_specs", "boost_spec", "params", "query_expansion_spec", "spell_correction_spec", "user_pseudo_id", "content_search_spec", "embedding_spec", "ranking_expression", "safe_search", "user_labels", "natural_language_query_understanding_spec", "search_as_you_type_spec", "session", "session_spec", "relevance_threshold", "personalization_spec")
    class RelevanceThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELEVANCE_THRESHOLD_UNSPECIFIED: _ClassVar[SearchRequest.RelevanceThreshold]
        LOWEST: _ClassVar[SearchRequest.RelevanceThreshold]
        LOW: _ClassVar[SearchRequest.RelevanceThreshold]
        MEDIUM: _ClassVar[SearchRequest.RelevanceThreshold]
        HIGH: _ClassVar[SearchRequest.RelevanceThreshold]
    RELEVANCE_THRESHOLD_UNSPECIFIED: SearchRequest.RelevanceThreshold
    LOWEST: SearchRequest.RelevanceThreshold
    LOW: SearchRequest.RelevanceThreshold
    MEDIUM: SearchRequest.RelevanceThreshold
    HIGH: SearchRequest.RelevanceThreshold
    class ImageQuery(_message.Message):
        __slots__ = ("image_bytes",)
        IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        image_bytes: str
        def __init__(self, image_bytes: _Optional[str] = ...) -> None: ...
    class DataStoreSpec(_message.Message):
        __slots__ = ("data_store", "filter")
        DATA_STORE_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        data_store: str
        filter: str
        def __init__(self, data_store: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...
    class FacetSpec(_message.Message):
        __slots__ = ("facet_key", "limit", "excluded_filter_keys", "enable_dynamic_position")
        class FacetKey(_message.Message):
            __slots__ = ("key", "intervals", "restricted_values", "prefixes", "contains", "case_insensitive", "order_by")
            KEY_FIELD_NUMBER: _ClassVar[int]
            INTERVALS_FIELD_NUMBER: _ClassVar[int]
            RESTRICTED_VALUES_FIELD_NUMBER: _ClassVar[int]
            PREFIXES_FIELD_NUMBER: _ClassVar[int]
            CONTAINS_FIELD_NUMBER: _ClassVar[int]
            CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
            ORDER_BY_FIELD_NUMBER: _ClassVar[int]
            key: str
            intervals: _containers.RepeatedCompositeFieldContainer[_common_pb2.Interval]
            restricted_values: _containers.RepeatedScalarFieldContainer[str]
            prefixes: _containers.RepeatedScalarFieldContainer[str]
            contains: _containers.RepeatedScalarFieldContainer[str]
            case_insensitive: bool
            order_by: str
            def __init__(self, key: _Optional[str] = ..., intervals: _Optional[_Iterable[_Union[_common_pb2.Interval, _Mapping]]] = ..., restricted_values: _Optional[_Iterable[str]] = ..., prefixes: _Optional[_Iterable[str]] = ..., contains: _Optional[_Iterable[str]] = ..., case_insensitive: bool = ..., order_by: _Optional[str] = ...) -> None: ...
        FACET_KEY_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_FILTER_KEYS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_DYNAMIC_POSITION_FIELD_NUMBER: _ClassVar[int]
        facet_key: SearchRequest.FacetSpec.FacetKey
        limit: int
        excluded_filter_keys: _containers.RepeatedScalarFieldContainer[str]
        enable_dynamic_position: bool
        def __init__(self, facet_key: _Optional[_Union[SearchRequest.FacetSpec.FacetKey, _Mapping]] = ..., limit: _Optional[int] = ..., excluded_filter_keys: _Optional[_Iterable[str]] = ..., enable_dynamic_position: bool = ...) -> None: ...
    class BoostSpec(_message.Message):
        __slots__ = ("condition_boost_specs",)
        class ConditionBoostSpec(_message.Message):
            __slots__ = ("condition", "boost", "boost_control_spec")
            class BoostControlSpec(_message.Message):
                __slots__ = ("field_name", "attribute_type", "interpolation_type", "control_points")
                class AttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    ATTRIBUTE_TYPE_UNSPECIFIED: _ClassVar[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                    NUMERICAL: _ClassVar[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                    FRESHNESS: _ClassVar[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                ATTRIBUTE_TYPE_UNSPECIFIED: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                NUMERICAL: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                FRESHNESS: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                class InterpolationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    INTERPOLATION_TYPE_UNSPECIFIED: _ClassVar[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType]
                    LINEAR: _ClassVar[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType]
                INTERPOLATION_TYPE_UNSPECIFIED: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
                LINEAR: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
                class ControlPoint(_message.Message):
                    __slots__ = ("attribute_value", "boost_amount")
                    ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
                    BOOST_AMOUNT_FIELD_NUMBER: _ClassVar[int]
                    attribute_value: str
                    boost_amount: float
                    def __init__(self, attribute_value: _Optional[str] = ..., boost_amount: _Optional[float] = ...) -> None: ...
                FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
                ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
                INTERPOLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
                CONTROL_POINTS_FIELD_NUMBER: _ClassVar[int]
                field_name: str
                attribute_type: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                interpolation_type: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
                control_points: _containers.RepeatedCompositeFieldContainer[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint]
                def __init__(self, field_name: _Optional[str] = ..., attribute_type: _Optional[_Union[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType, str]] = ..., interpolation_type: _Optional[_Union[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType, str]] = ..., control_points: _Optional[_Iterable[_Union[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint, _Mapping]]] = ...) -> None: ...
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            BOOST_FIELD_NUMBER: _ClassVar[int]
            BOOST_CONTROL_SPEC_FIELD_NUMBER: _ClassVar[int]
            condition: str
            boost: float
            boost_control_spec: SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec
            def __init__(self, condition: _Optional[str] = ..., boost: _Optional[float] = ..., boost_control_spec: _Optional[_Union[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec, _Mapping]] = ...) -> None: ...
        CONDITION_BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
        condition_boost_specs: _containers.RepeatedCompositeFieldContainer[SearchRequest.BoostSpec.ConditionBoostSpec]
        def __init__(self, condition_boost_specs: _Optional[_Iterable[_Union[SearchRequest.BoostSpec.ConditionBoostSpec, _Mapping]]] = ...) -> None: ...
    class QueryExpansionSpec(_message.Message):
        __slots__ = ("condition", "pin_unexpanded_results")
        class Condition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONDITION_UNSPECIFIED: _ClassVar[SearchRequest.QueryExpansionSpec.Condition]
            DISABLED: _ClassVar[SearchRequest.QueryExpansionSpec.Condition]
            AUTO: _ClassVar[SearchRequest.QueryExpansionSpec.Condition]
        CONDITION_UNSPECIFIED: SearchRequest.QueryExpansionSpec.Condition
        DISABLED: SearchRequest.QueryExpansionSpec.Condition
        AUTO: SearchRequest.QueryExpansionSpec.Condition
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        PIN_UNEXPANDED_RESULTS_FIELD_NUMBER: _ClassVar[int]
        condition: SearchRequest.QueryExpansionSpec.Condition
        pin_unexpanded_results: bool
        def __init__(self, condition: _Optional[_Union[SearchRequest.QueryExpansionSpec.Condition, str]] = ..., pin_unexpanded_results: bool = ...) -> None: ...
    class SpellCorrectionSpec(_message.Message):
        __slots__ = ("mode",)
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[SearchRequest.SpellCorrectionSpec.Mode]
            SUGGESTION_ONLY: _ClassVar[SearchRequest.SpellCorrectionSpec.Mode]
            AUTO: _ClassVar[SearchRequest.SpellCorrectionSpec.Mode]
        MODE_UNSPECIFIED: SearchRequest.SpellCorrectionSpec.Mode
        SUGGESTION_ONLY: SearchRequest.SpellCorrectionSpec.Mode
        AUTO: SearchRequest.SpellCorrectionSpec.Mode
        MODE_FIELD_NUMBER: _ClassVar[int]
        mode: SearchRequest.SpellCorrectionSpec.Mode
        def __init__(self, mode: _Optional[_Union[SearchRequest.SpellCorrectionSpec.Mode, str]] = ...) -> None: ...
    class ContentSearchSpec(_message.Message):
        __slots__ = ("snippet_spec", "summary_spec", "extractive_content_spec", "search_result_mode", "chunk_spec")
        class SearchResultMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEARCH_RESULT_MODE_UNSPECIFIED: _ClassVar[SearchRequest.ContentSearchSpec.SearchResultMode]
            DOCUMENTS: _ClassVar[SearchRequest.ContentSearchSpec.SearchResultMode]
            CHUNKS: _ClassVar[SearchRequest.ContentSearchSpec.SearchResultMode]
        SEARCH_RESULT_MODE_UNSPECIFIED: SearchRequest.ContentSearchSpec.SearchResultMode
        DOCUMENTS: SearchRequest.ContentSearchSpec.SearchResultMode
        CHUNKS: SearchRequest.ContentSearchSpec.SearchResultMode
        class SnippetSpec(_message.Message):
            __slots__ = ("max_snippet_count", "reference_only", "return_snippet")
            MAX_SNIPPET_COUNT_FIELD_NUMBER: _ClassVar[int]
            REFERENCE_ONLY_FIELD_NUMBER: _ClassVar[int]
            RETURN_SNIPPET_FIELD_NUMBER: _ClassVar[int]
            max_snippet_count: int
            reference_only: bool
            return_snippet: bool
            def __init__(self, max_snippet_count: _Optional[int] = ..., reference_only: bool = ..., return_snippet: bool = ...) -> None: ...
        class SummarySpec(_message.Message):
            __slots__ = ("summary_result_count", "include_citations", "ignore_adversarial_query", "ignore_non_summary_seeking_query", "ignore_low_relevant_content", "ignore_jail_breaking_query", "model_prompt_spec", "language_code", "model_spec", "use_semantic_chunks")
            class ModelPromptSpec(_message.Message):
                __slots__ = ("preamble",)
                PREAMBLE_FIELD_NUMBER: _ClassVar[int]
                preamble: str
                def __init__(self, preamble: _Optional[str] = ...) -> None: ...
            class ModelSpec(_message.Message):
                __slots__ = ("version",)
                VERSION_FIELD_NUMBER: _ClassVar[int]
                version: str
                def __init__(self, version: _Optional[str] = ...) -> None: ...
            SUMMARY_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_CITATIONS_FIELD_NUMBER: _ClassVar[int]
            IGNORE_ADVERSARIAL_QUERY_FIELD_NUMBER: _ClassVar[int]
            IGNORE_NON_SUMMARY_SEEKING_QUERY_FIELD_NUMBER: _ClassVar[int]
            IGNORE_LOW_RELEVANT_CONTENT_FIELD_NUMBER: _ClassVar[int]
            IGNORE_JAIL_BREAKING_QUERY_FIELD_NUMBER: _ClassVar[int]
            MODEL_PROMPT_SPEC_FIELD_NUMBER: _ClassVar[int]
            LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
            MODEL_SPEC_FIELD_NUMBER: _ClassVar[int]
            USE_SEMANTIC_CHUNKS_FIELD_NUMBER: _ClassVar[int]
            summary_result_count: int
            include_citations: bool
            ignore_adversarial_query: bool
            ignore_non_summary_seeking_query: bool
            ignore_low_relevant_content: bool
            ignore_jail_breaking_query: bool
            model_prompt_spec: SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec
            language_code: str
            model_spec: SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec
            use_semantic_chunks: bool
            def __init__(self, summary_result_count: _Optional[int] = ..., include_citations: bool = ..., ignore_adversarial_query: bool = ..., ignore_non_summary_seeking_query: bool = ..., ignore_low_relevant_content: bool = ..., ignore_jail_breaking_query: bool = ..., model_prompt_spec: _Optional[_Union[SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec, _Mapping]] = ..., language_code: _Optional[str] = ..., model_spec: _Optional[_Union[SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec, _Mapping]] = ..., use_semantic_chunks: bool = ...) -> None: ...
        class ExtractiveContentSpec(_message.Message):
            __slots__ = ("max_extractive_answer_count", "max_extractive_segment_count", "return_extractive_segment_score", "num_previous_segments", "num_next_segments")
            MAX_EXTRACTIVE_ANSWER_COUNT_FIELD_NUMBER: _ClassVar[int]
            MAX_EXTRACTIVE_SEGMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            RETURN_EXTRACTIVE_SEGMENT_SCORE_FIELD_NUMBER: _ClassVar[int]
            NUM_PREVIOUS_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
            NUM_NEXT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
            max_extractive_answer_count: int
            max_extractive_segment_count: int
            return_extractive_segment_score: bool
            num_previous_segments: int
            num_next_segments: int
            def __init__(self, max_extractive_answer_count: _Optional[int] = ..., max_extractive_segment_count: _Optional[int] = ..., return_extractive_segment_score: bool = ..., num_previous_segments: _Optional[int] = ..., num_next_segments: _Optional[int] = ...) -> None: ...
        class ChunkSpec(_message.Message):
            __slots__ = ("num_previous_chunks", "num_next_chunks")
            NUM_PREVIOUS_CHUNKS_FIELD_NUMBER: _ClassVar[int]
            NUM_NEXT_CHUNKS_FIELD_NUMBER: _ClassVar[int]
            num_previous_chunks: int
            num_next_chunks: int
            def __init__(self, num_previous_chunks: _Optional[int] = ..., num_next_chunks: _Optional[int] = ...) -> None: ...
        SNIPPET_SPEC_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_SPEC_FIELD_NUMBER: _ClassVar[int]
        EXTRACTIVE_CONTENT_SPEC_FIELD_NUMBER: _ClassVar[int]
        SEARCH_RESULT_MODE_FIELD_NUMBER: _ClassVar[int]
        CHUNK_SPEC_FIELD_NUMBER: _ClassVar[int]
        snippet_spec: SearchRequest.ContentSearchSpec.SnippetSpec
        summary_spec: SearchRequest.ContentSearchSpec.SummarySpec
        extractive_content_spec: SearchRequest.ContentSearchSpec.ExtractiveContentSpec
        search_result_mode: SearchRequest.ContentSearchSpec.SearchResultMode
        chunk_spec: SearchRequest.ContentSearchSpec.ChunkSpec
        def __init__(self, snippet_spec: _Optional[_Union[SearchRequest.ContentSearchSpec.SnippetSpec, _Mapping]] = ..., summary_spec: _Optional[_Union[SearchRequest.ContentSearchSpec.SummarySpec, _Mapping]] = ..., extractive_content_spec: _Optional[_Union[SearchRequest.ContentSearchSpec.ExtractiveContentSpec, _Mapping]] = ..., search_result_mode: _Optional[_Union[SearchRequest.ContentSearchSpec.SearchResultMode, str]] = ..., chunk_spec: _Optional[_Union[SearchRequest.ContentSearchSpec.ChunkSpec, _Mapping]] = ...) -> None: ...
    class EmbeddingSpec(_message.Message):
        __slots__ = ("embedding_vectors",)
        class EmbeddingVector(_message.Message):
            __slots__ = ("field_path", "vector")
            FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
            VECTOR_FIELD_NUMBER: _ClassVar[int]
            field_path: str
            vector: _containers.RepeatedScalarFieldContainer[float]
            def __init__(self, field_path: _Optional[str] = ..., vector: _Optional[_Iterable[float]] = ...) -> None: ...
        EMBEDDING_VECTORS_FIELD_NUMBER: _ClassVar[int]
        embedding_vectors: _containers.RepeatedCompositeFieldContainer[SearchRequest.EmbeddingSpec.EmbeddingVector]
        def __init__(self, embedding_vectors: _Optional[_Iterable[_Union[SearchRequest.EmbeddingSpec.EmbeddingVector, _Mapping]]] = ...) -> None: ...
    class NaturalLanguageQueryUnderstandingSpec(_message.Message):
        __slots__ = ("filter_extraction_condition", "geo_search_query_detection_field_names")
        class FilterExtractionCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONDITION_UNSPECIFIED: _ClassVar[SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition]
            DISABLED: _ClassVar[SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition]
            ENABLED: _ClassVar[SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition]
        CONDITION_UNSPECIFIED: SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition
        DISABLED: SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition
        ENABLED: SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition
        FILTER_EXTRACTION_CONDITION_FIELD_NUMBER: _ClassVar[int]
        GEO_SEARCH_QUERY_DETECTION_FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
        filter_extraction_condition: SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition
        geo_search_query_detection_field_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, filter_extraction_condition: _Optional[_Union[SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition, str]] = ..., geo_search_query_detection_field_names: _Optional[_Iterable[str]] = ...) -> None: ...
    class SearchAsYouTypeSpec(_message.Message):
        __slots__ = ("condition",)
        class Condition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONDITION_UNSPECIFIED: _ClassVar[SearchRequest.SearchAsYouTypeSpec.Condition]
            DISABLED: _ClassVar[SearchRequest.SearchAsYouTypeSpec.Condition]
            ENABLED: _ClassVar[SearchRequest.SearchAsYouTypeSpec.Condition]
        CONDITION_UNSPECIFIED: SearchRequest.SearchAsYouTypeSpec.Condition
        DISABLED: SearchRequest.SearchAsYouTypeSpec.Condition
        ENABLED: SearchRequest.SearchAsYouTypeSpec.Condition
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        condition: SearchRequest.SearchAsYouTypeSpec.Condition
        def __init__(self, condition: _Optional[_Union[SearchRequest.SearchAsYouTypeSpec.Condition, str]] = ...) -> None: ...
    class SessionSpec(_message.Message):
        __slots__ = ("query_id", "search_result_persistence_count")
        QUERY_ID_FIELD_NUMBER: _ClassVar[int]
        SEARCH_RESULT_PERSISTENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        query_id: str
        search_result_persistence_count: int
        def __init__(self, query_id: _Optional[str] = ..., search_result_persistence_count: _Optional[int] = ...) -> None: ...
    class PersonalizationSpec(_message.Message):
        __slots__ = ("mode",)
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[SearchRequest.PersonalizationSpec.Mode]
            AUTO: _ClassVar[SearchRequest.PersonalizationSpec.Mode]
            DISABLED: _ClassVar[SearchRequest.PersonalizationSpec.Mode]
        MODE_UNSPECIFIED: SearchRequest.PersonalizationSpec.Mode
        AUTO: SearchRequest.PersonalizationSpec.Mode
        DISABLED: SearchRequest.PersonalizationSpec.Mode
        MODE_FIELD_NUMBER: _ClassVar[int]
        mode: SearchRequest.PersonalizationSpec.Mode
        def __init__(self, mode: _Optional[_Union[SearchRequest.PersonalizationSpec.Mode, str]] = ...) -> None: ...
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ONE_BOX_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_SPECS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    FACET_SPECS_FIELD_NUMBER: _ClassVar[int]
    BOOST_SPEC_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_EXPANSION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SPELL_CORRECTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SEARCH_SPEC_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_SPEC_FIELD_NUMBER: _ClassVar[int]
    RANKING_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    SAFE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    NATURAL_LANGUAGE_QUERY_UNDERSTANDING_SPEC_FIELD_NUMBER: _ClassVar[int]
    SEARCH_AS_YOU_TYPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_SPEC_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    serving_config: str
    branch: str
    query: str
    image_query: SearchRequest.ImageQuery
    page_size: int
    page_token: str
    offset: int
    one_box_page_size: int
    data_store_specs: _containers.RepeatedCompositeFieldContainer[SearchRequest.DataStoreSpec]
    filter: str
    canonical_filter: str
    order_by: str
    user_info: _common_pb2.UserInfo
    language_code: str
    region_code: str
    facet_specs: _containers.RepeatedCompositeFieldContainer[SearchRequest.FacetSpec]
    boost_spec: SearchRequest.BoostSpec
    params: _containers.MessageMap[str, _struct_pb2.Value]
    query_expansion_spec: SearchRequest.QueryExpansionSpec
    spell_correction_spec: SearchRequest.SpellCorrectionSpec
    user_pseudo_id: str
    content_search_spec: SearchRequest.ContentSearchSpec
    embedding_spec: SearchRequest.EmbeddingSpec
    ranking_expression: str
    safe_search: bool
    user_labels: _containers.ScalarMap[str, str]
    natural_language_query_understanding_spec: SearchRequest.NaturalLanguageQueryUnderstandingSpec
    search_as_you_type_spec: SearchRequest.SearchAsYouTypeSpec
    session: str
    session_spec: SearchRequest.SessionSpec
    relevance_threshold: SearchRequest.RelevanceThreshold
    personalization_spec: SearchRequest.PersonalizationSpec
    def __init__(self, serving_config: _Optional[str] = ..., branch: _Optional[str] = ..., query: _Optional[str] = ..., image_query: _Optional[_Union[SearchRequest.ImageQuery, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., offset: _Optional[int] = ..., one_box_page_size: _Optional[int] = ..., data_store_specs: _Optional[_Iterable[_Union[SearchRequest.DataStoreSpec, _Mapping]]] = ..., filter: _Optional[str] = ..., canonical_filter: _Optional[str] = ..., order_by: _Optional[str] = ..., user_info: _Optional[_Union[_common_pb2.UserInfo, _Mapping]] = ..., language_code: _Optional[str] = ..., region_code: _Optional[str] = ..., facet_specs: _Optional[_Iterable[_Union[SearchRequest.FacetSpec, _Mapping]]] = ..., boost_spec: _Optional[_Union[SearchRequest.BoostSpec, _Mapping]] = ..., params: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., query_expansion_spec: _Optional[_Union[SearchRequest.QueryExpansionSpec, _Mapping]] = ..., spell_correction_spec: _Optional[_Union[SearchRequest.SpellCorrectionSpec, _Mapping]] = ..., user_pseudo_id: _Optional[str] = ..., content_search_spec: _Optional[_Union[SearchRequest.ContentSearchSpec, _Mapping]] = ..., embedding_spec: _Optional[_Union[SearchRequest.EmbeddingSpec, _Mapping]] = ..., ranking_expression: _Optional[str] = ..., safe_search: bool = ..., user_labels: _Optional[_Mapping[str, str]] = ..., natural_language_query_understanding_spec: _Optional[_Union[SearchRequest.NaturalLanguageQueryUnderstandingSpec, _Mapping]] = ..., search_as_you_type_spec: _Optional[_Union[SearchRequest.SearchAsYouTypeSpec, _Mapping]] = ..., session: _Optional[str] = ..., session_spec: _Optional[_Union[SearchRequest.SessionSpec, _Mapping]] = ..., relevance_threshold: _Optional[_Union[SearchRequest.RelevanceThreshold, str]] = ..., personalization_spec: _Optional[_Union[SearchRequest.PersonalizationSpec, _Mapping]] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("results", "facets", "guided_search_result", "total_size", "attribution_token", "redirect_uri", "next_page_token", "corrected_query", "summary", "applied_controls", "geo_search_debug_info", "query_expansion_info", "natural_language_query_understanding_info", "session_info", "one_box_results")
    class SearchResult(_message.Message):
        __slots__ = ("id", "document", "chunk", "model_scores")
        class ModelScoresEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _common_pb2.DoubleList
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.DoubleList, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        MODEL_SCORES_FIELD_NUMBER: _ClassVar[int]
        id: str
        document: _document_pb2.Document
        chunk: _chunk_pb2.Chunk
        model_scores: _containers.MessageMap[str, _common_pb2.DoubleList]
        def __init__(self, id: _Optional[str] = ..., document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., chunk: _Optional[_Union[_chunk_pb2.Chunk, _Mapping]] = ..., model_scores: _Optional[_Mapping[str, _common_pb2.DoubleList]] = ...) -> None: ...
    class Facet(_message.Message):
        __slots__ = ("key", "values", "dynamic_facet")
        class FacetValue(_message.Message):
            __slots__ = ("value", "interval", "count")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            INTERVAL_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            value: str
            interval: _common_pb2.Interval
            count: int
            def __init__(self, value: _Optional[str] = ..., interval: _Optional[_Union[_common_pb2.Interval, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_FACET_FIELD_NUMBER: _ClassVar[int]
        key: str
        values: _containers.RepeatedCompositeFieldContainer[SearchResponse.Facet.FacetValue]
        dynamic_facet: bool
        def __init__(self, key: _Optional[str] = ..., values: _Optional[_Iterable[_Union[SearchResponse.Facet.FacetValue, _Mapping]]] = ..., dynamic_facet: bool = ...) -> None: ...
    class GuidedSearchResult(_message.Message):
        __slots__ = ("refinement_attributes", "follow_up_questions")
        class RefinementAttribute(_message.Message):
            __slots__ = ("attribute_key", "attribute_value")
            ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
            ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
            attribute_key: str
            attribute_value: str
            def __init__(self, attribute_key: _Optional[str] = ..., attribute_value: _Optional[str] = ...) -> None: ...
        REFINEMENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        FOLLOW_UP_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
        refinement_attributes: _containers.RepeatedCompositeFieldContainer[SearchResponse.GuidedSearchResult.RefinementAttribute]
        follow_up_questions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, refinement_attributes: _Optional[_Iterable[_Union[SearchResponse.GuidedSearchResult.RefinementAttribute, _Mapping]]] = ..., follow_up_questions: _Optional[_Iterable[str]] = ...) -> None: ...
    class Summary(_message.Message):
        __slots__ = ("summary_text", "summary_skipped_reasons", "safety_attributes", "summary_with_metadata")
        class SummarySkippedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUMMARY_SKIPPED_REASON_UNSPECIFIED: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            ADVERSARIAL_QUERY_IGNORED: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            NON_SUMMARY_SEEKING_QUERY_IGNORED: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            OUT_OF_DOMAIN_QUERY_IGNORED: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            POTENTIAL_POLICY_VIOLATION: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            LLM_ADDON_NOT_ENABLED: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            NO_RELEVANT_CONTENT: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            JAIL_BREAKING_QUERY_IGNORED: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            CUSTOMER_POLICY_VIOLATION: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
            NON_SUMMARY_SEEKING_QUERY_IGNORED_V2: _ClassVar[SearchResponse.Summary.SummarySkippedReason]
        SUMMARY_SKIPPED_REASON_UNSPECIFIED: SearchResponse.Summary.SummarySkippedReason
        ADVERSARIAL_QUERY_IGNORED: SearchResponse.Summary.SummarySkippedReason
        NON_SUMMARY_SEEKING_QUERY_IGNORED: SearchResponse.Summary.SummarySkippedReason
        OUT_OF_DOMAIN_QUERY_IGNORED: SearchResponse.Summary.SummarySkippedReason
        POTENTIAL_POLICY_VIOLATION: SearchResponse.Summary.SummarySkippedReason
        LLM_ADDON_NOT_ENABLED: SearchResponse.Summary.SummarySkippedReason
        NO_RELEVANT_CONTENT: SearchResponse.Summary.SummarySkippedReason
        JAIL_BREAKING_QUERY_IGNORED: SearchResponse.Summary.SummarySkippedReason
        CUSTOMER_POLICY_VIOLATION: SearchResponse.Summary.SummarySkippedReason
        NON_SUMMARY_SEEKING_QUERY_IGNORED_V2: SearchResponse.Summary.SummarySkippedReason
        class SafetyAttributes(_message.Message):
            __slots__ = ("categories", "scores")
            CATEGORIES_FIELD_NUMBER: _ClassVar[int]
            SCORES_FIELD_NUMBER: _ClassVar[int]
            categories: _containers.RepeatedScalarFieldContainer[str]
            scores: _containers.RepeatedScalarFieldContainer[float]
            def __init__(self, categories: _Optional[_Iterable[str]] = ..., scores: _Optional[_Iterable[float]] = ...) -> None: ...
        class CitationMetadata(_message.Message):
            __slots__ = ("citations",)
            CITATIONS_FIELD_NUMBER: _ClassVar[int]
            citations: _containers.RepeatedCompositeFieldContainer[SearchResponse.Summary.Citation]
            def __init__(self, citations: _Optional[_Iterable[_Union[SearchResponse.Summary.Citation, _Mapping]]] = ...) -> None: ...
        class Citation(_message.Message):
            __slots__ = ("start_index", "end_index", "sources")
            START_INDEX_FIELD_NUMBER: _ClassVar[int]
            END_INDEX_FIELD_NUMBER: _ClassVar[int]
            SOURCES_FIELD_NUMBER: _ClassVar[int]
            start_index: int
            end_index: int
            sources: _containers.RepeatedCompositeFieldContainer[SearchResponse.Summary.CitationSource]
            def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ..., sources: _Optional[_Iterable[_Union[SearchResponse.Summary.CitationSource, _Mapping]]] = ...) -> None: ...
        class CitationSource(_message.Message):
            __slots__ = ("reference_index",)
            REFERENCE_INDEX_FIELD_NUMBER: _ClassVar[int]
            reference_index: int
            def __init__(self, reference_index: _Optional[int] = ...) -> None: ...
        class Reference(_message.Message):
            __slots__ = ("title", "document", "uri", "chunk_contents")
            class ChunkContent(_message.Message):
                __slots__ = ("content", "page_identifier")
                CONTENT_FIELD_NUMBER: _ClassVar[int]
                PAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                content: str
                page_identifier: str
                def __init__(self, content: _Optional[str] = ..., page_identifier: _Optional[str] = ...) -> None: ...
            TITLE_FIELD_NUMBER: _ClassVar[int]
            DOCUMENT_FIELD_NUMBER: _ClassVar[int]
            URI_FIELD_NUMBER: _ClassVar[int]
            CHUNK_CONTENTS_FIELD_NUMBER: _ClassVar[int]
            title: str
            document: str
            uri: str
            chunk_contents: _containers.RepeatedCompositeFieldContainer[SearchResponse.Summary.Reference.ChunkContent]
            def __init__(self, title: _Optional[str] = ..., document: _Optional[str] = ..., uri: _Optional[str] = ..., chunk_contents: _Optional[_Iterable[_Union[SearchResponse.Summary.Reference.ChunkContent, _Mapping]]] = ...) -> None: ...
        class SummaryWithMetadata(_message.Message):
            __slots__ = ("summary", "citation_metadata", "references")
            SUMMARY_FIELD_NUMBER: _ClassVar[int]
            CITATION_METADATA_FIELD_NUMBER: _ClassVar[int]
            REFERENCES_FIELD_NUMBER: _ClassVar[int]
            summary: str
            citation_metadata: SearchResponse.Summary.CitationMetadata
            references: _containers.RepeatedCompositeFieldContainer[SearchResponse.Summary.Reference]
            def __init__(self, summary: _Optional[str] = ..., citation_metadata: _Optional[_Union[SearchResponse.Summary.CitationMetadata, _Mapping]] = ..., references: _Optional[_Iterable[_Union[SearchResponse.Summary.Reference, _Mapping]]] = ...) -> None: ...
        SUMMARY_TEXT_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_SKIPPED_REASONS_FIELD_NUMBER: _ClassVar[int]
        SAFETY_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_WITH_METADATA_FIELD_NUMBER: _ClassVar[int]
        summary_text: str
        summary_skipped_reasons: _containers.RepeatedScalarFieldContainer[SearchResponse.Summary.SummarySkippedReason]
        safety_attributes: SearchResponse.Summary.SafetyAttributes
        summary_with_metadata: SearchResponse.Summary.SummaryWithMetadata
        def __init__(self, summary_text: _Optional[str] = ..., summary_skipped_reasons: _Optional[_Iterable[_Union[SearchResponse.Summary.SummarySkippedReason, str]]] = ..., safety_attributes: _Optional[_Union[SearchResponse.Summary.SafetyAttributes, _Mapping]] = ..., summary_with_metadata: _Optional[_Union[SearchResponse.Summary.SummaryWithMetadata, _Mapping]] = ...) -> None: ...
    class GeoSearchDebugInfo(_message.Message):
        __slots__ = ("original_address_query", "error_message")
        ORIGINAL_ADDRESS_QUERY_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        original_address_query: str
        error_message: str
        def __init__(self, original_address_query: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...
    class QueryExpansionInfo(_message.Message):
        __slots__ = ("expanded_query", "pinned_result_count")
        EXPANDED_QUERY_FIELD_NUMBER: _ClassVar[int]
        PINNED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
        expanded_query: bool
        pinned_result_count: int
        def __init__(self, expanded_query: bool = ..., pinned_result_count: _Optional[int] = ...) -> None: ...
    class NaturalLanguageQueryUnderstandingInfo(_message.Message):
        __slots__ = ("extracted_filters", "rewritten_query", "structured_extracted_filter")
        class StructuredExtractedFilter(_message.Message):
            __slots__ = ("expression",)
            class StringConstraint(_message.Message):
                __slots__ = ("field_name", "values", "query_segment")
                FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
                VALUES_FIELD_NUMBER: _ClassVar[int]
                QUERY_SEGMENT_FIELD_NUMBER: _ClassVar[int]
                field_name: str
                values: _containers.RepeatedScalarFieldContainer[str]
                query_segment: str
                def __init__(self, field_name: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ..., query_segment: _Optional[str] = ...) -> None: ...
            class NumberConstraint(_message.Message):
                __slots__ = ("field_name", "comparison", "value", "query_segment")
                class Comparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    COMPARISON_UNSPECIFIED: _ClassVar[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison]
                    EQUALS: _ClassVar[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison]
                    LESS_THAN_EQUALS: _ClassVar[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison]
                    LESS_THAN: _ClassVar[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison]
                    GREATER_THAN_EQUALS: _ClassVar[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison]
                    GREATER_THAN: _ClassVar[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison]
                COMPARISON_UNSPECIFIED: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison
                EQUALS: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison
                LESS_THAN_EQUALS: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison
                LESS_THAN: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison
                GREATER_THAN_EQUALS: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison
                GREATER_THAN: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison
                FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
                COMPARISON_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                QUERY_SEGMENT_FIELD_NUMBER: _ClassVar[int]
                field_name: str
                comparison: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison
                value: float
                query_segment: str
                def __init__(self, field_name: _Optional[str] = ..., comparison: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison, str]] = ..., value: _Optional[float] = ..., query_segment: _Optional[str] = ...) -> None: ...
            class GeolocationConstraint(_message.Message):
                __slots__ = ("field_name", "address", "latitude", "longitude", "radius_in_meters")
                FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
                ADDRESS_FIELD_NUMBER: _ClassVar[int]
                LATITUDE_FIELD_NUMBER: _ClassVar[int]
                LONGITUDE_FIELD_NUMBER: _ClassVar[int]
                RADIUS_IN_METERS_FIELD_NUMBER: _ClassVar[int]
                field_name: str
                address: str
                latitude: float
                longitude: float
                radius_in_meters: float
                def __init__(self, field_name: _Optional[str] = ..., address: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., radius_in_meters: _Optional[float] = ...) -> None: ...
            class AndExpression(_message.Message):
                __slots__ = ("expressions",)
                EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
                expressions: _containers.RepeatedCompositeFieldContainer[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression]
                def __init__(self, expressions: _Optional[_Iterable[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression, _Mapping]]] = ...) -> None: ...
            class OrExpression(_message.Message):
                __slots__ = ("expressions",)
                EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
                expressions: _containers.RepeatedCompositeFieldContainer[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression]
                def __init__(self, expressions: _Optional[_Iterable[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression, _Mapping]]] = ...) -> None: ...
            class Expression(_message.Message):
                __slots__ = ("string_constraint", "number_constraint", "geolocation_constraint", "and_expr", "or_expr")
                STRING_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
                NUMBER_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
                GEOLOCATION_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
                AND_EXPR_FIELD_NUMBER: _ClassVar[int]
                OR_EXPR_FIELD_NUMBER: _ClassVar[int]
                string_constraint: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.StringConstraint
                number_constraint: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint
                geolocation_constraint: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.GeolocationConstraint
                and_expr: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.AndExpression
                or_expr: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.OrExpression
                def __init__(self, string_constraint: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.StringConstraint, _Mapping]] = ..., number_constraint: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint, _Mapping]] = ..., geolocation_constraint: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.GeolocationConstraint, _Mapping]] = ..., and_expr: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.AndExpression, _Mapping]] = ..., or_expr: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.OrExpression, _Mapping]] = ...) -> None: ...
            EXPRESSION_FIELD_NUMBER: _ClassVar[int]
            expression: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression
            def __init__(self, expression: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression, _Mapping]] = ...) -> None: ...
        EXTRACTED_FILTERS_FIELD_NUMBER: _ClassVar[int]
        REWRITTEN_QUERY_FIELD_NUMBER: _ClassVar[int]
        STRUCTURED_EXTRACTED_FILTER_FIELD_NUMBER: _ClassVar[int]
        extracted_filters: str
        rewritten_query: str
        structured_extracted_filter: SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter
        def __init__(self, extracted_filters: _Optional[str] = ..., rewritten_query: _Optional[str] = ..., structured_extracted_filter: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter, _Mapping]] = ...) -> None: ...
    class SessionInfo(_message.Message):
        __slots__ = ("name", "query_id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        query_id: str
        def __init__(self, name: _Optional[str] = ..., query_id: _Optional[str] = ...) -> None: ...
    class OneBoxResult(_message.Message):
        __slots__ = ("one_box_type", "search_results")
        class OneBoxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ONE_BOX_TYPE_UNSPECIFIED: _ClassVar[SearchResponse.OneBoxResult.OneBoxType]
            PEOPLE: _ClassVar[SearchResponse.OneBoxResult.OneBoxType]
            ORGANIZATION: _ClassVar[SearchResponse.OneBoxResult.OneBoxType]
            SLACK: _ClassVar[SearchResponse.OneBoxResult.OneBoxType]
            KNOWLEDGE_GRAPH: _ClassVar[SearchResponse.OneBoxResult.OneBoxType]
        ONE_BOX_TYPE_UNSPECIFIED: SearchResponse.OneBoxResult.OneBoxType
        PEOPLE: SearchResponse.OneBoxResult.OneBoxType
        ORGANIZATION: SearchResponse.OneBoxResult.OneBoxType
        SLACK: SearchResponse.OneBoxResult.OneBoxType
        KNOWLEDGE_GRAPH: SearchResponse.OneBoxResult.OneBoxType
        ONE_BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
        SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
        one_box_type: SearchResponse.OneBoxResult.OneBoxType
        search_results: _containers.RepeatedCompositeFieldContainer[SearchResponse.SearchResult]
        def __init__(self, one_box_type: _Optional[_Union[SearchResponse.OneBoxResult.OneBoxType, str]] = ..., search_results: _Optional[_Iterable[_Union[SearchResponse.SearchResult, _Mapping]]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    GUIDED_SEARCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_QUERY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    GEO_SEARCH_DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    QUERY_EXPANSION_INFO_FIELD_NUMBER: _ClassVar[int]
    NATURAL_LANGUAGE_QUERY_UNDERSTANDING_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ONE_BOX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchResponse.SearchResult]
    facets: _containers.RepeatedCompositeFieldContainer[SearchResponse.Facet]
    guided_search_result: SearchResponse.GuidedSearchResult
    total_size: int
    attribution_token: str
    redirect_uri: str
    next_page_token: str
    corrected_query: str
    summary: SearchResponse.Summary
    applied_controls: _containers.RepeatedScalarFieldContainer[str]
    geo_search_debug_info: _containers.RepeatedCompositeFieldContainer[SearchResponse.GeoSearchDebugInfo]
    query_expansion_info: SearchResponse.QueryExpansionInfo
    natural_language_query_understanding_info: SearchResponse.NaturalLanguageQueryUnderstandingInfo
    session_info: SearchResponse.SessionInfo
    one_box_results: _containers.RepeatedCompositeFieldContainer[SearchResponse.OneBoxResult]
    def __init__(self, results: _Optional[_Iterable[_Union[SearchResponse.SearchResult, _Mapping]]] = ..., facets: _Optional[_Iterable[_Union[SearchResponse.Facet, _Mapping]]] = ..., guided_search_result: _Optional[_Union[SearchResponse.GuidedSearchResult, _Mapping]] = ..., total_size: _Optional[int] = ..., attribution_token: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., next_page_token: _Optional[str] = ..., corrected_query: _Optional[str] = ..., summary: _Optional[_Union[SearchResponse.Summary, _Mapping]] = ..., applied_controls: _Optional[_Iterable[str]] = ..., geo_search_debug_info: _Optional[_Iterable[_Union[SearchResponse.GeoSearchDebugInfo, _Mapping]]] = ..., query_expansion_info: _Optional[_Union[SearchResponse.QueryExpansionInfo, _Mapping]] = ..., natural_language_query_understanding_info: _Optional[_Union[SearchResponse.NaturalLanguageQueryUnderstandingInfo, _Mapping]] = ..., session_info: _Optional[_Union[SearchResponse.SessionInfo, _Mapping]] = ..., one_box_results: _Optional[_Iterable[_Union[SearchResponse.OneBoxResult, _Mapping]]] = ...) -> None: ...
