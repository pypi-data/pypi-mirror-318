from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignFeedErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignFeedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        UNKNOWN: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        CANNOT_CREATE_FOR_REMOVED_FEED: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        INVALID_PLACEHOLDER_TYPE: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        NO_EXISTING_LOCATION_CUSTOMER_FEED: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
        LEGACY_FEED_TYPE_READ_ONLY: _ClassVar[CampaignFeedErrorEnum.CampaignFeedError]
    UNSPECIFIED: CampaignFeedErrorEnum.CampaignFeedError
    UNKNOWN: CampaignFeedErrorEnum.CampaignFeedError
    FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError
    CANNOT_CREATE_FOR_REMOVED_FEED: CampaignFeedErrorEnum.CampaignFeedError
    CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED: CampaignFeedErrorEnum.CampaignFeedError
    CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED: CampaignFeedErrorEnum.CampaignFeedError
    INVALID_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError
    MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError
    NO_EXISTING_LOCATION_CUSTOMER_FEED: CampaignFeedErrorEnum.CampaignFeedError
    LEGACY_FEED_TYPE_READ_ONLY: CampaignFeedErrorEnum.CampaignFeedError

    def __init__(self) -> None:
        ...