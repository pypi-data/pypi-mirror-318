from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v17.common import dates_pb2 as _dates_pb2
from google.ads.googleads.v17.common import keyword_plan_common_pb2 as _keyword_plan_common_pb2
from google.ads.googleads.v17.enums import keyword_match_type_pb2 as _keyword_match_type_pb2
from google.ads.googleads.v17.enums import keyword_plan_keyword_annotation_pb2 as _keyword_plan_keyword_annotation_pb2
from google.ads.googleads.v17.enums import keyword_plan_network_pb2 as _keyword_plan_network_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateKeywordIdeasRequest(_message.Message):
    __slots__ = ("customer_id", "language", "geo_target_constants", "include_adult_keywords", "page_token", "page_size", "keyword_plan_network", "keyword_annotation", "aggregate_metrics", "historical_metrics_options", "keyword_and_url_seed", "keyword_seed", "url_seed", "site_seed")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ADULT_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_PLAN_NETWORK_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRICS_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_METRICS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_AND_URL_SEED_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_SEED_FIELD_NUMBER: _ClassVar[int]
    URL_SEED_FIELD_NUMBER: _ClassVar[int]
    SITE_SEED_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    language: str
    geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
    include_adult_keywords: bool
    page_token: str
    page_size: int
    keyword_plan_network: _keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork
    keyword_annotation: _containers.RepeatedScalarFieldContainer[_keyword_plan_keyword_annotation_pb2.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation]
    aggregate_metrics: _keyword_plan_common_pb2.KeywordPlanAggregateMetrics
    historical_metrics_options: _keyword_plan_common_pb2.HistoricalMetricsOptions
    keyword_and_url_seed: KeywordAndUrlSeed
    keyword_seed: KeywordSeed
    url_seed: UrlSeed
    site_seed: SiteSeed
    def __init__(self, customer_id: _Optional[str] = ..., language: _Optional[str] = ..., geo_target_constants: _Optional[_Iterable[str]] = ..., include_adult_keywords: bool = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., keyword_plan_network: _Optional[_Union[_keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork, str]] = ..., keyword_annotation: _Optional[_Iterable[_Union[_keyword_plan_keyword_annotation_pb2.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation, str]]] = ..., aggregate_metrics: _Optional[_Union[_keyword_plan_common_pb2.KeywordPlanAggregateMetrics, _Mapping]] = ..., historical_metrics_options: _Optional[_Union[_keyword_plan_common_pb2.HistoricalMetricsOptions, _Mapping]] = ..., keyword_and_url_seed: _Optional[_Union[KeywordAndUrlSeed, _Mapping]] = ..., keyword_seed: _Optional[_Union[KeywordSeed, _Mapping]] = ..., url_seed: _Optional[_Union[UrlSeed, _Mapping]] = ..., site_seed: _Optional[_Union[SiteSeed, _Mapping]] = ...) -> None: ...

class KeywordAndUrlSeed(_message.Message):
    __slots__ = ("url", "keywords")
    URL_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    url: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, url: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ...) -> None: ...

class KeywordSeed(_message.Message):
    __slots__ = ("keywords",)
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    keywords: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keywords: _Optional[_Iterable[str]] = ...) -> None: ...

class SiteSeed(_message.Message):
    __slots__ = ("site",)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: str
    def __init__(self, site: _Optional[str] = ...) -> None: ...

