from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class HotelDateSelectionTypeEnum(_message.Message):
    __slots__ = ()

    class HotelDateSelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[HotelDateSelectionTypeEnum.HotelDateSelectionType]
        UNKNOWN: _ClassVar[HotelDateSelectionTypeEnum.HotelDateSelectionType]
        DEFAULT_SELECTION: _ClassVar[HotelDateSelectionTypeEnum.HotelDateSelectionType]
        USER_SELECTED: _ClassVar[HotelDateSelectionTypeEnum.HotelDateSelectionType]
    UNSPECIFIED: HotelDateSelectionTypeEnum.HotelDateSelectionType
    UNKNOWN: HotelDateSelectionTypeEnum.HotelDateSelectionType
    DEFAULT_SELECTION: HotelDateSelectionTypeEnum.HotelDateSelectionType
    USER_SELECTED: HotelDateSelectionTypeEnum.HotelDateSelectionType

    def __init__(self) -> None:
        ...