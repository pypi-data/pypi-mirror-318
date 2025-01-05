from google.ads.googleads.v18.enums import custom_conversion_goal_status_pb2 as _custom_conversion_goal_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomConversionGoal(_message.Message):
    __slots__ = ('resource_name', 'id', 'name', 'conversion_actions', 'status')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    conversion_actions: _containers.RepeatedScalarFieldContainer[str]
    status: _custom_conversion_goal_status_pb2.CustomConversionGoalStatusEnum.CustomConversionGoalStatus

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., name: _Optional[str]=..., conversion_actions: _Optional[_Iterable[str]]=..., status: _Optional[_Union[_custom_conversion_goal_status_pb2.CustomConversionGoalStatusEnum.CustomConversionGoalStatus, str]]=...) -> None:
        ...