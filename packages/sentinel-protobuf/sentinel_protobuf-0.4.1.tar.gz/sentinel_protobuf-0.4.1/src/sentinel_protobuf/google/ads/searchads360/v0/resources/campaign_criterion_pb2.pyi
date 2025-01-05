from google.ads.searchads360.v0.common import criteria_pb2 as _criteria_pb2
from google.ads.searchads360.v0.enums import campaign_criterion_status_pb2 as _campaign_criterion_status_pb2
from google.ads.searchads360.v0.enums import criterion_type_pb2 as _criterion_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignCriterion(_message.Message):
    __slots__ = ("resource_name", "criterion_id", "display_name", "bid_modifier", "negative", "type", "status", "last_modified_time", "keyword", "location", "device", "age_range", "gender", "user_list", "language", "webpage", "location_group")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_GROUP_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    criterion_id: int
    display_name: str
    bid_modifier: float
    negative: bool
    type: _criterion_type_pb2.CriterionTypeEnum.CriterionType
    status: _campaign_criterion_status_pb2.CampaignCriterionStatusEnum.CampaignCriterionStatus
    last_modified_time: str
    keyword: _criteria_pb2.KeywordInfo
    location: _criteria_pb2.LocationInfo
    device: _criteria_pb2.DeviceInfo
    age_range: _criteria_pb2.AgeRangeInfo
    gender: _criteria_pb2.GenderInfo
    user_list: _criteria_pb2.UserListInfo
    language: _criteria_pb2.LanguageInfo
    webpage: _criteria_pb2.WebpageInfo
    location_group: _criteria_pb2.LocationGroupInfo
    def __init__(self, resource_name: _Optional[str] = ..., criterion_id: _Optional[int] = ..., display_name: _Optional[str] = ..., bid_modifier: _Optional[float] = ..., negative: bool = ..., type: _Optional[_Union[_criterion_type_pb2.CriterionTypeEnum.CriterionType, str]] = ..., status: _Optional[_Union[_campaign_criterion_status_pb2.CampaignCriterionStatusEnum.CampaignCriterionStatus, str]] = ..., last_modified_time: _Optional[str] = ..., keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]] = ..., device: _Optional[_Union[_criteria_pb2.DeviceInfo, _Mapping]] = ..., age_range: _Optional[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]] = ..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]] = ..., user_list: _Optional[_Union[_criteria_pb2.UserListInfo, _Mapping]] = ..., language: _Optional[_Union[_criteria_pb2.LanguageInfo, _Mapping]] = ..., webpage: _Optional[_Union[_criteria_pb2.WebpageInfo, _Mapping]] = ..., location_group: _Optional[_Union[_criteria_pb2.LocationGroupInfo, _Mapping]] = ...) -> None: ...
