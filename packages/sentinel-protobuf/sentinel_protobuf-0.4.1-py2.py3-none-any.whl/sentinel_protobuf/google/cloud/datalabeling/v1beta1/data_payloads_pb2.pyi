from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImagePayload(_message.Message):
    __slots__ = ('mime_type', 'image_thumbnail', 'image_uri', 'signed_uri')
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    SIGNED_URI_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    image_thumbnail: bytes
    image_uri: str
    signed_uri: str

    def __init__(self, mime_type: _Optional[str]=..., image_thumbnail: _Optional[bytes]=..., image_uri: _Optional[str]=..., signed_uri: _Optional[str]=...) -> None:
        ...

class TextPayload(_message.Message):
    __slots__ = ('text_content',)
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    text_content: str

    def __init__(self, text_content: _Optional[str]=...) -> None:
        ...

class VideoThumbnail(_message.Message):
    __slots__ = ('thumbnail', 'time_offset')
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    thumbnail: bytes
    time_offset: _duration_pb2.Duration

    def __init__(self, thumbnail: _Optional[bytes]=..., time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class VideoPayload(_message.Message):
    __slots__ = ('mime_type', 'video_uri', 'video_thumbnails', 'frame_rate', 'signed_uri')
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URI_FIELD_NUMBER: _ClassVar[int]
    VIDEO_THUMBNAILS_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_URI_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    video_uri: str
    video_thumbnails: _containers.RepeatedCompositeFieldContainer[VideoThumbnail]
    frame_rate: float
    signed_uri: str

    def __init__(self, mime_type: _Optional[str]=..., video_uri: _Optional[str]=..., video_thumbnails: _Optional[_Iterable[_Union[VideoThumbnail, _Mapping]]]=..., frame_rate: _Optional[float]=..., signed_uri: _Optional[str]=...) -> None:
        ...