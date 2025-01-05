from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.managedkafka.v1 import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListClustersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "next_page_token", "unreachable")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Cluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, clusters: _Optional[_Iterable[_Union[_resources_pb2.Cluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("parent", "cluster_id", "cluster", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: _resources_pb2.Cluster
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("update_mask", "cluster", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    cluster: _resources_pb2.Cluster
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListTopicsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTopicsResponse(_message.Message):
    __slots__ = ("topics", "next_page_token")
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Topic]
    next_page_token: str
    def __init__(self, topics: _Optional[_Iterable[_Union[_resources_pb2.Topic, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetTopicRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateTopicRequest(_message.Message):
    __slots__ = ("parent", "topic_id", "topic")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    topic_id: str
    topic: _resources_pb2.Topic
    def __init__(self, parent: _Optional[str] = ..., topic_id: _Optional[str] = ..., topic: _Optional[_Union[_resources_pb2.Topic, _Mapping]] = ...) -> None: ...

class UpdateTopicRequest(_message.Message):
    __slots__ = ("update_mask", "topic")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    topic: _resources_pb2.Topic
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., topic: _Optional[_Union[_resources_pb2.Topic, _Mapping]] = ...) -> None: ...

class DeleteTopicRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListConsumerGroupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListConsumerGroupsResponse(_message.Message):
    __slots__ = ("consumer_groups", "next_page_token")
    CONSUMER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    consumer_groups: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ConsumerGroup]
    next_page_token: str
    def __init__(self, consumer_groups: _Optional[_Iterable[_Union[_resources_pb2.ConsumerGroup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetConsumerGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateConsumerGroupRequest(_message.Message):
    __slots__ = ("update_mask", "consumer_group")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    consumer_group: _resources_pb2.ConsumerGroup
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., consumer_group: _Optional[_Union[_resources_pb2.ConsumerGroup, _Mapping]] = ...) -> None: ...

class DeleteConsumerGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
