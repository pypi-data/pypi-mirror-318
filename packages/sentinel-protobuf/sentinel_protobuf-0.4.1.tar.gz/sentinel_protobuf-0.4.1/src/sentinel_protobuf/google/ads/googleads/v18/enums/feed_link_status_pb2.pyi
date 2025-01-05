from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedLinkStatusEnum(_message.Message):
    __slots__ = ()

    class FeedLinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedLinkStatusEnum.FeedLinkStatus]
        UNKNOWN: _ClassVar[FeedLinkStatusEnum.FeedLinkStatus]
        ENABLED: _ClassVar[FeedLinkStatusEnum.FeedLinkStatus]
        REMOVED: _ClassVar[FeedLinkStatusEnum.FeedLinkStatus]
    UNSPECIFIED: FeedLinkStatusEnum.FeedLinkStatus
    UNKNOWN: FeedLinkStatusEnum.FeedLinkStatus
    ENABLED: FeedLinkStatusEnum.FeedLinkStatus
    REMOVED: FeedLinkStatusEnum.FeedLinkStatus

    def __init__(self) -> None:
        ...