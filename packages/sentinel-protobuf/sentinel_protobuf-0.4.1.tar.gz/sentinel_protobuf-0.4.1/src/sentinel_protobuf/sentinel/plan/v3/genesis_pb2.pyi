from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.plan.v3 import plan_pb2 as _plan_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisPlan(_message.Message):
    __slots__ = ('plan', 'nodes')
    PLAN_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    plan: _plan_pb2.Plan
    nodes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, plan: _Optional[_Union[_plan_pb2.Plan, _Mapping]]=..., nodes: _Optional[_Iterable[str]]=...) -> None:
        ...

class GenesisState(_message.Message):
    __slots__ = ('plans',)
    PLANS_FIELD_NUMBER: _ClassVar[int]
    plans: _containers.RepeatedCompositeFieldContainer[GenesisPlan]

    def __init__(self, plans: _Optional[_Iterable[_Union[GenesisPlan, _Mapping]]]=...) -> None:
        ...