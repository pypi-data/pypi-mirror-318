from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeStatusResourceTypeEnum(_message.Message):
    __slots__ = ()

    class ChangeStatusResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        UNKNOWN: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        AD_GROUP: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        AD_GROUP_AD: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        AD_GROUP_CRITERION: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        CAMPAIGN: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        CAMPAIGN_CRITERION: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        FEED: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        FEED_ITEM: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        AD_GROUP_FEED: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        CAMPAIGN_FEED: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        AD_GROUP_BID_MODIFIER: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        SHARED_SET: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        CAMPAIGN_SHARED_SET: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        ASSET: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        CUSTOMER_ASSET: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        CAMPAIGN_ASSET: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        AD_GROUP_ASSET: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
        COMBINED_AUDIENCE: _ClassVar[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]
    UNSPECIFIED: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    UNKNOWN: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    AD_GROUP: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    AD_GROUP_AD: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    AD_GROUP_CRITERION: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    CAMPAIGN: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    CAMPAIGN_CRITERION: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    FEED: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    FEED_ITEM: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    AD_GROUP_FEED: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    CAMPAIGN_FEED: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    AD_GROUP_BID_MODIFIER: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    SHARED_SET: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    CAMPAIGN_SHARED_SET: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    ASSET: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    CUSTOMER_ASSET: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    CAMPAIGN_ASSET: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    AD_GROUP_ASSET: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    COMBINED_AUDIENCE: ChangeStatusResourceTypeEnum.ChangeStatusResourceType

    def __init__(self) -> None:
        ...