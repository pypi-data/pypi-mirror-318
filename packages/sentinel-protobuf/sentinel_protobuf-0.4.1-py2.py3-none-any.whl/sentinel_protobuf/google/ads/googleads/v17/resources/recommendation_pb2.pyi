from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v17.enums import ad_strength_pb2 as _ad_strength_pb2
from google.ads.googleads.v17.enums import app_bidding_goal_pb2 as _app_bidding_goal_pb2
from google.ads.googleads.v17.enums import keyword_match_type_pb2 as _keyword_match_type_pb2
from google.ads.googleads.v17.enums import recommendation_type_pb2 as _recommendation_type_pb2
from google.ads.googleads.v17.enums import shopping_add_products_to_campaign_recommendation_enum_pb2 as _shopping_add_products_to_campaign_recommendation_enum_pb2
from google.ads.googleads.v17.enums import target_cpa_opt_in_recommendation_goal_pb2 as _target_cpa_opt_in_recommendation_goal_pb2
from google.ads.googleads.v17.resources import ad_pb2 as _ad_pb2
from google.ads.googleads.v17.resources import asset_pb2 as _asset_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recommendation(_message.Message):
    __slots__ = ("resource_name", "type", "impact", "campaign_budget", "campaign", "ad_group", "dismissed", "campaigns", "campaign_budget_recommendation", "forecasting_campaign_budget_recommendation", "keyword_recommendation", "text_ad_recommendation", "target_cpa_opt_in_recommendation", "maximize_conversions_opt_in_recommendation", "enhanced_cpc_opt_in_recommendation", "search_partners_opt_in_recommendation", "maximize_clicks_opt_in_recommendation", "optimize_ad_rotation_recommendation", "keyword_match_type_recommendation", "move_unused_budget_recommendation", "target_roas_opt_in_recommendation", "responsive_search_ad_recommendation", "marginal_roi_campaign_budget_recommendation", "use_broad_match_keyword_recommendation", "responsive_search_ad_asset_recommendation", "upgrade_smart_shopping_campaign_to_performance_max_recommendation", "responsive_search_ad_improve_ad_strength_recommendation", "display_expansion_opt_in_recommendation", "upgrade_local_campaign_to_performance_max_recommendation", "raise_target_cpa_bid_too_low_recommendation", "forecasting_set_target_roas_recommendation", "callout_asset_recommendation", "sitelink_asset_recommendation", "call_asset_recommendation", "shopping_add_age_group_recommendation", "shopping_add_color_recommendation", "shopping_add_gender_recommendation", "shopping_add_gtin_recommendation", "shopping_add_more_identifiers_recommendation", "shopping_add_size_recommendation", "shopping_add_products_to_campaign_recommendation", "shopping_fix_disapproved_products_recommendation", "shopping_target_all_offers_recommendation", "shopping_fix_suspended_merchant_center_account_recommendation", "shopping_fix_merchant_center_account_suspension_warning_recommendation", "shopping_migrate_regular_shopping_campaign_offers_to_performance_max_recommendation", "dynamic_image_extension_opt_in_recommendation", "raise_target_cpa_recommendation", "lower_target_roas_recommendation", "performance_max_opt_in_recommendation", "improve_performance_max_ad_strength_recommendation", "migrate_dynamic_search_ads_campaign_to_performance_max_recommendation", "forecasting_set_target_cpa_recommendation", "set_target_cpa_recommendation", "set_target_roas_recommendation", "maximize_conversion_value_opt_in_recommendation", "improve_google_tag_coverage_recommendation", "performance_max_final_url_opt_in_recommendation", "refresh_customer_match_list_recommendation", "custom_audience_opt_in_recommendation", "lead_form_asset_recommendation", "improve_demand_gen_ad_strength_recommendation")
    class MerchantInfo(_message.Message):
        __slots__ = ("id", "name", "multi_client")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MULTI_CLIENT_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        multi_client: bool
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., multi_client: bool = ...) -> None: ...
    class RecommendationImpact(_message.Message):
        __slots__ = ("base_metrics", "potential_metrics")
        BASE_METRICS_FIELD_NUMBER: _ClassVar[int]
        POTENTIAL_METRICS_FIELD_NUMBER: _ClassVar[int]
        base_metrics: Recommendation.RecommendationMetrics
        potential_metrics: Recommendation.RecommendationMetrics
        def __init__(self, base_metrics: _Optional[_Union[Recommendation.RecommendationMetrics, _Mapping]] = ..., potential_metrics: _Optional[_Union[Recommendation.RecommendationMetrics, _Mapping]] = ...) -> None: ...
    class RecommendationMetrics(_message.Message):
        __slots__ = ("impressions", "clicks", "cost_micros", "conversions", "conversions_value", "video_views")
        IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        CLICKS_FIELD_NUMBER: _ClassVar[int]
        COST_MICROS_FIELD_NUMBER: _ClassVar[int]
        CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
        CONVERSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_VIEWS_FIELD_NUMBER: _ClassVar[int]
        impressions: float
        clicks: float
        cost_micros: int
        conversions: float
        conversions_value: float
        video_views: float
        def __init__(self, impressions: _Optional[float] = ..., clicks: _Optional[float] = ..., cost_micros: _Optional[int] = ..., conversions: _Optional[float] = ..., conversions_value: _Optional[float] = ..., video_views: _Optional[float] = ...) -> None: ...
    class CampaignBudgetRecommendation(_message.Message):
        __slots__ = ("current_budget_amount_micros", "recommended_budget_amount_micros", "budget_options")
        class CampaignBudgetRecommendationOption(_message.Message):
            __slots__ = ("budget_amount_micros", "impact")
            BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
            IMPACT_FIELD_NUMBER: _ClassVar[int]
            budget_amount_micros: int
            impact: Recommendation.RecommendationImpact
            def __init__(self, budget_amount_micros: _Optional[int] = ..., impact: _Optional[_Union[Recommendation.RecommendationImpact, _Mapping]] = ...) -> None: ...
        CURRENT_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        BUDGET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        current_budget_amount_micros: int
        recommended_budget_amount_micros: int
        budget_options: _containers.RepeatedCompositeFieldContainer[Recommendation.CampaignBudgetRecommendation.CampaignBudgetRecommendationOption]
        def __init__(self, current_budget_amount_micros: _Optional[int] = ..., recommended_budget_amount_micros: _Optional[int] = ..., budget_options: _Optional[_Iterable[_Union[Recommendation.CampaignBudgetRecommendation.CampaignBudgetRecommendationOption, _Mapping]]] = ...) -> None: ...
    class KeywordRecommendation(_message.Message):
        __slots__ = ("keyword", "search_terms", "recommended_cpc_bid_micros")
        class SearchTerm(_message.Message):
            __slots__ = ("text", "estimated_weekly_search_count")
            TEXT_FIELD_NUMBER: _ClassVar[int]
            ESTIMATED_WEEKLY_SEARCH_COUNT_FIELD_NUMBER: _ClassVar[int]
            text: str
            estimated_weekly_search_count: int
            def __init__(self, text: _Optional[str] = ..., estimated_weekly_search_count: _Optional[int] = ...) -> None: ...
        KEYWORD_FIELD_NUMBER: _ClassVar[int]
        SEARCH_TERMS_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
        keyword: _criteria_pb2.KeywordInfo
        search_terms: _containers.RepeatedCompositeFieldContainer[Recommendation.KeywordRecommendation.SearchTerm]
        recommended_cpc_bid_micros: int
        def __init__(self, keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., search_terms: _Optional[_Iterable[_Union[Recommendation.KeywordRecommendation.SearchTerm, _Mapping]]] = ..., recommended_cpc_bid_micros: _Optional[int] = ...) -> None: ...
    class TextAdRecommendation(_message.Message):
        __slots__ = ("ad", "creation_date", "auto_apply_date")
        AD_FIELD_NUMBER: _ClassVar[int]
        CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
        AUTO_APPLY_DATE_FIELD_NUMBER: _ClassVar[int]
        ad: _ad_pb2.Ad
        creation_date: str
        auto_apply_date: str
        def __init__(self, ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ..., creation_date: _Optional[str] = ..., auto_apply_date: _Optional[str] = ...) -> None: ...
    class TargetCpaOptInRecommendation(_message.Message):
        __slots__ = ("options", "recommended_target_cpa_micros")
        class TargetCpaOptInRecommendationOption(_message.Message):
            __slots__ = ("goal", "target_cpa_micros", "required_campaign_budget_amount_micros", "impact")
            GOAL_FIELD_NUMBER: _ClassVar[int]
            TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
            REQUIRED_CAMPAIGN_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
            IMPACT_FIELD_NUMBER: _ClassVar[int]
            goal: _target_cpa_opt_in_recommendation_goal_pb2.TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
            target_cpa_micros: int
            required_campaign_budget_amount_micros: int
            impact: Recommendation.RecommendationImpact
            def __init__(self, goal: _Optional[_Union[_target_cpa_opt_in_recommendation_goal_pb2.TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal, str]] = ..., target_cpa_micros: _Optional[int] = ..., required_campaign_budget_amount_micros: _Optional[int] = ..., impact: _Optional[_Union[Recommendation.RecommendationImpact, _Mapping]] = ...) -> None: ...
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        options: _containers.RepeatedCompositeFieldContainer[Recommendation.TargetCpaOptInRecommendation.TargetCpaOptInRecommendationOption]
        recommended_target_cpa_micros: int
        def __init__(self, options: _Optional[_Iterable[_Union[Recommendation.TargetCpaOptInRecommendation.TargetCpaOptInRecommendationOption, _Mapping]]] = ..., recommended_target_cpa_micros: _Optional[int] = ...) -> None: ...
    class MaximizeConversionsOptInRecommendation(_message.Message):
        __slots__ = ("recommended_budget_amount_micros",)
        RECOMMENDED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        recommended_budget_amount_micros: int
        def __init__(self, recommended_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class EnhancedCpcOptInRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SearchPartnersOptInRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MaximizeClicksOptInRecommendation(_message.Message):
        __slots__ = ("recommended_budget_amount_micros",)
        RECOMMENDED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        recommended_budget_amount_micros: int
        def __init__(self, recommended_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class OptimizeAdRotationRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CalloutAssetRecommendation(_message.Message):
        __slots__ = ("recommended_campaign_callout_assets", "recommended_customer_callout_assets")
        RECOMMENDED_CAMPAIGN_CALLOUT_ASSETS_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_CUSTOMER_CALLOUT_ASSETS_FIELD_NUMBER: _ClassVar[int]
        recommended_campaign_callout_assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.Asset]
        recommended_customer_callout_assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.Asset]
        def __init__(self, recommended_campaign_callout_assets: _Optional[_Iterable[_Union[_asset_pb2.Asset, _Mapping]]] = ..., recommended_customer_callout_assets: _Optional[_Iterable[_Union[_asset_pb2.Asset, _Mapping]]] = ...) -> None: ...
    class SitelinkAssetRecommendation(_message.Message):
        __slots__ = ("recommended_campaign_sitelink_assets", "recommended_customer_sitelink_assets")
        RECOMMENDED_CAMPAIGN_SITELINK_ASSETS_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_CUSTOMER_SITELINK_ASSETS_FIELD_NUMBER: _ClassVar[int]
        recommended_campaign_sitelink_assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.Asset]
        recommended_customer_sitelink_assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.Asset]
        def __init__(self, recommended_campaign_sitelink_assets: _Optional[_Iterable[_Union[_asset_pb2.Asset, _Mapping]]] = ..., recommended_customer_sitelink_assets: _Optional[_Iterable[_Union[_asset_pb2.Asset, _Mapping]]] = ...) -> None: ...
    class CallAssetRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class KeywordMatchTypeRecommendation(_message.Message):
        __slots__ = ("keyword", "recommended_match_type")
        KEYWORD_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        keyword: _criteria_pb2.KeywordInfo
        recommended_match_type: _keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType
        def __init__(self, keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., recommended_match_type: _Optional[_Union[_keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType, str]] = ...) -> None: ...
    class MoveUnusedBudgetRecommendation(_message.Message):
        __slots__ = ("excess_campaign_budget", "budget_recommendation")
        EXCESS_CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
        BUDGET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
        excess_campaign_budget: str
        budget_recommendation: Recommendation.CampaignBudgetRecommendation
        def __init__(self, excess_campaign_budget: _Optional[str] = ..., budget_recommendation: _Optional[_Union[Recommendation.CampaignBudgetRecommendation, _Mapping]] = ...) -> None: ...
    class TargetRoasOptInRecommendation(_message.Message):
        __slots__ = ("recommended_target_roas", "required_campaign_budget_amount_micros")
        RECOMMENDED_TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_CAMPAIGN_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        recommended_target_roas: float
        required_campaign_budget_amount_micros: int
        def __init__(self, recommended_target_roas: _Optional[float] = ..., required_campaign_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class ResponsiveSearchAdAssetRecommendation(_message.Message):
        __slots__ = ("current_ad", "recommended_assets")
        CURRENT_AD_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_ASSETS_FIELD_NUMBER: _ClassVar[int]
        current_ad: _ad_pb2.Ad
        recommended_assets: _ad_pb2.Ad
        def __init__(self, current_ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ..., recommended_assets: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ...) -> None: ...
    class ResponsiveSearchAdImproveAdStrengthRecommendation(_message.Message):
        __slots__ = ("current_ad", "recommended_ad")
        CURRENT_AD_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_AD_FIELD_NUMBER: _ClassVar[int]
        current_ad: _ad_pb2.Ad
        recommended_ad: _ad_pb2.Ad
        def __init__(self, current_ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ..., recommended_ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ...) -> None: ...
    class ResponsiveSearchAdRecommendation(_message.Message):
        __slots__ = ("ad",)
        AD_FIELD_NUMBER: _ClassVar[int]
        ad: _ad_pb2.Ad
        def __init__(self, ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ...) -> None: ...
    class UseBroadMatchKeywordRecommendation(_message.Message):
        __slots__ = ("keyword", "suggested_keywords_count", "campaign_keywords_count", "campaign_uses_shared_budget", "required_campaign_budget_amount_micros")
        KEYWORD_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_KEYWORDS_COUNT_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_KEYWORDS_COUNT_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_USES_SHARED_BUDGET_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_CAMPAIGN_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        keyword: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.KeywordInfo]
        suggested_keywords_count: int
        campaign_keywords_count: int
        campaign_uses_shared_budget: bool
        required_campaign_budget_amount_micros: int
        def __init__(self, keyword: _Optional[_Iterable[_Union[_criteria_pb2.KeywordInfo, _Mapping]]] = ..., suggested_keywords_count: _Optional[int] = ..., campaign_keywords_count: _Optional[int] = ..., campaign_uses_shared_budget: bool = ..., required_campaign_budget_amount_micros: _Optional[int] = ...) -> None: ...
    class UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation(_message.Message):
        __slots__ = ("merchant_id", "sales_country_code")
        MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
        SALES_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        merchant_id: int
        sales_country_code: str
        def __init__(self, merchant_id: _Optional[int] = ..., sales_country_code: _Optional[str] = ...) -> None: ...
    class RaiseTargetCpaBidTooLowRecommendation(_message.Message):
        __slots__ = ("recommended_target_multiplier", "average_target_cpa_micros")
        RECOMMENDED_TARGET_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        AVERAGE_TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        recommended_target_multiplier: float
        average_target_cpa_micros: int
        def __init__(self, recommended_target_multiplier: _Optional[float] = ..., average_target_cpa_micros: _Optional[int] = ...) -> None: ...
    class DisplayExpansionOptInRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class UpgradeLocalCampaignToPerformanceMaxRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ForecastingSetTargetRoasRecommendation(_message.Message):
        __slots__ = ("recommended_target_roas", "campaign_budget")
        RECOMMENDED_TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
        recommended_target_roas: float
        campaign_budget: Recommendation.CampaignBudget
        def __init__(self, recommended_target_roas: _Optional[float] = ..., campaign_budget: _Optional[_Union[Recommendation.CampaignBudget, _Mapping]] = ...) -> None: ...
    class ShoppingOfferAttributeRecommendation(_message.Message):
        __slots__ = ("merchant", "feed_label", "offers_count", "demoted_offers_count")
        MERCHANT_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        OFFERS_COUNT_FIELD_NUMBER: _ClassVar[int]
        DEMOTED_OFFERS_COUNT_FIELD_NUMBER: _ClassVar[int]
        merchant: Recommendation.MerchantInfo
        feed_label: str
        offers_count: int
        demoted_offers_count: int
        def __init__(self, merchant: _Optional[_Union[Recommendation.MerchantInfo, _Mapping]] = ..., feed_label: _Optional[str] = ..., offers_count: _Optional[int] = ..., demoted_offers_count: _Optional[int] = ...) -> None: ...
    class ShoppingFixDisapprovedProductsRecommendation(_message.Message):
        __slots__ = ("merchant", "feed_label", "products_count", "disapproved_products_count")
        MERCHANT_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        PRODUCTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        DISAPPROVED_PRODUCTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        merchant: Recommendation.MerchantInfo
        feed_label: str
        products_count: int
        disapproved_products_count: int
        def __init__(self, merchant: _Optional[_Union[Recommendation.MerchantInfo, _Mapping]] = ..., feed_label: _Optional[str] = ..., products_count: _Optional[int] = ..., disapproved_products_count: _Optional[int] = ...) -> None: ...
    class ShoppingTargetAllOffersRecommendation(_message.Message):
        __slots__ = ("merchant", "untargeted_offers_count", "feed_label")
        MERCHANT_FIELD_NUMBER: _ClassVar[int]
        UNTARGETED_OFFERS_COUNT_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        merchant: Recommendation.MerchantInfo
        untargeted_offers_count: int
        feed_label: str
        def __init__(self, merchant: _Optional[_Union[Recommendation.MerchantInfo, _Mapping]] = ..., untargeted_offers_count: _Optional[int] = ..., feed_label: _Optional[str] = ...) -> None: ...
    class ShoppingAddProductsToCampaignRecommendation(_message.Message):
        __slots__ = ("merchant", "feed_label", "reason")
        MERCHANT_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        merchant: Recommendation.MerchantInfo
        feed_label: str
        reason: _shopping_add_products_to_campaign_recommendation_enum_pb2.ShoppingAddProductsToCampaignRecommendationEnum.Reason
        def __init__(self, merchant: _Optional[_Union[Recommendation.MerchantInfo, _Mapping]] = ..., feed_label: _Optional[str] = ..., reason: _Optional[_Union[_shopping_add_products_to_campaign_recommendation_enum_pb2.ShoppingAddProductsToCampaignRecommendationEnum.Reason, str]] = ...) -> None: ...
    class ShoppingMerchantCenterAccountSuspensionRecommendation(_message.Message):
        __slots__ = ("merchant", "feed_label")
        MERCHANT_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        merchant: Recommendation.MerchantInfo
        feed_label: str
        def __init__(self, merchant: _Optional[_Union[Recommendation.MerchantInfo, _Mapping]] = ..., feed_label: _Optional[str] = ...) -> None: ...
    class ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation(_message.Message):
        __slots__ = ("merchant", "feed_label")
        MERCHANT_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        merchant: Recommendation.MerchantInfo
        feed_label: str
        def __init__(self, merchant: _Optional[_Union[Recommendation.MerchantInfo, _Mapping]] = ..., feed_label: _Optional[str] = ...) -> None: ...
    class TargetAdjustmentInfo(_message.Message):
        __slots__ = ("shared_set", "recommended_target_multiplier", "current_average_target_micros")
        SHARED_SET_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_TARGET_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        CURRENT_AVERAGE_TARGET_MICROS_FIELD_NUMBER: _ClassVar[int]
        shared_set: str
        recommended_target_multiplier: float
        current_average_target_micros: int
        def __init__(self, shared_set: _Optional[str] = ..., recommended_target_multiplier: _Optional[float] = ..., current_average_target_micros: _Optional[int] = ...) -> None: ...
    class RaiseTargetCpaRecommendation(_message.Message):
        __slots__ = ("target_adjustment", "app_bidding_goal")
        TARGET_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
        APP_BIDDING_GOAL_FIELD_NUMBER: _ClassVar[int]
        target_adjustment: Recommendation.TargetAdjustmentInfo
        app_bidding_goal: _app_bidding_goal_pb2.AppBiddingGoalEnum.AppBiddingGoal
        def __init__(self, target_adjustment: _Optional[_Union[Recommendation.TargetAdjustmentInfo, _Mapping]] = ..., app_bidding_goal: _Optional[_Union[_app_bidding_goal_pb2.AppBiddingGoalEnum.AppBiddingGoal, str]] = ...) -> None: ...
    class LowerTargetRoasRecommendation(_message.Message):
        __slots__ = ("target_adjustment",)
        TARGET_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
        target_adjustment: Recommendation.TargetAdjustmentInfo
        def __init__(self, target_adjustment: _Optional[_Union[Recommendation.TargetAdjustmentInfo, _Mapping]] = ...) -> None: ...
    class DynamicImageExtensionOptInRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CampaignBudget(_message.Message):
        __slots__ = ("current_amount_micros", "recommended_new_amount_micros", "new_start_date")
        CURRENT_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDED_NEW_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        NEW_START_DATE_FIELD_NUMBER: _ClassVar[int]
        current_amount_micros: int
        recommended_new_amount_micros: int
        new_start_date: str
        def __init__(self, current_amount_micros: _Optional[int] = ..., recommended_new_amount_micros: _Optional[int] = ..., new_start_date: _Optional[str] = ...) -> None: ...
    class PerformanceMaxOptInRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ImprovePerformanceMaxAdStrengthRecommendation(_message.Message):
        __slots__ = ("asset_group",)
        ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
        asset_group: str
        def __init__(self, asset_group: _Optional[str] = ...) -> None: ...
    class MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation(_message.Message):
        __slots__ = ("apply_link",)
        APPLY_LINK_FIELD_NUMBER: _ClassVar[int]
        apply_link: str
        def __init__(self, apply_link: _Optional[str] = ...) -> None: ...
    class ForecastingSetTargetCpaRecommendation(_message.Message):
        __slots__ = ("recommended_target_cpa_micros", "campaign_budget")
        RECOMMENDED_TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
        recommended_target_cpa_micros: int
        campaign_budget: Recommendation.CampaignBudget
        def __init__(self, recommended_target_cpa_micros: _Optional[int] = ..., campaign_budget: _Optional[_Union[Recommendation.CampaignBudget, _Mapping]] = ...) -> None: ...
    class MaximizeConversionValueOptInRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ImproveGoogleTagCoverageRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PerformanceMaxFinalUrlOptInRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RefreshCustomerMatchListRecommendation(_message.Message):
        __slots__ = ("user_list_id", "user_list_name", "days_since_last_refresh", "top_spending_account", "targeting_accounts_count", "owner_account")
        USER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
        USER_LIST_NAME_FIELD_NUMBER: _ClassVar[int]
        DAYS_SINCE_LAST_REFRESH_FIELD_NUMBER: _ClassVar[int]
        TOP_SPENDING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        TARGETING_ACCOUNTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        OWNER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        user_list_id: int
        user_list_name: str
        days_since_last_refresh: int
        top_spending_account: _containers.RepeatedCompositeFieldContainer[Recommendation.AccountInfo]
        targeting_accounts_count: int
        owner_account: Recommendation.AccountInfo
        def __init__(self, user_list_id: _Optional[int] = ..., user_list_name: _Optional[str] = ..., days_since_last_refresh: _Optional[int] = ..., top_spending_account: _Optional[_Iterable[_Union[Recommendation.AccountInfo, _Mapping]]] = ..., targeting_accounts_count: _Optional[int] = ..., owner_account: _Optional[_Union[Recommendation.AccountInfo, _Mapping]] = ...) -> None: ...
    class AccountInfo(_message.Message):
        __slots__ = ("customer_id", "descriptive_name")
        CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        customer_id: int
        descriptive_name: str
        def __init__(self, customer_id: _Optional[int] = ..., descriptive_name: _Optional[str] = ...) -> None: ...
    class CustomAudienceOptInRecommendation(_message.Message):
        __slots__ = ("keywords",)
        KEYWORDS_FIELD_NUMBER: _ClassVar[int]
        keywords: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.KeywordInfo]
        def __init__(self, keywords: _Optional[_Iterable[_Union[_criteria_pb2.KeywordInfo, _Mapping]]] = ...) -> None: ...
    class LeadFormAssetRecommendation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ImproveDemandGenAdStrengthRecommendation(_message.Message):
        __slots__ = ("ad", "ad_strength", "demand_gen_asset_action_items")
        AD_FIELD_NUMBER: _ClassVar[int]
        AD_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        DEMAND_GEN_ASSET_ACTION_ITEMS_FIELD_NUMBER: _ClassVar[int]
        ad: str
        ad_strength: _ad_strength_pb2.AdStrengthEnum.AdStrength
        demand_gen_asset_action_items: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, ad: _Optional[str] = ..., ad_strength: _Optional[_Union[_ad_strength_pb2.AdStrengthEnum.AdStrength, str]] = ..., demand_gen_asset_action_items: _Optional[_Iterable[str]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IMPACT_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    DISMISSED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    FORECASTING_CAMPAIGN_BUDGET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_AD_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSIONS_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    ENHANCED_CPC_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARTNERS_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CLICKS_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_AD_ROTATION_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_MATCH_TYPE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MOVE_UNUSED_BUDGET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MARGINAL_ROI_CAMPAIGN_BUDGET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    USE_BROAD_MATCH_KEYWORD_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_ASSET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SMART_SHOPPING_CAMPAIGN_TO_PERFORMANCE_MAX_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_IMPROVE_AD_STRENGTH_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_EXPANSION_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_LOCAL_CAMPAIGN_TO_PERFORMANCE_MAX_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    RAISE_TARGET_CPA_BID_TOO_LOW_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    FORECASTING_SET_TARGET_ROAS_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_ASSET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SITELINK_ASSET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    CALL_ASSET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADD_AGE_GROUP_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADD_COLOR_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADD_GENDER_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADD_GTIN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADD_MORE_IDENTIFIERS_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADD_SIZE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADD_PRODUCTS_TO_CAMPAIGN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_FIX_DISAPPROVED_PRODUCTS_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_TARGET_ALL_OFFERS_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_FIX_SUSPENDED_MERCHANT_CENTER_ACCOUNT_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_FIX_MERCHANT_CENTER_ACCOUNT_SUSPENSION_WARNING_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_MIGRATE_REGULAR_SHOPPING_CAMPAIGN_OFFERS_TO_PERFORMANCE_MAX_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_IMAGE_EXTENSION_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    RAISE_TARGET_CPA_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    LOWER_TARGET_ROAS_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_MAX_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    IMPROVE_PERFORMANCE_MAX_AD_STRENGTH_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_DYNAMIC_SEARCH_ADS_CAMPAIGN_TO_PERFORMANCE_MAX_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    FORECASTING_SET_TARGET_CPA_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SET_TARGET_CPA_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    SET_TARGET_ROAS_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSION_VALUE_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    IMPROVE_GOOGLE_TAG_COVERAGE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_MAX_FINAL_URL_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    REFRESH_CUSTOMER_MATCH_LIST_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AUDIENCE_OPT_IN_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    LEAD_FORM_ASSET_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    IMPROVE_DEMAND_GEN_AD_STRENGTH_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    type: _recommendation_type_pb2.RecommendationTypeEnum.RecommendationType
    impact: Recommendation.RecommendationImpact
    campaign_budget: str
    campaign: str
    ad_group: str
    dismissed: bool
    campaigns: _containers.RepeatedScalarFieldContainer[str]
    campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation
    forecasting_campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation
    keyword_recommendation: Recommendation.KeywordRecommendation
    text_ad_recommendation: Recommendation.TextAdRecommendation
    target_cpa_opt_in_recommendation: Recommendation.TargetCpaOptInRecommendation
    maximize_conversions_opt_in_recommendation: Recommendation.MaximizeConversionsOptInRecommendation
    enhanced_cpc_opt_in_recommendation: Recommendation.EnhancedCpcOptInRecommendation
    search_partners_opt_in_recommendation: Recommendation.SearchPartnersOptInRecommendation
    maximize_clicks_opt_in_recommendation: Recommendation.MaximizeClicksOptInRecommendation
    optimize_ad_rotation_recommendation: Recommendation.OptimizeAdRotationRecommendation
    keyword_match_type_recommendation: Recommendation.KeywordMatchTypeRecommendation
    move_unused_budget_recommendation: Recommendation.MoveUnusedBudgetRecommendation
    target_roas_opt_in_recommendation: Recommendation.TargetRoasOptInRecommendation
    responsive_search_ad_recommendation: Recommendation.ResponsiveSearchAdRecommendation
    marginal_roi_campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation
    use_broad_match_keyword_recommendation: Recommendation.UseBroadMatchKeywordRecommendation
    responsive_search_ad_asset_recommendation: Recommendation.ResponsiveSearchAdAssetRecommendation
    upgrade_smart_shopping_campaign_to_performance_max_recommendation: Recommendation.UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation
    responsive_search_ad_improve_ad_strength_recommendation: Recommendation.ResponsiveSearchAdImproveAdStrengthRecommendation
    display_expansion_opt_in_recommendation: Recommendation.DisplayExpansionOptInRecommendation
    upgrade_local_campaign_to_performance_max_recommendation: Recommendation.UpgradeLocalCampaignToPerformanceMaxRecommendation
    raise_target_cpa_bid_too_low_recommendation: Recommendation.RaiseTargetCpaBidTooLowRecommendation
    forecasting_set_target_roas_recommendation: Recommendation.ForecastingSetTargetRoasRecommendation
    callout_asset_recommendation: Recommendation.CalloutAssetRecommendation
    sitelink_asset_recommendation: Recommendation.SitelinkAssetRecommendation
    call_asset_recommendation: Recommendation.CallAssetRecommendation
    shopping_add_age_group_recommendation: Recommendation.ShoppingOfferAttributeRecommendation
    shopping_add_color_recommendation: Recommendation.ShoppingOfferAttributeRecommendation
    shopping_add_gender_recommendation: Recommendation.ShoppingOfferAttributeRecommendation
    shopping_add_gtin_recommendation: Recommendation.ShoppingOfferAttributeRecommendation
    shopping_add_more_identifiers_recommendation: Recommendation.ShoppingOfferAttributeRecommendation
    shopping_add_size_recommendation: Recommendation.ShoppingOfferAttributeRecommendation
    shopping_add_products_to_campaign_recommendation: Recommendation.ShoppingAddProductsToCampaignRecommendation
    shopping_fix_disapproved_products_recommendation: Recommendation.ShoppingFixDisapprovedProductsRecommendation
    shopping_target_all_offers_recommendation: Recommendation.ShoppingTargetAllOffersRecommendation
    shopping_fix_suspended_merchant_center_account_recommendation: Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation
    shopping_fix_merchant_center_account_suspension_warning_recommendation: Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation
    shopping_migrate_regular_shopping_campaign_offers_to_performance_max_recommendation: Recommendation.ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation
    dynamic_image_extension_opt_in_recommendation: Recommendation.DynamicImageExtensionOptInRecommendation
    raise_target_cpa_recommendation: Recommendation.RaiseTargetCpaRecommendation
    lower_target_roas_recommendation: Recommendation.LowerTargetRoasRecommendation
    performance_max_opt_in_recommendation: Recommendation.PerformanceMaxOptInRecommendation
    improve_performance_max_ad_strength_recommendation: Recommendation.ImprovePerformanceMaxAdStrengthRecommendation
    migrate_dynamic_search_ads_campaign_to_performance_max_recommendation: Recommendation.MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation
    forecasting_set_target_cpa_recommendation: Recommendation.ForecastingSetTargetCpaRecommendation
    set_target_cpa_recommendation: Recommendation.ForecastingSetTargetCpaRecommendation
    set_target_roas_recommendation: Recommendation.ForecastingSetTargetRoasRecommendation
    maximize_conversion_value_opt_in_recommendation: Recommendation.MaximizeConversionValueOptInRecommendation
    improve_google_tag_coverage_recommendation: Recommendation.ImproveGoogleTagCoverageRecommendation
    performance_max_final_url_opt_in_recommendation: Recommendation.PerformanceMaxFinalUrlOptInRecommendation
    refresh_customer_match_list_recommendation: Recommendation.RefreshCustomerMatchListRecommendation
    custom_audience_opt_in_recommendation: Recommendation.CustomAudienceOptInRecommendation
    lead_form_asset_recommendation: Recommendation.LeadFormAssetRecommendation
    improve_demand_gen_ad_strength_recommendation: Recommendation.ImproveDemandGenAdStrengthRecommendation
    def __init__(self, resource_name: _Optional[str] = ..., type: _Optional[_Union[_recommendation_type_pb2.RecommendationTypeEnum.RecommendationType, str]] = ..., impact: _Optional[_Union[Recommendation.RecommendationImpact, _Mapping]] = ..., campaign_budget: _Optional[str] = ..., campaign: _Optional[str] = ..., ad_group: _Optional[str] = ..., dismissed: bool = ..., campaigns: _Optional[_Iterable[str]] = ..., campaign_budget_recommendation: _Optional[_Union[Recommendation.CampaignBudgetRecommendation, _Mapping]] = ..., forecasting_campaign_budget_recommendation: _Optional[_Union[Recommendation.CampaignBudgetRecommendation, _Mapping]] = ..., keyword_recommendation: _Optional[_Union[Recommendation.KeywordRecommendation, _Mapping]] = ..., text_ad_recommendation: _Optional[_Union[Recommendation.TextAdRecommendation, _Mapping]] = ..., target_cpa_opt_in_recommendation: _Optional[_Union[Recommendation.TargetCpaOptInRecommendation, _Mapping]] = ..., maximize_conversions_opt_in_recommendation: _Optional[_Union[Recommendation.MaximizeConversionsOptInRecommendation, _Mapping]] = ..., enhanced_cpc_opt_in_recommendation: _Optional[_Union[Recommendation.EnhancedCpcOptInRecommendation, _Mapping]] = ..., search_partners_opt_in_recommendation: _Optional[_Union[Recommendation.SearchPartnersOptInRecommendation, _Mapping]] = ..., maximize_clicks_opt_in_recommendation: _Optional[_Union[Recommendation.MaximizeClicksOptInRecommendation, _Mapping]] = ..., optimize_ad_rotation_recommendation: _Optional[_Union[Recommendation.OptimizeAdRotationRecommendation, _Mapping]] = ..., keyword_match_type_recommendation: _Optional[_Union[Recommendation.KeywordMatchTypeRecommendation, _Mapping]] = ..., move_unused_budget_recommendation: _Optional[_Union[Recommendation.MoveUnusedBudgetRecommendation, _Mapping]] = ..., target_roas_opt_in_recommendation: _Optional[_Union[Recommendation.TargetRoasOptInRecommendation, _Mapping]] = ..., responsive_search_ad_recommendation: _Optional[_Union[Recommendation.ResponsiveSearchAdRecommendation, _Mapping]] = ..., marginal_roi_campaign_budget_recommendation: _Optional[_Union[Recommendation.CampaignBudgetRecommendation, _Mapping]] = ..., use_broad_match_keyword_recommendation: _Optional[_Union[Recommendation.UseBroadMatchKeywordRecommendation, _Mapping]] = ..., responsive_search_ad_asset_recommendation: _Optional[_Union[Recommendation.ResponsiveSearchAdAssetRecommendation, _Mapping]] = ..., upgrade_smart_shopping_campaign_to_performance_max_recommendation: _Optional[_Union[Recommendation.UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation, _Mapping]] = ..., responsive_search_ad_improve_ad_strength_recommendation: _Optional[_Union[Recommendation.ResponsiveSearchAdImproveAdStrengthRecommendation, _Mapping]] = ..., display_expansion_opt_in_recommendation: _Optional[_Union[Recommendation.DisplayExpansionOptInRecommendation, _Mapping]] = ..., upgrade_local_campaign_to_performance_max_recommendation: _Optional[_Union[Recommendation.UpgradeLocalCampaignToPerformanceMaxRecommendation, _Mapping]] = ..., raise_target_cpa_bid_too_low_recommendation: _Optional[_Union[Recommendation.RaiseTargetCpaBidTooLowRecommendation, _Mapping]] = ..., forecasting_set_target_roas_recommendation: _Optional[_Union[Recommendation.ForecastingSetTargetRoasRecommendation, _Mapping]] = ..., callout_asset_recommendation: _Optional[_Union[Recommendation.CalloutAssetRecommendation, _Mapping]] = ..., sitelink_asset_recommendation: _Optional[_Union[Recommendation.SitelinkAssetRecommendation, _Mapping]] = ..., call_asset_recommendation: _Optional[_Union[Recommendation.CallAssetRecommendation, _Mapping]] = ..., shopping_add_age_group_recommendation: _Optional[_Union[Recommendation.ShoppingOfferAttributeRecommendation, _Mapping]] = ..., shopping_add_color_recommendation: _Optional[_Union[Recommendation.ShoppingOfferAttributeRecommendation, _Mapping]] = ..., shopping_add_gender_recommendation: _Optional[_Union[Recommendation.ShoppingOfferAttributeRecommendation, _Mapping]] = ..., shopping_add_gtin_recommendation: _Optional[_Union[Recommendation.ShoppingOfferAttributeRecommendation, _Mapping]] = ..., shopping_add_more_identifiers_recommendation: _Optional[_Union[Recommendation.ShoppingOfferAttributeRecommendation, _Mapping]] = ..., shopping_add_size_recommendation: _Optional[_Union[Recommendation.ShoppingOfferAttributeRecommendation, _Mapping]] = ..., shopping_add_products_to_campaign_recommendation: _Optional[_Union[Recommendation.ShoppingAddProductsToCampaignRecommendation, _Mapping]] = ..., shopping_fix_disapproved_products_recommendation: _Optional[_Union[Recommendation.ShoppingFixDisapprovedProductsRecommendation, _Mapping]] = ..., shopping_target_all_offers_recommendation: _Optional[_Union[Recommendation.ShoppingTargetAllOffersRecommendation, _Mapping]] = ..., shopping_fix_suspended_merchant_center_account_recommendation: _Optional[_Union[Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation, _Mapping]] = ..., shopping_fix_merchant_center_account_suspension_warning_recommendation: _Optional[_Union[Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation, _Mapping]] = ..., shopping_migrate_regular_shopping_campaign_offers_to_performance_max_recommendation: _Optional[_Union[Recommendation.ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation, _Mapping]] = ..., dynamic_image_extension_opt_in_recommendation: _Optional[_Union[Recommendation.DynamicImageExtensionOptInRecommendation, _Mapping]] = ..., raise_target_cpa_recommendation: _Optional[_Union[Recommendation.RaiseTargetCpaRecommendation, _Mapping]] = ..., lower_target_roas_recommendation: _Optional[_Union[Recommendation.LowerTargetRoasRecommendation, _Mapping]] = ..., performance_max_opt_in_recommendation: _Optional[_Union[Recommendation.PerformanceMaxOptInRecommendation, _Mapping]] = ..., improve_performance_max_ad_strength_recommendation: _Optional[_Union[Recommendation.ImprovePerformanceMaxAdStrengthRecommendation, _Mapping]] = ..., migrate_dynamic_search_ads_campaign_to_performance_max_recommendation: _Optional[_Union[Recommendation.MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation, _Mapping]] = ..., forecasting_set_target_cpa_recommendation: _Optional[_Union[Recommendation.ForecastingSetTargetCpaRecommendation, _Mapping]] = ..., set_target_cpa_recommendation: _Optional[_Union[Recommendation.ForecastingSetTargetCpaRecommendation, _Mapping]] = ..., set_target_roas_recommendation: _Optional[_Union[Recommendation.ForecastingSetTargetRoasRecommendation, _Mapping]] = ..., maximize_conversion_value_opt_in_recommendation: _Optional[_Union[Recommendation.MaximizeConversionValueOptInRecommendation, _Mapping]] = ..., improve_google_tag_coverage_recommendation: _Optional[_Union[Recommendation.ImproveGoogleTagCoverageRecommendation, _Mapping]] = ..., performance_max_final_url_opt_in_recommendation: _Optional[_Union[Recommendation.PerformanceMaxFinalUrlOptInRecommendation, _Mapping]] = ..., refresh_customer_match_list_recommendation: _Optional[_Union[Recommendation.RefreshCustomerMatchListRecommendation, _Mapping]] = ..., custom_audience_opt_in_recommendation: _Optional[_Union[Recommendation.CustomAudienceOptInRecommendation, _Mapping]] = ..., lead_form_asset_recommendation: _Optional[_Union[Recommendation.LeadFormAssetRecommendation, _Mapping]] = ..., improve_demand_gen_ad_strength_recommendation: _Optional[_Union[Recommendation.ImproveDemandGenAdStrengthRecommendation, _Mapping]] = ...) -> None: ...
