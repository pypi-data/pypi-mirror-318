from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.documentai.v1beta3 import document_pb2 as _document_pb2
from google.cloud.documentai.v1beta3 import document_io_pb2 as _document_io_pb2
from google.cloud.documentai.v1beta3 import document_schema_pb2 as _document_schema_pb2
from google.cloud.documentai.v1beta3 import evaluation_pb2 as _evaluation_pb2
from google.cloud.documentai.v1beta3 import operation_metadata_pb2 as _operation_metadata_pb2
from google.cloud.documentai.v1beta3 import processor_pb2 as _processor_pb2
from google.cloud.documentai.v1beta3 import processor_type_pb2 as _processor_type_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProcessOptions(_message.Message):
    __slots__ = ('individual_page_selector', 'from_start', 'from_end', 'ocr_config', 'layout_config', 'schema_override')

    class LayoutConfig(_message.Message):
        __slots__ = ('chunking_config',)

        class ChunkingConfig(_message.Message):
            __slots__ = ('chunk_size', 'include_ancestor_headings', 'semantic_chunking_group_size', 'breakpoint_percentile_threshold')
            CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_ANCESTOR_HEADINGS_FIELD_NUMBER: _ClassVar[int]
            SEMANTIC_CHUNKING_GROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
            BREAKPOINT_PERCENTILE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            chunk_size: int
            include_ancestor_headings: bool
            semantic_chunking_group_size: bool
            breakpoint_percentile_threshold: int

            def __init__(self, chunk_size: _Optional[int]=..., include_ancestor_headings: bool=..., semantic_chunking_group_size: bool=..., breakpoint_percentile_threshold: _Optional[int]=...) -> None:
                ...
        CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        chunking_config: ProcessOptions.LayoutConfig.ChunkingConfig

        def __init__(self, chunking_config: _Optional[_Union[ProcessOptions.LayoutConfig.ChunkingConfig, _Mapping]]=...) -> None:
            ...

    class IndividualPageSelector(_message.Message):
        __slots__ = ('pages',)
        PAGES_FIELD_NUMBER: _ClassVar[int]
        pages: _containers.RepeatedScalarFieldContainer[int]

        def __init__(self, pages: _Optional[_Iterable[int]]=...) -> None:
            ...
    INDIVIDUAL_PAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    FROM_START_FIELD_NUMBER: _ClassVar[int]
    FROM_END_FIELD_NUMBER: _ClassVar[int]
    OCR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    individual_page_selector: ProcessOptions.IndividualPageSelector
    from_start: int
    from_end: int
    ocr_config: _document_io_pb2.OcrConfig
    layout_config: ProcessOptions.LayoutConfig
    schema_override: _document_schema_pb2.DocumentSchema

    def __init__(self, individual_page_selector: _Optional[_Union[ProcessOptions.IndividualPageSelector, _Mapping]]=..., from_start: _Optional[int]=..., from_end: _Optional[int]=..., ocr_config: _Optional[_Union[_document_io_pb2.OcrConfig, _Mapping]]=..., layout_config: _Optional[_Union[ProcessOptions.LayoutConfig, _Mapping]]=..., schema_override: _Optional[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]=...) -> None:
        ...

