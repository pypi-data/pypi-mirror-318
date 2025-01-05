from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttributeConfigLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED: _ClassVar[AttributeConfigLevel]
    PRODUCT_LEVEL_ATTRIBUTE_CONFIG: _ClassVar[AttributeConfigLevel]
    CATALOG_LEVEL_ATTRIBUTE_CONFIG: _ClassVar[AttributeConfigLevel]

class SolutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOLUTION_TYPE_UNSPECIFIED: _ClassVar[SolutionType]
    SOLUTION_TYPE_RECOMMENDATION: _ClassVar[SolutionType]
    SOLUTION_TYPE_SEARCH: _ClassVar[SolutionType]

class RecommendationsFilteringOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED: _ClassVar[RecommendationsFilteringOption]
    RECOMMENDATIONS_FILTERING_DISABLED: _ClassVar[RecommendationsFilteringOption]
    RECOMMENDATIONS_FILTERING_ENABLED: _ClassVar[RecommendationsFilteringOption]

class SearchSolutionUseCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_SOLUTION_USE_CASE_UNSPECIFIED: _ClassVar[SearchSolutionUseCase]
    SEARCH_SOLUTION_USE_CASE_SEARCH: _ClassVar[SearchSolutionUseCase]
    SEARCH_SOLUTION_USE_CASE_BROWSE: _ClassVar[SearchSolutionUseCase]
ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED: AttributeConfigLevel
PRODUCT_LEVEL_ATTRIBUTE_CONFIG: AttributeConfigLevel
CATALOG_LEVEL_ATTRIBUTE_CONFIG: AttributeConfigLevel
SOLUTION_TYPE_UNSPECIFIED: SolutionType
SOLUTION_TYPE_RECOMMENDATION: SolutionType
SOLUTION_TYPE_SEARCH: SolutionType
RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED: RecommendationsFilteringOption
RECOMMENDATIONS_FILTERING_DISABLED: RecommendationsFilteringOption
RECOMMENDATIONS_FILTERING_ENABLED: RecommendationsFilteringOption
SEARCH_SOLUTION_USE_CASE_UNSPECIFIED: SearchSolutionUseCase
SEARCH_SOLUTION_USE_CASE_SEARCH: SearchSolutionUseCase
SEARCH_SOLUTION_USE_CASE_BROWSE: SearchSolutionUseCase

