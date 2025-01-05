from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionActionTypeEnum(_message.Message):
    __slots__ = ()

    class ConversionActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        UNKNOWN: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        AD_CALL: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        CLICK_TO_CALL: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        GOOGLE_PLAY_DOWNLOAD: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        GOOGLE_PLAY_IN_APP_PURCHASE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        UPLOAD_CALLS: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        UPLOAD_CLICKS: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        WEBPAGE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        WEBSITE_CALL: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        STORE_SALES_DIRECT_UPLOAD: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        STORE_SALES: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FIREBASE_ANDROID_FIRST_OPEN: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FIREBASE_ANDROID_IN_APP_PURCHASE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FIREBASE_ANDROID_CUSTOM: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FIREBASE_IOS_FIRST_OPEN: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FIREBASE_IOS_IN_APP_PURCHASE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FIREBASE_IOS_CUSTOM: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        ANDROID_APP_PRE_REGISTRATION: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        ANDROID_INSTALLS_ALL_OTHER_APPS: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FLOODLIGHT_ACTION: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        FLOODLIGHT_TRANSACTION: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        GOOGLE_HOSTED: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        LEAD_FORM_SUBMIT: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        SALESFORCE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        SEARCH_ADS_360: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        SMART_CAMPAIGN_AD_CLICKS_TO_CALL: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        SMART_CAMPAIGN_MAP_CLICKS_TO_CALL: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        SMART_CAMPAIGN_MAP_DIRECTIONS: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        SMART_CAMPAIGN_TRACKED_CALLS: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        STORE_VISITS: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        WEBPAGE_CODELESS: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        UNIVERSAL_ANALYTICS_GOAL: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        UNIVERSAL_ANALYTICS_TRANSACTION: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        GOOGLE_ANALYTICS_4_CUSTOM: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
        GOOGLE_ANALYTICS_4_PURCHASE: _ClassVar[ConversionActionTypeEnum.ConversionActionType]
    UNSPECIFIED: ConversionActionTypeEnum.ConversionActionType
    UNKNOWN: ConversionActionTypeEnum.ConversionActionType
    AD_CALL: ConversionActionTypeEnum.ConversionActionType
    CLICK_TO_CALL: ConversionActionTypeEnum.ConversionActionType
    GOOGLE_PLAY_DOWNLOAD: ConversionActionTypeEnum.ConversionActionType
    GOOGLE_PLAY_IN_APP_PURCHASE: ConversionActionTypeEnum.ConversionActionType
    UPLOAD_CALLS: ConversionActionTypeEnum.ConversionActionType
    UPLOAD_CLICKS: ConversionActionTypeEnum.ConversionActionType
    WEBPAGE: ConversionActionTypeEnum.ConversionActionType
    WEBSITE_CALL: ConversionActionTypeEnum.ConversionActionType
    STORE_SALES_DIRECT_UPLOAD: ConversionActionTypeEnum.ConversionActionType
    STORE_SALES: ConversionActionTypeEnum.ConversionActionType
    FIREBASE_ANDROID_FIRST_OPEN: ConversionActionTypeEnum.ConversionActionType
    FIREBASE_ANDROID_IN_APP_PURCHASE: ConversionActionTypeEnum.ConversionActionType
    FIREBASE_ANDROID_CUSTOM: ConversionActionTypeEnum.ConversionActionType
    FIREBASE_IOS_FIRST_OPEN: ConversionActionTypeEnum.ConversionActionType
    FIREBASE_IOS_IN_APP_PURCHASE: ConversionActionTypeEnum.ConversionActionType
    FIREBASE_IOS_CUSTOM: ConversionActionTypeEnum.ConversionActionType
    THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN: ConversionActionTypeEnum.ConversionActionType
    THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE: ConversionActionTypeEnum.ConversionActionType
    THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM: ConversionActionTypeEnum.ConversionActionType
    THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN: ConversionActionTypeEnum.ConversionActionType
    THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE: ConversionActionTypeEnum.ConversionActionType
    THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM: ConversionActionTypeEnum.ConversionActionType
    ANDROID_APP_PRE_REGISTRATION: ConversionActionTypeEnum.ConversionActionType
    ANDROID_INSTALLS_ALL_OTHER_APPS: ConversionActionTypeEnum.ConversionActionType
    FLOODLIGHT_ACTION: ConversionActionTypeEnum.ConversionActionType
    FLOODLIGHT_TRANSACTION: ConversionActionTypeEnum.ConversionActionType
    GOOGLE_HOSTED: ConversionActionTypeEnum.ConversionActionType
    LEAD_FORM_SUBMIT: ConversionActionTypeEnum.ConversionActionType
    SALESFORCE: ConversionActionTypeEnum.ConversionActionType
    SEARCH_ADS_360: ConversionActionTypeEnum.ConversionActionType
    SMART_CAMPAIGN_AD_CLICKS_TO_CALL: ConversionActionTypeEnum.ConversionActionType
    SMART_CAMPAIGN_MAP_CLICKS_TO_CALL: ConversionActionTypeEnum.ConversionActionType
    SMART_CAMPAIGN_MAP_DIRECTIONS: ConversionActionTypeEnum.ConversionActionType
    SMART_CAMPAIGN_TRACKED_CALLS: ConversionActionTypeEnum.ConversionActionType
    STORE_VISITS: ConversionActionTypeEnum.ConversionActionType
    WEBPAGE_CODELESS: ConversionActionTypeEnum.ConversionActionType
    UNIVERSAL_ANALYTICS_GOAL: ConversionActionTypeEnum.ConversionActionType
    UNIVERSAL_ANALYTICS_TRANSACTION: ConversionActionTypeEnum.ConversionActionType
    GOOGLE_ANALYTICS_4_CUSTOM: ConversionActionTypeEnum.ConversionActionType
    GOOGLE_ANALYTICS_4_PURCHASE: ConversionActionTypeEnum.ConversionActionType

    def __init__(self) -> None:
        ...