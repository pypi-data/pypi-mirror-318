from google.ads.googleads.v17.enums import media_type_pb2 as _media_type_pb2
from google.ads.googleads.v17.enums import mime_type_pb2 as _mime_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaFile(_message.Message):
    __slots__ = ("resource_name", "id", "type", "mime_type", "source_url", "name", "file_size", "image", "media_bundle", "audio", "video")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    type: _media_type_pb2.MediaTypeEnum.MediaType
    mime_type: _mime_type_pb2.MimeTypeEnum.MimeType
    source_url: str
    name: str
    file_size: int
    image: MediaImage
    media_bundle: MediaBundle
    audio: MediaAudio
    video: MediaVideo
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., type: _Optional[_Union[_media_type_pb2.MediaTypeEnum.MediaType, str]] = ..., mime_type: _Optional[_Union[_mime_type_pb2.MimeTypeEnum.MimeType, str]] = ..., source_url: _Optional[str] = ..., name: _Optional[str] = ..., file_size: _Optional[int] = ..., image: _Optional[_Union[MediaImage, _Mapping]] = ..., media_bundle: _Optional[_Union[MediaBundle, _Mapping]] = ..., audio: _Optional[_Union[MediaAudio, _Mapping]] = ..., video: _Optional[_Union[MediaVideo, _Mapping]] = ...) -> None: ...

class MediaImage(_message.Message):
    __slots__ = ("data", "full_size_image_url", "preview_size_image_url")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FULL_SIZE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_SIZE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    full_size_image_url: str
    preview_size_image_url: str
    def __init__(self, data: _Optional[bytes] = ..., full_size_image_url: _Optional[str] = ..., preview_size_image_url: _Optional[str] = ...) -> None: ...

class MediaBundle(_message.Message):
    __slots__ = ("data", "url")
    DATA_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    url: str
    def __init__(self, data: _Optional[bytes] = ..., url: _Optional[str] = ...) -> None: ...

class MediaAudio(_message.Message):
    __slots__ = ("ad_duration_millis",)
    AD_DURATION_MILLIS_FIELD_NUMBER: _ClassVar[int]
    ad_duration_millis: int
    def __init__(self, ad_duration_millis: _Optional[int] = ...) -> None: ...

class MediaVideo(_message.Message):
    __slots__ = ("ad_duration_millis", "youtube_video_id", "advertising_id_code", "isci_code")
    AD_DURATION_MILLIS_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_ID_CODE_FIELD_NUMBER: _ClassVar[int]
    ISCI_CODE_FIELD_NUMBER: _ClassVar[int]
    ad_duration_millis: int
    youtube_video_id: str
    advertising_id_code: str
    isci_code: str
    def __init__(self, ad_duration_millis: _Optional[int] = ..., youtube_video_id: _Optional[str] = ..., advertising_id_code: _Optional[str] = ..., isci_code: _Optional[str] = ...) -> None: ...
