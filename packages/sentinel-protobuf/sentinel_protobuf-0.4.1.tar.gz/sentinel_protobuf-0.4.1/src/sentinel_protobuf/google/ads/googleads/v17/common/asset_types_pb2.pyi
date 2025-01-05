from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v17.common import feed_common_pb2 as _feed_common_pb2
from google.ads.googleads.v17.enums import call_conversion_reporting_state_pb2 as _call_conversion_reporting_state_pb2
from google.ads.googleads.v17.enums import call_to_action_type_pb2 as _call_to_action_type_pb2
from google.ads.googleads.v17.enums import lead_form_call_to_action_type_pb2 as _lead_form_call_to_action_type_pb2
from google.ads.googleads.v17.enums import lead_form_desired_intent_pb2 as _lead_form_desired_intent_pb2
from google.ads.googleads.v17.enums import lead_form_field_user_input_type_pb2 as _lead_form_field_user_input_type_pb2
from google.ads.googleads.v17.enums import lead_form_post_submit_call_to_action_type_pb2 as _lead_form_post_submit_call_to_action_type_pb2
from google.ads.googleads.v17.enums import location_ownership_type_pb2 as _location_ownership_type_pb2
from google.ads.googleads.v17.enums import mime_type_pb2 as _mime_type_pb2
from google.ads.googleads.v17.enums import mobile_app_vendor_pb2 as _mobile_app_vendor_pb2
from google.ads.googleads.v17.enums import price_extension_price_qualifier_pb2 as _price_extension_price_qualifier_pb2
from google.ads.googleads.v17.enums import price_extension_price_unit_pb2 as _price_extension_price_unit_pb2
from google.ads.googleads.v17.enums import price_extension_type_pb2 as _price_extension_type_pb2
from google.ads.googleads.v17.enums import promotion_extension_discount_modifier_pb2 as _promotion_extension_discount_modifier_pb2
from google.ads.googleads.v17.enums import promotion_extension_occasion_pb2 as _promotion_extension_occasion_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class YoutubeVideoAsset(_message.Message):
    __slots__ = ("youtube_video_id", "youtube_video_title")
    YOUTUBE_VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_TITLE_FIELD_NUMBER: _ClassVar[int]
    youtube_video_id: str
    youtube_video_title: str
    def __init__(self, youtube_video_id: _Optional[str] = ..., youtube_video_title: _Optional[str] = ...) -> None: ...

