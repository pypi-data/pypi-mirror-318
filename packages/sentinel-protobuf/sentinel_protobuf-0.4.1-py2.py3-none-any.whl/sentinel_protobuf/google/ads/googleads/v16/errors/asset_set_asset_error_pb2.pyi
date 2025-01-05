from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetAssetErrorEnum(_message.Message):
    __slots__ = ()

    class AssetSetAssetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSetAssetErrorEnum.AssetSetAssetError]
        UNKNOWN: _ClassVar[AssetSetAssetErrorEnum.AssetSetAssetError]
        INVALID_ASSET_TYPE: _ClassVar[AssetSetAssetErrorEnum.AssetSetAssetError]
        INVALID_ASSET_SET_TYPE: _ClassVar[AssetSetAssetErrorEnum.AssetSetAssetError]
        DUPLICATE_EXTERNAL_KEY: _ClassVar[AssetSetAssetErrorEnum.AssetSetAssetError]
        PARENT_LINKAGE_DOES_NOT_EXIST: _ClassVar[AssetSetAssetErrorEnum.AssetSetAssetError]
    UNSPECIFIED: AssetSetAssetErrorEnum.AssetSetAssetError
    UNKNOWN: AssetSetAssetErrorEnum.AssetSetAssetError
    INVALID_ASSET_TYPE: AssetSetAssetErrorEnum.AssetSetAssetError
    INVALID_ASSET_SET_TYPE: AssetSetAssetErrorEnum.AssetSetAssetError
    DUPLICATE_EXTERNAL_KEY: AssetSetAssetErrorEnum.AssetSetAssetError
    PARENT_LINKAGE_DOES_NOT_EXIST: AssetSetAssetErrorEnum.AssetSetAssetError

    def __init__(self) -> None:
        ...