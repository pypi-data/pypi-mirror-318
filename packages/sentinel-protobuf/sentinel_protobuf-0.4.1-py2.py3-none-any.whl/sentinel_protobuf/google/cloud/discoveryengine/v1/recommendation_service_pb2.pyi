from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import document_pb2 as _document_pb2
from google.cloud.discoveryengine.v1 import user_event_pb2 as _user_event_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecommendRequest(_message.Message):
    __slots__ = ("serving_config", "user_event", "page_size", "filter", "validate_only", "params", "user_labels")
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    serving_config: str
    user_event: _user_event_pb2.UserEvent
    page_size: int
    filter: str
    validate_only: bool
    params: _containers.MessageMap[str, _struct_pb2.Value]
    user_labels: _containers.ScalarMap[str, str]
    def __init__(self, serving_config: _Optional[str] = ..., user_event: _Optional[_Union[_user_event_pb2.UserEvent, _Mapping]] = ..., page_size: _Optional[int] = ..., filter: _Optional[str] = ..., validate_only: bool = ..., params: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., user_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RecommendResponse(_message.Message):
    __slots__ = ("results", "attribution_token", "missing_ids", "validate_only")
    class RecommendationResult(_message.Message):
        __slots__ = ("id", "document", "metadata")
        class MetadataEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        id: str
        document: _document_pb2.Document
        metadata: _containers.MessageMap[str, _struct_pb2.Value]
        def __init__(self, id: _Optional[str] = ..., document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MISSING_IDS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[RecommendResponse.RecommendationResult]
    attribution_token: str
    missing_ids: _containers.RepeatedScalarFieldContainer[str]
    validate_only: bool
    def __init__(self, results: _Optional[_Iterable[_Union[RecommendResponse.RecommendationResult, _Mapping]]] = ..., attribution_token: _Optional[str] = ..., missing_ids: _Optional[_Iterable[str]] = ..., validate_only: bool = ...) -> None: ...
