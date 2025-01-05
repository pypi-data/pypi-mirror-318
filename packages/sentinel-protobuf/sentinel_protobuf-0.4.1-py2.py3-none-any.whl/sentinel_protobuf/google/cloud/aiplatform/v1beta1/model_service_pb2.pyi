from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import evaluated_annotation_pb2 as _evaluated_annotation_pb2
from google.cloud.aiplatform.v1beta1 import explanation_pb2 as _explanation_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import model_pb2 as _model_pb2
from google.cloud.aiplatform.v1beta1 import model_evaluation_pb2 as _model_evaluation_pb2
from google.cloud.aiplatform.v1beta1 import model_evaluation_slice_pb2 as _model_evaluation_slice_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadModelRequest(_message.Message):
    __slots__ = ("parent", "parent_model", "model_id", "model", "service_account")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    parent_model: str
    model_id: str
    model: _model_pb2.Model
    service_account: str
    def __init__(self, parent: _Optional[str] = ..., parent_model: _Optional[str] = ..., model_id: _Optional[str] = ..., model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ..., service_account: _Optional[str] = ...) -> None: ...

class UploadModelOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class UploadModelResponse(_message.Message):
    __slots__ = ("model", "model_version_id")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    model: str
    model_version_id: str
    def __init__(self, model: _Optional[str] = ..., model_version_id: _Optional[str] = ...) -> None: ...

class GetModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models", "next_page_token")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model]
    next_page_token: str
    def __init__(self, models: _Optional[_Iterable[_Union[_model_pb2.Model, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListModelVersionsRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token", "filter", "read_mask", "order_by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    filter: str
    read_mask: _field_mask_pb2.FieldMask
    order_by: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListModelVersionsResponse(_message.Message):
    __slots__ = ("models", "next_page_token")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model]
    next_page_token: str
    def __init__(self, models: _Optional[_Iterable[_Union[_model_pb2.Model, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateModelRequest(_message.Message):
    __slots__ = ("model", "update_mask")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    model: _model_pb2.Model
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateExplanationDatasetRequest(_message.Message):
    __slots__ = ("model", "examples")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    model: str
    examples: _explanation_pb2.Examples
    def __init__(self, model: _Optional[str] = ..., examples: _Optional[_Union[_explanation_pb2.Examples, _Mapping]] = ...) -> None: ...

class UpdateExplanationDatasetOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class DeleteModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteModelVersionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class MergeVersionAliasesRequest(_message.Message):
    __slots__ = ("name", "version_aliases")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ALIASES_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., version_aliases: _Optional[_Iterable[str]] = ...) -> None: ...

class ExportModelRequest(_message.Message):
    __slots__ = ("name", "output_config")
    class OutputConfig(_message.Message):
        __slots__ = ("export_format_id", "artifact_destination", "image_destination")
        EXPORT_FORMAT_ID_FIELD_NUMBER: _ClassVar[int]
        ARTIFACT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        IMAGE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        export_format_id: str
        artifact_destination: _io_pb2.GcsDestination
        image_destination: _io_pb2.ContainerRegistryDestination
        def __init__(self, export_format_id: _Optional[str] = ..., artifact_destination: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]] = ..., image_destination: _Optional[_Union[_io_pb2.ContainerRegistryDestination, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: ExportModelRequest.OutputConfig
    def __init__(self, name: _Optional[str] = ..., output_config: _Optional[_Union[ExportModelRequest.OutputConfig, _Mapping]] = ...) -> None: ...

class ExportModelOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata", "output_info")
    class OutputInfo(_message.Message):
        __slots__ = ("artifact_output_uri", "image_output_uri")
        ARTIFACT_OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
        IMAGE_OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
        artifact_output_uri: str
        image_output_uri: str
        def __init__(self, artifact_output_uri: _Optional[str] = ..., image_output_uri: _Optional[str] = ...) -> None: ...
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_INFO_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    output_info: ExportModelOperationMetadata.OutputInfo
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ..., output_info: _Optional[_Union[ExportModelOperationMetadata.OutputInfo, _Mapping]] = ...) -> None: ...

class UpdateExplanationDatasetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyModelRequest(_message.Message):
    __slots__ = ("model_id", "parent_model", "parent", "source_model", "encryption_spec")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    parent_model: str
    parent: str
    source_model: str
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    def __init__(self, model_id: _Optional[str] = ..., parent_model: _Optional[str] = ..., parent: _Optional[str] = ..., source_model: _Optional[str] = ..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]] = ...) -> None: ...

class CopyModelOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class CopyModelResponse(_message.Message):
    __slots__ = ("model", "model_version_id")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    model: str
    model_version_id: str
    def __init__(self, model: _Optional[str] = ..., model_version_id: _Optional[str] = ...) -> None: ...

class ImportModelEvaluationRequest(_message.Message):
    __slots__ = ("parent", "model_evaluation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model_evaluation: _model_evaluation_pb2.ModelEvaluation
    def __init__(self, parent: _Optional[str] = ..., model_evaluation: _Optional[_Union[_model_evaluation_pb2.ModelEvaluation, _Mapping]] = ...) -> None: ...

class BatchImportModelEvaluationSlicesRequest(_message.Message):
    __slots__ = ("parent", "model_evaluation_slices")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_EVALUATION_SLICES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model_evaluation_slices: _containers.RepeatedCompositeFieldContainer[_model_evaluation_slice_pb2.ModelEvaluationSlice]
    def __init__(self, parent: _Optional[str] = ..., model_evaluation_slices: _Optional[_Iterable[_Union[_model_evaluation_slice_pb2.ModelEvaluationSlice, _Mapping]]] = ...) -> None: ...

class BatchImportModelEvaluationSlicesResponse(_message.Message):
    __slots__ = ("imported_model_evaluation_slices",)
    IMPORTED_MODEL_EVALUATION_SLICES_FIELD_NUMBER: _ClassVar[int]
    imported_model_evaluation_slices: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, imported_model_evaluation_slices: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchImportEvaluatedAnnotationsRequest(_message.Message):
    __slots__ = ("parent", "evaluated_annotations")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    evaluated_annotations: _containers.RepeatedCompositeFieldContainer[_evaluated_annotation_pb2.EvaluatedAnnotation]
    def __init__(self, parent: _Optional[str] = ..., evaluated_annotations: _Optional[_Iterable[_Union[_evaluated_annotation_pb2.EvaluatedAnnotation, _Mapping]]] = ...) -> None: ...

class BatchImportEvaluatedAnnotationsResponse(_message.Message):
    __slots__ = ("imported_evaluated_annotations_count",)
    IMPORTED_EVALUATED_ANNOTATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    imported_evaluated_annotations_count: int
    def __init__(self, imported_evaluated_annotations_count: _Optional[int] = ...) -> None: ...

class GetModelEvaluationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelEvaluationsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListModelEvaluationsResponse(_message.Message):
    __slots__ = ("model_evaluations", "next_page_token")
    MODEL_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_evaluations: _containers.RepeatedCompositeFieldContainer[_model_evaluation_pb2.ModelEvaluation]
    next_page_token: str
    def __init__(self, model_evaluations: _Optional[_Iterable[_Union[_model_evaluation_pb2.ModelEvaluation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetModelEvaluationSliceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelEvaluationSlicesRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListModelEvaluationSlicesResponse(_message.Message):
    __slots__ = ("model_evaluation_slices", "next_page_token")
    MODEL_EVALUATION_SLICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_evaluation_slices: _containers.RepeatedCompositeFieldContainer[_model_evaluation_slice_pb2.ModelEvaluationSlice]
    next_page_token: str
    def __init__(self, model_evaluation_slices: _Optional[_Iterable[_Union[_model_evaluation_slice_pb2.ModelEvaluationSlice, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
