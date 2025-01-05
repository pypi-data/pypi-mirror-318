from google.ads.googleads.v18.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v18.enums import ad_destination_type_pb2 as _ad_destination_type_pb2
from google.ads.googleads.v18.enums import ad_format_type_pb2 as _ad_format_type_pb2
from google.ads.googleads.v18.enums import ad_network_type_pb2 as _ad_network_type_pb2
from google.ads.googleads.v18.enums import budget_campaign_association_status_pb2 as _budget_campaign_association_status_pb2
from google.ads.googleads.v18.enums import click_type_pb2 as _click_type_pb2
from google.ads.googleads.v18.enums import conversion_action_category_pb2 as _conversion_action_category_pb2
from google.ads.googleads.v18.enums import conversion_attribution_event_type_pb2 as _conversion_attribution_event_type_pb2
from google.ads.googleads.v18.enums import conversion_lag_bucket_pb2 as _conversion_lag_bucket_pb2
from google.ads.googleads.v18.enums import conversion_or_adjustment_lag_bucket_pb2 as _conversion_or_adjustment_lag_bucket_pb2
from google.ads.googleads.v18.enums import conversion_value_rule_primary_dimension_pb2 as _conversion_value_rule_primary_dimension_pb2
from google.ads.googleads.v18.enums import converting_user_prior_engagement_type_and_ltv_bucket_pb2 as _converting_user_prior_engagement_type_and_ltv_bucket_pb2
from google.ads.googleads.v18.enums import day_of_week_pb2 as _day_of_week_pb2
from google.ads.googleads.v18.enums import device_pb2 as _device_pb2
from google.ads.googleads.v18.enums import external_conversion_source_pb2 as _external_conversion_source_pb2
from google.ads.googleads.v18.enums import hotel_date_selection_type_pb2 as _hotel_date_selection_type_pb2
from google.ads.googleads.v18.enums import hotel_price_bucket_pb2 as _hotel_price_bucket_pb2
from google.ads.googleads.v18.enums import hotel_rate_type_pb2 as _hotel_rate_type_pb2
from google.ads.googleads.v18.enums import month_of_year_pb2 as _month_of_year_pb2
from google.ads.googleads.v18.enums import placeholder_type_pb2 as _placeholder_type_pb2
from google.ads.googleads.v18.enums import product_channel_pb2 as _product_channel_pb2
from google.ads.googleads.v18.enums import product_channel_exclusivity_pb2 as _product_channel_exclusivity_pb2
from google.ads.googleads.v18.enums import product_condition_pb2 as _product_condition_pb2
from google.ads.googleads.v18.enums import recommendation_type_pb2 as _recommendation_type_pb2
from google.ads.googleads.v18.enums import search_engine_results_page_type_pb2 as _search_engine_results_page_type_pb2
from google.ads.googleads.v18.enums import search_term_match_type_pb2 as _search_term_match_type_pb2
from google.ads.googleads.v18.enums import sk_ad_network_ad_event_type_pb2 as _sk_ad_network_ad_event_type_pb2
from google.ads.googleads.v18.enums import sk_ad_network_attribution_credit_pb2 as _sk_ad_network_attribution_credit_pb2
from google.ads.googleads.v18.enums import sk_ad_network_coarse_conversion_value_pb2 as _sk_ad_network_coarse_conversion_value_pb2
from google.ads.googleads.v18.enums import sk_ad_network_source_type_pb2 as _sk_ad_network_source_type_pb2
from google.ads.googleads.v18.enums import sk_ad_network_user_type_pb2 as _sk_ad_network_user_type_pb2
from google.ads.googleads.v18.enums import slot_pb2 as _slot_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Segments(_message.Message):
    __slots__ = ("activity_account_id", "activity_city", "activity_country", "activity_rating", "activity_state", "external_activity_id", "ad_destination_type", "ad_format_type", "ad_network_type", "ad_group", "asset_group", "auction_insight_domain", "budget_campaign_association_status", "campaign", "click_type", "conversion_action", "conversion_action_category", "conversion_action_name", "conversion_adjustment", "conversion_attribution_event_type", "conversion_lag_bucket", "conversion_or_adjustment_lag_bucket", "date", "day_of_week", "device", "external_conversion_source", "geo_target_airport", "geo_target_canton", "geo_target_city", "geo_target_country", "geo_target_county", "geo_target_district", "geo_target_metro", "geo_target_most_specific_location", "geo_target_postal_code", "geo_target_province", "geo_target_region", "geo_target_state", "hotel_booking_window_days", "hotel_center_id", "hotel_check_in_date", "hotel_check_in_day_of_week", "hotel_city", "hotel_class", "hotel_country", "hotel_date_selection_type", "hotel_length_of_stay", "hotel_rate_rule_id", "hotel_rate_type", "hotel_price_bucket", "hotel_state", "hour", "interaction_on_this_extension", "keyword", "month", "month_of_year", "partner_hotel_id", "placeholder_type", "product_aggregator_id", "product_category_level1", "product_category_level2", "product_category_level3", "product_category_level4", "product_category_level5", "product_brand", "product_channel", "product_channel_exclusivity", "product_condition", "product_country", "product_custom_attribute0", "product_custom_attribute1", "product_custom_attribute2", "product_custom_attribute3", "product_custom_attribute4", "product_feed_label", "product_item_id", "product_language", "product_merchant_id", "product_store_id", "product_title", "product_type_l1", "product_type_l2", "product_type_l3", "product_type_l4", "product_type_l5", "quarter", "travel_destination_city", "travel_destination_country", "travel_destination_region", "recommendation_type", "search_engine_results_page_type", "search_subcategory", "search_term", "search_term_match_type", "slot", "conversion_value_rule_primary_dimension", "webpage", "week", "year", "sk_ad_network_fine_conversion_value", "sk_ad_network_redistributed_fine_conversion_value", "sk_ad_network_user_type", "sk_ad_network_ad_event_type", "sk_ad_network_source_app", "sk_ad_network_attribution_credit", "sk_ad_network_coarse_conversion_value", "sk_ad_network_source_domain", "sk_ad_network_source_type", "sk_ad_network_postback_sequence_index", "sk_ad_network_version", "asset_interaction_target", "new_versus_returning_customers")
    ACTIVITY_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_CITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_RATING_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_STATE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    AD_DESTINATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_FORMAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    AUCTION_INSIGHT_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CAMPAIGN_ASSOCIATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CLICK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ATTRIBUTION_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_LAG_BUCKET_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_OR_ADJUSTMENT_LAG_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONVERSION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_AIRPORT_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CANTON_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CITY_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_COUNTY_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_DISTRICT_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_METRO_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_MOST_SPECIFIC_LOCATION_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_PROVINCE_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_REGION_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_STATE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_BOOKING_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CHECK_IN_DATE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CHECK_IN_DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CITY_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CLASS_FIELD_NUMBER: _ClassVar[int]
    HOTEL_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    HOTEL_DATE_SELECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_LENGTH_OF_STAY_FIELD_NUMBER: _ClassVar[int]
    HOTEL_RATE_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    HOTEL_RATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_PRICE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    HOTEL_STATE_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_ON_THIS_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTH_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    PARTNER_HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_AGGREGATOR_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_LEVEL1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_LEVEL2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_LEVEL3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_LEVEL4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_LEVEL5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BRAND_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE0_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TITLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L5_FIELD_NUMBER: _ClassVar[int]
    QUARTER_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DESTINATION_CITY_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DESTINATION_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DESTINATION_REGION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ENGINE_RESULTS_PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SUBCATEGORY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_VALUE_RULE_PRIMARY_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_FINE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_REDISTRIBUTED_FINE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_AD_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_SOURCE_APP_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_ATTRIBUTION_CREDIT_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_COARSE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_SOURCE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_POSTBACK_SEQUENCE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SK_AD_NETWORK_VERSION_FIELD_NUMBER: _ClassVar[int]
    ASSET_INTERACTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    NEW_VERSUS_RETURNING_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    activity_account_id: int
    activity_city: str
    activity_country: str
    activity_rating: int
    activity_state: str
    external_activity_id: str
    ad_destination_type: _ad_destination_type_pb2.AdDestinationTypeEnum.AdDestinationType
    ad_format_type: _ad_format_type_pb2.AdFormatTypeEnum.AdFormatType
    ad_network_type: _ad_network_type_pb2.AdNetworkTypeEnum.AdNetworkType
    ad_group: str
    asset_group: str
    auction_insight_domain: str
    budget_campaign_association_status: BudgetCampaignAssociationStatus
    campaign: str
    click_type: _click_type_pb2.ClickTypeEnum.ClickType
    conversion_action: str
    conversion_action_category: _conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory
    conversion_action_name: str
    conversion_adjustment: bool
    conversion_attribution_event_type: _conversion_attribution_event_type_pb2.ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    conversion_lag_bucket: _conversion_lag_bucket_pb2.ConversionLagBucketEnum.ConversionLagBucket
    conversion_or_adjustment_lag_bucket: _conversion_or_adjustment_lag_bucket_pb2.ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
    date: str
    day_of_week: _day_of_week_pb2.DayOfWeekEnum.DayOfWeek
    device: _device_pb2.DeviceEnum.Device
    external_conversion_source: _external_conversion_source_pb2.ExternalConversionSourceEnum.ExternalConversionSource
    geo_target_airport: str
    geo_target_canton: str
    geo_target_city: str
    geo_target_country: str
    geo_target_county: str
    geo_target_district: str
    geo_target_metro: str
    geo_target_most_specific_location: str
    geo_target_postal_code: str
    geo_target_province: str
    geo_target_region: str
    geo_target_state: str
    hotel_booking_window_days: int
    hotel_center_id: int
    hotel_check_in_date: str
    hotel_check_in_day_of_week: _day_of_week_pb2.DayOfWeekEnum.DayOfWeek
    hotel_city: str
    hotel_class: int
    hotel_country: str
    hotel_date_selection_type: _hotel_date_selection_type_pb2.HotelDateSelectionTypeEnum.HotelDateSelectionType
    hotel_length_of_stay: int
    hotel_rate_rule_id: str
    hotel_rate_type: _hotel_rate_type_pb2.HotelRateTypeEnum.HotelRateType
    hotel_price_bucket: _hotel_price_bucket_pb2.HotelPriceBucketEnum.HotelPriceBucket
    hotel_state: str
    hour: int
    interaction_on_this_extension: bool
    keyword: Keyword
    month: str
    month_of_year: _month_of_year_pb2.MonthOfYearEnum.MonthOfYear
    partner_hotel_id: str
    placeholder_type: _placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType
    product_aggregator_id: int
    product_category_level1: str
    product_category_level2: str
    product_category_level3: str
    product_category_level4: str
    product_category_level5: str
    product_brand: str
    product_channel: _product_channel_pb2.ProductChannelEnum.ProductChannel
    product_channel_exclusivity: _product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity
    product_condition: _product_condition_pb2.ProductConditionEnum.ProductCondition
    product_country: str
    product_custom_attribute0: str
    product_custom_attribute1: str
    product_custom_attribute2: str
    product_custom_attribute3: str
    product_custom_attribute4: str
    product_feed_label: str
    product_item_id: str
    product_language: str
    product_merchant_id: int
    product_store_id: str
    product_title: str
    product_type_l1: str
    product_type_l2: str
    product_type_l3: str
    product_type_l4: str
    product_type_l5: str
    quarter: str
    travel_destination_city: str
    travel_destination_country: str
    travel_destination_region: str
    recommendation_type: _recommendation_type_pb2.RecommendationTypeEnum.RecommendationType
    search_engine_results_page_type: _search_engine_results_page_type_pb2.SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    search_subcategory: str
    search_term: str
    search_term_match_type: _search_term_match_type_pb2.SearchTermMatchTypeEnum.SearchTermMatchType
    slot: _slot_pb2.SlotEnum.Slot
    conversion_value_rule_primary_dimension: _conversion_value_rule_primary_dimension_pb2.ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    webpage: str
    week: str
    year: int
    sk_ad_network_fine_conversion_value: int
    sk_ad_network_redistributed_fine_conversion_value: int
    sk_ad_network_user_type: _sk_ad_network_user_type_pb2.SkAdNetworkUserTypeEnum.SkAdNetworkUserType
    sk_ad_network_ad_event_type: _sk_ad_network_ad_event_type_pb2.SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    sk_ad_network_source_app: SkAdNetworkSourceApp
    sk_ad_network_attribution_credit: _sk_ad_network_attribution_credit_pb2.SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    sk_ad_network_coarse_conversion_value: _sk_ad_network_coarse_conversion_value_pb2.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    sk_ad_network_source_domain: str
    sk_ad_network_source_type: _sk_ad_network_source_type_pb2.SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType
    sk_ad_network_postback_sequence_index: int
    sk_ad_network_version: str
    asset_interaction_target: AssetInteractionTarget
    new_versus_returning_customers: _converting_user_prior_engagement_type_and_ltv_bucket_pb2.ConvertingUserPriorEngagementTypeAndLtvBucketEnum.ConvertingUserPriorEngagementTypeAndLtvBucket
    def __init__(self, activity_account_id: _Optional[int] = ..., activity_city: _Optional[str] = ..., activity_country: _Optional[str] = ..., activity_rating: _Optional[int] = ..., activity_state: _Optional[str] = ..., external_activity_id: _Optional[str] = ..., ad_destination_type: _Optional[_Union[_ad_destination_type_pb2.AdDestinationTypeEnum.AdDestinationType, str]] = ..., ad_format_type: _Optional[_Union[_ad_format_type_pb2.AdFormatTypeEnum.AdFormatType, str]] = ..., ad_network_type: _Optional[_Union[_ad_network_type_pb2.AdNetworkTypeEnum.AdNetworkType, str]] = ..., ad_group: _Optional[str] = ..., asset_group: _Optional[str] = ..., auction_insight_domain: _Optional[str] = ..., budget_campaign_association_status: _Optional[_Union[BudgetCampaignAssociationStatus, _Mapping]] = ..., campaign: _Optional[str] = ..., click_type: _Optional[_Union[_click_type_pb2.ClickTypeEnum.ClickType, str]] = ..., conversion_action: _Optional[str] = ..., conversion_action_category: _Optional[_Union[_conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory, str]] = ..., conversion_action_name: _Optional[str] = ..., conversion_adjustment: bool = ..., conversion_attribution_event_type: _Optional[_Union[_conversion_attribution_event_type_pb2.ConversionAttributionEventTypeEnum.ConversionAttributionEventType, str]] = ..., conversion_lag_bucket: _Optional[_Union[_conversion_lag_bucket_pb2.ConversionLagBucketEnum.ConversionLagBucket, str]] = ..., conversion_or_adjustment_lag_bucket: _Optional[_Union[_conversion_or_adjustment_lag_bucket_pb2.ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket, str]] = ..., date: _Optional[str] = ..., day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeekEnum.DayOfWeek, str]] = ..., device: _Optional[_Union[_device_pb2.DeviceEnum.Device, str]] = ..., external_conversion_source: _Optional[_Union[_external_conversion_source_pb2.ExternalConversionSourceEnum.ExternalConversionSource, str]] = ..., geo_target_airport: _Optional[str] = ..., geo_target_canton: _Optional[str] = ..., geo_target_city: _Optional[str] = ..., geo_target_country: _Optional[str] = ..., geo_target_county: _Optional[str] = ..., geo_target_district: _Optional[str] = ..., geo_target_metro: _Optional[str] = ..., geo_target_most_specific_location: _Optional[str] = ..., geo_target_postal_code: _Optional[str] = ..., geo_target_province: _Optional[str] = ..., geo_target_region: _Optional[str] = ..., geo_target_state: _Optional[str] = ..., hotel_booking_window_days: _Optional[int] = ..., hotel_center_id: _Optional[int] = ..., hotel_check_in_date: _Optional[str] = ..., hotel_check_in_day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeekEnum.DayOfWeek, str]] = ..., hotel_city: _Optional[str] = ..., hotel_class: _Optional[int] = ..., hotel_country: _Optional[str] = ..., hotel_date_selection_type: _Optional[_Union[_hotel_date_selection_type_pb2.HotelDateSelectionTypeEnum.HotelDateSelectionType, str]] = ..., hotel_length_of_stay: _Optional[int] = ..., hotel_rate_rule_id: _Optional[str] = ..., hotel_rate_type: _Optional[_Union[_hotel_rate_type_pb2.HotelRateTypeEnum.HotelRateType, str]] = ..., hotel_price_bucket: _Optional[_Union[_hotel_price_bucket_pb2.HotelPriceBucketEnum.HotelPriceBucket, str]] = ..., hotel_state: _Optional[str] = ..., hour: _Optional[int] = ..., interaction_on_this_extension: bool = ..., keyword: _Optional[_Union[Keyword, _Mapping]] = ..., month: _Optional[str] = ..., month_of_year: _Optional[_Union[_month_of_year_pb2.MonthOfYearEnum.MonthOfYear, str]] = ..., partner_hotel_id: _Optional[str] = ..., placeholder_type: _Optional[_Union[_placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType, str]] = ..., product_aggregator_id: _Optional[int] = ..., product_category_level1: _Optional[str] = ..., product_category_level2: _Optional[str] = ..., product_category_level3: _Optional[str] = ..., product_category_level4: _Optional[str] = ..., product_category_level5: _Optional[str] = ..., product_brand: _Optional[str] = ..., product_channel: _Optional[_Union[_product_channel_pb2.ProductChannelEnum.ProductChannel, str]] = ..., product_channel_exclusivity: _Optional[_Union[_product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity, str]] = ..., product_condition: _Optional[_Union[_product_condition_pb2.ProductConditionEnum.ProductCondition, str]] = ..., product_country: _Optional[str] = ..., product_custom_attribute0: _Optional[str] = ..., product_custom_attribute1: _Optional[str] = ..., product_custom_attribute2: _Optional[str] = ..., product_custom_attribute3: _Optional[str] = ..., product_custom_attribute4: _Optional[str] = ..., product_feed_label: _Optional[str] = ..., product_item_id: _Optional[str] = ..., product_language: _Optional[str] = ..., product_merchant_id: _Optional[int] = ..., product_store_id: _Optional[str] = ..., product_title: _Optional[str] = ..., product_type_l1: _Optional[str] = ..., product_type_l2: _Optional[str] = ..., product_type_l3: _Optional[str] = ..., product_type_l4: _Optional[str] = ..., product_type_l5: _Optional[str] = ..., quarter: _Optional[str] = ..., travel_destination_city: _Optional[str] = ..., travel_destination_country: _Optional[str] = ..., travel_destination_region: _Optional[str] = ..., recommendation_type: _Optional[_Union[_recommendation_type_pb2.RecommendationTypeEnum.RecommendationType, str]] = ..., search_engine_results_page_type: _Optional[_Union[_search_engine_results_page_type_pb2.SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType, str]] = ..., search_subcategory: _Optional[str] = ..., search_term: _Optional[str] = ..., search_term_match_type: _Optional[_Union[_search_term_match_type_pb2.SearchTermMatchTypeEnum.SearchTermMatchType, str]] = ..., slot: _Optional[_Union[_slot_pb2.SlotEnum.Slot, str]] = ..., conversion_value_rule_primary_dimension: _Optional[_Union[_conversion_value_rule_primary_dimension_pb2.ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension, str]] = ..., webpage: _Optional[str] = ..., week: _Optional[str] = ..., year: _Optional[int] = ..., sk_ad_network_fine_conversion_value: _Optional[int] = ..., sk_ad_network_redistributed_fine_conversion_value: _Optional[int] = ..., sk_ad_network_user_type: _Optional[_Union[_sk_ad_network_user_type_pb2.SkAdNetworkUserTypeEnum.SkAdNetworkUserType, str]] = ..., sk_ad_network_ad_event_type: _Optional[_Union[_sk_ad_network_ad_event_type_pb2.SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType, str]] = ..., sk_ad_network_source_app: _Optional[_Union[SkAdNetworkSourceApp, _Mapping]] = ..., sk_ad_network_attribution_credit: _Optional[_Union[_sk_ad_network_attribution_credit_pb2.SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit, str]] = ..., sk_ad_network_coarse_conversion_value: _Optional[_Union[_sk_ad_network_coarse_conversion_value_pb2.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue, str]] = ..., sk_ad_network_source_domain: _Optional[str] = ..., sk_ad_network_source_type: _Optional[_Union[_sk_ad_network_source_type_pb2.SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType, str]] = ..., sk_ad_network_postback_sequence_index: _Optional[int] = ..., sk_ad_network_version: _Optional[str] = ..., asset_interaction_target: _Optional[_Union[AssetInteractionTarget, _Mapping]] = ..., new_versus_returning_customers: _Optional[_Union[_converting_user_prior_engagement_type_and_ltv_bucket_pb2.ConvertingUserPriorEngagementTypeAndLtvBucketEnum.ConvertingUserPriorEngagementTypeAndLtvBucket, str]] = ...) -> None: ...

