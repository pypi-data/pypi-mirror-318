from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AndroidPrivacyNetworkTypeEnum(_message.Message):
    __slots__ = ()

    class AndroidPrivacyNetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType]
        UNKNOWN: _ClassVar[AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType]
        SEARCH: _ClassVar[AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType]
        DISPLAY: _ClassVar[AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType]
        YOUTUBE: _ClassVar[AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType]
    UNSPECIFIED: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    UNKNOWN: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    SEARCH: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    DISPLAY: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    YOUTUBE: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType

    def __init__(self) -> None:
        ...