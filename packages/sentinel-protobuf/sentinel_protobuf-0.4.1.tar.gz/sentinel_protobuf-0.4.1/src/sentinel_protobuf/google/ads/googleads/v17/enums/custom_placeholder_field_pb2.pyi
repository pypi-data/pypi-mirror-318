from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class CustomPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        UNKNOWN: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ID: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ID2: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ITEM_TITLE: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ITEM_SUBTITLE: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ITEM_DESCRIPTION: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ITEM_ADDRESS: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        PRICE: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        FORMATTED_PRICE: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        SALE_PRICE: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        FORMATTED_SALE_PRICE: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        IMAGE_URL: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ITEM_CATEGORY: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        FINAL_URLS: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        FINAL_MOBILE_URLS: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        TRACKING_URL: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        CONTEXTUAL_KEYWORDS: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        ANDROID_APP_LINK: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        SIMILAR_IDS: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        IOS_APP_LINK: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
        IOS_APP_STORE_ID: _ClassVar[CustomPlaceholderFieldEnum.CustomPlaceholderField]
    UNSPECIFIED: CustomPlaceholderFieldEnum.CustomPlaceholderField
    UNKNOWN: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ID: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ID2: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ITEM_TITLE: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ITEM_SUBTITLE: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ITEM_DESCRIPTION: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ITEM_ADDRESS: CustomPlaceholderFieldEnum.CustomPlaceholderField
    PRICE: CustomPlaceholderFieldEnum.CustomPlaceholderField
    FORMATTED_PRICE: CustomPlaceholderFieldEnum.CustomPlaceholderField
    SALE_PRICE: CustomPlaceholderFieldEnum.CustomPlaceholderField
    FORMATTED_SALE_PRICE: CustomPlaceholderFieldEnum.CustomPlaceholderField
    IMAGE_URL: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ITEM_CATEGORY: CustomPlaceholderFieldEnum.CustomPlaceholderField
    FINAL_URLS: CustomPlaceholderFieldEnum.CustomPlaceholderField
    FINAL_MOBILE_URLS: CustomPlaceholderFieldEnum.CustomPlaceholderField
    TRACKING_URL: CustomPlaceholderFieldEnum.CustomPlaceholderField
    CONTEXTUAL_KEYWORDS: CustomPlaceholderFieldEnum.CustomPlaceholderField
    ANDROID_APP_LINK: CustomPlaceholderFieldEnum.CustomPlaceholderField
    SIMILAR_IDS: CustomPlaceholderFieldEnum.CustomPlaceholderField
    IOS_APP_LINK: CustomPlaceholderFieldEnum.CustomPlaceholderField
    IOS_APP_STORE_ID: CustomPlaceholderFieldEnum.CustomPlaceholderField

    def __init__(self) -> None:
        ...