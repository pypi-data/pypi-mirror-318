from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetLinkErrorEnum(_message.Message):
    __slots__ = ()

    class AssetLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        UNKNOWN: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        PINNING_UNSUPPORTED: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        UNSUPPORTED_FIELD_TYPE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        FIELD_TYPE_INCOMPATIBLE_WITH_ASSET_TYPE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        FIELD_TYPE_INCOMPATIBLE_WITH_CAMPAIGN_TYPE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        IMAGE_NOT_WITHIN_SPECIFIED_DIMENSION_RANGE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        INVALID_PINNED_FIELD: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        MEDIA_BUNDLE_ASSET_FILE_SIZE_TOO_LARGE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        NOT_ENOUGH_AVAILABLE_ASSET_LINKS_FOR_VALID_COMBINATION: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK_FOR_VALID_COMBINATION: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        YOUTUBE_VIDEO_REMOVED: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        YOUTUBE_VIDEO_TOO_LONG: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        YOUTUBE_VIDEO_TOO_SHORT: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        EXCLUDED_PARENT_FIELD_TYPE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        INVALID_STATUS: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        YOUTUBE_VIDEO_DURATION_NOT_DEFINED: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        CANNOT_CREATE_AUTOMATICALLY_CREATED_LINKS: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        CANNOT_LINK_TO_AUTOMATICALLY_CREATED_ASSET: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        CANNOT_MODIFY_ASSET_LINK_SOURCE: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        CANNOT_LINK_LOCATION_LEAD_FORM_WITHOUT_LOCATION_ASSET: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        CUSTOMER_NOT_VERIFIED: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        UNSUPPORTED_CALL_TO_ACTION: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        BRAND_ASSETS_NOT_LINKED_AT_ASSET_GROUP_LEVEL: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
        BRAND_ASSETS_NOT_LINKED_AT_CAMPAIGN_LEVEL: _ClassVar[AssetLinkErrorEnum.AssetLinkError]
    UNSPECIFIED: AssetLinkErrorEnum.AssetLinkError
    UNKNOWN: AssetLinkErrorEnum.AssetLinkError
    PINNING_UNSUPPORTED: AssetLinkErrorEnum.AssetLinkError
    UNSUPPORTED_FIELD_TYPE: AssetLinkErrorEnum.AssetLinkError
    FIELD_TYPE_INCOMPATIBLE_WITH_ASSET_TYPE: AssetLinkErrorEnum.AssetLinkError
    FIELD_TYPE_INCOMPATIBLE_WITH_CAMPAIGN_TYPE: AssetLinkErrorEnum.AssetLinkError
    INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE: AssetLinkErrorEnum.AssetLinkError
    IMAGE_NOT_WITHIN_SPECIFIED_DIMENSION_RANGE: AssetLinkErrorEnum.AssetLinkError
    INVALID_PINNED_FIELD: AssetLinkErrorEnum.AssetLinkError
    MEDIA_BUNDLE_ASSET_FILE_SIZE_TOO_LARGE: AssetLinkErrorEnum.AssetLinkError
    NOT_ENOUGH_AVAILABLE_ASSET_LINKS_FOR_VALID_COMBINATION: AssetLinkErrorEnum.AssetLinkError
    NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK: AssetLinkErrorEnum.AssetLinkError
    NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK_FOR_VALID_COMBINATION: AssetLinkErrorEnum.AssetLinkError
    YOUTUBE_VIDEO_REMOVED: AssetLinkErrorEnum.AssetLinkError
    YOUTUBE_VIDEO_TOO_LONG: AssetLinkErrorEnum.AssetLinkError
    YOUTUBE_VIDEO_TOO_SHORT: AssetLinkErrorEnum.AssetLinkError
    EXCLUDED_PARENT_FIELD_TYPE: AssetLinkErrorEnum.AssetLinkError
    INVALID_STATUS: AssetLinkErrorEnum.AssetLinkError
    YOUTUBE_VIDEO_DURATION_NOT_DEFINED: AssetLinkErrorEnum.AssetLinkError
    CANNOT_CREATE_AUTOMATICALLY_CREATED_LINKS: AssetLinkErrorEnum.AssetLinkError
    CANNOT_LINK_TO_AUTOMATICALLY_CREATED_ASSET: AssetLinkErrorEnum.AssetLinkError
    CANNOT_MODIFY_ASSET_LINK_SOURCE: AssetLinkErrorEnum.AssetLinkError
    CANNOT_LINK_LOCATION_LEAD_FORM_WITHOUT_LOCATION_ASSET: AssetLinkErrorEnum.AssetLinkError
    CUSTOMER_NOT_VERIFIED: AssetLinkErrorEnum.AssetLinkError
    UNSUPPORTED_CALL_TO_ACTION: AssetLinkErrorEnum.AssetLinkError
    BRAND_ASSETS_NOT_LINKED_AT_ASSET_GROUP_LEVEL: AssetLinkErrorEnum.AssetLinkError
    BRAND_ASSETS_NOT_LINKED_AT_CAMPAIGN_LEVEL: AssetLinkErrorEnum.AssetLinkError

    def __init__(self) -> None:
        ...