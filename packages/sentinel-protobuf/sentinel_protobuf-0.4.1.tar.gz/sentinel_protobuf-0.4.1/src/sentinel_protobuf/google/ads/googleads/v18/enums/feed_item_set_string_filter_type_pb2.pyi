from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemSetStringFilterTypeEnum(_message.Message):
    __slots__ = ()

    class FeedItemSetStringFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType]
        UNKNOWN: _ClassVar[FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType]
        EXACT: _ClassVar[FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType]
    UNSPECIFIED: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType
    UNKNOWN: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType
    EXACT: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType

    def __init__(self) -> None:
        ...