class MediaBundleAsset(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class ImageAsset(_message.Message):
    __slots__ = ("data", "file_size", "mime_type", "full_size")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FULL_SIZE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    file_size: int
    mime_type: _mime_type_pb2.MimeTypeEnum.MimeType
    full_size: ImageDimension
    def __init__(self, data: _Optional[bytes] = ..., file_size: _Optional[int] = ..., mime_type: _Optional[_Union[_mime_type_pb2.MimeTypeEnum.MimeType, str]] = ..., full_size: _Optional[_Union[ImageDimension, _Mapping]] = ...) -> None: ...

class ImageDimension(_message.Message):
    __slots__ = ("height_pixels", "width_pixels", "url")
    HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    height_pixels: int
    width_pixels: int
    url: str
    def __init__(self, height_pixels: _Optional[int] = ..., width_pixels: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class TextAsset(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class LeadFormAsset(_message.Message):
    __slots__ = ("business_name", "call_to_action_type", "call_to_action_description", "headline", "description", "privacy_policy_url", "post_submit_headline", "post_submit_description", "fields", "custom_question_fields", "delivery_methods", "post_submit_call_to_action_type", "background_image_asset", "desired_intent", "custom_disclosure")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_URL_FIELD_NUMBER: _ClassVar[int]
    POST_SUBMIT_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    POST_SUBMIT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_QUESTION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHODS_FIELD_NUMBER: _ClassVar[int]
    POST_SUBMIT_CALL_TO_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    DESIRED_INTENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DISCLOSURE_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    call_to_action_type: _lead_form_call_to_action_type_pb2.LeadFormCallToActionTypeEnum.LeadFormCallToActionType
    call_to_action_description: str
    headline: str
    description: str
    privacy_policy_url: str
    post_submit_headline: str
    post_submit_description: str
    fields: _containers.RepeatedCompositeFieldContainer[LeadFormField]
    custom_question_fields: _containers.RepeatedCompositeFieldContainer[LeadFormCustomQuestionField]
    delivery_methods: _containers.RepeatedCompositeFieldContainer[LeadFormDeliveryMethod]
    post_submit_call_to_action_type: _lead_form_post_submit_call_to_action_type_pb2.LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    background_image_asset: str
    desired_intent: _lead_form_desired_intent_pb2.LeadFormDesiredIntentEnum.LeadFormDesiredIntent
    custom_disclosure: str
    def __init__(self, business_name: _Optional[str] = ..., call_to_action_type: _Optional[_Union[_lead_form_call_to_action_type_pb2.LeadFormCallToActionTypeEnum.LeadFormCallToActionType, str]] = ..., call_to_action_description: _Optional[str] = ..., headline: _Optional[str] = ..., description: _Optional[str] = ..., privacy_policy_url: _Optional[str] = ..., post_submit_headline: _Optional[str] = ..., post_submit_description: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[LeadFormField, _Mapping]]] = ..., custom_question_fields: _Optional[_Iterable[_Union[LeadFormCustomQuestionField, _Mapping]]] = ..., delivery_methods: _Optional[_Iterable[_Union[LeadFormDeliveryMethod, _Mapping]]] = ..., post_submit_call_to_action_type: _Optional[_Union[_lead_form_post_submit_call_to_action_type_pb2.LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType, str]] = ..., background_image_asset: _Optional[str] = ..., desired_intent: _Optional[_Union[_lead_form_desired_intent_pb2.LeadFormDesiredIntentEnum.LeadFormDesiredIntent, str]] = ..., custom_disclosure: _Optional[str] = ...) -> None: ...

class LeadFormField(_message.Message):
    __slots__ = ("input_type", "single_choice_answers", "has_location_answer")
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_CHOICE_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    HAS_LOCATION_ANSWER_FIELD_NUMBER: _ClassVar[int]
    input_type: _lead_form_field_user_input_type_pb2.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool
    def __init__(self, input_type: _Optional[_Union[_lead_form_field_user_input_type_pb2.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType, str]] = ..., single_choice_answers: _Optional[_Union[LeadFormSingleChoiceAnswers, _Mapping]] = ..., has_location_answer: bool = ...) -> None: ...

class LeadFormCustomQuestionField(_message.Message):
    __slots__ = ("custom_question_text", "single_choice_answers", "has_location_answer")
    CUSTOM_QUESTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    SINGLE_CHOICE_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    HAS_LOCATION_ANSWER_FIELD_NUMBER: _ClassVar[int]
    custom_question_text: str
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool
    def __init__(self, custom_question_text: _Optional[str] = ..., single_choice_answers: _Optional[_Union[LeadFormSingleChoiceAnswers, _Mapping]] = ..., has_location_answer: bool = ...) -> None: ...

class LeadFormSingleChoiceAnswers(_message.Message):
    __slots__ = ("answers",)
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    answers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, answers: _Optional[_Iterable[str]] = ...) -> None: ...

