from google.ads.googleads.v18.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v18.enums import criterion_type_pb2 as _criterion_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerNegativeCriterion(_message.Message):
    __slots__ = ("resource_name", "id", "type", "content_label", "mobile_application", "mobile_app_category", "placement", "youtube_video", "youtube_channel", "negative_keyword_list", "ip_block")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LABEL_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_KEYWORD_LIST_FIELD_NUMBER: _ClassVar[int]
    IP_BLOCK_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    type: _criterion_type_pb2.CriterionTypeEnum.CriterionType
    content_label: _criteria_pb2.ContentLabelInfo
    mobile_application: _criteria_pb2.MobileApplicationInfo
    mobile_app_category: _criteria_pb2.MobileAppCategoryInfo
    placement: _criteria_pb2.PlacementInfo
    youtube_video: _criteria_pb2.YouTubeVideoInfo
    youtube_channel: _criteria_pb2.YouTubeChannelInfo
    negative_keyword_list: _criteria_pb2.NegativeKeywordListInfo
    ip_block: _criteria_pb2.IpBlockInfo
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., type: _Optional[_Union[_criterion_type_pb2.CriterionTypeEnum.CriterionType, str]] = ..., content_label: _Optional[_Union[_criteria_pb2.ContentLabelInfo, _Mapping]] = ..., mobile_application: _Optional[_Union[_criteria_pb2.MobileApplicationInfo, _Mapping]] = ..., mobile_app_category: _Optional[_Union[_criteria_pb2.MobileAppCategoryInfo, _Mapping]] = ..., placement: _Optional[_Union[_criteria_pb2.PlacementInfo, _Mapping]] = ..., youtube_video: _Optional[_Union[_criteria_pb2.YouTubeVideoInfo, _Mapping]] = ..., youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]] = ..., negative_keyword_list: _Optional[_Union[_criteria_pb2.NegativeKeywordListInfo, _Mapping]] = ..., ip_block: _Optional[_Union[_criteria_pb2.IpBlockInfo, _Mapping]] = ...) -> None: ...
