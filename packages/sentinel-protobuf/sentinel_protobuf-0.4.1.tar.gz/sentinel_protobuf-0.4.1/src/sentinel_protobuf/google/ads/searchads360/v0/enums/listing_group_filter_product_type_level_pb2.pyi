from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupFilterProductTypeLevelEnum(_message.Message):
    __slots__ = ()

    class ListingGroupFilterProductTypeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel]
        UNKNOWN: _ClassVar[ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel]
        LEVEL1: _ClassVar[ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel]
        LEVEL2: _ClassVar[ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel]
        LEVEL3: _ClassVar[ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel]
        LEVEL4: _ClassVar[ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel]
        LEVEL5: _ClassVar[ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel]
    UNSPECIFIED: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    UNKNOWN: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    LEVEL1: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    LEVEL2: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    LEVEL3: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    LEVEL4: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    LEVEL5: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel

    def __init__(self) -> None:
        ...