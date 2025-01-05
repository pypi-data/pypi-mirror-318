from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LookalikeExpansionLevelEnum(_message.Message):
    __slots__ = ()

    class LookalikeExpansionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LookalikeExpansionLevelEnum.LookalikeExpansionLevel]
        UNKNOWN: _ClassVar[LookalikeExpansionLevelEnum.LookalikeExpansionLevel]
        NARROW: _ClassVar[LookalikeExpansionLevelEnum.LookalikeExpansionLevel]
        BALANCED: _ClassVar[LookalikeExpansionLevelEnum.LookalikeExpansionLevel]
        BROAD: _ClassVar[LookalikeExpansionLevelEnum.LookalikeExpansionLevel]
    UNSPECIFIED: LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    UNKNOWN: LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    NARROW: LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    BALANCED: LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    BROAD: LookalikeExpansionLevelEnum.LookalikeExpansionLevel

    def __init__(self) -> None:
        ...