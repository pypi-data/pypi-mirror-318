from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_PERIOD_UNSPECIFIED: _ClassVar[SubscriptionPeriod]
    MONTH: _ClassVar[SubscriptionPeriod]
    YEAR: _ClassVar[SubscriptionPeriod]
SUBSCRIPTION_PERIOD_UNSPECIFIED: SubscriptionPeriod
MONTH: SubscriptionPeriod
YEAR: SubscriptionPeriod

class Attributes(_message.Message):
    __slots__ = ("cpp_link", "cpp_mobile_link", "cpp_ads_redirect", "low_price", "high_price", "number_of_offers", "headline_offer_condition", "headline_offer_price", "headline_offer_link", "headline_offer_mobile_link", "headline_offer_shipping_price", "title", "image_link", "additional_image_links", "description", "brand", "mpn", "gtin", "product_types", "google_product_category", "adult", "multipack", "is_bundle", "age_group", "color", "gender", "material", "pattern", "size", "size_system", "size_types", "item_group_id", "product_details", "product_weight", "product_length", "product_width", "product_height", "product_highlights", "certifications", "expiration_date", "included_destinations", "excluded_destinations", "pause", "custom_label_0", "custom_label_1", "custom_label_2", "custom_label_3", "custom_label_4", "headline_offer_installment", "headline_offer_subscription_cost")
    CPP_LINK_FIELD_NUMBER: _ClassVar[int]
    CPP_MOBILE_LINK_FIELD_NUMBER: _ClassVar[int]
    CPP_ADS_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    LOW_PRICE_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRICE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_OFFERS_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_OFFER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_OFFER_PRICE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_OFFER_LINK_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_OFFER_MOBILE_LINK_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_OFFER_SHIPPING_PRICE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_LINK_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_IMAGE_LINKS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    MPN_FIELD_NUMBER: _ClassVar[int]
    GTIN_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPES_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PRODUCT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ADULT_FIELD_NUMBER: _ClassVar[int]
    MULTIPACK_FIELD_NUMBER: _ClassVar[int]
    IS_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    AGE_GROUP_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SIZE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SIZE_TYPES_FIELD_NUMBER: _ClassVar[int]
    ITEM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_0_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_1_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_2_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_3_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_4_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_OFFER_INSTALLMENT_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_OFFER_SUBSCRIPTION_COST_FIELD_NUMBER: _ClassVar[int]
    cpp_link: str
    cpp_mobile_link: str
    cpp_ads_redirect: str
    low_price: _types_pb2.Price
    high_price: _types_pb2.Price
    number_of_offers: int
    headline_offer_condition: str
    headline_offer_price: _types_pb2.Price
    headline_offer_link: str
    headline_offer_mobile_link: str
    headline_offer_shipping_price: _types_pb2.Price
    title: str
    image_link: str
    additional_image_links: _containers.RepeatedScalarFieldContainer[str]
    description: str
    brand: str
    mpn: str
    gtin: str
    product_types: _containers.RepeatedScalarFieldContainer[str]
    google_product_category: str
    adult: bool
    multipack: int
    is_bundle: bool
    age_group: str
    color: str
    gender: str
    material: str
    pattern: str
    size: str
    size_system: str
    size_types: _containers.RepeatedScalarFieldContainer[str]
    item_group_id: str
    product_details: _containers.RepeatedCompositeFieldContainer[ProductDetail]
    product_weight: ProductWeight
    product_length: ProductDimension
    product_width: ProductDimension
    product_height: ProductDimension
    product_highlights: _containers.RepeatedScalarFieldContainer[str]
    certifications: _containers.RepeatedCompositeFieldContainer[Certification]
    expiration_date: _timestamp_pb2.Timestamp
    included_destinations: _containers.RepeatedScalarFieldContainer[str]
    excluded_destinations: _containers.RepeatedScalarFieldContainer[str]
    pause: str
    custom_label_0: str
    custom_label_1: str
    custom_label_2: str
    custom_label_3: str
    custom_label_4: str
    headline_offer_installment: HeadlineOfferInstallment
    headline_offer_subscription_cost: HeadlineOfferSubscriptionCost
    def __init__(self, cpp_link: _Optional[str] = ..., cpp_mobile_link: _Optional[str] = ..., cpp_ads_redirect: _Optional[str] = ..., low_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., high_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., number_of_offers: _Optional[int] = ..., headline_offer_condition: _Optional[str] = ..., headline_offer_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., headline_offer_link: _Optional[str] = ..., headline_offer_mobile_link: _Optional[str] = ..., headline_offer_shipping_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., title: _Optional[str] = ..., image_link: _Optional[str] = ..., additional_image_links: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., brand: _Optional[str] = ..., mpn: _Optional[str] = ..., gtin: _Optional[str] = ..., product_types: _Optional[_Iterable[str]] = ..., google_product_category: _Optional[str] = ..., adult: bool = ..., multipack: _Optional[int] = ..., is_bundle: bool = ..., age_group: _Optional[str] = ..., color: _Optional[str] = ..., gender: _Optional[str] = ..., material: _Optional[str] = ..., pattern: _Optional[str] = ..., size: _Optional[str] = ..., size_system: _Optional[str] = ..., size_types: _Optional[_Iterable[str]] = ..., item_group_id: _Optional[str] = ..., product_details: _Optional[_Iterable[_Union[ProductDetail, _Mapping]]] = ..., product_weight: _Optional[_Union[ProductWeight, _Mapping]] = ..., product_length: _Optional[_Union[ProductDimension, _Mapping]] = ..., product_width: _Optional[_Union[ProductDimension, _Mapping]] = ..., product_height: _Optional[_Union[ProductDimension, _Mapping]] = ..., product_highlights: _Optional[_Iterable[str]] = ..., certifications: _Optional[_Iterable[_Union[Certification, _Mapping]]] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., included_destinations: _Optional[_Iterable[str]] = ..., excluded_destinations: _Optional[_Iterable[str]] = ..., pause: _Optional[str] = ..., custom_label_0: _Optional[str] = ..., custom_label_1: _Optional[str] = ..., custom_label_2: _Optional[str] = ..., custom_label_3: _Optional[str] = ..., custom_label_4: _Optional[str] = ..., headline_offer_installment: _Optional[_Union[HeadlineOfferInstallment, _Mapping]] = ..., headline_offer_subscription_cost: _Optional[_Union[HeadlineOfferSubscriptionCost, _Mapping]] = ...) -> None: ...

