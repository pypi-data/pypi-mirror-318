from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SeasonalityEventStatusEnum(_message.Message):
    __slots__ = ()

    class SeasonalityEventStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SeasonalityEventStatusEnum.SeasonalityEventStatus]
        UNKNOWN: _ClassVar[SeasonalityEventStatusEnum.SeasonalityEventStatus]
        ENABLED: _ClassVar[SeasonalityEventStatusEnum.SeasonalityEventStatus]
        REMOVED: _ClassVar[SeasonalityEventStatusEnum.SeasonalityEventStatus]
    UNSPECIFIED: SeasonalityEventStatusEnum.SeasonalityEventStatus
    UNKNOWN: SeasonalityEventStatusEnum.SeasonalityEventStatus
    ENABLED: SeasonalityEventStatusEnum.SeasonalityEventStatus
    REMOVED: SeasonalityEventStatusEnum.SeasonalityEventStatus

    def __init__(self) -> None:
        ...