class UrlSeed(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GenerateKeywordIdeaResponse(_message.Message):
    __slots__ = ("results", "aggregate_metric_results", "next_page_token", "total_size")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRIC_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GenerateKeywordIdeaResult]
    aggregate_metric_results: _keyword_plan_common_pb2.KeywordPlanAggregateMetricResults
    next_page_token: str
    total_size: int
    def __init__(self, results: _Optional[_Iterable[_Union[GenerateKeywordIdeaResult, _Mapping]]] = ..., aggregate_metric_results: _Optional[_Union[_keyword_plan_common_pb2.KeywordPlanAggregateMetricResults, _Mapping]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class GenerateKeywordIdeaResult(_message.Message):
    __slots__ = ("text", "keyword_idea_metrics", "keyword_annotations", "close_variants")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_IDEA_METRICS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CLOSE_VARIANTS_FIELD_NUMBER: _ClassVar[int]
    text: str
    keyword_idea_metrics: _keyword_plan_common_pb2.KeywordPlanHistoricalMetrics
    keyword_annotations: _keyword_plan_common_pb2.KeywordAnnotations
    close_variants: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, text: _Optional[str] = ..., keyword_idea_metrics: _Optional[_Union[_keyword_plan_common_pb2.KeywordPlanHistoricalMetrics, _Mapping]] = ..., keyword_annotations: _Optional[_Union[_keyword_plan_common_pb2.KeywordAnnotations, _Mapping]] = ..., close_variants: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateKeywordHistoricalMetricsRequest(_message.Message):
    __slots__ = ("customer_id", "keywords", "language", "include_adult_keywords", "geo_target_constants", "keyword_plan_network", "aggregate_metrics", "historical_metrics_options")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ADULT_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_PLAN_NETWORK_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRICS_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_METRICS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    language: str
    include_adult_keywords: bool
    geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
    keyword_plan_network: _keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork
    aggregate_metrics: _keyword_plan_common_pb2.KeywordPlanAggregateMetrics
    historical_metrics_options: _keyword_plan_common_pb2.HistoricalMetricsOptions
    def __init__(self, customer_id: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ..., language: _Optional[str] = ..., include_adult_keywords: bool = ..., geo_target_constants: _Optional[_Iterable[str]] = ..., keyword_plan_network: _Optional[_Union[_keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork, str]] = ..., aggregate_metrics: _Optional[_Union[_keyword_plan_common_pb2.KeywordPlanAggregateMetrics, _Mapping]] = ..., historical_metrics_options: _Optional[_Union[_keyword_plan_common_pb2.HistoricalMetricsOptions, _Mapping]] = ...) -> None: ...

class GenerateKeywordHistoricalMetricsResponse(_message.Message):
    __slots__ = ("results", "aggregate_metric_results")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRIC_RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GenerateKeywordHistoricalMetricsResult]
    aggregate_metric_results: _keyword_plan_common_pb2.KeywordPlanAggregateMetricResults
    def __init__(self, results: _Optional[_Iterable[_Union[GenerateKeywordHistoricalMetricsResult, _Mapping]]] = ..., aggregate_metric_results: _Optional[_Union[_keyword_plan_common_pb2.KeywordPlanAggregateMetricResults, _Mapping]] = ...) -> None: ...

class GenerateKeywordHistoricalMetricsResult(_message.Message):
    __slots__ = ("text", "close_variants", "keyword_metrics")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_VARIANTS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_METRICS_FIELD_NUMBER: _ClassVar[int]
    text: str
    close_variants: _containers.RepeatedScalarFieldContainer[str]
    keyword_metrics: _keyword_plan_common_pb2.KeywordPlanHistoricalMetrics
    def __init__(self, text: _Optional[str] = ..., close_variants: _Optional[_Iterable[str]] = ..., keyword_metrics: _Optional[_Union[_keyword_plan_common_pb2.KeywordPlanHistoricalMetrics, _Mapping]] = ...) -> None: ...

class GenerateAdGroupThemesRequest(_message.Message):
    __slots__ = ("customer_id", "keywords", "ad_groups")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    AD_GROUPS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    ad_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, customer_id: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ..., ad_groups: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateAdGroupThemesResponse(_message.Message):
    __slots__ = ("ad_group_keyword_suggestions", "unusable_ad_groups")
    AD_GROUP_KEYWORD_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    UNUSABLE_AD_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ad_group_keyword_suggestions: _containers.RepeatedCompositeFieldContainer[AdGroupKeywordSuggestion]
    unusable_ad_groups: _containers.RepeatedCompositeFieldContainer[UnusableAdGroup]
    def __init__(self, ad_group_keyword_suggestions: _Optional[_Iterable[_Union[AdGroupKeywordSuggestion, _Mapping]]] = ..., unusable_ad_groups: _Optional[_Iterable[_Union[UnusableAdGroup, _Mapping]]] = ...) -> None: ...

class AdGroupKeywordSuggestion(_message.Message):
    __slots__ = ("keyword_text", "suggested_keyword_text", "suggested_match_type", "suggested_ad_group", "suggested_campaign")
    KEYWORD_TEXT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_KEYWORD_TEXT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    keyword_text: str
    suggested_keyword_text: str
    suggested_match_type: _keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType
    suggested_ad_group: str
    suggested_campaign: str
    def __init__(self, keyword_text: _Optional[str] = ..., suggested_keyword_text: _Optional[str] = ..., suggested_match_type: _Optional[_Union[_keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType, str]] = ..., suggested_ad_group: _Optional[str] = ..., suggested_campaign: _Optional[str] = ...) -> None: ...

class UnusableAdGroup(_message.Message):
    __slots__ = ("ad_group", "campaign")
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ad_group: str
    campaign: str
    def __init__(self, ad_group: _Optional[str] = ..., campaign: _Optional[str] = ...) -> None: ...

class GenerateKeywordForecastMetricsRequest(_message.Message):
    __slots__ = ("customer_id", "currency_code", "forecast_period", "campaign")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    FORECAST_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    currency_code: str
    forecast_period: _dates_pb2.DateRange
    campaign: CampaignToForecast
    def __init__(self, customer_id: _Optional[str] = ..., currency_code: _Optional[str] = ..., forecast_period: _Optional[_Union[_dates_pb2.DateRange, _Mapping]] = ..., campaign: _Optional[_Union[CampaignToForecast, _Mapping]] = ...) -> None: ...

class CampaignToForecast(_message.Message):
    __slots__ = ("language_constants", "geo_modifiers", "keyword_plan_network", "negative_keywords", "bidding_strategy", "conversion_rate", "ad_groups")
    class CampaignBiddingStrategy(_message.Message):
        __slots__ = ("manual_cpc_bidding_strategy", "maximize_clicks_bidding_strategy", "maximize_conversions_bidding_strategy")
        MANUAL_CPC_BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
        MAXIMIZE_CLICKS_BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
        MAXIMIZE_CONVERSIONS_BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
        manual_cpc_bidding_strategy: ManualCpcBiddingStrategy
        maximize_clicks_bidding_strategy: MaximizeClicksBiddingStrategy
        maximize_conversions_bidding_strategy: MaximizeConversionsBiddingStrategy
        def __init__(self, manual_cpc_bidding_strategy: _Optional[_Union[ManualCpcBiddingStrategy, _Mapping]] = ..., maximize_clicks_bidding_strategy: _Optional[_Union[MaximizeClicksBiddingStrategy, _Mapping]] = ..., maximize_conversions_bidding_strategy: _Optional[_Union[MaximizeConversionsBiddingStrategy, _Mapping]] = ...) -> None: ...
    LANGUAGE_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    GEO_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_PLAN_NETWORK_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_RATE_FIELD_NUMBER: _ClassVar[int]
    AD_GROUPS_FIELD_NUMBER: _ClassVar[int]
    language_constants: _containers.RepeatedScalarFieldContainer[str]
    geo_modifiers: _containers.RepeatedCompositeFieldContainer[CriterionBidModifier]
    keyword_plan_network: _keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork
    negative_keywords: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.KeywordInfo]
    bidding_strategy: CampaignToForecast.CampaignBiddingStrategy
    conversion_rate: float
    ad_groups: _containers.RepeatedCompositeFieldContainer[ForecastAdGroup]
    def __init__(self, language_constants: _Optional[_Iterable[str]] = ..., geo_modifiers: _Optional[_Iterable[_Union[CriterionBidModifier, _Mapping]]] = ..., keyword_plan_network: _Optional[_Union[_keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork, str]] = ..., negative_keywords: _Optional[_Iterable[_Union[_criteria_pb2.KeywordInfo, _Mapping]]] = ..., bidding_strategy: _Optional[_Union[CampaignToForecast.CampaignBiddingStrategy, _Mapping]] = ..., conversion_rate: _Optional[float] = ..., ad_groups: _Optional[_Iterable[_Union[ForecastAdGroup, _Mapping]]] = ...) -> None: ...

