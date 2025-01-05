from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupErrorEnum(_message.Message):
    __slots__ = ()

    class AssetGroupError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        UNKNOWN: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        DUPLICATE_NAME: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        CANNOT_ADD_ASSET_GROUP_FOR_CAMPAIGN_TYPE: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        NOT_ENOUGH_HEADLINE_ASSET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        NOT_ENOUGH_LONG_HEADLINE_ASSET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        NOT_ENOUGH_DESCRIPTION_ASSET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        NOT_ENOUGH_BUSINESS_NAME_ASSET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        NOT_ENOUGH_MARKETING_IMAGE_ASSET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        NOT_ENOUGH_SQUARE_MARKETING_IMAGE_ASSET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        NOT_ENOUGH_LOGO_ASSET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        FINAL_URL_SHOPPING_MERCHANT_HOME_PAGE_URL_DOMAINS_DIFFER: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        PATH1_REQUIRED_WHEN_PATH2_IS_SET: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        SHORT_DESCRIPTION_REQUIRED: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        FINAL_URL_REQUIRED: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        FINAL_URL_CONTAINS_INVALID_DOMAIN_NAME: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        AD_CUSTOMIZER_NOT_SUPPORTED: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
        CANNOT_MUTATE_ASSET_GROUP_FOR_REMOVED_CAMPAIGN: _ClassVar[AssetGroupErrorEnum.AssetGroupError]
    UNSPECIFIED: AssetGroupErrorEnum.AssetGroupError
    UNKNOWN: AssetGroupErrorEnum.AssetGroupError
    DUPLICATE_NAME: AssetGroupErrorEnum.AssetGroupError
    CANNOT_ADD_ASSET_GROUP_FOR_CAMPAIGN_TYPE: AssetGroupErrorEnum.AssetGroupError
    NOT_ENOUGH_HEADLINE_ASSET: AssetGroupErrorEnum.AssetGroupError
    NOT_ENOUGH_LONG_HEADLINE_ASSET: AssetGroupErrorEnum.AssetGroupError
    NOT_ENOUGH_DESCRIPTION_ASSET: AssetGroupErrorEnum.AssetGroupError
    NOT_ENOUGH_BUSINESS_NAME_ASSET: AssetGroupErrorEnum.AssetGroupError
    NOT_ENOUGH_MARKETING_IMAGE_ASSET: AssetGroupErrorEnum.AssetGroupError
    NOT_ENOUGH_SQUARE_MARKETING_IMAGE_ASSET: AssetGroupErrorEnum.AssetGroupError
    NOT_ENOUGH_LOGO_ASSET: AssetGroupErrorEnum.AssetGroupError
    FINAL_URL_SHOPPING_MERCHANT_HOME_PAGE_URL_DOMAINS_DIFFER: AssetGroupErrorEnum.AssetGroupError
    PATH1_REQUIRED_WHEN_PATH2_IS_SET: AssetGroupErrorEnum.AssetGroupError
    SHORT_DESCRIPTION_REQUIRED: AssetGroupErrorEnum.AssetGroupError
    FINAL_URL_REQUIRED: AssetGroupErrorEnum.AssetGroupError
    FINAL_URL_CONTAINS_INVALID_DOMAIN_NAME: AssetGroupErrorEnum.AssetGroupError
    AD_CUSTOMIZER_NOT_SUPPORTED: AssetGroupErrorEnum.AssetGroupError
    CANNOT_MUTATE_ASSET_GROUP_FOR_REMOVED_CAMPAIGN: AssetGroupErrorEnum.AssetGroupError

    def __init__(self) -> None:
        ...