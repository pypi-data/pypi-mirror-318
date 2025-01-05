from google.ads.searchads360.v0.common import metrics_pb2 as _metrics_pb2
from google.ads.searchads360.v0.common import segments_pb2 as _segments_pb2
from google.ads.searchads360.v0.common import value_pb2 as _value_pb2
from google.ads.searchads360.v0.enums import summary_row_setting_pb2 as _summary_row_setting_pb2
from google.ads.searchads360.v0.resources import accessible_bidding_strategy_pb2 as _accessible_bidding_strategy_pb2
from google.ads.searchads360.v0.resources import ad_group_pb2 as _ad_group_pb2
from google.ads.searchads360.v0.resources import ad_group_ad_pb2 as _ad_group_ad_pb2
from google.ads.searchads360.v0.resources import ad_group_ad_effective_label_pb2 as _ad_group_ad_effective_label_pb2
from google.ads.searchads360.v0.resources import ad_group_ad_label_pb2 as _ad_group_ad_label_pb2
from google.ads.searchads360.v0.resources import ad_group_asset_pb2 as _ad_group_asset_pb2
from google.ads.searchads360.v0.resources import ad_group_asset_set_pb2 as _ad_group_asset_set_pb2
from google.ads.searchads360.v0.resources import ad_group_audience_view_pb2 as _ad_group_audience_view_pb2
from google.ads.searchads360.v0.resources import ad_group_bid_modifier_pb2 as _ad_group_bid_modifier_pb2
from google.ads.searchads360.v0.resources import ad_group_criterion_pb2 as _ad_group_criterion_pb2
from google.ads.searchads360.v0.resources import ad_group_criterion_effective_label_pb2 as _ad_group_criterion_effective_label_pb2
from google.ads.searchads360.v0.resources import ad_group_criterion_label_pb2 as _ad_group_criterion_label_pb2
from google.ads.searchads360.v0.resources import ad_group_effective_label_pb2 as _ad_group_effective_label_pb2
from google.ads.searchads360.v0.resources import ad_group_label_pb2 as _ad_group_label_pb2
from google.ads.searchads360.v0.resources import age_range_view_pb2 as _age_range_view_pb2
from google.ads.searchads360.v0.resources import asset_pb2 as _asset_pb2
from google.ads.searchads360.v0.resources import asset_group_pb2 as _asset_group_pb2
from google.ads.searchads360.v0.resources import asset_group_asset_pb2 as _asset_group_asset_pb2
from google.ads.searchads360.v0.resources import asset_group_listing_group_filter_pb2 as _asset_group_listing_group_filter_pb2
from google.ads.searchads360.v0.resources import asset_group_signal_pb2 as _asset_group_signal_pb2
from google.ads.searchads360.v0.resources import asset_group_top_combination_view_pb2 as _asset_group_top_combination_view_pb2
from google.ads.searchads360.v0.resources import asset_set_pb2 as _asset_set_pb2
from google.ads.searchads360.v0.resources import asset_set_asset_pb2 as _asset_set_asset_pb2
from google.ads.searchads360.v0.resources import audience_pb2 as _audience_pb2
from google.ads.searchads360.v0.resources import bidding_strategy_pb2 as _bidding_strategy_pb2
from google.ads.searchads360.v0.resources import campaign_pb2 as _campaign_pb2
from google.ads.searchads360.v0.resources import campaign_asset_pb2 as _campaign_asset_pb2
from google.ads.searchads360.v0.resources import campaign_asset_set_pb2 as _campaign_asset_set_pb2
from google.ads.searchads360.v0.resources import campaign_audience_view_pb2 as _campaign_audience_view_pb2
from google.ads.searchads360.v0.resources import campaign_budget_pb2 as _campaign_budget_pb2
from google.ads.searchads360.v0.resources import campaign_criterion_pb2 as _campaign_criterion_pb2
from google.ads.searchads360.v0.resources import campaign_effective_label_pb2 as _campaign_effective_label_pb2
from google.ads.searchads360.v0.resources import campaign_label_pb2 as _campaign_label_pb2
from google.ads.searchads360.v0.resources import cart_data_sales_view_pb2 as _cart_data_sales_view_pb2
from google.ads.searchads360.v0.resources import conversion_pb2 as _conversion_pb2
from google.ads.searchads360.v0.resources import conversion_action_pb2 as _conversion_action_pb2
from google.ads.searchads360.v0.resources import conversion_custom_variable_pb2 as _conversion_custom_variable_pb2
from google.ads.searchads360.v0.resources import customer_pb2 as _customer_pb2
from google.ads.searchads360.v0.resources import customer_asset_pb2 as _customer_asset_pb2
from google.ads.searchads360.v0.resources import customer_asset_set_pb2 as _customer_asset_set_pb2
from google.ads.searchads360.v0.resources import customer_client_pb2 as _customer_client_pb2
from google.ads.searchads360.v0.resources import customer_manager_link_pb2 as _customer_manager_link_pb2
from google.ads.searchads360.v0.resources import dynamic_search_ads_search_term_view_pb2 as _dynamic_search_ads_search_term_view_pb2
from google.ads.searchads360.v0.resources import gender_view_pb2 as _gender_view_pb2
from google.ads.searchads360.v0.resources import geo_target_constant_pb2 as _geo_target_constant_pb2
from google.ads.searchads360.v0.resources import keyword_view_pb2 as _keyword_view_pb2
from google.ads.searchads360.v0.resources import label_pb2 as _label_pb2
from google.ads.searchads360.v0.resources import language_constant_pb2 as _language_constant_pb2
from google.ads.searchads360.v0.resources import location_view_pb2 as _location_view_pb2
from google.ads.searchads360.v0.resources import product_bidding_category_constant_pb2 as _product_bidding_category_constant_pb2
from google.ads.searchads360.v0.resources import product_group_view_pb2 as _product_group_view_pb2
from google.ads.searchads360.v0.resources import shopping_performance_view_pb2 as _shopping_performance_view_pb2
from google.ads.searchads360.v0.resources import user_list_pb2 as _user_list_pb2
from google.ads.searchads360.v0.resources import user_location_view_pb2 as _user_location_view_pb2
from google.ads.searchads360.v0.resources import visit_pb2 as _visit_pb2
from google.ads.searchads360.v0.resources import webpage_view_pb2 as _webpage_view_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchSearchAds360Request(_message.Message):
    __slots__ = ("customer_id", "query", "page_token", "page_size", "validate_only", "return_total_results_count", "summary_row_setting")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RETURN_TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ROW_SETTING_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    query: str
    page_token: str
    page_size: int
    validate_only: bool
    return_total_results_count: bool
    summary_row_setting: _summary_row_setting_pb2.SummaryRowSettingEnum.SummaryRowSetting
    def __init__(self, customer_id: _Optional[str] = ..., query: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., validate_only: bool = ..., return_total_results_count: bool = ..., summary_row_setting: _Optional[_Union[_summary_row_setting_pb2.SummaryRowSettingEnum.SummaryRowSetting, str]] = ...) -> None: ...

