from google.firestore.v1 import document_pb2 as _document_pb2
from google.firestore.v1 import query_pb2 as _query_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BundledQuery(_message.Message):
    __slots__ = ('parent', 'structured_query', 'limit_type')

    class LimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIRST: _ClassVar[BundledQuery.LimitType]
        LAST: _ClassVar[BundledQuery.LimitType]
    FIRST: BundledQuery.LimitType
    LAST: BundledQuery.LimitType
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    structured_query: _query_pb2.StructuredQuery
    limit_type: BundledQuery.LimitType

    def __init__(self, parent: _Optional[str]=..., structured_query: _Optional[_Union[_query_pb2.StructuredQuery, _Mapping]]=..., limit_type: _Optional[_Union[BundledQuery.LimitType, str]]=...) -> None:
        ...

class NamedQuery(_message.Message):
    __slots__ = ('name', 'bundled_query', 'read_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUNDLED_QUERY_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    bundled_query: BundledQuery
    read_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., bundled_query: _Optional[_Union[BundledQuery, _Mapping]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BundledDocumentMetadata(_message.Message):
    __slots__ = ('name', 'read_time', 'exists', 'queries')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_time: _timestamp_pb2.Timestamp
    exists: bool
    queries: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., exists: bool=..., queries: _Optional[_Iterable[str]]=...) -> None:
        ...

class BundleMetadata(_message.Message):
    __slots__ = ('id', 'create_time', 'version', 'total_documents', 'total_bytes')
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    create_time: _timestamp_pb2.Timestamp
    version: int
    total_documents: int
    total_bytes: int

    def __init__(self, id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version: _Optional[int]=..., total_documents: _Optional[int]=..., total_bytes: _Optional[int]=...) -> None:
        ...

class BundleElement(_message.Message):
    __slots__ = ('metadata', 'named_query', 'document_metadata', 'document')
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAMED_QUERY_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    metadata: BundleMetadata
    named_query: NamedQuery
    document_metadata: BundledDocumentMetadata
    document: _document_pb2.Document

    def __init__(self, metadata: _Optional[_Union[BundleMetadata, _Mapping]]=..., named_query: _Optional[_Union[NamedQuery, _Mapping]]=..., document_metadata: _Optional[_Union[BundledDocumentMetadata, _Mapping]]=..., document: _Optional[_Union[_document_pb2.Document, _Mapping]]=...) -> None:
        ...