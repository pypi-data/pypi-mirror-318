from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Chunk(_message.Message):
    __slots__ = ("name", "id", "content", "relevance_score", "document_metadata", "derived_struct_data", "page_span", "chunk_metadata")
    class DocumentMetadata(_message.Message):
        __slots__ = ("uri", "title", "struct_data")
        URI_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
        uri: str
        title: str
        struct_data: _struct_pb2.Struct
        def __init__(self, uri: _Optional[str] = ..., title: _Optional[str] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    class PageSpan(_message.Message):
        __slots__ = ("page_start", "page_end")
        PAGE_START_FIELD_NUMBER: _ClassVar[int]
        PAGE_END_FIELD_NUMBER: _ClassVar[int]
        page_start: int
        page_end: int
        def __init__(self, page_start: _Optional[int] = ..., page_end: _Optional[int] = ...) -> None: ...
    class ChunkMetadata(_message.Message):
        __slots__ = ("previous_chunks", "next_chunks")
        PREVIOUS_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        NEXT_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        previous_chunks: _containers.RepeatedCompositeFieldContainer[Chunk]
        next_chunks: _containers.RepeatedCompositeFieldContainer[Chunk]
        def __init__(self, previous_chunks: _Optional[_Iterable[_Union[Chunk, _Mapping]]] = ..., next_chunks: _Optional[_Iterable[_Union[Chunk, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    DERIVED_STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
    PAGE_SPAN_FIELD_NUMBER: _ClassVar[int]
    CHUNK_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    content: str
    relevance_score: float
    document_metadata: Chunk.DocumentMetadata
    derived_struct_data: _struct_pb2.Struct
    page_span: Chunk.PageSpan
    chunk_metadata: Chunk.ChunkMetadata
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., content: _Optional[str] = ..., relevance_score: _Optional[float] = ..., document_metadata: _Optional[_Union[Chunk.DocumentMetadata, _Mapping]] = ..., derived_struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., page_span: _Optional[_Union[Chunk.PageSpan, _Mapping]] = ..., chunk_metadata: _Optional[_Union[Chunk.ChunkMetadata, _Mapping]] = ...) -> None: ...
