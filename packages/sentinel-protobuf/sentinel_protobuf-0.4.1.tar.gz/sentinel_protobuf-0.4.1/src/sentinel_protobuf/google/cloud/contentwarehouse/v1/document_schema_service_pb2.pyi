from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import document_schema_pb2 as _document_schema_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDocumentSchemaRequest(_message.Message):
    __slots__ = ('parent', 'document_schema')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    document_schema: _document_schema_pb2.DocumentSchema

    def __init__(self, parent: _Optional[str]=..., document_schema: _Optional[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]=...) -> None:
        ...

class GetDocumentSchemaRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDocumentSchemaRequest(_message.Message):
    __slots__ = ('name', 'document_schema')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    document_schema: _document_schema_pb2.DocumentSchema

    def __init__(self, name: _Optional[str]=..., document_schema: _Optional[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]=...) -> None:
        ...

class DeleteDocumentSchemaRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDocumentSchemasRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDocumentSchemasResponse(_message.Message):
    __slots__ = ('document_schemas', 'next_page_token')
    DOCUMENT_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    document_schemas: _containers.RepeatedCompositeFieldContainer[_document_schema_pb2.DocumentSchema]
    next_page_token: str

    def __init__(self, document_schemas: _Optional[_Iterable[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...