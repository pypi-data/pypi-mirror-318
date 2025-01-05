from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupStatusEnum(_message.Message):
    __slots__ = ()

    class AssetGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupStatusEnum.AssetGroupStatus]
        UNKNOWN: _ClassVar[AssetGroupStatusEnum.AssetGroupStatus]
        ENABLED: _ClassVar[AssetGroupStatusEnum.AssetGroupStatus]
        PAUSED: _ClassVar[AssetGroupStatusEnum.AssetGroupStatus]
        REMOVED: _ClassVar[AssetGroupStatusEnum.AssetGroupStatus]
    UNSPECIFIED: AssetGroupStatusEnum.AssetGroupStatus
    UNKNOWN: AssetGroupStatusEnum.AssetGroupStatus
    ENABLED: AssetGroupStatusEnum.AssetGroupStatus
    PAUSED: AssetGroupStatusEnum.AssetGroupStatus
    REMOVED: AssetGroupStatusEnum.AssetGroupStatus

    def __init__(self) -> None:
        ...