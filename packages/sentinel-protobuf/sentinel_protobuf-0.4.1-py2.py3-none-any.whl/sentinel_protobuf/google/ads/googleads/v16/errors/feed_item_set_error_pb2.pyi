from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemSetErrorEnum(_message.Message):
    __slots__ = ()

    class FeedItemSetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        UNKNOWN: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        FEED_ITEM_SET_REMOVED: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        CANNOT_CLEAR_DYNAMIC_FILTER: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        CANNOT_CREATE_DYNAMIC_FILTER: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        INVALID_FEED_TYPE: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        DUPLICATE_NAME: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
        DYNAMIC_FILTER_INVALID_CHAIN_IDS: _ClassVar[FeedItemSetErrorEnum.FeedItemSetError]
    UNSPECIFIED: FeedItemSetErrorEnum.FeedItemSetError
    UNKNOWN: FeedItemSetErrorEnum.FeedItemSetError
    FEED_ITEM_SET_REMOVED: FeedItemSetErrorEnum.FeedItemSetError
    CANNOT_CLEAR_DYNAMIC_FILTER: FeedItemSetErrorEnum.FeedItemSetError
    CANNOT_CREATE_DYNAMIC_FILTER: FeedItemSetErrorEnum.FeedItemSetError
    INVALID_FEED_TYPE: FeedItemSetErrorEnum.FeedItemSetError
    DUPLICATE_NAME: FeedItemSetErrorEnum.FeedItemSetError
    WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE: FeedItemSetErrorEnum.FeedItemSetError
    DYNAMIC_FILTER_INVALID_CHAIN_IDS: FeedItemSetErrorEnum.FeedItemSetError

    def __init__(self) -> None:
        ...