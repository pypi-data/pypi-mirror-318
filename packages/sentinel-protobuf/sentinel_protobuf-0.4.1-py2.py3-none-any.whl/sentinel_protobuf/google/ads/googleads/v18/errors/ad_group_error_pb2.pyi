from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupErrorEnum(_message.Message):
    __slots__ = ()

    class AdGroupError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupErrorEnum.AdGroupError]
        UNKNOWN: _ClassVar[AdGroupErrorEnum.AdGroupError]
        DUPLICATE_ADGROUP_NAME: _ClassVar[AdGroupErrorEnum.AdGroupError]
        INVALID_ADGROUP_NAME: _ClassVar[AdGroupErrorEnum.AdGroupError]
        ADVERTISER_NOT_ON_CONTENT_NETWORK: _ClassVar[AdGroupErrorEnum.AdGroupError]
        BID_TOO_BIG: _ClassVar[AdGroupErrorEnum.AdGroupError]
        BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH: _ClassVar[AdGroupErrorEnum.AdGroupError]
        MISSING_ADGROUP_NAME: _ClassVar[AdGroupErrorEnum.AdGroupError]
        ADGROUP_LABEL_DOES_NOT_EXIST: _ClassVar[AdGroupErrorEnum.AdGroupError]
        ADGROUP_LABEL_ALREADY_EXISTS: _ClassVar[AdGroupErrorEnum.AdGroupError]
        INVALID_CONTENT_BID_CRITERION_TYPE_GROUP: _ClassVar[AdGroupErrorEnum.AdGroupError]
        AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE: _ClassVar[AdGroupErrorEnum.AdGroupError]
        ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY: _ClassVar[AdGroupErrorEnum.AdGroupError]
        CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING: _ClassVar[AdGroupErrorEnum.AdGroupError]
        PROMOTED_HOTEL_AD_GROUPS_NOT_AVAILABLE_FOR_CUSTOMER: _ClassVar[AdGroupErrorEnum.AdGroupError]
        INVALID_EXCLUDED_PARENT_ASSET_FIELD_TYPE: _ClassVar[AdGroupErrorEnum.AdGroupError]
        INVALID_EXCLUDED_PARENT_ASSET_SET_TYPE: _ClassVar[AdGroupErrorEnum.AdGroupError]
        CANNOT_ADD_AD_GROUP_FOR_CAMPAIGN_TYPE: _ClassVar[AdGroupErrorEnum.AdGroupError]
        INVALID_STATUS: _ClassVar[AdGroupErrorEnum.AdGroupError]
    UNSPECIFIED: AdGroupErrorEnum.AdGroupError
    UNKNOWN: AdGroupErrorEnum.AdGroupError
    DUPLICATE_ADGROUP_NAME: AdGroupErrorEnum.AdGroupError
    INVALID_ADGROUP_NAME: AdGroupErrorEnum.AdGroupError
    ADVERTISER_NOT_ON_CONTENT_NETWORK: AdGroupErrorEnum.AdGroupError
    BID_TOO_BIG: AdGroupErrorEnum.AdGroupError
    BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH: AdGroupErrorEnum.AdGroupError
    MISSING_ADGROUP_NAME: AdGroupErrorEnum.AdGroupError
    ADGROUP_LABEL_DOES_NOT_EXIST: AdGroupErrorEnum.AdGroupError
    ADGROUP_LABEL_ALREADY_EXISTS: AdGroupErrorEnum.AdGroupError
    INVALID_CONTENT_BID_CRITERION_TYPE_GROUP: AdGroupErrorEnum.AdGroupError
    AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE: AdGroupErrorEnum.AdGroupError
    ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY: AdGroupErrorEnum.AdGroupError
    CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING: AdGroupErrorEnum.AdGroupError
    PROMOTED_HOTEL_AD_GROUPS_NOT_AVAILABLE_FOR_CUSTOMER: AdGroupErrorEnum.AdGroupError
    INVALID_EXCLUDED_PARENT_ASSET_FIELD_TYPE: AdGroupErrorEnum.AdGroupError
    INVALID_EXCLUDED_PARENT_ASSET_SET_TYPE: AdGroupErrorEnum.AdGroupError
    CANNOT_ADD_AD_GROUP_FOR_CAMPAIGN_TYPE: AdGroupErrorEnum.AdGroupError
    INVALID_STATUS: AdGroupErrorEnum.AdGroupError

    def __init__(self) -> None:
        ...