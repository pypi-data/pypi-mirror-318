from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupFilterVerticalEnum(_message.Message):
    __slots__ = ()

    class ListingGroupFilterVertical(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupFilterVerticalEnum.ListingGroupFilterVertical]
        UNKNOWN: _ClassVar[ListingGroupFilterVerticalEnum.ListingGroupFilterVertical]
        SHOPPING: _ClassVar[ListingGroupFilterVerticalEnum.ListingGroupFilterVertical]
    UNSPECIFIED: ListingGroupFilterVerticalEnum.ListingGroupFilterVertical
    UNKNOWN: ListingGroupFilterVerticalEnum.ListingGroupFilterVertical
    SHOPPING: ListingGroupFilterVerticalEnum.ListingGroupFilterVertical

    def __init__(self) -> None:
        ...