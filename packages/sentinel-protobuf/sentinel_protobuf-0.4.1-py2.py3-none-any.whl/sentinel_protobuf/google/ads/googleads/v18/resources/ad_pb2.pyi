from google.ads.googleads.v18.common import ad_type_infos_pb2 as _ad_type_infos_pb2
from google.ads.googleads.v18.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v18.common import final_app_url_pb2 as _final_app_url_pb2
from google.ads.googleads.v18.common import url_collection_pb2 as _url_collection_pb2
from google.ads.googleads.v18.enums import ad_type_pb2 as _ad_type_pb2
from google.ads.googleads.v18.enums import device_pb2 as _device_pb2
from google.ads.googleads.v18.enums import system_managed_entity_source_pb2 as _system_managed_entity_source_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ad(_message.Message):
    __slots__ = ("resource_name", "id", "final_urls", "final_app_urls", "final_mobile_urls", "tracking_url_template", "final_url_suffix", "url_custom_parameters", "display_url", "type", "added_by_google_ads", "device_preference", "url_collections", "name", "system_managed_resource_source", "text_ad", "expanded_text_ad", "call_ad", "expanded_dynamic_search_ad", "hotel_ad", "shopping_smart_ad", "shopping_product_ad", "image_ad", "video_ad", "video_responsive_ad", "responsive_search_ad", "legacy_responsive_display_ad", "app_ad", "legacy_app_install_ad", "responsive_display_ad", "local_ad", "display_upload_ad", "app_engagement_ad", "shopping_comparison_listing_ad", "smart_campaign_ad", "app_pre_registration_ad", "demand_gen_multi_asset_ad", "demand_gen_carousel_ad", "demand_gen_video_responsive_ad", "demand_gen_product_ad", "travel_ad")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_APP_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDED_BY_GOOGLE_ADS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    URL_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MANAGED_RESOURCE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TEXT_AD_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_TEXT_AD_FIELD_NUMBER: _ClassVar[int]
    CALL_AD_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_DYNAMIC_SEARCH_AD_FIELD_NUMBER: _ClassVar[int]
    HOTEL_AD_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_SMART_AD_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_PRODUCT_AD_FIELD_NUMBER: _ClassVar[int]
    IMAGE_AD_FIELD_NUMBER: _ClassVar[int]
    VIDEO_AD_FIELD_NUMBER: _ClassVar[int]
    VIDEO_RESPONSIVE_AD_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_FIELD_NUMBER: _ClassVar[int]
    LEGACY_RESPONSIVE_DISPLAY_AD_FIELD_NUMBER: _ClassVar[int]
    APP_AD_FIELD_NUMBER: _ClassVar[int]
    LEGACY_APP_INSTALL_AD_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_DISPLAY_AD_FIELD_NUMBER: _ClassVar[int]
    LOCAL_AD_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_UPLOAD_AD_FIELD_NUMBER: _ClassVar[int]
    APP_ENGAGEMENT_AD_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_COMPARISON_LISTING_AD_FIELD_NUMBER: _ClassVar[int]
    SMART_CAMPAIGN_AD_FIELD_NUMBER: _ClassVar[int]
    APP_PRE_REGISTRATION_AD_FIELD_NUMBER: _ClassVar[int]
    DEMAND_GEN_MULTI_ASSET_AD_FIELD_NUMBER: _ClassVar[int]
    DEMAND_GEN_CAROUSEL_AD_FIELD_NUMBER: _ClassVar[int]
    DEMAND_GEN_VIDEO_RESPONSIVE_AD_FIELD_NUMBER: _ClassVar[int]
    DEMAND_GEN_PRODUCT_AD_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_AD_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_app_urls: _containers.RepeatedCompositeFieldContainer[_final_app_url_pb2.FinalAppUrl]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    final_url_suffix: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    display_url: str
    type: _ad_type_pb2.AdTypeEnum.AdType
    added_by_google_ads: bool
    device_preference: _device_pb2.DeviceEnum.Device
    url_collections: _containers.RepeatedCompositeFieldContainer[_url_collection_pb2.UrlCollection]
    name: str
    system_managed_resource_source: _system_managed_entity_source_pb2.SystemManagedResourceSourceEnum.SystemManagedResourceSource
    text_ad: _ad_type_infos_pb2.TextAdInfo
    expanded_text_ad: _ad_type_infos_pb2.ExpandedTextAdInfo
    call_ad: _ad_type_infos_pb2.CallAdInfo
    expanded_dynamic_search_ad: _ad_type_infos_pb2.ExpandedDynamicSearchAdInfo
    hotel_ad: _ad_type_infos_pb2.HotelAdInfo
    shopping_smart_ad: _ad_type_infos_pb2.ShoppingSmartAdInfo
    shopping_product_ad: _ad_type_infos_pb2.ShoppingProductAdInfo
    image_ad: _ad_type_infos_pb2.ImageAdInfo
    video_ad: _ad_type_infos_pb2.VideoAdInfo
    video_responsive_ad: _ad_type_infos_pb2.VideoResponsiveAdInfo
    responsive_search_ad: _ad_type_infos_pb2.ResponsiveSearchAdInfo
    legacy_responsive_display_ad: _ad_type_infos_pb2.LegacyResponsiveDisplayAdInfo
    app_ad: _ad_type_infos_pb2.AppAdInfo
    legacy_app_install_ad: _ad_type_infos_pb2.LegacyAppInstallAdInfo
    responsive_display_ad: _ad_type_infos_pb2.ResponsiveDisplayAdInfo
    local_ad: _ad_type_infos_pb2.LocalAdInfo
    display_upload_ad: _ad_type_infos_pb2.DisplayUploadAdInfo
    app_engagement_ad: _ad_type_infos_pb2.AppEngagementAdInfo
    shopping_comparison_listing_ad: _ad_type_infos_pb2.ShoppingComparisonListingAdInfo
    smart_campaign_ad: _ad_type_infos_pb2.SmartCampaignAdInfo
    app_pre_registration_ad: _ad_type_infos_pb2.AppPreRegistrationAdInfo
    demand_gen_multi_asset_ad: _ad_type_infos_pb2.DemandGenMultiAssetAdInfo
    demand_gen_carousel_ad: _ad_type_infos_pb2.DemandGenCarouselAdInfo
    demand_gen_video_responsive_ad: _ad_type_infos_pb2.DemandGenVideoResponsiveAdInfo
    demand_gen_product_ad: _ad_type_infos_pb2.DemandGenProductAdInfo
    travel_ad: _ad_type_infos_pb2.TravelAdInfo
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_app_urls: _Optional[_Iterable[_Union[_final_app_url_pb2.FinalAppUrl, _Mapping]]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ..., tracking_url_template: _Optional[str] = ..., final_url_suffix: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., display_url: _Optional[str] = ..., type: _Optional[_Union[_ad_type_pb2.AdTypeEnum.AdType, str]] = ..., added_by_google_ads: bool = ..., device_preference: _Optional[_Union[_device_pb2.DeviceEnum.Device, str]] = ..., url_collections: _Optional[_Iterable[_Union[_url_collection_pb2.UrlCollection, _Mapping]]] = ..., name: _Optional[str] = ..., system_managed_resource_source: _Optional[_Union[_system_managed_entity_source_pb2.SystemManagedResourceSourceEnum.SystemManagedResourceSource, str]] = ..., text_ad: _Optional[_Union[_ad_type_infos_pb2.TextAdInfo, _Mapping]] = ..., expanded_text_ad: _Optional[_Union[_ad_type_infos_pb2.ExpandedTextAdInfo, _Mapping]] = ..., call_ad: _Optional[_Union[_ad_type_infos_pb2.CallAdInfo, _Mapping]] = ..., expanded_dynamic_search_ad: _Optional[_Union[_ad_type_infos_pb2.ExpandedDynamicSearchAdInfo, _Mapping]] = ..., hotel_ad: _Optional[_Union[_ad_type_infos_pb2.HotelAdInfo, _Mapping]] = ..., shopping_smart_ad: _Optional[_Union[_ad_type_infos_pb2.ShoppingSmartAdInfo, _Mapping]] = ..., shopping_product_ad: _Optional[_Union[_ad_type_infos_pb2.ShoppingProductAdInfo, _Mapping]] = ..., image_ad: _Optional[_Union[_ad_type_infos_pb2.ImageAdInfo, _Mapping]] = ..., video_ad: _Optional[_Union[_ad_type_infos_pb2.VideoAdInfo, _Mapping]] = ..., video_responsive_ad: _Optional[_Union[_ad_type_infos_pb2.VideoResponsiveAdInfo, _Mapping]] = ..., responsive_search_ad: _Optional[_Union[_ad_type_infos_pb2.ResponsiveSearchAdInfo, _Mapping]] = ..., legacy_responsive_display_ad: _Optional[_Union[_ad_type_infos_pb2.LegacyResponsiveDisplayAdInfo, _Mapping]] = ..., app_ad: _Optional[_Union[_ad_type_infos_pb2.AppAdInfo, _Mapping]] = ..., legacy_app_install_ad: _Optional[_Union[_ad_type_infos_pb2.LegacyAppInstallAdInfo, _Mapping]] = ..., responsive_display_ad: _Optional[_Union[_ad_type_infos_pb2.ResponsiveDisplayAdInfo, _Mapping]] = ..., local_ad: _Optional[_Union[_ad_type_infos_pb2.LocalAdInfo, _Mapping]] = ..., display_upload_ad: _Optional[_Union[_ad_type_infos_pb2.DisplayUploadAdInfo, _Mapping]] = ..., app_engagement_ad: _Optional[_Union[_ad_type_infos_pb2.AppEngagementAdInfo, _Mapping]] = ..., shopping_comparison_listing_ad: _Optional[_Union[_ad_type_infos_pb2.ShoppingComparisonListingAdInfo, _Mapping]] = ..., smart_campaign_ad: _Optional[_Union[_ad_type_infos_pb2.SmartCampaignAdInfo, _Mapping]] = ..., app_pre_registration_ad: _Optional[_Union[_ad_type_infos_pb2.AppPreRegistrationAdInfo, _Mapping]] = ..., demand_gen_multi_asset_ad: _Optional[_Union[_ad_type_infos_pb2.DemandGenMultiAssetAdInfo, _Mapping]] = ..., demand_gen_carousel_ad: _Optional[_Union[_ad_type_infos_pb2.DemandGenCarouselAdInfo, _Mapping]] = ..., demand_gen_video_responsive_ad: _Optional[_Union[_ad_type_infos_pb2.DemandGenVideoResponsiveAdInfo, _Mapping]] = ..., demand_gen_product_ad: _Optional[_Union[_ad_type_infos_pb2.DemandGenProductAdInfo, _Mapping]] = ..., travel_ad: _Optional[_Union[_ad_type_infos_pb2.TravelAdInfo, _Mapping]] = ...) -> None: ...
