from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import vertex_rag_data_pb2 as _vertex_rag_data_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRagCorpusRequest(_message.Message):
    __slots__ = ("parent", "rag_corpus")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RAG_CORPUS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rag_corpus: _vertex_rag_data_pb2.RagCorpus
    def __init__(self, parent: _Optional[str] = ..., rag_corpus: _Optional[_Union[_vertex_rag_data_pb2.RagCorpus, _Mapping]] = ...) -> None: ...

class GetRagCorpusRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRagCorporaRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRagCorporaResponse(_message.Message):
    __slots__ = ("rag_corpora", "next_page_token")
    RAG_CORPORA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rag_corpora: _containers.RepeatedCompositeFieldContainer[_vertex_rag_data_pb2.RagCorpus]
    next_page_token: str
    def __init__(self, rag_corpora: _Optional[_Iterable[_Union[_vertex_rag_data_pb2.RagCorpus, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteRagCorpusRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class UploadRagFileRequest(_message.Message):
    __slots__ = ("parent", "rag_file", "upload_rag_file_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_RAG_FILE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rag_file: _vertex_rag_data_pb2.RagFile
    upload_rag_file_config: _vertex_rag_data_pb2.UploadRagFileConfig
    def __init__(self, parent: _Optional[str] = ..., rag_file: _Optional[_Union[_vertex_rag_data_pb2.RagFile, _Mapping]] = ..., upload_rag_file_config: _Optional[_Union[_vertex_rag_data_pb2.UploadRagFileConfig, _Mapping]] = ...) -> None: ...

class UploadRagFileResponse(_message.Message):
    __slots__ = ("rag_file", "error")
    RAG_FILE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    rag_file: _vertex_rag_data_pb2.RagFile
    error: _status_pb2.Status
    def __init__(self, rag_file: _Optional[_Union[_vertex_rag_data_pb2.RagFile, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class ImportRagFilesRequest(_message.Message):
    __slots__ = ("parent", "import_rag_files_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_RAG_FILES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    import_rag_files_config: _vertex_rag_data_pb2.ImportRagFilesConfig
    def __init__(self, parent: _Optional[str] = ..., import_rag_files_config: _Optional[_Union[_vertex_rag_data_pb2.ImportRagFilesConfig, _Mapping]] = ...) -> None: ...

class ImportRagFilesResponse(_message.Message):
    __slots__ = ("partial_failures_gcs_path", "partial_failures_bigquery_table", "imported_rag_files_count", "failed_rag_files_count", "skipped_rag_files_count")
    PARTIAL_FAILURES_GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_BIGQUERY_TABLE_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_RAG_FILES_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_RAG_FILES_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_RAG_FILES_COUNT_FIELD_NUMBER: _ClassVar[int]
    partial_failures_gcs_path: str
    partial_failures_bigquery_table: str
    imported_rag_files_count: int
    failed_rag_files_count: int
    skipped_rag_files_count: int
    def __init__(self, partial_failures_gcs_path: _Optional[str] = ..., partial_failures_bigquery_table: _Optional[str] = ..., imported_rag_files_count: _Optional[int] = ..., failed_rag_files_count: _Optional[int] = ..., skipped_rag_files_count: _Optional[int] = ...) -> None: ...

class GetRagFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRagFilesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRagFilesResponse(_message.Message):
    __slots__ = ("rag_files", "next_page_token")
    RAG_FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rag_files: _containers.RepeatedCompositeFieldContainer[_vertex_rag_data_pb2.RagFile]
    next_page_token: str
    def __init__(self, rag_files: _Optional[_Iterable[_Union[_vertex_rag_data_pb2.RagFile, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteRagFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRagCorpusOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class UpdateRagCorpusRequest(_message.Message):
    __slots__ = ("rag_corpus",)
    RAG_CORPUS_FIELD_NUMBER: _ClassVar[int]
    rag_corpus: _vertex_rag_data_pb2.RagCorpus
    def __init__(self, rag_corpus: _Optional[_Union[_vertex_rag_data_pb2.RagCorpus, _Mapping]] = ...) -> None: ...

class UpdateRagCorpusOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class ImportRagFilesOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata", "rag_corpus_id", "import_rag_files_config", "progress_percentage")
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    RAG_CORPUS_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_RAG_FILES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    rag_corpus_id: int
    import_rag_files_config: _vertex_rag_data_pb2.ImportRagFilesConfig
    progress_percentage: int
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ..., rag_corpus_id: _Optional[int] = ..., import_rag_files_config: _Optional[_Union[_vertex_rag_data_pb2.ImportRagFilesConfig, _Mapping]] = ..., progress_percentage: _Optional[int] = ...) -> None: ...