class LeadFormDeliveryMethod(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: WebhookDelivery
    def __init__(self, webhook: _Optional[_Union[WebhookDelivery, _Mapping]] = ...) -> None: ...

class WebhookDelivery(_message.Message):
    __slots__ = ("advertiser_webhook_url", "google_secret", "payload_schema_version")
    ADVERTISER_WEBHOOK_URL_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SECRET_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    advertiser_webhook_url: str
    google_secret: str
    payload_schema_version: int
    def __init__(self, advertiser_webhook_url: _Optional[str] = ..., google_secret: _Optional[str] = ..., payload_schema_version: _Optional[int] = ...) -> None: ...

class BookOnGoogleAsset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PromotionAsset(_message.Message):
    __slots__ = ("promotion_target", "discount_modifier", "redemption_start_date", "redemption_end_date", "occasion", "language_code", "start_date", "end_date", "ad_schedule_targets", "percent_off", "money_amount_off", "promotion_code", "orders_over_amount")
    PROMOTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    REDEMPTION_START_DATE_FIELD_NUMBER: _ClassVar[int]
    REDEMPTION_END_DATE_FIELD_NUMBER: _ClassVar[int]
    OCCASION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_OFF_FIELD_NUMBER: _ClassVar[int]
    MONEY_AMOUNT_OFF_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_CODE_FIELD_NUMBER: _ClassVar[int]
    ORDERS_OVER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    promotion_target: str
    discount_modifier: _promotion_extension_discount_modifier_pb2.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    redemption_start_date: str
    redemption_end_date: str
    occasion: _promotion_extension_occasion_pb2.PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    language_code: str
    start_date: str
    end_date: str
    ad_schedule_targets: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    percent_off: int
    money_amount_off: _feed_common_pb2.Money
    promotion_code: str
    orders_over_amount: _feed_common_pb2.Money
    def __init__(self, promotion_target: _Optional[str] = ..., discount_modifier: _Optional[_Union[_promotion_extension_discount_modifier_pb2.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier, str]] = ..., redemption_start_date: _Optional[str] = ..., redemption_end_date: _Optional[str] = ..., occasion: _Optional[_Union[_promotion_extension_occasion_pb2.PromotionExtensionOccasionEnum.PromotionExtensionOccasion, str]] = ..., language_code: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., ad_schedule_targets: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ..., percent_off: _Optional[int] = ..., money_amount_off: _Optional[_Union[_feed_common_pb2.Money, _Mapping]] = ..., promotion_code: _Optional[str] = ..., orders_over_amount: _Optional[_Union[_feed_common_pb2.Money, _Mapping]] = ...) -> None: ...

class CalloutAsset(_message.Message):
    __slots__ = ("callout_text", "start_date", "end_date", "ad_schedule_targets")
    CALLOUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    callout_text: str
    start_date: str
    end_date: str
    ad_schedule_targets: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    def __init__(self, callout_text: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., ad_schedule_targets: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ...) -> None: ...

class StructuredSnippetAsset(_message.Message):
    __slots__ = ("header", "values")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    header: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class SitelinkAsset(_message.Message):
    __slots__ = ("link_text", "description1", "description2", "start_date", "end_date", "ad_schedule_targets")
    LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    link_text: str
    description1: str
    description2: str
    start_date: str
    end_date: str
    ad_schedule_targets: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    def __init__(self, link_text: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., ad_schedule_targets: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ...) -> None: ...

class PageFeedAsset(_message.Message):
    __slots__ = ("page_url", "labels")
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    page_url: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, page_url: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...

class DynamicEducationAsset(_message.Message):
    __slots__ = ("program_id", "location_id", "program_name", "subject", "program_description", "school_name", "address", "contextual_keywords", "android_app_link", "similar_program_ids", "ios_app_link", "ios_app_store_id", "thumbnail_image_url", "image_url")
    PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCHOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_PROGRAM_IDS_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    program_id: str
    location_id: str
    program_name: str
    subject: str
    program_description: str
    school_name: str
    address: str
    contextual_keywords: _containers.RepeatedScalarFieldContainer[str]
    android_app_link: str
    similar_program_ids: _containers.RepeatedScalarFieldContainer[str]
    ios_app_link: str
    ios_app_store_id: int
    thumbnail_image_url: str
    image_url: str
    def __init__(self, program_id: _Optional[str] = ..., location_id: _Optional[str] = ..., program_name: _Optional[str] = ..., subject: _Optional[str] = ..., program_description: _Optional[str] = ..., school_name: _Optional[str] = ..., address: _Optional[str] = ..., contextual_keywords: _Optional[_Iterable[str]] = ..., android_app_link: _Optional[str] = ..., similar_program_ids: _Optional[_Iterable[str]] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ..., thumbnail_image_url: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...

class MobileAppAsset(_message.Message):
    __slots__ = ("app_id", "app_store", "link_text", "start_date", "end_date")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_STORE_FIELD_NUMBER: _ClassVar[int]
    LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    app_store: _mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor
    link_text: str
    start_date: str
    end_date: str
    def __init__(self, app_id: _Optional[str] = ..., app_store: _Optional[_Union[_mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor, str]] = ..., link_text: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class HotelCalloutAsset(_message.Message):
    __slots__ = ("text", "language_code")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    text: str
    language_code: str
    def __init__(self, text: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class CallAsset(_message.Message):
    __slots__ = ("country_code", "phone_number", "call_conversion_reporting_state", "call_conversion_action", "ad_schedule_targets")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_REPORTING_STATE_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    phone_number: str
    call_conversion_reporting_state: _call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState
    call_conversion_action: str
    ad_schedule_targets: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    def __init__(self, country_code: _Optional[str] = ..., phone_number: _Optional[str] = ..., call_conversion_reporting_state: _Optional[_Union[_call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState, str]] = ..., call_conversion_action: _Optional[str] = ..., ad_schedule_targets: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ...) -> None: ...

class PriceAsset(_message.Message):
    __slots__ = ("type", "price_qualifier", "language_code", "price_offerings")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PRICE_OFFERINGS_FIELD_NUMBER: _ClassVar[int]
    type: _price_extension_type_pb2.PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier: _price_extension_price_qualifier_pb2.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    language_code: str
    price_offerings: _containers.RepeatedCompositeFieldContainer[PriceOffering]
    def __init__(self, type: _Optional[_Union[_price_extension_type_pb2.PriceExtensionTypeEnum.PriceExtensionType, str]] = ..., price_qualifier: _Optional[_Union[_price_extension_price_qualifier_pb2.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier, str]] = ..., language_code: _Optional[str] = ..., price_offerings: _Optional[_Iterable[_Union[PriceOffering, _Mapping]]] = ...) -> None: ...

class PriceOffering(_message.Message):
    __slots__ = ("header", "description", "price", "unit", "final_url", "final_mobile_url")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URL_FIELD_NUMBER: _ClassVar[int]
    header: str
    description: str
    price: _feed_common_pb2.Money
    unit: _price_extension_price_unit_pb2.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_url: str
    final_mobile_url: str
    def __init__(self, header: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[_Union[_feed_common_pb2.Money, _Mapping]] = ..., unit: _Optional[_Union[_price_extension_price_unit_pb2.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit, str]] = ..., final_url: _Optional[str] = ..., final_mobile_url: _Optional[str] = ...) -> None: ...

class CallToActionAsset(_message.Message):
    __slots__ = ("call_to_action",)
    CALL_TO_ACTION_FIELD_NUMBER: _ClassVar[int]
    call_to_action: _call_to_action_type_pb2.CallToActionTypeEnum.CallToActionType
    def __init__(self, call_to_action: _Optional[_Union[_call_to_action_type_pb2.CallToActionTypeEnum.CallToActionType, str]] = ...) -> None: ...

class DynamicRealEstateAsset(_message.Message):
    __slots__ = ("listing_id", "listing_name", "city_name", "description", "address", "price", "image_url", "property_type", "listing_type", "contextual_keywords", "formatted_price", "android_app_link", "ios_app_link", "ios_app_store_id", "similar_listing_ids")
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    LISTING_NAME_FIELD_NUMBER: _ClassVar[int]
    CITY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LISTING_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_LISTING_IDS_FIELD_NUMBER: _ClassVar[int]
    listing_id: str
    listing_name: str
    city_name: str
    description: str
    address: str
    price: str
    image_url: str
    property_type: str
    listing_type: str
    contextual_keywords: _containers.RepeatedScalarFieldContainer[str]
    formatted_price: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    similar_listing_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, listing_id: _Optional[str] = ..., listing_name: _Optional[str] = ..., city_name: _Optional[str] = ..., description: _Optional[str] = ..., address: _Optional[str] = ..., price: _Optional[str] = ..., image_url: _Optional[str] = ..., property_type: _Optional[str] = ..., listing_type: _Optional[str] = ..., contextual_keywords: _Optional[_Iterable[str]] = ..., formatted_price: _Optional[str] = ..., android_app_link: _Optional[str] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ..., similar_listing_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DynamicCustomAsset(_message.Message):
    __slots__ = ("id", "id2", "item_title", "item_subtitle", "item_description", "item_address", "item_category", "price", "sale_price", "formatted_price", "formatted_sale_price", "image_url", "contextual_keywords", "android_app_link", "ios_app_link", "ios_app_store_id", "similar_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    ID2_FIELD_NUMBER: _ClassVar[int]
    ITEM_TITLE_FIELD_NUMBER: _ClassVar[int]
    ITEM_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    ITEM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ITEM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ITEM_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    id2: str
    item_title: str
    item_subtitle: str
    item_description: str
    item_address: str
    item_category: str
    price: str
    sale_price: str
    formatted_price: str
    formatted_sale_price: str
    image_url: str
    contextual_keywords: _containers.RepeatedScalarFieldContainer[str]
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    similar_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., id2: _Optional[str] = ..., item_title: _Optional[str] = ..., item_subtitle: _Optional[str] = ..., item_description: _Optional[str] = ..., item_address: _Optional[str] = ..., item_category: _Optional[str] = ..., price: _Optional[str] = ..., sale_price: _Optional[str] = ..., formatted_price: _Optional[str] = ..., formatted_sale_price: _Optional[str] = ..., image_url: _Optional[str] = ..., contextual_keywords: _Optional[_Iterable[str]] = ..., android_app_link: _Optional[str] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ..., similar_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DynamicHotelsAndRentalsAsset(_message.Message):
    __slots__ = ("property_id", "property_name", "image_url", "destination_name", "description", "price", "sale_price", "star_rating", "category", "contextual_keywords", "address", "android_app_link", "ios_app_link", "ios_app_store_id", "formatted_price", "formatted_sale_price", "similar_property_ids")
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    STAR_RATING_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_PROPERTY_IDS_FIELD_NUMBER: _ClassVar[int]
    property_id: str
    property_name: str
    image_url: str
    destination_name: str
    description: str
    price: str
    sale_price: str
    star_rating: int
    category: str
    contextual_keywords: _containers.RepeatedScalarFieldContainer[str]
    address: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    formatted_price: str
    formatted_sale_price: str
    similar_property_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, property_id: _Optional[str] = ..., property_name: _Optional[str] = ..., image_url: _Optional[str] = ..., destination_name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[str] = ..., sale_price: _Optional[str] = ..., star_rating: _Optional[int] = ..., category: _Optional[str] = ..., contextual_keywords: _Optional[_Iterable[str]] = ..., address: _Optional[str] = ..., android_app_link: _Optional[str] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ..., formatted_price: _Optional[str] = ..., formatted_sale_price: _Optional[str] = ..., similar_property_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DynamicFlightsAsset(_message.Message):
    __slots__ = ("destination_id", "origin_id", "flight_description", "image_url", "destination_name", "origin_name", "flight_price", "flight_sale_price", "formatted_price", "formatted_sale_price", "android_app_link", "ios_app_link", "ios_app_store_id", "similar_destination_ids", "custom_mapping")
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ID_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_PRICE_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_DESTINATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MAPPING_FIELD_NUMBER: _ClassVar[int]
    destination_id: str
    origin_id: str
    flight_description: str
    image_url: str
    destination_name: str
    origin_name: str
    flight_price: str
    flight_sale_price: str
    formatted_price: str
    formatted_sale_price: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    similar_destination_ids: _containers.RepeatedScalarFieldContainer[str]
    custom_mapping: str
    def __init__(self, destination_id: _Optional[str] = ..., origin_id: _Optional[str] = ..., flight_description: _Optional[str] = ..., image_url: _Optional[str] = ..., destination_name: _Optional[str] = ..., origin_name: _Optional[str] = ..., flight_price: _Optional[str] = ..., flight_sale_price: _Optional[str] = ..., formatted_price: _Optional[str] = ..., formatted_sale_price: _Optional[str] = ..., android_app_link: _Optional[str] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ..., similar_destination_ids: _Optional[_Iterable[str]] = ..., custom_mapping: _Optional[str] = ...) -> None: ...

class DemandGenCarouselCardAsset(_message.Message):
    __slots__ = ("marketing_image_asset", "square_marketing_image_asset", "portrait_marketing_image_asset", "headline", "call_to_action_text")
    MARKETING_IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    SQUARE_MARKETING_IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_MARKETING_IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    marketing_image_asset: str
    square_marketing_image_asset: str
    portrait_marketing_image_asset: str
    headline: str
    call_to_action_text: str
    def __init__(self, marketing_image_asset: _Optional[str] = ..., square_marketing_image_asset: _Optional[str] = ..., portrait_marketing_image_asset: _Optional[str] = ..., headline: _Optional[str] = ..., call_to_action_text: _Optional[str] = ...) -> None: ...

class DynamicTravelAsset(_message.Message):
    __slots__ = ("destination_id", "origin_id", "title", "destination_name", "destination_address", "origin_name", "price", "sale_price", "formatted_price", "formatted_sale_price", "category", "contextual_keywords", "similar_destination_ids", "image_url", "android_app_link", "ios_app_link", "ios_app_store_id")
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_DESTINATION_IDS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    destination_id: str
    origin_id: str
    title: str
    destination_name: str
    destination_address: str
    origin_name: str
    price: str
    sale_price: str
    formatted_price: str
    formatted_sale_price: str
    category: str
    contextual_keywords: _containers.RepeatedScalarFieldContainer[str]
    similar_destination_ids: _containers.RepeatedScalarFieldContainer[str]
    image_url: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    def __init__(self, destination_id: _Optional[str] = ..., origin_id: _Optional[str] = ..., title: _Optional[str] = ..., destination_name: _Optional[str] = ..., destination_address: _Optional[str] = ..., origin_name: _Optional[str] = ..., price: _Optional[str] = ..., sale_price: _Optional[str] = ..., formatted_price: _Optional[str] = ..., formatted_sale_price: _Optional[str] = ..., category: _Optional[str] = ..., contextual_keywords: _Optional[_Iterable[str]] = ..., similar_destination_ids: _Optional[_Iterable[str]] = ..., image_url: _Optional[str] = ..., android_app_link: _Optional[str] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ...) -> None: ...

class DynamicLocalAsset(_message.Message):
    __slots__ = ("deal_id", "deal_name", "subtitle", "description", "price", "sale_price", "image_url", "address", "category", "contextual_keywords", "formatted_price", "formatted_sale_price", "android_app_link", "similar_deal_ids", "ios_app_link", "ios_app_store_id")
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    DEAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_DEAL_IDS_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    deal_id: str
    deal_name: str
    subtitle: str
    description: str
    price: str
    sale_price: str
    image_url: str
    address: str
    category: str
    contextual_keywords: _containers.RepeatedScalarFieldContainer[str]
    formatted_price: str
    formatted_sale_price: str
    android_app_link: str
    similar_deal_ids: _containers.RepeatedScalarFieldContainer[str]
    ios_app_link: str
    ios_app_store_id: int
    def __init__(self, deal_id: _Optional[str] = ..., deal_name: _Optional[str] = ..., subtitle: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[str] = ..., sale_price: _Optional[str] = ..., image_url: _Optional[str] = ..., address: _Optional[str] = ..., category: _Optional[str] = ..., contextual_keywords: _Optional[_Iterable[str]] = ..., formatted_price: _Optional[str] = ..., formatted_sale_price: _Optional[str] = ..., android_app_link: _Optional[str] = ..., similar_deal_ids: _Optional[_Iterable[str]] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ...) -> None: ...

class DynamicJobsAsset(_message.Message):
    __slots__ = ("job_id", "location_id", "job_title", "job_subtitle", "description", "image_url", "job_category", "contextual_keywords", "address", "salary", "android_app_link", "similar_job_ids", "ios_app_link", "ios_app_store_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TITLE_FIELD_NUMBER: _ClassVar[int]
    JOB_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    JOB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SALARY_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_JOB_IDS_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_LINK_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    location_id: str
    job_title: str
    job_subtitle: str
    description: str
    image_url: str
    job_category: str
    contextual_keywords: _containers.RepeatedScalarFieldContainer[str]
    address: str
    salary: str
    android_app_link: str
    similar_job_ids: _containers.RepeatedScalarFieldContainer[str]
    ios_app_link: str
    ios_app_store_id: int
    def __init__(self, job_id: _Optional[str] = ..., location_id: _Optional[str] = ..., job_title: _Optional[str] = ..., job_subtitle: _Optional[str] = ..., description: _Optional[str] = ..., image_url: _Optional[str] = ..., job_category: _Optional[str] = ..., contextual_keywords: _Optional[_Iterable[str]] = ..., address: _Optional[str] = ..., salary: _Optional[str] = ..., android_app_link: _Optional[str] = ..., similar_job_ids: _Optional[_Iterable[str]] = ..., ios_app_link: _Optional[str] = ..., ios_app_store_id: _Optional[int] = ...) -> None: ...

class LocationAsset(_message.Message):
    __slots__ = ("place_id", "business_profile_locations", "location_ownership_type")
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_PROFILE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OWNERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    business_profile_locations: _containers.RepeatedCompositeFieldContainer[BusinessProfileLocation]
    location_ownership_type: _location_ownership_type_pb2.LocationOwnershipTypeEnum.LocationOwnershipType
    def __init__(self, place_id: _Optional[str] = ..., business_profile_locations: _Optional[_Iterable[_Union[BusinessProfileLocation, _Mapping]]] = ..., location_ownership_type: _Optional[_Union[_location_ownership_type_pb2.LocationOwnershipTypeEnum.LocationOwnershipType, str]] = ...) -> None: ...

class BusinessProfileLocation(_message.Message):
    __slots__ = ("labels", "store_code", "listing_id")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STORE_CODE_FIELD_NUMBER: _ClassVar[int]
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedScalarFieldContainer[str]
    store_code: str
    listing_id: int
    def __init__(self, labels: _Optional[_Iterable[str]] = ..., store_code: _Optional[str] = ..., listing_id: _Optional[int] = ...) -> None: ...

class HotelPropertyAsset(_message.Message):
    __slots__ = ("place_id", "hotel_address", "hotel_name")
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    HOTEL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HOTEL_NAME_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    hotel_address: str
    hotel_name: str
    def __init__(self, place_id: _Optional[str] = ..., hotel_address: _Optional[str] = ..., hotel_name: _Optional[str] = ...) -> None: ...
