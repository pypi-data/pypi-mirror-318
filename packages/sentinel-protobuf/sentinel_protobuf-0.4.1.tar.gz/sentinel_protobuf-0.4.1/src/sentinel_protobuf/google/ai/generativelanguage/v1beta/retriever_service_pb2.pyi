from google.ai.generativelanguage.v1beta import retriever_pb2 as _retriever_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateCorpusRequest(_message.Message):
    __slots__ = ('corpus',)
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    corpus: _retriever_pb2.Corpus

    def __init__(self, corpus: _Optional[_Union[_retriever_pb2.Corpus, _Mapping]]=...) -> None:
        ...

class GetCorpusRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateCorpusRequest(_message.Message):
    __slots__ = ('corpus', 'update_mask')
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    corpus: _retriever_pb2.Corpus
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, corpus: _Optional[_Union[_retriever_pb2.Corpus, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCorpusRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListCorporaRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCorporaResponse(_message.Message):
    __slots__ = ('corpora', 'next_page_token')
    CORPORA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    corpora: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.Corpus]
    next_page_token: str

    def __init__(self, corpora: _Optional[_Iterable[_Union[_retriever_pb2.Corpus, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class QueryCorpusRequest(_message.Message):
    __slots__ = ('name', 'query', 'metadata_filters', 'results_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FILTERS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: str
    metadata_filters: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.MetadataFilter]
    results_count: int

    def __init__(self, name: _Optional[str]=..., query: _Optional[str]=..., metadata_filters: _Optional[_Iterable[_Union[_retriever_pb2.MetadataFilter, _Mapping]]]=..., results_count: _Optional[int]=...) -> None:
        ...

class QueryCorpusResponse(_message.Message):
    __slots__ = ('relevant_chunks',)
    RELEVANT_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    relevant_chunks: _containers.RepeatedCompositeFieldContainer[RelevantChunk]

    def __init__(self, relevant_chunks: _Optional[_Iterable[_Union[RelevantChunk, _Mapping]]]=...) -> None:
        ...

class RelevantChunk(_message.Message):
    __slots__ = ('chunk_relevance_score', 'chunk')
    CHUNK_RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk_relevance_score: float
    chunk: _retriever_pb2.Chunk

    def __init__(self, chunk_relevance_score: _Optional[float]=..., chunk: _Optional[_Union[_retriever_pb2.Chunk, _Mapping]]=...) -> None:
        ...

class CreateDocumentRequest(_message.Message):
    __slots__ = ('parent', 'document')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    document: _retriever_pb2.Document

    def __init__(self, parent: _Optional[str]=..., document: _Optional[_Union[_retriever_pb2.Document, _Mapping]]=...) -> None:
        ...

class GetDocumentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDocumentRequest(_message.Message):
    __slots__ = ('document', 'update_mask')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    document: _retriever_pb2.Document
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, document: _Optional[_Union[_retriever_pb2.Document, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDocumentRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListDocumentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDocumentsResponse(_message.Message):
    __slots__ = ('documents', 'next_page_token')
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.Document]
    next_page_token: str

    def __init__(self, documents: _Optional[_Iterable[_Union[_retriever_pb2.Document, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class QueryDocumentRequest(_message.Message):
    __slots__ = ('name', 'query', 'results_count', 'metadata_filters')
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FILTERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: str
    results_count: int
    metadata_filters: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.MetadataFilter]

    def __init__(self, name: _Optional[str]=..., query: _Optional[str]=..., results_count: _Optional[int]=..., metadata_filters: _Optional[_Iterable[_Union[_retriever_pb2.MetadataFilter, _Mapping]]]=...) -> None:
        ...

class QueryDocumentResponse(_message.Message):
    __slots__ = ('relevant_chunks',)
    RELEVANT_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    relevant_chunks: _containers.RepeatedCompositeFieldContainer[RelevantChunk]

    def __init__(self, relevant_chunks: _Optional[_Iterable[_Union[RelevantChunk, _Mapping]]]=...) -> None:
        ...

class CreateChunkRequest(_message.Message):
    __slots__ = ('parent', 'chunk')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    chunk: _retriever_pb2.Chunk

    def __init__(self, parent: _Optional[str]=..., chunk: _Optional[_Union[_retriever_pb2.Chunk, _Mapping]]=...) -> None:
        ...

class BatchCreateChunksRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateChunkRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateChunkRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateChunksResponse(_message.Message):
    __slots__ = ('chunks',)
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    chunks: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.Chunk]

    def __init__(self, chunks: _Optional[_Iterable[_Union[_retriever_pb2.Chunk, _Mapping]]]=...) -> None:
        ...

class GetChunkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateChunkRequest(_message.Message):
    __slots__ = ('chunk', 'update_mask')
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    chunk: _retriever_pb2.Chunk
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, chunk: _Optional[_Union[_retriever_pb2.Chunk, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class BatchUpdateChunksRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateChunkRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[UpdateChunkRequest, _Mapping]]]=...) -> None:
        ...

class BatchUpdateChunksResponse(_message.Message):
    __slots__ = ('chunks',)
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    chunks: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.Chunk]

    def __init__(self, chunks: _Optional[_Iterable[_Union[_retriever_pb2.Chunk, _Mapping]]]=...) -> None:
        ...

class DeleteChunkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchDeleteChunksRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[DeleteChunkRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[DeleteChunkRequest, _Mapping]]]=...) -> None:
        ...

class ListChunksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListChunksResponse(_message.Message):
    __slots__ = ('chunks', 'next_page_token')
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    chunks: _containers.RepeatedCompositeFieldContainer[_retriever_pb2.Chunk]
    next_page_token: str

    def __init__(self, chunks: _Optional[_Iterable[_Union[_retriever_pb2.Chunk, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...