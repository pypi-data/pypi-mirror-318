from google.ads.googleads.v17.enums import ad_customizer_placeholder_field_pb2 as _ad_customizer_placeholder_field_pb2
from google.ads.googleads.v17.enums import affiliate_location_placeholder_field_pb2 as _affiliate_location_placeholder_field_pb2
from google.ads.googleads.v17.enums import app_placeholder_field_pb2 as _app_placeholder_field_pb2
from google.ads.googleads.v17.enums import call_placeholder_field_pb2 as _call_placeholder_field_pb2
from google.ads.googleads.v17.enums import callout_placeholder_field_pb2 as _callout_placeholder_field_pb2
from google.ads.googleads.v17.enums import custom_placeholder_field_pb2 as _custom_placeholder_field_pb2
from google.ads.googleads.v17.enums import dsa_page_feed_criterion_field_pb2 as _dsa_page_feed_criterion_field_pb2
from google.ads.googleads.v17.enums import education_placeholder_field_pb2 as _education_placeholder_field_pb2
from google.ads.googleads.v17.enums import feed_mapping_criterion_type_pb2 as _feed_mapping_criterion_type_pb2
from google.ads.googleads.v17.enums import feed_mapping_status_pb2 as _feed_mapping_status_pb2
from google.ads.googleads.v17.enums import flight_placeholder_field_pb2 as _flight_placeholder_field_pb2
from google.ads.googleads.v17.enums import hotel_placeholder_field_pb2 as _hotel_placeholder_field_pb2
from google.ads.googleads.v17.enums import image_placeholder_field_pb2 as _image_placeholder_field_pb2
from google.ads.googleads.v17.enums import job_placeholder_field_pb2 as _job_placeholder_field_pb2
from google.ads.googleads.v17.enums import local_placeholder_field_pb2 as _local_placeholder_field_pb2
from google.ads.googleads.v17.enums import location_extension_targeting_criterion_field_pb2 as _location_extension_targeting_criterion_field_pb2
from google.ads.googleads.v17.enums import location_placeholder_field_pb2 as _location_placeholder_field_pb2
from google.ads.googleads.v17.enums import message_placeholder_field_pb2 as _message_placeholder_field_pb2
from google.ads.googleads.v17.enums import placeholder_type_pb2 as _placeholder_type_pb2
from google.ads.googleads.v17.enums import price_placeholder_field_pb2 as _price_placeholder_field_pb2
from google.ads.googleads.v17.enums import promotion_placeholder_field_pb2 as _promotion_placeholder_field_pb2
from google.ads.googleads.v17.enums import real_estate_placeholder_field_pb2 as _real_estate_placeholder_field_pb2
from google.ads.googleads.v17.enums import sitelink_placeholder_field_pb2 as _sitelink_placeholder_field_pb2
from google.ads.googleads.v17.enums import structured_snippet_placeholder_field_pb2 as _structured_snippet_placeholder_field_pb2
from google.ads.googleads.v17.enums import travel_placeholder_field_pb2 as _travel_placeholder_field_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedMapping(_message.Message):
    __slots__ = ("resource_name", "feed", "attribute_field_mappings", "status", "placeholder_type", "criterion_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CRITERION_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    feed: str
    attribute_field_mappings: _containers.RepeatedCompositeFieldContainer[AttributeFieldMapping]
    status: _feed_mapping_status_pb2.FeedMappingStatusEnum.FeedMappingStatus
    placeholder_type: _placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType
    criterion_type: _feed_mapping_criterion_type_pb2.FeedMappingCriterionTypeEnum.FeedMappingCriterionType
    def __init__(self, resource_name: _Optional[str] = ..., feed: _Optional[str] = ..., attribute_field_mappings: _Optional[_Iterable[_Union[AttributeFieldMapping, _Mapping]]] = ..., status: _Optional[_Union[_feed_mapping_status_pb2.FeedMappingStatusEnum.FeedMappingStatus, str]] = ..., placeholder_type: _Optional[_Union[_placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType, str]] = ..., criterion_type: _Optional[_Union[_feed_mapping_criterion_type_pb2.FeedMappingCriterionTypeEnum.FeedMappingCriterionType, str]] = ...) -> None: ...

class AttributeFieldMapping(_message.Message):
    __slots__ = ("feed_attribute_id", "field_id", "sitelink_field", "call_field", "app_field", "location_field", "affiliate_location_field", "callout_field", "structured_snippet_field", "message_field", "price_field", "promotion_field", "ad_customizer_field", "dsa_page_feed_field", "location_extension_targeting_field", "education_field", "flight_field", "custom_field", "hotel_field", "real_estate_field", "travel_field", "local_field", "job_field", "image_field")
    FEED_ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    SITELINK_FIELD_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    AFFILIATE_LOCATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_SNIPPET_FIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_FIELD_FIELD_NUMBER: _ClassVar[int]
    AD_CUSTOMIZER_FIELD_FIELD_NUMBER: _ClassVar[int]
    DSA_PAGE_FEED_FIELD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_EXTENSION_TARGETING_FIELD_FIELD_NUMBER: _ClassVar[int]
    EDUCATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_FIELD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    HOTEL_FIELD_FIELD_NUMBER: _ClassVar[int]
    REAL_ESTATE_FIELD_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_FIELD_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    feed_attribute_id: int
    field_id: int
    sitelink_field: _sitelink_placeholder_field_pb2.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    call_field: _call_placeholder_field_pb2.CallPlaceholderFieldEnum.CallPlaceholderField
    app_field: _app_placeholder_field_pb2.AppPlaceholderFieldEnum.AppPlaceholderField
    location_field: _location_placeholder_field_pb2.LocationPlaceholderFieldEnum.LocationPlaceholderField
    affiliate_location_field: _affiliate_location_placeholder_field_pb2.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField
    callout_field: _callout_placeholder_field_pb2.CalloutPlaceholderFieldEnum.CalloutPlaceholderField
    structured_snippet_field: _structured_snippet_placeholder_field_pb2.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField
    message_field: _message_placeholder_field_pb2.MessagePlaceholderFieldEnum.MessagePlaceholderField
    price_field: _price_placeholder_field_pb2.PricePlaceholderFieldEnum.PricePlaceholderField
    promotion_field: _promotion_placeholder_field_pb2.PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    ad_customizer_field: _ad_customizer_placeholder_field_pb2.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    dsa_page_feed_field: _dsa_page_feed_criterion_field_pb2.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField
    location_extension_targeting_field: _location_extension_targeting_criterion_field_pb2.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    education_field: _education_placeholder_field_pb2.EducationPlaceholderFieldEnum.EducationPlaceholderField
    flight_field: _flight_placeholder_field_pb2.FlightPlaceholderFieldEnum.FlightPlaceholderField
    custom_field: _custom_placeholder_field_pb2.CustomPlaceholderFieldEnum.CustomPlaceholderField
    hotel_field: _hotel_placeholder_field_pb2.HotelPlaceholderFieldEnum.HotelPlaceholderField
    real_estate_field: _real_estate_placeholder_field_pb2.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField
    travel_field: _travel_placeholder_field_pb2.TravelPlaceholderFieldEnum.TravelPlaceholderField
    local_field: _local_placeholder_field_pb2.LocalPlaceholderFieldEnum.LocalPlaceholderField
    job_field: _job_placeholder_field_pb2.JobPlaceholderFieldEnum.JobPlaceholderField
    image_field: _image_placeholder_field_pb2.ImagePlaceholderFieldEnum.ImagePlaceholderField
    def __init__(self, feed_attribute_id: _Optional[int] = ..., field_id: _Optional[int] = ..., sitelink_field: _Optional[_Union[_sitelink_placeholder_field_pb2.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField, str]] = ..., call_field: _Optional[_Union[_call_placeholder_field_pb2.CallPlaceholderFieldEnum.CallPlaceholderField, str]] = ..., app_field: _Optional[_Union[_app_placeholder_field_pb2.AppPlaceholderFieldEnum.AppPlaceholderField, str]] = ..., location_field: _Optional[_Union[_location_placeholder_field_pb2.LocationPlaceholderFieldEnum.LocationPlaceholderField, str]] = ..., affiliate_location_field: _Optional[_Union[_affiliate_location_placeholder_field_pb2.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField, str]] = ..., callout_field: _Optional[_Union[_callout_placeholder_field_pb2.CalloutPlaceholderFieldEnum.CalloutPlaceholderField, str]] = ..., structured_snippet_field: _Optional[_Union[_structured_snippet_placeholder_field_pb2.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField, str]] = ..., message_field: _Optional[_Union[_message_placeholder_field_pb2.MessagePlaceholderFieldEnum.MessagePlaceholderField, str]] = ..., price_field: _Optional[_Union[_price_placeholder_field_pb2.PricePlaceholderFieldEnum.PricePlaceholderField, str]] = ..., promotion_field: _Optional[_Union[_promotion_placeholder_field_pb2.PromotionPlaceholderFieldEnum.PromotionPlaceholderField, str]] = ..., ad_customizer_field: _Optional[_Union[_ad_customizer_placeholder_field_pb2.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField, str]] = ..., dsa_page_feed_field: _Optional[_Union[_dsa_page_feed_criterion_field_pb2.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField, str]] = ..., location_extension_targeting_field: _Optional[_Union[_location_extension_targeting_criterion_field_pb2.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField, str]] = ..., education_field: _Optional[_Union[_education_placeholder_field_pb2.EducationPlaceholderFieldEnum.EducationPlaceholderField, str]] = ..., flight_field: _Optional[_Union[_flight_placeholder_field_pb2.FlightPlaceholderFieldEnum.FlightPlaceholderField, str]] = ..., custom_field: _Optional[_Union[_custom_placeholder_field_pb2.CustomPlaceholderFieldEnum.CustomPlaceholderField, str]] = ..., hotel_field: _Optional[_Union[_hotel_placeholder_field_pb2.HotelPlaceholderFieldEnum.HotelPlaceholderField, str]] = ..., real_estate_field: _Optional[_Union[_real_estate_placeholder_field_pb2.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField, str]] = ..., travel_field: _Optional[_Union[_travel_placeholder_field_pb2.TravelPlaceholderFieldEnum.TravelPlaceholderField, str]] = ..., local_field: _Optional[_Union[_local_placeholder_field_pb2.LocalPlaceholderFieldEnum.LocalPlaceholderField, str]] = ..., job_field: _Optional[_Union[_job_placeholder_field_pb2.JobPlaceholderFieldEnum.JobPlaceholderField, str]] = ..., image_field: _Optional[_Union[_image_placeholder_field_pb2.ImagePlaceholderFieldEnum.ImagePlaceholderField, str]] = ...) -> None: ...
