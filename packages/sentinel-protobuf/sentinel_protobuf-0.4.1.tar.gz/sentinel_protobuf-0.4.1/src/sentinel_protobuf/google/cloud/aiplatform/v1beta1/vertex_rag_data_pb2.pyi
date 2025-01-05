from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import api_auth_pb2 as _api_auth_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RagEmbeddingModelConfig(_message.Message):
    __slots__ = ("vertex_prediction_endpoint", "hybrid_search_config")
    class VertexPredictionEndpoint(_message.Message):
        __slots__ = ("endpoint", "model", "model_version_id")
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        model: str
        model_version_id: str
        def __init__(self, endpoint: _Optional[str] = ..., model: _Optional[str] = ..., model_version_id: _Optional[str] = ...) -> None: ...
    class SparseEmbeddingConfig(_message.Message):
        __slots__ = ("bm25",)
        class Bm25(_message.Message):
            __slots__ = ("multilingual", "k1", "b")
            MULTILINGUAL_FIELD_NUMBER: _ClassVar[int]
            K1_FIELD_NUMBER: _ClassVar[int]
            B_FIELD_NUMBER: _ClassVar[int]
            multilingual: bool
            k1: float
            b: float
            def __init__(self, multilingual: bool = ..., k1: _Optional[float] = ..., b: _Optional[float] = ...) -> None: ...
        BM25_FIELD_NUMBER: _ClassVar[int]
        bm25: RagEmbeddingModelConfig.SparseEmbeddingConfig.Bm25
        def __init__(self, bm25: _Optional[_Union[RagEmbeddingModelConfig.SparseEmbeddingConfig.Bm25, _Mapping]] = ...) -> None: ...
    class HybridSearchConfig(_message.Message):
        __slots__ = ("sparse_embedding_config", "dense_embedding_model_prediction_endpoint")
        SPARSE_EMBEDDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        DENSE_EMBEDDING_MODEL_PREDICTION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        sparse_embedding_config: RagEmbeddingModelConfig.SparseEmbeddingConfig
        dense_embedding_model_prediction_endpoint: RagEmbeddingModelConfig.VertexPredictionEndpoint
        def __init__(self, sparse_embedding_config: _Optional[_Union[RagEmbeddingModelConfig.SparseEmbeddingConfig, _Mapping]] = ..., dense_embedding_model_prediction_endpoint: _Optional[_Union[RagEmbeddingModelConfig.VertexPredictionEndpoint, _Mapping]] = ...) -> None: ...
    VERTEX_PREDICTION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HYBRID_SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    vertex_prediction_endpoint: RagEmbeddingModelConfig.VertexPredictionEndpoint
    hybrid_search_config: RagEmbeddingModelConfig.HybridSearchConfig
    def __init__(self, vertex_prediction_endpoint: _Optional[_Union[RagEmbeddingModelConfig.VertexPredictionEndpoint, _Mapping]] = ..., hybrid_search_config: _Optional[_Union[RagEmbeddingModelConfig.HybridSearchConfig, _Mapping]] = ...) -> None: ...

