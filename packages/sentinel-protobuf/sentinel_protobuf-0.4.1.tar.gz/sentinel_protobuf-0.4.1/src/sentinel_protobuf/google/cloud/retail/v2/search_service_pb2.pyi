from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import common_pb2 as _common_pb2
from google.cloud.retail.v2 import product_pb2 as _product_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductAttributeValue(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ProductAttributeInterval(_message.Message):
    __slots__ = ("name", "interval")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    interval: _common_pb2.Interval
    def __init__(self, name: _Optional[str] = ..., interval: _Optional[_Union[_common_pb2.Interval, _Mapping]] = ...) -> None: ...

class Tile(_message.Message):
    __slots__ = ("product_attribute_value", "product_attribute_interval", "representative_product_id")
    PRODUCT_ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ATTRIBUTE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIVE_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_attribute_value: ProductAttributeValue
    product_attribute_interval: ProductAttributeInterval
    representative_product_id: str
    def __init__(self, product_attribute_value: _Optional[_Union[ProductAttributeValue, _Mapping]] = ..., product_attribute_interval: _Optional[_Union[ProductAttributeInterval, _Mapping]] = ..., representative_product_id: _Optional[str] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("placement", "branch", "query", "visitor_id", "user_info", "page_size", "page_token", "offset", "filter", "canonical_filter", "order_by", "facet_specs", "dynamic_facet_spec", "boost_spec", "query_expansion_spec", "variant_rollup_keys", "page_categories", "search_mode", "personalization_spec", "labels", "spell_correction_spec", "entity", "conversational_search_spec", "tile_navigation_spec")
    class SearchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEARCH_MODE_UNSPECIFIED: _ClassVar[SearchRequest.SearchMode]
        PRODUCT_SEARCH_ONLY: _ClassVar[SearchRequest.SearchMode]
        FACETED_SEARCH_ONLY: _ClassVar[SearchRequest.SearchMode]
    SEARCH_MODE_UNSPECIFIED: SearchRequest.SearchMode
    PRODUCT_SEARCH_ONLY: SearchRequest.SearchMode
    FACETED_SEARCH_ONLY: SearchRequest.SearchMode
    class FacetSpec(_message.Message):
        __slots__ = ("facet_key", "limit", "excluded_filter_keys", "enable_dynamic_position")
        class FacetKey(_message.Message):
            __slots__ = ("key", "intervals", "restricted_values", "prefixes", "contains", "case_insensitive", "order_by", "query", "return_min_max")
            KEY_FIELD_NUMBER: _ClassVar[int]
            INTERVALS_FIELD_NUMBER: _ClassVar[int]
            RESTRICTED_VALUES_FIELD_NUMBER: _ClassVar[int]
            PREFIXES_FIELD_NUMBER: _ClassVar[int]
            CONTAINS_FIELD_NUMBER: _ClassVar[int]
            CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
            ORDER_BY_FIELD_NUMBER: _ClassVar[int]
            QUERY_FIELD_NUMBER: _ClassVar[int]
            RETURN_MIN_MAX_FIELD_NUMBER: _ClassVar[int]
            key: str
            intervals: _containers.RepeatedCompositeFieldContainer[_common_pb2.Interval]
            restricted_values: _containers.RepeatedScalarFieldContainer[str]
            prefixes: _containers.RepeatedScalarFieldContainer[str]
            contains: _containers.RepeatedScalarFieldContainer[str]
            case_insensitive: bool
            order_by: str
            query: str
            return_min_max: bool
            def __init__(self, key: _Optional[str] = ..., intervals: _Optional[_Iterable[_Union[_common_pb2.Interval, _Mapping]]] = ..., restricted_values: _Optional[_Iterable[str]] = ..., prefixes: _Optional[_Iterable[str]] = ..., contains: _Optional[_Iterable[str]] = ..., case_insensitive: bool = ..., order_by: _Optional[str] = ..., query: _Optional[str] = ..., return_min_max: bool = ...) -> None: ...
        FACET_KEY_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_FILTER_KEYS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_DYNAMIC_POSITION_FIELD_NUMBER: _ClassVar[int]
        facet_key: SearchRequest.FacetSpec.FacetKey
        limit: int
        excluded_filter_keys: _containers.RepeatedScalarFieldContainer[str]
        enable_dynamic_position: bool
        def __init__(self, facet_key: _Optional[_Union[SearchRequest.FacetSpec.FacetKey, _Mapping]] = ..., limit: _Optional[int] = ..., excluded_filter_keys: _Optional[_Iterable[str]] = ..., enable_dynamic_position: bool = ...) -> None: ...
    class DynamicFacetSpec(_message.Message):
        __slots__ = ("mode",)
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[SearchRequest.DynamicFacetSpec.Mode]
            DISABLED: _ClassVar[SearchRequest.DynamicFacetSpec.Mode]
            ENABLED: _ClassVar[SearchRequest.DynamicFacetSpec.Mode]
        MODE_UNSPECIFIED: SearchRequest.DynamicFacetSpec.Mode
        DISABLED: SearchRequest.DynamicFacetSpec.Mode
        ENABLED: SearchRequest.DynamicFacetSpec.Mode
        MODE_FIELD_NUMBER: _ClassVar[int]
        mode: SearchRequest.DynamicFacetSpec.Mode
        def __init__(self, mode: _Optional[_Union[SearchRequest.DynamicFacetSpec.Mode, str]] = ...) -> None: ...
    class BoostSpec(_message.Message):
        __slots__ = ("condition_boost_specs", "skip_boost_spec_validation")
        class ConditionBoostSpec(_message.Message):
            __slots__ = ("condition", "boost")
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            BOOST_FIELD_NUMBER: _ClassVar[int]
            condition: str
            boost: float
            def __init__(self, condition: _Optional[str] = ..., boost: _Optional[float] = ...) -> None: ...
        CONDITION_BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
        SKIP_BOOST_SPEC_VALIDATION_FIELD_NUMBER: _ClassVar[int]
        condition_boost_specs: _containers.RepeatedCompositeFieldContainer[SearchRequest.BoostSpec.ConditionBoostSpec]
        skip_boost_spec_validation: bool
        def __init__(self, condition_boost_specs: _Optional[_Iterable[_Union[SearchRequest.BoostSpec.ConditionBoostSpec, _Mapping]]] = ..., skip_boost_spec_validation: bool = ...) -> None: ...
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
    class ConversationalSearchSpec(_message.Message):
        __slots__ = ("followup_conversation_requested", "conversation_id", "user_answer")
        class UserAnswer(_message.Message):
            __slots__ = ("text_answer", "selected_answer")
            class SelectedAnswer(_message.Message):
                __slots__ = ("product_attribute_values", "product_attribute_value")
                PRODUCT_ATTRIBUTE_VALUES_FIELD_NUMBER: _ClassVar[int]
                PRODUCT_ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
                product_attribute_values: _containers.RepeatedCompositeFieldContainer[ProductAttributeValue]
                product_attribute_value: ProductAttributeValue
                def __init__(self, product_attribute_values: _Optional[_Iterable[_Union[ProductAttributeValue, _Mapping]]] = ..., product_attribute_value: _Optional[_Union[ProductAttributeValue, _Mapping]] = ...) -> None: ...
            TEXT_ANSWER_FIELD_NUMBER: _ClassVar[int]
            SELECTED_ANSWER_FIELD_NUMBER: _ClassVar[int]
            text_answer: str
            selected_answer: SearchRequest.ConversationalSearchSpec.UserAnswer.SelectedAnswer
            def __init__(self, text_answer: _Optional[str] = ..., selected_answer: _Optional[_Union[SearchRequest.ConversationalSearchSpec.UserAnswer.SelectedAnswer, _Mapping]] = ...) -> None: ...
        FOLLOWUP_CONVERSATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
        USER_ANSWER_FIELD_NUMBER: _ClassVar[int]
        followup_conversation_requested: bool
        conversation_id: str
        user_answer: SearchRequest.ConversationalSearchSpec.UserAnswer
        def __init__(self, followup_conversation_requested: bool = ..., conversation_id: _Optional[str] = ..., user_answer: _Optional[_Union[SearchRequest.ConversationalSearchSpec.UserAnswer, _Mapping]] = ...) -> None: ...
    class TileNavigationSpec(_message.Message):
        __slots__ = ("tile_navigation_requested", "applied_tiles")
        TILE_NAVIGATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        APPLIED_TILES_FIELD_NUMBER: _ClassVar[int]
        tile_navigation_requested: bool
        applied_tiles: _containers.RepeatedCompositeFieldContainer[Tile]
        def __init__(self, tile_navigation_requested: bool = ..., applied_tiles: _Optional[_Iterable[_Union[Tile, _Mapping]]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    VISITOR_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FACET_SPECS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FACET_SPEC_FIELD_NUMBER: _ClassVar[int]
    BOOST_SPEC_FIELD_NUMBER: _ClassVar[int]
    QUERY_EXPANSION_SPEC_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ROLLUP_KEYS_FIELD_NUMBER: _ClassVar[int]
    PAGE_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_MODE_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SPELL_CORRECTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONAL_SEARCH_SPEC_FIELD_NUMBER: _ClassVar[int]
    TILE_NAVIGATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    placement: str
    branch: str
    query: str
    visitor_id: str
    user_info: _common_pb2.UserInfo
    page_size: int
    page_token: str
    offset: int
    filter: str
    canonical_filter: str
    order_by: str
    facet_specs: _containers.RepeatedCompositeFieldContainer[SearchRequest.FacetSpec]
    dynamic_facet_spec: SearchRequest.DynamicFacetSpec
    boost_spec: SearchRequest.BoostSpec
    query_expansion_spec: SearchRequest.QueryExpansionSpec
    variant_rollup_keys: _containers.RepeatedScalarFieldContainer[str]
    page_categories: _containers.RepeatedScalarFieldContainer[str]
    search_mode: SearchRequest.SearchMode
    personalization_spec: SearchRequest.PersonalizationSpec
    labels: _containers.ScalarMap[str, str]
    spell_correction_spec: SearchRequest.SpellCorrectionSpec
    entity: str
    conversational_search_spec: SearchRequest.ConversationalSearchSpec
    tile_navigation_spec: SearchRequest.TileNavigationSpec
    def __init__(self, placement: _Optional[str] = ..., branch: _Optional[str] = ..., query: _Optional[str] = ..., visitor_id: _Optional[str] = ..., user_info: _Optional[_Union[_common_pb2.UserInfo, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., offset: _Optional[int] = ..., filter: _Optional[str] = ..., canonical_filter: _Optional[str] = ..., order_by: _Optional[str] = ..., facet_specs: _Optional[_Iterable[_Union[SearchRequest.FacetSpec, _Mapping]]] = ..., dynamic_facet_spec: _Optional[_Union[SearchRequest.DynamicFacetSpec, _Mapping]] = ..., boost_spec: _Optional[_Union[SearchRequest.BoostSpec, _Mapping]] = ..., query_expansion_spec: _Optional[_Union[SearchRequest.QueryExpansionSpec, _Mapping]] = ..., variant_rollup_keys: _Optional[_Iterable[str]] = ..., page_categories: _Optional[_Iterable[str]] = ..., search_mode: _Optional[_Union[SearchRequest.SearchMode, str]] = ..., personalization_spec: _Optional[_Union[SearchRequest.PersonalizationSpec, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., spell_correction_spec: _Optional[_Union[SearchRequest.SpellCorrectionSpec, _Mapping]] = ..., entity: _Optional[str] = ..., conversational_search_spec: _Optional[_Union[SearchRequest.ConversationalSearchSpec, _Mapping]] = ..., tile_navigation_spec: _Optional[_Union[SearchRequest.TileNavigationSpec, _Mapping]] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("results", "facets", "total_size", "corrected_query", "attribution_token", "next_page_token", "query_expansion_info", "redirect_uri", "applied_controls", "invalid_condition_boost_specs", "experiment_info", "conversational_search_result", "tile_navigation_result")
    class SearchResult(_message.Message):
        __slots__ = ("id", "product", "matching_variant_count", "matching_variant_fields", "variant_rollup_values", "personal_labels")
        class MatchingVariantFieldsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _field_mask_pb2.FieldMask
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
        class VariantRollupValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_FIELD_NUMBER: _ClassVar[int]
        MATCHING_VARIANT_COUNT_FIELD_NUMBER: _ClassVar[int]
        MATCHING_VARIANT_FIELDS_FIELD_NUMBER: _ClassVar[int]
        VARIANT_ROLLUP_VALUES_FIELD_NUMBER: _ClassVar[int]
        PERSONAL_LABELS_FIELD_NUMBER: _ClassVar[int]
        id: str
        product: _product_pb2.Product
        matching_variant_count: int
        matching_variant_fields: _containers.MessageMap[str, _field_mask_pb2.FieldMask]
        variant_rollup_values: _containers.MessageMap[str, _struct_pb2.Value]
        personal_labels: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ..., matching_variant_count: _Optional[int] = ..., matching_variant_fields: _Optional[_Mapping[str, _field_mask_pb2.FieldMask]] = ..., variant_rollup_values: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., personal_labels: _Optional[_Iterable[str]] = ...) -> None: ...
    class Facet(_message.Message):
        __slots__ = ("key", "values", "dynamic_facet")
        class FacetValue(_message.Message):
            __slots__ = ("value", "interval", "count", "min_value", "max_value")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            INTERVAL_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
            MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            interval: _common_pb2.Interval
            count: int
            min_value: float
            max_value: float
            def __init__(self, value: _Optional[str] = ..., interval: _Optional[_Union[_common_pb2.Interval, _Mapping]] = ..., count: _Optional[int] = ..., min_value: _Optional[float] = ..., max_value: _Optional[float] = ...) -> None: ...
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_FACET_FIELD_NUMBER: _ClassVar[int]
        key: str
        values: _containers.RepeatedCompositeFieldContainer[SearchResponse.Facet.FacetValue]
        dynamic_facet: bool
        def __init__(self, key: _Optional[str] = ..., values: _Optional[_Iterable[_Union[SearchResponse.Facet.FacetValue, _Mapping]]] = ..., dynamic_facet: bool = ...) -> None: ...
    class QueryExpansionInfo(_message.Message):
        __slots__ = ("expanded_query", "pinned_result_count")
        EXPANDED_QUERY_FIELD_NUMBER: _ClassVar[int]
        PINNED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
        expanded_query: bool
        pinned_result_count: int
        def __init__(self, expanded_query: bool = ..., pinned_result_count: _Optional[int] = ...) -> None: ...
    class ConversationalSearchResult(_message.Message):
        __slots__ = ("conversation_id", "refined_query", "additional_filters", "followup_question", "suggested_answers", "additional_filter")
        class SuggestedAnswer(_message.Message):
            __slots__ = ("product_attribute_value",)
            PRODUCT_ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
            product_attribute_value: ProductAttributeValue
            def __init__(self, product_attribute_value: _Optional[_Union[ProductAttributeValue, _Mapping]] = ...) -> None: ...
        class AdditionalFilter(_message.Message):
            __slots__ = ("product_attribute_value",)
            PRODUCT_ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
            product_attribute_value: ProductAttributeValue
            def __init__(self, product_attribute_value: _Optional[_Union[ProductAttributeValue, _Mapping]] = ...) -> None: ...
        CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
        REFINED_QUERY_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_FILTERS_FIELD_NUMBER: _ClassVar[int]
        FOLLOWUP_QUESTION_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_ANSWERS_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_FILTER_FIELD_NUMBER: _ClassVar[int]
        conversation_id: str
        refined_query: str
        additional_filters: _containers.RepeatedCompositeFieldContainer[SearchResponse.ConversationalSearchResult.AdditionalFilter]
        followup_question: str
        suggested_answers: _containers.RepeatedCompositeFieldContainer[SearchResponse.ConversationalSearchResult.SuggestedAnswer]
        additional_filter: SearchResponse.ConversationalSearchResult.AdditionalFilter
        def __init__(self, conversation_id: _Optional[str] = ..., refined_query: _Optional[str] = ..., additional_filters: _Optional[_Iterable[_Union[SearchResponse.ConversationalSearchResult.AdditionalFilter, _Mapping]]] = ..., followup_question: _Optional[str] = ..., suggested_answers: _Optional[_Iterable[_Union[SearchResponse.ConversationalSearchResult.SuggestedAnswer, _Mapping]]] = ..., additional_filter: _Optional[_Union[SearchResponse.ConversationalSearchResult.AdditionalFilter, _Mapping]] = ...) -> None: ...
    class TileNavigationResult(_message.Message):
        __slots__ = ("tiles",)
        TILES_FIELD_NUMBER: _ClassVar[int]
        tiles: _containers.RepeatedCompositeFieldContainer[Tile]
        def __init__(self, tiles: _Optional[_Iterable[_Union[Tile, _Mapping]]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_QUERY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_EXPANSION_INFO_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    INVALID_CONDITION_BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONAL_SEARCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    TILE_NAVIGATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchResponse.SearchResult]
    facets: _containers.RepeatedCompositeFieldContainer[SearchResponse.Facet]
    total_size: int
    corrected_query: str
    attribution_token: str
    next_page_token: str
    query_expansion_info: SearchResponse.QueryExpansionInfo
    redirect_uri: str
    applied_controls: _containers.RepeatedScalarFieldContainer[str]
    invalid_condition_boost_specs: _containers.RepeatedCompositeFieldContainer[SearchRequest.BoostSpec.ConditionBoostSpec]
    experiment_info: _containers.RepeatedCompositeFieldContainer[ExperimentInfo]
    conversational_search_result: SearchResponse.ConversationalSearchResult
    tile_navigation_result: SearchResponse.TileNavigationResult
    def __init__(self, results: _Optional[_Iterable[_Union[SearchResponse.SearchResult, _Mapping]]] = ..., facets: _Optional[_Iterable[_Union[SearchResponse.Facet, _Mapping]]] = ..., total_size: _Optional[int] = ..., corrected_query: _Optional[str] = ..., attribution_token: _Optional[str] = ..., next_page_token: _Optional[str] = ..., query_expansion_info: _Optional[_Union[SearchResponse.QueryExpansionInfo, _Mapping]] = ..., redirect_uri: _Optional[str] = ..., applied_controls: _Optional[_Iterable[str]] = ..., invalid_condition_boost_specs: _Optional[_Iterable[_Union[SearchRequest.BoostSpec.ConditionBoostSpec, _Mapping]]] = ..., experiment_info: _Optional[_Iterable[_Union[ExperimentInfo, _Mapping]]] = ..., conversational_search_result: _Optional[_Union[SearchResponse.ConversationalSearchResult, _Mapping]] = ..., tile_navigation_result: _Optional[_Union[SearchResponse.TileNavigationResult, _Mapping]] = ...) -> None: ...

class ExperimentInfo(_message.Message):
    __slots__ = ("serving_config_experiment", "experiment")
    class ServingConfigExperiment(_message.Message):
        __slots__ = ("original_serving_config", "experiment_serving_config")
        ORIGINAL_SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        EXPERIMENT_SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        original_serving_config: str
        experiment_serving_config: str
        def __init__(self, original_serving_config: _Optional[str] = ..., experiment_serving_config: _Optional[str] = ...) -> None: ...
    SERVING_CONFIG_EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    serving_config_experiment: ExperimentInfo.ServingConfigExperiment
    experiment: str
    def __init__(self, serving_config_experiment: _Optional[_Union[ExperimentInfo.ServingConfigExperiment, _Mapping]] = ..., experiment: _Optional[str] = ...) -> None: ...
