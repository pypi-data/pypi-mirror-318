from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MediaTypeEnum(_message.Message):
    __slots__ = ()

    class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MediaTypeEnum.MediaType]
        UNKNOWN: _ClassVar[MediaTypeEnum.MediaType]
        IMAGE: _ClassVar[MediaTypeEnum.MediaType]
        ICON: _ClassVar[MediaTypeEnum.MediaType]
        MEDIA_BUNDLE: _ClassVar[MediaTypeEnum.MediaType]
        AUDIO: _ClassVar[MediaTypeEnum.MediaType]
        VIDEO: _ClassVar[MediaTypeEnum.MediaType]
        DYNAMIC_IMAGE: _ClassVar[MediaTypeEnum.MediaType]
    UNSPECIFIED: MediaTypeEnum.MediaType
    UNKNOWN: MediaTypeEnum.MediaType
    IMAGE: MediaTypeEnum.MediaType
    ICON: MediaTypeEnum.MediaType
    MEDIA_BUNDLE: MediaTypeEnum.MediaType
    AUDIO: MediaTypeEnum.MediaType
    VIDEO: MediaTypeEnum.MediaType
    DYNAMIC_IMAGE: MediaTypeEnum.MediaType

    def __init__(self) -> None:
        ...