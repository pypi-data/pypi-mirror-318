from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupFilterProductChannelEnum(_message.Message):
    __slots__ = ()

    class ListingGroupFilterProductChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel]
        UNKNOWN: _ClassVar[ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel]
        ONLINE: _ClassVar[ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel]
        LOCAL: _ClassVar[ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel]
    UNSPECIFIED: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
    UNKNOWN: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
    ONLINE: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
    LOCAL: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel

    def __init__(self) -> None:
        ...