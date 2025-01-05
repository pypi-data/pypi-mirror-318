from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemStatusEnum(_message.Message):
    __slots__ = ()

    class FeedItemStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemStatusEnum.FeedItemStatus]
        UNKNOWN: _ClassVar[FeedItemStatusEnum.FeedItemStatus]
        ENABLED: _ClassVar[FeedItemStatusEnum.FeedItemStatus]
        REMOVED: _ClassVar[FeedItemStatusEnum.FeedItemStatus]
    UNSPECIFIED: FeedItemStatusEnum.FeedItemStatus
    UNKNOWN: FeedItemStatusEnum.FeedItemStatus
    ENABLED: FeedItemStatusEnum.FeedItemStatus
    REMOVED: FeedItemStatusEnum.FeedItemStatus

    def __init__(self) -> None:
        ...