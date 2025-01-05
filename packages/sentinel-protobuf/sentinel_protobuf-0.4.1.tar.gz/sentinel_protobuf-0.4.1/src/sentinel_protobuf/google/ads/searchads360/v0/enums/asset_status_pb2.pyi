from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetStatusEnum(_message.Message):
    __slots__ = ()

    class AssetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetStatusEnum.AssetStatus]
        UNKNOWN: _ClassVar[AssetStatusEnum.AssetStatus]
        ENABLED: _ClassVar[AssetStatusEnum.AssetStatus]
        REMOVED: _ClassVar[AssetStatusEnum.AssetStatus]
        ARCHIVED: _ClassVar[AssetStatusEnum.AssetStatus]
        PENDING_SYSTEM_GENERATED: _ClassVar[AssetStatusEnum.AssetStatus]
    UNSPECIFIED: AssetStatusEnum.AssetStatus
    UNKNOWN: AssetStatusEnum.AssetStatus
    ENABLED: AssetStatusEnum.AssetStatus
    REMOVED: AssetStatusEnum.AssetStatus
    ARCHIVED: AssetStatusEnum.AssetStatus
    PENDING_SYSTEM_GENERATED: AssetStatusEnum.AssetStatus

    def __init__(self) -> None:
        ...