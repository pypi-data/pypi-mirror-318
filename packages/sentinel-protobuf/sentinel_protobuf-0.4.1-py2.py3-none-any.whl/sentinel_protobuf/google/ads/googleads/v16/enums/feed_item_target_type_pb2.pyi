from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemTargetTypeEnum(_message.Message):
    __slots__ = ()

    class FeedItemTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemTargetTypeEnum.FeedItemTargetType]
        UNKNOWN: _ClassVar[FeedItemTargetTypeEnum.FeedItemTargetType]
        CAMPAIGN: _ClassVar[FeedItemTargetTypeEnum.FeedItemTargetType]
        AD_GROUP: _ClassVar[FeedItemTargetTypeEnum.FeedItemTargetType]
        CRITERION: _ClassVar[FeedItemTargetTypeEnum.FeedItemTargetType]
    UNSPECIFIED: FeedItemTargetTypeEnum.FeedItemTargetType
    UNKNOWN: FeedItemTargetTypeEnum.FeedItemTargetType
    CAMPAIGN: FeedItemTargetTypeEnum.FeedItemTargetType
    AD_GROUP: FeedItemTargetTypeEnum.FeedItemTargetType
    CRITERION: FeedItemTargetTypeEnum.FeedItemTargetType

    def __init__(self) -> None:
        ...