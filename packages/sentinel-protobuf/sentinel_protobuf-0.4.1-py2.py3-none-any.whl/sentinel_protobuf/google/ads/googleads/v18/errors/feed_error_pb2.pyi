from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedErrorEnum(_message.Message):
    __slots__ = ()

    class FeedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedErrorEnum.FeedError]
        UNKNOWN: _ClassVar[FeedErrorEnum.FeedError]
        ATTRIBUTE_NAMES_NOT_UNIQUE: _ClassVar[FeedErrorEnum.FeedError]
        ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES: _ClassVar[FeedErrorEnum.FeedError]
        CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED: _ClassVar[FeedErrorEnum.FeedError]
        CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED: _ClassVar[FeedErrorEnum.FeedError]
        CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED: _ClassVar[FeedErrorEnum.FeedError]
        CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE: _ClassVar[FeedErrorEnum.FeedError]
        FEED_REMOVED: _ClassVar[FeedErrorEnum.FeedError]
        INVALID_ORIGIN_VALUE: _ClassVar[FeedErrorEnum.FeedError]
        FEED_ORIGIN_IS_NOT_USER: _ClassVar[FeedErrorEnum.FeedError]
        INVALID_AUTH_TOKEN_FOR_EMAIL: _ClassVar[FeedErrorEnum.FeedError]
        INVALID_EMAIL: _ClassVar[FeedErrorEnum.FeedError]
        DUPLICATE_FEED_NAME: _ClassVar[FeedErrorEnum.FeedError]
        INVALID_FEED_NAME: _ClassVar[FeedErrorEnum.FeedError]
        MISSING_OAUTH_INFO: _ClassVar[FeedErrorEnum.FeedError]
        NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY: _ClassVar[FeedErrorEnum.FeedError]
        TOO_MANY_ATTRIBUTES: _ClassVar[FeedErrorEnum.FeedError]
        INVALID_BUSINESS_ACCOUNT: _ClassVar[FeedErrorEnum.FeedError]
        BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT: _ClassVar[FeedErrorEnum.FeedError]
        INVALID_AFFILIATE_CHAIN_ID: _ClassVar[FeedErrorEnum.FeedError]
        DUPLICATE_SYSTEM_FEED: _ClassVar[FeedErrorEnum.FeedError]
        GMB_ACCESS_ERROR: _ClassVar[FeedErrorEnum.FeedError]
        CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS: _ClassVar[FeedErrorEnum.FeedError]
        LEGACY_EXTENSION_TYPE_READ_ONLY: _ClassVar[FeedErrorEnum.FeedError]
    UNSPECIFIED: FeedErrorEnum.FeedError
    UNKNOWN: FeedErrorEnum.FeedError
    ATTRIBUTE_NAMES_NOT_UNIQUE: FeedErrorEnum.FeedError
    ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES: FeedErrorEnum.FeedError
    CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED: FeedErrorEnum.FeedError
    CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED: FeedErrorEnum.FeedError
    CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED: FeedErrorEnum.FeedError
    CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE: FeedErrorEnum.FeedError
    FEED_REMOVED: FeedErrorEnum.FeedError
    INVALID_ORIGIN_VALUE: FeedErrorEnum.FeedError
    FEED_ORIGIN_IS_NOT_USER: FeedErrorEnum.FeedError
    INVALID_AUTH_TOKEN_FOR_EMAIL: FeedErrorEnum.FeedError
    INVALID_EMAIL: FeedErrorEnum.FeedError
    DUPLICATE_FEED_NAME: FeedErrorEnum.FeedError
    INVALID_FEED_NAME: FeedErrorEnum.FeedError
    MISSING_OAUTH_INFO: FeedErrorEnum.FeedError
    NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY: FeedErrorEnum.FeedError
    TOO_MANY_ATTRIBUTES: FeedErrorEnum.FeedError
    INVALID_BUSINESS_ACCOUNT: FeedErrorEnum.FeedError
    BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT: FeedErrorEnum.FeedError
    INVALID_AFFILIATE_CHAIN_ID: FeedErrorEnum.FeedError
    DUPLICATE_SYSTEM_FEED: FeedErrorEnum.FeedError
    GMB_ACCESS_ERROR: FeedErrorEnum.FeedError
    CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS: FeedErrorEnum.FeedError
    LEGACY_EXTENSION_TYPE_READ_ONLY: FeedErrorEnum.FeedError

    def __init__(self) -> None:
        ...