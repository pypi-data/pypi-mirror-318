from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ThemeCustomization(_message.Message):
    __slots__ = ('background_color', 'primary_color', 'font_family', 'image_corner_style', 'landscape_background_image', 'portrait_background_image')

    class ImageCornerStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE_CORNER_STYLE_UNSPECIFIED: _ClassVar[ThemeCustomization.ImageCornerStyle]
        CURVED: _ClassVar[ThemeCustomization.ImageCornerStyle]
        ANGLED: _ClassVar[ThemeCustomization.ImageCornerStyle]
    IMAGE_CORNER_STYLE_UNSPECIFIED: ThemeCustomization.ImageCornerStyle
    CURVED: ThemeCustomization.ImageCornerStyle
    ANGLED: ThemeCustomization.ImageCornerStyle
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    FONT_FAMILY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CORNER_STYLE_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_BACKGROUND_IMAGE_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_BACKGROUND_IMAGE_FIELD_NUMBER: _ClassVar[int]
    background_color: str
    primary_color: str
    font_family: str
    image_corner_style: ThemeCustomization.ImageCornerStyle
    landscape_background_image: str
    portrait_background_image: str

    def __init__(self, background_color: _Optional[str]=..., primary_color: _Optional[str]=..., font_family: _Optional[str]=..., image_corner_style: _Optional[_Union[ThemeCustomization.ImageCornerStyle, str]]=..., landscape_background_image: _Optional[str]=..., portrait_background_image: _Optional[str]=...) -> None:
        ...