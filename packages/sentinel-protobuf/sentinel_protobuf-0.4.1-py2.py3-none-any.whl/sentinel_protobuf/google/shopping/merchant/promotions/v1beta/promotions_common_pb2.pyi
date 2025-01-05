from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductApplicability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_APPLICABILITY_UNSPECIFIED: _ClassVar[ProductApplicability]
    ALL_PRODUCTS: _ClassVar[ProductApplicability]
    SPECIFIC_PRODUCTS: _ClassVar[ProductApplicability]

class StoreApplicability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORE_APPLICABILITY_UNSPECIFIED: _ClassVar[StoreApplicability]
    ALL_STORES: _ClassVar[StoreApplicability]
    SPECIFIC_STORES: _ClassVar[StoreApplicability]

class OfferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFFER_TYPE_UNSPECIFIED: _ClassVar[OfferType]
    NO_CODE: _ClassVar[OfferType]
    GENERIC_CODE: _ClassVar[OfferType]

class RedemptionChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REDEMPTION_CHANNEL_UNSPECIFIED: _ClassVar[RedemptionChannel]
    IN_STORE: _ClassVar[RedemptionChannel]
    ONLINE: _ClassVar[RedemptionChannel]

class CouponValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COUPON_VALUE_TYPE_UNSPECIFIED: _ClassVar[CouponValueType]
    MONEY_OFF: _ClassVar[CouponValueType]
    PERCENT_OFF: _ClassVar[CouponValueType]
    BUY_M_GET_N_MONEY_OFF: _ClassVar[CouponValueType]
    BUY_M_GET_N_PERCENT_OFF: _ClassVar[CouponValueType]
    BUY_M_GET_MONEY_OFF: _ClassVar[CouponValueType]
    BUY_M_GET_PERCENT_OFF: _ClassVar[CouponValueType]
    FREE_GIFT: _ClassVar[CouponValueType]
    FREE_GIFT_WITH_VALUE: _ClassVar[CouponValueType]
    FREE_GIFT_WITH_ITEM_ID: _ClassVar[CouponValueType]
    FREE_SHIPPING_STANDARD: _ClassVar[CouponValueType]
    FREE_SHIPPING_OVERNIGHT: _ClassVar[CouponValueType]
    FREE_SHIPPING_TWO_DAY: _ClassVar[CouponValueType]
PRODUCT_APPLICABILITY_UNSPECIFIED: ProductApplicability
ALL_PRODUCTS: ProductApplicability
SPECIFIC_PRODUCTS: ProductApplicability
STORE_APPLICABILITY_UNSPECIFIED: StoreApplicability
ALL_STORES: StoreApplicability
SPECIFIC_STORES: StoreApplicability
OFFER_TYPE_UNSPECIFIED: OfferType
NO_CODE: OfferType
GENERIC_CODE: OfferType
REDEMPTION_CHANNEL_UNSPECIFIED: RedemptionChannel
IN_STORE: RedemptionChannel
ONLINE: RedemptionChannel
COUPON_VALUE_TYPE_UNSPECIFIED: CouponValueType
MONEY_OFF: CouponValueType
PERCENT_OFF: CouponValueType
BUY_M_GET_N_MONEY_OFF: CouponValueType
BUY_M_GET_N_PERCENT_OFF: CouponValueType
BUY_M_GET_MONEY_OFF: CouponValueType
BUY_M_GET_PERCENT_OFF: CouponValueType
FREE_GIFT: CouponValueType
FREE_GIFT_WITH_VALUE: CouponValueType
FREE_GIFT_WITH_ITEM_ID: CouponValueType
FREE_SHIPPING_STANDARD: CouponValueType
FREE_SHIPPING_OVERNIGHT: CouponValueType
FREE_SHIPPING_TWO_DAY: CouponValueType

