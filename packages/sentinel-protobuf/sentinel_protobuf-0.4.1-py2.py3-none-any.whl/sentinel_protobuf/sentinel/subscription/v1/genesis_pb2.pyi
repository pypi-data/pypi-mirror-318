from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.subscription.v1 import params_pb2 as _params_pb2
from sentinel.subscription.v1 import quota_pb2 as _quota_pb2
from sentinel.subscription.v1 import subscription_pb2 as _subscription_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisSubscription(_message.Message):
    __slots__ = ('subscription', 'quotas')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUOTAS_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_pb2.Subscription
    quotas: _containers.RepeatedCompositeFieldContainer[_quota_pb2.Quota]

    def __init__(self, subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]]=..., quotas: _Optional[_Iterable[_Union[_quota_pb2.Quota, _Mapping]]]=...) -> None:
        ...

class GenesisState(_message.Message):
    __slots__ = ('subscriptions', 'params')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[GenesisSubscription]
    params: _params_pb2.Params

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[GenesisSubscription, _Mapping]]]=..., params: _Optional[_Union[_params_pb2.Params, _Mapping]]=...) -> None:
        ...