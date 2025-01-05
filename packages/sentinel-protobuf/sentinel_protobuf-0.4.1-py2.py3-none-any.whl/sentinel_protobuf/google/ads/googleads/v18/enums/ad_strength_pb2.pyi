from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdStrengthEnum(_message.Message):
    __slots__ = ()

    class AdStrength(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdStrengthEnum.AdStrength]
        UNKNOWN: _ClassVar[AdStrengthEnum.AdStrength]
        PENDING: _ClassVar[AdStrengthEnum.AdStrength]
        NO_ADS: _ClassVar[AdStrengthEnum.AdStrength]
        POOR: _ClassVar[AdStrengthEnum.AdStrength]
        AVERAGE: _ClassVar[AdStrengthEnum.AdStrength]
        GOOD: _ClassVar[AdStrengthEnum.AdStrength]
        EXCELLENT: _ClassVar[AdStrengthEnum.AdStrength]
    UNSPECIFIED: AdStrengthEnum.AdStrength
    UNKNOWN: AdStrengthEnum.AdStrength
    PENDING: AdStrengthEnum.AdStrength
    NO_ADS: AdStrengthEnum.AdStrength
    POOR: AdStrengthEnum.AdStrength
    AVERAGE: AdStrengthEnum.AdStrength
    GOOD: AdStrengthEnum.AdStrength
    EXCELLENT: AdStrengthEnum.AdStrength

    def __init__(self) -> None:
        ...