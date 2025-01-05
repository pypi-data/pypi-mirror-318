from google.ads.searchads360.v0.common import criteria_pb2 as _criteria_pb2
from google.ads.searchads360.v0.enums import ad_group_criterion_engine_status_pb2 as _ad_group_criterion_engine_status_pb2
from google.ads.searchads360.v0.enums import ad_group_criterion_status_pb2 as _ad_group_criterion_status_pb2
from google.ads.searchads360.v0.enums import criterion_type_pb2 as _criterion_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterion(_message.Message):
    __slots__ = ("resource_name", "criterion_id", "creation_time", "status", "quality_info", "ad_group", "type", "negative", "labels", "effective_labels", "bid_modifier", "cpc_bid_micros", "effective_cpc_bid_micros", "position_estimates", "final_urls", "engine_status", "final_url_suffix", "tracking_url_template", "engine_id", "last_modified_time", "keyword", "listing_group", "age_range", "gender", "user_list", "webpage", "location")
    class QualityInfo(_message.Message):
        __slots__ = ("quality_score",)
        QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
        quality_score: int
        def __init__(self, quality_score: _Optional[int] = ...) -> None: ...
    class PositionEstimates(_message.Message):
        __slots__ = ("top_of_page_cpc_micros",)
        TOP_OF_PAGE_CPC_MICROS_FIELD_NUMBER: _ClassVar[int]
        top_of_page_cpc_micros: int
        def __init__(self, top_of_page_cpc_micros: _Optional[int] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_INFO_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_LABELS_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    POSITION_ESTIMATES_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    ENGINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    LISTING_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    criterion_id: int
    creation_time: str
    status: _ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    quality_info: AdGroupCriterion.QualityInfo
    ad_group: str
    type: _criterion_type_pb2.CriterionTypeEnum.CriterionType
    negative: bool
    labels: _containers.RepeatedScalarFieldContainer[str]
    effective_labels: _containers.RepeatedScalarFieldContainer[str]
    bid_modifier: float
    cpc_bid_micros: int
    effective_cpc_bid_micros: int
    position_estimates: AdGroupCriterion.PositionEstimates
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    engine_status: _ad_group_criterion_engine_status_pb2.AdGroupCriterionEngineStatusEnum.AdGroupCriterionEngineStatus
    final_url_suffix: str
    tracking_url_template: str
    engine_id: str
    last_modified_time: str
    keyword: _criteria_pb2.KeywordInfo
    listing_group: _criteria_pb2.ListingGroupInfo
    age_range: _criteria_pb2.AgeRangeInfo
    gender: _criteria_pb2.GenderInfo
    user_list: _criteria_pb2.UserListInfo
    webpage: _criteria_pb2.WebpageInfo
    location: _criteria_pb2.LocationInfo
    def __init__(self, resource_name: _Optional[str] = ..., criterion_id: _Optional[int] = ..., creation_time: _Optional[str] = ..., status: _Optional[_Union[_ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus, str]] = ..., quality_info: _Optional[_Union[AdGroupCriterion.QualityInfo, _Mapping]] = ..., ad_group: _Optional[str] = ..., type: _Optional[_Union[_criterion_type_pb2.CriterionTypeEnum.CriterionType, str]] = ..., negative: bool = ..., labels: _Optional[_Iterable[str]] = ..., effective_labels: _Optional[_Iterable[str]] = ..., bid_modifier: _Optional[float] = ..., cpc_bid_micros: _Optional[int] = ..., effective_cpc_bid_micros: _Optional[int] = ..., position_estimates: _Optional[_Union[AdGroupCriterion.PositionEstimates, _Mapping]] = ..., final_urls: _Optional[_Iterable[str]] = ..., engine_status: _Optional[_Union[_ad_group_criterion_engine_status_pb2.AdGroupCriterionEngineStatusEnum.AdGroupCriterionEngineStatus, str]] = ..., final_url_suffix: _Optional[str] = ..., tracking_url_template: _Optional[str] = ..., engine_id: _Optional[str] = ..., last_modified_time: _Optional[str] = ..., keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., listing_group: _Optional[_Union[_criteria_pb2.ListingGroupInfo, _Mapping]] = ..., age_range: _Optional[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]] = ..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]] = ..., user_list: _Optional[_Union[_criteria_pb2.UserListInfo, _Mapping]] = ..., webpage: _Optional[_Union[_criteria_pb2.WebpageInfo, _Mapping]] = ..., location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]] = ...) -> None: ...
