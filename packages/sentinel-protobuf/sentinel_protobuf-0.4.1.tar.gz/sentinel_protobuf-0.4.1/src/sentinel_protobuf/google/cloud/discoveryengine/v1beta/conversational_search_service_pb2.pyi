from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import answer_pb2 as _answer_pb2
from google.cloud.discoveryengine.v1beta import conversation_pb2 as _conversation_pb2
from google.cloud.discoveryengine.v1beta import search_service_pb2 as _search_service_pb2
from google.cloud.discoveryengine.v1beta import session_pb2 as _session_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConverseConversationRequest(_message.Message):
    __slots__ = ("name", "query", "serving_config", "conversation", "safe_search", "user_labels", "summary_spec", "filter", "boost_spec")
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    SAFE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_SPEC_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    BOOST_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: _conversation_pb2.TextInput
    serving_config: str
    conversation: _conversation_pb2.Conversation
    safe_search: bool
    user_labels: _containers.ScalarMap[str, str]
    summary_spec: _search_service_pb2.SearchRequest.ContentSearchSpec.SummarySpec
    filter: str
    boost_spec: _search_service_pb2.SearchRequest.BoostSpec
    def __init__(self, name: _Optional[str] = ..., query: _Optional[_Union[_conversation_pb2.TextInput, _Mapping]] = ..., serving_config: _Optional[str] = ..., conversation: _Optional[_Union[_conversation_pb2.Conversation, _Mapping]] = ..., safe_search: bool = ..., user_labels: _Optional[_Mapping[str, str]] = ..., summary_spec: _Optional[_Union[_search_service_pb2.SearchRequest.ContentSearchSpec.SummarySpec, _Mapping]] = ..., filter: _Optional[str] = ..., boost_spec: _Optional[_Union[_search_service_pb2.SearchRequest.BoostSpec, _Mapping]] = ...) -> None: ...

class ConverseConversationResponse(_message.Message):
    __slots__ = ("reply", "conversation", "related_questions", "search_results")
    REPLY_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    RELATED_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    reply: _conversation_pb2.Reply
    conversation: _conversation_pb2.Conversation
    related_questions: _containers.RepeatedScalarFieldContainer[str]
    search_results: _containers.RepeatedCompositeFieldContainer[_search_service_pb2.SearchResponse.SearchResult]
    def __init__(self, reply: _Optional[_Union[_conversation_pb2.Reply, _Mapping]] = ..., conversation: _Optional[_Union[_conversation_pb2.Conversation, _Mapping]] = ..., related_questions: _Optional[_Iterable[str]] = ..., search_results: _Optional[_Iterable[_Union[_search_service_pb2.SearchResponse.SearchResult, _Mapping]]] = ...) -> None: ...

