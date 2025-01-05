from google.ads.googleads.v16.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v16.resources import feed_mapping_pb2 as _feed_mapping_pb2
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

class MutateFeedMappingsRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[FeedMappingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[FeedMappingOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class FeedMappingOperation(_message.Message):
    __slots__ = ("create", "remove")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    create: _feed_mapping_pb2.FeedMapping
    remove: str
    def __init__(self, create: _Optional[_Union[_feed_mapping_pb2.FeedMapping, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateFeedMappingsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateFeedMappingResult]
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[MutateFeedMappingResult, _Mapping]]] = ...) -> None: ...

class MutateFeedMappingResult(_message.Message):
    __slots__ = ("resource_name", "feed_mapping")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FEED_MAPPING_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    feed_mapping: _feed_mapping_pb2.FeedMapping
    def __init__(self, resource_name: _Optional[str] = ..., feed_mapping: _Optional[_Union[_feed_mapping_pb2.FeedMapping, _Mapping]] = ...) -> None: ...
