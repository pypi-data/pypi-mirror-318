from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetStatusEnum(_message.Message):
    __slots__ = ()

    class AssetSetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSetStatusEnum.AssetSetStatus]
        UNKNOWN: _ClassVar[AssetSetStatusEnum.AssetSetStatus]
        ENABLED: _ClassVar[AssetSetStatusEnum.AssetSetStatus]
        REMOVED: _ClassVar[AssetSetStatusEnum.AssetSetStatus]
    UNSPECIFIED: AssetSetStatusEnum.AssetSetStatus
    UNKNOWN: AssetSetStatusEnum.AssetSetStatus
    ENABLED: AssetSetStatusEnum.AssetSetStatus
    REMOVED: AssetSetStatusEnum.AssetSetStatus

    def __init__(self) -> None:
        ...