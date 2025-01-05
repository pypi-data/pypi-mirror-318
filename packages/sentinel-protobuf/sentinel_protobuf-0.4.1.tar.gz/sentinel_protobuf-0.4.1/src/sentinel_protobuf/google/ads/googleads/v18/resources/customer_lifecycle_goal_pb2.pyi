from google.ads.googleads.v18.common import lifecycle_goals_pb2 as _lifecycle_goals_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerLifecycleGoal(_message.Message):
    __slots__ = ("resource_name", "customer_acquisition_goal_value_settings")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ACQUISITION_GOAL_VALUE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    customer_acquisition_goal_value_settings: _lifecycle_goals_pb2.LifecycleGoalValueSettings
    def __init__(self, resource_name: _Optional[str] = ..., customer_acquisition_goal_value_settings: _Optional[_Union[_lifecycle_goals_pb2.LifecycleGoalValueSettings, _Mapping]] = ...) -> None: ...
