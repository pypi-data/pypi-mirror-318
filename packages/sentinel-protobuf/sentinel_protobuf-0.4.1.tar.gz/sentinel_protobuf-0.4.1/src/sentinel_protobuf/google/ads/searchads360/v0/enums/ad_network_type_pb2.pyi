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
        YOUTUBE_SEARCH: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        YOUTUBE_WATCH: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
        MIXED: _ClassVar[AdNetworkTypeEnum.AdNetworkType]
    UNSPECIFIED: AdNetworkTypeEnum.AdNetworkType
    UNKNOWN: AdNetworkTypeEnum.AdNetworkType
    SEARCH: AdNetworkTypeEnum.AdNetworkType
    SEARCH_PARTNERS: AdNetworkTypeEnum.AdNetworkType
    CONTENT: AdNetworkTypeEnum.AdNetworkType
    YOUTUBE_SEARCH: AdNetworkTypeEnum.AdNetworkType
    YOUTUBE_WATCH: AdNetworkTypeEnum.AdNetworkType
    MIXED: AdNetworkTypeEnum.AdNetworkType

    def __init__(self) -> None:
        ...