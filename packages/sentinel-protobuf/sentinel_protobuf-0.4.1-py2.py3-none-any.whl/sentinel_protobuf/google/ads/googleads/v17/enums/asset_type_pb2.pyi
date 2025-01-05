from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetTypeEnum(_message.Message):
    __slots__ = ()

    class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetTypeEnum.AssetType]
        UNKNOWN: _ClassVar[AssetTypeEnum.AssetType]
        YOUTUBE_VIDEO: _ClassVar[AssetTypeEnum.AssetType]
        MEDIA_BUNDLE: _ClassVar[AssetTypeEnum.AssetType]
        IMAGE: _ClassVar[AssetTypeEnum.AssetType]
        TEXT: _ClassVar[AssetTypeEnum.AssetType]
        LEAD_FORM: _ClassVar[AssetTypeEnum.AssetType]
        BOOK_ON_GOOGLE: _ClassVar[AssetTypeEnum.AssetType]
        PROMOTION: _ClassVar[AssetTypeEnum.AssetType]
        CALLOUT: _ClassVar[AssetTypeEnum.AssetType]
        STRUCTURED_SNIPPET: _ClassVar[AssetTypeEnum.AssetType]
        SITELINK: _ClassVar[AssetTypeEnum.AssetType]
        PAGE_FEED: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_EDUCATION: _ClassVar[AssetTypeEnum.AssetType]
        MOBILE_APP: _ClassVar[AssetTypeEnum.AssetType]
        HOTEL_CALLOUT: _ClassVar[AssetTypeEnum.AssetType]
        CALL: _ClassVar[AssetTypeEnum.AssetType]
        PRICE: _ClassVar[AssetTypeEnum.AssetType]
        CALL_TO_ACTION: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_REAL_ESTATE: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_CUSTOM: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_HOTELS_AND_RENTALS: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_FLIGHTS: _ClassVar[AssetTypeEnum.AssetType]
        DISCOVERY_CAROUSEL_CARD: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_TRAVEL: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_LOCAL: _ClassVar[AssetTypeEnum.AssetType]
        DYNAMIC_JOBS: _ClassVar[AssetTypeEnum.AssetType]
        LOCATION: _ClassVar[AssetTypeEnum.AssetType]
        HOTEL_PROPERTY: _ClassVar[AssetTypeEnum.AssetType]
    UNSPECIFIED: AssetTypeEnum.AssetType
    UNKNOWN: AssetTypeEnum.AssetType
    YOUTUBE_VIDEO: AssetTypeEnum.AssetType
    MEDIA_BUNDLE: AssetTypeEnum.AssetType
    IMAGE: AssetTypeEnum.AssetType
    TEXT: AssetTypeEnum.AssetType
    LEAD_FORM: AssetTypeEnum.AssetType
    BOOK_ON_GOOGLE: AssetTypeEnum.AssetType
    PROMOTION: AssetTypeEnum.AssetType
    CALLOUT: AssetTypeEnum.AssetType
    STRUCTURED_SNIPPET: AssetTypeEnum.AssetType
    SITELINK: AssetTypeEnum.AssetType
    PAGE_FEED: AssetTypeEnum.AssetType
    DYNAMIC_EDUCATION: AssetTypeEnum.AssetType
    MOBILE_APP: AssetTypeEnum.AssetType
    HOTEL_CALLOUT: AssetTypeEnum.AssetType
    CALL: AssetTypeEnum.AssetType
    PRICE: AssetTypeEnum.AssetType
    CALL_TO_ACTION: AssetTypeEnum.AssetType
    DYNAMIC_REAL_ESTATE: AssetTypeEnum.AssetType
    DYNAMIC_CUSTOM: AssetTypeEnum.AssetType
    DYNAMIC_HOTELS_AND_RENTALS: AssetTypeEnum.AssetType
    DYNAMIC_FLIGHTS: AssetTypeEnum.AssetType
    DISCOVERY_CAROUSEL_CARD: AssetTypeEnum.AssetType
    DYNAMIC_TRAVEL: AssetTypeEnum.AssetType
    DYNAMIC_LOCAL: AssetTypeEnum.AssetType
    DYNAMIC_JOBS: AssetTypeEnum.AssetType
    LOCATION: AssetTypeEnum.AssetType
    HOTEL_PROPERTY: AssetTypeEnum.AssetType

    def __init__(self) -> None:
        ...