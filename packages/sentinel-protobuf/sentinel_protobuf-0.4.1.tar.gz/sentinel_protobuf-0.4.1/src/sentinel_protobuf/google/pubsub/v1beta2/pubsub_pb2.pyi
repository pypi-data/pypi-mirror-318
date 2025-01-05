from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Topic(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PubsubMessage(_message.Message):
    __slots__ = ('data', 'attributes', 'message_id')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    attributes: _containers.ScalarMap[str, str]
    message_id: str

    def __init__(self, data: _Optional[bytes]=..., attributes: _Optional[_Mapping[str, str]]=..., message_id: _Optional[str]=...) -> None:
        ...

class GetTopicRequest(_message.Message):
    __slots__ = ('topic',)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str

    def __init__(self, topic: _Optional[str]=...) -> None:
        ...

class PublishRequest(_message.Message):
    __slots__ = ('topic', 'messages')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    topic: str
    messages: _containers.RepeatedCompositeFieldContainer[PubsubMessage]

    def __init__(self, topic: _Optional[str]=..., messages: _Optional[_Iterable[_Union[PubsubMessage, _Mapping]]]=...) -> None:
        ...

class PublishResponse(_message.Message):
    __slots__ = ('message_ids',)
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    message_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, message_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListTopicsRequest(_message.Message):
    __slots__ = ('project', 'page_size', 'page_token')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project: str
    page_size: int
    page_token: str

    def __init__(self, project: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTopicsResponse(_message.Message):
    __slots__ = ('topics', 'next_page_token')
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[Topic]
    next_page_token: str

    def __init__(self, topics: _Optional[_Iterable[_Union[Topic, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListTopicSubscriptionsRequest(_message.Message):
    __slots__ = ('topic', 'page_size', 'page_token')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    topic: str
    page_size: int
    page_token: str

    def __init__(self, topic: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTopicSubscriptionsResponse(_message.Message):
    __slots__ = ('subscriptions', 'next_page_token')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, subscriptions: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteTopicRequest(_message.Message):
    __slots__ = ('topic',)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str

    def __init__(self, topic: _Optional[str]=...) -> None:
        ...

class Subscription(_message.Message):
    __slots__ = ('name', 'topic', 'push_config', 'ack_deadline_seconds')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PUSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACK_DEADLINE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    topic: str
    push_config: PushConfig
    ack_deadline_seconds: int

    def __init__(self, name: _Optional[str]=..., topic: _Optional[str]=..., push_config: _Optional[_Union[PushConfig, _Mapping]]=..., ack_deadline_seconds: _Optional[int]=...) -> None:
        ...

class PushConfig(_message.Message):
    __slots__ = ('push_endpoint', 'attributes')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PUSH_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    push_endpoint: str
    attributes: _containers.ScalarMap[str, str]

    def __init__(self, push_endpoint: _Optional[str]=..., attributes: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ReceivedMessage(_message.Message):
    __slots__ = ('ack_id', 'message')
    ACK_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ack_id: str
    message: PubsubMessage

    def __init__(self, ack_id: _Optional[str]=..., message: _Optional[_Union[PubsubMessage, _Mapping]]=...) -> None:
        ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ('subscription',)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: str

    def __init__(self, subscription: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsRequest(_message.Message):
    __slots__ = ('project', 'page_size', 'page_token')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project: str
    page_size: int
    page_token: str

    def __init__(self, project: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsResponse(_message.Message):
    __slots__ = ('subscriptions', 'next_page_token')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[Subscription]
    next_page_token: str

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[Subscription, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteSubscriptionRequest(_message.Message):
    __slots__ = ('subscription',)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: str

    def __init__(self, subscription: _Optional[str]=...) -> None:
        ...

class ModifyPushConfigRequest(_message.Message):
    __slots__ = ('subscription', 'push_config')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PUSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    push_config: PushConfig

    def __init__(self, subscription: _Optional[str]=..., push_config: _Optional[_Union[PushConfig, _Mapping]]=...) -> None:
        ...

class PullRequest(_message.Message):
    __slots__ = ('subscription', 'return_immediately', 'max_messages')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RETURN_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    return_immediately: bool
    max_messages: int

    def __init__(self, subscription: _Optional[str]=..., return_immediately: bool=..., max_messages: _Optional[int]=...) -> None:
        ...

class PullResponse(_message.Message):
    __slots__ = ('received_messages',)
    RECEIVED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    received_messages: _containers.RepeatedCompositeFieldContainer[ReceivedMessage]

    def __init__(self, received_messages: _Optional[_Iterable[_Union[ReceivedMessage, _Mapping]]]=...) -> None:
        ...

class ModifyAckDeadlineRequest(_message.Message):
    __slots__ = ('subscription', 'ack_id', 'ack_deadline_seconds')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACK_ID_FIELD_NUMBER: _ClassVar[int]
    ACK_DEADLINE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    ack_id: str
    ack_deadline_seconds: int

    def __init__(self, subscription: _Optional[str]=..., ack_id: _Optional[str]=..., ack_deadline_seconds: _Optional[int]=...) -> None:
        ...

class AcknowledgeRequest(_message.Message):
    __slots__ = ('subscription', 'ack_ids')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACK_IDS_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    ack_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, subscription: _Optional[str]=..., ack_ids: _Optional[_Iterable[str]]=...) -> None:
        ...