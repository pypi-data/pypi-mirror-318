from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.documentai.v1beta3 import dataset_pb2 as _dataset_pb2
from google.cloud.documentai.v1beta3 import document_pb2 as _document_pb2
from google.cloud.documentai.v1beta3 import document_io_pb2 as _document_io_pb2
from google.cloud.documentai.v1beta3 import operation_metadata_pb2 as _operation_metadata_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DatasetSplitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_SPLIT_TYPE_UNSPECIFIED: _ClassVar[DatasetSplitType]
    DATASET_SPLIT_TRAIN: _ClassVar[DatasetSplitType]
    DATASET_SPLIT_TEST: _ClassVar[DatasetSplitType]
    DATASET_SPLIT_UNASSIGNED: _ClassVar[DatasetSplitType]

class DocumentLabelingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOCUMENT_LABELING_STATE_UNSPECIFIED: _ClassVar[DocumentLabelingState]
    DOCUMENT_LABELED: _ClassVar[DocumentLabelingState]
    DOCUMENT_UNLABELED: _ClassVar[DocumentLabelingState]
    DOCUMENT_AUTO_LABELED: _ClassVar[DocumentLabelingState]
DATASET_SPLIT_TYPE_UNSPECIFIED: DatasetSplitType
DATASET_SPLIT_TRAIN: DatasetSplitType
DATASET_SPLIT_TEST: DatasetSplitType
DATASET_SPLIT_UNASSIGNED: DatasetSplitType
DOCUMENT_LABELING_STATE_UNSPECIFIED: DocumentLabelingState
DOCUMENT_LABELED: DocumentLabelingState
DOCUMENT_UNLABELED: DocumentLabelingState
DOCUMENT_AUTO_LABELED: DocumentLabelingState

class UpdateDatasetRequest(_message.Message):
    __slots__ = ('dataset', 'update_mask')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_pb2.Dataset
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateDatasetOperationMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class ImportDocumentsRequest(_message.Message):
    __slots__ = ('dataset', 'batch_documents_import_configs')

    class BatchDocumentsImportConfig(_message.Message):
        __slots__ = ('dataset_split', 'auto_split_config', 'batch_input_config')

        class AutoSplitConfig(_message.Message):
            __slots__ = ('training_split_ratio',)
            TRAINING_SPLIT_RATIO_FIELD_NUMBER: _ClassVar[int]
            training_split_ratio: float

            def __init__(self, training_split_ratio: _Optional[float]=...) -> None:
                ...
        DATASET_SPLIT_FIELD_NUMBER: _ClassVar[int]
        AUTO_SPLIT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        BATCH_INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        dataset_split: DatasetSplitType
        auto_split_config: ImportDocumentsRequest.BatchDocumentsImportConfig.AutoSplitConfig
        batch_input_config: _document_io_pb2.BatchDocumentsInputConfig

        def __init__(self, dataset_split: _Optional[_Union[DatasetSplitType, str]]=..., auto_split_config: _Optional[_Union[ImportDocumentsRequest.BatchDocumentsImportConfig.AutoSplitConfig, _Mapping]]=..., batch_input_config: _Optional[_Union[_document_io_pb2.BatchDocumentsInputConfig, _Mapping]]=...) -> None:
            ...
    DATASET_FIELD_NUMBER: _ClassVar[int]
    BATCH_DOCUMENTS_IMPORT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    batch_documents_import_configs: _containers.RepeatedCompositeFieldContainer[ImportDocumentsRequest.BatchDocumentsImportConfig]

    def __init__(self, dataset: _Optional[str]=..., batch_documents_import_configs: _Optional[_Iterable[_Union[ImportDocumentsRequest.BatchDocumentsImportConfig, _Mapping]]]=...) -> None:
        ...

class ImportDocumentsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ImportDocumentsMetadata(_message.Message):
    __slots__ = ('common_metadata', 'individual_import_statuses', 'import_config_validation_results', 'total_document_count')

    class IndividualImportStatus(_message.Message):
        __slots__ = ('input_gcs_source', 'status', 'output_document_id')
        INPUT_GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        input_gcs_source: str
        status: _status_pb2.Status
        output_document_id: _dataset_pb2.DocumentId

        def __init__(self, input_gcs_source: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., output_document_id: _Optional[_Union[_dataset_pb2.DocumentId, _Mapping]]=...) -> None:
            ...

    class ImportConfigValidationResult(_message.Message):
        __slots__ = ('input_gcs_source', 'status')
        INPUT_GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        input_gcs_source: str
        status: _status_pb2.Status

        def __init__(self, input_gcs_source: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_IMPORT_STATUSES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CONFIG_VALIDATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DOCUMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata
    individual_import_statuses: _containers.RepeatedCompositeFieldContainer[ImportDocumentsMetadata.IndividualImportStatus]
    import_config_validation_results: _containers.RepeatedCompositeFieldContainer[ImportDocumentsMetadata.ImportConfigValidationResult]
    total_document_count: int

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=..., individual_import_statuses: _Optional[_Iterable[_Union[ImportDocumentsMetadata.IndividualImportStatus, _Mapping]]]=..., import_config_validation_results: _Optional[_Iterable[_Union[ImportDocumentsMetadata.ImportConfigValidationResult, _Mapping]]]=..., total_document_count: _Optional[int]=...) -> None:
        ...

