from google.ads.googleads.v16.resources import feed_item_set_link_pb2 as _feed_item_set_link_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MutateFeedItemSetLinksRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'partial_failure', 'validate_only')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[FeedItemSetLinkOperation]
    partial_failure: bool
    validate_only: bool

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[FeedItemSetLinkOperation, _Mapping]]]=..., partial_failure: bool=..., validate_only: bool=...) -> None:
        ...

class FeedItemSetLinkOperation(_message.Message):
    __slots__ = ('create', 'remove')
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    create: _feed_item_set_link_pb2.FeedItemSetLink
    remove: str

    def __init__(self, create: _Optional[_Union[_feed_item_set_link_pb2.FeedItemSetLink, _Mapping]]=..., remove: _Optional[str]=...) -> None:
        ...

class MutateFeedItemSetLinksResponse(_message.Message):
    __slots__ = ('results', 'partial_failure_error')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateFeedItemSetLinkResult]
    partial_failure_error: _status_pb2.Status

    def __init__(self, results: _Optional[_Iterable[_Union[MutateFeedItemSetLinkResult, _Mapping]]]=..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class MutateFeedItemSetLinkResult(_message.Message):
    __slots__ = ('resource_name',)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str

    def __init__(self, resource_name: _Optional[str]=...) -> None:
        ...