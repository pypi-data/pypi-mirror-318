from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetErrorEnum(_message.Message):
    __slots__ = ()

    class AssetSetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSetErrorEnum.AssetSetError]
        UNKNOWN: _ClassVar[AssetSetErrorEnum.AssetSetError]
        DUPLICATE_ASSET_SET_NAME: _ClassVar[AssetSetErrorEnum.AssetSetError]
        INVALID_PARENT_ASSET_SET_TYPE: _ClassVar[AssetSetErrorEnum.AssetSetError]
        ASSET_SET_SOURCE_INCOMPATIBLE_WITH_PARENT_ASSET_SET: _ClassVar[AssetSetErrorEnum.AssetSetError]
        ASSET_SET_TYPE_CANNOT_BE_LINKED_TO_CUSTOMER: _ClassVar[AssetSetErrorEnum.AssetSetError]
        INVALID_CHAIN_IDS: _ClassVar[AssetSetErrorEnum.AssetSetError]
        LOCATION_SYNC_ASSET_SET_DOES_NOT_SUPPORT_RELATIONSHIP_TYPE: _ClassVar[AssetSetErrorEnum.AssetSetError]
        NOT_UNIQUE_ENABLED_LOCATION_SYNC_TYPED_ASSET_SET: _ClassVar[AssetSetErrorEnum.AssetSetError]
        INVALID_PLACE_IDS: _ClassVar[AssetSetErrorEnum.AssetSetError]
        OAUTH_INFO_INVALID: _ClassVar[AssetSetErrorEnum.AssetSetError]
        OAUTH_INFO_MISSING: _ClassVar[AssetSetErrorEnum.AssetSetError]
        CANNOT_DELETE_AS_ENABLED_LINKAGES_EXIST: _ClassVar[AssetSetErrorEnum.AssetSetError]
    UNSPECIFIED: AssetSetErrorEnum.AssetSetError
    UNKNOWN: AssetSetErrorEnum.AssetSetError
    DUPLICATE_ASSET_SET_NAME: AssetSetErrorEnum.AssetSetError
    INVALID_PARENT_ASSET_SET_TYPE: AssetSetErrorEnum.AssetSetError
    ASSET_SET_SOURCE_INCOMPATIBLE_WITH_PARENT_ASSET_SET: AssetSetErrorEnum.AssetSetError
    ASSET_SET_TYPE_CANNOT_BE_LINKED_TO_CUSTOMER: AssetSetErrorEnum.AssetSetError
    INVALID_CHAIN_IDS: AssetSetErrorEnum.AssetSetError
    LOCATION_SYNC_ASSET_SET_DOES_NOT_SUPPORT_RELATIONSHIP_TYPE: AssetSetErrorEnum.AssetSetError
    NOT_UNIQUE_ENABLED_LOCATION_SYNC_TYPED_ASSET_SET: AssetSetErrorEnum.AssetSetError
    INVALID_PLACE_IDS: AssetSetErrorEnum.AssetSetError
    OAUTH_INFO_INVALID: AssetSetErrorEnum.AssetSetError
    OAUTH_INFO_MISSING: AssetSetErrorEnum.AssetSetError
    CANNOT_DELETE_AS_ENABLED_LINKAGES_EXIST: AssetSetErrorEnum.AssetSetError

    def __init__(self) -> None:
        ...