class RagVectorDbConfig(_message.Message):
    __slots__ = ("rag_managed_db", "weaviate", "pinecone", "vertex_feature_store", "vertex_vector_search", "api_auth", "rag_embedding_model_config")
    class RagManagedDb(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Weaviate(_message.Message):
        __slots__ = ("http_endpoint", "collection_name")
        HTTP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
        http_endpoint: str
        collection_name: str
        def __init__(self, http_endpoint: _Optional[str] = ..., collection_name: _Optional[str] = ...) -> None: ...
    class Pinecone(_message.Message):
        __slots__ = ("index_name",)
        INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
        index_name: str
        def __init__(self, index_name: _Optional[str] = ...) -> None: ...
    class VertexFeatureStore(_message.Message):
        __slots__ = ("feature_view_resource_name",)
        FEATURE_VIEW_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        feature_view_resource_name: str
        def __init__(self, feature_view_resource_name: _Optional[str] = ...) -> None: ...
    class VertexVectorSearch(_message.Message):
        __slots__ = ("index_endpoint", "index")
        INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        index_endpoint: str
        index: str
        def __init__(self, index_endpoint: _Optional[str] = ..., index: _Optional[str] = ...) -> None: ...
    RAG_MANAGED_DB_FIELD_NUMBER: _ClassVar[int]
    WEAVIATE_FIELD_NUMBER: _ClassVar[int]
    PINECONE_FIELD_NUMBER: _ClassVar[int]
    VERTEX_FEATURE_STORE_FIELD_NUMBER: _ClassVar[int]
    VERTEX_VECTOR_SEARCH_FIELD_NUMBER: _ClassVar[int]
    API_AUTH_FIELD_NUMBER: _ClassVar[int]
    RAG_EMBEDDING_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_managed_db: RagVectorDbConfig.RagManagedDb
    weaviate: RagVectorDbConfig.Weaviate
    pinecone: RagVectorDbConfig.Pinecone
    vertex_feature_store: RagVectorDbConfig.VertexFeatureStore
    vertex_vector_search: RagVectorDbConfig.VertexVectorSearch
    api_auth: _api_auth_pb2.ApiAuth
    rag_embedding_model_config: RagEmbeddingModelConfig
    def __init__(self, rag_managed_db: _Optional[_Union[RagVectorDbConfig.RagManagedDb, _Mapping]] = ..., weaviate: _Optional[_Union[RagVectorDbConfig.Weaviate, _Mapping]] = ..., pinecone: _Optional[_Union[RagVectorDbConfig.Pinecone, _Mapping]] = ..., vertex_feature_store: _Optional[_Union[RagVectorDbConfig.VertexFeatureStore, _Mapping]] = ..., vertex_vector_search: _Optional[_Union[RagVectorDbConfig.VertexVectorSearch, _Mapping]] = ..., api_auth: _Optional[_Union[_api_auth_pb2.ApiAuth, _Mapping]] = ..., rag_embedding_model_config: _Optional[_Union[RagEmbeddingModelConfig, _Mapping]] = ...) -> None: ...

class FileStatus(_message.Message):
    __slots__ = ("state", "error_status")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[FileStatus.State]
        ACTIVE: _ClassVar[FileStatus.State]
        ERROR: _ClassVar[FileStatus.State]
    STATE_UNSPECIFIED: FileStatus.State
    ACTIVE: FileStatus.State
    ERROR: FileStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    state: FileStatus.State
    error_status: str
    def __init__(self, state: _Optional[_Union[FileStatus.State, str]] = ..., error_status: _Optional[str] = ...) -> None: ...

class VertexAiSearchConfig(_message.Message):
    __slots__ = ("serving_config",)
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    serving_config: str
    def __init__(self, serving_config: _Optional[str] = ...) -> None: ...

class CorpusStatus(_message.Message):
    __slots__ = ("state", "error_status")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CorpusStatus.State]
        INITIALIZED: _ClassVar[CorpusStatus.State]
        ACTIVE: _ClassVar[CorpusStatus.State]
        ERROR: _ClassVar[CorpusStatus.State]
    UNKNOWN: CorpusStatus.State
    INITIALIZED: CorpusStatus.State
    ACTIVE: CorpusStatus.State
    ERROR: CorpusStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    state: CorpusStatus.State
    error_status: str
    def __init__(self, state: _Optional[_Union[CorpusStatus.State, str]] = ..., error_status: _Optional[str] = ...) -> None: ...

