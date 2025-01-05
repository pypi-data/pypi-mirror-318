from google.ads.googleads.v18.common import simulation_pb2 as _simulation_pb2
from google.ads.googleads.v18.enums import simulation_modification_method_pb2 as _simulation_modification_method_pb2
from google.ads.googleads.v18.enums import simulation_type_pb2 as _simulation_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterionSimulation(_message.Message):
    __slots__ = ("resource_name", "ad_group_id", "criterion_id", "type", "modification_method", "start_date", "end_date", "cpc_bid_point_list", "percent_cpc_bid_point_list")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODIFICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    PERCENT_CPC_BID_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group_id: int
    criterion_id: int
    type: _simulation_type_pb2.SimulationTypeEnum.SimulationType
    modification_method: _simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: _simulation_pb2.CpcBidSimulationPointList
    percent_cpc_bid_point_list: _simulation_pb2.PercentCpcBidSimulationPointList
    def __init__(self, resource_name: _Optional[str] = ..., ad_group_id: _Optional[int] = ..., criterion_id: _Optional[int] = ..., type: _Optional[_Union[_simulation_type_pb2.SimulationTypeEnum.SimulationType, str]] = ..., modification_method: _Optional[_Union[_simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod, str]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., cpc_bid_point_list: _Optional[_Union[_simulation_pb2.CpcBidSimulationPointList, _Mapping]] = ..., percent_cpc_bid_point_list: _Optional[_Union[_simulation_pb2.PercentCpcBidSimulationPointList, _Mapping]] = ...) -> None: ...
