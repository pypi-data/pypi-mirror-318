from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VideoThumbnailEnum(_message.Message):
    __slots__ = ()

    class VideoThumbnail(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[VideoThumbnailEnum.VideoThumbnail]
        UNKNOWN: _ClassVar[VideoThumbnailEnum.VideoThumbnail]
        DEFAULT_THUMBNAIL: _ClassVar[VideoThumbnailEnum.VideoThumbnail]
        THUMBNAIL_1: _ClassVar[VideoThumbnailEnum.VideoThumbnail]
        THUMBNAIL_2: _ClassVar[VideoThumbnailEnum.VideoThumbnail]
        THUMBNAIL_3: _ClassVar[VideoThumbnailEnum.VideoThumbnail]
    UNSPECIFIED: VideoThumbnailEnum.VideoThumbnail
    UNKNOWN: VideoThumbnailEnum.VideoThumbnail
    DEFAULT_THUMBNAIL: VideoThumbnailEnum.VideoThumbnail
    THUMBNAIL_1: VideoThumbnailEnum.VideoThumbnail
    THUMBNAIL_2: VideoThumbnailEnum.VideoThumbnail
    THUMBNAIL_3: VideoThumbnailEnum.VideoThumbnail

    def __init__(self) -> None:
        ...