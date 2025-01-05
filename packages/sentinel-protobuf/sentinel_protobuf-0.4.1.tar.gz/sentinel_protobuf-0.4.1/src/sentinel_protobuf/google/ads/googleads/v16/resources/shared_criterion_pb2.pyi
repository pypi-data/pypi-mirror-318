from google.ads.googleads.v16.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v16.enums import criterion_type_pb2 as _criterion_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SharedCriterion(_message.Message):
    __slots__ = ("resource_name", "shared_set", "criterion_id", "type", "keyword", "youtube_video", "youtube_channel", "placement", "mobile_app_category", "mobile_application", "brand")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_SET_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    shared_set: str
    criterion_id: int
    type: _criterion_type_pb2.CriterionTypeEnum.CriterionType
    keyword: _criteria_pb2.KeywordInfo
    youtube_video: _criteria_pb2.YouTubeVideoInfo
    youtube_channel: _criteria_pb2.YouTubeChannelInfo
    placement: _criteria_pb2.PlacementInfo
    mobile_app_category: _criteria_pb2.MobileAppCategoryInfo
    mobile_application: _criteria_pb2.MobileApplicationInfo
    brand: _criteria_pb2.BrandInfo
    def __init__(self, resource_name: _Optional[str] = ..., shared_set: _Optional[str] = ..., criterion_id: _Optional[int] = ..., type: _Optional[_Union[_criterion_type_pb2.CriterionTypeEnum.CriterionType, str]] = ..., keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., youtube_video: _Optional[_Union[_criteria_pb2.YouTubeVideoInfo, _Mapping]] = ..., youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]] = ..., placement: _Optional[_Union[_criteria_pb2.PlacementInfo, _Mapping]] = ..., mobile_app_category: _Optional[_Union[_criteria_pb2.MobileAppCategoryInfo, _Mapping]] = ..., mobile_application: _Optional[_Union[_criteria_pb2.MobileApplicationInfo, _Mapping]] = ..., brand: _Optional[_Union[_criteria_pb2.BrandInfo, _Mapping]] = ...) -> None: ...
