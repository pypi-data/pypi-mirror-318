from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemSetStatusEnum(_message.Message):
    __slots__ = ()

    class FeedItemSetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemSetStatusEnum.FeedItemSetStatus]
        UNKNOWN: _ClassVar[FeedItemSetStatusEnum.FeedItemSetStatus]
        ENABLED: _ClassVar[FeedItemSetStatusEnum.FeedItemSetStatus]
        REMOVED: _ClassVar[FeedItemSetStatusEnum.FeedItemSetStatus]
    UNSPECIFIED: FeedItemSetStatusEnum.FeedItemSetStatus
    UNKNOWN: FeedItemSetStatusEnum.FeedItemSetStatus
    ENABLED: FeedItemSetStatusEnum.FeedItemSetStatus
    REMOVED: FeedItemSetStatusEnum.FeedItemSetStatus

    def __init__(self) -> None:
        ...