from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListingTypeEnum(_message.Message):
    __slots__ = ()

    class ListingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListingTypeEnum.ListingType]
        UNKNOWN: _ClassVar[ListingTypeEnum.ListingType]
        VEHICLES: _ClassVar[ListingTypeEnum.ListingType]
    UNSPECIFIED: ListingTypeEnum.ListingType
    UNKNOWN: ListingTypeEnum.ListingType
    VEHICLES: ListingTypeEnum.ListingType

    def __init__(self) -> None:
        ...