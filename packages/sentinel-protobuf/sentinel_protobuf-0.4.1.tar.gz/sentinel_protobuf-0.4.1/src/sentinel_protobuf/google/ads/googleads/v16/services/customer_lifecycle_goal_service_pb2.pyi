from google.ads.googleads.v16.resources import customer_lifecycle_goal_pb2 as _customer_lifecycle_goal_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigureCustomerLifecycleGoalsRequest(_message.Message):
    __slots__ = ("customer_id", "operation", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: CustomerLifecycleGoalOperation
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[CustomerLifecycleGoalOperation, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class CustomerLifecycleGoalOperation(_message.Message):
    __slots__ = ("update_mask", "create", "update")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _customer_lifecycle_goal_pb2.CustomerLifecycleGoal
    update: _customer_lifecycle_goal_pb2.CustomerLifecycleGoal
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_customer_lifecycle_goal_pb2.CustomerLifecycleGoal, _Mapping]] = ..., update: _Optional[_Union[_customer_lifecycle_goal_pb2.CustomerLifecycleGoal, _Mapping]] = ...) -> None: ...

class ConfigureCustomerLifecycleGoalsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ConfigureCustomerLifecycleGoalsResult
    def __init__(self, result: _Optional[_Union[ConfigureCustomerLifecycleGoalsResult, _Mapping]] = ...) -> None: ...

class ConfigureCustomerLifecycleGoalsResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
