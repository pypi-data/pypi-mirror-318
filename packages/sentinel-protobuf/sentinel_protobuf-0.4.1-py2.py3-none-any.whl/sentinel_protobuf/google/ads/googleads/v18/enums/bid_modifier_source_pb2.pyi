from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BidModifierSourceEnum(_message.Message):
    __slots__ = ()

    class BidModifierSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BidModifierSourceEnum.BidModifierSource]
        UNKNOWN: _ClassVar[BidModifierSourceEnum.BidModifierSource]
        CAMPAIGN: _ClassVar[BidModifierSourceEnum.BidModifierSource]
        AD_GROUP: _ClassVar[BidModifierSourceEnum.BidModifierSource]
    UNSPECIFIED: BidModifierSourceEnum.BidModifierSource
    UNKNOWN: BidModifierSourceEnum.BidModifierSource
    CAMPAIGN: BidModifierSourceEnum.BidModifierSource
    AD_GROUP: BidModifierSourceEnum.BidModifierSource

    def __init__(self) -> None:
        ...