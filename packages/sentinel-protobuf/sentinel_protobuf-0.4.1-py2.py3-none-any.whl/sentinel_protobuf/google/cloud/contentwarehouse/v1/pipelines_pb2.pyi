from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import common_pb2 as _common_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunPipelineResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RunPipelineMetadata(_message.Message):
    __slots__ = ("total_file_count", "failed_file_count", "user_info", "gcs_ingest_pipeline_metadata", "export_to_cdw_pipeline_metadata", "process_with_doc_ai_pipeline_metadata", "individual_document_statuses")
    class GcsIngestPipelineMetadata(_message.Message):
        __slots__ = ("input_path",)
        INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
        input_path: str
        def __init__(self, input_path: _Optional[str] = ...) -> None: ...
    class ExportToCdwPipelineMetadata(_message.Message):
        __slots__ = ("documents", "doc_ai_dataset", "output_path")
        DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        DOC_AI_DATASET_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
        documents: _containers.RepeatedScalarFieldContainer[str]
        doc_ai_dataset: str
        output_path: str
        def __init__(self, documents: _Optional[_Iterable[str]] = ..., doc_ai_dataset: _Optional[str] = ..., output_path: _Optional[str] = ...) -> None: ...
    class ProcessWithDocAiPipelineMetadata(_message.Message):
        __slots__ = ("documents", "processor_info")
        DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        PROCESSOR_INFO_FIELD_NUMBER: _ClassVar[int]
        documents: _containers.RepeatedScalarFieldContainer[str]
        processor_info: ProcessorInfo
        def __init__(self, documents: _Optional[_Iterable[str]] = ..., processor_info: _Optional[_Union[ProcessorInfo, _Mapping]] = ...) -> None: ...
    class IndividualDocumentStatus(_message.Message):
        __slots__ = ("document_id", "status")
        DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        document_id: str
        status: _status_pb2.Status
        def __init__(self, document_id: _Optional[str] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
    TOTAL_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    GCS_INGEST_PIPELINE_METADATA_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TO_CDW_PIPELINE_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROCESS_WITH_DOC_AI_PIPELINE_METADATA_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_DOCUMENT_STATUSES_FIELD_NUMBER: _ClassVar[int]
    total_file_count: int
    failed_file_count: int
    user_info: _common_pb2.UserInfo
    gcs_ingest_pipeline_metadata: RunPipelineMetadata.GcsIngestPipelineMetadata
    export_to_cdw_pipeline_metadata: RunPipelineMetadata.ExportToCdwPipelineMetadata
    process_with_doc_ai_pipeline_metadata: RunPipelineMetadata.ProcessWithDocAiPipelineMetadata
    individual_document_statuses: _containers.RepeatedCompositeFieldContainer[RunPipelineMetadata.IndividualDocumentStatus]
    def __init__(self, total_file_count: _Optional[int] = ..., failed_file_count: _Optional[int] = ..., user_info: _Optional[_Union[_common_pb2.UserInfo, _Mapping]] = ..., gcs_ingest_pipeline_metadata: _Optional[_Union[RunPipelineMetadata.GcsIngestPipelineMetadata, _Mapping]] = ..., export_to_cdw_pipeline_metadata: _Optional[_Union[RunPipelineMetadata.ExportToCdwPipelineMetadata, _Mapping]] = ..., process_with_doc_ai_pipeline_metadata: _Optional[_Union[RunPipelineMetadata.ProcessWithDocAiPipelineMetadata, _Mapping]] = ..., individual_document_statuses: _Optional[_Iterable[_Union[RunPipelineMetadata.IndividualDocumentStatus, _Mapping]]] = ...) -> None: ...

class ProcessorInfo(_message.Message):
    __slots__ = ("processor_name", "document_type", "schema_name")
    PROCESSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    processor_name: str
    document_type: str
    schema_name: str
    def __init__(self, processor_name: _Optional[str] = ..., document_type: _Optional[str] = ..., schema_name: _Optional[str] = ...) -> None: ...

class IngestPipelineConfig(_message.Message):
    __slots__ = ("document_acl_policy", "enable_document_text_extraction", "folder", "cloud_function")
    DOCUMENT_ACL_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DOCUMENT_TEXT_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    document_acl_policy: _policy_pb2.Policy
    enable_document_text_extraction: bool
    folder: str
    cloud_function: str
    def __init__(self, document_acl_policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., enable_document_text_extraction: bool = ..., folder: _Optional[str] = ..., cloud_function: _Optional[str] = ...) -> None: ...

class GcsIngestPipeline(_message.Message):
    __slots__ = ("input_path", "schema_name", "processor_type", "skip_ingested_documents", "pipeline_config")
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKIP_INGESTED_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    input_path: str
    schema_name: str
    processor_type: str
    skip_ingested_documents: bool
    pipeline_config: IngestPipelineConfig
    def __init__(self, input_path: _Optional[str] = ..., schema_name: _Optional[str] = ..., processor_type: _Optional[str] = ..., skip_ingested_documents: bool = ..., pipeline_config: _Optional[_Union[IngestPipelineConfig, _Mapping]] = ...) -> None: ...

class GcsIngestWithDocAiProcessorsPipeline(_message.Message):
    __slots__ = ("input_path", "split_classify_processor_info", "extract_processor_infos", "processor_results_folder_path", "skip_ingested_documents", "pipeline_config")
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    SPLIT_CLASSIFY_PROCESSOR_INFO_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_PROCESSOR_INFOS_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_RESULTS_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    SKIP_INGESTED_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    input_path: str
    split_classify_processor_info: ProcessorInfo
    extract_processor_infos: _containers.RepeatedCompositeFieldContainer[ProcessorInfo]
    processor_results_folder_path: str
    skip_ingested_documents: bool
    pipeline_config: IngestPipelineConfig
    def __init__(self, input_path: _Optional[str] = ..., split_classify_processor_info: _Optional[_Union[ProcessorInfo, _Mapping]] = ..., extract_processor_infos: _Optional[_Iterable[_Union[ProcessorInfo, _Mapping]]] = ..., processor_results_folder_path: _Optional[str] = ..., skip_ingested_documents: bool = ..., pipeline_config: _Optional[_Union[IngestPipelineConfig, _Mapping]] = ...) -> None: ...

class ExportToCdwPipeline(_message.Message):
    __slots__ = ("documents", "export_folder_path", "doc_ai_dataset", "training_split_ratio")
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    DOC_AI_DATASET_FIELD_NUMBER: _ClassVar[int]
    TRAINING_SPLIT_RATIO_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedScalarFieldContainer[str]
    export_folder_path: str
    doc_ai_dataset: str
    training_split_ratio: float
    def __init__(self, documents: _Optional[_Iterable[str]] = ..., export_folder_path: _Optional[str] = ..., doc_ai_dataset: _Optional[str] = ..., training_split_ratio: _Optional[float] = ...) -> None: ...

class ProcessWithDocAiPipeline(_message.Message):
    __slots__ = ("documents", "export_folder_path", "processor_info", "processor_results_folder_path")
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_INFO_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_RESULTS_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedScalarFieldContainer[str]
    export_folder_path: str
    processor_info: ProcessorInfo
    processor_results_folder_path: str
    def __init__(self, documents: _Optional[_Iterable[str]] = ..., export_folder_path: _Optional[str] = ..., processor_info: _Optional[_Union[ProcessorInfo, _Mapping]] = ..., processor_results_folder_path: _Optional[str] = ...) -> None: ...
