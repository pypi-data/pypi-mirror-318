from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetLinkErrorEnum(_message.Message):
    __slots__ = ()

    class AssetSetLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSetLinkErrorEnum.AssetSetLinkError]
        UNKNOWN: _ClassVar[AssetSetLinkErrorEnum.AssetSetLinkError]
        INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE: _ClassVar[AssetSetLinkErrorEnum.AssetSetLinkError]
        DUPLICATE_FEED_LINK: _ClassVar[AssetSetLinkErrorEnum.AssetSetLinkError]
        INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE: _ClassVar[AssetSetLinkErrorEnum.AssetSetLinkError]
        DUPLICATE_ASSET_SET_LINK: _ClassVar[AssetSetLinkErrorEnum.AssetSetLinkError]
        ASSET_SET_LINK_CANNOT_BE_REMOVED: _ClassVar[AssetSetLinkErrorEnum.AssetSetLinkError]
    UNSPECIFIED: AssetSetLinkErrorEnum.AssetSetLinkError
    UNKNOWN: AssetSetLinkErrorEnum.AssetSetLinkError
    INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE: AssetSetLinkErrorEnum.AssetSetLinkError
    DUPLICATE_FEED_LINK: AssetSetLinkErrorEnum.AssetSetLinkError
    INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE: AssetSetLinkErrorEnum.AssetSetLinkError
    DUPLICATE_ASSET_SET_LINK: AssetSetLinkErrorEnum.AssetSetLinkError
    ASSET_SET_LINK_CANNOT_BE_REMOVED: AssetSetLinkErrorEnum.AssetSetLinkError

    def __init__(self) -> None:
        ...