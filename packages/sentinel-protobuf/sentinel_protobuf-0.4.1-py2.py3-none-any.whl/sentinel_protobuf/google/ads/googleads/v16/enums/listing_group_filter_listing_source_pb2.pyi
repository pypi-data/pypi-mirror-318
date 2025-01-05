from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupFilterListingSourceEnum(_message.Message):
    __slots__ = ()

    class ListingGroupFilterListingSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource]
        UNKNOWN: _ClassVar[ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource]
        SHOPPING: _ClassVar[ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource]
        WEBPAGE: _ClassVar[ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource]
    UNSPECIFIED: ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    UNKNOWN: ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    SHOPPING: ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    WEBPAGE: ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource

    def __init__(self) -> None:
        ...