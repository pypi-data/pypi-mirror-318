from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupFeedErrorEnum(_message.Message):
    __slots__ = ()

    class AdGroupFeedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        UNKNOWN: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        CANNOT_CREATE_FOR_REMOVED_FEED: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        ADGROUP_FEED_ALREADY_EXISTS: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        INVALID_PLACEHOLDER_TYPE: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
        NO_EXISTING_LOCATION_CUSTOMER_FEED: _ClassVar[AdGroupFeedErrorEnum.AdGroupFeedError]
    UNSPECIFIED: AdGroupFeedErrorEnum.AdGroupFeedError
    UNKNOWN: AdGroupFeedErrorEnum.AdGroupFeedError
    FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: AdGroupFeedErrorEnum.AdGroupFeedError
    CANNOT_CREATE_FOR_REMOVED_FEED: AdGroupFeedErrorEnum.AdGroupFeedError
    ADGROUP_FEED_ALREADY_EXISTS: AdGroupFeedErrorEnum.AdGroupFeedError
    CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED: AdGroupFeedErrorEnum.AdGroupFeedError
    INVALID_PLACEHOLDER_TYPE: AdGroupFeedErrorEnum.AdGroupFeedError
    MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: AdGroupFeedErrorEnum.AdGroupFeedError
    NO_EXISTING_LOCATION_CUSTOMER_FEED: AdGroupFeedErrorEnum.AdGroupFeedError

    def __init__(self) -> None:
        ...