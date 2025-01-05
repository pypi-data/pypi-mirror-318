from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ShoppingAddProductsToCampaignRecommendationEnum(_message.Message):
    __slots__ = ()

    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ShoppingAddProductsToCampaignRecommendationEnum.Reason]
        UNKNOWN: _ClassVar[ShoppingAddProductsToCampaignRecommendationEnum.Reason]
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS: _ClassVar[ShoppingAddProductsToCampaignRecommendationEnum.Reason]
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS_IN_FEED: _ClassVar[ShoppingAddProductsToCampaignRecommendationEnum.Reason]
        ADS_ACCOUNT_EXCLUDES_OFFERS_FROM_CAMPAIGN: _ClassVar[ShoppingAddProductsToCampaignRecommendationEnum.Reason]
        ALL_PRODUCTS_ARE_EXCLUDED_FROM_CAMPAIGN: _ClassVar[ShoppingAddProductsToCampaignRecommendationEnum.Reason]
    UNSPECIFIED: ShoppingAddProductsToCampaignRecommendationEnum.Reason
    UNKNOWN: ShoppingAddProductsToCampaignRecommendationEnum.Reason
    MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS: ShoppingAddProductsToCampaignRecommendationEnum.Reason
    MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS_IN_FEED: ShoppingAddProductsToCampaignRecommendationEnum.Reason
    ADS_ACCOUNT_EXCLUDES_OFFERS_FROM_CAMPAIGN: ShoppingAddProductsToCampaignRecommendationEnum.Reason
    ALL_PRODUCTS_ARE_EXCLUDED_FROM_CAMPAIGN: ShoppingAddProductsToCampaignRecommendationEnum.Reason

    def __init__(self) -> None:
        ...