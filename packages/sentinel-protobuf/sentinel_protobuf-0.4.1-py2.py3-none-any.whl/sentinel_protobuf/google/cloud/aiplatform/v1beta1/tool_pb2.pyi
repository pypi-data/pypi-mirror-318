from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import openapi_pb2 as _openapi_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tool(_message.Message):
    __slots__ = ("function_declarations", "retrieval", "google_search", "google_search_retrieval", "code_execution")
    class GoogleSearch(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CodeExecution(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    FUNCTION_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SEARCH_RETRIEVAL_FIELD_NUMBER: _ClassVar[int]
    CODE_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    function_declarations: _containers.RepeatedCompositeFieldContainer[FunctionDeclaration]
    retrieval: Retrieval
    google_search: Tool.GoogleSearch
    google_search_retrieval: GoogleSearchRetrieval
    code_execution: Tool.CodeExecution
    def __init__(self, function_declarations: _Optional[_Iterable[_Union[FunctionDeclaration, _Mapping]]] = ..., retrieval: _Optional[_Union[Retrieval, _Mapping]] = ..., google_search: _Optional[_Union[Tool.GoogleSearch, _Mapping]] = ..., google_search_retrieval: _Optional[_Union[GoogleSearchRetrieval, _Mapping]] = ..., code_execution: _Optional[_Union[Tool.CodeExecution, _Mapping]] = ...) -> None: ...

class ToolUseExample(_message.Message):
    __slots__ = ("extension_operation", "function_name", "display_name", "query", "request_params", "response_params", "response_summary")
    class ExtensionOperation(_message.Message):
        __slots__ = ("extension", "operation_id")
        EXTENSION_FIELD_NUMBER: _ClassVar[int]
        OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
        extension: str
        operation_id: str
        def __init__(self, extension: _Optional[str] = ..., operation_id: _Optional[str] = ...) -> None: ...
    EXTENSION_OPERATION_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    extension_operation: ToolUseExample.ExtensionOperation
    function_name: str
    display_name: str
    query: str
    request_params: _struct_pb2.Struct
    response_params: _struct_pb2.Struct
    response_summary: str
    def __init__(self, extension_operation: _Optional[_Union[ToolUseExample.ExtensionOperation, _Mapping]] = ..., function_name: _Optional[str] = ..., display_name: _Optional[str] = ..., query: _Optional[str] = ..., request_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., response_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., response_summary: _Optional[str] = ...) -> None: ...

class FunctionDeclaration(_message.Message):
    __slots__ = ("name", "description", "parameters", "response")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: _openapi_pb2.Schema
    response: _openapi_pb2.Schema
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Union[_openapi_pb2.Schema, _Mapping]] = ..., response: _Optional[_Union[_openapi_pb2.Schema, _Mapping]] = ...) -> None: ...

class FunctionCall(_message.Message):
    __slots__ = ("name", "args")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    args: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., args: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class FunctionResponse(_message.Message):
    __slots__ = ("name", "response")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    name: str
    response: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., response: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ExecutableCode(_message.Message):
    __slots__ = ("language", "code")
    class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LANGUAGE_UNSPECIFIED: _ClassVar[ExecutableCode.Language]
        PYTHON: _ClassVar[ExecutableCode.Language]
    LANGUAGE_UNSPECIFIED: ExecutableCode.Language
    PYTHON: ExecutableCode.Language
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    language: ExecutableCode.Language
    code: str
    def __init__(self, language: _Optional[_Union[ExecutableCode.Language, str]] = ..., code: _Optional[str] = ...) -> None: ...

class CodeExecutionResult(_message.Message):
    __slots__ = ("outcome", "output")
    class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTCOME_UNSPECIFIED: _ClassVar[CodeExecutionResult.Outcome]
        OUTCOME_OK: _ClassVar[CodeExecutionResult.Outcome]
        OUTCOME_FAILED: _ClassVar[CodeExecutionResult.Outcome]
        OUTCOME_DEADLINE_EXCEEDED: _ClassVar[CodeExecutionResult.Outcome]
    OUTCOME_UNSPECIFIED: CodeExecutionResult.Outcome
    OUTCOME_OK: CodeExecutionResult.Outcome
    OUTCOME_FAILED: CodeExecutionResult.Outcome
    OUTCOME_DEADLINE_EXCEEDED: CodeExecutionResult.Outcome
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    outcome: CodeExecutionResult.Outcome
    output: str
    def __init__(self, outcome: _Optional[_Union[CodeExecutionResult.Outcome, str]] = ..., output: _Optional[str] = ...) -> None: ...

class Retrieval(_message.Message):
    __slots__ = ("vertex_ai_search", "vertex_rag_store", "disable_attribution")
    VERTEX_AI_SEARCH_FIELD_NUMBER: _ClassVar[int]
    VERTEX_RAG_STORE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    vertex_ai_search: VertexAISearch
    vertex_rag_store: VertexRagStore
    disable_attribution: bool
    def __init__(self, vertex_ai_search: _Optional[_Union[VertexAISearch, _Mapping]] = ..., vertex_rag_store: _Optional[_Union[VertexRagStore, _Mapping]] = ..., disable_attribution: bool = ...) -> None: ...

