from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import common_pb2 as _common_pb2
from google.cloud.contentwarehouse.v1 import pipelines_pb2 as _pipelines_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunPipelineRequest(_message.Message):
    __slots__ = ("name", "gcs_ingest_pipeline", "gcs_ingest_with_doc_ai_processors_pipeline", "export_cdw_pipeline", "process_with_doc_ai_pipeline", "request_metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GCS_INGEST_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    GCS_INGEST_WITH_DOC_AI_PROCESSORS_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CDW_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    PROCESS_WITH_DOC_AI_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    gcs_ingest_pipeline: _pipelines_pb2.GcsIngestPipeline
    gcs_ingest_with_doc_ai_processors_pipeline: _pipelines_pb2.GcsIngestWithDocAiProcessorsPipeline
    export_cdw_pipeline: _pipelines_pb2.ExportToCdwPipeline
    process_with_doc_ai_pipeline: _pipelines_pb2.ProcessWithDocAiPipeline
    request_metadata: _common_pb2.RequestMetadata
    def __init__(self, name: _Optional[str] = ..., gcs_ingest_pipeline: _Optional[_Union[_pipelines_pb2.GcsIngestPipeline, _Mapping]] = ..., gcs_ingest_with_doc_ai_processors_pipeline: _Optional[_Union[_pipelines_pb2.GcsIngestWithDocAiProcessorsPipeline, _Mapping]] = ..., export_cdw_pipeline: _Optional[_Union[_pipelines_pb2.ExportToCdwPipeline, _Mapping]] = ..., process_with_doc_ai_pipeline: _Optional[_Union[_pipelines_pb2.ProcessWithDocAiPipeline, _Mapping]] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
