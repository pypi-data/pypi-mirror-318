from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupTypeEnum(_message.Message):
    __slots__ = ()

    class ListingGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupTypeEnum.ListingGroupType]
        UNKNOWN: _ClassVar[ListingGroupTypeEnum.ListingGroupType]
        SUBDIVISION: _ClassVar[ListingGroupTypeEnum.ListingGroupType]
        UNIT: _ClassVar[ListingGroupTypeEnum.ListingGroupType]
    UNSPECIFIED: ListingGroupTypeEnum.ListingGroupType
    UNKNOWN: ListingGroupTypeEnum.ListingGroupType
    SUBDIVISION: ListingGroupTypeEnum.ListingGroupType
    UNIT: ListingGroupTypeEnum.ListingGroupType

    def __init__(self) -> None:
        ...