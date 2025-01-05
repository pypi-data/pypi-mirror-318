from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.pubsublite.v1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateTopicRequest(_message.Message):
    __slots__ = ('parent', 'topic', 'topic_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    topic: _common_pb2.Topic
    topic_id: str

    def __init__(self, parent: _Optional[str]=..., topic: _Optional[_Union[_common_pb2.Topic, _Mapping]]=..., topic_id: _Optional[str]=...) -> None:
        ...

class GetTopicRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetTopicPartitionsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class TopicPartitions(_message.Message):
    __slots__ = ('partition_count',)
    PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    partition_count: int

    def __init__(self, partition_count: _Optional[int]=...) -> None:
        ...

class ListTopicsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTopicsResponse(_message.Message):
    __slots__ = ('topics', 'next_page_token')
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Topic]
    next_page_token: str

    def __init__(self, topics: _Optional[_Iterable[_Union[_common_pb2.Topic, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateTopicRequest(_message.Message):
    __slots__ = ('topic', 'update_mask')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    topic: _common_pb2.Topic
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, topic: _Optional[_Union[_common_pb2.Topic, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteTopicRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTopicSubscriptionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTopicSubscriptionsResponse(_message.Message):
    __slots__ = ('subscriptions', 'next_page_token')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, subscriptions: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateSubscriptionRequest(_message.Message):
    __slots__ = ('parent', 'subscription', 'subscription_id', 'skip_backlog')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_BACKLOG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    subscription: _common_pb2.Subscription
    subscription_id: str
    skip_backlog: bool

    def __init__(self, parent: _Optional[str]=..., subscription: _Optional[_Union[_common_pb2.Subscription, _Mapping]]=..., subscription_id: _Optional[str]=..., skip_backlog: bool=...) -> None:
        ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsResponse(_message.Message):
    __slots__ = ('subscriptions', 'next_page_token')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Subscription]
    next_page_token: str

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_common_pb2.Subscription, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateSubscriptionRequest(_message.Message):
    __slots__ = ('subscription', 'update_mask')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    subscription: _common_pb2.Subscription
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, subscription: _Optional[_Union[_common_pb2.Subscription, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSubscriptionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SeekSubscriptionRequest(_message.Message):
    __slots__ = ('name', 'named_target', 'time_target')

    class NamedTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NAMED_TARGET_UNSPECIFIED: _ClassVar[SeekSubscriptionRequest.NamedTarget]
        TAIL: _ClassVar[SeekSubscriptionRequest.NamedTarget]
        HEAD: _ClassVar[SeekSubscriptionRequest.NamedTarget]
    NAMED_TARGET_UNSPECIFIED: SeekSubscriptionRequest.NamedTarget
    TAIL: SeekSubscriptionRequest.NamedTarget
    HEAD: SeekSubscriptionRequest.NamedTarget
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMED_TARGET_FIELD_NUMBER: _ClassVar[int]
    TIME_TARGET_FIELD_NUMBER: _ClassVar[int]
    name: str
    named_target: SeekSubscriptionRequest.NamedTarget
    time_target: _common_pb2.TimeTarget

    def __init__(self, name: _Optional[str]=..., named_target: _Optional[_Union[SeekSubscriptionRequest.NamedTarget, str]]=..., time_target: _Optional[_Union[_common_pb2.TimeTarget, _Mapping]]=...) -> None:
        ...

class SeekSubscriptionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=...) -> None:
        ...

class CreateReservationRequest(_message.Message):
    __slots__ = ('parent', 'reservation', 'reservation_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reservation: _common_pb2.Reservation
    reservation_id: str

    def __init__(self, parent: _Optional[str]=..., reservation: _Optional[_Union[_common_pb2.Reservation, _Mapping]]=..., reservation_id: _Optional[str]=...) -> None:
        ...

class GetReservationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListReservationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReservationsResponse(_message.Message):
    __slots__ = ('reservations', 'next_page_token')
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reservations: _containers.RepeatedCompositeFieldContainer[_common_pb2.Reservation]
    next_page_token: str

    def __init__(self, reservations: _Optional[_Iterable[_Union[_common_pb2.Reservation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateReservationRequest(_message.Message):
    __slots__ = ('reservation', 'update_mask')
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    reservation: _common_pb2.Reservation
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, reservation: _Optional[_Union[_common_pb2.Reservation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteReservationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListReservationTopicsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReservationTopicsResponse(_message.Message):
    __slots__ = ('topics', 'next_page_token')
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, topics: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...