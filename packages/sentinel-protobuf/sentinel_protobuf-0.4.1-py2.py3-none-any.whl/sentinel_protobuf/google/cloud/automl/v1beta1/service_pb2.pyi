from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.automl.v1beta1 import annotation_payload_pb2 as _annotation_payload_pb2
from google.cloud.automl.v1beta1 import annotation_spec_pb2 as _annotation_spec_pb2
from google.cloud.automl.v1beta1 import column_spec_pb2 as _column_spec_pb2
from google.cloud.automl.v1beta1 import dataset_pb2 as _dataset_pb2
from google.cloud.automl.v1beta1 import image_pb2 as _image_pb2
from google.cloud.automl.v1beta1 import io_pb2 as _io_pb2
from google.cloud.automl.v1beta1 import model_pb2 as _model_pb2
from google.cloud.automl.v1beta1 import model_evaluation_pb2 as _model_evaluation_pb2
from google.cloud.automl.v1beta1 import operations_pb2 as _operations_pb2
from google.cloud.automl.v1beta1 import table_spec_pb2 as _table_spec_pb2
from google.longrunning import operations_pb2 as _operations_pb2_1
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDatasetRequest(_message.Message):
    __slots__ = ('parent', 'dataset')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset: _dataset_pb2.Dataset

    def __init__(self, parent: _Optional[str]=..., dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=...) -> None:
        ...

class GetDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDatasetsRequest(_message.Message):
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

class ListDatasetsResponse(_message.Message):
    __slots__ = ('datasets', 'next_page_token')
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Dataset]
    next_page_token: str

    def __init__(self, datasets: _Optional[_Iterable[_Union[_dataset_pb2.Dataset, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateDatasetRequest(_message.Message):
    __slots__ = ('dataset', 'update_mask')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_pb2.Dataset
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ImportDataRequest(_message.Message):
    __slots__ = ('name', 'input_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_config: _io_pb2.InputConfig

    def __init__(self, name: _Optional[str]=..., input_config: _Optional[_Union[_io_pb2.InputConfig, _Mapping]]=...) -> None:
        ...

class ExportDataRequest(_message.Message):
    __slots__ = ('name', 'output_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: _io_pb2.OutputConfig

    def __init__(self, name: _Optional[str]=..., output_config: _Optional[_Union[_io_pb2.OutputConfig, _Mapping]]=...) -> None:
        ...

class GetAnnotationSpecRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetTableSpecRequest(_message.Message):
    __slots__ = ('name', 'field_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListTableSpecsRequest(_message.Message):
    __slots__ = ('parent', 'field_mask', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    field_mask: _field_mask_pb2.FieldMask
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTableSpecsResponse(_message.Message):
    __slots__ = ('table_specs', 'next_page_token')
    TABLE_SPECS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    table_specs: _containers.RepeatedCompositeFieldContainer[_table_spec_pb2.TableSpec]
    next_page_token: str

    def __init__(self, table_specs: _Optional[_Iterable[_Union[_table_spec_pb2.TableSpec, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateTableSpecRequest(_message.Message):
    __slots__ = ('table_spec', 'update_mask')
    TABLE_SPEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    table_spec: _table_spec_pb2.TableSpec
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, table_spec: _Optional[_Union[_table_spec_pb2.TableSpec, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetColumnSpecRequest(_message.Message):
    __slots__ = ('name', 'field_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListColumnSpecsRequest(_message.Message):
    __slots__ = ('parent', 'field_mask', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    field_mask: _field_mask_pb2.FieldMask
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListColumnSpecsResponse(_message.Message):
    __slots__ = ('column_specs', 'next_page_token')
    COLUMN_SPECS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    column_specs: _containers.RepeatedCompositeFieldContainer[_column_spec_pb2.ColumnSpec]
    next_page_token: str

    def __init__(self, column_specs: _Optional[_Iterable[_Union[_column_spec_pb2.ColumnSpec, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateColumnSpecRequest(_message.Message):
    __slots__ = ('column_spec', 'update_mask')
    COLUMN_SPEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    column_spec: _column_spec_pb2.ColumnSpec
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, column_spec: _Optional[_Union[_column_spec_pb2.ColumnSpec, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CreateModelRequest(_message.Message):
    __slots__ = ('parent', 'model')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model: _model_pb2.Model

    def __init__(self, parent: _Optional[str]=..., model: _Optional[_Union[_model_pb2.Model, _Mapping]]=...) -> None:
        ...

class GetModelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListModelsRequest(_message.Message):
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

class ListModelsResponse(_message.Message):
    __slots__ = ('model', 'next_page_token')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model]
    next_page_token: str

    def __init__(self, model: _Optional[_Iterable[_Union[_model_pb2.Model, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteModelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeployModelRequest(_message.Message):
    __slots__ = ('image_object_detection_model_deployment_metadata', 'image_classification_model_deployment_metadata', 'name')
    IMAGE_OBJECT_DETECTION_MODEL_DEPLOYMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CLASSIFICATION_MODEL_DEPLOYMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    image_object_detection_model_deployment_metadata: _image_pb2.ImageObjectDetectionModelDeploymentMetadata
    image_classification_model_deployment_metadata: _image_pb2.ImageClassificationModelDeploymentMetadata
    name: str

    def __init__(self, image_object_detection_model_deployment_metadata: _Optional[_Union[_image_pb2.ImageObjectDetectionModelDeploymentMetadata, _Mapping]]=..., image_classification_model_deployment_metadata: _Optional[_Union[_image_pb2.ImageClassificationModelDeploymentMetadata, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class UndeployModelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ExportModelRequest(_message.Message):
    __slots__ = ('name', 'output_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: _io_pb2.ModelExportOutputConfig

    def __init__(self, name: _Optional[str]=..., output_config: _Optional[_Union[_io_pb2.ModelExportOutputConfig, _Mapping]]=...) -> None:
        ...

class ExportEvaluatedExamplesRequest(_message.Message):
    __slots__ = ('name', 'output_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: _io_pb2.ExportEvaluatedExamplesOutputConfig

    def __init__(self, name: _Optional[str]=..., output_config: _Optional[_Union[_io_pb2.ExportEvaluatedExamplesOutputConfig, _Mapping]]=...) -> None:
        ...

class GetModelEvaluationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListModelEvaluationsRequest(_message.Message):
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

class ListModelEvaluationsResponse(_message.Message):
    __slots__ = ('model_evaluation', 'next_page_token')
    MODEL_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_evaluation: _containers.RepeatedCompositeFieldContainer[_model_evaluation_pb2.ModelEvaluation]
    next_page_token: str

    def __init__(self, model_evaluation: _Optional[_Iterable[_Union[_model_evaluation_pb2.ModelEvaluation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...