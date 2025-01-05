from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InteractionEventTypeEnum(_message.Message):
    __slots__ = ()

    class InteractionEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InteractionEventTypeEnum.InteractionEventType]
        UNKNOWN: _ClassVar[InteractionEventTypeEnum.InteractionEventType]
        CLICK: _ClassVar[InteractionEventTypeEnum.InteractionEventType]
        ENGAGEMENT: _ClassVar[InteractionEventTypeEnum.InteractionEventType]
        VIDEO_VIEW: _ClassVar[InteractionEventTypeEnum.InteractionEventType]
        NONE: _ClassVar[InteractionEventTypeEnum.InteractionEventType]
    UNSPECIFIED: InteractionEventTypeEnum.InteractionEventType
    UNKNOWN: InteractionEventTypeEnum.InteractionEventType
    CLICK: InteractionEventTypeEnum.InteractionEventType
    ENGAGEMENT: InteractionEventTypeEnum.InteractionEventType
    VIDEO_VIEW: InteractionEventTypeEnum.InteractionEventType
    NONE: InteractionEventTypeEnum.InteractionEventType

    def __init__(self) -> None:
        ...