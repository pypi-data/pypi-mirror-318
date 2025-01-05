from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AppPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class AppPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        UNKNOWN: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        STORE: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        ID: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        LINK_TEXT: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        URL: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        FINAL_URLS: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        FINAL_MOBILE_URLS: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        TRACKING_URL: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
        FINAL_URL_SUFFIX: _ClassVar[AppPlaceholderFieldEnum.AppPlaceholderField]
    UNSPECIFIED: AppPlaceholderFieldEnum.AppPlaceholderField
    UNKNOWN: AppPlaceholderFieldEnum.AppPlaceholderField
    STORE: AppPlaceholderFieldEnum.AppPlaceholderField
    ID: AppPlaceholderFieldEnum.AppPlaceholderField
    LINK_TEXT: AppPlaceholderFieldEnum.AppPlaceholderField
    URL: AppPlaceholderFieldEnum.AppPlaceholderField
    FINAL_URLS: AppPlaceholderFieldEnum.AppPlaceholderField
    FINAL_MOBILE_URLS: AppPlaceholderFieldEnum.AppPlaceholderField
    TRACKING_URL: AppPlaceholderFieldEnum.AppPlaceholderField
    FINAL_URL_SUFFIX: AppPlaceholderFieldEnum.AppPlaceholderField

    def __init__(self) -> None:
        ...