class VertexRagStore(_message.Message):
    __slots__ = ("rag_corpora", "rag_resources", "similarity_top_k", "vector_distance_threshold", "rag_retrieval_config")
    class RagResource(_message.Message):
        __slots__ = ("rag_corpus", "rag_file_ids")
        RAG_CORPUS_FIELD_NUMBER: _ClassVar[int]
        RAG_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
        rag_corpus: str
        rag_file_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, rag_corpus: _Optional[str] = ..., rag_file_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    RAG_CORPORA_FIELD_NUMBER: _ClassVar[int]
    RAG_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_TOP_K_FIELD_NUMBER: _ClassVar[int]
    VECTOR_DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RAG_RETRIEVAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_corpora: _containers.RepeatedScalarFieldContainer[str]
    rag_resources: _containers.RepeatedCompositeFieldContainer[VertexRagStore.RagResource]
    similarity_top_k: int
    vector_distance_threshold: float
    rag_retrieval_config: RagRetrievalConfig
    def __init__(self, rag_corpora: _Optional[_Iterable[str]] = ..., rag_resources: _Optional[_Iterable[_Union[VertexRagStore.RagResource, _Mapping]]] = ..., similarity_top_k: _Optional[int] = ..., vector_distance_threshold: _Optional[float] = ..., rag_retrieval_config: _Optional[_Union[RagRetrievalConfig, _Mapping]] = ...) -> None: ...

class VertexAISearch(_message.Message):
    __slots__ = ("datastore",)
    DATASTORE_FIELD_NUMBER: _ClassVar[int]
    datastore: str
    def __init__(self, datastore: _Optional[str] = ...) -> None: ...

class GoogleSearchRetrieval(_message.Message):
    __slots__ = ("dynamic_retrieval_config",)
    DYNAMIC_RETRIEVAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    dynamic_retrieval_config: DynamicRetrievalConfig
    def __init__(self, dynamic_retrieval_config: _Optional[_Union[DynamicRetrievalConfig, _Mapping]] = ...) -> None: ...

class DynamicRetrievalConfig(_message.Message):
    __slots__ = ("mode", "dynamic_threshold")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[DynamicRetrievalConfig.Mode]
        MODE_DYNAMIC: _ClassVar[DynamicRetrievalConfig.Mode]
    MODE_UNSPECIFIED: DynamicRetrievalConfig.Mode
    MODE_DYNAMIC: DynamicRetrievalConfig.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    mode: DynamicRetrievalConfig.Mode
    dynamic_threshold: float
    def __init__(self, mode: _Optional[_Union[DynamicRetrievalConfig.Mode, str]] = ..., dynamic_threshold: _Optional[float] = ...) -> None: ...

class ToolConfig(_message.Message):
    __slots__ = ("function_calling_config",)
    FUNCTION_CALLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    function_calling_config: FunctionCallingConfig
    def __init__(self, function_calling_config: _Optional[_Union[FunctionCallingConfig, _Mapping]] = ...) -> None: ...

class FunctionCallingConfig(_message.Message):
    __slots__ = ("mode", "allowed_function_names")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[FunctionCallingConfig.Mode]
        AUTO: _ClassVar[FunctionCallingConfig.Mode]
        ANY: _ClassVar[FunctionCallingConfig.Mode]
        NONE: _ClassVar[FunctionCallingConfig.Mode]
    MODE_UNSPECIFIED: FunctionCallingConfig.Mode
    AUTO: FunctionCallingConfig.Mode
    ANY: FunctionCallingConfig.Mode
    NONE: FunctionCallingConfig.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FUNCTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    mode: FunctionCallingConfig.Mode
    allowed_function_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mode: _Optional[_Union[FunctionCallingConfig.Mode, str]] = ..., allowed_function_names: _Optional[_Iterable[str]] = ...) -> None: ...

class RagRetrievalConfig(_message.Message):
    __slots__ = ("top_k", "hybrid_search", "filter", "ranking")
    class HybridSearch(_message.Message):
        __slots__ = ("alpha",)
        ALPHA_FIELD_NUMBER: _ClassVar[int]
        alpha: float
        def __init__(self, alpha: _Optional[float] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ("vector_distance_threshold", "vector_similarity_threshold", "metadata_filter")
        VECTOR_DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        VECTOR_SIMILARITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        METADATA_FILTER_FIELD_NUMBER: _ClassVar[int]
        vector_distance_threshold: float
        vector_similarity_threshold: float
        metadata_filter: str
        def __init__(self, vector_distance_threshold: _Optional[float] = ..., vector_similarity_threshold: _Optional[float] = ..., metadata_filter: _Optional[str] = ...) -> None: ...
    class Ranking(_message.Message):
        __slots__ = ("rank_service", "llm_ranker")
        class RankService(_message.Message):
            __slots__ = ("model_name",)
            MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
            model_name: str
            def __init__(self, model_name: _Optional[str] = ...) -> None: ...
        class LlmRanker(_message.Message):
            __slots__ = ("model_name",)
            MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
            model_name: str
            def __init__(self, model_name: _Optional[str] = ...) -> None: ...
        RANK_SERVICE_FIELD_NUMBER: _ClassVar[int]
        LLM_RANKER_FIELD_NUMBER: _ClassVar[int]
        rank_service: RagRetrievalConfig.Ranking.RankService
        llm_ranker: RagRetrievalConfig.Ranking.LlmRanker
        def __init__(self, rank_service: _Optional[_Union[RagRetrievalConfig.Ranking.RankService, _Mapping]] = ..., llm_ranker: _Optional[_Union[RagRetrievalConfig.Ranking.LlmRanker, _Mapping]] = ...) -> None: ...
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    HYBRID_SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    RANKING_FIELD_NUMBER: _ClassVar[int]
    top_k: int
    hybrid_search: RagRetrievalConfig.HybridSearch
    filter: RagRetrievalConfig.Filter
    ranking: RagRetrievalConfig.Ranking
    def __init__(self, top_k: _Optional[int] = ..., hybrid_search: _Optional[_Union[RagRetrievalConfig.HybridSearch, _Mapping]] = ..., filter: _Optional[_Union[RagRetrievalConfig.Filter, _Mapping]] = ..., ranking: _Optional[_Union[RagRetrievalConfig.Ranking, _Mapping]] = ...) -> None: ...
