from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ImagePlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class ImagePlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ImagePlaceholderFieldEnum.ImagePlaceholderField]
        UNKNOWN: _ClassVar[ImagePlaceholderFieldEnum.ImagePlaceholderField]
        ASSET_ID: _ClassVar[ImagePlaceholderFieldEnum.ImagePlaceholderField]
    UNSPECIFIED: ImagePlaceholderFieldEnum.ImagePlaceholderField
    UNKNOWN: ImagePlaceholderFieldEnum.ImagePlaceholderField
    ASSET_ID: ImagePlaceholderFieldEnum.ImagePlaceholderField

    def __init__(self) -> None:
        ...