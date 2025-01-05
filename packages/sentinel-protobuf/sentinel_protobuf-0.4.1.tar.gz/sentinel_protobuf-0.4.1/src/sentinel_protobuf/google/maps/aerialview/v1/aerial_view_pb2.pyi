from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Video(_message.Message):
    __slots__ = ('uris', 'state', 'metadata')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Video.State]
        PROCESSING: _ClassVar[Video.State]
        ACTIVE: _ClassVar[Video.State]
        FAILED: _ClassVar[Video.State]
    STATE_UNSPECIFIED: Video.State
    PROCESSING: Video.State
    ACTIVE: Video.State
    FAILED: Video.State

    class UrisEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Uris

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Uris, _Mapping]]=...) -> None:
            ...
    URIS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.MessageMap[str, Uris]
    state: Video.State
    metadata: VideoMetadata

    def __init__(self, uris: _Optional[_Mapping[str, Uris]]=..., state: _Optional[_Union[Video.State, str]]=..., metadata: _Optional[_Union[VideoMetadata, _Mapping]]=...) -> None:
        ...

class Uris(_message.Message):
    __slots__ = ('landscape_uri', 'portrait_uri')
    LANDSCAPE_URI_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_URI_FIELD_NUMBER: _ClassVar[int]
    landscape_uri: str
    portrait_uri: str

    def __init__(self, landscape_uri: _Optional[str]=..., portrait_uri: _Optional[str]=...) -> None:
        ...

class VideoMetadata(_message.Message):
    __slots__ = ('video_id', 'capture_date', 'duration')
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_DATE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    capture_date: _date_pb2.Date
    duration: _duration_pb2.Duration

    def __init__(self, video_id: _Optional[str]=..., capture_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class RenderVideoRequest(_message.Message):
    __slots__ = ('address',)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str

    def __init__(self, address: _Optional[str]=...) -> None:
        ...

class RenderVideoResponse(_message.Message):
    __slots__ = ('state', 'metadata')
    STATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    state: Video.State
    metadata: VideoMetadata

    def __init__(self, state: _Optional[_Union[Video.State, str]]=..., metadata: _Optional[_Union[VideoMetadata, _Mapping]]=...) -> None:
        ...

class LookupVideoRequest(_message.Message):
    __slots__ = ('video_id', 'address')
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    address: str

    def __init__(self, video_id: _Optional[str]=..., address: _Optional[str]=...) -> None:
        ...