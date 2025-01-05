from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class LocalPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        UNKNOWN: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        DEAL_ID: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        DEAL_NAME: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        SUBTITLE: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        DESCRIPTION: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        PRICE: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        FORMATTED_PRICE: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        SALE_PRICE: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        FORMATTED_SALE_PRICE: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        IMAGE_URL: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        ADDRESS: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        CATEGORY: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        CONTEXTUAL_KEYWORDS: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        FINAL_URLS: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        FINAL_MOBILE_URLS: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        TRACKING_URL: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        ANDROID_APP_LINK: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        SIMILAR_DEAL_IDS: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        IOS_APP_LINK: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
        IOS_APP_STORE_ID: _ClassVar[LocalPlaceholderFieldEnum.LocalPlaceholderField]
    UNSPECIFIED: LocalPlaceholderFieldEnum.LocalPlaceholderField
    UNKNOWN: LocalPlaceholderFieldEnum.LocalPlaceholderField
    DEAL_ID: LocalPlaceholderFieldEnum.LocalPlaceholderField
    DEAL_NAME: LocalPlaceholderFieldEnum.LocalPlaceholderField
    SUBTITLE: LocalPlaceholderFieldEnum.LocalPlaceholderField
    DESCRIPTION: LocalPlaceholderFieldEnum.LocalPlaceholderField
    PRICE: LocalPlaceholderFieldEnum.LocalPlaceholderField
    FORMATTED_PRICE: LocalPlaceholderFieldEnum.LocalPlaceholderField
    SALE_PRICE: LocalPlaceholderFieldEnum.LocalPlaceholderField
    FORMATTED_SALE_PRICE: LocalPlaceholderFieldEnum.LocalPlaceholderField
    IMAGE_URL: LocalPlaceholderFieldEnum.LocalPlaceholderField
    ADDRESS: LocalPlaceholderFieldEnum.LocalPlaceholderField
    CATEGORY: LocalPlaceholderFieldEnum.LocalPlaceholderField
    CONTEXTUAL_KEYWORDS: LocalPlaceholderFieldEnum.LocalPlaceholderField
    FINAL_URLS: LocalPlaceholderFieldEnum.LocalPlaceholderField
    FINAL_MOBILE_URLS: LocalPlaceholderFieldEnum.LocalPlaceholderField
    TRACKING_URL: LocalPlaceholderFieldEnum.LocalPlaceholderField
    ANDROID_APP_LINK: LocalPlaceholderFieldEnum.LocalPlaceholderField
    SIMILAR_DEAL_IDS: LocalPlaceholderFieldEnum.LocalPlaceholderField
    IOS_APP_LINK: LocalPlaceholderFieldEnum.LocalPlaceholderField
    IOS_APP_STORE_ID: LocalPlaceholderFieldEnum.LocalPlaceholderField

    def __init__(self) -> None:
        ...