from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetLinkStatusEnum(_message.Message):
    __slots__ = ()

    class AssetLinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetLinkStatusEnum.AssetLinkStatus]
        UNKNOWN: _ClassVar[AssetLinkStatusEnum.AssetLinkStatus]
        ENABLED: _ClassVar[AssetLinkStatusEnum.AssetLinkStatus]
        REMOVED: _ClassVar[AssetLinkStatusEnum.AssetLinkStatus]
        PAUSED: _ClassVar[AssetLinkStatusEnum.AssetLinkStatus]
    UNSPECIFIED: AssetLinkStatusEnum.AssetLinkStatus
    UNKNOWN: AssetLinkStatusEnum.AssetLinkStatus
    ENABLED: AssetLinkStatusEnum.AssetLinkStatus
    REMOVED: AssetLinkStatusEnum.AssetLinkStatus
    PAUSED: AssetLinkStatusEnum.AssetLinkStatus

    def __init__(self) -> None:
        ...