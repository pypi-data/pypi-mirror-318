from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanAdGroup(_message.Message):
    __slots__ = ("resource_name", "keyword_plan_campaign", "id", "name", "cpc_bid_micros")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_PLAN_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    keyword_plan_campaign: str
    id: int
    name: str
    cpc_bid_micros: int
    def __init__(self, resource_name: _Optional[str] = ..., keyword_plan_campaign: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., cpc_bid_micros: _Optional[int] = ...) -> None: ...