class ProcessRequest(_message.Message):
    __slots__ = ('inline_document', 'raw_document', 'gcs_document', 'name', 'document', 'skip_human_review', 'field_mask', 'process_options', 'labels', 'imageless_mode')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    INLINE_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    RAW_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    GCS_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    SKIP_HUMAN_REVIEW_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    PROCESS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    IMAGELESS_MODE_FIELD_NUMBER: _ClassVar[int]
    inline_document: _document_pb2.Document
    raw_document: _document_io_pb2.RawDocument
    gcs_document: _document_io_pb2.GcsDocument
    name: str
    document: _document_pb2.Document
    skip_human_review: bool
    field_mask: _field_mask_pb2.FieldMask
    process_options: ProcessOptions
    labels: _containers.ScalarMap[str, str]
    imageless_mode: bool

    def __init__(self, inline_document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., raw_document: _Optional[_Union[_document_io_pb2.RawDocument, _Mapping]]=..., gcs_document: _Optional[_Union[_document_io_pb2.GcsDocument, _Mapping]]=..., name: _Optional[str]=..., document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., skip_human_review: bool=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., process_options: _Optional[_Union[ProcessOptions, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., imageless_mode: bool=...) -> None:
        ...

class HumanReviewStatus(_message.Message):
    __slots__ = ('state', 'state_message', 'human_review_operation')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[HumanReviewStatus.State]
        SKIPPED: _ClassVar[HumanReviewStatus.State]
        VALIDATION_PASSED: _ClassVar[HumanReviewStatus.State]
        IN_PROGRESS: _ClassVar[HumanReviewStatus.State]
        ERROR: _ClassVar[HumanReviewStatus.State]
    STATE_UNSPECIFIED: HumanReviewStatus.State
    SKIPPED: HumanReviewStatus.State
    VALIDATION_PASSED: HumanReviewStatus.State
    IN_PROGRESS: HumanReviewStatus.State
    ERROR: HumanReviewStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMAN_REVIEW_OPERATION_FIELD_NUMBER: _ClassVar[int]
    state: HumanReviewStatus.State
    state_message: str
    human_review_operation: str

    def __init__(self, state: _Optional[_Union[HumanReviewStatus.State, str]]=..., state_message: _Optional[str]=..., human_review_operation: _Optional[str]=...) -> None:
        ...

class ProcessResponse(_message.Message):
    __slots__ = ('document', 'human_review_operation', 'human_review_status')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    HUMAN_REVIEW_OPERATION_FIELD_NUMBER: _ClassVar[int]
    HUMAN_REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    human_review_operation: str
    human_review_status: HumanReviewStatus

    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., human_review_operation: _Optional[str]=..., human_review_status: _Optional[_Union[HumanReviewStatus, _Mapping]]=...) -> None:
        ...

class BatchProcessRequest(_message.Message):
    __slots__ = ('name', 'input_configs', 'output_config', 'input_documents', 'document_output_config', 'skip_human_review', 'process_options', 'labels')

    class BatchInputConfig(_message.Message):
        __slots__ = ('gcs_source', 'mime_type')
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        gcs_source: str
        mime_type: str

        def __init__(self, gcs_source: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
            ...

    class BatchOutputConfig(_message.Message):
        __slots__ = ('gcs_destination',)
        GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        gcs_destination: str

        def __init__(self, gcs_destination: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SKIP_HUMAN_REVIEW_FIELD_NUMBER: _ClassVar[int]
    PROCESS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_configs: _containers.RepeatedCompositeFieldContainer[BatchProcessRequest.BatchInputConfig]
    output_config: BatchProcessRequest.BatchOutputConfig
    input_documents: _document_io_pb2.BatchDocumentsInputConfig
    document_output_config: _document_io_pb2.DocumentOutputConfig
    skip_human_review: bool
    process_options: ProcessOptions
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., input_configs: _Optional[_Iterable[_Union[BatchProcessRequest.BatchInputConfig, _Mapping]]]=..., output_config: _Optional[_Union[BatchProcessRequest.BatchOutputConfig, _Mapping]]=..., input_documents: _Optional[_Union[_document_io_pb2.BatchDocumentsInputConfig, _Mapping]]=..., document_output_config: _Optional[_Union[_document_io_pb2.DocumentOutputConfig, _Mapping]]=..., skip_human_review: bool=..., process_options: _Optional[_Union[ProcessOptions, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BatchProcessResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class BatchProcessMetadata(_message.Message):
    __slots__ = ('state', 'state_message', 'create_time', 'update_time', 'individual_process_statuses')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchProcessMetadata.State]
        WAITING: _ClassVar[BatchProcessMetadata.State]
        RUNNING: _ClassVar[BatchProcessMetadata.State]
        SUCCEEDED: _ClassVar[BatchProcessMetadata.State]
        CANCELLING: _ClassVar[BatchProcessMetadata.State]
        CANCELLED: _ClassVar[BatchProcessMetadata.State]
        FAILED: _ClassVar[BatchProcessMetadata.State]
    STATE_UNSPECIFIED: BatchProcessMetadata.State
    WAITING: BatchProcessMetadata.State
    RUNNING: BatchProcessMetadata.State
    SUCCEEDED: BatchProcessMetadata.State
    CANCELLING: BatchProcessMetadata.State
    CANCELLED: BatchProcessMetadata.State
    FAILED: BatchProcessMetadata.State

    class IndividualProcessStatus(_message.Message):
        __slots__ = ('input_gcs_source', 'status', 'output_gcs_destination', 'human_review_operation', 'human_review_status')
        INPUT_GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        HUMAN_REVIEW_OPERATION_FIELD_NUMBER: _ClassVar[int]
        HUMAN_REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
        input_gcs_source: str
        status: _status_pb2.Status
        output_gcs_destination: str
        human_review_operation: str
        human_review_status: HumanReviewStatus

        def __init__(self, input_gcs_source: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., output_gcs_destination: _Optional[str]=..., human_review_operation: _Optional[str]=..., human_review_status: _Optional[_Union[HumanReviewStatus, _Mapping]]=...) -> None:
            ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_PROCESS_STATUSES_FIELD_NUMBER: _ClassVar[int]
    state: BatchProcessMetadata.State
    state_message: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    individual_process_statuses: _containers.RepeatedCompositeFieldContainer[BatchProcessMetadata.IndividualProcessStatus]

    def __init__(self, state: _Optional[_Union[BatchProcessMetadata.State, str]]=..., state_message: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., individual_process_statuses: _Optional[_Iterable[_Union[BatchProcessMetadata.IndividualProcessStatus, _Mapping]]]=...) -> None:
        ...

class FetchProcessorTypesRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class FetchProcessorTypesResponse(_message.Message):
    __slots__ = ('processor_types',)
    PROCESSOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    processor_types: _containers.RepeatedCompositeFieldContainer[_processor_type_pb2.ProcessorType]

    def __init__(self, processor_types: _Optional[_Iterable[_Union[_processor_type_pb2.ProcessorType, _Mapping]]]=...) -> None:
        ...

class ListProcessorTypesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProcessorTypesResponse(_message.Message):
    __slots__ = ('processor_types', 'next_page_token')
    PROCESSOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    processor_types: _containers.RepeatedCompositeFieldContainer[_processor_type_pb2.ProcessorType]
    next_page_token: str

    def __init__(self, processor_types: _Optional[_Iterable[_Union[_processor_type_pb2.ProcessorType, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListProcessorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProcessorsResponse(_message.Message):
    __slots__ = ('processors', 'next_page_token')
    PROCESSORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    processors: _containers.RepeatedCompositeFieldContainer[_processor_pb2.Processor]
    next_page_token: str

    def __init__(self, processors: _Optional[_Iterable[_Union[_processor_pb2.Processor, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetProcessorTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetProcessorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetProcessorVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListProcessorVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProcessorVersionsResponse(_message.Message):
    __slots__ = ('processor_versions', 'next_page_token')
    PROCESSOR_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    processor_versions: _containers.RepeatedCompositeFieldContainer[_processor_pb2.ProcessorVersion]
    next_page_token: str

    def __init__(self, processor_versions: _Optional[_Iterable[_Union[_processor_pb2.ProcessorVersion, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteProcessorVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteProcessorVersionMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class DeployProcessorVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeployProcessorVersionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeployProcessorVersionMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class UndeployProcessorVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeployProcessorVersionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UndeployProcessorVersionMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class CreateProcessorRequest(_message.Message):
    __slots__ = ('parent', 'processor')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    processor: _processor_pb2.Processor

    def __init__(self, parent: _Optional[str]=..., processor: _Optional[_Union[_processor_pb2.Processor, _Mapping]]=...) -> None:
        ...

class DeleteProcessorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteProcessorMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class EnableProcessorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EnableProcessorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnableProcessorMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class DisableProcessorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DisableProcessorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DisableProcessorMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class SetDefaultProcessorVersionRequest(_message.Message):
    __slots__ = ('processor', 'default_processor_version')
    PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    processor: str
    default_processor_version: str

    def __init__(self, processor: _Optional[str]=..., default_processor_version: _Optional[str]=...) -> None:
        ...

class SetDefaultProcessorVersionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SetDefaultProcessorVersionMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class TrainProcessorVersionRequest(_message.Message):
    __slots__ = ('custom_document_extraction_options', 'foundation_model_tuning_options', 'parent', 'processor_version', 'document_schema', 'input_data', 'base_processor_version')

    class InputData(_message.Message):
        __slots__ = ('training_documents', 'test_documents')
        TRAINING_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        TEST_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        training_documents: _document_io_pb2.BatchDocumentsInputConfig
        test_documents: _document_io_pb2.BatchDocumentsInputConfig

        def __init__(self, training_documents: _Optional[_Union[_document_io_pb2.BatchDocumentsInputConfig, _Mapping]]=..., test_documents: _Optional[_Union[_document_io_pb2.BatchDocumentsInputConfig, _Mapping]]=...) -> None:
            ...

    class CustomDocumentExtractionOptions(_message.Message):
        __slots__ = ('training_method',)

        class TrainingMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TRAINING_METHOD_UNSPECIFIED: _ClassVar[TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod]
            MODEL_BASED: _ClassVar[TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod]
            TEMPLATE_BASED: _ClassVar[TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod]
        TRAINING_METHOD_UNSPECIFIED: TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod
        MODEL_BASED: TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod
        TEMPLATE_BASED: TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod
        TRAINING_METHOD_FIELD_NUMBER: _ClassVar[int]
        training_method: TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod

        def __init__(self, training_method: _Optional[_Union[TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod, str]]=...) -> None:
            ...

    class FoundationModelTuningOptions(_message.Message):
        __slots__ = ('train_steps', 'learning_rate_multiplier')
        TRAIN_STEPS_FIELD_NUMBER: _ClassVar[int]
        LEARNING_RATE_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        train_steps: int
        learning_rate_multiplier: float

        def __init__(self, train_steps: _Optional[int]=..., learning_rate_multiplier: _Optional[float]=...) -> None:
            ...
    CUSTOM_DOCUMENT_EXTRACTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FOUNDATION_MODEL_TUNING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    BASE_PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    custom_document_extraction_options: TrainProcessorVersionRequest.CustomDocumentExtractionOptions
    foundation_model_tuning_options: TrainProcessorVersionRequest.FoundationModelTuningOptions
    parent: str
    processor_version: _processor_pb2.ProcessorVersion
    document_schema: _document_schema_pb2.DocumentSchema
    input_data: TrainProcessorVersionRequest.InputData
    base_processor_version: str

    def __init__(self, custom_document_extraction_options: _Optional[_Union[TrainProcessorVersionRequest.CustomDocumentExtractionOptions, _Mapping]]=..., foundation_model_tuning_options: _Optional[_Union[TrainProcessorVersionRequest.FoundationModelTuningOptions, _Mapping]]=..., parent: _Optional[str]=..., processor_version: _Optional[_Union[_processor_pb2.ProcessorVersion, _Mapping]]=..., document_schema: _Optional[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]=..., input_data: _Optional[_Union[TrainProcessorVersionRequest.InputData, _Mapping]]=..., base_processor_version: _Optional[str]=...) -> None:
        ...

class TrainProcessorVersionResponse(_message.Message):
    __slots__ = ('processor_version',)
    PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    processor_version: str

    def __init__(self, processor_version: _Optional[str]=...) -> None:
        ...

class TrainProcessorVersionMetadata(_message.Message):
    __slots__ = ('common_metadata', 'training_dataset_validation', 'test_dataset_validation')

    class DatasetValidation(_message.Message):
        __slots__ = ('document_error_count', 'dataset_error_count', 'document_errors', 'dataset_errors')
        DOCUMENT_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        DATASET_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_ERRORS_FIELD_NUMBER: _ClassVar[int]
        DATASET_ERRORS_FIELD_NUMBER: _ClassVar[int]
        document_error_count: int
        dataset_error_count: int
        document_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
        dataset_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

        def __init__(self, document_error_count: _Optional[int]=..., dataset_error_count: _Optional[int]=..., document_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., dataset_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
            ...
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DATASET_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    TEST_DATASET_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata
    training_dataset_validation: TrainProcessorVersionMetadata.DatasetValidation
    test_dataset_validation: TrainProcessorVersionMetadata.DatasetValidation

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=..., training_dataset_validation: _Optional[_Union[TrainProcessorVersionMetadata.DatasetValidation, _Mapping]]=..., test_dataset_validation: _Optional[_Union[TrainProcessorVersionMetadata.DatasetValidation, _Mapping]]=...) -> None:
        ...

class ReviewDocumentRequest(_message.Message):
    __slots__ = ('inline_document', 'human_review_config', 'document', 'enable_schema_validation', 'priority', 'document_schema')

    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ReviewDocumentRequest.Priority]
        URGENT: _ClassVar[ReviewDocumentRequest.Priority]
    DEFAULT: ReviewDocumentRequest.Priority
    URGENT: ReviewDocumentRequest.Priority
    INLINE_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    HUMAN_REVIEW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SCHEMA_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    inline_document: _document_pb2.Document
    human_review_config: str
    document: _document_pb2.Document
    enable_schema_validation: bool
    priority: ReviewDocumentRequest.Priority
    document_schema: _document_schema_pb2.DocumentSchema

    def __init__(self, inline_document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., human_review_config: _Optional[str]=..., document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., enable_schema_validation: bool=..., priority: _Optional[_Union[ReviewDocumentRequest.Priority, str]]=..., document_schema: _Optional[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]=...) -> None:
        ...

class ReviewDocumentResponse(_message.Message):
    __slots__ = ('gcs_destination', 'state', 'rejection_reason')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ReviewDocumentResponse.State]
        REJECTED: _ClassVar[ReviewDocumentResponse.State]
        SUCCEEDED: _ClassVar[ReviewDocumentResponse.State]
    STATE_UNSPECIFIED: ReviewDocumentResponse.State
    REJECTED: ReviewDocumentResponse.State
    SUCCEEDED: ReviewDocumentResponse.State
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: str
    state: ReviewDocumentResponse.State
    rejection_reason: str

    def __init__(self, gcs_destination: _Optional[str]=..., state: _Optional[_Union[ReviewDocumentResponse.State, str]]=..., rejection_reason: _Optional[str]=...) -> None:
        ...

class ReviewDocumentOperationMetadata(_message.Message):
    __slots__ = ('state', 'state_message', 'create_time', 'update_time', 'common_metadata', 'question_id')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ReviewDocumentOperationMetadata.State]
        RUNNING: _ClassVar[ReviewDocumentOperationMetadata.State]
        CANCELLING: _ClassVar[ReviewDocumentOperationMetadata.State]
        SUCCEEDED: _ClassVar[ReviewDocumentOperationMetadata.State]
        FAILED: _ClassVar[ReviewDocumentOperationMetadata.State]
        CANCELLED: _ClassVar[ReviewDocumentOperationMetadata.State]
    STATE_UNSPECIFIED: ReviewDocumentOperationMetadata.State
    RUNNING: ReviewDocumentOperationMetadata.State
    CANCELLING: ReviewDocumentOperationMetadata.State
    SUCCEEDED: ReviewDocumentOperationMetadata.State
    FAILED: ReviewDocumentOperationMetadata.State
    CANCELLED: ReviewDocumentOperationMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    state: ReviewDocumentOperationMetadata.State
    state_message: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata
    question_id: str

    def __init__(self, state: _Optional[_Union[ReviewDocumentOperationMetadata.State, str]]=..., state_message: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=..., question_id: _Optional[str]=...) -> None:
        ...

class EvaluateProcessorVersionRequest(_message.Message):
    __slots__ = ('processor_version', 'evaluation_documents')
    PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    processor_version: str
    evaluation_documents: _document_io_pb2.BatchDocumentsInputConfig

    def __init__(self, processor_version: _Optional[str]=..., evaluation_documents: _Optional[_Union[_document_io_pb2.BatchDocumentsInputConfig, _Mapping]]=...) -> None:
        ...

class EvaluateProcessorVersionMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class EvaluateProcessorVersionResponse(_message.Message):
    __slots__ = ('evaluation',)
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: str

    def __init__(self, evaluation: _Optional[str]=...) -> None:
        ...

class GetEvaluationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEvaluationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEvaluationsResponse(_message.Message):
    __slots__ = ('evaluations', 'next_page_token')
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[_evaluation_pb2.Evaluation]
    next_page_token: str

    def __init__(self, evaluations: _Optional[_Iterable[_Union[_evaluation_pb2.Evaluation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ImportProcessorVersionRequest(_message.Message):
    __slots__ = ('processor_version_source', 'external_processor_version_source', 'parent')

    class ExternalProcessorVersionSource(_message.Message):
        __slots__ = ('processor_version', 'service_endpoint')
        PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        processor_version: str
        service_endpoint: str

        def __init__(self, processor_version: _Optional[str]=..., service_endpoint: _Optional[str]=...) -> None:
            ...
    PROCESSOR_VERSION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PROCESSOR_VERSION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    processor_version_source: str
    external_processor_version_source: ImportProcessorVersionRequest.ExternalProcessorVersionSource
    parent: str

    def __init__(self, processor_version_source: _Optional[str]=..., external_processor_version_source: _Optional[_Union[ImportProcessorVersionRequest.ExternalProcessorVersionSource, _Mapping]]=..., parent: _Optional[str]=...) -> None:
        ...

class ImportProcessorVersionResponse(_message.Message):
    __slots__ = ('processor_version',)
    PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    processor_version: str

    def __init__(self, processor_version: _Optional[str]=...) -> None:
        ...

class ImportProcessorVersionMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...