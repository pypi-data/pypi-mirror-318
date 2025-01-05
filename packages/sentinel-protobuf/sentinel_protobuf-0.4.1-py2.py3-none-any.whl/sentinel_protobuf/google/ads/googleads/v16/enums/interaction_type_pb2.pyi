from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InteractionTypeEnum(_message.Message):
    __slots__ = ()

    class InteractionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InteractionTypeEnum.InteractionType]
        UNKNOWN: _ClassVar[InteractionTypeEnum.InteractionType]
        CALLS: _ClassVar[InteractionTypeEnum.InteractionType]
    UNSPECIFIED: InteractionTypeEnum.InteractionType
    UNKNOWN: InteractionTypeEnum.InteractionType
    CALLS: InteractionTypeEnum.InteractionType

    def __init__(self) -> None:
        ...