from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdNetworkTypeEnum(_message.Message):
    __slots__ = ()

    class AdNetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        UNKNOWN: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        SEARCH: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        SEARCH_PARTNERS: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        CONTENT: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        MIXED: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        YOUTUBE: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        GOOGLE_TV: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        GOOGLE_OWNED_CHANNELS: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
    UNSPECIFIED: AdNetworkTypeEnum.AdNetworkType
    UNKNOWN: AdNetworkTypeEnum.AdNetworkType
    SEARCH: AdNetworkTypeEnum.AdNetworkType
    SEARCH_PARTNERS: AdNetworkTypeEnum.AdNetworkType
    CONTENT: AdNetworkTypeEnum.AdNetworkType
    MIXED: AdNetworkTypeEnum.AdNetworkType
    YOUTUBE: AdNetworkTypeEnum.AdNetworkType
    GOOGLE_TV: AdNetworkTypeEnum.AdNetworkType
    GOOGLE_OWNED_CHANNELS: AdNetworkTypeEnum.AdNetworkType

    def __init__(self) -> None:
        ...