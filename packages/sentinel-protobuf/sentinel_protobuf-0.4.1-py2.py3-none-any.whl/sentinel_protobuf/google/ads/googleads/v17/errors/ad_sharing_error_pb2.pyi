from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdSharingErrorEnum(_message.Message):
    __slots__ = ()

    class AdSharingError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdSharingErrorEnum.AdSharingError]
        UNKNOWN: _ClassVar[AdSharingErrorEnum.AdSharingError]
        AD_GROUP_ALREADY_CONTAINS_AD: _ClassVar[AdSharingErrorEnum.AdSharingError]
        INCOMPATIBLE_AD_UNDER_AD_GROUP: _ClassVar[AdSharingErrorEnum.AdSharingError]
        CANNOT_SHARE_INACTIVE_AD: _ClassVar[AdSharingErrorEnum.AdSharingError]
    UNSPECIFIED: AdSharingErrorEnum.AdSharingError
    UNKNOWN: AdSharingErrorEnum.AdSharingError
    AD_GROUP_ALREADY_CONTAINS_AD: AdSharingErrorEnum.AdSharingError
    INCOMPATIBLE_AD_UNDER_AD_GROUP: AdSharingErrorEnum.AdSharingError
    CANNOT_SHARE_INACTIVE_AD: AdSharingErrorEnum.AdSharingError

    def __init__(self) -> None:
        ...