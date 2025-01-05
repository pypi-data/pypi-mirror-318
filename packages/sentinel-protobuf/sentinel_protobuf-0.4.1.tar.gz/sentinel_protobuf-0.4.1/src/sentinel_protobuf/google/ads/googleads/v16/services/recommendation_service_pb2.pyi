from google.ads.googleads.v16.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v16.common import extensions_pb2 as _extensions_pb2
from google.ads.googleads.v16.enums import ad_group_type_pb2 as _ad_group_type_pb2
from google.ads.googleads.v16.enums import advertising_channel_type_pb2 as _advertising_channel_type_pb2
from google.ads.googleads.v16.enums import bidding_strategy_type_pb2 as _bidding_strategy_type_pb2
from google.ads.googleads.v16.enums import conversion_tracking_status_enum_pb2 as _conversion_tracking_status_enum_pb2
from google.ads.googleads.v16.enums import keyword_match_type_pb2 as _keyword_match_type_pb2
from google.ads.googleads.v16.enums import recommendation_type_pb2 as _recommendation_type_pb2
from google.ads.googleads.v16.resources import ad_pb2 as _ad_pb2
from google.ads.googleads.v16.resources import asset_pb2 as _asset_pb2
from google.ads.googleads.v16.resources import recommendation_pb2 as _recommendation_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyRecommendationRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[ApplyRecommendationOperation]
    partial_failure: bool
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[ApplyRecommendationOperation, _Mapping]]] = ..., partial_failure: bool = ...) -> None: ...

