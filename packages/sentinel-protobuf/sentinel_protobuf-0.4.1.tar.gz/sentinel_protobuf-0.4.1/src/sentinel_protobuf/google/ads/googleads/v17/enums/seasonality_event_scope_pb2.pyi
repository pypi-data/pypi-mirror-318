from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SeasonalityEventScopeEnum(_message.Message):
    __slots__ = ()

    class SeasonalityEventScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SeasonalityEventScopeEnum.SeasonalityEventScope]
        UNKNOWN: _ClassVar[SeasonalityEventScopeEnum.SeasonalityEventScope]
        CUSTOMER: _ClassVar[SeasonalityEventScopeEnum.SeasonalityEventScope]
        CAMPAIGN: _ClassVar[SeasonalityEventScopeEnum.SeasonalityEventScope]
        CHANNEL: _ClassVar[SeasonalityEventScopeEnum.SeasonalityEventScope]
    UNSPECIFIED: SeasonalityEventScopeEnum.SeasonalityEventScope
    UNKNOWN: SeasonalityEventScopeEnum.SeasonalityEventScope
    CUSTOMER: SeasonalityEventScopeEnum.SeasonalityEventScope
    CAMPAIGN: SeasonalityEventScopeEnum.SeasonalityEventScope
    CHANNEL: SeasonalityEventScopeEnum.SeasonalityEventScope

    def __init__(self) -> None:
        ...