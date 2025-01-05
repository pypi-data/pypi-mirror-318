from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetAssetStatusEnum(_message.Message):
    __slots__ = ()

    class AssetSetAssetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSetAssetStatusEnum.AssetSetAssetStatus]
        UNKNOWN: _ClassVar[AssetSetAssetStatusEnum.AssetSetAssetStatus]
        ENABLED: _ClassVar[AssetSetAssetStatusEnum.AssetSetAssetStatus]
        REMOVED: _ClassVar[AssetSetAssetStatusEnum.AssetSetAssetStatus]
    UNSPECIFIED: AssetSetAssetStatusEnum.AssetSetAssetStatus
    UNKNOWN: AssetSetAssetStatusEnum.AssetSetAssetStatus
    ENABLED: AssetSetAssetStatusEnum.AssetSetAssetStatus
    REMOVED: AssetSetAssetStatusEnum.AssetSetAssetStatus

    def __init__(self) -> None:
        ...