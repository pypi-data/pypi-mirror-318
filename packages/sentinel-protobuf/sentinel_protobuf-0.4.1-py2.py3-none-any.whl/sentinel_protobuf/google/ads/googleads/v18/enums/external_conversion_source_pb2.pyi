from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExternalConversionSourceEnum(_message.Message):
    __slots__ = ()

    class ExternalConversionSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        UNKNOWN: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        WEBPAGE: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        ANALYTICS: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        UPLOAD: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        AD_CALL_METRICS: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        WEBSITE_CALL_METRICS: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        STORE_VISITS: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        ANDROID_IN_APP: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        IOS_IN_APP: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        IOS_FIRST_OPEN: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        APP_UNSPECIFIED: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        ANDROID_FIRST_OPEN: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        UPLOAD_CALLS: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        FIREBASE: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        CLICK_TO_CALL: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        SALESFORCE: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        STORE_SALES_CRM: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        STORE_SALES_PAYMENT_NETWORK: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        GOOGLE_PLAY: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        THIRD_PARTY_APP_ANALYTICS: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        GOOGLE_ATTRIBUTION: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        STORE_SALES_DIRECT_UPLOAD: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        STORE_SALES: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        SEARCH_ADS_360: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        GOOGLE_HOSTED: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        FLOODLIGHT: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        ANALYTICS_SEARCH_ADS_360: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        FIREBASE_SEARCH_ADS_360: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
        DISPLAY_AND_VIDEO_360_FLOODLIGHT: _ClassVar[ExternalConversionSourceEnum.ExternalConversionSource]
    UNSPECIFIED: ExternalConversionSourceEnum.ExternalConversionSource
    UNKNOWN: ExternalConversionSourceEnum.ExternalConversionSource
    WEBPAGE: ExternalConversionSourceEnum.ExternalConversionSource
    ANALYTICS: ExternalConversionSourceEnum.ExternalConversionSource
    UPLOAD: ExternalConversionSourceEnum.ExternalConversionSource
    AD_CALL_METRICS: ExternalConversionSourceEnum.ExternalConversionSource
    WEBSITE_CALL_METRICS: ExternalConversionSourceEnum.ExternalConversionSource
    STORE_VISITS: ExternalConversionSourceEnum.ExternalConversionSource
    ANDROID_IN_APP: ExternalConversionSourceEnum.ExternalConversionSource
    IOS_IN_APP: ExternalConversionSourceEnum.ExternalConversionSource
    IOS_FIRST_OPEN: ExternalConversionSourceEnum.ExternalConversionSource
    APP_UNSPECIFIED: ExternalConversionSourceEnum.ExternalConversionSource
    ANDROID_FIRST_OPEN: ExternalConversionSourceEnum.ExternalConversionSource
    UPLOAD_CALLS: ExternalConversionSourceEnum.ExternalConversionSource
    FIREBASE: ExternalConversionSourceEnum.ExternalConversionSource
    CLICK_TO_CALL: ExternalConversionSourceEnum.ExternalConversionSource
    SALESFORCE: ExternalConversionSourceEnum.ExternalConversionSource
    STORE_SALES_CRM: ExternalConversionSourceEnum.ExternalConversionSource
    STORE_SALES_PAYMENT_NETWORK: ExternalConversionSourceEnum.ExternalConversionSource
    GOOGLE_PLAY: ExternalConversionSourceEnum.ExternalConversionSource
    THIRD_PARTY_APP_ANALYTICS: ExternalConversionSourceEnum.ExternalConversionSource
    GOOGLE_ATTRIBUTION: ExternalConversionSourceEnum.ExternalConversionSource
    STORE_SALES_DIRECT_UPLOAD: ExternalConversionSourceEnum.ExternalConversionSource
    STORE_SALES: ExternalConversionSourceEnum.ExternalConversionSource
    SEARCH_ADS_360: ExternalConversionSourceEnum.ExternalConversionSource
    GOOGLE_HOSTED: ExternalConversionSourceEnum.ExternalConversionSource
    FLOODLIGHT: ExternalConversionSourceEnum.ExternalConversionSource
    ANALYTICS_SEARCH_ADS_360: ExternalConversionSourceEnum.ExternalConversionSource
    FIREBASE_SEARCH_ADS_360: ExternalConversionSourceEnum.ExternalConversionSource
    DISPLAY_AND_VIDEO_360_FLOODLIGHT: ExternalConversionSourceEnum.ExternalConversionSource

    def __init__(self) -> None:
        ...