class ForecastAdGroup(_message.Message):
    __slots__ = ("max_cpc_bid_micros", "biddable_keywords", "negative_keywords")
    MAX_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    max_cpc_bid_micros: int
    biddable_keywords: _containers.RepeatedCompositeFieldContainer[BiddableKeyword]
    negative_keywords: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.KeywordInfo]
    def __init__(self, max_cpc_bid_micros: _Optional[int] = ..., biddable_keywords: _Optional[_Iterable[_Union[BiddableKeyword, _Mapping]]] = ..., negative_keywords: _Optional[_Iterable[_Union[_criteria_pb2.KeywordInfo, _Mapping]]] = ...) -> None: ...

class BiddableKeyword(_message.Message):
    __slots__ = ("keyword", "max_cpc_bid_micros")
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    MAX_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    keyword: _criteria_pb2.KeywordInfo
    max_cpc_bid_micros: int
    def __init__(self, keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., max_cpc_bid_micros: _Optional[int] = ...) -> None: ...

class CriterionBidModifier(_message.Message):
    __slots__ = ("geo_target_constant", "bid_modifier")
    GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    geo_target_constant: str
    bid_modifier: float
    def __init__(self, geo_target_constant: _Optional[str] = ..., bid_modifier: _Optional[float] = ...) -> None: ...