class Certification(_message.Message):
    __slots__ = ("name", "authority", "code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    authority: str
    code: str
    def __init__(self, name: _Optional[str] = ..., authority: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ProductDetail(_message.Message):
    __slots__ = ("section_name", "attribute_name", "attribute_value")
    SECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
    section_name: str
    attribute_name: str
    attribute_value: str
    def __init__(self, section_name: _Optional[str] = ..., attribute_name: _Optional[str] = ..., attribute_value: _Optional[str] = ...) -> None: ...

class ProductDimension(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[str] = ...) -> None: ...

class ProductWeight(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[str] = ...) -> None: ...

class CssProductStatus(_message.Message):
    __slots__ = ("destination_statuses", "item_level_issues", "creation_date", "last_update_date", "google_expiration_date")
    class DestinationStatus(_message.Message):
        __slots__ = ("destination", "approved_countries", "pending_countries", "disapproved_countries")
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        APPROVED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        PENDING_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        DISAPPROVED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        destination: str
        approved_countries: _containers.RepeatedScalarFieldContainer[str]
        pending_countries: _containers.RepeatedScalarFieldContainer[str]
        disapproved_countries: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, destination: _Optional[str] = ..., approved_countries: _Optional[_Iterable[str]] = ..., pending_countries: _Optional[_Iterable[str]] = ..., disapproved_countries: _Optional[_Iterable[str]] = ...) -> None: ...
    class ItemLevelIssue(_message.Message):
        __slots__ = ("code", "servability", "resolution", "attribute", "destination", "description", "detail", "documentation", "applicable_countries")
        CODE_FIELD_NUMBER: _ClassVar[int]
        SERVABILITY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
        APPLICABLE_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        code: str
        servability: str
        resolution: str
        attribute: str
        destination: str
        description: str
        detail: str
        documentation: str
        applicable_countries: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, code: _Optional[str] = ..., servability: _Optional[str] = ..., resolution: _Optional[str] = ..., attribute: _Optional[str] = ..., destination: _Optional[str] = ..., description: _Optional[str] = ..., detail: _Optional[str] = ..., documentation: _Optional[str] = ..., applicable_countries: _Optional[_Iterable[str]] = ...) -> None: ...
    DESTINATION_STATUSES_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_ISSUES_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    destination_statuses: _containers.RepeatedCompositeFieldContainer[CssProductStatus.DestinationStatus]
    item_level_issues: _containers.RepeatedCompositeFieldContainer[CssProductStatus.ItemLevelIssue]
    creation_date: _timestamp_pb2.Timestamp
    last_update_date: _timestamp_pb2.Timestamp
    google_expiration_date: _timestamp_pb2.Timestamp
    def __init__(self, destination_statuses: _Optional[_Iterable[_Union[CssProductStatus.DestinationStatus, _Mapping]]] = ..., item_level_issues: _Optional[_Iterable[_Union[CssProductStatus.ItemLevelIssue, _Mapping]]] = ..., creation_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., google_expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class HeadlineOfferSubscriptionCost(_message.Message):
    __slots__ = ("period", "period_length", "amount")
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    PERIOD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    period: SubscriptionPeriod
    period_length: int
    amount: _types_pb2.Price
    def __init__(self, period: _Optional[_Union[SubscriptionPeriod, str]] = ..., period_length: _Optional[int] = ..., amount: _Optional[_Union[_types_pb2.Price, _Mapping]] = ...) -> None: ...

class HeadlineOfferInstallment(_message.Message):
    __slots__ = ("months", "amount", "downpayment")
    MONTHS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNPAYMENT_FIELD_NUMBER: _ClassVar[int]
    months: int
    amount: _types_pb2.Price
    downpayment: _types_pb2.Price
    def __init__(self, months: _Optional[int] = ..., amount: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., downpayment: _Optional[_Union[_types_pb2.Price, _Mapping]] = ...) -> None: ...
