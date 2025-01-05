from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FrequencyCapEventTypeEnum(_message.Message):
    __slots__ = ()

    class FrequencyCapEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FrequencyCapEventTypeEnum.FrequencyCapEventType]
        UNKNOWN: _ClassVar[FrequencyCapEventTypeEnum.FrequencyCapEventType]
        IMPRESSION: _ClassVar[FrequencyCapEventTypeEnum.FrequencyCapEventType]
        VIDEO_VIEW: _ClassVar[FrequencyCapEventTypeEnum.FrequencyCapEventType]
    UNSPECIFIED: FrequencyCapEventTypeEnum.FrequencyCapEventType
    UNKNOWN: FrequencyCapEventTypeEnum.FrequencyCapEventType
    IMPRESSION: FrequencyCapEventTypeEnum.FrequencyCapEventType
    VIDEO_VIEW: FrequencyCapEventTypeEnum.FrequencyCapEventType

    def __init__(self) -> None:
        ...