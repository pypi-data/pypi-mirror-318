from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ImageDataItem(_message.Message):
    __slots__ = ('gcs_uri', 'mime_type')
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    gcs_uri: str
    mime_type: str

    def __init__(self, gcs_uri: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
        ...

class VideoDataItem(_message.Message):
    __slots__ = ('gcs_uri', 'mime_type')
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    gcs_uri: str
    mime_type: str

    def __init__(self, gcs_uri: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
        ...

class TextDataItem(_message.Message):
    __slots__ = ('gcs_uri',)
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    gcs_uri: str

    def __init__(self, gcs_uri: _Optional[str]=...) -> None:
        ...