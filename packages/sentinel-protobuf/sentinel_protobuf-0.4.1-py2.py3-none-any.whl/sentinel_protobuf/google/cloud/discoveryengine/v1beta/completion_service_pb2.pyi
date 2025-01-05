from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import common_pb2 as _common_pb2
from google.cloud.discoveryengine.v1beta import document_pb2 as _document_pb2
from google.cloud.discoveryengine.v1beta import import_config_pb2 as _import_config_pb2
from google.cloud.discoveryengine.v1beta import purge_config_pb2 as _purge_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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

class AdvancedCompleteQueryRequest(_message.Message):
    __slots__ = ("completion_config", "query", "query_model", "user_pseudo_id", "user_info", "include_tail_suggestions", "boost_spec", "suggestion_types")
    class SuggestionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUGGESTION_TYPE_UNSPECIFIED: _ClassVar[AdvancedCompleteQueryRequest.SuggestionType]
        QUERY: _ClassVar[AdvancedCompleteQueryRequest.SuggestionType]
        PEOPLE: _ClassVar[AdvancedCompleteQueryRequest.SuggestionType]
        CONTENT: _ClassVar[AdvancedCompleteQueryRequest.SuggestionType]
        RECENT_SEARCH: _ClassVar[AdvancedCompleteQueryRequest.SuggestionType]
        GOOGLE_WORKSPACE: _ClassVar[AdvancedCompleteQueryRequest.SuggestionType]
    SUGGESTION_TYPE_UNSPECIFIED: AdvancedCompleteQueryRequest.SuggestionType
    QUERY: AdvancedCompleteQueryRequest.SuggestionType
    PEOPLE: AdvancedCompleteQueryRequest.SuggestionType
    CONTENT: AdvancedCompleteQueryRequest.SuggestionType
    RECENT_SEARCH: AdvancedCompleteQueryRequest.SuggestionType
    GOOGLE_WORKSPACE: AdvancedCompleteQueryRequest.SuggestionType
    class BoostSpec(_message.Message):
        __slots__ = ("condition_boost_specs",)
        class ConditionBoostSpec(_message.Message):
            __slots__ = ("condition", "boost")
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            BOOST_FIELD_NUMBER: _ClassVar[int]
            condition: str
            boost: float
            def __init__(self, condition: _Optional[str] = ..., boost: _Optional[float] = ...) -> None: ...
        CONDITION_BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
        condition_boost_specs: _containers.RepeatedCompositeFieldContainer[AdvancedCompleteQueryRequest.BoostSpec.ConditionBoostSpec]
        def __init__(self, condition_boost_specs: _Optional[_Iterable[_Union[AdvancedCompleteQueryRequest.BoostSpec.ConditionBoostSpec, _Mapping]]] = ...) -> None: ...
    COMPLETION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_MODEL_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TAIL_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    BOOST_SPEC_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    completion_config: str
    query: str
    query_model: str
    user_pseudo_id: str
    user_info: _common_pb2.UserInfo
    include_tail_suggestions: bool
    boost_spec: AdvancedCompleteQueryRequest.BoostSpec
    suggestion_types: _containers.RepeatedScalarFieldContainer[AdvancedCompleteQueryRequest.SuggestionType]
    def __init__(self, completion_config: _Optional[str] = ..., query: _Optional[str] = ..., query_model: _Optional[str] = ..., user_pseudo_id: _Optional[str] = ..., user_info: _Optional[_Union[_common_pb2.UserInfo, _Mapping]] = ..., include_tail_suggestions: bool = ..., boost_spec: _Optional[_Union[AdvancedCompleteQueryRequest.BoostSpec, _Mapping]] = ..., suggestion_types: _Optional[_Iterable[_Union[AdvancedCompleteQueryRequest.SuggestionType, str]]] = ...) -> None: ...

