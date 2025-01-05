from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemErrorEnum(_message.Message):
    __slots__ = ()

    class FeedItemError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemErrorEnum.FeedItemError]
        UNKNOWN: _ClassVar[FeedItemErrorEnum.FeedItemError]
        CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING: _ClassVar[FeedItemErrorEnum.FeedItemError]
        CANNOT_OPERATE_ON_REMOVED_FEED_ITEM: _ClassVar[FeedItemErrorEnum.FeedItemError]
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE: _ClassVar[FeedItemErrorEnum.FeedItemError]
        KEY_ATTRIBUTES_NOT_FOUND: _ClassVar[FeedItemErrorEnum.FeedItemError]
        INVALID_URL: _ClassVar[FeedItemErrorEnum.FeedItemError]
        MISSING_KEY_ATTRIBUTES: _ClassVar[FeedItemErrorEnum.FeedItemError]
        KEY_ATTRIBUTES_NOT_UNIQUE: _ClassVar[FeedItemErrorEnum.FeedItemError]
        CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE: _ClassVar[FeedItemErrorEnum.FeedItemError]
        SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE: _ClassVar[FeedItemErrorEnum.FeedItemError]
        LEGACY_FEED_TYPE_READ_ONLY: _ClassVar[FeedItemErrorEnum.FeedItemError]
    UNSPECIFIED: FeedItemErrorEnum.FeedItemError
    UNKNOWN: FeedItemErrorEnum.FeedItemError
    CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING: FeedItemErrorEnum.FeedItemError
    CANNOT_OPERATE_ON_REMOVED_FEED_ITEM: FeedItemErrorEnum.FeedItemError
    DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE: FeedItemErrorEnum.FeedItemError
    KEY_ATTRIBUTES_NOT_FOUND: FeedItemErrorEnum.FeedItemError
    INVALID_URL: FeedItemErrorEnum.FeedItemError
    MISSING_KEY_ATTRIBUTES: FeedItemErrorEnum.FeedItemError
    KEY_ATTRIBUTES_NOT_UNIQUE: FeedItemErrorEnum.FeedItemError
    CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE: FeedItemErrorEnum.FeedItemError
    SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE: FeedItemErrorEnum.FeedItemError
    LEGACY_FEED_TYPE_READ_ONLY: FeedItemErrorEnum.FeedItemError

    def __init__(self) -> None:
        ...