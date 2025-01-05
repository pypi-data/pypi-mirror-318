from google.ads.googleads.v18.common import bidding_pb2 as _bidding_pb2
from google.ads.googleads.v18.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v18.common import frequency_cap_pb2 as _frequency_cap_pb2
from google.ads.googleads.v18.common import real_time_bidding_setting_pb2 as _real_time_bidding_setting_pb2
from google.ads.googleads.v18.common import targeting_setting_pb2 as _targeting_setting_pb2
from google.ads.googleads.v18.enums import ad_serving_optimization_status_pb2 as _ad_serving_optimization_status_pb2
from google.ads.googleads.v18.enums import advertising_channel_sub_type_pb2 as _advertising_channel_sub_type_pb2
from google.ads.googleads.v18.enums import advertising_channel_type_pb2 as _advertising_channel_type_pb2
from google.ads.googleads.v18.enums import app_campaign_app_store_pb2 as _app_campaign_app_store_pb2
from google.ads.googleads.v18.enums import app_campaign_bidding_strategy_goal_type_pb2 as _app_campaign_bidding_strategy_goal_type_pb2
from google.ads.googleads.v18.enums import asset_automation_status_pb2 as _asset_automation_status_pb2
from google.ads.googleads.v18.enums import asset_automation_type_pb2 as _asset_automation_type_pb2
from google.ads.googleads.v18.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v18.enums import asset_set_type_pb2 as _asset_set_type_pb2
from google.ads.googleads.v18.enums import bidding_strategy_system_status_pb2 as _bidding_strategy_system_status_pb2
from google.ads.googleads.v18.enums import bidding_strategy_type_pb2 as _bidding_strategy_type_pb2
from google.ads.googleads.v18.enums import brand_safety_suitability_pb2 as _brand_safety_suitability_pb2
from google.ads.googleads.v18.enums import campaign_experiment_type_pb2 as _campaign_experiment_type_pb2
from google.ads.googleads.v18.enums import campaign_keyword_match_type_pb2 as _campaign_keyword_match_type_pb2
from google.ads.googleads.v18.enums import campaign_primary_status_pb2 as _campaign_primary_status_pb2
from google.ads.googleads.v18.enums import campaign_primary_status_reason_pb2 as _campaign_primary_status_reason_pb2
from google.ads.googleads.v18.enums import campaign_serving_status_pb2 as _campaign_serving_status_pb2
from google.ads.googleads.v18.enums import campaign_status_pb2 as _campaign_status_pb2
from google.ads.googleads.v18.enums import listing_type_pb2 as _listing_type_pb2
from google.ads.googleads.v18.enums import location_source_type_pb2 as _location_source_type_pb2
from google.ads.googleads.v18.enums import negative_geo_target_type_pb2 as _negative_geo_target_type_pb2
from google.ads.googleads.v18.enums import optimization_goal_type_pb2 as _optimization_goal_type_pb2
from google.ads.googleads.v18.enums import payment_mode_pb2 as _payment_mode_pb2
from google.ads.googleads.v18.enums import performance_max_upgrade_status_pb2 as _performance_max_upgrade_status_pb2
from google.ads.googleads.v18.enums import positive_geo_target_type_pb2 as _positive_geo_target_type_pb2
from google.ads.googleads.v18.enums import vanity_pharma_display_url_mode_pb2 as _vanity_pharma_display_url_mode_pb2
from google.ads.googleads.v18.enums import vanity_pharma_text_pb2 as _vanity_pharma_text_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Campaign(_message.Message):
    __slots__ = ("resource_name", "id", "name", "primary_status", "primary_status_reasons", "status", "serving_status", "bidding_strategy_system_status", "ad_serving_optimization_status", "advertising_channel_type", "advertising_channel_sub_type", "tracking_url_template", "url_custom_parameters", "local_services_campaign_settings", "travel_campaign_settings", "demand_gen_campaign_settings", "video_campaign_settings", "real_time_bidding_setting", "network_settings", "hotel_setting", "dynamic_search_ads_setting", "shopping_setting", "targeting_setting", "audience_setting", "geo_target_type_setting", "local_campaign_setting", "app_campaign_setting", "labels", "experiment_type", "base_campaign", "campaign_budget", "bidding_strategy_type", "accessible_bidding_strategy", "start_date", "campaign_group", "end_date", "final_url_suffix", "frequency_caps", "video_brand_safety_suitability", "vanity_pharma", "selective_optimization", "optimization_goal_setting", "tracking_setting", "payment_mode", "optimization_score", "excluded_parent_asset_field_types", "excluded_parent_asset_set_types", "url_expansion_opt_out", "performance_max_upgrade", "hotel_property_asset_set", "listing_type", "asset_automation_settings", "keyword_match_type", "brand_guidelines_enabled", "bidding_strategy", "commission", "manual_cpa", "manual_cpc", "manual_cpm", "manual_cpv", "maximize_conversions", "maximize_conversion_value", "target_cpa", "target_impression_share", "target_roas", "target_spend", "percent_cpc", "target_cpm", "fixed_cpm", "target_cpv")
    class PerformanceMaxUpgrade(_message.Message):
        __slots__ = ("performance_max_campaign", "pre_upgrade_campaign", "status")
        PERFORMANCE_MAX_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
        PRE_UPGRADE_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        performance_max_campaign: str
        pre_upgrade_campaign: str
        status: _performance_max_upgrade_status_pb2.PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
        def __init__(self, performance_max_campaign: _Optional[str] = ..., pre_upgrade_campaign: _Optional[str] = ..., status: _Optional[_Union[_performance_max_upgrade_status_pb2.PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus, str]] = ...) -> None: ...
    class NetworkSettings(_message.Message):
        __slots__ = ("target_google_search", "target_search_network", "target_content_network", "target_partner_search_network", "target_youtube", "target_google_tv_network")
        TARGET_GOOGLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
        TARGET_SEARCH_NETWORK_FIELD_NUMBER: _ClassVar[int]
        TARGET_CONTENT_NETWORK_FIELD_NUMBER: _ClassVar[int]
        TARGET_PARTNER_SEARCH_NETWORK_FIELD_NUMBER: _ClassVar[int]
        TARGET_YOUTUBE_FIELD_NUMBER: _ClassVar[int]
        TARGET_GOOGLE_TV_NETWORK_FIELD_NUMBER: _ClassVar[int]
        target_google_search: bool
        target_search_network: bool
        target_content_network: bool
        target_partner_search_network: bool
        target_youtube: bool
        target_google_tv_network: bool
        def __init__(self, target_google_search: bool = ..., target_search_network: bool = ..., target_content_network: bool = ..., target_partner_search_network: bool = ..., target_youtube: bool = ..., target_google_tv_network: bool = ...) -> None: ...
    class HotelSettingInfo(_message.Message):
        __slots__ = ("hotel_center_id",)
        HOTEL_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
        hotel_center_id: int
        def __init__(self, hotel_center_id: _Optional[int] = ...) -> None: ...
    class DynamicSearchAdsSetting(_message.Message):
        __slots__ = ("domain_name", "language_code", "use_supplied_urls_only", "feeds")
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        USE_SUPPLIED_URLS_ONLY_FIELD_NUMBER: _ClassVar[int]
        FEEDS_FIELD_NUMBER: _ClassVar[int]
        domain_name: str
        language_code: str
        use_supplied_urls_only: bool
        feeds: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, domain_name: _Optional[str] = ..., language_code: _Optional[str] = ..., use_supplied_urls_only: bool = ..., feeds: _Optional[_Iterable[str]] = ...) -> None: ...
    class ShoppingSetting(_message.Message):
        __slots__ = ("merchant_id", "feed_label", "campaign_priority", "enable_local", "use_vehicle_inventory", "advertising_partner_ids", "disable_product_feed")
        MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_LOCAL_FIELD_NUMBER: _ClassVar[int]
        USE_VEHICLE_INVENTORY_FIELD_NUMBER: _ClassVar[int]
        ADVERTISING_PARTNER_IDS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_PRODUCT_FEED_FIELD_NUMBER: _ClassVar[int]
        merchant_id: int
        feed_label: str
        campaign_priority: int
        enable_local: bool
        use_vehicle_inventory: bool
        advertising_partner_ids: _containers.RepeatedScalarFieldContainer[int]
        disable_product_feed: bool
        def __init__(self, merchant_id: _Optional[int] = ..., feed_label: _Optional[str] = ..., campaign_priority: _Optional[int] = ..., enable_local: bool = ..., use_vehicle_inventory: bool = ..., advertising_partner_ids: _Optional[_Iterable[int]] = ..., disable_product_feed: bool = ...) -> None: ...
    class TrackingSetting(_message.Message):
        __slots__ = ("tracking_url",)
        TRACKING_URL_FIELD_NUMBER: _ClassVar[int]
        tracking_url: str
        def __init__(self, tracking_url: _Optional[str] = ...) -> None: ...
    class GeoTargetTypeSetting(_message.Message):
        __slots__ = ("positive_geo_target_type", "negative_geo_target_type")
        POSITIVE_GEO_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
        NEGATIVE_GEO_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
        positive_geo_target_type: _positive_geo_target_type_pb2.PositiveGeoTargetTypeEnum.PositiveGeoTargetType
        negative_geo_target_type: _negative_geo_target_type_pb2.NegativeGeoTargetTypeEnum.NegativeGeoTargetType
        def __init__(self, positive_geo_target_type: _Optional[_Union[_positive_geo_target_type_pb2.PositiveGeoTargetTypeEnum.PositiveGeoTargetType, str]] = ..., negative_geo_target_type: _Optional[_Union[_negative_geo_target_type_pb2.NegativeGeoTargetTypeEnum.NegativeGeoTargetType, str]] = ...) -> None: ...
    class LocalCampaignSetting(_message.Message):
        __slots__ = ("location_source_type",)
        LOCATION_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        location_source_type: _location_source_type_pb2.LocationSourceTypeEnum.LocationSourceType
        def __init__(self, location_source_type: _Optional[_Union[_location_source_type_pb2.LocationSourceTypeEnum.LocationSourceType, str]] = ...) -> None: ...
    class AppCampaignSetting(_message.Message):
        __slots__ = ("bidding_strategy_goal_type", "app_id", "app_store")
        BIDDING_STRATEGY_GOAL_TYPE_FIELD_NUMBER: _ClassVar[int]
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        APP_STORE_FIELD_NUMBER: _ClassVar[int]
        bidding_strategy_goal_type: _app_campaign_bidding_strategy_goal_type_pb2.AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
        app_id: str
        app_store: _app_campaign_app_store_pb2.AppCampaignAppStoreEnum.AppCampaignAppStore
        def __init__(self, bidding_strategy_goal_type: _Optional[_Union[_app_campaign_bidding_strategy_goal_type_pb2.AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType, str]] = ..., app_id: _Optional[str] = ..., app_store: _Optional[_Union[_app_campaign_app_store_pb2.AppCampaignAppStoreEnum.AppCampaignAppStore, str]] = ...) -> None: ...
    class VanityPharma(_message.Message):
        __slots__ = ("vanity_pharma_display_url_mode", "vanity_pharma_text")
        VANITY_PHARMA_DISPLAY_URL_MODE_FIELD_NUMBER: _ClassVar[int]
        VANITY_PHARMA_TEXT_FIELD_NUMBER: _ClassVar[int]
        vanity_pharma_display_url_mode: _vanity_pharma_display_url_mode_pb2.VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
        vanity_pharma_text: _vanity_pharma_text_pb2.VanityPharmaTextEnum.VanityPharmaText
        def __init__(self, vanity_pharma_display_url_mode: _Optional[_Union[_vanity_pharma_display_url_mode_pb2.VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode, str]] = ..., vanity_pharma_text: _Optional[_Union[_vanity_pharma_text_pb2.VanityPharmaTextEnum.VanityPharmaText, str]] = ...) -> None: ...
    class SelectiveOptimization(_message.Message):
        __slots__ = ("conversion_actions",)
        CONVERSION_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        conversion_actions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, conversion_actions: _Optional[_Iterable[str]] = ...) -> None: ...
    class OptimizationGoalSetting(_message.Message):
        __slots__ = ("optimization_goal_types",)
        OPTIMIZATION_GOAL_TYPES_FIELD_NUMBER: _ClassVar[int]
        optimization_goal_types: _containers.RepeatedScalarFieldContainer[_optimization_goal_type_pb2.OptimizationGoalTypeEnum.OptimizationGoalType]
        def __init__(self, optimization_goal_types: _Optional[_Iterable[_Union[_optimization_goal_type_pb2.OptimizationGoalTypeEnum.OptimizationGoalType, str]]] = ...) -> None: ...
    class AudienceSetting(_message.Message):
        __slots__ = ("use_audience_grouped",)
        USE_AUDIENCE_GROUPED_FIELD_NUMBER: _ClassVar[int]
        use_audience_grouped: bool
        def __init__(self, use_audience_grouped: bool = ...) -> None: ...
    class LocalServicesCampaignSettings(_message.Message):
        __slots__ = ("category_bids",)
        CATEGORY_BIDS_FIELD_NUMBER: _ClassVar[int]
        category_bids: _containers.RepeatedCompositeFieldContainer[Campaign.CategoryBid]
        def __init__(self, category_bids: _Optional[_Iterable[_Union[Campaign.CategoryBid, _Mapping]]] = ...) -> None: ...
    class CategoryBid(_message.Message):
        __slots__ = ("category_id", "manual_cpa_bid_micros", "target_cpa_bid_micros")
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        MANUAL_CPA_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
        TARGET_CPA_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
        category_id: str
        manual_cpa_bid_micros: int
        target_cpa_bid_micros: int
        def __init__(self, category_id: _Optional[str] = ..., manual_cpa_bid_micros: _Optional[int] = ..., target_cpa_bid_micros: _Optional[int] = ...) -> None: ...
    class TravelCampaignSettings(_message.Message):
        __slots__ = ("travel_account_id",)
        TRAVEL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        travel_account_id: int
        def __init__(self, travel_account_id: _Optional[int] = ...) -> None: ...
    class DemandGenCampaignSettings(_message.Message):
        __slots__ = ("upgraded_targeting",)
        UPGRADED_TARGETING_FIELD_NUMBER: _ClassVar[int]
        upgraded_targeting: bool
        def __init__(self, upgraded_targeting: bool = ...) -> None: ...
    class VideoCampaignSettings(_message.Message):
        __slots__ = ("video_ad_inventory_control",)
        class VideoAdInventoryControl(_message.Message):
            __slots__ = ("allow_in_stream", "allow_in_feed", "allow_shorts")
            ALLOW_IN_STREAM_FIELD_NUMBER: _ClassVar[int]
            ALLOW_IN_FEED_FIELD_NUMBER: _ClassVar[int]
            ALLOW_SHORTS_FIELD_NUMBER: _ClassVar[int]
            allow_in_stream: bool
            allow_in_feed: bool
            allow_shorts: bool
            def __init__(self, allow_in_stream: bool = ..., allow_in_feed: bool = ..., allow_shorts: bool = ...) -> None: ...
        VIDEO_AD_INVENTORY_CONTROL_FIELD_NUMBER: _ClassVar[int]
        video_ad_inventory_control: Campaign.VideoCampaignSettings.VideoAdInventoryControl
        def __init__(self, video_ad_inventory_control: _Optional[_Union[Campaign.VideoCampaignSettings.VideoAdInventoryControl, _Mapping]] = ...) -> None: ...
    class AssetAutomationSetting(_message.Message):
        __slots__ = ("asset_automation_type", "asset_automation_status")
        ASSET_AUTOMATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        ASSET_AUTOMATION_STATUS_FIELD_NUMBER: _ClassVar[int]
        asset_automation_type: _asset_automation_type_pb2.AssetAutomationTypeEnum.AssetAutomationType
        asset_automation_status: _asset_automation_status_pb2.AssetAutomationStatusEnum.AssetAutomationStatus
        def __init__(self, asset_automation_type: _Optional[_Union[_asset_automation_type_pb2.AssetAutomationTypeEnum.AssetAutomationType, str]] = ..., asset_automation_status: _Optional[_Union[_asset_automation_status_pb2.AssetAutomationStatusEnum.AssetAutomationStatus, str]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_REASONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVING_STATUS_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_SYSTEM_STATUS_FIELD_NUMBER: _ClassVar[int]
    AD_SERVING_OPTIMIZATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SERVICES_CAMPAIGN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_CAMPAIGN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEMAND_GEN_CAMPAIGN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CAMPAIGN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REAL_TIME_BIDDING_SETTING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    HOTEL_SETTING_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_SEARCH_ADS_SETTING_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_SETTING_FIELD_NUMBER: _ClassVar[int]
    TARGETING_SETTING_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_SETTING_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_TYPE_SETTING_FIELD_NUMBER: _ClassVar[int]
    LOCAL_CAMPAIGN_SETTING_FIELD_NUMBER: _ClassVar[int]
    APP_CAMPAIGN_SETTING_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBLE_BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_GROUP_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_CAPS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_BRAND_SAFETY_SUITABILITY_FIELD_NUMBER: _ClassVar[int]
    VANITY_PHARMA_FIELD_NUMBER: _ClassVar[int]
    SELECTIVE_OPTIMIZATION_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_GOAL_SETTING_FIELD_NUMBER: _ClassVar[int]
    TRACKING_SETTING_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_SCORE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PARENT_ASSET_FIELD_TYPES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PARENT_ASSET_SET_TYPES_FIELD_NUMBER: _ClassVar[int]
    URL_EXPANSION_OPT_OUT_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_MAX_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_PROPERTY_ASSET_SET_FIELD_NUMBER: _ClassVar[int]
    LISTING_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_AUTOMATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    BRAND_GUIDELINES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CPA_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CPC_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CPM_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CPV_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
    TARGET_IMPRESSION_SHARE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SPEND_FIELD_NUMBER: _ClassVar[int]
    PERCENT_CPC_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPM_FIELD_NUMBER: _ClassVar[int]
    FIXED_CPM_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPV_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    primary_status: _campaign_primary_status_pb2.CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    primary_status_reasons: _containers.RepeatedScalarFieldContainer[_campaign_primary_status_reason_pb2.CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
    status: _campaign_status_pb2.CampaignStatusEnum.CampaignStatus
    serving_status: _campaign_serving_status_pb2.CampaignServingStatusEnum.CampaignServingStatus
    bidding_strategy_system_status: _bidding_strategy_system_status_pb2.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    ad_serving_optimization_status: _ad_serving_optimization_status_pb2.AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    advertising_channel_type: _advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType
    advertising_channel_sub_type: _advertising_channel_sub_type_pb2.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    local_services_campaign_settings: Campaign.LocalServicesCampaignSettings
    travel_campaign_settings: Campaign.TravelCampaignSettings
    demand_gen_campaign_settings: Campaign.DemandGenCampaignSettings
    video_campaign_settings: Campaign.VideoCampaignSettings
    real_time_bidding_setting: _real_time_bidding_setting_pb2.RealTimeBiddingSetting
    network_settings: Campaign.NetworkSettings
    hotel_setting: Campaign.HotelSettingInfo
    dynamic_search_ads_setting: Campaign.DynamicSearchAdsSetting
    shopping_setting: Campaign.ShoppingSetting
    targeting_setting: _targeting_setting_pb2.TargetingSetting
    audience_setting: Campaign.AudienceSetting
    geo_target_type_setting: Campaign.GeoTargetTypeSetting
    local_campaign_setting: Campaign.LocalCampaignSetting
    app_campaign_setting: Campaign.AppCampaignSetting
    labels: _containers.RepeatedScalarFieldContainer[str]
    experiment_type: _campaign_experiment_type_pb2.CampaignExperimentTypeEnum.CampaignExperimentType
    base_campaign: str
    campaign_budget: str
    bidding_strategy_type: _bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType
    accessible_bidding_strategy: str
    start_date: str
    campaign_group: str
    end_date: str
    final_url_suffix: str
    frequency_caps: _containers.RepeatedCompositeFieldContainer[_frequency_cap_pb2.FrequencyCapEntry]
    video_brand_safety_suitability: _brand_safety_suitability_pb2.BrandSafetySuitabilityEnum.BrandSafetySuitability
    vanity_pharma: Campaign.VanityPharma
    selective_optimization: Campaign.SelectiveOptimization
    optimization_goal_setting: Campaign.OptimizationGoalSetting
    tracking_setting: Campaign.TrackingSetting
    payment_mode: _payment_mode_pb2.PaymentModeEnum.PaymentMode
    optimization_score: float
    excluded_parent_asset_field_types: _containers.RepeatedScalarFieldContainer[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType]
    excluded_parent_asset_set_types: _containers.RepeatedScalarFieldContainer[_asset_set_type_pb2.AssetSetTypeEnum.AssetSetType]
    url_expansion_opt_out: bool
    performance_max_upgrade: Campaign.PerformanceMaxUpgrade
    hotel_property_asset_set: str
    listing_type: _listing_type_pb2.ListingTypeEnum.ListingType
    asset_automation_settings: _containers.RepeatedCompositeFieldContainer[Campaign.AssetAutomationSetting]
    keyword_match_type: _campaign_keyword_match_type_pb2.CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType
    brand_guidelines_enabled: bool
    bidding_strategy: str
    commission: _bidding_pb2.Commission
    manual_cpa: _bidding_pb2.ManualCpa
    manual_cpc: _bidding_pb2.ManualCpc
    manual_cpm: _bidding_pb2.ManualCpm
    manual_cpv: _bidding_pb2.ManualCpv
    maximize_conversions: _bidding_pb2.MaximizeConversions
    maximize_conversion_value: _bidding_pb2.MaximizeConversionValue
    target_cpa: _bidding_pb2.TargetCpa
    target_impression_share: _bidding_pb2.TargetImpressionShare
    target_roas: _bidding_pb2.TargetRoas
    target_spend: _bidding_pb2.TargetSpend
    percent_cpc: _bidding_pb2.PercentCpc
    target_cpm: _bidding_pb2.TargetCpm
    fixed_cpm: _bidding_pb2.FixedCpm
    target_cpv: _bidding_pb2.TargetCpv
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., primary_status: _Optional[_Union[_campaign_primary_status_pb2.CampaignPrimaryStatusEnum.CampaignPrimaryStatus, str]] = ..., primary_status_reasons: _Optional[_Iterable[_Union[_campaign_primary_status_reason_pb2.CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason, str]]] = ..., status: _Optional[_Union[_campaign_status_pb2.CampaignStatusEnum.CampaignStatus, str]] = ..., serving_status: _Optional[_Union[_campaign_serving_status_pb2.CampaignServingStatusEnum.CampaignServingStatus, str]] = ..., bidding_strategy_system_status: _Optional[_Union[_bidding_strategy_system_status_pb2.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus, str]] = ..., ad_serving_optimization_status: _Optional[_Union[_ad_serving_optimization_status_pb2.AdServingOptimizationStatusEnum.AdServingOptimizationStatus, str]] = ..., advertising_channel_type: _Optional[_Union[_advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType, str]] = ..., advertising_channel_sub_type: _Optional[_Union[_advertising_channel_sub_type_pb2.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType, str]] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., local_services_campaign_settings: _Optional[_Union[Campaign.LocalServicesCampaignSettings, _Mapping]] = ..., travel_campaign_settings: _Optional[_Union[Campaign.TravelCampaignSettings, _Mapping]] = ..., demand_gen_campaign_settings: _Optional[_Union[Campaign.DemandGenCampaignSettings, _Mapping]] = ..., video_campaign_settings: _Optional[_Union[Campaign.VideoCampaignSettings, _Mapping]] = ..., real_time_bidding_setting: _Optional[_Union[_real_time_bidding_setting_pb2.RealTimeBiddingSetting, _Mapping]] = ..., network_settings: _Optional[_Union[Campaign.NetworkSettings, _Mapping]] = ..., hotel_setting: _Optional[_Union[Campaign.HotelSettingInfo, _Mapping]] = ..., dynamic_search_ads_setting: _Optional[_Union[Campaign.DynamicSearchAdsSetting, _Mapping]] = ..., shopping_setting: _Optional[_Union[Campaign.ShoppingSetting, _Mapping]] = ..., targeting_setting: _Optional[_Union[_targeting_setting_pb2.TargetingSetting, _Mapping]] = ..., audience_setting: _Optional[_Union[Campaign.AudienceSetting, _Mapping]] = ..., geo_target_type_setting: _Optional[_Union[Campaign.GeoTargetTypeSetting, _Mapping]] = ..., local_campaign_setting: _Optional[_Union[Campaign.LocalCampaignSetting, _Mapping]] = ..., app_campaign_setting: _Optional[_Union[Campaign.AppCampaignSetting, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ..., experiment_type: _Optional[_Union[_campaign_experiment_type_pb2.CampaignExperimentTypeEnum.CampaignExperimentType, str]] = ..., base_campaign: _Optional[str] = ..., campaign_budget: _Optional[str] = ..., bidding_strategy_type: _Optional[_Union[_bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType, str]] = ..., accessible_bidding_strategy: _Optional[str] = ..., start_date: _Optional[str] = ..., campaign_group: _Optional[str] = ..., end_date: _Optional[str] = ..., final_url_suffix: _Optional[str] = ..., frequency_caps: _Optional[_Iterable[_Union[_frequency_cap_pb2.FrequencyCapEntry, _Mapping]]] = ..., video_brand_safety_suitability: _Optional[_Union[_brand_safety_suitability_pb2.BrandSafetySuitabilityEnum.BrandSafetySuitability, str]] = ..., vanity_pharma: _Optional[_Union[Campaign.VanityPharma, _Mapping]] = ..., selective_optimization: _Optional[_Union[Campaign.SelectiveOptimization, _Mapping]] = ..., optimization_goal_setting: _Optional[_Union[Campaign.OptimizationGoalSetting, _Mapping]] = ..., tracking_setting: _Optional[_Union[Campaign.TrackingSetting, _Mapping]] = ..., payment_mode: _Optional[_Union[_payment_mode_pb2.PaymentModeEnum.PaymentMode, str]] = ..., optimization_score: _Optional[float] = ..., excluded_parent_asset_field_types: _Optional[_Iterable[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]] = ..., excluded_parent_asset_set_types: _Optional[_Iterable[_Union[_asset_set_type_pb2.AssetSetTypeEnum.AssetSetType, str]]] = ..., url_expansion_opt_out: bool = ..., performance_max_upgrade: _Optional[_Union[Campaign.PerformanceMaxUpgrade, _Mapping]] = ..., hotel_property_asset_set: _Optional[str] = ..., listing_type: _Optional[_Union[_listing_type_pb2.ListingTypeEnum.ListingType, str]] = ..., asset_automation_settings: _Optional[_Iterable[_Union[Campaign.AssetAutomationSetting, _Mapping]]] = ..., keyword_match_type: _Optional[_Union[_campaign_keyword_match_type_pb2.CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType, str]] = ..., brand_guidelines_enabled: bool = ..., bidding_strategy: _Optional[str] = ..., commission: _Optional[_Union[_bidding_pb2.Commission, _Mapping]] = ..., manual_cpa: _Optional[_Union[_bidding_pb2.ManualCpa, _Mapping]] = ..., manual_cpc: _Optional[_Union[_bidding_pb2.ManualCpc, _Mapping]] = ..., manual_cpm: _Optional[_Union[_bidding_pb2.ManualCpm, _Mapping]] = ..., manual_cpv: _Optional[_Union[_bidding_pb2.ManualCpv, _Mapping]] = ..., maximize_conversions: _Optional[_Union[_bidding_pb2.MaximizeConversions, _Mapping]] = ..., maximize_conversion_value: _Optional[_Union[_bidding_pb2.MaximizeConversionValue, _Mapping]] = ..., target_cpa: _Optional[_Union[_bidding_pb2.TargetCpa, _Mapping]] = ..., target_impression_share: _Optional[_Union[_bidding_pb2.TargetImpressionShare, _Mapping]] = ..., target_roas: _Optional[_Union[_bidding_pb2.TargetRoas, _Mapping]] = ..., target_spend: _Optional[_Union[_bidding_pb2.TargetSpend, _Mapping]] = ..., percent_cpc: _Optional[_Union[_bidding_pb2.PercentCpc, _Mapping]] = ..., target_cpm: _Optional[_Union[_bidding_pb2.TargetCpm, _Mapping]] = ..., fixed_cpm: _Optional[_Union[_bidding_pb2.FixedCpm, _Mapping]] = ..., target_cpv: _Optional[_Union[_bidding_pb2.TargetCpv, _Mapping]] = ...) -> None: ...
