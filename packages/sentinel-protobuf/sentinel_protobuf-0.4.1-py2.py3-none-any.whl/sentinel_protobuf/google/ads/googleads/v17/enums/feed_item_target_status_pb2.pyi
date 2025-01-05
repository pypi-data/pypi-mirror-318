from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemTargetStatusEnum(_message.Message):
    __slots__ = ()

    class FeedItemTargetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemTargetStatusEnum.FeedItemTargetStatus]
        UNKNOWN: _ClassVar[FeedItemTargetStatusEnum.FeedItemTargetStatus]
        ENABLED: _ClassVar[FeedItemTargetStatusEnum.FeedItemTargetStatus]
        REMOVED: _ClassVar[FeedItemTargetStatusEnum.FeedItemTargetStatus]
    UNSPECIFIED: FeedItemTargetStatusEnum.FeedItemTargetStatus
    UNKNOWN: FeedItemTargetStatusEnum.FeedItemTargetStatus
    ENABLED: FeedItemTargetStatusEnum.FeedItemTargetStatus
    REMOVED: FeedItemTargetStatusEnum.FeedItemTargetStatus

    def __init__(self) -> None:
        ...