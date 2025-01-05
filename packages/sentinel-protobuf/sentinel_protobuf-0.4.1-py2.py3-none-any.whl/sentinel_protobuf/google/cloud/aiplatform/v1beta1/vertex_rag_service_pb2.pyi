from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import tool_pb2 as _tool_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RagQuery(_message.Message):
    __slots__ = ("text", "similarity_top_k", "ranking", "rag_retrieval_config")
    class Ranking(_message.Message):
        __slots__ = ("alpha",)
        ALPHA_FIELD_NUMBER: _ClassVar[int]
        alpha: float
        def __init__(self, alpha: _Optional[float] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_TOP_K_FIELD_NUMBER: _ClassVar[int]
    RANKING_FIELD_NUMBER: _ClassVar[int]
    RAG_RETRIEVAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    text: str
    similarity_top_k: int
    ranking: RagQuery.Ranking
    rag_retrieval_config: _tool_pb2.RagRetrievalConfig
    def __init__(self, text: _Optional[str] = ..., similarity_top_k: _Optional[int] = ..., ranking: _Optional[_Union[RagQuery.Ranking, _Mapping]] = ..., rag_retrieval_config: _Optional[_Union[_tool_pb2.RagRetrievalConfig, _Mapping]] = ...) -> None: ...

class RetrieveContextsRequest(_message.Message):
    __slots__ = ("vertex_rag_store", "parent", "query")
    class VertexRagStore(_message.Message):
        __slots__ = ("rag_corpora", "rag_resources", "vector_distance_threshold")
        class RagResource(_message.Message):
            __slots__ = ("rag_corpus", "rag_file_ids")
            RAG_CORPUS_FIELD_NUMBER: _ClassVar[int]
            RAG_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
            rag_corpus: str
            rag_file_ids: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, rag_corpus: _Optional[str] = ..., rag_file_ids: _Optional[_Iterable[str]] = ...) -> None: ...
        RAG_CORPORA_FIELD_NUMBER: _ClassVar[int]
        RAG_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        VECTOR_DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        rag_corpora: _containers.RepeatedScalarFieldContainer[str]
        rag_resources: _containers.RepeatedCompositeFieldContainer[RetrieveContextsRequest.VertexRagStore.RagResource]
        vector_distance_threshold: float
        def __init__(self, rag_corpora: _Optional[_Iterable[str]] = ..., rag_resources: _Optional[_Iterable[_Union[RetrieveContextsRequest.VertexRagStore.RagResource, _Mapping]]] = ..., vector_distance_threshold: _Optional[float] = ...) -> None: ...
    VERTEX_RAG_STORE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    vertex_rag_store: RetrieveContextsRequest.VertexRagStore
    parent: str
    query: RagQuery
    def __init__(self, vertex_rag_store: _Optional[_Union[RetrieveContextsRequest.VertexRagStore, _Mapping]] = ..., parent: _Optional[str] = ..., query: _Optional[_Union[RagQuery, _Mapping]] = ...) -> None: ...

class RagContexts(_message.Message):
    __slots__ = ("contexts",)
    class Context(_message.Message):
        __slots__ = ("source_uri", "source_display_name", "text", "distance", "sparse_distance", "score")
        SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
        SOURCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        SPARSE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        source_uri: str
        source_display_name: str
        text: str
        distance: float
        sparse_distance: float
        score: float
        def __init__(self, source_uri: _Optional[str] = ..., source_display_name: _Optional[str] = ..., text: _Optional[str] = ..., distance: _Optional[float] = ..., sparse_distance: _Optional[float] = ..., score: _Optional[float] = ...) -> None: ...
    CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    contexts: _containers.RepeatedCompositeFieldContainer[RagContexts.Context]
    def __init__(self, contexts: _Optional[_Iterable[_Union[RagContexts.Context, _Mapping]]] = ...) -> None: ...

class RetrieveContextsResponse(_message.Message):
    __slots__ = ("contexts",)
    CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    contexts: RagContexts
    def __init__(self, contexts: _Optional[_Union[RagContexts, _Mapping]] = ...) -> None: ...

class AugmentPromptRequest(_message.Message):
    __slots__ = ("vertex_rag_store", "parent", "contents", "model")
    class Model(_message.Message):
        __slots__ = ("model", "model_version")
        MODEL_FIELD_NUMBER: _ClassVar[int]
        MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
        model: str
        model_version: str
        def __init__(self, model: _Optional[str] = ..., model_version: _Optional[str] = ...) -> None: ...
    VERTEX_RAG_STORE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    vertex_rag_store: _tool_pb2.VertexRagStore
    parent: str
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    model: AugmentPromptRequest.Model
    def __init__(self, vertex_rag_store: _Optional[_Union[_tool_pb2.VertexRagStore, _Mapping]] = ..., parent: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ..., model: _Optional[_Union[AugmentPromptRequest.Model, _Mapping]] = ...) -> None: ...

class AugmentPromptResponse(_message.Message):
    __slots__ = ("augmented_prompt", "facts")
    AUGMENTED_PROMPT_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    augmented_prompt: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    facts: _containers.RepeatedCompositeFieldContainer[Fact]
    def __init__(self, augmented_prompt: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ..., facts: _Optional[_Iterable[_Union[Fact, _Mapping]]] = ...) -> None: ...

class CorroborateContentRequest(_message.Message):
    __slots__ = ("parent", "content", "facts", "parameters")
    class Parameters(_message.Message):
        __slots__ = ("citation_threshold",)
        CITATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        citation_threshold: float
        def __init__(self, citation_threshold: _Optional[float] = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    content: _content_pb2.Content
    facts: _containers.RepeatedCompositeFieldContainer[Fact]
    parameters: CorroborateContentRequest.Parameters
    def __init__(self, parent: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., facts: _Optional[_Iterable[_Union[Fact, _Mapping]]] = ..., parameters: _Optional[_Union[CorroborateContentRequest.Parameters, _Mapping]] = ...) -> None: ...

class CorroborateContentResponse(_message.Message):
    __slots__ = ("corroboration_score", "claims")
    CORROBORATION_SCORE_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    corroboration_score: float
    claims: _containers.RepeatedCompositeFieldContainer[Claim]
    def __init__(self, corroboration_score: _Optional[float] = ..., claims: _Optional[_Iterable[_Union[Claim, _Mapping]]] = ...) -> None: ...

class Fact(_message.Message):
    __slots__ = ("query", "title", "uri", "summary", "vector_distance", "score")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    VECTOR_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    query: str
    title: str
    uri: str
    summary: str
    vector_distance: float
    score: float
    def __init__(self, query: _Optional[str] = ..., title: _Optional[str] = ..., uri: _Optional[str] = ..., summary: _Optional[str] = ..., vector_distance: _Optional[float] = ..., score: _Optional[float] = ...) -> None: ...

class Claim(_message.Message):
    __slots__ = ("start_index", "end_index", "fact_indexes", "score")
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_INDEX_FIELD_NUMBER: _ClassVar[int]
    FACT_INDEXES_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    start_index: int
    end_index: int
    fact_indexes: _containers.RepeatedScalarFieldContainer[int]
    score: float
    def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ..., fact_indexes: _Optional[_Iterable[int]] = ..., score: _Optional[float] = ...) -> None: ...
