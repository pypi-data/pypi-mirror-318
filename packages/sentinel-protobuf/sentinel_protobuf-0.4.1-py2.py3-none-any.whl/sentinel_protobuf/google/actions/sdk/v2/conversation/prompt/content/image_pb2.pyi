from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ('url', 'alt', 'height', 'width')

    class ImageFill(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[Image.ImageFill]
        GRAY: _ClassVar[Image.ImageFill]
        WHITE: _ClassVar[Image.ImageFill]
        CROPPED: _ClassVar[Image.ImageFill]
    UNSPECIFIED: Image.ImageFill
    GRAY: Image.ImageFill
    WHITE: Image.ImageFill
    CROPPED: Image.ImageFill
    URL_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    url: str
    alt: str
    height: int
    width: int

    def __init__(self, url: _Optional[str]=..., alt: _Optional[str]=..., height: _Optional[int]=..., width: _Optional[int]=...) -> None:
        ...