class Attributes(_message.Message):
    __slots__ = ("product_applicability", "offer_type", "generic_redemption_code", "long_title", "coupon_value_type", "promotion_destinations", "item_id_inclusion", "brand_inclusion", "item_group_id_inclusion", "product_type_inclusion", "item_id_exclusion", "brand_exclusion", "item_group_id_exclusion", "product_type_exclusion", "minimum_purchase_amount", "minimum_purchase_quantity", "limit_quantity", "limit_value", "percent_off", "money_off_amount", "get_this_quantity_discounted", "free_gift_value", "free_gift_description", "free_gift_item_id", "promotion_effective_time_period", "promotion_display_time_period", "store_applicability", "store_codes_inclusion", "store_codes_exclusion", "promotion_url")
    PRODUCT_APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    GENERIC_REDEMPTION_CODE_FIELD_NUMBER: _ClassVar[int]
    LONG_TITLE_FIELD_NUMBER: _ClassVar[int]
    COUPON_VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    BRAND_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    ITEM_GROUP_ID_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    BRAND_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    ITEM_GROUP_ID_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PURCHASE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PURCHASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    PERCENT_OFF_FIELD_NUMBER: _ClassVar[int]
    MONEY_OFF_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    GET_THIS_QUANTITY_DISCOUNTED_FIELD_NUMBER: _ClassVar[int]
    FREE_GIFT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FREE_GIFT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FREE_GIFT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_EFFECTIVE_TIME_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_DISPLAY_TIME_PERIOD_FIELD_NUMBER: _ClassVar[int]
    STORE_APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    STORE_CODES_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    STORE_CODES_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_URL_FIELD_NUMBER: _ClassVar[int]
    product_applicability: ProductApplicability
    offer_type: OfferType
    generic_redemption_code: str
    long_title: str
    coupon_value_type: CouponValueType
    promotion_destinations: _containers.RepeatedScalarFieldContainer[_types_pb2.Destination.DestinationEnum]
    item_id_inclusion: _containers.RepeatedScalarFieldContainer[str]
    brand_inclusion: _containers.RepeatedScalarFieldContainer[str]
    item_group_id_inclusion: _containers.RepeatedScalarFieldContainer[str]
    product_type_inclusion: _containers.RepeatedScalarFieldContainer[str]
    item_id_exclusion: _containers.RepeatedScalarFieldContainer[str]
    brand_exclusion: _containers.RepeatedScalarFieldContainer[str]
    item_group_id_exclusion: _containers.RepeatedScalarFieldContainer[str]
    product_type_exclusion: _containers.RepeatedScalarFieldContainer[str]
    minimum_purchase_amount: _types_pb2.Price
    minimum_purchase_quantity: int
    limit_quantity: int
    limit_value: _types_pb2.Price
    percent_off: int
    money_off_amount: _types_pb2.Price
    get_this_quantity_discounted: int
    free_gift_value: _types_pb2.Price
    free_gift_description: str
    free_gift_item_id: str
    promotion_effective_time_period: _interval_pb2.Interval
    promotion_display_time_period: _interval_pb2.Interval
    store_applicability: StoreApplicability
    store_codes_inclusion: _containers.RepeatedScalarFieldContainer[str]
    store_codes_exclusion: _containers.RepeatedScalarFieldContainer[str]
    promotion_url: str
    def __init__(self, product_applicability: _Optional[_Union[ProductApplicability, str]] = ..., offer_type: _Optional[_Union[OfferType, str]] = ..., generic_redemption_code: _Optional[str] = ..., long_title: _Optional[str] = ..., coupon_value_type: _Optional[_Union[CouponValueType, str]] = ..., promotion_destinations: _Optional[_Iterable[_Union[_types_pb2.Destination.DestinationEnum, str]]] = ..., item_id_inclusion: _Optional[_Iterable[str]] = ..., brand_inclusion: _Optional[_Iterable[str]] = ..., item_group_id_inclusion: _Optional[_Iterable[str]] = ..., product_type_inclusion: _Optional[_Iterable[str]] = ..., item_id_exclusion: _Optional[_Iterable[str]] = ..., brand_exclusion: _Optional[_Iterable[str]] = ..., item_group_id_exclusion: _Optional[_Iterable[str]] = ..., product_type_exclusion: _Optional[_Iterable[str]] = ..., minimum_purchase_amount: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., minimum_purchase_quantity: _Optional[int] = ..., limit_quantity: _Optional[int] = ..., limit_value: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., percent_off: _Optional[int] = ..., money_off_amount: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., get_this_quantity_discounted: _Optional[int] = ..., free_gift_value: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., free_gift_description: _Optional[str] = ..., free_gift_item_id: _Optional[str] = ..., promotion_effective_time_period: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., promotion_display_time_period: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., store_applicability: _Optional[_Union[StoreApplicability, str]] = ..., store_codes_inclusion: _Optional[_Iterable[str]] = ..., store_codes_exclusion: _Optional[_Iterable[str]] = ..., promotion_url: _Optional[str] = ...) -> None: ...

