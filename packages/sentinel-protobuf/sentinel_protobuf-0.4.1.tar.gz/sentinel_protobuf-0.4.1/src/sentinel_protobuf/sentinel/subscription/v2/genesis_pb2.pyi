from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from sentinel.subscription.v2 import allocation_pb2 as _allocation_pb2
from sentinel.subscription.v2 import params_pb2 as _params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisSubscription(_message.Message):
    __slots__ = ('subscription', 'allocations')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    subscription: _any_pb2.Any
    allocations: _containers.RepeatedCompositeFieldContainer[_allocation_pb2.Allocation]

    def __init__(self, subscription: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., allocations: _Optional[_Iterable[_Union[_allocation_pb2.Allocation, _Mapping]]]=...) -> None:
        ...

class GenesisState(_message.Message):
    __slots__ = ('subscriptions', 'params')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[GenesisSubscription]
    params: _params_pb2.Params

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[GenesisSubscription, _Mapping]]]=..., params: _Optional[_Union[_params_pb2.Params, _Mapping]]=...) -> None:
        ...