class ApplyRecommendationOperation(_message.Message):
    __slots__ = ("resource_name", "campaign_budget", "text_ad", "keyword", "target_cpa_opt_in", "target_roas_opt_in", "callout_extension", "call_extension", "sitelink_extension", "move_unused_budget", "responsive_search_ad", "use_broad_match_keyword", "responsive_search_ad_asset", "responsive_search_ad_improve_ad_strength", "raise_target_cpa_bid_too_low", "forecasting_set_target_roas", "callout_asset", "call_asset", "sitelink_asset", "raise_target_cpa", "lower_target_roas", "forecasting_set_target_cpa", "set_target_cpa", "set_target_roas", "lead_form_asset")
    class CampaignBudgetParameters(_message.Message):
        __slots__ = ("new_budget_amount_micros",)
        NEW_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        new_budget_amount_micros: int
        def __init__(self, new_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class ForecastingSetTargetRoasParameters(_message.Message):
        __slots__ = ("target_roas", "campaign_budget_amount_micros")
        TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        target_roas: float
        campaign_budget_amount_micros: int
        def __init__(self, target_roas: _Optional[float] = ..., campaign_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class TextAdParameters(_message.Message):
        __slots__ = ("ad",)
        AD_FIELD_NUMBER: _ClassVar[int]
        ad: _ad_pb2.Ad
        def __init__(self, ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ...) -> None: ...
    class KeywordParameters(_message.Message):
        __slots__ = ("ad_group", "match_type", "cpc_bid_micros")
        AD_GROUP_FIELD_NUMBER: _ClassVar[int]
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
        ad_group: str
        match_type: _keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType
        cpc_bid_micros: int
        def __init__(self, ad_group: _Optional[str] = ..., match_type: _Optional[_Union[_keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType, str]] = ..., cpc_bid_micros: _Optional[int] = ...) -> None: ...
    class TargetCpaOptInParameters(_message.Message):
        __slots__ = ("target_cpa_micros", "new_campaign_budget_amount_micros")
        TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        NEW_CAMPAIGN_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        target_cpa_micros: int
        new_campaign_budget_amount_micros: int
        def __init__(self, target_cpa_micros: _Optional[int] = ..., new_campaign_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class TargetRoasOptInParameters(_message.Message):
        __slots__ = ("target_roas", "new_campaign_budget_amount_micros")
        TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
        NEW_CAMPAIGN_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        target_roas: float
        new_campaign_budget_amount_micros: int
        def __init__(self, target_roas: _Optional[float] = ..., new_campaign_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class CalloutExtensionParameters(_message.Message):
        __slots__ = ("callout_extensions",)
        CALLOUT_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
        callout_extensions: _containers.RepeatedCompositeFieldContainer[_extensions_pb2.CalloutFeedItem]
        def __init__(self, callout_extensions: _Optional[_Iterable[_Union[_extensions_pb2.CalloutFeedItem, _Mapping]]] = ...) -> None: ...
    class CallExtensionParameters(_message.Message):
        __slots__ = ("call_extensions",)
        CALL_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
        call_extensions: _containers.RepeatedCompositeFieldContainer[_extensions_pb2.CallFeedItem]
        def __init__(self, call_extensions: _Optional[_Iterable[_Union[_extensions_pb2.CallFeedItem, _Mapping]]] = ...) -> None: ...
    class SitelinkExtensionParameters(_message.Message):
        __slots__ = ("sitelink_extensions",)
        SITELINK_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
        sitelink_extensions: _containers.RepeatedCompositeFieldContainer[_extensions_pb2.SitelinkFeedItem]
        def __init__(self, sitelink_extensions: _Optional[_Iterable[_Union[_extensions_pb2.SitelinkFeedItem, _Mapping]]] = ...) -> None: ...
    class CalloutAssetParameters(_message.Message):
        __slots__ = ("ad_asset_apply_parameters",)
        AD_ASSET_APPLY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(self, ad_asset_apply_parameters: _Optional[_Union[ApplyRecommendationOperation.AdAssetApplyParameters, _Mapping]] = ...) -> None: ...
    class CallAssetParameters(_message.Message):
        __slots__ = ("ad_asset_apply_parameters",)
        AD_ASSET_APPLY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(self, ad_asset_apply_parameters: _Optional[_Union[ApplyRecommendationOperation.AdAssetApplyParameters, _Mapping]] = ...) -> None: ...
    class SitelinkAssetParameters(_message.Message):
        __slots__ = ("ad_asset_apply_parameters",)
        AD_ASSET_APPLY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(self, ad_asset_apply_parameters: _Optional[_Union[ApplyRecommendationOperation.AdAssetApplyParameters, _Mapping]] = ...) -> None: ...
    class RaiseTargetCpaParameters(_message.Message):
        __slots__ = ("target_cpa_multiplier",)
        TARGET_CPA_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        target_cpa_multiplier: float
        def __init__(self, target_cpa_multiplier: _Optional[float] = ...) -> None: ...
    class LowerTargetRoasParameters(_message.Message):
        __slots__ = ("target_roas_multiplier",)
        TARGET_ROAS_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        target_roas_multiplier: float
        def __init__(self, target_roas_multiplier: _Optional[float] = ...) -> None: ...
    class AdAssetApplyParameters(_message.Message):
        __slots__ = ("new_assets", "existing_assets", "scope")
        class ApplyScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope]
            UNKNOWN: _ClassVar[ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope]
            CUSTOMER: _ClassVar[ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope]
            CAMPAIGN: _ClassVar[ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope]
        UNSPECIFIED: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope
        UNKNOWN: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope
        CUSTOMER: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope
        CAMPAIGN: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope
        NEW_ASSETS_FIELD_NUMBER: _ClassVar[int]
        EXISTING_ASSETS_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        new_assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.Asset]
        existing_assets: _containers.RepeatedScalarFieldContainer[str]
        scope: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope
        def __init__(self, new_assets: _Optional[_Iterable[_Union[_asset_pb2.Asset, _Mapping]]] = ..., existing_assets: _Optional[_Iterable[str]] = ..., scope: _Optional[_Union[ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope, str]] = ...) -> None: ...
    class MoveUnusedBudgetParameters(_message.Message):
        __slots__ = ("budget_micros_to_move",)
        BUDGET_MICROS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
        budget_micros_to_move: int
        def __init__(self, budget_micros_to_move: _Optional[int] = ...) -> None: ...
    class ResponsiveSearchAdAssetParameters(_message.Message):
        __slots__ = ("updated_ad",)
        UPDATED_AD_FIELD_NUMBER: _ClassVar[int]
        updated_ad: _ad_pb2.Ad
        def __init__(self, updated_ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ...) -> None: ...
    class ResponsiveSearchAdImproveAdStrengthParameters(_message.Message):
        __slots__ = ("updated_ad",)
        UPDATED_AD_FIELD_NUMBER: _ClassVar[int]
        updated_ad: _ad_pb2.Ad
        def __init__(self, updated_ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ...) -> None: ...
    class ResponsiveSearchAdParameters(_message.Message):
        __slots__ = ("ad",)
        AD_FIELD_NUMBER: _ClassVar[int]
        ad: _ad_pb2.Ad
        def __init__(self, ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ...) -> None: ...
    class RaiseTargetCpaBidTooLowParameters(_message.Message):
        __slots__ = ("target_multiplier",)
        TARGET_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        target_multiplier: float
        def __init__(self, target_multiplier: _Optional[float] = ...) -> None: ...
    class UseBroadMatchKeywordParameters(_message.Message):
        __slots__ = ("new_budget_amount_micros",)
        NEW_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        new_budget_amount_micros: int
        def __init__(self, new_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class ForecastingSetTargetCpaParameters(_message.Message):
        __slots__ = ("target_cpa_micros", "campaign_budget_amount_micros")
        TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        target_cpa_micros: int
        campaign_budget_amount_micros: int
        def __init__(self, target_cpa_micros: _Optional[int] = ..., campaign_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class LeadFormAssetParameters(_message.Message):
        __slots__ = ("ad_asset_apply_parameters", "set_submit_lead_form_asset_campaign_goal")
        AD_ASSET_APPLY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        SET_SUBMIT_LEAD_FORM_ASSET_CAMPAIGN_GOAL_FIELD_NUMBER: _ClassVar[int]
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        set_submit_lead_form_asset_campaign_goal: bool
        def __init__(self, ad_asset_apply_parameters: _Optional[_Union[ApplyRecommendationOperation.AdAssetApplyParameters, _Mapping]] = ..., set_submit_lead_form_asset_campaign_goal: bool = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    TEXT_AD_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_OPT_IN_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_OPT_IN_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    CALL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    SITELINK_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    MOVE_UNUSED_BUDGET_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_FIELD_NUMBER: _ClassVar[int]
    USE_BROAD_MATCH_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_ASSET_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_IMPROVE_AD_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    RAISE_TARGET_CPA_BID_TOO_LOW_FIELD_NUMBER: _ClassVar[int]
    FORECASTING_SET_TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_ASSET_FIELD_NUMBER: _ClassVar[int]
    CALL_ASSET_FIELD_NUMBER: _ClassVar[int]
    SITELINK_ASSET_FIELD_NUMBER: _ClassVar[int]
    RAISE_TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
    LOWER_TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    FORECASTING_SET_TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
    SET_TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
    SET_TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    LEAD_FORM_ASSET_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign_budget: ApplyRecommendationOperation.CampaignBudgetParameters
    text_ad: ApplyRecommendationOperation.TextAdParameters
    keyword: ApplyRecommendationOperation.KeywordParameters
    target_cpa_opt_in: ApplyRecommendationOperation.TargetCpaOptInParameters
    target_roas_opt_in: ApplyRecommendationOperation.TargetRoasOptInParameters
    callout_extension: ApplyRecommendationOperation.CalloutExtensionParameters
    call_extension: ApplyRecommendationOperation.CallExtensionParameters
    sitelink_extension: ApplyRecommendationOperation.SitelinkExtensionParameters
    move_unused_budget: ApplyRecommendationOperation.MoveUnusedBudgetParameters
    responsive_search_ad: ApplyRecommendationOperation.ResponsiveSearchAdParameters
    use_broad_match_keyword: ApplyRecommendationOperation.UseBroadMatchKeywordParameters
    responsive_search_ad_asset: ApplyRecommendationOperation.ResponsiveSearchAdAssetParameters
    responsive_search_ad_improve_ad_strength: ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParameters
    raise_target_cpa_bid_too_low: ApplyRecommendationOperation.RaiseTargetCpaBidTooLowParameters
    forecasting_set_target_roas: ApplyRecommendationOperation.ForecastingSetTargetRoasParameters
    callout_asset: ApplyRecommendationOperation.CalloutAssetParameters
    call_asset: ApplyRecommendationOperation.CallAssetParameters
    sitelink_asset: ApplyRecommendationOperation.SitelinkAssetParameters
    raise_target_cpa: ApplyRecommendationOperation.RaiseTargetCpaParameters
    lower_target_roas: ApplyRecommendationOperation.LowerTargetRoasParameters
    forecasting_set_target_cpa: ApplyRecommendationOperation.ForecastingSetTargetCpaParameters
    set_target_cpa: ApplyRecommendationOperation.ForecastingSetTargetCpaParameters
    set_target_roas: ApplyRecommendationOperation.ForecastingSetTargetRoasParameters
    lead_form_asset: ApplyRecommendationOperation.LeadFormAssetParameters
    def __init__(self, resource_name: _Optional[str] = ..., campaign_budget: _Optional[_Union[ApplyRecommendationOperation.CampaignBudgetParameters, _Mapping]] = ..., text_ad: _Optional[_Union[ApplyRecommendationOperation.TextAdParameters, _Mapping]] = ..., keyword: _Optional[_Union[ApplyRecommendationOperation.KeywordParameters, _Mapping]] = ..., target_cpa_opt_in: _Optional[_Union[ApplyRecommendationOperation.TargetCpaOptInParameters, _Mapping]] = ..., target_roas_opt_in: _Optional[_Union[ApplyRecommendationOperation.TargetRoasOptInParameters, _Mapping]] = ..., callout_extension: _Optional[_Union[ApplyRecommendationOperation.CalloutExtensionParameters, _Mapping]] = ..., call_extension: _Optional[_Union[ApplyRecommendationOperation.CallExtensionParameters, _Mapping]] = ..., sitelink_extension: _Optional[_Union[ApplyRecommendationOperation.SitelinkExtensionParameters, _Mapping]] = ..., move_unused_budget: _Optional[_Union[ApplyRecommendationOperation.MoveUnusedBudgetParameters, _Mapping]] = ..., responsive_search_ad: _Optional[_Union[ApplyRecommendationOperation.ResponsiveSearchAdParameters, _Mapping]] = ..., use_broad_match_keyword: _Optional[_Union[ApplyRecommendationOperation.UseBroadMatchKeywordParameters, _Mapping]] = ..., responsive_search_ad_asset: _Optional[_Union[ApplyRecommendationOperation.ResponsiveSearchAdAssetParameters, _Mapping]] = ..., responsive_search_ad_improve_ad_strength: _Optional[_Union[ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParameters, _Mapping]] = ..., raise_target_cpa_bid_too_low: _Optional[_Union[ApplyRecommendationOperation.RaiseTargetCpaBidTooLowParameters, _Mapping]] = ..., forecasting_set_target_roas: _Optional[_Union[ApplyRecommendationOperation.ForecastingSetTargetRoasParameters, _Mapping]] = ..., callout_asset: _Optional[_Union[ApplyRecommendationOperation.CalloutAssetParameters, _Mapping]] = ..., call_asset: _Optional[_Union[ApplyRecommendationOperation.CallAssetParameters, _Mapping]] = ..., sitelink_asset: _Optional[_Union[ApplyRecommendationOperation.SitelinkAssetParameters, _Mapping]] = ..., raise_target_cpa: _Optional[_Union[ApplyRecommendationOperation.RaiseTargetCpaParameters, _Mapping]] = ..., lower_target_roas: _Optional[_Union[ApplyRecommendationOperation.LowerTargetRoasParameters, _Mapping]] = ..., forecasting_set_target_cpa: _Optional[_Union[ApplyRecommendationOperation.ForecastingSetTargetCpaParameters, _Mapping]] = ..., set_target_cpa: _Optional[_Union[ApplyRecommendationOperation.ForecastingSetTargetCpaParameters, _Mapping]] = ..., set_target_roas: _Optional[_Union[ApplyRecommendationOperation.ForecastingSetTargetRoasParameters, _Mapping]] = ..., lead_form_asset: _Optional[_Union[ApplyRecommendationOperation.LeadFormAssetParameters, _Mapping]] = ...) -> None: ...

class ApplyRecommendationResponse(_message.Message):
    __slots__ = ("results", "partial_failure_error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ApplyRecommendationResult]
    partial_failure_error: _status_pb2.Status
    def __init__(self, results: _Optional[_Iterable[_Union[ApplyRecommendationResult, _Mapping]]] = ..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class ApplyRecommendationResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class DismissRecommendationRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure")
    class DismissRecommendationOperation(_message.Message):
        __slots__ = ("resource_name",)
        RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        resource_name: str
        def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[DismissRecommendationRequest.DismissRecommendationOperation]
    partial_failure: bool
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[DismissRecommendationRequest.DismissRecommendationOperation, _Mapping]]] = ..., partial_failure: bool = ...) -> None: ...

class DismissRecommendationResponse(_message.Message):
    __slots__ = ("results", "partial_failure_error")
    class DismissRecommendationResult(_message.Message):
        __slots__ = ("resource_name",)
        RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        resource_name: str
        def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[DismissRecommendationResponse.DismissRecommendationResult]
    partial_failure_error: _status_pb2.Status
    def __init__(self, results: _Optional[_Iterable[_Union[DismissRecommendationResponse.DismissRecommendationResult, _Mapping]]] = ..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class GenerateRecommendationsRequest(_message.Message):
    __slots__ = ("customer_id", "recommendation_types", "advertising_channel_type", "campaign_sitelink_count", "conversion_tracking_status", "bidding_info", "ad_group_info", "seed_info")
    class BiddingInfo(_message.Message):
        __slots__ = ("bidding_strategy_type", "target_cpa_micros", "target_roas")
        BIDDING_STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
        TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
        bidding_strategy_type: _bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType
        target_cpa_micros: int
        target_roas: float
        def __init__(self, bidding_strategy_type: _Optional[_Union[_bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType, str]] = ..., target_cpa_micros: _Optional[int] = ..., target_roas: _Optional[float] = ...) -> None: ...
    class AdGroupInfo(_message.Message):
        __slots__ = ("ad_group_type", "keywords")
        AD_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        KEYWORDS_FIELD_NUMBER: _ClassVar[int]
        ad_group_type: _ad_group_type_pb2.AdGroupTypeEnum.AdGroupType
        keywords: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.KeywordInfo]
        def __init__(self, ad_group_type: _Optional[_Union[_ad_group_type_pb2.AdGroupTypeEnum.AdGroupType, str]] = ..., keywords: _Optional[_Iterable[_Union[_criteria_pb2.KeywordInfo, _Mapping]]] = ...) -> None: ...
    class SeedInfo(_message.Message):
        __slots__ = ("url_seed", "keyword_seeds")
        URL_SEED_FIELD_NUMBER: _ClassVar[int]
        KEYWORD_SEEDS_FIELD_NUMBER: _ClassVar[int]
        url_seed: str
        keyword_seeds: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, url_seed: _Optional[str] = ..., keyword_seeds: _Optional[_Iterable[str]] = ...) -> None: ...
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SITELINK_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TRACKING_STATUS_FIELD_NUMBER: _ClassVar[int]
    BIDDING_INFO_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    SEED_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    recommendation_types: _containers.RepeatedScalarFieldContainer[_recommendation_type_pb2.RecommendationTypeEnum.RecommendationType]
    advertising_channel_type: _advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType
    campaign_sitelink_count: int
    conversion_tracking_status: _conversion_tracking_status_enum_pb2.ConversionTrackingStatusEnum.ConversionTrackingStatus
    bidding_info: GenerateRecommendationsRequest.BiddingInfo
    ad_group_info: _containers.RepeatedCompositeFieldContainer[GenerateRecommendationsRequest.AdGroupInfo]
    seed_info: GenerateRecommendationsRequest.SeedInfo
    def __init__(self, customer_id: _Optional[str] = ..., recommendation_types: _Optional[_Iterable[_Union[_recommendation_type_pb2.RecommendationTypeEnum.RecommendationType, str]]] = ..., advertising_channel_type: _Optional[_Union[_advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType, str]] = ..., campaign_sitelink_count: _Optional[int] = ..., conversion_tracking_status: _Optional[_Union[_conversion_tracking_status_enum_pb2.ConversionTrackingStatusEnum.ConversionTrackingStatus, str]] = ..., bidding_info: _Optional[_Union[GenerateRecommendationsRequest.BiddingInfo, _Mapping]] = ..., ad_group_info: _Optional[_Iterable[_Union[GenerateRecommendationsRequest.AdGroupInfo, _Mapping]]] = ..., seed_info: _Optional[_Union[GenerateRecommendationsRequest.SeedInfo, _Mapping]] = ...) -> None: ...

class GenerateRecommendationsResponse(_message.Message):
    __slots__ = ("recommendations",)
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    recommendations: _containers.RepeatedCompositeFieldContainer[_recommendation_pb2.Recommendation]
    def __init__(self, recommendations: _Optional[_Iterable[_Union[_recommendation_pb2.Recommendation, _Mapping]]] = ...) -> None: ...
