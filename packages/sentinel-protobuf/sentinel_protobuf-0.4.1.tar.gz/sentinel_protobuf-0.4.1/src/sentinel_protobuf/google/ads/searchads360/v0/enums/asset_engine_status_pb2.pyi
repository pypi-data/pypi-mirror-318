from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetEngineStatusEnum(_message.Message):
    __slots__ = ()

    class AssetEngineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetEngineStatusEnum.AssetEngineStatus]
        UNKNOWN: _ClassVar[AssetEngineStatusEnum.AssetEngineStatus]
        SERVING: _ClassVar[AssetEngineStatusEnum.AssetEngineStatus]
        SERVING_LIMITED: _ClassVar[AssetEngineStatusEnum.AssetEngineStatus]
        DISAPPROVED: _ClassVar[AssetEngineStatusEnum.AssetEngineStatus]
        DISABLED: _ClassVar[AssetEngineStatusEnum.AssetEngineStatus]
        REMOVED: _ClassVar[AssetEngineStatusEnum.AssetEngineStatus]
    UNSPECIFIED: AssetEngineStatusEnum.AssetEngineStatus
    UNKNOWN: AssetEngineStatusEnum.AssetEngineStatus
    SERVING: AssetEngineStatusEnum.AssetEngineStatus
    SERVING_LIMITED: AssetEngineStatusEnum.AssetEngineStatus
    DISAPPROVED: AssetEngineStatusEnum.AssetEngineStatus
    DISABLED: AssetEngineStatusEnum.AssetEngineStatus
    REMOVED: AssetEngineStatusEnum.AssetEngineStatus

    def __init__(self) -> None:
        ...