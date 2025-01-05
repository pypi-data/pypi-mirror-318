from google.ads.googleads.v16.common import lifecycle_goals_pb2 as _lifecycle_goals_pb2
from google.ads.googleads.v16.enums import customer_acquisition_optimization_mode_pb2 as _customer_acquisition_optimization_mode_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignLifecycleGoal(_message.Message):
    __slots__ = ("resource_name", "campaign", "customer_acquisition_goal_settings")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ACQUISITION_GOAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings
    def __init__(self, resource_name: _Optional[str] = ..., campaign: _Optional[str] = ..., customer_acquisition_goal_settings: _Optional[_Union[CustomerAcquisitionGoalSettings, _Mapping]] = ...) -> None: ...

class CustomerAcquisitionGoalSettings(_message.Message):
    __slots__ = ("optimization_mode", "value_settings")
    OPTIMIZATION_MODE_FIELD_NUMBER: _ClassVar[int]
    VALUE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    optimization_mode: _customer_acquisition_optimization_mode_pb2.CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    value_settings: _lifecycle_goals_pb2.LifecycleGoalValueSettings
    def __init__(self, optimization_mode: _Optional[_Union[_customer_acquisition_optimization_mode_pb2.CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode, str]] = ..., value_settings: _Optional[_Union[_lifecycle_goals_pb2.LifecycleGoalValueSettings, _Mapping]] = ...) -> None: ...
