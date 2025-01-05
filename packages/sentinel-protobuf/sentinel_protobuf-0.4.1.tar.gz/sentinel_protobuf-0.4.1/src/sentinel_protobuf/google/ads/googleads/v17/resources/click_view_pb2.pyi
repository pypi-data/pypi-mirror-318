from google.ads.googleads.v17.common import click_location_pb2 as _click_location_pb2
from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickView(_message.Message):
    __slots__ = ("resource_name", "gclid", "area_of_interest", "location_of_presence", "page_number", "ad_group_ad", "campaign_location_target", "user_list", "keyword", "keyword_info")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    GCLID_FIELD_NUMBER: _ClassVar[int]
    AREA_OF_INTEREST_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OF_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_LOCATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_INFO_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    gclid: str
    area_of_interest: _click_location_pb2.ClickLocation
    location_of_presence: _click_location_pb2.ClickLocation
    page_number: int
    ad_group_ad: str
    campaign_location_target: str
    user_list: str
    keyword: str
    keyword_info: _criteria_pb2.KeywordInfo
    def __init__(self, resource_name: _Optional[str] = ..., gclid: _Optional[str] = ..., area_of_interest: _Optional[_Union[_click_location_pb2.ClickLocation, _Mapping]] = ..., location_of_presence: _Optional[_Union[_click_location_pb2.ClickLocation, _Mapping]] = ..., page_number: _Optional[int] = ..., ad_group_ad: _Optional[str] = ..., campaign_location_target: _Optional[str] = ..., user_list: _Optional[str] = ..., keyword: _Optional[str] = ..., keyword_info: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ...) -> None: ...