class Condition(_message.Message):
    __slots__ = ("query_terms", "active_time_range", "page_categories")
    class QueryTerm(_message.Message):
        __slots__ = ("value", "full_match")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        FULL_MATCH_FIELD_NUMBER: _ClassVar[int]
        value: str
        full_match: bool
        def __init__(self, value: _Optional[str] = ..., full_match: bool = ...) -> None: ...
    class TimeRange(_message.Message):
        __slots__ = ("start_time", "end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    QUERY_TERMS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    query_terms: _containers.RepeatedCompositeFieldContainer[Condition.QueryTerm]
    active_time_range: _containers.RepeatedCompositeFieldContainer[Condition.TimeRange]
    page_categories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, query_terms: _Optional[_Iterable[_Union[Condition.QueryTerm, _Mapping]]] = ..., active_time_range: _Optional[_Iterable[_Union[Condition.TimeRange, _Mapping]]] = ..., page_categories: _Optional[_Iterable[str]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ("boost_action", "redirect_action", "oneway_synonyms_action", "do_not_associate_action", "replacement_action", "ignore_action", "filter_action", "twoway_synonyms_action", "force_return_facet_action", "remove_facet_action", "condition")
    class BoostAction(_message.Message):
        __slots__ = ("boost", "products_filter")
        BOOST_FIELD_NUMBER: _ClassVar[int]
        PRODUCTS_FILTER_FIELD_NUMBER: _ClassVar[int]
        boost: float
        products_filter: str
        def __init__(self, boost: _Optional[float] = ..., products_filter: _Optional[str] = ...) -> None: ...
    class FilterAction(_message.Message):
        __slots__ = ("filter",)
        FILTER_FIELD_NUMBER: _ClassVar[int]
        filter: str
        def __init__(self, filter: _Optional[str] = ...) -> None: ...
    class RedirectAction(_message.Message):
        __slots__ = ("redirect_uri",)
        REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
        redirect_uri: str
        def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...
    class TwowaySynonymsAction(_message.Message):
        __slots__ = ("synonyms",)
        SYNONYMS_FIELD_NUMBER: _ClassVar[int]
        synonyms: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, synonyms: _Optional[_Iterable[str]] = ...) -> None: ...
    class OnewaySynonymsAction(_message.Message):
        __slots__ = ("query_terms", "synonyms", "oneway_terms")
        QUERY_TERMS_FIELD_NUMBER: _ClassVar[int]
        SYNONYMS_FIELD_NUMBER: _ClassVar[int]
        ONEWAY_TERMS_FIELD_NUMBER: _ClassVar[int]
        query_terms: _containers.RepeatedScalarFieldContainer[str]
        synonyms: _containers.RepeatedScalarFieldContainer[str]
        oneway_terms: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, query_terms: _Optional[_Iterable[str]] = ..., synonyms: _Optional[_Iterable[str]] = ..., oneway_terms: _Optional[_Iterable[str]] = ...) -> None: ...
    class DoNotAssociateAction(_message.Message):
        __slots__ = ("query_terms", "do_not_associate_terms", "terms")
        QUERY_TERMS_FIELD_NUMBER: _ClassVar[int]
        DO_NOT_ASSOCIATE_TERMS_FIELD_NUMBER: _ClassVar[int]
        TERMS_FIELD_NUMBER: _ClassVar[int]
        query_terms: _containers.RepeatedScalarFieldContainer[str]
        do_not_associate_terms: _containers.RepeatedScalarFieldContainer[str]
        terms: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, query_terms: _Optional[_Iterable[str]] = ..., do_not_associate_terms: _Optional[_Iterable[str]] = ..., terms: _Optional[_Iterable[str]] = ...) -> None: ...
    class ReplacementAction(_message.Message):
        __slots__ = ("query_terms", "replacement_term", "term")
        QUERY_TERMS_FIELD_NUMBER: _ClassVar[int]
        REPLACEMENT_TERM_FIELD_NUMBER: _ClassVar[int]
        TERM_FIELD_NUMBER: _ClassVar[int]
        query_terms: _containers.RepeatedScalarFieldContainer[str]
        replacement_term: str
        term: str
        def __init__(self, query_terms: _Optional[_Iterable[str]] = ..., replacement_term: _Optional[str] = ..., term: _Optional[str] = ...) -> None: ...
    class IgnoreAction(_message.Message):
        __slots__ = ("ignore_terms",)
        IGNORE_TERMS_FIELD_NUMBER: _ClassVar[int]
        ignore_terms: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, ignore_terms: _Optional[_Iterable[str]] = ...) -> None: ...
    class ForceReturnFacetAction(_message.Message):
        __slots__ = ("facet_position_adjustments",)
        class FacetPositionAdjustment(_message.Message):
            __slots__ = ("attribute_name", "position")
            ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
            POSITION_FIELD_NUMBER: _ClassVar[int]
            attribute_name: str
            position: int
            def __init__(self, attribute_name: _Optional[str] = ..., position: _Optional[int] = ...) -> None: ...
        FACET_POSITION_ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
        facet_position_adjustments: _containers.RepeatedCompositeFieldContainer[Rule.ForceReturnFacetAction.FacetPositionAdjustment]
        def __init__(self, facet_position_adjustments: _Optional[_Iterable[_Union[Rule.ForceReturnFacetAction.FacetPositionAdjustment, _Mapping]]] = ...) -> None: ...
    class RemoveFacetAction(_message.Message):
        __slots__ = ("attribute_names",)
        ATTRIBUTE_NAMES_FIELD_NUMBER: _ClassVar[int]
        attribute_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, attribute_names: _Optional[_Iterable[str]] = ...) -> None: ...
    BOOST_ACTION_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_ACTION_FIELD_NUMBER: _ClassVar[int]
    ONEWAY_SYNONYMS_ACTION_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_ASSOCIATE_ACTION_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ACTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_ACTION_FIELD_NUMBER: _ClassVar[int]
    TWOWAY_SYNONYMS_ACTION_FIELD_NUMBER: _ClassVar[int]
    FORCE_RETURN_FACET_ACTION_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FACET_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    boost_action: Rule.BoostAction
    redirect_action: Rule.RedirectAction
    oneway_synonyms_action: Rule.OnewaySynonymsAction
    do_not_associate_action: Rule.DoNotAssociateAction
    replacement_action: Rule.ReplacementAction
    ignore_action: Rule.IgnoreAction
    filter_action: Rule.FilterAction
    twoway_synonyms_action: Rule.TwowaySynonymsAction
    force_return_facet_action: Rule.ForceReturnFacetAction
    remove_facet_action: Rule.RemoveFacetAction
    condition: Condition
    def __init__(self, boost_action: _Optional[_Union[Rule.BoostAction, _Mapping]] = ..., redirect_action: _Optional[_Union[Rule.RedirectAction, _Mapping]] = ..., oneway_synonyms_action: _Optional[_Union[Rule.OnewaySynonymsAction, _Mapping]] = ..., do_not_associate_action: _Optional[_Union[Rule.DoNotAssociateAction, _Mapping]] = ..., replacement_action: _Optional[_Union[Rule.ReplacementAction, _Mapping]] = ..., ignore_action: _Optional[_Union[Rule.IgnoreAction, _Mapping]] = ..., filter_action: _Optional[_Union[Rule.FilterAction, _Mapping]] = ..., twoway_synonyms_action: _Optional[_Union[Rule.TwowaySynonymsAction, _Mapping]] = ..., force_return_facet_action: _Optional[_Union[Rule.ForceReturnFacetAction, _Mapping]] = ..., remove_facet_action: _Optional[_Union[Rule.RemoveFacetAction, _Mapping]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ...) -> None: ...

class Audience(_message.Message):
    __slots__ = ("genders", "age_groups")
    GENDERS_FIELD_NUMBER: _ClassVar[int]
    AGE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    genders: _containers.RepeatedScalarFieldContainer[str]
    age_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, genders: _Optional[_Iterable[str]] = ..., age_groups: _Optional[_Iterable[str]] = ...) -> None: ...

