from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemSetLinkErrorEnum(_message.Message):
    __slots__ = ()

    class FeedItemSetLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemSetLinkErrorEnum.FeedItemSetLinkError]
        UNKNOWN: _ClassVar[FeedItemSetLinkErrorEnum.FeedItemSetLinkError]
        FEED_ID_MISMATCH: _ClassVar[FeedItemSetLinkErrorEnum.FeedItemSetLinkError]
        NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET: _ClassVar[FeedItemSetLinkErrorEnum.FeedItemSetLinkError]
    UNSPECIFIED: FeedItemSetLinkErrorEnum.FeedItemSetLinkError
    UNKNOWN: FeedItemSetLinkErrorEnum.FeedItemSetLinkError
    FEED_ID_MISMATCH: FeedItemSetLinkErrorEnum.FeedItemSetLinkError
    NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET: FeedItemSetLinkErrorEnum.FeedItemSetLinkError

    def __init__(self) -> None:
        ...