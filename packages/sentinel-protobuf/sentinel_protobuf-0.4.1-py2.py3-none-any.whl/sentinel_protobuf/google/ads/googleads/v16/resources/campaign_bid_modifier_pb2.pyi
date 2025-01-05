from google.ads.googleads.v16.common import criteria_pb2 as _criteria_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignBidModifier(_message.Message):
    __slots__ = ("resource_name", "campaign", "criterion_id", "bid_modifier", "interaction_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    criterion_id: int
    bid_modifier: float
    interaction_type: _criteria_pb2.InteractionTypeInfo
    def __init__(self, resource_name: _Optional[str] = ..., campaign: _Optional[str] = ..., criterion_id: _Optional[int] = ..., bid_modifier: _Optional[float] = ..., interaction_type: _Optional[_Union[_criteria_pb2.InteractionTypeInfo, _Mapping]] = ...) -> None: ...