class AdvancedCompleteQueryResponse(_message.Message):
    __slots__ = ("query_suggestions", "tail_match_triggered", "people_suggestions", "content_suggestions", "recent_search_suggestions")
    class QuerySuggestion(_message.Message):
        __slots__ = ("suggestion", "completable_field_paths", "data_store")
        SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        COMPLETABLE_FIELD_PATHS_FIELD_NUMBER: _ClassVar[int]
        DATA_STORE_FIELD_NUMBER: _ClassVar[int]
        suggestion: str
        completable_field_paths: _containers.RepeatedScalarFieldContainer[str]
        data_store: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, suggestion: _Optional[str] = ..., completable_field_paths: _Optional[_Iterable[str]] = ..., data_store: _Optional[_Iterable[str]] = ...) -> None: ...
    class PersonSuggestion(_message.Message):
        __slots__ = ("suggestion", "person_type", "document", "data_store")
        class PersonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PERSON_TYPE_UNSPECIFIED: _ClassVar[AdvancedCompleteQueryResponse.PersonSuggestion.PersonType]
            CLOUD_IDENTITY: _ClassVar[AdvancedCompleteQueryResponse.PersonSuggestion.PersonType]
            THIRD_PARTY_IDENTITY: _ClassVar[AdvancedCompleteQueryResponse.PersonSuggestion.PersonType]
        PERSON_TYPE_UNSPECIFIED: AdvancedCompleteQueryResponse.PersonSuggestion.PersonType
        CLOUD_IDENTITY: AdvancedCompleteQueryResponse.PersonSuggestion.PersonType
        THIRD_PARTY_IDENTITY: AdvancedCompleteQueryResponse.PersonSuggestion.PersonType
        SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        PERSON_TYPE_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        DATA_STORE_FIELD_NUMBER: _ClassVar[int]
        suggestion: str
        person_type: AdvancedCompleteQueryResponse.PersonSuggestion.PersonType
        document: _document_pb2.Document
        data_store: str
        def __init__(self, suggestion: _Optional[str] = ..., person_type: _Optional[_Union[AdvancedCompleteQueryResponse.PersonSuggestion.PersonType, str]] = ..., document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., data_store: _Optional[str] = ...) -> None: ...
    class ContentSuggestion(_message.Message):
        __slots__ = ("suggestion", "content_type", "document", "data_store")
        class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_TYPE_UNSPECIFIED: _ClassVar[AdvancedCompleteQueryResponse.ContentSuggestion.ContentType]
            GOOGLE_WORKSPACE: _ClassVar[AdvancedCompleteQueryResponse.ContentSuggestion.ContentType]
            THIRD_PARTY: _ClassVar[AdvancedCompleteQueryResponse.ContentSuggestion.ContentType]
        CONTENT_TYPE_UNSPECIFIED: AdvancedCompleteQueryResponse.ContentSuggestion.ContentType
        GOOGLE_WORKSPACE: AdvancedCompleteQueryResponse.ContentSuggestion.ContentType
        THIRD_PARTY: AdvancedCompleteQueryResponse.ContentSuggestion.ContentType
        SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        DATA_STORE_FIELD_NUMBER: _ClassVar[int]
        suggestion: str
        content_type: AdvancedCompleteQueryResponse.ContentSuggestion.ContentType
        document: _document_pb2.Document
        data_store: str
        def __init__(self, suggestion: _Optional[str] = ..., content_type: _Optional[_Union[AdvancedCompleteQueryResponse.ContentSuggestion.ContentType, str]] = ..., document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., data_store: _Optional[str] = ...) -> None: ...
    class RecentSearchSuggestion(_message.Message):
        __slots__ = ("suggestion", "recent_search_time")
        SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        RECENT_SEARCH_TIME_FIELD_NUMBER: _ClassVar[int]
        suggestion: str
        recent_search_time: _timestamp_pb2.Timestamp
        def __init__(self, suggestion: _Optional[str] = ..., recent_search_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    QUERY_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    TAIL_MATCH_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    RECENT_SEARCH_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    query_suggestions: _containers.RepeatedCompositeFieldContainer[AdvancedCompleteQueryResponse.QuerySuggestion]
    tail_match_triggered: bool
    people_suggestions: _containers.RepeatedCompositeFieldContainer[AdvancedCompleteQueryResponse.PersonSuggestion]
    content_suggestions: _containers.RepeatedCompositeFieldContainer[AdvancedCompleteQueryResponse.ContentSuggestion]
    recent_search_suggestions: _containers.RepeatedCompositeFieldContainer[AdvancedCompleteQueryResponse.RecentSearchSuggestion]
    def __init__(self, query_suggestions: _Optional[_Iterable[_Union[AdvancedCompleteQueryResponse.QuerySuggestion, _Mapping]]] = ..., tail_match_triggered: bool = ..., people_suggestions: _Optional[_Iterable[_Union[AdvancedCompleteQueryResponse.PersonSuggestion, _Mapping]]] = ..., content_suggestions: _Optional[_Iterable[_Union[AdvancedCompleteQueryResponse.ContentSuggestion, _Mapping]]] = ..., recent_search_suggestions: _Optional[_Iterable[_Union[AdvancedCompleteQueryResponse.RecentSearchSuggestion, _Mapping]]] = ...) -> None: ...