class SearchSearchAds360Response(_message.Message):
    __slots__ = ("results", "next_page_token", "total_results_count", "field_mask", "summary_row", "custom_column_headers", "conversion_custom_metric_headers", "conversion_custom_dimension_headers", "raw_event_conversion_metric_headers", "raw_event_conversion_dimension_headers")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ROW_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COLUMN_HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CUSTOM_METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CUSTOM_DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    RAW_EVENT_CONVERSION_METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    RAW_EVENT_CONVERSION_DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchAds360Row]
    next_page_token: str
    total_results_count: int
    field_mask: _field_mask_pb2.FieldMask
    summary_row: SearchAds360Row
    custom_column_headers: _containers.RepeatedCompositeFieldContainer[CustomColumnHeader]
    conversion_custom_metric_headers: _containers.RepeatedCompositeFieldContainer[ConversionCustomMetricHeader]
    conversion_custom_dimension_headers: _containers.RepeatedCompositeFieldContainer[ConversionCustomDimensionHeader]
    raw_event_conversion_metric_headers: _containers.RepeatedCompositeFieldContainer[RawEventConversionMetricHeader]
    raw_event_conversion_dimension_headers: _containers.RepeatedCompositeFieldContainer[RawEventConversionDimensionHeader]
    def __init__(self, results: _Optional[_Iterable[_Union[SearchAds360Row, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_results_count: _Optional[int] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., summary_row: _Optional[_Union[SearchAds360Row, _Mapping]] = ..., custom_column_headers: _Optional[_Iterable[_Union[CustomColumnHeader, _Mapping]]] = ..., conversion_custom_metric_headers: _Optional[_Iterable[_Union[ConversionCustomMetricHeader, _Mapping]]] = ..., conversion_custom_dimension_headers: _Optional[_Iterable[_Union[ConversionCustomDimensionHeader, _Mapping]]] = ..., raw_event_conversion_metric_headers: _Optional[_Iterable[_Union[RawEventConversionMetricHeader, _Mapping]]] = ..., raw_event_conversion_dimension_headers: _Optional[_Iterable[_Union[RawEventConversionDimensionHeader, _Mapping]]] = ...) -> None: ...

class SearchSearchAds360StreamRequest(_message.Message):
    __slots__ = ("customer_id", "query", "batch_size", "summary_row_setting")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ROW_SETTING_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    query: str
    batch_size: int
    summary_row_setting: _summary_row_setting_pb2.SummaryRowSettingEnum.SummaryRowSetting
    def __init__(self, customer_id: _Optional[str] = ..., query: _Optional[str] = ..., batch_size: _Optional[int] = ..., summary_row_setting: _Optional[_Union[_summary_row_setting_pb2.SummaryRowSettingEnum.SummaryRowSetting, str]] = ...) -> None: ...

class SearchSearchAds360StreamResponse(_message.Message):
    __slots__ = ("results", "field_mask", "summary_row", "custom_column_headers", "conversion_custom_metric_headers", "conversion_custom_dimension_headers", "raw_event_conversion_metric_headers", "raw_event_conversion_dimension_headers", "request_id")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ROW_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COLUMN_HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CUSTOM_METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CUSTOM_DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    RAW_EVENT_CONVERSION_METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    RAW_EVENT_CONVERSION_DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchAds360Row]
    field_mask: _field_mask_pb2.FieldMask
    summary_row: SearchAds360Row
    custom_column_headers: _containers.RepeatedCompositeFieldContainer[CustomColumnHeader]
    conversion_custom_metric_headers: _containers.RepeatedCompositeFieldContainer[ConversionCustomMetricHeader]
    conversion_custom_dimension_headers: _containers.RepeatedCompositeFieldContainer[ConversionCustomDimensionHeader]
    raw_event_conversion_metric_headers: _containers.RepeatedCompositeFieldContainer[RawEventConversionMetricHeader]
    raw_event_conversion_dimension_headers: _containers.RepeatedCompositeFieldContainer[RawEventConversionDimensionHeader]
    request_id: str
    def __init__(self, results: _Optional[_Iterable[_Union[SearchAds360Row, _Mapping]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., summary_row: _Optional[_Union[SearchAds360Row, _Mapping]] = ..., custom_column_headers: _Optional[_Iterable[_Union[CustomColumnHeader, _Mapping]]] = ..., conversion_custom_metric_headers: _Optional[_Iterable[_Union[ConversionCustomMetricHeader, _Mapping]]] = ..., conversion_custom_dimension_headers: _Optional[_Iterable[_Union[ConversionCustomDimensionHeader, _Mapping]]] = ..., raw_event_conversion_metric_headers: _Optional[_Iterable[_Union[RawEventConversionMetricHeader, _Mapping]]] = ..., raw_event_conversion_dimension_headers: _Optional[_Iterable[_Union[RawEventConversionDimensionHeader, _Mapping]]] = ..., request_id: _Optional[str] = ...) -> None: ...

class SearchAds360Row(_message.Message):
    __slots__ = ("ad_group", "ad_group_ad", "ad_group_ad_effective_label", "ad_group_ad_label", "ad_group_asset", "ad_group_asset_set", "ad_group_audience_view", "ad_group_bid_modifier", "ad_group_criterion", "ad_group_criterion_effective_label", "ad_group_criterion_label", "ad_group_effective_label", "ad_group_label", "age_range_view", "asset", "asset_group_asset", "asset_group_signal", "asset_group_listing_group_filter", "asset_group_top_combination_view", "asset_group", "asset_set_asset", "asset_set", "bidding_strategy", "campaign_budget", "campaign", "campaign_asset", "campaign_asset_set", "campaign_audience_view", "campaign_criterion", "campaign_effective_label", "campaign_label", "cart_data_sales_view", "audience", "conversion_action", "conversion_custom_variable", "customer", "customer_asset", "customer_asset_set", "accessible_bidding_strategy", "customer_manager_link", "customer_client", "dynamic_search_ads_search_term_view", "gender_view", "geo_target_constant", "keyword_view", "label", "language_constant", "location_view", "product_bidding_category_constant", "product_group_view", "shopping_performance_view", "user_list", "user_location_view", "webpage_view", "visit", "conversion", "metrics", "segments", "custom_columns")
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_EFFECTIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_LABEL_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_ASSET_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_ASSET_SET_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AUDIENCE_VIEW_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_CRITERION_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_CRITERION_EFFECTIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_CRITERION_LABEL_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_EFFECTIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_LABEL_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_VIEW_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_LISTING_GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_TOP_COMBINATION_VIEW_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    ASSET_SET_ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_SET_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ASSET_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ASSET_SET_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_AUDIENCE_VIEW_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_CRITERION_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_EFFECTIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_LABEL_FIELD_NUMBER: _ClassVar[int]
    CART_DATA_SALES_VIEW_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CUSTOM_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ASSET_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ASSET_SET_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBLE_BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MANAGER_LINK_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CLIENT_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_SEARCH_ADS_SEARCH_TERM_VIEW_FIELD_NUMBER: _ClassVar[int]
    GENDER_VIEW_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_VIEW_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_VIEW_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BIDDING_CATEGORY_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_GROUP_VIEW_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_PERFORMANCE_VIEW_FIELD_NUMBER: _ClassVar[int]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    USER_LOCATION_VIEW_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_VIEW_FIELD_NUMBER: _ClassVar[int]
    VISIT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ad_group: _ad_group_pb2.AdGroup
    ad_group_ad: _ad_group_ad_pb2.AdGroupAd
    ad_group_ad_effective_label: _ad_group_ad_effective_label_pb2.AdGroupAdEffectiveLabel
    ad_group_ad_label: _ad_group_ad_label_pb2.AdGroupAdLabel
    ad_group_asset: _ad_group_asset_pb2.AdGroupAsset
    ad_group_asset_set: _ad_group_asset_set_pb2.AdGroupAssetSet
    ad_group_audience_view: _ad_group_audience_view_pb2.AdGroupAudienceView
    ad_group_bid_modifier: _ad_group_bid_modifier_pb2.AdGroupBidModifier
    ad_group_criterion: _ad_group_criterion_pb2.AdGroupCriterion
    ad_group_criterion_effective_label: _ad_group_criterion_effective_label_pb2.AdGroupCriterionEffectiveLabel
    ad_group_criterion_label: _ad_group_criterion_label_pb2.AdGroupCriterionLabel
    ad_group_effective_label: _ad_group_effective_label_pb2.AdGroupEffectiveLabel
    ad_group_label: _ad_group_label_pb2.AdGroupLabel
    age_range_view: _age_range_view_pb2.AgeRangeView
    asset: _asset_pb2.Asset
    asset_group_asset: _asset_group_asset_pb2.AssetGroupAsset
    asset_group_signal: _asset_group_signal_pb2.AssetGroupSignal
    asset_group_listing_group_filter: _asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter
    asset_group_top_combination_view: _asset_group_top_combination_view_pb2.AssetGroupTopCombinationView
    asset_group: _asset_group_pb2.AssetGroup
    asset_set_asset: _asset_set_asset_pb2.AssetSetAsset
    asset_set: _asset_set_pb2.AssetSet
    bidding_strategy: _bidding_strategy_pb2.BiddingStrategy
    campaign_budget: _campaign_budget_pb2.CampaignBudget
    campaign: _campaign_pb2.Campaign
    campaign_asset: _campaign_asset_pb2.CampaignAsset
    campaign_asset_set: _campaign_asset_set_pb2.CampaignAssetSet
    campaign_audience_view: _campaign_audience_view_pb2.CampaignAudienceView
    campaign_criterion: _campaign_criterion_pb2.CampaignCriterion
    campaign_effective_label: _campaign_effective_label_pb2.CampaignEffectiveLabel
    campaign_label: _campaign_label_pb2.CampaignLabel
    cart_data_sales_view: _cart_data_sales_view_pb2.CartDataSalesView
    audience: _audience_pb2.Audience
    conversion_action: _conversion_action_pb2.ConversionAction
    conversion_custom_variable: _conversion_custom_variable_pb2.ConversionCustomVariable
    customer: _customer_pb2.Customer
    customer_asset: _customer_asset_pb2.CustomerAsset
    customer_asset_set: _customer_asset_set_pb2.CustomerAssetSet
    accessible_bidding_strategy: _accessible_bidding_strategy_pb2.AccessibleBiddingStrategy
    customer_manager_link: _customer_manager_link_pb2.CustomerManagerLink
    customer_client: _customer_client_pb2.CustomerClient
    dynamic_search_ads_search_term_view: _dynamic_search_ads_search_term_view_pb2.DynamicSearchAdsSearchTermView
    gender_view: _gender_view_pb2.GenderView
    geo_target_constant: _geo_target_constant_pb2.GeoTargetConstant
    keyword_view: _keyword_view_pb2.KeywordView
    label: _label_pb2.Label
    language_constant: _language_constant_pb2.LanguageConstant
    location_view: _location_view_pb2.LocationView
    product_bidding_category_constant: _product_bidding_category_constant_pb2.ProductBiddingCategoryConstant
    product_group_view: _product_group_view_pb2.ProductGroupView
    shopping_performance_view: _shopping_performance_view_pb2.ShoppingPerformanceView
    user_list: _user_list_pb2.UserList
    user_location_view: _user_location_view_pb2.UserLocationView
    webpage_view: _webpage_view_pb2.WebpageView
    visit: _visit_pb2.Visit
    conversion: _conversion_pb2.Conversion
    metrics: _metrics_pb2.Metrics
    segments: _segments_pb2.Segments
    custom_columns: _containers.RepeatedCompositeFieldContainer[_value_pb2.Value]
    def __init__(self, ad_group: _Optional[_Union[_ad_group_pb2.AdGroup, _Mapping]] = ..., ad_group_ad: _Optional[_Union[_ad_group_ad_pb2.AdGroupAd, _Mapping]] = ..., ad_group_ad_effective_label: _Optional[_Union[_ad_group_ad_effective_label_pb2.AdGroupAdEffectiveLabel, _Mapping]] = ..., ad_group_ad_label: _Optional[_Union[_ad_group_ad_label_pb2.AdGroupAdLabel, _Mapping]] = ..., ad_group_asset: _Optional[_Union[_ad_group_asset_pb2.AdGroupAsset, _Mapping]] = ..., ad_group_asset_set: _Optional[_Union[_ad_group_asset_set_pb2.AdGroupAssetSet, _Mapping]] = ..., ad_group_audience_view: _Optional[_Union[_ad_group_audience_view_pb2.AdGroupAudienceView, _Mapping]] = ..., ad_group_bid_modifier: _Optional[_Union[_ad_group_bid_modifier_pb2.AdGroupBidModifier, _Mapping]] = ..., ad_group_criterion: _Optional[_Union[_ad_group_criterion_pb2.AdGroupCriterion, _Mapping]] = ..., ad_group_criterion_effective_label: _Optional[_Union[_ad_group_criterion_effective_label_pb2.AdGroupCriterionEffectiveLabel, _Mapping]] = ..., ad_group_criterion_label: _Optional[_Union[_ad_group_criterion_label_pb2.AdGroupCriterionLabel, _Mapping]] = ..., ad_group_effective_label: _Optional[_Union[_ad_group_effective_label_pb2.AdGroupEffectiveLabel, _Mapping]] = ..., ad_group_label: _Optional[_Union[_ad_group_label_pb2.AdGroupLabel, _Mapping]] = ..., age_range_view: _Optional[_Union[_age_range_view_pb2.AgeRangeView, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.Asset, _Mapping]] = ..., asset_group_asset: _Optional[_Union[_asset_group_asset_pb2.AssetGroupAsset, _Mapping]] = ..., asset_group_signal: _Optional[_Union[_asset_group_signal_pb2.AssetGroupSignal, _Mapping]] = ..., asset_group_listing_group_filter: _Optional[_Union[_asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter, _Mapping]] = ..., asset_group_top_combination_view: _Optional[_Union[_asset_group_top_combination_view_pb2.AssetGroupTopCombinationView, _Mapping]] = ..., asset_group: _Optional[_Union[_asset_group_pb2.AssetGroup, _Mapping]] = ..., asset_set_asset: _Optional[_Union[_asset_set_asset_pb2.AssetSetAsset, _Mapping]] = ..., asset_set: _Optional[_Union[_asset_set_pb2.AssetSet, _Mapping]] = ..., bidding_strategy: _Optional[_Union[_bidding_strategy_pb2.BiddingStrategy, _Mapping]] = ..., campaign_budget: _Optional[_Union[_campaign_budget_pb2.CampaignBudget, _Mapping]] = ..., campaign: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]] = ..., campaign_asset: _Optional[_Union[_campaign_asset_pb2.CampaignAsset, _Mapping]] = ..., campaign_asset_set: _Optional[_Union[_campaign_asset_set_pb2.CampaignAssetSet, _Mapping]] = ..., campaign_audience_view: _Optional[_Union[_campaign_audience_view_pb2.CampaignAudienceView, _Mapping]] = ..., campaign_criterion: _Optional[_Union[_campaign_criterion_pb2.CampaignCriterion, _Mapping]] = ..., campaign_effective_label: _Optional[_Union[_campaign_effective_label_pb2.CampaignEffectiveLabel, _Mapping]] = ..., campaign_label: _Optional[_Union[_campaign_label_pb2.CampaignLabel, _Mapping]] = ..., cart_data_sales_view: _Optional[_Union[_cart_data_sales_view_pb2.CartDataSalesView, _Mapping]] = ..., audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ..., conversion_action: _Optional[_Union[_conversion_action_pb2.ConversionAction, _Mapping]] = ..., conversion_custom_variable: _Optional[_Union[_conversion_custom_variable_pb2.ConversionCustomVariable, _Mapping]] = ..., customer: _Optional[_Union[_customer_pb2.Customer, _Mapping]] = ..., customer_asset: _Optional[_Union[_customer_asset_pb2.CustomerAsset, _Mapping]] = ..., customer_asset_set: _Optional[_Union[_customer_asset_set_pb2.CustomerAssetSet, _Mapping]] = ..., accessible_bidding_strategy: _Optional[_Union[_accessible_bidding_strategy_pb2.AccessibleBiddingStrategy, _Mapping]] = ..., customer_manager_link: _Optional[_Union[_customer_manager_link_pb2.CustomerManagerLink, _Mapping]] = ..., customer_client: _Optional[_Union[_customer_client_pb2.CustomerClient, _Mapping]] = ..., dynamic_search_ads_search_term_view: _Optional[_Union[_dynamic_search_ads_search_term_view_pb2.DynamicSearchAdsSearchTermView, _Mapping]] = ..., gender_view: _Optional[_Union[_gender_view_pb2.GenderView, _Mapping]] = ..., geo_target_constant: _Optional[_Union[_geo_target_constant_pb2.GeoTargetConstant, _Mapping]] = ..., keyword_view: _Optional[_Union[_keyword_view_pb2.KeywordView, _Mapping]] = ..., label: _Optional[_Union[_label_pb2.Label, _Mapping]] = ..., language_constant: _Optional[_Union[_language_constant_pb2.LanguageConstant, _Mapping]] = ..., location_view: _Optional[_Union[_location_view_pb2.LocationView, _Mapping]] = ..., product_bidding_category_constant: _Optional[_Union[_product_bidding_category_constant_pb2.ProductBiddingCategoryConstant, _Mapping]] = ..., product_group_view: _Optional[_Union[_product_group_view_pb2.ProductGroupView, _Mapping]] = ..., shopping_performance_view: _Optional[_Union[_shopping_performance_view_pb2.ShoppingPerformanceView, _Mapping]] = ..., user_list: _Optional[_Union[_user_list_pb2.UserList, _Mapping]] = ..., user_location_view: _Optional[_Union[_user_location_view_pb2.UserLocationView, _Mapping]] = ..., webpage_view: _Optional[_Union[_webpage_view_pb2.WebpageView, _Mapping]] = ..., visit: _Optional[_Union[_visit_pb2.Visit, _Mapping]] = ..., conversion: _Optional[_Union[_conversion_pb2.Conversion, _Mapping]] = ..., metrics: _Optional[_Union[_metrics_pb2.Metrics, _Mapping]] = ..., segments: _Optional[_Union[_segments_pb2.Segments, _Mapping]] = ..., custom_columns: _Optional[_Iterable[_Union[_value_pb2.Value, _Mapping]]] = ...) -> None: ...

class CustomColumnHeader(_message.Message):
    __slots__ = ("id", "name", "references_metrics")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_METRICS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    references_metrics: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., references_metrics: bool = ...) -> None: ...

class ConversionCustomMetricHeader(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ConversionCustomDimensionHeader(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class RawEventConversionMetricHeader(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class RawEventConversionDimensionHeader(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
