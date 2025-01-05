from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import common_pb2 as _common_pb2
from google.cloud.contentwarehouse.v1 import document_pb2 as _document_pb2
from google.cloud.contentwarehouse.v1 import document_service_request_pb2 as _document_service_request_pb2
from google.cloud.contentwarehouse.v1 import histogram_pb2 as _histogram_pb2
from google.cloud.contentwarehouse.v1 import rule_engine_pb2 as _rule_engine_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDocumentResponse(_message.Message):
    __slots__ = ("document", "rule_engine_output", "metadata", "long_running_operations")
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    RULE_ENGINE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LONG_RUNNING_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    rule_engine_output: _rule_engine_pb2.RuleEngineOutput
    metadata: _common_pb2.ResponseMetadata
    long_running_operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., rule_engine_output: _Optional[_Union[_rule_engine_pb2.RuleEngineOutput, _Mapping]] = ..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ..., long_running_operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]] = ...) -> None: ...

class UpdateDocumentResponse(_message.Message):
    __slots__ = ("document", "rule_engine_output", "metadata")
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    RULE_ENGINE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    rule_engine_output: _rule_engine_pb2.RuleEngineOutput
    metadata: _common_pb2.ResponseMetadata
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., rule_engine_output: _Optional[_Union[_rule_engine_pb2.RuleEngineOutput, _Mapping]] = ..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...

class QAResult(_message.Message):
    __slots__ = ("highlights", "confidence_score")
    class Highlight(_message.Message):
        __slots__ = ("start_index", "end_index")
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        END_INDEX_FIELD_NUMBER: _ClassVar[int]
        start_index: int
        end_index: int
        def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ...) -> None: ...
    HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    highlights: _containers.RepeatedCompositeFieldContainer[QAResult.Highlight]
    confidence_score: float
    def __init__(self, highlights: _Optional[_Iterable[_Union[QAResult.Highlight, _Mapping]]] = ..., confidence_score: _Optional[float] = ...) -> None: ...

class SearchDocumentsResponse(_message.Message):
    __slots__ = ("matching_documents", "next_page_token", "total_size", "metadata", "histogram_query_results", "question_answer")
    class MatchingDocument(_message.Message):
        __slots__ = ("document", "search_text_snippet", "qa_result", "matched_token_page_indices")
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        SEARCH_TEXT_SNIPPET_FIELD_NUMBER: _ClassVar[int]
        QA_RESULT_FIELD_NUMBER: _ClassVar[int]
        MATCHED_TOKEN_PAGE_INDICES_FIELD_NUMBER: _ClassVar[int]
        document: _document_pb2.Document
        search_text_snippet: str
        qa_result: QAResult
        matched_token_page_indices: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., search_text_snippet: _Optional[str] = ..., qa_result: _Optional[_Union[QAResult, _Mapping]] = ..., matched_token_page_indices: _Optional[_Iterable[int]] = ...) -> None: ...
    MATCHING_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWER_FIELD_NUMBER: _ClassVar[int]
    matching_documents: _containers.RepeatedCompositeFieldContainer[SearchDocumentsResponse.MatchingDocument]
    next_page_token: str
    total_size: int
    metadata: _common_pb2.ResponseMetadata
    histogram_query_results: _containers.RepeatedCompositeFieldContainer[_histogram_pb2.HistogramQueryResult]
    question_answer: str
    def __init__(self, matching_documents: _Optional[_Iterable[_Union[SearchDocumentsResponse.MatchingDocument, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ..., histogram_query_results: _Optional[_Iterable[_Union[_histogram_pb2.HistogramQueryResult, _Mapping]]] = ..., question_answer: _Optional[str] = ...) -> None: ...

class FetchAclResponse(_message.Message):
    __slots__ = ("policy", "metadata")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    policy: _policy_pb2.Policy
    metadata: _common_pb2.ResponseMetadata
    def __init__(self, policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...

class SetAclResponse(_message.Message):
    __slots__ = ("policy", "metadata")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    policy: _policy_pb2.Policy
    metadata: _common_pb2.ResponseMetadata
    def __init__(self, policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
