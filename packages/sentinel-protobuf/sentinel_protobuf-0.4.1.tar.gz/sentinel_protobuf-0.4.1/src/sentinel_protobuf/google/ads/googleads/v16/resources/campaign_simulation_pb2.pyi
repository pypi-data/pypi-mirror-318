from google.ads.googleads.v16.common import simulation_pb2 as _simulation_pb2
from google.ads.googleads.v16.enums import simulation_modification_method_pb2 as _simulation_modification_method_pb2
from google.ads.googleads.v16.enums import simulation_type_pb2 as _simulation_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignSimulation(_message.Message):
    __slots__ = ("resource_name", "campaign_id", "type", "modification_method", "start_date", "end_date", "cpc_bid_point_list", "target_cpa_point_list", "target_roas_point_list", "target_impression_share_point_list", "budget_point_list")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODIFICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_IMPRESSION_SHARE_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    BUDGET_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign_id: int
    type: _simulation_type_pb2.SimulationTypeEnum.SimulationType
    modification_method: _simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: _simulation_pb2.CpcBidSimulationPointList
    target_cpa_point_list: _simulation_pb2.TargetCpaSimulationPointList
    target_roas_point_list: _simulation_pb2.TargetRoasSimulationPointList
    target_impression_share_point_list: _simulation_pb2.TargetImpressionShareSimulationPointList
    budget_point_list: _simulation_pb2.BudgetSimulationPointList
    def __init__(self, resource_name: _Optional[str] = ..., campaign_id: _Optional[int] = ..., type: _Optional[_Union[_simulation_type_pb2.SimulationTypeEnum.SimulationType, str]] = ..., modification_method: _Optional[_Union[_simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod, str]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., cpc_bid_point_list: _Optional[_Union[_simulation_pb2.CpcBidSimulationPointList, _Mapping]] = ..., target_cpa_point_list: _Optional[_Union[_simulation_pb2.TargetCpaSimulationPointList, _Mapping]] = ..., target_roas_point_list: _Optional[_Union[_simulation_pb2.TargetRoasSimulationPointList, _Mapping]] = ..., target_impression_share_point_list: _Optional[_Union[_simulation_pb2.TargetImpressionShareSimulationPointList, _Mapping]] = ..., budget_point_list: _Optional[_Union[_simulation_pb2.BudgetSimulationPointList, _Mapping]] = ...) -> None: ...
