from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SkAdNetworkCoarseConversionValueEnum(_message.Message):
    __slots__ = ()

    class SkAdNetworkCoarseConversionValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue]
        UNKNOWN: _ClassVar[SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue]
        UNAVAILABLE: _ClassVar[SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue]
        LOW: _ClassVar[SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue]
        MEDIUM: _ClassVar[SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue]
        HIGH: _ClassVar[SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue]
        NONE: _ClassVar[SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue]
    UNSPECIFIED: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    UNKNOWN: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    UNAVAILABLE: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    LOW: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    MEDIUM: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    HIGH: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    NONE: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue

    def __init__(self) -> None:
        ...