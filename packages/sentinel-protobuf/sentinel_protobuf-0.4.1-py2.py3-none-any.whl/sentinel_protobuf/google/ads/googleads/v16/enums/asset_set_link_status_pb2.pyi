from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetLinkStatusEnum(_message.Message):
    __slots__ = ()

    class AssetSetLinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSetLinkStatusEnum.AssetSetLinkStatus]
        UNKNOWN: _ClassVar[AssetSetLinkStatusEnum.AssetSetLinkStatus]
        ENABLED: _ClassVar[AssetSetLinkStatusEnum.AssetSetLinkStatus]
        REMOVED: _ClassVar[AssetSetLinkStatusEnum.AssetSetLinkStatus]
    UNSPECIFIED: AssetSetLinkStatusEnum.AssetSetLinkStatus
    UNKNOWN: AssetSetLinkStatusEnum.AssetSetLinkStatus
    ENABLED: AssetSetLinkStatusEnum.AssetSetLinkStatus
    REMOVED: AssetSetLinkStatusEnum.AssetSetLinkStatus

    def __init__(self) -> None:
        ...