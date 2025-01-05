from google.api import annotations_pb2 as _annotations_pb2
from google.firestore.admin.v1beta1 import index_pb2 as _index_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[OperationState]
    INITIALIZING: _ClassVar[OperationState]
    PROCESSING: _ClassVar[OperationState]
    CANCELLING: _ClassVar[OperationState]
    FINALIZING: _ClassVar[OperationState]
    SUCCESSFUL: _ClassVar[OperationState]
    FAILED: _ClassVar[OperationState]
    CANCELLED: _ClassVar[OperationState]
STATE_UNSPECIFIED: OperationState
INITIALIZING: OperationState
PROCESSING: OperationState
CANCELLING: OperationState
FINALIZING: OperationState
SUCCESSFUL: OperationState
FAILED: OperationState
CANCELLED: OperationState

class IndexOperationMetadata(_message.Message):
    __slots__ = ('start_time', 'end_time', 'index', 'operation_type', 'cancelled', 'document_progress')

    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[IndexOperationMetadata.OperationType]
        CREATING_INDEX: _ClassVar[IndexOperationMetadata.OperationType]
    OPERATION_TYPE_UNSPECIFIED: IndexOperationMetadata.OperationType
    CREATING_INDEX: IndexOperationMetadata.OperationType
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    index: str
    operation_type: IndexOperationMetadata.OperationType
    cancelled: bool
    document_progress: Progress

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., index: _Optional[str]=..., operation_type: _Optional[_Union[IndexOperationMetadata.OperationType, str]]=..., cancelled: bool=..., document_progress: _Optional[_Union[Progress, _Mapping]]=...) -> None:
        ...

class Progress(_message.Message):
    __slots__ = ('work_completed', 'work_estimated')
    WORK_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    WORK_ESTIMATED_FIELD_NUMBER: _ClassVar[int]
    work_completed: int
    work_estimated: int

    def __init__(self, work_completed: _Optional[int]=..., work_estimated: _Optional[int]=...) -> None:
        ...

class CreateIndexRequest(_message.Message):
    __slots__ = ('parent', 'index')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    parent: str
    index: _index_pb2.Index

    def __init__(self, parent: _Optional[str]=..., index: _Optional[_Union[_index_pb2.Index, _Mapping]]=...) -> None:
        ...

class GetIndexRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
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

class DeleteIndexRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListIndexesResponse(_message.Message):
    __slots__ = ('indexes', 'next_page_token')
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    indexes: _containers.RepeatedCompositeFieldContainer[_index_pb2.Index]
    next_page_token: str

    def __init__(self, indexes: _Optional[_Iterable[_Union[_index_pb2.Index, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
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

class ExportDocumentsResponse(_message.Message):
    __slots__ = ('output_uri_prefix',)
    OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    output_uri_prefix: str

    def __init__(self, output_uri_prefix: _Optional[str]=...) -> None:
        ...

class ExportDocumentsMetadata(_message.Message):
    __slots__ = ('start_time', 'end_time', 'operation_state', 'progress_documents', 'progress_bytes', 'collection_ids', 'output_uri_prefix')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_BYTES_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    operation_state: OperationState
    progress_documents: Progress
    progress_bytes: Progress
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    output_uri_prefix: str

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., operation_state: _Optional[_Union[OperationState, str]]=..., progress_documents: _Optional[_Union[Progress, _Mapping]]=..., progress_bytes: _Optional[_Union[Progress, _Mapping]]=..., collection_ids: _Optional[_Iterable[str]]=..., output_uri_prefix: _Optional[str]=...) -> None:
        ...

class ImportDocumentsMetadata(_message.Message):
    __slots__ = ('start_time', 'end_time', 'operation_state', 'progress_documents', 'progress_bytes', 'collection_ids', 'input_uri_prefix')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_BYTES_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    INPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    operation_state: OperationState
    progress_documents: Progress
    progress_bytes: Progress
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    input_uri_prefix: str

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., operation_state: _Optional[_Union[OperationState, str]]=..., progress_documents: _Optional[_Union[Progress, _Mapping]]=..., progress_bytes: _Optional[_Union[Progress, _Mapping]]=..., collection_ids: _Optional[_Iterable[str]]=..., input_uri_prefix: _Optional[str]=...) -> None:
        ...