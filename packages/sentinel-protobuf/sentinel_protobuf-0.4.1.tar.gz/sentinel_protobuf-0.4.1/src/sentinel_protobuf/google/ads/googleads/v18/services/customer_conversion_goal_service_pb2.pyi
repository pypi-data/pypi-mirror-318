from google.ads.googleads.v18.resources import customer_conversion_goal_pb2 as _customer_conversion_goal_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MutateCustomerConversionGoalsRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'validate_only')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[CustomerConversionGoalOperation]
    validate_only: bool

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[CustomerConversionGoalOperation, _Mapping]]]=..., validate_only: bool=...) -> None:
        ...

class CustomerConversionGoalOperation(_message.Message):
    __slots__ = ('update_mask', 'update')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    update: _customer_conversion_goal_pb2.CustomerConversionGoal

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., update: _Optional[_Union[_customer_conversion_goal_pb2.CustomerConversionGoal, _Mapping]]=...) -> None:
        ...

class MutateCustomerConversionGoalsResponse(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateCustomerConversionGoalResult]

    def __init__(self, results: _Optional[_Iterable[_Union[MutateCustomerConversionGoalResult, _Mapping]]]=...) -> None:
        ...

class MutateCustomerConversionGoalResult(_message.Message):
    __slots__ = ('resource_name',)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str

    def __init__(self, resource_name: _Optional[str]=...) -> None:
        ...