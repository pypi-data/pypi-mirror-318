from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemTargetErrorEnum(_message.Message):
    __slots__ = ()

    class FeedItemTargetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        UNKNOWN: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        MUST_SET_TARGET_ONEOF_ON_CREATE: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        FEED_ITEM_TARGET_ALREADY_EXISTS: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        FEED_ITEM_SCHEDULES_CANNOT_OVERLAP: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        TOO_MANY_SCHEDULES_PER_DAY: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        DUPLICATE_AD_SCHEDULE: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
        DUPLICATE_KEYWORD: _ClassVar[FeedItemTargetErrorEnum.FeedItemTargetError]
    UNSPECIFIED: FeedItemTargetErrorEnum.FeedItemTargetError
    UNKNOWN: FeedItemTargetErrorEnum.FeedItemTargetError
    MUST_SET_TARGET_ONEOF_ON_CREATE: FeedItemTargetErrorEnum.FeedItemTargetError
    FEED_ITEM_TARGET_ALREADY_EXISTS: FeedItemTargetErrorEnum.FeedItemTargetError
    FEED_ITEM_SCHEDULES_CANNOT_OVERLAP: FeedItemTargetErrorEnum.FeedItemTargetError
    TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE: FeedItemTargetErrorEnum.FeedItemTargetError
    TOO_MANY_SCHEDULES_PER_DAY: FeedItemTargetErrorEnum.FeedItemTargetError
    CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS: FeedItemTargetErrorEnum.FeedItemTargetError
    DUPLICATE_AD_SCHEDULE: FeedItemTargetErrorEnum.FeedItemTargetError
    DUPLICATE_KEYWORD: FeedItemTargetErrorEnum.FeedItemTargetError

    def __init__(self) -> None:
        ...