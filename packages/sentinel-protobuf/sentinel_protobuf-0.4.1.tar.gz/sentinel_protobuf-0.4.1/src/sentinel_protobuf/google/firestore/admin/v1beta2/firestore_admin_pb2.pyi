from google.api import annotations_pb2 as _annotations_pb2
from google.firestore.admin.v1beta2 import field_pb2 as _field_pb2
from google.firestore.admin.v1beta2 import index_pb2 as _index_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateIndexRequest(_message.Message):
    __slots__ = ('parent', 'index')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    parent: str
    index: _index_pb2.Index

    def __init__(self, parent: _Optional[str]=..., index: _Optional[_Union[_index_pb2.Index, _Mapping]]=...) -> None:
        ...

class ListIndexesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListIndexesResponse(_message.Message):
    __slots__ = ('indexes', 'next_page_token')
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    indexes: _containers.RepeatedCompositeFieldContainer[_index_pb2.Index]
    next_page_token: str

    def __init__(self, indexes: _Optional[_Iterable[_Union[_index_pb2.Index, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetIndexRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteIndexRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateFieldRequest(_message.Message):
    __slots__ = ('field', 'update_mask')
    FIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    field: _field_pb2.Field
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, field: _Optional[_Union[_field_pb2.Field, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetFieldRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFieldsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListFieldsResponse(_message.Message):
    __slots__ = ('fields', 'next_page_token')
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[_field_pb2.Field]
    next_page_token: str

    def __init__(self, fields: _Optional[_Iterable[_Union[_field_pb2.Field, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ExportDocumentsRequest(_message.Message):
    __slots__ = ('name', 'collection_ids', 'output_uri_prefix')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    name: str
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    output_uri_prefix: str

    def __init__(self, name: _Optional[str]=..., collection_ids: _Optional[_Iterable[str]]=..., output_uri_prefix: _Optional[str]=...) -> None:
        ...

class ImportDocumentsRequest(_message.Message):
    __slots__ = ('name', 'collection_ids', 'input_uri_prefix')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    INPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    name: str
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    input_uri_prefix: str

    def __init__(self, name: _Optional[str]=..., collection_ids: _Optional[_Iterable[str]]=..., input_uri_prefix: _Optional[str]=...) -> None:
        ...