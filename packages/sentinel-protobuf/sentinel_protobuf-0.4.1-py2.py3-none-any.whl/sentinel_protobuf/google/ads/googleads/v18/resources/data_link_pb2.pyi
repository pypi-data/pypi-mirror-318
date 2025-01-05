from google.ads.googleads.v18.enums import data_link_status_pb2 as _data_link_status_pb2
from google.ads.googleads.v18.enums import data_link_type_pb2 as _data_link_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataLink(_message.Message):
    __slots__ = ("resource_name", "product_link_id", "data_link_id", "type", "status", "youtube_video")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    product_link_id: int
    data_link_id: int
    type: _data_link_type_pb2.DataLinkTypeEnum.DataLinkType
    status: _data_link_status_pb2.DataLinkStatusEnum.DataLinkStatus
    youtube_video: YoutubeVideoIdentifier
    def __init__(self, resource_name: _Optional[str] = ..., product_link_id: _Optional[int] = ..., data_link_id: _Optional[int] = ..., type: _Optional[_Union[_data_link_type_pb2.DataLinkTypeEnum.DataLinkType, str]] = ..., status: _Optional[_Union[_data_link_status_pb2.DataLinkStatusEnum.DataLinkStatus, str]] = ..., youtube_video: _Optional[_Union[YoutubeVideoIdentifier, _Mapping]] = ...) -> None: ...

class YoutubeVideoIdentifier(_message.Message):
    __slots__ = ("channel_id", "video_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    video_id: str
    def __init__(self, channel_id: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...
