from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Answer(_message.Message):
    __slots__ = ("name", "state", "answer_text", "citations", "references", "related_questions", "steps", "query_understanding_info", "answer_skipped_reasons", "create_time", "complete_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Answer.State]
        IN_PROGRESS: _ClassVar[Answer.State]
        FAILED: _ClassVar[Answer.State]
        SUCCEEDED: _ClassVar[Answer.State]
    STATE_UNSPECIFIED: Answer.State
    IN_PROGRESS: Answer.State
    FAILED: Answer.State
    SUCCEEDED: Answer.State
    class AnswerSkippedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANSWER_SKIPPED_REASON_UNSPECIFIED: _ClassVar[Answer.AnswerSkippedReason]
        ADVERSARIAL_QUERY_IGNORED: _ClassVar[Answer.AnswerSkippedReason]
        NON_ANSWER_SEEKING_QUERY_IGNORED: _ClassVar[Answer.AnswerSkippedReason]
        OUT_OF_DOMAIN_QUERY_IGNORED: _ClassVar[Answer.AnswerSkippedReason]
        POTENTIAL_POLICY_VIOLATION: _ClassVar[Answer.AnswerSkippedReason]
        NO_RELEVANT_CONTENT: _ClassVar[Answer.AnswerSkippedReason]
        JAIL_BREAKING_QUERY_IGNORED: _ClassVar[Answer.AnswerSkippedReason]
        CUSTOMER_POLICY_VIOLATION: _ClassVar[Answer.AnswerSkippedReason]
        NON_ANSWER_SEEKING_QUERY_IGNORED_V2: _ClassVar[Answer.AnswerSkippedReason]
        LOW_GROUNDED_ANSWER: _ClassVar[Answer.AnswerSkippedReason]
    ANSWER_SKIPPED_REASON_UNSPECIFIED: Answer.AnswerSkippedReason
    ADVERSARIAL_QUERY_IGNORED: Answer.AnswerSkippedReason
    NON_ANSWER_SEEKING_QUERY_IGNORED: Answer.AnswerSkippedReason
    OUT_OF_DOMAIN_QUERY_IGNORED: Answer.AnswerSkippedReason
    POTENTIAL_POLICY_VIOLATION: Answer.AnswerSkippedReason
    NO_RELEVANT_CONTENT: Answer.AnswerSkippedReason
    JAIL_BREAKING_QUERY_IGNORED: Answer.AnswerSkippedReason
    CUSTOMER_POLICY_VIOLATION: Answer.AnswerSkippedReason
    NON_ANSWER_SEEKING_QUERY_IGNORED_V2: Answer.AnswerSkippedReason
    LOW_GROUNDED_ANSWER: Answer.AnswerSkippedReason
    class Citation(_message.Message):
        __slots__ = ("start_index", "end_index", "sources")
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        END_INDEX_FIELD_NUMBER: _ClassVar[int]
        SOURCES_FIELD_NUMBER: _ClassVar[int]
        start_index: int
        end_index: int
        sources: _containers.RepeatedCompositeFieldContainer[Answer.CitationSource]
        def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ..., sources: _Optional[_Iterable[_Union[Answer.CitationSource, _Mapping]]] = ...) -> None: ...
    class CitationSource(_message.Message):
        __slots__ = ("reference_id",)
        REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
        reference_id: str
        def __init__(self, reference_id: _Optional[str] = ...) -> None: ...
    class Reference(_message.Message):
        __slots__ = ("unstructured_document_info", "chunk_info", "structured_document_info")
        class UnstructuredDocumentInfo(_message.Message):
            __slots__ = ("document", "uri", "title", "chunk_contents", "struct_data")
            class ChunkContent(_message.Message):
                __slots__ = ("content", "page_identifier", "relevance_score")
                CONTENT_FIELD_NUMBER: _ClassVar[int]
                PAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
                content: str
                page_identifier: str
                relevance_score: float
                def __init__(self, content: _Optional[str] = ..., page_identifier: _Optional[str] = ..., relevance_score: _Optional[float] = ...) -> None: ...
            DOCUMENT_FIELD_NUMBER: _ClassVar[int]
            URI_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            CHUNK_CONTENTS_FIELD_NUMBER: _ClassVar[int]
            STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
            document: str
            uri: str
            title: str
            chunk_contents: _containers.RepeatedCompositeFieldContainer[Answer.Reference.UnstructuredDocumentInfo.ChunkContent]
            struct_data: _struct_pb2.Struct
            def __init__(self, document: _Optional[str] = ..., uri: _Optional[str] = ..., title: _Optional[str] = ..., chunk_contents: _Optional[_Iterable[_Union[Answer.Reference.UnstructuredDocumentInfo.ChunkContent, _Mapping]]] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
        class ChunkInfo(_message.Message):
            __slots__ = ("chunk", "content", "relevance_score", "document_metadata")
            class DocumentMetadata(_message.Message):
                __slots__ = ("document", "uri", "title", "page_identifier", "struct_data")
                DOCUMENT_FIELD_NUMBER: _ClassVar[int]
                URI_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                PAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
                document: str
                uri: str
                title: str
                page_identifier: str
                struct_data: _struct_pb2.Struct
                def __init__(self, document: _Optional[str] = ..., uri: _Optional[str] = ..., title: _Optional[str] = ..., page_identifier: _Optional[str] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
            CHUNK_FIELD_NUMBER: _ClassVar[int]
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
            DOCUMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
            chunk: str
            content: str
            relevance_score: float
            document_metadata: Answer.Reference.ChunkInfo.DocumentMetadata
            def __init__(self, chunk: _Optional[str] = ..., content: _Optional[str] = ..., relevance_score: _Optional[float] = ..., document_metadata: _Optional[_Union[Answer.Reference.ChunkInfo.DocumentMetadata, _Mapping]] = ...) -> None: ...
        class StructuredDocumentInfo(_message.Message):
            __slots__ = ("document", "struct_data")
            DOCUMENT_FIELD_NUMBER: _ClassVar[int]
            STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
            document: str
            struct_data: _struct_pb2.Struct
            def __init__(self, document: _Optional[str] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
        UNSTRUCTURED_DOCUMENT_INFO_FIELD_NUMBER: _ClassVar[int]
        CHUNK_INFO_FIELD_NUMBER: _ClassVar[int]
        STRUCTURED_DOCUMENT_INFO_FIELD_NUMBER: _ClassVar[int]
        unstructured_document_info: Answer.Reference.UnstructuredDocumentInfo
        chunk_info: Answer.Reference.ChunkInfo
        structured_document_info: Answer.Reference.StructuredDocumentInfo
        def __init__(self, unstructured_document_info: _Optional[_Union[Answer.Reference.UnstructuredDocumentInfo, _Mapping]] = ..., chunk_info: _Optional[_Union[Answer.Reference.ChunkInfo, _Mapping]] = ..., structured_document_info: _Optional[_Union[Answer.Reference.StructuredDocumentInfo, _Mapping]] = ...) -> None: ...
    class Step(_message.Message):
        __slots__ = ("state", "description", "thought", "actions")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Answer.Step.State]
            IN_PROGRESS: _ClassVar[Answer.Step.State]
            FAILED: _ClassVar[Answer.Step.State]
            SUCCEEDED: _ClassVar[Answer.Step.State]
        STATE_UNSPECIFIED: Answer.Step.State
        IN_PROGRESS: Answer.Step.State
        FAILED: Answer.Step.State
        SUCCEEDED: Answer.Step.State
        class Action(_message.Message):
            __slots__ = ("search_action", "observation")
            class SearchAction(_message.Message):
                __slots__ = ("query",)
                QUERY_FIELD_NUMBER: _ClassVar[int]
                query: str
                def __init__(self, query: _Optional[str] = ...) -> None: ...
            class Observation(_message.Message):
                __slots__ = ("search_results",)
                class SearchResult(_message.Message):
                    __slots__ = ("document", "uri", "title", "snippet_info", "chunk_info", "struct_data")
                    class SnippetInfo(_message.Message):
                        __slots__ = ("snippet", "snippet_status")
                        SNIPPET_FIELD_NUMBER: _ClassVar[int]
                        SNIPPET_STATUS_FIELD_NUMBER: _ClassVar[int]
                        snippet: str
                        snippet_status: str
                        def __init__(self, snippet: _Optional[str] = ..., snippet_status: _Optional[str] = ...) -> None: ...
                    class ChunkInfo(_message.Message):
                        __slots__ = ("chunk", "content", "relevance_score")
                        CHUNK_FIELD_NUMBER: _ClassVar[int]
                        CONTENT_FIELD_NUMBER: _ClassVar[int]
                        RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
                        chunk: str
                        content: str
                        relevance_score: float
                        def __init__(self, chunk: _Optional[str] = ..., content: _Optional[str] = ..., relevance_score: _Optional[float] = ...) -> None: ...
                    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
                    URI_FIELD_NUMBER: _ClassVar[int]
                    TITLE_FIELD_NUMBER: _ClassVar[int]
                    SNIPPET_INFO_FIELD_NUMBER: _ClassVar[int]
                    CHUNK_INFO_FIELD_NUMBER: _ClassVar[int]
                    STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
                    document: str
                    uri: str
                    title: str
                    snippet_info: _containers.RepeatedCompositeFieldContainer[Answer.Step.Action.Observation.SearchResult.SnippetInfo]
                    chunk_info: _containers.RepeatedCompositeFieldContainer[Answer.Step.Action.Observation.SearchResult.ChunkInfo]
                    struct_data: _struct_pb2.Struct
                    def __init__(self, document: _Optional[str] = ..., uri: _Optional[str] = ..., title: _Optional[str] = ..., snippet_info: _Optional[_Iterable[_Union[Answer.Step.Action.Observation.SearchResult.SnippetInfo, _Mapping]]] = ..., chunk_info: _Optional[_Iterable[_Union[Answer.Step.Action.Observation.SearchResult.ChunkInfo, _Mapping]]] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
                SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
                search_results: _containers.RepeatedCompositeFieldContainer[Answer.Step.Action.Observation.SearchResult]
                def __init__(self, search_results: _Optional[_Iterable[_Union[Answer.Step.Action.Observation.SearchResult, _Mapping]]] = ...) -> None: ...
            SEARCH_ACTION_FIELD_NUMBER: _ClassVar[int]
            OBSERVATION_FIELD_NUMBER: _ClassVar[int]
            search_action: Answer.Step.Action.SearchAction
            observation: Answer.Step.Action.Observation
            def __init__(self, search_action: _Optional[_Union[Answer.Step.Action.SearchAction, _Mapping]] = ..., observation: _Optional[_Union[Answer.Step.Action.Observation, _Mapping]] = ...) -> None: ...
        STATE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        THOUGHT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        state: Answer.Step.State
        description: str
        thought: str
        actions: _containers.RepeatedCompositeFieldContainer[Answer.Step.Action]
        def __init__(self, state: _Optional[_Union[Answer.Step.State, str]] = ..., description: _Optional[str] = ..., thought: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[Answer.Step.Action, _Mapping]]] = ...) -> None: ...
    class QueryUnderstandingInfo(_message.Message):
        __slots__ = ("query_classification_info",)
        class QueryClassificationInfo(_message.Message):
            __slots__ = ("type", "positive")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNSPECIFIED: _ClassVar[Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type]
                ADVERSARIAL_QUERY: _ClassVar[Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type]
                NON_ANSWER_SEEKING_QUERY: _ClassVar[Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type]
                JAIL_BREAKING_QUERY: _ClassVar[Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type]
                NON_ANSWER_SEEKING_QUERY_V2: _ClassVar[Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type]
            TYPE_UNSPECIFIED: Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type
            ADVERSARIAL_QUERY: Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type
            NON_ANSWER_SEEKING_QUERY: Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type
            JAIL_BREAKING_QUERY: Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type
            NON_ANSWER_SEEKING_QUERY_V2: Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            POSITIVE_FIELD_NUMBER: _ClassVar[int]
            type: Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type
            positive: bool
            def __init__(self, type: _Optional[_Union[Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type, str]] = ..., positive: bool = ...) -> None: ...
        QUERY_CLASSIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        query_classification_info: _containers.RepeatedCompositeFieldContainer[Answer.QueryUnderstandingInfo.QueryClassificationInfo]
        def __init__(self, query_classification_info: _Optional[_Iterable[_Union[Answer.QueryUnderstandingInfo.QueryClassificationInfo, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ANSWER_TEXT_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    RELATED_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    QUERY_UNDERSTANDING_INFO_FIELD_NUMBER: _ClassVar[int]
    ANSWER_SKIPPED_REASONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Answer.State
    answer_text: str
    citations: _containers.RepeatedCompositeFieldContainer[Answer.Citation]
    references: _containers.RepeatedCompositeFieldContainer[Answer.Reference]
    related_questions: _containers.RepeatedScalarFieldContainer[str]
    steps: _containers.RepeatedCompositeFieldContainer[Answer.Step]
    query_understanding_info: Answer.QueryUnderstandingInfo
    answer_skipped_reasons: _containers.RepeatedScalarFieldContainer[Answer.AnswerSkippedReason]
    create_time: _timestamp_pb2.Timestamp
    complete_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Answer.State, str]] = ..., answer_text: _Optional[str] = ..., citations: _Optional[_Iterable[_Union[Answer.Citation, _Mapping]]] = ..., references: _Optional[_Iterable[_Union[Answer.Reference, _Mapping]]] = ..., related_questions: _Optional[_Iterable[str]] = ..., steps: _Optional[_Iterable[_Union[Answer.Step, _Mapping]]] = ..., query_understanding_info: _Optional[_Union[Answer.QueryUnderstandingInfo, _Mapping]] = ..., answer_skipped_reasons: _Optional[_Iterable[_Union[Answer.AnswerSkippedReason, str]]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
