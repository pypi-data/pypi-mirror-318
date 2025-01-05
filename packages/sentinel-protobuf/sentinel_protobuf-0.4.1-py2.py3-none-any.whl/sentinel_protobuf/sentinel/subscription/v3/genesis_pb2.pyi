from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.subscription.v2 import allocation_pb2 as _allocation_pb2
from sentinel.subscription.v2 import params_pb2 as _params_pb2
from sentinel.subscription.v3 import subscription_pb2 as _subscription_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ('allocations', 'subscriptions', 'params')
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    allocations: _containers.RepeatedCompositeFieldContainer[_allocation_pb2.Allocation]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_subscription_pb2.Subscription]
    params: _params_pb2.Params

    def __init__(self, allocations: _Optional[_Iterable[_Union[_allocation_pb2.Allocation, _Mapping]]]=..., subscriptions: _Optional[_Iterable[_Union[_subscription_pb2.Subscription, _Mapping]]]=..., params: _Optional[_Union[_params_pb2.Params, _Mapping]]=...) -> None:
        ...