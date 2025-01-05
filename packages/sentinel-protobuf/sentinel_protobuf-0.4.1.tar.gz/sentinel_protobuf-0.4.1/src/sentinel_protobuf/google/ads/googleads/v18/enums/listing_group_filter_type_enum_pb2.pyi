from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupFilterTypeEnum(_message.Message):
    __slots__ = ()

    class ListingGroupFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupFilterTypeEnum.ListingGroupFilterType]
        UNKNOWN: _ClassVar[ListingGroupFilterTypeEnum.ListingGroupFilterType]
        SUBDIVISION: _ClassVar[ListingGroupFilterTypeEnum.ListingGroupFilterType]
        UNIT_INCLUDED: _ClassVar[ListingGroupFilterTypeEnum.ListingGroupFilterType]
        UNIT_EXCLUDED: _ClassVar[ListingGroupFilterTypeEnum.ListingGroupFilterType]
    UNSPECIFIED: ListingGroupFilterTypeEnum.ListingGroupFilterType
    UNKNOWN: ListingGroupFilterTypeEnum.ListingGroupFilterType
    SUBDIVISION: ListingGroupFilterTypeEnum.ListingGroupFilterType
    UNIT_INCLUDED: ListingGroupFilterTypeEnum.ListingGroupFilterType
    UNIT_EXCLUDED: ListingGroupFilterTypeEnum.ListingGroupFilterType

    def __init__(self) -> None:
        ...