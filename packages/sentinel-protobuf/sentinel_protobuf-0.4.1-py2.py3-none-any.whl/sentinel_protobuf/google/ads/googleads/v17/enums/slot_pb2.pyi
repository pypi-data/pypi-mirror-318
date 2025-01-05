from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SlotEnum(_message.Message):
    __slots__ = ()

    class Slot(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SlotEnum.Slot]
        UNKNOWN: _ClassVar[SlotEnum.Slot]
        SEARCH_SIDE: _ClassVar[SlotEnum.Slot]
        SEARCH_TOP: _ClassVar[SlotEnum.Slot]
        SEARCH_OTHER: _ClassVar[SlotEnum.Slot]
        CONTENT: _ClassVar[SlotEnum.Slot]
        SEARCH_PARTNER_TOP: _ClassVar[SlotEnum.Slot]
        SEARCH_PARTNER_OTHER: _ClassVar[SlotEnum.Slot]
        MIXED: _ClassVar[SlotEnum.Slot]
    UNSPECIFIED: SlotEnum.Slot
    UNKNOWN: SlotEnum.Slot
    SEARCH_SIDE: SlotEnum.Slot
    SEARCH_TOP: SlotEnum.Slot
    SEARCH_OTHER: SlotEnum.Slot
    CONTENT: SlotEnum.Slot
    SEARCH_PARTNER_TOP: SlotEnum.Slot
    SEARCH_PARTNER_OTHER: SlotEnum.Slot
    MIXED: SlotEnum.Slot

    def __init__(self) -> None:
        ...