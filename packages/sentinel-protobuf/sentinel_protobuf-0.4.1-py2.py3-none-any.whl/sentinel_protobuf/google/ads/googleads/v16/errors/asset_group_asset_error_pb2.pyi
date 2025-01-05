from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupAssetErrorEnum(_message.Message):
    __slots__ = ()

    class AssetGroupAssetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupAssetErrorEnum.AssetGroupAssetError]
        UNKNOWN: _ClassVar[AssetGroupAssetErrorEnum.AssetGroupAssetError]
        DUPLICATE_RESOURCE: _ClassVar[AssetGroupAssetErrorEnum.AssetGroupAssetError]
        EXPANDABLE_TAGS_NOT_ALLOWED_IN_DESCRIPTION: _ClassVar[AssetGroupAssetErrorEnum.AssetGroupAssetError]
        AD_CUSTOMIZER_NOT_SUPPORTED: _ClassVar[AssetGroupAssetErrorEnum.AssetGroupAssetError]
        HOTEL_PROPERTY_ASSET_NOT_LINKED_TO_CAMPAIGN: _ClassVar[AssetGroupAssetErrorEnum.AssetGroupAssetError]
    UNSPECIFIED: AssetGroupAssetErrorEnum.AssetGroupAssetError
    UNKNOWN: AssetGroupAssetErrorEnum.AssetGroupAssetError
    DUPLICATE_RESOURCE: AssetGroupAssetErrorEnum.AssetGroupAssetError
    EXPANDABLE_TAGS_NOT_ALLOWED_IN_DESCRIPTION: AssetGroupAssetErrorEnum.AssetGroupAssetError
    AD_CUSTOMIZER_NOT_SUPPORTED: AssetGroupAssetErrorEnum.AssetGroupAssetError
    HOTEL_PROPERTY_ASSET_NOT_LINKED_TO_CAMPAIGN: AssetGroupAssetErrorEnum.AssetGroupAssetError

    def __init__(self) -> None:
        ...