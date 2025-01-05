from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v17.enums import campaign_criterion_status_pb2 as _campaign_criterion_status_pb2
from google.ads.googleads.v17.enums import criterion_type_pb2 as _criterion_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignCriterion(_message.Message):
    __slots__ = ("resource_name", "campaign", "criterion_id", "display_name", "bid_modifier", "negative", "type", "status", "keyword", "placement", "mobile_app_category", "mobile_application", "location", "device", "ad_schedule", "age_range", "gender", "income_range", "parental_status", "user_list", "youtube_video", "youtube_channel", "proximity", "topic", "listing_scope", "language", "ip_block", "content_label", "carrier", "user_interest", "webpage", "operating_system_version", "mobile_device", "location_group", "custom_affinity", "custom_audience", "combined_audience", "keyword_theme", "local_service_id", "brand_list")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    INCOME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    LISTING_SCOPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    IP_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LABEL_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    USER_INTEREST_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_VERSION_FIELD_NUMBER: _ClassVar[int]
    MOBILE_DEVICE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_GROUP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    COMBINED_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_THEME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    BRAND_LIST_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    criterion_id: int
    display_name: str
    bid_modifier: float
    negative: bool
    type: _criterion_type_pb2.CriterionTypeEnum.CriterionType
    status: _campaign_criterion_status_pb2.CampaignCriterionStatusEnum.CampaignCriterionStatus
    keyword: _criteria_pb2.KeywordInfo
    placement: _criteria_pb2.PlacementInfo
    mobile_app_category: _criteria_pb2.MobileAppCategoryInfo
    mobile_application: _criteria_pb2.MobileApplicationInfo
    location: _criteria_pb2.LocationInfo
    device: _criteria_pb2.DeviceInfo
    ad_schedule: _criteria_pb2.AdScheduleInfo
    age_range: _criteria_pb2.AgeRangeInfo
    gender: _criteria_pb2.GenderInfo
    income_range: _criteria_pb2.IncomeRangeInfo
    parental_status: _criteria_pb2.ParentalStatusInfo
    user_list: _criteria_pb2.UserListInfo
    youtube_video: _criteria_pb2.YouTubeVideoInfo
    youtube_channel: _criteria_pb2.YouTubeChannelInfo
    proximity: _criteria_pb2.ProximityInfo
    topic: _criteria_pb2.TopicInfo
    listing_scope: _criteria_pb2.ListingScopeInfo
    language: _criteria_pb2.LanguageInfo
    ip_block: _criteria_pb2.IpBlockInfo
    content_label: _criteria_pb2.ContentLabelInfo
    carrier: _criteria_pb2.CarrierInfo
    user_interest: _criteria_pb2.UserInterestInfo
    webpage: _criteria_pb2.WebpageInfo
    operating_system_version: _criteria_pb2.OperatingSystemVersionInfo
    mobile_device: _criteria_pb2.MobileDeviceInfo
    location_group: _criteria_pb2.LocationGroupInfo
    custom_affinity: _criteria_pb2.CustomAffinityInfo
    custom_audience: _criteria_pb2.CustomAudienceInfo
    combined_audience: _criteria_pb2.CombinedAudienceInfo
    keyword_theme: _criteria_pb2.KeywordThemeInfo
    local_service_id: _criteria_pb2.LocalServiceIdInfo
    brand_list: _criteria_pb2.BrandListInfo
    def __init__(self, resource_name: _Optional[str] = ..., campaign: _Optional[str] = ..., criterion_id: _Optional[int] = ..., display_name: _Optional[str] = ..., bid_modifier: _Optional[float] = ..., negative: bool = ..., type: _Optional[_Union[_criterion_type_pb2.CriterionTypeEnum.CriterionType, str]] = ..., status: _Optional[_Union[_campaign_criterion_status_pb2.CampaignCriterionStatusEnum.CampaignCriterionStatus, str]] = ..., keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., placement: _Optional[_Union[_criteria_pb2.PlacementInfo, _Mapping]] = ..., mobile_app_category: _Optional[_Union[_criteria_pb2.MobileAppCategoryInfo, _Mapping]] = ..., mobile_application: _Optional[_Union[_criteria_pb2.MobileApplicationInfo, _Mapping]] = ..., location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]] = ..., device: _Optional[_Union[_criteria_pb2.DeviceInfo, _Mapping]] = ..., ad_schedule: _Optional[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]] = ..., age_range: _Optional[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]] = ..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]] = ..., income_range: _Optional[_Union[_criteria_pb2.IncomeRangeInfo, _Mapping]] = ..., parental_status: _Optional[_Union[_criteria_pb2.ParentalStatusInfo, _Mapping]] = ..., user_list: _Optional[_Union[_criteria_pb2.UserListInfo, _Mapping]] = ..., youtube_video: _Optional[_Union[_criteria_pb2.YouTubeVideoInfo, _Mapping]] = ..., youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]] = ..., proximity: _Optional[_Union[_criteria_pb2.ProximityInfo, _Mapping]] = ..., topic: _Optional[_Union[_criteria_pb2.TopicInfo, _Mapping]] = ..., listing_scope: _Optional[_Union[_criteria_pb2.ListingScopeInfo, _Mapping]] = ..., language: _Optional[_Union[_criteria_pb2.LanguageInfo, _Mapping]] = ..., ip_block: _Optional[_Union[_criteria_pb2.IpBlockInfo, _Mapping]] = ..., content_label: _Optional[_Union[_criteria_pb2.ContentLabelInfo, _Mapping]] = ..., carrier: _Optional[_Union[_criteria_pb2.CarrierInfo, _Mapping]] = ..., user_interest: _Optional[_Union[_criteria_pb2.UserInterestInfo, _Mapping]] = ..., webpage: _Optional[_Union[_criteria_pb2.WebpageInfo, _Mapping]] = ..., operating_system_version: _Optional[_Union[_criteria_pb2.OperatingSystemVersionInfo, _Mapping]] = ..., mobile_device: _Optional[_Union[_criteria_pb2.MobileDeviceInfo, _Mapping]] = ..., location_group: _Optional[_Union[_criteria_pb2.LocationGroupInfo, _Mapping]] = ..., custom_affinity: _Optional[_Union[_criteria_pb2.CustomAffinityInfo, _Mapping]] = ..., custom_audience: _Optional[_Union[_criteria_pb2.CustomAudienceInfo, _Mapping]] = ..., combined_audience: _Optional[_Union[_criteria_pb2.CombinedAudienceInfo, _Mapping]] = ..., keyword_theme: _Optional[_Union[_criteria_pb2.KeywordThemeInfo, _Mapping]] = ..., local_service_id: _Optional[_Union[_criteria_pb2.LocalServiceIdInfo, _Mapping]] = ..., brand_list: _Optional[_Union[_criteria_pb2.BrandListInfo, _Mapping]] = ...) -> None: ...
