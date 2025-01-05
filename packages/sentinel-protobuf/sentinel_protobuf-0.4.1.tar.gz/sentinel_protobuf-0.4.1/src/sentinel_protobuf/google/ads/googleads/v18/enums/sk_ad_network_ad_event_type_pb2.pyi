from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SkAdNetworkAdEventTypeEnum(_message.Message):
    __slots__ = ()

    class SkAdNetworkAdEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType]
        UNKNOWN: _ClassVar[SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType]
        UNAVAILABLE: _ClassVar[SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType]
        INTERACTION: _ClassVar[SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType]
        VIEW: _ClassVar[SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType]
    UNSPECIFIED: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    UNKNOWN: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    UNAVAILABLE: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    INTERACTION: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    VIEW: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType

    def __init__(self) -> None:
        ...