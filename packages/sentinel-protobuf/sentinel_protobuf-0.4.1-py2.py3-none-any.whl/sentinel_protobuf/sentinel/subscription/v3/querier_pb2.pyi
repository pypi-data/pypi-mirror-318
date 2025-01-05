from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from sentinel.subscription.v3 import subscription_pb2 as _subscription_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QuerySubscriptionsRequest(_message.Message):
    __slots__ = ('pagination',)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest

    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QuerySubscriptionsForAccountRequest(_message.Message):
    __slots__ = ('address', 'pagination')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    pagination: _pagination_pb2.PageRequest

    def __init__(self, address: _Optional[str]=..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QuerySubscriptionsForPlanRequest(_message.Message):
    __slots__ = ('id', 'pagination')
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    pagination: _pagination_pb2.PageRequest

    def __init__(self, id: _Optional[int]=..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QuerySubscriptionRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class QuerySubscriptionsResponse(_message.Message):
    __slots__ = ('subscriptions', 'pagination')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_subscription_pb2.Subscription]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_subscription_pb2.Subscription, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QuerySubscriptionsForAccountResponse(_message.Message):
    __slots__ = ('subscriptions', 'pagination')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_subscription_pb2.Subscription]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_subscription_pb2.Subscription, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QuerySubscriptionsForPlanResponse(_message.Message):
    __slots__ = ('subscriptions', 'pagination')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_subscription_pb2.Subscription]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_subscription_pb2.Subscription, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QuerySubscriptionResponse(_message.Message):
    __slots__ = ('subscription',)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_pb2.Subscription

    def __init__(self, subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]]=...) -> None:
        ...