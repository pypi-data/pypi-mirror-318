from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SkAdNetworkSourceTypeEnum(_message.Message):
    __slots__ = ()

    class SkAdNetworkSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType]
        UNKNOWN: _ClassVar[SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType]
        UNAVAILABLE: _ClassVar[SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType]
        WEBSITE: _ClassVar[SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType]
        MOBILE_APPLICATION: _ClassVar[SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType]
    UNSPECIFIED: SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType
    UNKNOWN: SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType
    UNAVAILABLE: SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType
    WEBSITE: SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType
    MOBILE_APPLICATION: SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType

    def __init__(self) -> None:
        ...