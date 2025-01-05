from google.ads.googleads.v16.common import bidding_pb2 as _bidding_pb2
from google.ads.googleads.v16.enums import bidding_strategy_status_pb2 as _bidding_strategy_status_pb2
from google.ads.googleads.v16.enums import bidding_strategy_type_pb2 as _bidding_strategy_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BiddingStrategy(_message.Message):
    __slots__ = ("resource_name", "id", "name", "status", "type", "currency_code", "effective_currency_code", "aligned_campaign_budget_id", "campaign_count", "non_removed_campaign_count", "enhanced_cpc", "maximize_conversion_value", "maximize_conversions", "target_cpa", "target_impression_share", "target_roas", "target_spend")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_CAMPAIGN_BUDGET_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_COUNT_FIELD_NUMBER: _ClassVar[int]
    NON_REMOVED_CAMPAIGN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENHANCED_CPC_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAXIMIZE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_FIELD_NUMBER: _ClassVar[int]
    TARGET_IMPRESSION_SHARE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SPEND_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    status: _bidding_strategy_status_pb2.BiddingStrategyStatusEnum.BiddingStrategyStatus
    type: _bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType
    currency_code: str
    effective_currency_code: str
    aligned_campaign_budget_id: int
    campaign_count: int
    non_removed_campaign_count: int
    enhanced_cpc: _bidding_pb2.EnhancedCpc
    maximize_conversion_value: _bidding_pb2.MaximizeConversionValue
    maximize_conversions: _bidding_pb2.MaximizeConversions
    target_cpa: _bidding_pb2.TargetCpa
    target_impression_share: _bidding_pb2.TargetImpressionShare
    target_roas: _bidding_pb2.TargetRoas
    target_spend: _bidding_pb2.TargetSpend
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_bidding_strategy_status_pb2.BiddingStrategyStatusEnum.BiddingStrategyStatus, str]] = ..., type: _Optional[_Union[_bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType, str]] = ..., currency_code: _Optional[str] = ..., effective_currency_code: _Optional[str] = ..., aligned_campaign_budget_id: _Optional[int] = ..., campaign_count: _Optional[int] = ..., non_removed_campaign_count: _Optional[int] = ..., enhanced_cpc: _Optional[_Union[_bidding_pb2.EnhancedCpc, _Mapping]] = ..., maximize_conversion_value: _Optional[_Union[_bidding_pb2.MaximizeConversionValue, _Mapping]] = ..., maximize_conversions: _Optional[_Union[_bidding_pb2.MaximizeConversions, _Mapping]] = ..., target_cpa: _Optional[_Union[_bidding_pb2.TargetCpa, _Mapping]] = ..., target_impression_share: _Optional[_Union[_bidding_pb2.TargetImpressionShare, _Mapping]] = ..., target_roas: _Optional[_Union[_bidding_pb2.TargetRoas, _Mapping]] = ..., target_spend: _Optional[_Union[_bidding_pb2.TargetSpend, _Mapping]] = ...) -> None: ...
