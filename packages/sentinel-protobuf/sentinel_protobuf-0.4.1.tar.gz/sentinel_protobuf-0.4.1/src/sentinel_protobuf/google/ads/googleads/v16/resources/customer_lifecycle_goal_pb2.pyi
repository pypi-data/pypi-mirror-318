from google.ads.googleads.v16.common import lifecycle_goals_pb2 as _lifecycle_goals_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerLifecycleGoal(_message.Message):
    __slots__ = ("resource_name", "lifecycle_goal_customer_definition_settings", "customer_acquisition_goal_value_settings")
    class LifecycleGoalCustomerDefinitionSettings(_message.Message):
        __slots__ = ("existing_user_lists", "high_lifetime_value_user_lists")
        EXISTING_USER_LISTS_FIELD_NUMBER: _ClassVar[int]
        HIGH_LIFETIME_VALUE_USER_LISTS_FIELD_NUMBER: _ClassVar[int]
        existing_user_lists: _containers.RepeatedScalarFieldContainer[str]
        high_lifetime_value_user_lists: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, existing_user_lists: _Optional[_Iterable[str]] = ..., high_lifetime_value_user_lists: _Optional[_Iterable[str]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_GOAL_CUSTOMER_DEFINITION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ACQUISITION_GOAL_VALUE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    lifecycle_goal_customer_definition_settings: CustomerLifecycleGoal.LifecycleGoalCustomerDefinitionSettings
    customer_acquisition_goal_value_settings: _lifecycle_goals_pb2.LifecycleGoalValueSettings
    def __init__(self, resource_name: _Optional[str] = ..., lifecycle_goal_customer_definition_settings: _Optional[_Union[CustomerLifecycleGoal.LifecycleGoalCustomerDefinitionSettings, _Mapping]] = ..., customer_acquisition_goal_value_settings: _Optional[_Union[_lifecycle_goals_pb2.LifecycleGoalValueSettings, _Mapping]] = ...) -> None: ...
