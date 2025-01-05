from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class StaticImagePrompt(_message.Message):
    __slots__ = ('url', 'alt', 'height', 'width')

    class ImageFill(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[StaticImagePrompt.ImageFill]
        GRAY: _ClassVar[StaticImagePrompt.ImageFill]
        WHITE: _ClassVar[StaticImagePrompt.ImageFill]
        CROPPED: _ClassVar[StaticImagePrompt.ImageFill]
    UNSPECIFIED: StaticImagePrompt.ImageFill
    GRAY: StaticImagePrompt.ImageFill
    WHITE: StaticImagePrompt.ImageFill
    CROPPED: StaticImagePrompt.ImageFill
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