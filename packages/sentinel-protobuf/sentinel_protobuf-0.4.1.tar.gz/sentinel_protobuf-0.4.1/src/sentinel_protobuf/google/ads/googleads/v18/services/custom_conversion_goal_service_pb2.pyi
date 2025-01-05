from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import custom_conversion_goal_pb2 as _custom_conversion_goal_pb2
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

class MutateCustomConversionGoalsRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'validate_only', 'response_content_type')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[CustomConversionGoalOperation]
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[CustomConversionGoalOperation, _Mapping]]]=..., validate_only: bool=..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]]=...) -> None:
        ...

class CustomConversionGoalOperation(_message.Message):
    __slots__ = ('update_mask', 'create', 'update', 'remove')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _custom_conversion_goal_pb2.CustomConversionGoal
    update: _custom_conversion_goal_pb2.CustomConversionGoal
    remove: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., create: _Optional[_Union[_custom_conversion_goal_pb2.CustomConversionGoal, _Mapping]]=..., update: _Optional[_Union[_custom_conversion_goal_pb2.CustomConversionGoal, _Mapping]]=..., remove: _Optional[str]=...) -> None:
        ...

class MutateCustomConversionGoalsResponse(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateCustomConversionGoalResult]

    def __init__(self, results: _Optional[_Iterable[_Union[MutateCustomConversionGoalResult, _Mapping]]]=...) -> None:
        ...

class MutateCustomConversionGoalResult(_message.Message):
    __slots__ = ('resource_name', 'custom_conversion_goal')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONVERSION_GOAL_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    custom_conversion_goal: _custom_conversion_goal_pb2.CustomConversionGoal

    def __init__(self, resource_name: _Optional[str]=..., custom_conversion_goal: _Optional[_Union[_custom_conversion_goal_pb2.CustomConversionGoal, _Mapping]]=...) -> None:
        ...