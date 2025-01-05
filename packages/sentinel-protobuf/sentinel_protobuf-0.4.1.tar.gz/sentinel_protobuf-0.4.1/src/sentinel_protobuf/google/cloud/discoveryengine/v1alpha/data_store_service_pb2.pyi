from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import data_store_pb2 as _data_store_pb2
from google.cloud.discoveryengine.v1alpha import document_processing_config_pb2 as _document_processing_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDataStoreRequest(_message.Message):
    __slots__ = ('parent', 'data_store', 'data_store_id', 'create_advanced_site_search', 'skip_default_schema_creation')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_ADVANCED_SITE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    SKIP_DEFAULT_SCHEMA_CREATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_store: _data_store_pb2.DataStore
    data_store_id: str
    create_advanced_site_search: bool
    skip_default_schema_creation: bool

    def __init__(self, parent: _Optional[str]=..., data_store: _Optional[_Union[_data_store_pb2.DataStore, _Mapping]]=..., data_store_id: _Optional[str]=..., create_advanced_site_search: bool=..., skip_default_schema_creation: bool=...) -> None:
        ...

class GetDataStoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDataStoreMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListDataStoresRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListDataStoresResponse(_message.Message):
    __slots__ = ('data_stores', 'next_page_token')
    DATA_STORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_stores: _containers.RepeatedCompositeFieldContainer[_data_store_pb2.DataStore]
    next_page_token: str

    def __init__(self, data_stores: _Optional[_Iterable[_Union[_data_store_pb2.DataStore, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteDataStoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDataStoreRequest(_message.Message):
    __slots__ = ('data_store', 'update_mask')
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_store: _data_store_pb2.DataStore
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, data_store: _Optional[_Union[_data_store_pb2.DataStore, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDataStoreMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetDocumentProcessingConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDocumentProcessingConfigRequest(_message.Message):
    __slots__ = ('document_processing_config', 'update_mask')
    DOCUMENT_PROCESSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    document_processing_config: _document_processing_config_pb2.DocumentProcessingConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, document_processing_config: _Optional[_Union[_document_processing_config_pb2.DocumentProcessingConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...