from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedMappingStatusEnum(_message.Message):
    __slots__ = ()

    class FeedMappingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedMappingStatusEnum.FeedMappingStatus]
        UNKNOWN: _ClassVar[FeedMappingStatusEnum.FeedMappingStatus]
        ENABLED: _ClassVar[FeedMappingStatusEnum.FeedMappingStatus]
        REMOVED: _ClassVar[FeedMappingStatusEnum.FeedMappingStatus]
    UNSPECIFIED: FeedMappingStatusEnum.FeedMappingStatus
    UNKNOWN: FeedMappingStatusEnum.FeedMappingStatus
    ENABLED: FeedMappingStatusEnum.FeedMappingStatus
    REMOVED: FeedMappingStatusEnum.FeedMappingStatus

    def __init__(self) -> None:
        ...