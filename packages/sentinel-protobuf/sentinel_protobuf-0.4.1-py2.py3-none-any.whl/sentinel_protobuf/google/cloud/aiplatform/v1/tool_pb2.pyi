from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import openapi_pb2 as _openapi_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tool(_message.Message):
    __slots__ = ("function_declarations", "retrieval", "google_search_retrieval")
    FUNCTION_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SEARCH_RETRIEVAL_FIELD_NUMBER: _ClassVar[int]
    function_declarations: _containers.RepeatedCompositeFieldContainer[FunctionDeclaration]
    retrieval: Retrieval
    google_search_retrieval: GoogleSearchRetrieval
    def __init__(self, function_declarations: _Optional[_Iterable[_Union[FunctionDeclaration, _Mapping]]] = ..., retrieval: _Optional[_Union[Retrieval, _Mapping]] = ..., google_search_retrieval: _Optional[_Union[GoogleSearchRetrieval, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("rag_resources", "similarity_top_k", "vector_distance_threshold", "rag_retrieval_config")
    class RagResource(_message.Message):
        __slots__ = ("rag_corpus", "rag_file_ids")
        RAG_CORPUS_FIELD_NUMBER: _ClassVar[int]
        RAG_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
        rag_corpus: str
        rag_file_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, rag_corpus: _Optional[str] = ..., rag_file_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    RAG_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_TOP_K_FIELD_NUMBER: _ClassVar[int]
    VECTOR_DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RAG_RETRIEVAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_resources: _containers.RepeatedCompositeFieldContainer[VertexRagStore.RagResource]
    similarity_top_k: int
    vector_distance_threshold: float
    rag_retrieval_config: RagRetrievalConfig
    def __init__(self, rag_resources: _Optional[_Iterable[_Union[VertexRagStore.RagResource, _Mapping]]] = ..., similarity_top_k: _Optional[int] = ..., vector_distance_threshold: _Optional[float] = ..., rag_retrieval_config: _Optional[_Union[RagRetrievalConfig, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("top_k", "filter")
    class Filter(_message.Message):
        __slots__ = ("vector_distance_threshold", "vector_similarity_threshold", "metadata_filter")
        VECTOR_DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        VECTOR_SIMILARITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        METADATA_FILTER_FIELD_NUMBER: _ClassVar[int]
        vector_distance_threshold: float
        vector_similarity_threshold: float
        metadata_filter: str
        def __init__(self, vector_distance_threshold: _Optional[float] = ..., vector_similarity_threshold: _Optional[float] = ..., metadata_filter: _Optional[str] = ...) -> None: ...
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    top_k: int
    filter: RagRetrievalConfig.Filter
    def __init__(self, top_k: _Optional[int] = ..., filter: _Optional[_Union[RagRetrievalConfig.Filter, _Mapping]] = ...) -> None: ...
