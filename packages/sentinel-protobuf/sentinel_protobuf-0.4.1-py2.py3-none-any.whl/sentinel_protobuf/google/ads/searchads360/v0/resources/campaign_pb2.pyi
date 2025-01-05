from google.ads.searchads360.v0.common import bidding_pb2 as _bidding_pb2
from google.ads.searchads360.v0.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.searchads360.v0.common import frequency_cap_pb2 as _frequency_cap_pb2
from google.ads.searchads360.v0.common import real_time_bidding_setting_pb2 as _real_time_bidding_setting_pb2
from google.ads.searchads360.v0.enums import ad_serving_optimization_status_pb2 as _ad_serving_optimization_status_pb2
from google.ads.searchads360.v0.enums import advertising_channel_sub_type_pb2 as _advertising_channel_sub_type_pb2
from google.ads.searchads360.v0.enums import advertising_channel_type_pb2 as _advertising_channel_type_pb2
from google.ads.searchads360.v0.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.searchads360.v0.enums import bidding_strategy_system_status_pb2 as _bidding_strategy_system_status_pb2
from google.ads.searchads360.v0.enums import bidding_strategy_type_pb2 as _bidding_strategy_type_pb2
from google.ads.searchads360.v0.enums import campaign_serving_status_pb2 as _campaign_serving_status_pb2
from google.ads.searchads360.v0.enums import campaign_status_pb2 as _campaign_status_pb2
from google.ads.searchads360.v0.enums import negative_geo_target_type_pb2 as _negative_geo_target_type_pb2
from google.ads.searchads360.v0.enums import optimization_goal_type_pb2 as _optimization_goal_type_pb2
from google.ads.searchads360.v0.enums import positive_geo_target_type_pb2 as _positive_geo_target_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Campaign(_message.Message):
    __slots__ = ("resource_name", "id", "name", "status", "serving_status", "bidding_strategy_system_status", "ad_serving_optimization_status", "advertising_channel_type", "advertising_channel_sub_type", "tracking_url_template", "url_custom_parameters", "real_time_bidding_setting", "network_settings", "dynamic_search_ads_setting", "shopping_setting", "geo_target_type_setting", "effective_labels", "labels", "campaign_budget", "bidding_strategy_type", "accessible_bidding_strategy", "start_date", "end_date", "final_url_suffix", "frequency_caps", "selective_optimization", "optimization_goal_setting", "tracking_setting", "engine_id", "excluded_parent_asset_field_types", "create_time", "creation_time", "last_modified_time", "url_expansion_opt_out", "bidding_strategy", "manual_cpa", "manual_cpc", "manual_cpm", "maximize_conversions", "maximize_conversion_value", "target_cpa", "target_impression_share", "target_roas", "target_spend", "percent_cpc", "target_cpm")
    class NetworkSettings(_message.Message):
        __slots__ = ("target_google_search", "target_search_network", "target_content_network", "target_partner_search_network")
        TARGET_GOOGLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
        TARGET_SEARCH_NETWORK_FIELD_NUMBER: _ClassVar[int]
        TARGET_CONTENT_NETWORK_FIELD_NUMBER: _ClassVar[int]
        TARGET_PARTNER_SEARCH_NETWORK_FIELD_NUMBER: _ClassVar[int]
        target_google_search: bool
        target_search_network: bool
        target_content_network: bool
        target_partner_search_network: bool
        def __init__(self, target_google_search: bool = ..., target_search_network: bool = ..., target_content_network: bool = ..., target_partner_search_network: bool = ...) -> None: ...
    class DynamicSearchAdsSetting(_message.Message):
        __slots__ = ("domain_name", "language_code", "use_supplied_urls_only")
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        USE_SUPPLIED_URLS_ONLY_FIELD_NUMBER: _ClassVar[int]
        domain_name: str
        language_code: str
        use_supplied_urls_only: bool
        def __init__(self, domain_name: _Optional[str] = ..., language_code: _Optional[str] = ..., use_supplied_urls_only: bool = ...) -> None: ...
    class ShoppingSetting(_message.Message):
        __slots__ = ("merchant_id", "sales_country", "feed_label", "campaign_priority", "enable_local", "use_vehicle_inventory")
        MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
        SALES_COUNTRY_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_LOCAL_FIELD_NUMBER: _ClassVar[int]
        USE_VEHICLE_INVENTORY_FIELD_NUMBER: _ClassVar[int]
        merchant_id: int
        sales_country: str
        feed_label: str
        campaign_priority: int
        enable_local: bool
        use_vehicle_inventory: bool
        def __init__(self, merchant_id: _Optional[int] = ..., sales_country: _Optional[str] = ..., feed_label: _Optional[str] = ..., campaign_priority: _Optional[int] = ..., enable_local: bool = ..., use_vehicle_inventory: bool = ...) -> None: ...
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
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVING_STATUS_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_SYSTEM_STATUS_FIELD_NUMBER: _ClassVar[int]
    AD_SERVING_OPTIMIZATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REAL_TIME_BIDDING_SETTING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_SEARCH_ADS_SETTING_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_SETTING_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_TYPE_SETTING_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_LABELS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBLE_BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_CAPS_FIELD_NUMBER: _ClassVar[int]
    SELECTIVE_OPTIMIZATION_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_GOAL_SETTING_FIELD_NUMBER: _ClassVar[int]
    TRACKING_SETTING_FIELD_NUMBER: _ClassVar[int]
    ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PARENT_ASSET_FIELD_TYPES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    URL_EXPANSION_OPT_OUT_FIELD_NUMBER: _ClassVar[int]
    BIDDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CPA_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CPC_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CPM_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
    TARGET_IMPRESSION_SHARE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SPEND_FIELD_NUMBER: _ClassVar[int]
    PERCENT_CPC_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPM_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    status: _campaign_status_pb2.CampaignStatusEnum.CampaignStatus
    serving_status: _campaign_serving_status_pb2.CampaignServingStatusEnum.CampaignServingStatus
    bidding_strategy_system_status: _bidding_strategy_system_status_pb2.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    ad_serving_optimization_status: _ad_serving_optimization_status_pb2.AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    advertising_channel_type: _advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType
    advertising_channel_sub_type: _advertising_channel_sub_type_pb2.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    real_time_bidding_setting: _real_time_bidding_setting_pb2.RealTimeBiddingSetting
    network_settings: Campaign.NetworkSettings
    dynamic_search_ads_setting: Campaign.DynamicSearchAdsSetting
    shopping_setting: Campaign.ShoppingSetting
    geo_target_type_setting: Campaign.GeoTargetTypeSetting
    effective_labels: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.RepeatedScalarFieldContainer[str]
    campaign_budget: str
    bidding_strategy_type: _bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType
    accessible_bidding_strategy: str
    start_date: str
    end_date: str
    final_url_suffix: str
    frequency_caps: _containers.RepeatedCompositeFieldContainer[_frequency_cap_pb2.FrequencyCapEntry]
    selective_optimization: Campaign.SelectiveOptimization
    optimization_goal_setting: Campaign.OptimizationGoalSetting
    tracking_setting: Campaign.TrackingSetting
    engine_id: str
    excluded_parent_asset_field_types: _containers.RepeatedScalarFieldContainer[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType]
    create_time: str
    creation_time: str
    last_modified_time: str
    url_expansion_opt_out: bool
    bidding_strategy: str
    manual_cpa: _bidding_pb2.ManualCpa
    manual_cpc: _bidding_pb2.ManualCpc
    manual_cpm: _bidding_pb2.ManualCpm
    maximize_conversions: _bidding_pb2.MaximizeConversions
    maximize_conversion_value: _bidding_pb2.MaximizeConversionValue
    target_cpa: _bidding_pb2.TargetCpa
    target_impression_share: _bidding_pb2.TargetImpressionShare
    target_roas: _bidding_pb2.TargetRoas
    target_spend: _bidding_pb2.TargetSpend
    percent_cpc: _bidding_pb2.PercentCpc
    target_cpm: _bidding_pb2.TargetCpm
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_campaign_status_pb2.CampaignStatusEnum.CampaignStatus, str]] = ..., serving_status: _Optional[_Union[_campaign_serving_status_pb2.CampaignServingStatusEnum.CampaignServingStatus, str]] = ..., bidding_strategy_system_status: _Optional[_Union[_bidding_strategy_system_status_pb2.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus, str]] = ..., ad_serving_optimization_status: _Optional[_Union[_ad_serving_optimization_status_pb2.AdServingOptimizationStatusEnum.AdServingOptimizationStatus, str]] = ..., advertising_channel_type: _Optional[_Union[_advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType, str]] = ..., advertising_channel_sub_type: _Optional[_Union[_advertising_channel_sub_type_pb2.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType, str]] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., real_time_bidding_setting: _Optional[_Union[_real_time_bidding_setting_pb2.RealTimeBiddingSetting, _Mapping]] = ..., network_settings: _Optional[_Union[Campaign.NetworkSettings, _Mapping]] = ..., dynamic_search_ads_setting: _Optional[_Union[Campaign.DynamicSearchAdsSetting, _Mapping]] = ..., shopping_setting: _Optional[_Union[Campaign.ShoppingSetting, _Mapping]] = ..., geo_target_type_setting: _Optional[_Union[Campaign.GeoTargetTypeSetting, _Mapping]] = ..., effective_labels: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[str]] = ..., campaign_budget: _Optional[str] = ..., bidding_strategy_type: _Optional[_Union[_bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType, str]] = ..., accessible_bidding_strategy: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., final_url_suffix: _Optional[str] = ..., frequency_caps: _Optional[_Iterable[_Union[_frequency_cap_pb2.FrequencyCapEntry, _Mapping]]] = ..., selective_optimization: _Optional[_Union[Campaign.SelectiveOptimization, _Mapping]] = ..., optimization_goal_setting: _Optional[_Union[Campaign.OptimizationGoalSetting, _Mapping]] = ..., tracking_setting: _Optional[_Union[Campaign.TrackingSetting, _Mapping]] = ..., engine_id: _Optional[str] = ..., excluded_parent_asset_field_types: _Optional[_Iterable[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]] = ..., create_time: _Optional[str] = ..., creation_time: _Optional[str] = ..., last_modified_time: _Optional[str] = ..., url_expansion_opt_out: bool = ..., bidding_strategy: _Optional[str] = ..., manual_cpa: _Optional[_Union[_bidding_pb2.ManualCpa, _Mapping]] = ..., manual_cpc: _Optional[_Union[_bidding_pb2.ManualCpc, _Mapping]] = ..., manual_cpm: _Optional[_Union[_bidding_pb2.ManualCpm, _Mapping]] = ..., maximize_conversions: _Optional[_Union[_bidding_pb2.MaximizeConversions, _Mapping]] = ..., maximize_conversion_value: _Optional[_Union[_bidding_pb2.MaximizeConversionValue, _Mapping]] = ..., target_cpa: _Optional[_Union[_bidding_pb2.TargetCpa, _Mapping]] = ..., target_impression_share: _Optional[_Union[_bidding_pb2.TargetImpressionShare, _Mapping]] = ..., target_roas: _Optional[_Union[_bidding_pb2.TargetRoas, _Mapping]] = ..., target_spend: _Optional[_Union[_bidding_pb2.TargetSpend, _Mapping]] = ..., percent_cpc: _Optional[_Union[_bidding_pb2.PercentCpc, _Mapping]] = ..., target_cpm: _Optional[_Union[_bidding_pb2.TargetCpm, _Mapping]] = ...) -> None: ...
