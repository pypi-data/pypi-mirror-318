from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ('video_metadata', 'name', 'display_name', 'mime_type', 'size_bytes', 'create_time', 'update_time', 'expiration_time', 'sha256_hash', 'uri', 'state', 'error')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[File.State]
        PROCESSING: _ClassVar[File.State]
        ACTIVE: _ClassVar[File.State]
        FAILED: _ClassVar[File.State]
    STATE_UNSPECIFIED: File.State
    PROCESSING: File.State
    ACTIVE: File.State
    FAILED: File.State
    VIDEO_METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    video_metadata: VideoMetadata
    name: str
    display_name: str
    mime_type: str
    size_bytes: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    sha256_hash: bytes
    uri: str
    state: File.State
    error: _status_pb2.Status

    def __init__(self, video_metadata: _Optional[_Union[VideoMetadata, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., mime_type: _Optional[str]=..., size_bytes: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., sha256_hash: _Optional[bytes]=..., uri: _Optional[str]=..., state: _Optional[_Union[File.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class VideoMetadata(_message.Message):
    __slots__ = ('video_duration',)
    VIDEO_DURATION_FIELD_NUMBER: _ClassVar[int]
    video_duration: _duration_pb2.Duration

    def __init__(self, video_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...