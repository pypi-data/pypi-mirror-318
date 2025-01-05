from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetTypeEnum(_message.Message):
    __slots__ = ()

    class AssetSetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSetTypeEnum.AssetSetType]
        UNKNOWN: _ClassVar[AssetSetTypeEnum.AssetSetType]
        PAGE_FEED: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_EDUCATION: _ClassVar[AssetSetTypeEnum.AssetSetType]
        MERCHANT_CENTER_FEED: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_REAL_ESTATE: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_CUSTOM: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_HOTELS_AND_RENTALS: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_FLIGHTS: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_TRAVEL: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_LOCAL: _ClassVar[AssetSetTypeEnum.AssetSetType]
        DYNAMIC_JOBS: _ClassVar[AssetSetTypeEnum.AssetSetType]
        LOCATION_SYNC: _ClassVar[AssetSetTypeEnum.AssetSetType]
        BUSINESS_PROFILE_DYNAMIC_LOCATION_GROUP: _ClassVar[AssetSetTypeEnum.AssetSetType]
        CHAIN_DYNAMIC_LOCATION_GROUP: _ClassVar[AssetSetTypeEnum.AssetSetType]
        STATIC_LOCATION_GROUP: _ClassVar[AssetSetTypeEnum.AssetSetType]
        HOTEL_PROPERTY: _ClassVar[AssetSetTypeEnum.AssetSetType]
        TRAVEL_FEED: _ClassVar[AssetSetTypeEnum.AssetSetType]
    UNSPECIFIED: AssetSetTypeEnum.AssetSetType
    UNKNOWN: AssetSetTypeEnum.AssetSetType
    PAGE_FEED: AssetSetTypeEnum.AssetSetType
    DYNAMIC_EDUCATION: AssetSetTypeEnum.AssetSetType
    MERCHANT_CENTER_FEED: AssetSetTypeEnum.AssetSetType
    DYNAMIC_REAL_ESTATE: AssetSetTypeEnum.AssetSetType
    DYNAMIC_CUSTOM: AssetSetTypeEnum.AssetSetType
    DYNAMIC_HOTELS_AND_RENTALS: AssetSetTypeEnum.AssetSetType
    DYNAMIC_FLIGHTS: AssetSetTypeEnum.AssetSetType
    DYNAMIC_TRAVEL: AssetSetTypeEnum.AssetSetType
    DYNAMIC_LOCAL: AssetSetTypeEnum.AssetSetType
    DYNAMIC_JOBS: AssetSetTypeEnum.AssetSetType
    LOCATION_SYNC: AssetSetTypeEnum.AssetSetType
    BUSINESS_PROFILE_DYNAMIC_LOCATION_GROUP: AssetSetTypeEnum.AssetSetType
    CHAIN_DYNAMIC_LOCATION_GROUP: AssetSetTypeEnum.AssetSetType
    STATIC_LOCATION_GROUP: AssetSetTypeEnum.AssetSetType
    HOTEL_PROPERTY: AssetSetTypeEnum.AssetSetType
    TRAVEL_FEED: AssetSetTypeEnum.AssetSetType

    def __init__(self) -> None:
        ...