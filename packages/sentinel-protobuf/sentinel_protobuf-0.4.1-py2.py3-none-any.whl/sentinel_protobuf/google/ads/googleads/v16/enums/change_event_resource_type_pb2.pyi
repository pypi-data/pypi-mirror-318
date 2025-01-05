from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeEventResourceTypeEnum(_message.Message):
    __slots__ = ()

    class ChangeEventResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        UNKNOWN: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        AD: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        AD_GROUP: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        AD_GROUP_CRITERION: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        CAMPAIGN: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        CAMPAIGN_BUDGET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        AD_GROUP_BID_MODIFIER: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        CAMPAIGN_CRITERION: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        FEED: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        FEED_ITEM: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        CAMPAIGN_FEED: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        AD_GROUP_FEED: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        AD_GROUP_AD: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        ASSET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        CUSTOMER_ASSET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        CAMPAIGN_ASSET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        AD_GROUP_ASSET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        ASSET_SET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        ASSET_SET_ASSET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
        CAMPAIGN_ASSET_SET: _ClassVar[ChangeEventResourceTypeEnum.ChangeEventResourceType]
    UNSPECIFIED: ChangeEventResourceTypeEnum.ChangeEventResourceType
    UNKNOWN: ChangeEventResourceTypeEnum.ChangeEventResourceType
    AD: ChangeEventResourceTypeEnum.ChangeEventResourceType
    AD_GROUP: ChangeEventResourceTypeEnum.ChangeEventResourceType
    AD_GROUP_CRITERION: ChangeEventResourceTypeEnum.ChangeEventResourceType
    CAMPAIGN: ChangeEventResourceTypeEnum.ChangeEventResourceType
    CAMPAIGN_BUDGET: ChangeEventResourceTypeEnum.ChangeEventResourceType
    AD_GROUP_BID_MODIFIER: ChangeEventResourceTypeEnum.ChangeEventResourceType
    CAMPAIGN_CRITERION: ChangeEventResourceTypeEnum.ChangeEventResourceType
    FEED: ChangeEventResourceTypeEnum.ChangeEventResourceType
    FEED_ITEM: ChangeEventResourceTypeEnum.ChangeEventResourceType
    CAMPAIGN_FEED: ChangeEventResourceTypeEnum.ChangeEventResourceType
    AD_GROUP_FEED: ChangeEventResourceTypeEnum.ChangeEventResourceType
    AD_GROUP_AD: ChangeEventResourceTypeEnum.ChangeEventResourceType
    ASSET: ChangeEventResourceTypeEnum.ChangeEventResourceType
    CUSTOMER_ASSET: ChangeEventResourceTypeEnum.ChangeEventResourceType
    CAMPAIGN_ASSET: ChangeEventResourceTypeEnum.ChangeEventResourceType
    AD_GROUP_ASSET: ChangeEventResourceTypeEnum.ChangeEventResourceType
    ASSET_SET: ChangeEventResourceTypeEnum.ChangeEventResourceType
    ASSET_SET_ASSET: ChangeEventResourceTypeEnum.ChangeEventResourceType
    CAMPAIGN_ASSET_SET: ChangeEventResourceTypeEnum.ChangeEventResourceType

    def __init__(self) -> None:
        ...