class ManualCpcBiddingStrategy(_message.Message):
    __slots__ = ("daily_budget_micros", "max_cpc_bid_micros")
    DAILY_BUDGET_MICROS_FIELD_NUMBER: _ClassVar[int]
    MAX_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    daily_budget_micros: int
    max_cpc_bid_micros: int
    def __init__(self, daily_budget_micros: _Optional[int] = ..., max_cpc_bid_micros: _Optional[int] = ...) -> None: ...

class MaximizeClicksBiddingStrategy(_message.Message):
    __slots__ = ("daily_target_spend_micros", "max_cpc_bid_ceiling_micros")
    DAILY_TARGET_SPEND_MICROS_FIELD_NUMBER: _ClassVar[int]
    MAX_CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    daily_target_spend_micros: int
    max_cpc_bid_ceiling_micros: int
    def __init__(self, daily_target_spend_micros: _Optional[int] = ..., max_cpc_bid_ceiling_micros: _Optional[int] = ...) -> None: ...

class MaximizeConversionsBiddingStrategy(_message.Message):
    __slots__ = ("daily_target_spend_micros",)
    DAILY_TARGET_SPEND_MICROS_FIELD_NUMBER: _ClassVar[int]
    daily_target_spend_micros: int
    def __init__(self, daily_target_spend_micros: _Optional[int] = ...) -> None: ...

class GenerateKeywordForecastMetricsResponse(_message.Message):
    __slots__ = ("campaign_forecast_metrics",)
    CAMPAIGN_FORECAST_METRICS_FIELD_NUMBER: _ClassVar[int]
    campaign_forecast_metrics: KeywordForecastMetrics
    def __init__(self, campaign_forecast_metrics: _Optional[_Union[KeywordForecastMetrics, _Mapping]] = ...) -> None: ...

class KeywordForecastMetrics(_message.Message):
    __slots__ = ("impressions", "click_through_rate", "average_cpc_micros", "clicks", "cost_micros", "conversions", "conversion_rate", "average_cpa_micros")
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    CLICK_THROUGH_RATE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CPC_MICROS_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_RATE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
    impressions: float
    click_through_rate: float
    average_cpc_micros: int
    clicks: float
    cost_micros: int
    conversions: float
    conversion_rate: float
    average_cpa_micros: int
    def __init__(self, impressions: _Optional[float] = ..., click_through_rate: _Optional[float] = ..., average_cpc_micros: _Optional[int] = ..., clicks: _Optional[float] = ..., cost_micros: _Optional[int] = ..., conversions: _Optional[float] = ..., conversion_rate: _Optional[float] = ..., average_cpa_micros: _Optional[int] = ...) -> None: ...
