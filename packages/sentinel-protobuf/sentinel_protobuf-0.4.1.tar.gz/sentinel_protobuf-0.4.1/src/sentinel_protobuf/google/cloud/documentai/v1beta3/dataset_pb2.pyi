from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.documentai.v1beta3 import document_pb2 as _document_pb2
from google.cloud.documentai.v1beta3 import document_io_pb2 as _document_io_pb2
from google.cloud.documentai.v1beta3 import document_schema_pb2 as _document_schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Dataset(_message.Message):
    __slots__ = ('gcs_managed_config', 'document_warehouse_config', 'unmanaged_dataset_config', 'spanner_indexing_config', 'name', 'state', 'satisfies_pzs', 'satisfies_pzi')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Dataset.State]
        UNINITIALIZED: _ClassVar[Dataset.State]
        INITIALIZING: _ClassVar[Dataset.State]
        INITIALIZED: _ClassVar[Dataset.State]
    STATE_UNSPECIFIED: Dataset.State
    UNINITIALIZED: Dataset.State
    INITIALIZING: Dataset.State
    INITIALIZED: Dataset.State

    class GCSManagedConfig(_message.Message):
        __slots__ = ('gcs_prefix',)
        GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
        gcs_prefix: _document_io_pb2.GcsPrefix

        def __init__(self, gcs_prefix: _Optional[_Union[_document_io_pb2.GcsPrefix, _Mapping]]=...) -> None:
            ...

    class DocumentWarehouseConfig(_message.Message):
        __slots__ = ('collection', 'schema')
        COLLECTION_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        collection: str
        schema: str

        def __init__(self, collection: _Optional[str]=..., schema: _Optional[str]=...) -> None:
            ...

    class UnmanagedDatasetConfig(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class SpannerIndexingConfig(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    GCS_MANAGED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_WAREHOUSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UNMANAGED_DATASET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPANNER_INDEXING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    gcs_managed_config: Dataset.GCSManagedConfig
    document_warehouse_config: Dataset.DocumentWarehouseConfig
    unmanaged_dataset_config: Dataset.UnmanagedDatasetConfig
    spanner_indexing_config: Dataset.SpannerIndexingConfig
    name: str
    state: Dataset.State
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, gcs_managed_config: _Optional[_Union[Dataset.GCSManagedConfig, _Mapping]]=..., document_warehouse_config: _Optional[_Union[Dataset.DocumentWarehouseConfig, _Mapping]]=..., unmanaged_dataset_config: _Optional[_Union[Dataset.UnmanagedDatasetConfig, _Mapping]]=..., spanner_indexing_config: _Optional[_Union[Dataset.SpannerIndexingConfig, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[Dataset.State, str]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...

class DocumentId(_message.Message):
    __slots__ = ('gcs_managed_doc_id', 'unmanaged_doc_id', 'revision_ref')

    class GCSManagedDocumentId(_message.Message):
        __slots__ = ('gcs_uri', 'cw_doc_id')
        GCS_URI_FIELD_NUMBER: _ClassVar[int]
        CW_DOC_ID_FIELD_NUMBER: _ClassVar[int]
        gcs_uri: str
        cw_doc_id: str

        def __init__(self, gcs_uri: _Optional[str]=..., cw_doc_id: _Optional[str]=...) -> None:
            ...

    class UnmanagedDocumentId(_message.Message):
        __slots__ = ('doc_id',)
        DOC_ID_FIELD_NUMBER: _ClassVar[int]
        doc_id: str

        def __init__(self, doc_id: _Optional[str]=...) -> None:
            ...
    GCS_MANAGED_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    UNMANAGED_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_REF_FIELD_NUMBER: _ClassVar[int]
    gcs_managed_doc_id: DocumentId.GCSManagedDocumentId
    unmanaged_doc_id: DocumentId.UnmanagedDocumentId
    revision_ref: _document_pb2.RevisionRef

    def __init__(self, gcs_managed_doc_id: _Optional[_Union[DocumentId.GCSManagedDocumentId, _Mapping]]=..., unmanaged_doc_id: _Optional[_Union[DocumentId.UnmanagedDocumentId, _Mapping]]=..., revision_ref: _Optional[_Union[_document_pb2.RevisionRef, _Mapping]]=...) -> None:
        ...

class DatasetSchema(_message.Message):
    __slots__ = ('name', 'document_schema', 'satisfies_pzs', 'satisfies_pzi')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    document_schema: _document_schema_pb2.DocumentSchema
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., document_schema: _Optional[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...

class BatchDatasetDocuments(_message.Message):
    __slots__ = ('individual_document_ids', 'filter')

    class IndividualDocumentIds(_message.Message):
        __slots__ = ('document_ids',)
        DOCUMENT_IDS_FIELD_NUMBER: _ClassVar[int]
        document_ids: _containers.RepeatedCompositeFieldContainer[DocumentId]

        def __init__(self, document_ids: _Optional[_Iterable[_Union[DocumentId, _Mapping]]]=...) -> None:
            ...
    INDIVIDUAL_DOCUMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    individual_document_ids: BatchDatasetDocuments.IndividualDocumentIds
    filter: str

    def __init__(self, individual_document_ids: _Optional[_Union[BatchDatasetDocuments.IndividualDocumentIds, _Mapping]]=..., filter: _Optional[str]=...) -> None:
        ...