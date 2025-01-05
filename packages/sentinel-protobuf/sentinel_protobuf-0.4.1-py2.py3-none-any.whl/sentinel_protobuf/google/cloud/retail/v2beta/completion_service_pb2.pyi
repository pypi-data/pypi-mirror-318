from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2beta import common_pb2 as _common_pb2
from google.cloud.retail.v2beta import import_config_pb2 as _import_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteQueryRequest(_message.Message):
    __slots__ = ("catalog", "query", "visitor_id", "language_codes", "device_type", "dataset", "max_suggestions", "enable_attribute_suggestions", "entity")
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    VISITOR_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    MAX_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ATTRIBUTE_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    query: str
    visitor_id: str
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    device_type: str
    dataset: str
    max_suggestions: int
    enable_attribute_suggestions: bool
    entity: str
    def __init__(self, catalog: _Optional[str] = ..., query: _Optional[str] = ..., visitor_id: _Optional[str] = ..., language_codes: _Optional[_Iterable[str]] = ..., device_type: _Optional[str] = ..., dataset: _Optional[str] = ..., max_suggestions: _Optional[int] = ..., enable_attribute_suggestions: bool = ..., entity: _Optional[str] = ...) -> None: ...

class CompleteQueryResponse(_message.Message):
    __slots__ = ("completion_results", "attribution_token", "recent_search_results", "attribute_results")
    class CompletionResult(_message.Message):
        __slots__ = ("suggestion", "attributes")
        class AttributesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _common_pb2.CustomAttribute
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.CustomAttribute, _Mapping]] = ...) -> None: ...
        SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        suggestion: str
        attributes: _containers.MessageMap[str, _common_pb2.CustomAttribute]
        def __init__(self, suggestion: _Optional[str] = ..., attributes: _Optional[_Mapping[str, _common_pb2.CustomAttribute]] = ...) -> None: ...
    class RecentSearchResult(_message.Message):
        __slots__ = ("recent_search",)
        RECENT_SEARCH_FIELD_NUMBER: _ClassVar[int]
        recent_search: str
        def __init__(self, recent_search: _Optional[str] = ...) -> None: ...
    class AttributeResult(_message.Message):
        __slots__ = ("suggestions",)
        SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
        suggestions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, suggestions: _Optional[_Iterable[str]] = ...) -> None: ...
    class AttributeResultsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CompleteQueryResponse.AttributeResult
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CompleteQueryResponse.AttributeResult, _Mapping]] = ...) -> None: ...
    COMPLETION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RECENT_SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    completion_results: _containers.RepeatedCompositeFieldContainer[CompleteQueryResponse.CompletionResult]
    attribution_token: str
    recent_search_results: _containers.RepeatedCompositeFieldContainer[CompleteQueryResponse.RecentSearchResult]
    attribute_results: _containers.MessageMap[str, CompleteQueryResponse.AttributeResult]
    def __init__(self, completion_results: _Optional[_Iterable[_Union[CompleteQueryResponse.CompletionResult, _Mapping]]] = ..., attribution_token: _Optional[str] = ..., recent_search_results: _Optional[_Iterable[_Union[CompleteQueryResponse.RecentSearchResult, _Mapping]]] = ..., attribute_results: _Optional[_Mapping[str, CompleteQueryResponse.AttributeResult]] = ...) -> None: ...
