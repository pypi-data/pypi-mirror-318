from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PromotionPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class PromotionPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        UNKNOWN: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        PROMOTION_TARGET: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        DISCOUNT_MODIFIER: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        PERCENT_OFF: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        MONEY_AMOUNT_OFF: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        PROMOTION_CODE: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        ORDERS_OVER_AMOUNT: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        PROMOTION_START: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        PROMOTION_END: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        OCCASION: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        FINAL_URLS: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        FINAL_MOBILE_URLS: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        TRACKING_URL: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        LANGUAGE: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
        FINAL_URL_SUFFIX: _ClassVar[PromotionPlaceholderFieldEnum.PromotionPlaceholderField]
    UNSPECIFIED: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    UNKNOWN: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    PROMOTION_TARGET: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    DISCOUNT_MODIFIER: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    PERCENT_OFF: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    MONEY_AMOUNT_OFF: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    PROMOTION_CODE: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    ORDERS_OVER_AMOUNT: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    PROMOTION_START: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    PROMOTION_END: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    OCCASION: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    FINAL_URLS: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    FINAL_MOBILE_URLS: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    TRACKING_URL: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    LANGUAGE: PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    FINAL_URL_SUFFIX: PromotionPlaceholderFieldEnum.PromotionPlaceholderField

    def __init__(self) -> None:
        ...