class RagCorpus(_message.Message):
    __slots__ = ("name", "display_name", "description", "rag_embedding_model_config", "rag_vector_db_config", "create_time", "update_time", "corpus_status", "vector_db_config", "vertex_ai_search_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RAG_EMBEDDING_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RAG_VECTOR_DB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CORPUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    VECTOR_DB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERTEX_AI_SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    rag_embedding_model_config: RagEmbeddingModelConfig
    rag_vector_db_config: RagVectorDbConfig
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    corpus_status: CorpusStatus
    vector_db_config: RagVectorDbConfig
    vertex_ai_search_config: VertexAiSearchConfig
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., rag_embedding_model_config: _Optional[_Union[RagEmbeddingModelConfig, _Mapping]] = ..., rag_vector_db_config: _Optional[_Union[RagVectorDbConfig, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., corpus_status: _Optional[_Union[CorpusStatus, _Mapping]] = ..., vector_db_config: _Optional[_Union[RagVectorDbConfig, _Mapping]] = ..., vertex_ai_search_config: _Optional[_Union[VertexAiSearchConfig, _Mapping]] = ...) -> None: ...

class RagFile(_message.Message):
    __slots__ = ("gcs_source", "google_drive_source", "direct_upload_source", "slack_source", "jira_source", "share_point_sources", "name", "display_name", "description", "size_bytes", "rag_file_type", "create_time", "update_time", "file_status")
    class RagFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RAG_FILE_TYPE_UNSPECIFIED: _ClassVar[RagFile.RagFileType]
        RAG_FILE_TYPE_TXT: _ClassVar[RagFile.RagFileType]
        RAG_FILE_TYPE_PDF: _ClassVar[RagFile.RagFileType]
    RAG_FILE_TYPE_UNSPECIFIED: RagFile.RagFileType
    RAG_FILE_TYPE_TXT: RagFile.RagFileType
    RAG_FILE_TYPE_PDF: RagFile.RagFileType
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIRECT_UPLOAD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SLACK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JIRA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SHARE_POINT_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_STATUS_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _io_pb2.GcsSource
    google_drive_source: _io_pb2.GoogleDriveSource
    direct_upload_source: _io_pb2.DirectUploadSource
    slack_source: _io_pb2.SlackSource
    jira_source: _io_pb2.JiraSource
    share_point_sources: _io_pb2.SharePointSources
    name: str
    display_name: str
    description: str
    size_bytes: int
    rag_file_type: RagFile.RagFileType
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    file_status: FileStatus
    def __init__(self, gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]] = ..., google_drive_source: _Optional[_Union[_io_pb2.GoogleDriveSource, _Mapping]] = ..., direct_upload_source: _Optional[_Union[_io_pb2.DirectUploadSource, _Mapping]] = ..., slack_source: _Optional[_Union[_io_pb2.SlackSource, _Mapping]] = ..., jira_source: _Optional[_Union[_io_pb2.JiraSource, _Mapping]] = ..., share_point_sources: _Optional[_Union[_io_pb2.SharePointSources, _Mapping]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., size_bytes: _Optional[int] = ..., rag_file_type: _Optional[_Union[RagFile.RagFileType, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., file_status: _Optional[_Union[FileStatus, _Mapping]] = ...) -> None: ...

class RagFileChunkingConfig(_message.Message):
    __slots__ = ("fixed_length_chunking", "chunk_size", "chunk_overlap")
    class FixedLengthChunking(_message.Message):
        __slots__ = ("chunk_size", "chunk_overlap")
        CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        CHUNK_OVERLAP_FIELD_NUMBER: _ClassVar[int]
        chunk_size: int
        chunk_overlap: int
        def __init__(self, chunk_size: _Optional[int] = ..., chunk_overlap: _Optional[int] = ...) -> None: ...
    FIXED_LENGTH_CHUNKING_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    fixed_length_chunking: RagFileChunkingConfig.FixedLengthChunking
    chunk_size: int
    chunk_overlap: int
    def __init__(self, fixed_length_chunking: _Optional[_Union[RagFileChunkingConfig.FixedLengthChunking, _Mapping]] = ..., chunk_size: _Optional[int] = ..., chunk_overlap: _Optional[int] = ...) -> None: ...

class RagFileTransformationConfig(_message.Message):
    __slots__ = ("rag_file_chunking_config",)
    RAG_FILE_CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_file_chunking_config: RagFileChunkingConfig
    def __init__(self, rag_file_chunking_config: _Optional[_Union[RagFileChunkingConfig, _Mapping]] = ...) -> None: ...

class RagFileParsingConfig(_message.Message):
    __slots__ = ("advanced_parser", "layout_parser", "llm_parser", "use_advanced_pdf_parsing")
    class AdvancedParser(_message.Message):
        __slots__ = ("use_advanced_pdf_parsing",)
        USE_ADVANCED_PDF_PARSING_FIELD_NUMBER: _ClassVar[int]
        use_advanced_pdf_parsing: bool
        def __init__(self, use_advanced_pdf_parsing: bool = ...) -> None: ...
    class LayoutParser(_message.Message):
        __slots__ = ("processor_name", "max_parsing_requests_per_min")
        PROCESSOR_NAME_FIELD_NUMBER: _ClassVar[int]
        MAX_PARSING_REQUESTS_PER_MIN_FIELD_NUMBER: _ClassVar[int]
        processor_name: str
        max_parsing_requests_per_min: int
        def __init__(self, processor_name: _Optional[str] = ..., max_parsing_requests_per_min: _Optional[int] = ...) -> None: ...
    class LlmParser(_message.Message):
        __slots__ = ("model_name", "max_parsing_requests_per_min", "custom_parsing_prompt")
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        MAX_PARSING_REQUESTS_PER_MIN_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_PARSING_PROMPT_FIELD_NUMBER: _ClassVar[int]
        model_name: str
        max_parsing_requests_per_min: int
        custom_parsing_prompt: str
        def __init__(self, model_name: _Optional[str] = ..., max_parsing_requests_per_min: _Optional[int] = ..., custom_parsing_prompt: _Optional[str] = ...) -> None: ...
    ADVANCED_PARSER_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_PARSER_FIELD_NUMBER: _ClassVar[int]
    LLM_PARSER_FIELD_NUMBER: _ClassVar[int]
    USE_ADVANCED_PDF_PARSING_FIELD_NUMBER: _ClassVar[int]
    advanced_parser: RagFileParsingConfig.AdvancedParser
    layout_parser: RagFileParsingConfig.LayoutParser
    llm_parser: RagFileParsingConfig.LlmParser
    use_advanced_pdf_parsing: bool
    def __init__(self, advanced_parser: _Optional[_Union[RagFileParsingConfig.AdvancedParser, _Mapping]] = ..., layout_parser: _Optional[_Union[RagFileParsingConfig.LayoutParser, _Mapping]] = ..., llm_parser: _Optional[_Union[RagFileParsingConfig.LlmParser, _Mapping]] = ..., use_advanced_pdf_parsing: bool = ...) -> None: ...

class UploadRagFileConfig(_message.Message):
    __slots__ = ("rag_file_chunking_config", "rag_file_transformation_config")
    RAG_FILE_CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_TRANSFORMATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_file_chunking_config: RagFileChunkingConfig
    rag_file_transformation_config: RagFileTransformationConfig
    def __init__(self, rag_file_chunking_config: _Optional[_Union[RagFileChunkingConfig, _Mapping]] = ..., rag_file_transformation_config: _Optional[_Union[RagFileTransformationConfig, _Mapping]] = ...) -> None: ...

class ImportRagFilesConfig(_message.Message):
    __slots__ = ("gcs_source", "google_drive_source", "slack_source", "jira_source", "share_point_sources", "partial_failure_gcs_sink", "partial_failure_bigquery_sink", "rag_file_chunking_config", "rag_file_transformation_config", "rag_file_parsing_config", "max_embedding_requests_per_min")
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SLACK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JIRA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SHARE_POINT_SOURCES_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_GCS_SINK_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_BIGQUERY_SINK_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_TRANSFORMATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_PARSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAX_EMBEDDING_REQUESTS_PER_MIN_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _io_pb2.GcsSource
    google_drive_source: _io_pb2.GoogleDriveSource
    slack_source: _io_pb2.SlackSource
    jira_source: _io_pb2.JiraSource
    share_point_sources: _io_pb2.SharePointSources
    partial_failure_gcs_sink: _io_pb2.GcsDestination
    partial_failure_bigquery_sink: _io_pb2.BigQueryDestination
    rag_file_chunking_config: RagFileChunkingConfig
    rag_file_transformation_config: RagFileTransformationConfig
    rag_file_parsing_config: RagFileParsingConfig
    max_embedding_requests_per_min: int
    def __init__(self, gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]] = ..., google_drive_source: _Optional[_Union[_io_pb2.GoogleDriveSource, _Mapping]] = ..., slack_source: _Optional[_Union[_io_pb2.SlackSource, _Mapping]] = ..., jira_source: _Optional[_Union[_io_pb2.JiraSource, _Mapping]] = ..., share_point_sources: _Optional[_Union[_io_pb2.SharePointSources, _Mapping]] = ..., partial_failure_gcs_sink: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]] = ..., partial_failure_bigquery_sink: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]] = ..., rag_file_chunking_config: _Optional[_Union[RagFileChunkingConfig, _Mapping]] = ..., rag_file_transformation_config: _Optional[_Union[RagFileTransformationConfig, _Mapping]] = ..., rag_file_parsing_config: _Optional[_Union[RagFileParsingConfig, _Mapping]] = ..., max_embedding_requests_per_min: _Optional[int] = ...) -> None: ...
