from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import import_config_pb2 as _import_config_pb2
from google.cloud.discoveryengine.v1alpha import purge_config_pb2 as _purge_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteQueryRequest(_message.Message):
    __slots__ = ("data_store", "query", "query_model", "user_pseudo_id", "include_tail_suggestions")
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_MODEL_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TAIL_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    data_store: str
    query: str
    query_model: str
    user_pseudo_id: str
    include_tail_suggestions: bool
    def __init__(self, data_store: _Optional[str] = ..., query: _Optional[str] = ..., query_model: _Optional[str] = ..., user_pseudo_id: _Optional[str] = ..., include_tail_suggestions: bool = ...) -> None: ...

class CompleteQueryResponse(_message.Message):
    __slots__ = ("query_suggestions", "tail_match_triggered")
    class QuerySuggestion(_message.Message):
        __slots__ = ("suggestion", "completable_field_paths")
        SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        COMPLETABLE_FIELD_PATHS_FIELD_NUMBER: _ClassVar[int]
        suggestion: str
        completable_field_paths: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, suggestion: _Optional[str] = ..., completable_field_paths: _Optional[_Iterable[str]] = ...) -> None: ...
    QUERY_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    TAIL_MATCH_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    query_suggestions: _containers.RepeatedCompositeFieldContainer[CompleteQueryResponse.QuerySuggestion]
    tail_match_triggered: bool
    def __init__(self, query_suggestions: _Optional[_Iterable[_Union[CompleteQueryResponse.QuerySuggestion, _Mapping]]] = ..., tail_match_triggered: bool = ...) -> None: ...
