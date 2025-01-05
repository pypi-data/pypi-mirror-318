from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupFilterProductCategoryLevelEnum(_message.Message):
    __slots__ = ()

    class ListingGroupFilterProductCategoryLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel]
        UNKNOWN: _ClassVar[ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel]
        LEVEL1: _ClassVar[ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel]
        LEVEL2: _ClassVar[ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel]
        LEVEL3: _ClassVar[ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel]
        LEVEL4: _ClassVar[ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel]
        LEVEL5: _ClassVar[ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel]
    UNSPECIFIED: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    UNKNOWN: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    LEVEL1: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    LEVEL2: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    LEVEL3: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    LEVEL4: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    LEVEL5: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel

    def __init__(self) -> None:
        ...