class GetDocumentRequest(_message.Message):
    __slots__ = ('dataset', 'document_id', 'read_mask', 'page_range')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    document_id: _dataset_pb2.DocumentId
    read_mask: _field_mask_pb2.FieldMask
    page_range: DocumentPageRange

    def __init__(self, dataset: _Optional[str]=..., document_id: _Optional[_Union[_dataset_pb2.DocumentId, _Mapping]]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., page_range: _Optional[_Union[DocumentPageRange, _Mapping]]=...) -> None:
        ...

class GetDocumentResponse(_message.Message):
    __slots__ = ('document',)
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document

    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]]=...) -> None:
        ...

class ListDocumentsRequest(_message.Message):
    __slots__ = ('dataset', 'page_size', 'page_token', 'filter', 'return_total_size', 'skip')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    RETURN_TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    page_size: int
    page_token: str
    filter: str
    return_total_size: bool
    skip: int

    def __init__(self, dataset: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., return_total_size: bool=..., skip: _Optional[int]=...) -> None:
        ...

class ListDocumentsResponse(_message.Message):
    __slots__ = ('document_metadata', 'next_page_token', 'total_size')
    DOCUMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    document_metadata: _containers.RepeatedCompositeFieldContainer[DocumentMetadata]
    next_page_token: str
    total_size: int

    def __init__(self, document_metadata: _Optional[_Iterable[_Union[DocumentMetadata, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class BatchDeleteDocumentsRequest(_message.Message):
    __slots__ = ('dataset', 'dataset_documents')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    DATASET_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    dataset_documents: _dataset_pb2.BatchDatasetDocuments

    def __init__(self, dataset: _Optional[str]=..., dataset_documents: _Optional[_Union[_dataset_pb2.BatchDatasetDocuments, _Mapping]]=...) -> None:
        ...

class BatchDeleteDocumentsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class BatchDeleteDocumentsMetadata(_message.Message):
    __slots__ = ('common_metadata', 'individual_batch_delete_statuses', 'total_document_count', 'error_document_count')

    class IndividualBatchDeleteStatus(_message.Message):
        __slots__ = ('document_id', 'status')
        DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        document_id: _dataset_pb2.DocumentId
        status: _status_pb2.Status

        def __init__(self, document_id: _Optional[_Union[_dataset_pb2.DocumentId, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_BATCH_DELETE_STATUSES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DOCUMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_DOCUMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata
    individual_batch_delete_statuses: _containers.RepeatedCompositeFieldContainer[BatchDeleteDocumentsMetadata.IndividualBatchDeleteStatus]
    total_document_count: int
    error_document_count: int

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=..., individual_batch_delete_statuses: _Optional[_Iterable[_Union[BatchDeleteDocumentsMetadata.IndividualBatchDeleteStatus, _Mapping]]]=..., total_document_count: _Optional[int]=..., error_document_count: _Optional[int]=...) -> None:
        ...

class GetDatasetSchemaRequest(_message.Message):
    __slots__ = ('name', 'visible_fields_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELDS_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    visible_fields_only: bool

    def __init__(self, name: _Optional[str]=..., visible_fields_only: bool=...) -> None:
        ...

class UpdateDatasetSchemaRequest(_message.Message):
    __slots__ = ('dataset_schema', 'update_mask')
    DATASET_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dataset_schema: _dataset_pb2.DatasetSchema
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dataset_schema: _Optional[_Union[_dataset_pb2.DatasetSchema, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DocumentPageRange(_message.Message):
    __slots__ = ('start', 'end')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int

    def __init__(self, start: _Optional[int]=..., end: _Optional[int]=...) -> None:
        ...

class DocumentMetadata(_message.Message):
    __slots__ = ('document_id', 'page_count', 'dataset_type', 'labeling_state', 'display_name')
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATASET_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELING_STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    document_id: _dataset_pb2.DocumentId
    page_count: int
    dataset_type: DatasetSplitType
    labeling_state: DocumentLabelingState
    display_name: str

    def __init__(self, document_id: _Optional[_Union[_dataset_pb2.DocumentId, _Mapping]]=..., page_count: _Optional[int]=..., dataset_type: _Optional[_Union[DatasetSplitType, str]]=..., labeling_state: _Optional[_Union[DocumentLabelingState, str]]=..., display_name: _Optional[str]=...) -> None:
        ...