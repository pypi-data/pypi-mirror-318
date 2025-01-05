from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.apps.events.subscriptions.v1 import subscription_resource_pb2 as _subscription_resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSubscriptionRequest(_message.Message):
    __slots__ = ('subscription', 'validate_only')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_resource_pb2.Subscription
    validate_only: bool

    def __init__(self, subscription: _Optional[_Union[_subscription_resource_pb2.Subscription, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteSubscriptionRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'allow_missing', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    allow_missing: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., allow_missing: bool=..., etag: _Optional[str]=...) -> None:
        ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSubscriptionRequest(_message.Message):
    __slots__ = ('subscription', 'update_mask', 'validate_only')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_resource_pb2.Subscription
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, subscription: _Optional[_Union[_subscription_resource_pb2.Subscription, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class ReactivateSubscriptionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'filter')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsResponse(_message.Message):
    __slots__ = ('subscriptions', 'next_page_token')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_subscription_resource_pb2.Subscription]
    next_page_token: str

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_subscription_resource_pb2.Subscription, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateSubscriptionMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateSubscriptionMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteSubscriptionMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReactivateSubscriptionMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...