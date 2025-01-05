from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedStatusEnum(_message.Message):
    __slots__ = ()

    class FeedStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedStatusEnum.FeedStatus]
        UNKNOWN: _ClassVar[FeedStatusEnum.FeedStatus]
        ENABLED: _ClassVar[FeedStatusEnum.FeedStatus]
        REMOVED: _ClassVar[FeedStatusEnum.FeedStatus]
    UNSPECIFIED: FeedStatusEnum.FeedStatus
    UNKNOWN: FeedStatusEnum.FeedStatus
    ENABLED: FeedStatusEnum.FeedStatus
    REMOVED: FeedStatusEnum.FeedStatus

    def __init__(self) -> None:
        ...