class Keyword(_message.Message):
    __slots__ = ("ad_group_criterion", "info")
    AD_GROUP_CRITERION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    ad_group_criterion: str
    info: _criteria_pb2.KeywordInfo
    def __init__(self, ad_group_criterion: _Optional[str] = ..., info: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ...) -> None: ...

class BudgetCampaignAssociationStatus(_message.Message):
    __slots__ = ("campaign", "status")
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    campaign: str
    status: _budget_campaign_association_status_pb2.BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    def __init__(self, campaign: _Optional[str] = ..., status: _Optional[_Union[_budget_campaign_association_status_pb2.BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus, str]] = ...) -> None: ...

class AssetInteractionTarget(_message.Message):
    __slots__ = ("asset", "interaction_on_this_asset")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_ON_THIS_ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    interaction_on_this_asset: bool
    def __init__(self, asset: _Optional[str] = ..., interaction_on_this_asset: bool = ...) -> None: ...

class SkAdNetworkSourceApp(_message.Message):
    __slots__ = ("sk_ad_network_source_app_id",)
    SK_AD_NETWORK_SOURCE_APP_ID_FIELD_NUMBER: _ClassVar[int]
    sk_ad_network_source_app_id: str
    def __init__(self, sk_ad_network_source_app_id: _Optional[str] = ...) -> None: ...