class CreateConversationRequest(_message.Message):
    __slots__ = ("parent", "conversation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation: _conversation_pb2.Conversation
    def __init__(self, parent: _Optional[str] = ..., conversation: _Optional[_Union[_conversation_pb2.Conversation, _Mapping]] = ...) -> None: ...

class UpdateConversationRequest(_message.Message):
    __slots__ = ("conversation", "update_mask")
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    conversation: _conversation_pb2.Conversation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, conversation: _Optional[_Union[_conversation_pb2.Conversation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteConversationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetConversationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListConversationsRequest(_message.Message):
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

class ListConversationsResponse(_message.Message):
    __slots__ = ("conversations", "next_page_token")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[_conversation_pb2.Conversation]
    next_page_token: str
    def __init__(self, conversations: _Optional[_Iterable[_Union[_conversation_pb2.Conversation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AnswerQueryRequest(_message.Message):
    __slots__ = ("serving_config", "query", "session", "safety_spec", "related_questions_spec", "grounding_spec", "answer_generation_spec", "search_spec", "query_understanding_spec", "asynchronous_mode", "user_pseudo_id", "user_labels")
    class SafetySpec(_message.Message):
        __slots__ = ("enable",)
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        enable: bool
        def __init__(self, enable: bool = ...) -> None: ...
    class RelatedQuestionsSpec(_message.Message):
        __slots__ = ("enable",)
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        enable: bool
        def __init__(self, enable: bool = ...) -> None: ...
    class GroundingSpec(_message.Message):
        __slots__ = ("include_grounding_supports", "filtering_level")
        class FilteringLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FILTERING_LEVEL_UNSPECIFIED: _ClassVar[AnswerQueryRequest.GroundingSpec.FilteringLevel]
            FILTERING_LEVEL_LOW: _ClassVar[AnswerQueryRequest.GroundingSpec.FilteringLevel]
            FILTERING_LEVEL_HIGH: _ClassVar[AnswerQueryRequest.GroundingSpec.FilteringLevel]
        FILTERING_LEVEL_UNSPECIFIED: AnswerQueryRequest.GroundingSpec.FilteringLevel
        FILTERING_LEVEL_LOW: AnswerQueryRequest.GroundingSpec.FilteringLevel
        FILTERING_LEVEL_HIGH: AnswerQueryRequest.GroundingSpec.FilteringLevel
        INCLUDE_GROUNDING_SUPPORTS_FIELD_NUMBER: _ClassVar[int]
        FILTERING_LEVEL_FIELD_NUMBER: _ClassVar[int]
        include_grounding_supports: bool
        filtering_level: AnswerQueryRequest.GroundingSpec.FilteringLevel
        def __init__(self, include_grounding_supports: bool = ..., filtering_level: _Optional[_Union[AnswerQueryRequest.GroundingSpec.FilteringLevel, str]] = ...) -> None: ...
    class AnswerGenerationSpec(_message.Message):
        __slots__ = ("model_spec", "prompt_spec", "include_citations", "answer_language_code", "ignore_adversarial_query", "ignore_non_answer_seeking_query", "ignore_low_relevant_content", "ignore_jail_breaking_query")
        class ModelSpec(_message.Message):
            __slots__ = ("model_version",)
            MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
            model_version: str
            def __init__(self, model_version: _Optional[str] = ...) -> None: ...
        class PromptSpec(_message.Message):
            __slots__ = ("preamble",)
            PREAMBLE_FIELD_NUMBER: _ClassVar[int]
            preamble: str
            def __init__(self, preamble: _Optional[str] = ...) -> None: ...
        MODEL_SPEC_FIELD_NUMBER: _ClassVar[int]
        PROMPT_SPEC_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_CITATIONS_FIELD_NUMBER: _ClassVar[int]
        ANSWER_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        IGNORE_ADVERSARIAL_QUERY_FIELD_NUMBER: _ClassVar[int]
        IGNORE_NON_ANSWER_SEEKING_QUERY_FIELD_NUMBER: _ClassVar[int]
        IGNORE_LOW_RELEVANT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        IGNORE_JAIL_BREAKING_QUERY_FIELD_NUMBER: _ClassVar[int]
        model_spec: AnswerQueryRequest.AnswerGenerationSpec.ModelSpec
        prompt_spec: AnswerQueryRequest.AnswerGenerationSpec.PromptSpec
        include_citations: bool
        answer_language_code: str
        ignore_adversarial_query: bool
        ignore_non_answer_seeking_query: bool
        ignore_low_relevant_content: bool
        ignore_jail_breaking_query: bool
        def __init__(self, model_spec: _Optional[_Union[AnswerQueryRequest.AnswerGenerationSpec.ModelSpec, _Mapping]] = ..., prompt_spec: _Optional[_Union[AnswerQueryRequest.AnswerGenerationSpec.PromptSpec, _Mapping]] = ..., include_citations: bool = ..., answer_language_code: _Optional[str] = ..., ignore_adversarial_query: bool = ..., ignore_non_answer_seeking_query: bool = ..., ignore_low_relevant_content: bool = ..., ignore_jail_breaking_query: bool = ...) -> None: ...
    class SearchSpec(_message.Message):
        __slots__ = ("search_params", "search_result_list")
        class SearchParams(_message.Message):
            __slots__ = ("max_return_results", "filter", "boost_spec", "order_by", "search_result_mode", "data_store_specs", "natural_language_query_understanding_spec")
            MAX_RETURN_RESULTS_FIELD_NUMBER: _ClassVar[int]
            FILTER_FIELD_NUMBER: _ClassVar[int]
            BOOST_SPEC_FIELD_NUMBER: _ClassVar[int]
            ORDER_BY_FIELD_NUMBER: _ClassVar[int]
            SEARCH_RESULT_MODE_FIELD_NUMBER: _ClassVar[int]
            DATA_STORE_SPECS_FIELD_NUMBER: _ClassVar[int]
            NATURAL_LANGUAGE_QUERY_UNDERSTANDING_SPEC_FIELD_NUMBER: _ClassVar[int]
            max_return_results: int
            filter: str
            boost_spec: _search_service_pb2.SearchRequest.BoostSpec
            order_by: str
            search_result_mode: _search_service_pb2.SearchRequest.ContentSearchSpec.SearchResultMode
            data_store_specs: _containers.RepeatedCompositeFieldContainer[_search_service_pb2.SearchRequest.DataStoreSpec]
            natural_language_query_understanding_spec: _search_service_pb2.SearchRequest.NaturalLanguageQueryUnderstandingSpec
            def __init__(self, max_return_results: _Optional[int] = ..., filter: _Optional[str] = ..., boost_spec: _Optional[_Union[_search_service_pb2.SearchRequest.BoostSpec, _Mapping]] = ..., order_by: _Optional[str] = ..., search_result_mode: _Optional[_Union[_search_service_pb2.SearchRequest.ContentSearchSpec.SearchResultMode, str]] = ..., data_store_specs: _Optional[_Iterable[_Union[_search_service_pb2.SearchRequest.DataStoreSpec, _Mapping]]] = ..., natural_language_query_understanding_spec: _Optional[_Union[_search_service_pb2.SearchRequest.NaturalLanguageQueryUnderstandingSpec, _Mapping]] = ...) -> None: ...
        class SearchResultList(_message.Message):
            __slots__ = ("search_results",)
            class SearchResult(_message.Message):
                __slots__ = ("unstructured_document_info", "chunk_info")
                class UnstructuredDocumentInfo(_message.Message):
                    __slots__ = ("document", "uri", "title", "document_contexts", "extractive_segments", "extractive_answers")
                    class DocumentContext(_message.Message):
                        __slots__ = ("page_identifier", "content")
                        PAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                        CONTENT_FIELD_NUMBER: _ClassVar[int]
                        page_identifier: str
                        content: str
                        def __init__(self, page_identifier: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
                    class ExtractiveSegment(_message.Message):
                        __slots__ = ("page_identifier", "content")
                        PAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                        CONTENT_FIELD_NUMBER: _ClassVar[int]
                        page_identifier: str
                        content: str
                        def __init__(self, page_identifier: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
                    class ExtractiveAnswer(_message.Message):
                        __slots__ = ("page_identifier", "content")
                        PAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                        CONTENT_FIELD_NUMBER: _ClassVar[int]
                        page_identifier: str
                        content: str
                        def __init__(self, page_identifier: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
                    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
                    URI_FIELD_NUMBER: _ClassVar[int]
                    TITLE_FIELD_NUMBER: _ClassVar[int]
                    DOCUMENT_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
                    EXTRACTIVE_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
                    EXTRACTIVE_ANSWERS_FIELD_NUMBER: _ClassVar[int]
                    document: str
                    uri: str
                    title: str
                    document_contexts: _containers.RepeatedCompositeFieldContainer[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.DocumentContext]
                    extractive_segments: _containers.RepeatedCompositeFieldContainer[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveSegment]
                    extractive_answers: _containers.RepeatedCompositeFieldContainer[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveAnswer]
                    def __init__(self, document: _Optional[str] = ..., uri: _Optional[str] = ..., title: _Optional[str] = ..., document_contexts: _Optional[_Iterable[_Union[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.DocumentContext, _Mapping]]] = ..., extractive_segments: _Optional[_Iterable[_Union[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveSegment, _Mapping]]] = ..., extractive_answers: _Optional[_Iterable[_Union[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveAnswer, _Mapping]]] = ...) -> None: ...
                class ChunkInfo(_message.Message):
                    __slots__ = ("chunk", "content", "document_metadata")
                    class DocumentMetadata(_message.Message):
                        __slots__ = ("uri", "title")
                        URI_FIELD_NUMBER: _ClassVar[int]
                        TITLE_FIELD_NUMBER: _ClassVar[int]
                        uri: str
                        title: str
                        def __init__(self, uri: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
                    CHUNK_FIELD_NUMBER: _ClassVar[int]
                    CONTENT_FIELD_NUMBER: _ClassVar[int]
                    DOCUMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
                    chunk: str
                    content: str
                    document_metadata: AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo.DocumentMetadata
                    def __init__(self, chunk: _Optional[str] = ..., content: _Optional[str] = ..., document_metadata: _Optional[_Union[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo.DocumentMetadata, _Mapping]] = ...) -> None: ...
                UNSTRUCTURED_DOCUMENT_INFO_FIELD_NUMBER: _ClassVar[int]
                CHUNK_INFO_FIELD_NUMBER: _ClassVar[int]
                unstructured_document_info: AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo
                chunk_info: AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo
                def __init__(self, unstructured_document_info: _Optional[_Union[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo, _Mapping]] = ..., chunk_info: _Optional[_Union[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo, _Mapping]] = ...) -> None: ...
            SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
            search_results: _containers.RepeatedCompositeFieldContainer[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult]
            def __init__(self, search_results: _Optional[_Iterable[_Union[AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult, _Mapping]]] = ...) -> None: ...
        SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
        SEARCH_RESULT_LIST_FIELD_NUMBER: _ClassVar[int]
        search_params: AnswerQueryRequest.SearchSpec.SearchParams
        search_result_list: AnswerQueryRequest.SearchSpec.SearchResultList
        def __init__(self, search_params: _Optional[_Union[AnswerQueryRequest.SearchSpec.SearchParams, _Mapping]] = ..., search_result_list: _Optional[_Union[AnswerQueryRequest.SearchSpec.SearchResultList, _Mapping]] = ...) -> None: ...
    class QueryUnderstandingSpec(_message.Message):
        __slots__ = ("query_classification_spec", "query_rephraser_spec")
        class QueryClassificationSpec(_message.Message):
            __slots__ = ("types",)
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNSPECIFIED: _ClassVar[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type]
                ADVERSARIAL_QUERY: _ClassVar[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type]
                NON_ANSWER_SEEKING_QUERY: _ClassVar[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type]
                JAIL_BREAKING_QUERY: _ClassVar[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type]
                NON_ANSWER_SEEKING_QUERY_V2: _ClassVar[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type]
            TYPE_UNSPECIFIED: AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type
            ADVERSARIAL_QUERY: AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type
            NON_ANSWER_SEEKING_QUERY: AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type
            JAIL_BREAKING_QUERY: AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type
            NON_ANSWER_SEEKING_QUERY_V2: AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type
            TYPES_FIELD_NUMBER: _ClassVar[int]
            types: _containers.RepeatedScalarFieldContainer[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type]
            def __init__(self, types: _Optional[_Iterable[_Union[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type, str]]] = ...) -> None: ...
        class QueryRephraserSpec(_message.Message):
            __slots__ = ("disable", "max_rephrase_steps")
            DISABLE_FIELD_NUMBER: _ClassVar[int]
            MAX_REPHRASE_STEPS_FIELD_NUMBER: _ClassVar[int]
            disable: bool
            max_rephrase_steps: int
            def __init__(self, disable: bool = ..., max_rephrase_steps: _Optional[int] = ...) -> None: ...
        QUERY_CLASSIFICATION_SPEC_FIELD_NUMBER: _ClassVar[int]
        QUERY_REPHRASER_SPEC_FIELD_NUMBER: _ClassVar[int]
        query_classification_spec: AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec
        query_rephraser_spec: AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec
        def __init__(self, query_classification_spec: _Optional[_Union[AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec, _Mapping]] = ..., query_rephraser_spec: _Optional[_Union[AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec, _Mapping]] = ...) -> None: ...
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SAFETY_SPEC_FIELD_NUMBER: _ClassVar[int]
    RELATED_QUESTIONS_SPEC_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_SPEC_FIELD_NUMBER: _ClassVar[int]
    ANSWER_GENERATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SPEC_FIELD_NUMBER: _ClassVar[int]
    QUERY_UNDERSTANDING_SPEC_FIELD_NUMBER: _ClassVar[int]
    ASYNCHRONOUS_MODE_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    serving_config: str
    query: _session_pb2.Query
    session: str
    safety_spec: AnswerQueryRequest.SafetySpec
    related_questions_spec: AnswerQueryRequest.RelatedQuestionsSpec
    grounding_spec: AnswerQueryRequest.GroundingSpec
    answer_generation_spec: AnswerQueryRequest.AnswerGenerationSpec
    search_spec: AnswerQueryRequest.SearchSpec
    query_understanding_spec: AnswerQueryRequest.QueryUnderstandingSpec
    asynchronous_mode: bool
    user_pseudo_id: str
    user_labels: _containers.ScalarMap[str, str]
    def __init__(self, serving_config: _Optional[str] = ..., query: _Optional[_Union[_session_pb2.Query, _Mapping]] = ..., session: _Optional[str] = ..., safety_spec: _Optional[_Union[AnswerQueryRequest.SafetySpec, _Mapping]] = ..., related_questions_spec: _Optional[_Union[AnswerQueryRequest.RelatedQuestionsSpec, _Mapping]] = ..., grounding_spec: _Optional[_Union[AnswerQueryRequest.GroundingSpec, _Mapping]] = ..., answer_generation_spec: _Optional[_Union[AnswerQueryRequest.AnswerGenerationSpec, _Mapping]] = ..., search_spec: _Optional[_Union[AnswerQueryRequest.SearchSpec, _Mapping]] = ..., query_understanding_spec: _Optional[_Union[AnswerQueryRequest.QueryUnderstandingSpec, _Mapping]] = ..., asynchronous_mode: bool = ..., user_pseudo_id: _Optional[str] = ..., user_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AnswerQueryResponse(_message.Message):
    __slots__ = ("answer", "session", "answer_query_token")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    ANSWER_QUERY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    answer: _answer_pb2.Answer
    session: _session_pb2.Session
    answer_query_token: str
    def __init__(self, answer: _Optional[_Union[_answer_pb2.Answer, _Mapping]] = ..., session: _Optional[_Union[_session_pb2.Session, _Mapping]] = ..., answer_query_token: _Optional[str] = ...) -> None: ...

class GetAnswerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("parent", "session")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    session: _session_pb2.Session
    def __init__(self, parent: _Optional[str] = ..., session: _Optional[_Union[_session_pb2.Session, _Mapping]] = ...) -> None: ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ("session", "update_mask")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    session: _session_pb2.Session
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, session: _Optional[_Union[_session_pb2.Session, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
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

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions", "next_page_token")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_session_pb2.Session]
    next_page_token: str
    def __init__(self, sessions: _Optional[_Iterable[_Union[_session_pb2.Session, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