class ColorInfo(_message.Message):
    __slots__ = ("color_families", "colors")
    COLOR_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    COLORS_FIELD_NUMBER: _ClassVar[int]
    color_families: _containers.RepeatedScalarFieldContainer[str]
    colors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, color_families: _Optional[_Iterable[str]] = ..., colors: _Optional[_Iterable[str]] = ...) -> None: ...

class CustomAttribute(_message.Message):
    __slots__ = ("text", "numbers", "searchable", "indexable")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    SEARCHABLE_FIELD_NUMBER: _ClassVar[int]
    INDEXABLE_FIELD_NUMBER: _ClassVar[int]
    text: _containers.RepeatedScalarFieldContainer[str]
    numbers: _containers.RepeatedScalarFieldContainer[float]
    searchable: bool
    indexable: bool
    def __init__(self, text: _Optional[_Iterable[str]] = ..., numbers: _Optional[_Iterable[float]] = ..., searchable: bool = ..., indexable: bool = ...) -> None: ...

class FulfillmentInfo(_message.Message):
    __slots__ = ("type", "place_ids")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACE_IDS_FIELD_NUMBER: _ClassVar[int]
    type: str
    place_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., place_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("uri", "height", "width")
    URI_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    height: int
    width: int
    def __init__(self, uri: _Optional[str] = ..., height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...

class Interval(_message.Message):
    __slots__ = ("minimum", "exclusive_minimum", "maximum", "exclusive_maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: float
    exclusive_minimum: float
    maximum: float
    exclusive_maximum: float
    def __init__(self, minimum: _Optional[float] = ..., exclusive_minimum: _Optional[float] = ..., maximum: _Optional[float] = ..., exclusive_maximum: _Optional[float] = ...) -> None: ...

class PriceInfo(_message.Message):
    __slots__ = ("currency_code", "price", "original_price", "cost", "price_effective_time", "price_expire_time", "price_range")
    class PriceRange(_message.Message):
        __slots__ = ("price", "original_price")
        PRICE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
        price: Interval
        original_price: Interval
        def __init__(self, price: _Optional[_Union[Interval, _Mapping]] = ..., original_price: _Optional[_Union[Interval, _Mapping]] = ...) -> None: ...
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    PRICE_EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_RANGE_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    price: float
    original_price: float
    cost: float
    price_effective_time: _timestamp_pb2.Timestamp
    price_expire_time: _timestamp_pb2.Timestamp
    price_range: PriceInfo.PriceRange
    def __init__(self, currency_code: _Optional[str] = ..., price: _Optional[float] = ..., original_price: _Optional[float] = ..., cost: _Optional[float] = ..., price_effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., price_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., price_range: _Optional[_Union[PriceInfo.PriceRange, _Mapping]] = ...) -> None: ...

class Rating(_message.Message):
    __slots__ = ("rating_count", "average_rating", "rating_histogram")
    RATING_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    rating_count: int
    average_rating: float
    rating_histogram: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, rating_count: _Optional[int] = ..., average_rating: _Optional[float] = ..., rating_histogram: _Optional[_Iterable[int]] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("user_id", "ip_address", "user_agent", "direct_user_request")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    DIRECT_USER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    ip_address: str
    user_agent: str
    direct_user_request: bool
    def __init__(self, user_id: _Optional[str] = ..., ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ..., direct_user_request: bool = ...) -> None: ...

class LocalInventory(_message.Message):
    __slots__ = ("place_id", "price_info", "attributes", "fulfillment_types")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomAttribute
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomAttribute, _Mapping]] = ...) -> None: ...
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    price_info: PriceInfo
    attributes: _containers.MessageMap[str, CustomAttribute]
    fulfillment_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, place_id: _Optional[str] = ..., price_info: _Optional[_Union[PriceInfo, _Mapping]] = ..., attributes: _Optional[_Mapping[str, CustomAttribute]] = ..., fulfillment_types: _Optional[_Iterable[str]] = ...) -> None: ...
