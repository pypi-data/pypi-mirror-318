from google.ads.googleads.v16.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v16.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v16.enums import ad_group_criterion_approval_status_pb2 as _ad_group_criterion_approval_status_pb2
from google.ads.googleads.v16.enums import ad_group_criterion_status_pb2 as _ad_group_criterion_status_pb2
from google.ads.googleads.v16.enums import bidding_source_pb2 as _bidding_source_pb2
from google.ads.googleads.v16.enums import criterion_system_serving_status_pb2 as _criterion_system_serving_status_pb2
from google.ads.googleads.v16.enums import criterion_type_pb2 as _criterion_type_pb2
from google.ads.googleads.v16.enums import quality_score_bucket_pb2 as _quality_score_bucket_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterion(_message.Message):
    __slots__ = ("resource_name", "criterion_id", "display_name", "status", "quality_info", "ad_group", "type", "negative", "system_serving_status", "approval_status", "disapproval_reasons", "labels", "bid_modifier", "cpc_bid_micros", "cpm_bid_micros", "cpv_bid_micros", "percent_cpc_bid_micros", "effective_cpc_bid_micros", "effective_cpm_bid_micros", "effective_cpv_bid_micros", "effective_percent_cpc_bid_micros", "effective_cpc_bid_source", "effective_cpm_bid_source", "effective_cpv_bid_source", "effective_percent_cpc_bid_source", "position_estimates", "final_urls", "final_mobile_urls", "final_url_suffix", "tracking_url_template", "url_custom_parameters", "keyword", "placement", "mobile_app_category", "mobile_application", "listing_group", "age_range", "gender", "income_range", "parental_status", "user_list", "youtube_video", "youtube_channel", "topic", "user_interest", "webpage", "app_payment_model", "custom_affinity", "custom_intent", "custom_audience", "combined_audience", "audience", "location", "language")
    class QualityInfo(_message.Message):
        __slots__ = ("quality_score", "creative_quality_score", "post_click_quality_score", "search_predicted_ctr")
        QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
        CREATIVE_QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
        POST_CLICK_QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
        SEARCH_PREDICTED_CTR_FIELD_NUMBER: _ClassVar[int]
        quality_score: int
        creative_quality_score: _quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket
        post_click_quality_score: _quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket
        search_predicted_ctr: _quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket
        def __init__(self, quality_score: _Optional[int] = ..., creative_quality_score: _Optional[_Union[_quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket, str]] = ..., post_click_quality_score: _Optional[_Union[_quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket, str]] = ..., search_predicted_ctr: _Optional[_Union[_quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket, str]] = ...) -> None: ...
    class PositionEstimates(_message.Message):
        __slots__ = ("first_page_cpc_micros", "first_position_cpc_micros", "top_of_page_cpc_micros", "estimated_add_clicks_at_first_position_cpc", "estimated_add_cost_at_first_position_cpc")
        FIRST_PAGE_CPC_MICROS_FIELD_NUMBER: _ClassVar[int]
        FIRST_POSITION_CPC_MICROS_FIELD_NUMBER: _ClassVar[int]
        TOP_OF_PAGE_CPC_MICROS_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_ADD_CLICKS_AT_FIRST_POSITION_CPC_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_ADD_COST_AT_FIRST_POSITION_CPC_FIELD_NUMBER: _ClassVar[int]
        first_page_cpc_micros: int
        first_position_cpc_micros: int
        top_of_page_cpc_micros: int
        estimated_add_clicks_at_first_position_cpc: int
        estimated_add_cost_at_first_position_cpc: int
        def __init__(self, first_page_cpc_micros: _Optional[int] = ..., first_position_cpc_micros: _Optional[int] = ..., top_of_page_cpc_micros: _Optional[int] = ..., estimated_add_clicks_at_first_position_cpc: _Optional[int] = ..., estimated_add_cost_at_first_position_cpc: _Optional[int] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_INFO_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SERVING_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISAPPROVAL_REASONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPM_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPV_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPM_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPV_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PERCENT_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPC_BID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPM_BID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPV_BID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PERCENT_CPC_BID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    POSITION_ESTIMATES_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    LISTING_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    INCOME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    USER_INTEREST_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_FIELD_NUMBER: _ClassVar[int]
    APP_PAYMENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_INTENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    COMBINED_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    criterion_id: int
    display_name: str
    status: _ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    quality_info: AdGroupCriterion.QualityInfo
    ad_group: str
    type: _criterion_type_pb2.CriterionTypeEnum.CriterionType
    negative: bool
    system_serving_status: _criterion_system_serving_status_pb2.CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    approval_status: _ad_group_criterion_approval_status_pb2.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    disapproval_reasons: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.RepeatedScalarFieldContainer[str]
    bid_modifier: float
    cpc_bid_micros: int
    cpm_bid_micros: int
    cpv_bid_micros: int
    percent_cpc_bid_micros: int
    effective_cpc_bid_micros: int
    effective_cpm_bid_micros: int
    effective_cpv_bid_micros: int
    effective_percent_cpc_bid_micros: int
    effective_cpc_bid_source: _bidding_source_pb2.BiddingSourceEnum.BiddingSource
    effective_cpm_bid_source: _bidding_source_pb2.BiddingSourceEnum.BiddingSource
    effective_cpv_bid_source: _bidding_source_pb2.BiddingSourceEnum.BiddingSource
    effective_percent_cpc_bid_source: _bidding_source_pb2.BiddingSourceEnum.BiddingSource
    position_estimates: AdGroupCriterion.PositionEstimates
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    final_url_suffix: str
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    keyword: _criteria_pb2.KeywordInfo
    placement: _criteria_pb2.PlacementInfo
    mobile_app_category: _criteria_pb2.MobileAppCategoryInfo
    mobile_application: _criteria_pb2.MobileApplicationInfo
    listing_group: _criteria_pb2.ListingGroupInfo
    age_range: _criteria_pb2.AgeRangeInfo
    gender: _criteria_pb2.GenderInfo
    income_range: _criteria_pb2.IncomeRangeInfo
    parental_status: _criteria_pb2.ParentalStatusInfo
    user_list: _criteria_pb2.UserListInfo
    youtube_video: _criteria_pb2.YouTubeVideoInfo
    youtube_channel: _criteria_pb2.YouTubeChannelInfo
    topic: _criteria_pb2.TopicInfo
    user_interest: _criteria_pb2.UserInterestInfo
    webpage: _criteria_pb2.WebpageInfo
    app_payment_model: _criteria_pb2.AppPaymentModelInfo
    custom_affinity: _criteria_pb2.CustomAffinityInfo
    custom_intent: _criteria_pb2.CustomIntentInfo
    custom_audience: _criteria_pb2.CustomAudienceInfo
    combined_audience: _criteria_pb2.CombinedAudienceInfo
    audience: _criteria_pb2.AudienceInfo
    location: _criteria_pb2.LocationInfo
    language: _criteria_pb2.LanguageInfo
    def __init__(self, resource_name: _Optional[str] = ..., criterion_id: _Optional[int] = ..., display_name: _Optional[str] = ..., status: _Optional[_Union[_ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus, str]] = ..., quality_info: _Optional[_Union[AdGroupCriterion.QualityInfo, _Mapping]] = ..., ad_group: _Optional[str] = ..., type: _Optional[_Union[_criterion_type_pb2.CriterionTypeEnum.CriterionType, str]] = ..., negative: bool = ..., system_serving_status: _Optional[_Union[_criterion_system_serving_status_pb2.CriterionSystemServingStatusEnum.CriterionSystemServingStatus, str]] = ..., approval_status: _Optional[_Union[_ad_group_criterion_approval_status_pb2.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus, str]] = ..., disapproval_reasons: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[str]] = ..., bid_modifier: _Optional[float] = ..., cpc_bid_micros: _Optional[int] = ..., cpm_bid_micros: _Optional[int] = ..., cpv_bid_micros: _Optional[int] = ..., percent_cpc_bid_micros: _Optional[int] = ..., effective_cpc_bid_micros: _Optional[int] = ..., effective_cpm_bid_micros: _Optional[int] = ..., effective_cpv_bid_micros: _Optional[int] = ..., effective_percent_cpc_bid_micros: _Optional[int] = ..., effective_cpc_bid_source: _Optional[_Union[_bidding_source_pb2.BiddingSourceEnum.BiddingSource, str]] = ..., effective_cpm_bid_source: _Optional[_Union[_bidding_source_pb2.BiddingSourceEnum.BiddingSource, str]] = ..., effective_cpv_bid_source: _Optional[_Union[_bidding_source_pb2.BiddingSourceEnum.BiddingSource, str]] = ..., effective_percent_cpc_bid_source: _Optional[_Union[_bidding_source_pb2.BiddingSourceEnum.BiddingSource, str]] = ..., position_estimates: _Optional[_Union[AdGroupCriterion.PositionEstimates, _Mapping]] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ..., final_url_suffix: _Optional[str] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., placement: _Optional[_Union[_criteria_pb2.PlacementInfo, _Mapping]] = ..., mobile_app_category: _Optional[_Union[_criteria_pb2.MobileAppCategoryInfo, _Mapping]] = ..., mobile_application: _Optional[_Union[_criteria_pb2.MobileApplicationInfo, _Mapping]] = ..., listing_group: _Optional[_Union[_criteria_pb2.ListingGroupInfo, _Mapping]] = ..., age_range: _Optional[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]] = ..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]] = ..., income_range: _Optional[_Union[_criteria_pb2.IncomeRangeInfo, _Mapping]] = ..., parental_status: _Optional[_Union[_criteria_pb2.ParentalStatusInfo, _Mapping]] = ..., user_list: _Optional[_Union[_criteria_pb2.UserListInfo, _Mapping]] = ..., youtube_video: _Optional[_Union[_criteria_pb2.YouTubeVideoInfo, _Mapping]] = ..., youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]] = ..., topic: _Optional[_Union[_criteria_pb2.TopicInfo, _Mapping]] = ..., user_interest: _Optional[_Union[_criteria_pb2.UserInterestInfo, _Mapping]] = ..., webpage: _Optional[_Union[_criteria_pb2.WebpageInfo, _Mapping]] = ..., app_payment_model: _Optional[_Union[_criteria_pb2.AppPaymentModelInfo, _Mapping]] = ..., custom_affinity: _Optional[_Union[_criteria_pb2.CustomAffinityInfo, _Mapping]] = ..., custom_intent: _Optional[_Union[_criteria_pb2.CustomIntentInfo, _Mapping]] = ..., custom_audience: _Optional[_Union[_criteria_pb2.CustomAudienceInfo, _Mapping]] = ..., combined_audience: _Optional[_Union[_criteria_pb2.CombinedAudienceInfo, _Mapping]] = ..., audience: _Optional[_Union[_criteria_pb2.AudienceInfo, _Mapping]] = ..., location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]] = ..., language: _Optional[_Union[_criteria_pb2.LanguageInfo, _Mapping]] = ...) -> None: ...