class PromotionStatus(_message.Message):
    __slots__ = ("destination_statuses", "item_level_issues", "creation_date", "last_update_date")
    class DestinationStatus(_message.Message):
        __slots__ = ("reporting_context", "status")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[PromotionStatus.DestinationStatus.State]
            IN_REVIEW: _ClassVar[PromotionStatus.DestinationStatus.State]
            REJECTED: _ClassVar[PromotionStatus.DestinationStatus.State]
            LIVE: _ClassVar[PromotionStatus.DestinationStatus.State]
            STOPPED: _ClassVar[PromotionStatus.DestinationStatus.State]
            EXPIRED: _ClassVar[PromotionStatus.DestinationStatus.State]
            PENDING: _ClassVar[PromotionStatus.DestinationStatus.State]
        STATE_UNSPECIFIED: PromotionStatus.DestinationStatus.State
        IN_REVIEW: PromotionStatus.DestinationStatus.State
        REJECTED: PromotionStatus.DestinationStatus.State
        LIVE: PromotionStatus.DestinationStatus.State
        STOPPED: PromotionStatus.DestinationStatus.State
        EXPIRED: PromotionStatus.DestinationStatus.State
        PENDING: PromotionStatus.DestinationStatus.State
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        status: PromotionStatus.DestinationStatus.State
        def __init__(self, reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ..., status: _Optional[_Union[PromotionStatus.DestinationStatus.State, str]] = ...) -> None: ...
    class ItemLevelIssue(_message.Message):
        __slots__ = ("code", "severity", "resolution", "attribute", "reporting_context", "description", "detail", "documentation", "applicable_countries")
        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEVERITY_UNSPECIFIED: _ClassVar[PromotionStatus.ItemLevelIssue.Severity]
            NOT_IMPACTED: _ClassVar[PromotionStatus.ItemLevelIssue.Severity]
            DEMOTED: _ClassVar[PromotionStatus.ItemLevelIssue.Severity]
            DISAPPROVED: _ClassVar[PromotionStatus.ItemLevelIssue.Severity]
        SEVERITY_UNSPECIFIED: PromotionStatus.ItemLevelIssue.Severity
        NOT_IMPACTED: PromotionStatus.ItemLevelIssue.Severity
        DEMOTED: PromotionStatus.ItemLevelIssue.Severity
        DISAPPROVED: PromotionStatus.ItemLevelIssue.Severity
        CODE_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
        APPLICABLE_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        code: str
        severity: PromotionStatus.ItemLevelIssue.Severity
        resolution: str
        attribute: str
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        description: str
        detail: str
        documentation: str
        applicable_countries: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, code: _Optional[str] = ..., severity: _Optional[_Union[PromotionStatus.ItemLevelIssue.Severity, str]] = ..., resolution: _Optional[str] = ..., attribute: _Optional[str] = ..., reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ..., description: _Optional[str] = ..., detail: _Optional[str] = ..., documentation: _Optional[str] = ..., applicable_countries: _Optional[_Iterable[str]] = ...) -> None: ...
    DESTINATION_STATUSES_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_ISSUES_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    destination_statuses: _containers.RepeatedCompositeFieldContainer[PromotionStatus.DestinationStatus]
    item_level_issues: _containers.RepeatedCompositeFieldContainer[PromotionStatus.ItemLevelIssue]
    creation_date: _timestamp_pb2.Timestamp
    last_update_date: _timestamp_pb2.Timestamp
    def __init__(self, destination_statuses: _Optional[_Iterable[_Union[PromotionStatus.DestinationStatus, _Mapping]]] = ..., item_level_issues: _Optional[_Iterable[_Union[PromotionStatus.ItemLevelIssue, _Mapping]]] = ..., creation_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
