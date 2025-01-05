from google.ads.googleads.v17.enums import keyword_match_type_pb2 as _keyword_match_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanAdGroupKeyword(_message.Message):
    __slots__ = ("resource_name", "keyword_plan_ad_group", "id", "text", "match_type", "cpc_bid_micros", "negative")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_PLAN_AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    keyword_plan_ad_group: str
    id: int
    text: str
    match_type: _keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType
    cpc_bid_micros: int
    negative: bool
    def __init__(self, resource_name: _Optional[str] = ..., keyword_plan_ad_group: _Optional[str] = ..., id: _Optional[int] = ..., text: _Optional[str] = ..., match_type: _Optional[_Union[_keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType, str]] = ..., cpc_bid_micros: _Optional[int] = ..., negative: bool = ...) -> None: ...
