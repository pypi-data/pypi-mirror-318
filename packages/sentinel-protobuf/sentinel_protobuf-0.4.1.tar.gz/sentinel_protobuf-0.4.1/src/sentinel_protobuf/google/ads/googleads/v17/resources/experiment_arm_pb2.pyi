from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentArm(_message.Message):
    __slots__ = ('resource_name', 'experiment', 'name', 'control', 'traffic_split', 'campaigns', 'in_design_campaigns')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SPLIT_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    IN_DESIGN_CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    experiment: str
    name: str
    control: bool
    traffic_split: int
    campaigns: _containers.RepeatedScalarFieldContainer[str]
    in_design_campaigns: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, resource_name: _Optional[str]=..., experiment: _Optional[str]=..., name: _Optional[str]=..., control: bool=..., traffic_split: _Optional[int]=..., campaigns: _Optional[_Iterable[str]]=..., in_design_campaigns: _Optional[_Iterable[str]]=...) -> None:
        ...