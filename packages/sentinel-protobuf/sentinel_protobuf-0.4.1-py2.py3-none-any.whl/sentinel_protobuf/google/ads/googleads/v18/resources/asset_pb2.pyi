from google.ads.googleads.v18.common import asset_types_pb2 as _asset_types_pb2
from google.ads.googleads.v18.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v18.common import policy_pb2 as _policy_pb2
from google.ads.googleads.v18.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v18.enums import asset_source_pb2 as _asset_source_pb2
from google.ads.googleads.v18.enums import asset_type_pb2 as _asset_type_pb2
from google.ads.googleads.v18.enums import policy_approval_status_pb2 as _policy_approval_status_pb2
from google.ads.googleads.v18.enums import policy_review_status_pb2 as _policy_review_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Asset(_message.Message):
    __slots__ = ("resource_name", "id", "name", "type", "final_urls", "final_mobile_urls", "tracking_url_template", "url_custom_parameters", "final_url_suffix", "source", "policy_summary", "field_type_policy_summaries", "youtube_video_asset", "media_bundle_asset", "image_asset", "text_asset", "lead_form_asset", "book_on_google_asset", "promotion_asset", "callout_asset", "structured_snippet_asset", "sitelink_asset", "page_feed_asset", "dynamic_education_asset", "mobile_app_asset", "hotel_callout_asset", "call_asset", "price_asset", "call_to_action_asset", "dynamic_real_estate_asset", "dynamic_custom_asset", "dynamic_hotels_and_rentals_asset", "dynamic_flights_asset", "demand_gen_carousel_card_asset", "dynamic_travel_asset", "dynamic_local_asset", "dynamic_jobs_asset", "location_asset", "hotel_property_asset")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_POLICY_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_ASSET_FIELD_NUMBER: _ClassVar[int]
    MEDIA_BUNDLE_ASSET_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    TEXT_ASSET_FIELD_NUMBER: _ClassVar[int]
    LEAD_FORM_ASSET_FIELD_NUMBER: _ClassVar[int]
    BOOK_ON_GOOGLE_ASSET_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_ASSET_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_ASSET_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_SNIPPET_ASSET_FIELD_NUMBER: _ClassVar[int]
    SITELINK_ASSET_FIELD_NUMBER: _ClassVar[int]
    PAGE_FEED_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_EDUCATION_ASSET_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_ASSET_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CALLOUT_ASSET_FIELD_NUMBER: _ClassVar[int]
    CALL_ASSET_FIELD_NUMBER: _ClassVar[int]
    PRICE_ASSET_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_REAL_ESTATE_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CUSTOM_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_HOTELS_AND_RENTALS_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FLIGHTS_ASSET_FIELD_NUMBER: _ClassVar[int]
    DEMAND_GEN_CAROUSEL_CARD_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_TRAVEL_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_LOCAL_ASSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_JOBS_ASSET_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ASSET_FIELD_NUMBER: _ClassVar[int]
    HOTEL_PROPERTY_ASSET_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    type: _asset_type_pb2.AssetTypeEnum.AssetType
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    final_url_suffix: str
    source: _asset_source_pb2.AssetSourceEnum.AssetSource
    policy_summary: AssetPolicySummary
    field_type_policy_summaries: _containers.RepeatedCompositeFieldContainer[AssetFieldTypePolicySummary]
    youtube_video_asset: _asset_types_pb2.YoutubeVideoAsset
    media_bundle_asset: _asset_types_pb2.MediaBundleAsset
    image_asset: _asset_types_pb2.ImageAsset
    text_asset: _asset_types_pb2.TextAsset
    lead_form_asset: _asset_types_pb2.LeadFormAsset
    book_on_google_asset: _asset_types_pb2.BookOnGoogleAsset
    promotion_asset: _asset_types_pb2.PromotionAsset
    callout_asset: _asset_types_pb2.CalloutAsset
    structured_snippet_asset: _asset_types_pb2.StructuredSnippetAsset
    sitelink_asset: _asset_types_pb2.SitelinkAsset
    page_feed_asset: _asset_types_pb2.PageFeedAsset
    dynamic_education_asset: _asset_types_pb2.DynamicEducationAsset
    mobile_app_asset: _asset_types_pb2.MobileAppAsset
    hotel_callout_asset: _asset_types_pb2.HotelCalloutAsset
    call_asset: _asset_types_pb2.CallAsset
    price_asset: _asset_types_pb2.PriceAsset
    call_to_action_asset: _asset_types_pb2.CallToActionAsset
    dynamic_real_estate_asset: _asset_types_pb2.DynamicRealEstateAsset
    dynamic_custom_asset: _asset_types_pb2.DynamicCustomAsset
    dynamic_hotels_and_rentals_asset: _asset_types_pb2.DynamicHotelsAndRentalsAsset
    dynamic_flights_asset: _asset_types_pb2.DynamicFlightsAsset
    demand_gen_carousel_card_asset: _asset_types_pb2.DemandGenCarouselCardAsset
    dynamic_travel_asset: _asset_types_pb2.DynamicTravelAsset
    dynamic_local_asset: _asset_types_pb2.DynamicLocalAsset
    dynamic_jobs_asset: _asset_types_pb2.DynamicJobsAsset
    location_asset: _asset_types_pb2.LocationAsset
    hotel_property_asset: _asset_types_pb2.HotelPropertyAsset
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_asset_type_pb2.AssetTypeEnum.AssetType, str]] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., final_url_suffix: _Optional[str] = ..., source: _Optional[_Union[_asset_source_pb2.AssetSourceEnum.AssetSource, str]] = ..., policy_summary: _Optional[_Union[AssetPolicySummary, _Mapping]] = ..., field_type_policy_summaries: _Optional[_Iterable[_Union[AssetFieldTypePolicySummary, _Mapping]]] = ..., youtube_video_asset: _Optional[_Union[_asset_types_pb2.YoutubeVideoAsset, _Mapping]] = ..., media_bundle_asset: _Optional[_Union[_asset_types_pb2.MediaBundleAsset, _Mapping]] = ..., image_asset: _Optional[_Union[_asset_types_pb2.ImageAsset, _Mapping]] = ..., text_asset: _Optional[_Union[_asset_types_pb2.TextAsset, _Mapping]] = ..., lead_form_asset: _Optional[_Union[_asset_types_pb2.LeadFormAsset, _Mapping]] = ..., book_on_google_asset: _Optional[_Union[_asset_types_pb2.BookOnGoogleAsset, _Mapping]] = ..., promotion_asset: _Optional[_Union[_asset_types_pb2.PromotionAsset, _Mapping]] = ..., callout_asset: _Optional[_Union[_asset_types_pb2.CalloutAsset, _Mapping]] = ..., structured_snippet_asset: _Optional[_Union[_asset_types_pb2.StructuredSnippetAsset, _Mapping]] = ..., sitelink_asset: _Optional[_Union[_asset_types_pb2.SitelinkAsset, _Mapping]] = ..., page_feed_asset: _Optional[_Union[_asset_types_pb2.PageFeedAsset, _Mapping]] = ..., dynamic_education_asset: _Optional[_Union[_asset_types_pb2.DynamicEducationAsset, _Mapping]] = ..., mobile_app_asset: _Optional[_Union[_asset_types_pb2.MobileAppAsset, _Mapping]] = ..., hotel_callout_asset: _Optional[_Union[_asset_types_pb2.HotelCalloutAsset, _Mapping]] = ..., call_asset: _Optional[_Union[_asset_types_pb2.CallAsset, _Mapping]] = ..., price_asset: _Optional[_Union[_asset_types_pb2.PriceAsset, _Mapping]] = ..., call_to_action_asset: _Optional[_Union[_asset_types_pb2.CallToActionAsset, _Mapping]] = ..., dynamic_real_estate_asset: _Optional[_Union[_asset_types_pb2.DynamicRealEstateAsset, _Mapping]] = ..., dynamic_custom_asset: _Optional[_Union[_asset_types_pb2.DynamicCustomAsset, _Mapping]] = ..., dynamic_hotels_and_rentals_asset: _Optional[_Union[_asset_types_pb2.DynamicHotelsAndRentalsAsset, _Mapping]] = ..., dynamic_flights_asset: _Optional[_Union[_asset_types_pb2.DynamicFlightsAsset, _Mapping]] = ..., demand_gen_carousel_card_asset: _Optional[_Union[_asset_types_pb2.DemandGenCarouselCardAsset, _Mapping]] = ..., dynamic_travel_asset: _Optional[_Union[_asset_types_pb2.DynamicTravelAsset, _Mapping]] = ..., dynamic_local_asset: _Optional[_Union[_asset_types_pb2.DynamicLocalAsset, _Mapping]] = ..., dynamic_jobs_asset: _Optional[_Union[_asset_types_pb2.DynamicJobsAsset, _Mapping]] = ..., location_asset: _Optional[_Union[_asset_types_pb2.LocationAsset, _Mapping]] = ..., hotel_property_asset: _Optional[_Union[_asset_types_pb2.HotelPropertyAsset, _Mapping]] = ...) -> None: ...

class AssetFieldTypePolicySummary(_message.Message):
    __slots__ = ("asset_field_type", "asset_source", "policy_summary_info")
    ASSET_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SOURCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_SUMMARY_INFO_FIELD_NUMBER: _ClassVar[int]
    asset_field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType
    asset_source: _asset_source_pb2.AssetSourceEnum.AssetSource
    policy_summary_info: AssetPolicySummary
    def __init__(self, asset_field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]] = ..., asset_source: _Optional[_Union[_asset_source_pb2.AssetSourceEnum.AssetSource, str]] = ..., policy_summary_info: _Optional[_Union[AssetPolicySummary, _Mapping]] = ...) -> None: ...

class AssetPolicySummary(_message.Message):
    __slots__ = ("policy_topic_entries", "review_status", "approval_status")
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    policy_topic_entries: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyTopicEntry]
    review_status: _policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: _policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(self, policy_topic_entries: _Optional[_Iterable[_Union[_policy_pb2.PolicyTopicEntry, _Mapping]]] = ..., review_status: _Optional[_Union[_policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus, str]] = ..., approval_status: _Optional[_Union[_policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus, str]] = ...) -> None: ...
