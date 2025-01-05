from google.ads.googleads.v17.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v17.common import feed_common_pb2 as _feed_common_pb2
from google.ads.googleads.v17.enums import app_store_pb2 as _app_store_pb2
from google.ads.googleads.v17.enums import call_conversion_reporting_state_pb2 as _call_conversion_reporting_state_pb2
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

class AppFeedItem(_message.Message):
    __slots__ = ("link_text", "app_id", "app_store", "final_urls", "final_mobile_urls", "tracking_url_template", "url_custom_parameters", "final_url_suffix")
    LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_STORE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    link_text: str
    app_id: str
    app_store: _app_store_pb2.AppStoreEnum.AppStore
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    final_url_suffix: str
    def __init__(self, link_text: _Optional[str] = ..., app_id: _Optional[str] = ..., app_store: _Optional[_Union[_app_store_pb2.AppStoreEnum.AppStore, str]] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., final_url_suffix: _Optional[str] = ...) -> None: ...

class CallFeedItem(_message.Message):
    __slots__ = ("phone_number", "country_code", "call_tracking_enabled", "call_conversion_action", "call_conversion_tracking_disabled", "call_conversion_reporting_state")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CALL_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_TRACKING_DISABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_REPORTING_STATE_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    country_code: str
    call_tracking_enabled: bool
    call_conversion_action: str
    call_conversion_tracking_disabled: bool
    call_conversion_reporting_state: _call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState
    def __init__(self, phone_number: _Optional[str] = ..., country_code: _Optional[str] = ..., call_tracking_enabled: bool = ..., call_conversion_action: _Optional[str] = ..., call_conversion_tracking_disabled: bool = ..., call_conversion_reporting_state: _Optional[_Union[_call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState, str]] = ...) -> None: ...

class CalloutFeedItem(_message.Message):
    __slots__ = ("callout_text",)
    CALLOUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    callout_text: str
    def __init__(self, callout_text: _Optional[str] = ...) -> None: ...

class LocationFeedItem(_message.Message):
    __slots__ = ("business_name", "address_line_1", "address_line_2", "city", "province", "postal_code", "country_code", "phone_number")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE_1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE_2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    address_line_1: str
    address_line_2: str
    city: str
    province: str
    postal_code: str
    country_code: str
    phone_number: str
    def __init__(self, business_name: _Optional[str] = ..., address_line_1: _Optional[str] = ..., address_line_2: _Optional[str] = ..., city: _Optional[str] = ..., province: _Optional[str] = ..., postal_code: _Optional[str] = ..., country_code: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...

class AffiliateLocationFeedItem(_message.Message):
    __slots__ = ("business_name", "address_line_1", "address_line_2", "city", "province", "postal_code", "country_code", "phone_number", "chain_id", "chain_name")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE_1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE_2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    address_line_1: str
    address_line_2: str
    city: str
    province: str
    postal_code: str
    country_code: str
    phone_number: str
    chain_id: int
    chain_name: str
    def __init__(self, business_name: _Optional[str] = ..., address_line_1: _Optional[str] = ..., address_line_2: _Optional[str] = ..., city: _Optional[str] = ..., province: _Optional[str] = ..., postal_code: _Optional[str] = ..., country_code: _Optional[str] = ..., phone_number: _Optional[str] = ..., chain_id: _Optional[int] = ..., chain_name: _Optional[str] = ...) -> None: ...

class TextMessageFeedItem(_message.Message):
    __slots__ = ("business_name", "country_code", "phone_number", "text", "extension_text")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_TEXT_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    country_code: str
    phone_number: str
    text: str
    extension_text: str
    def __init__(self, business_name: _Optional[str] = ..., country_code: _Optional[str] = ..., phone_number: _Optional[str] = ..., text: _Optional[str] = ..., extension_text: _Optional[str] = ...) -> None: ...

class PriceFeedItem(_message.Message):
    __slots__ = ("type", "price_qualifier", "tracking_url_template", "language_code", "price_offerings", "final_url_suffix")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PRICE_OFFERINGS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    type: _price_extension_type_pb2.PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier: _price_extension_price_qualifier_pb2.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    tracking_url_template: str
    language_code: str
    price_offerings: _containers.RepeatedCompositeFieldContainer[PriceOffer]
    final_url_suffix: str
    def __init__(self, type: _Optional[_Union[_price_extension_type_pb2.PriceExtensionTypeEnum.PriceExtensionType, str]] = ..., price_qualifier: _Optional[_Union[_price_extension_price_qualifier_pb2.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier, str]] = ..., tracking_url_template: _Optional[str] = ..., language_code: _Optional[str] = ..., price_offerings: _Optional[_Iterable[_Union[PriceOffer, _Mapping]]] = ..., final_url_suffix: _Optional[str] = ...) -> None: ...

class PriceOffer(_message.Message):
    __slots__ = ("header", "description", "price", "unit", "final_urls", "final_mobile_urls")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    header: str
    description: str
    price: _feed_common_pb2.Money
    unit: _price_extension_price_unit_pb2.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[_Union[_feed_common_pb2.Money, _Mapping]] = ..., unit: _Optional[_Union[_price_extension_price_unit_pb2.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit, str]] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ...) -> None: ...

