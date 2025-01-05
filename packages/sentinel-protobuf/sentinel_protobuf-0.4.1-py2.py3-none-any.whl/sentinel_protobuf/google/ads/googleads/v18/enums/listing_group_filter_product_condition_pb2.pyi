from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingGroupFilterProductConditionEnum(_message.Message):
    __slots__ = ()

    class ListingGroupFilterProductCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition]
        UNKNOWN: _ClassVar[ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition]
        NEW: _ClassVar[ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition]
        REFURBISHED: _ClassVar[ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition]
        USED: _ClassVar[ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition]
    UNSPECIFIED: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    UNKNOWN: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    NEW: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    REFURBISHED: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    USED: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition

    def __init__(self) -> None:
        ...