from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SitelinkPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class SitelinkPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        UNKNOWN: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        TEXT: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        LINE_1: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        LINE_2: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        FINAL_URLS: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        FINAL_MOBILE_URLS: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        TRACKING_URL: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
        FINAL_URL_SUFFIX: _ClassVar[SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField]
    UNSPECIFIED: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    UNKNOWN: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    TEXT: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    LINE_1: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    LINE_2: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    FINAL_URLS: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    FINAL_MOBILE_URLS: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    TRACKING_URL: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    FINAL_URL_SUFFIX: SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField

    def __init__(self) -> None:
        ...