class PromotionFeedItem(_message.Message):
    __slots__ = ("promotion_target", "discount_modifier", "promotion_start_date", "promotion_end_date", "occasion", "final_urls", "final_mobile_urls", "tracking_url_template", "url_custom_parameters", "final_url_suffix", "language_code", "percent_off", "money_amount_off", "promotion_code", "orders_over_amount")
    PROMOTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_START_DATE_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_END_DATE_FIELD_NUMBER: _ClassVar[int]
    OCCASION_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PERCENT_OFF_FIELD_NUMBER: _ClassVar[int]
    MONEY_AMOUNT_OFF_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_CODE_FIELD_NUMBER: _ClassVar[int]
    ORDERS_OVER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    promotion_target: str
    discount_modifier: _promotion_extension_discount_modifier_pb2.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    promotion_start_date: str
    promotion_end_date: str
    occasion: _promotion_extension_occasion_pb2.PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    final_url_suffix: str
    language_code: str
    percent_off: int
    money_amount_off: _feed_common_pb2.Money
    promotion_code: str
    orders_over_amount: _feed_common_pb2.Money
    def __init__(self, promotion_target: _Optional[str] = ..., discount_modifier: _Optional[_Union[_promotion_extension_discount_modifier_pb2.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier, str]] = ..., promotion_start_date: _Optional[str] = ..., promotion_end_date: _Optional[str] = ..., occasion: _Optional[_Union[_promotion_extension_occasion_pb2.PromotionExtensionOccasionEnum.PromotionExtensionOccasion, str]] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., final_url_suffix: _Optional[str] = ..., language_code: _Optional[str] = ..., percent_off: _Optional[int] = ..., money_amount_off: _Optional[_Union[_feed_common_pb2.Money, _Mapping]] = ..., promotion_code: _Optional[str] = ..., orders_over_amount: _Optional[_Union[_feed_common_pb2.Money, _Mapping]] = ...) -> None: ...

class StructuredSnippetFeedItem(_message.Message):
    __slots__ = ("header", "values")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    header: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class SitelinkFeedItem(_message.Message):
    __slots__ = ("link_text", "line1", "line2", "final_urls", "final_mobile_urls", "tracking_url_template", "url_custom_parameters", "final_url_suffix")
    LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
    LINE1_FIELD_NUMBER: _ClassVar[int]
    LINE2_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    link_text: str
    line1: str
    line2: str
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    final_url_suffix: str
    def __init__(self, link_text: _Optional[str] = ..., line1: _Optional[str] = ..., line2: _Optional[str] = ..., final_urls: _Optional[_Iterable[str]] = ..., final_mobile_urls: _Optional[_Iterable[str]] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., final_url_suffix: _Optional[str] = ...) -> None: ...

class HotelCalloutFeedItem(_message.Message):
    __slots__ = ("text", "language_code")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    text: str
    language_code: str
    def __init__(self, text: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class ImageFeedItem(_message.Message):
    __slots__ = ("image_asset",)
    IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    image_asset: str
    def __init__(self, image_asset: _Optional[str] = ...) -> None: ...
