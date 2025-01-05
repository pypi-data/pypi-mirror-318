from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupAdStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupAdStatusEnum.AdGroupAdStatus]
        UNKNOWN: _ClassVar[AdGroupAdStatusEnum.AdGroupAdStatus]
        ENABLED: _ClassVar[AdGroupAdStatusEnum.AdGroupAdStatus]
        PAUSED: _ClassVar[AdGroupAdStatusEnum.AdGroupAdStatus]
        REMOVED: _ClassVar[AdGroupAdStatusEnum.AdGroupAdStatus]
    UNSPECIFIED: AdGroupAdStatusEnum.AdGroupAdStatus
    UNKNOWN: AdGroupAdStatusEnum.AdGroupAdStatus
    ENABLED: AdGroupAdStatusEnum.AdGroupAdStatus
    PAUSED: AdGroupAdStatusEnum.AdGroupAdStatus
    REMOVED: AdGroupAdStatusEnum.AdGroupAdStatus

    def __init__(self) -> None:
        ...