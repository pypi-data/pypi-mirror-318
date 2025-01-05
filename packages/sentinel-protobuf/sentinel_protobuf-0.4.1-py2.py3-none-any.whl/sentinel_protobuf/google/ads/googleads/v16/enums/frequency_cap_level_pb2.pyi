from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FrequencyCapLevelEnum(_message.Message):
    __slots__ = ()

    class FrequencyCapLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FrequencyCapLevelEnum.FrequencyCapLevel]
        UNKNOWN: _ClassVar[FrequencyCapLevelEnum.FrequencyCapLevel]
        AD_GROUP_AD: _ClassVar[FrequencyCapLevelEnum.FrequencyCapLevel]
        AD_GROUP: _ClassVar[FrequencyCapLevelEnum.FrequencyCapLevel]
        CAMPAIGN: _ClassVar[FrequencyCapLevelEnum.FrequencyCapLevel]
    UNSPECIFIED: FrequencyCapLevelEnum.FrequencyCapLevel
    UNKNOWN: FrequencyCapLevelEnum.FrequencyCapLevel
    AD_GROUP_AD: FrequencyCapLevelEnum.FrequencyCapLevel
    AD_GROUP: FrequencyCapLevelEnum.FrequencyCapLevel
    CAMPAIGN: FrequencyCapLevelEnum.FrequencyCapLevel

    def __init__(self) -> None:
        ...