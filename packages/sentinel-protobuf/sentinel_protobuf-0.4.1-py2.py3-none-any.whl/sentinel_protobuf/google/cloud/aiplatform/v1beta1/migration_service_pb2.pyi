from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import migratable_resource_pb2 as _migratable_resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SearchMigratableResourcesRequest(_message.Message):
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

class SearchMigratableResourcesResponse(_message.Message):
    __slots__ = ('migratable_resources', 'next_page_token')
    MIGRATABLE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    migratable_resources: _containers.RepeatedCompositeFieldContainer[_migratable_resource_pb2.MigratableResource]
    next_page_token: str

    def __init__(self, migratable_resources: _Optional[_Iterable[_Union[_migratable_resource_pb2.MigratableResource, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BatchMigrateResourcesRequest(_message.Message):
    __slots__ = ('parent', 'migrate_resource_requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_RESOURCE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    migrate_resource_requests: _containers.RepeatedCompositeFieldContainer[MigrateResourceRequest]

    def __init__(self, parent: _Optional[str]=..., migrate_resource_requests: _Optional[_Iterable[_Union[MigrateResourceRequest, _Mapping]]]=...) -> None:
        ...

class MigrateResourceRequest(_message.Message):
    __slots__ = ('migrate_ml_engine_model_version_config', 'migrate_automl_model_config', 'migrate_automl_dataset_config', 'migrate_data_labeling_dataset_config')

    class MigrateMlEngineModelVersionConfig(_message.Message):
        __slots__ = ('endpoint', 'model_version', 'model_display_name')
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
        MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        model_version: str
        model_display_name: str

        def __init__(self, endpoint: _Optional[str]=..., model_version: _Optional[str]=..., model_display_name: _Optional[str]=...) -> None:
            ...

    class MigrateAutomlModelConfig(_message.Message):
        __slots__ = ('model', 'model_display_name')
        MODEL_FIELD_NUMBER: _ClassVar[int]
        MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        model: str
        model_display_name: str

        def __init__(self, model: _Optional[str]=..., model_display_name: _Optional[str]=...) -> None:
            ...

    class MigrateAutomlDatasetConfig(_message.Message):
        __slots__ = ('dataset', 'dataset_display_name')
        DATASET_FIELD_NUMBER: _ClassVar[int]
        DATASET_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        dataset_display_name: str

        def __init__(self, dataset: _Optional[str]=..., dataset_display_name: _Optional[str]=...) -> None:
            ...

    class MigrateDataLabelingDatasetConfig(_message.Message):
        __slots__ = ('dataset', 'dataset_display_name', 'migrate_data_labeling_annotated_dataset_configs')

        class MigrateDataLabelingAnnotatedDatasetConfig(_message.Message):
            __slots__ = ('annotated_dataset',)
            ANNOTATED_DATASET_FIELD_NUMBER: _ClassVar[int]
            annotated_dataset: str

            def __init__(self, annotated_dataset: _Optional[str]=...) -> None:
                ...
        DATASET_FIELD_NUMBER: _ClassVar[int]
        DATASET_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        MIGRATE_DATA_LABELING_ANNOTATED_DATASET_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        dataset_display_name: str
        migrate_data_labeling_annotated_dataset_configs: _containers.RepeatedCompositeFieldContainer[MigrateResourceRequest.MigrateDataLabelingDatasetConfig.MigrateDataLabelingAnnotatedDatasetConfig]

        def __init__(self, dataset: _Optional[str]=..., dataset_display_name: _Optional[str]=..., migrate_data_labeling_annotated_dataset_configs: _Optional[_Iterable[_Union[MigrateResourceRequest.MigrateDataLabelingDatasetConfig.MigrateDataLabelingAnnotatedDatasetConfig, _Mapping]]]=...) -> None:
            ...
    MIGRATE_ML_ENGINE_MODEL_VERSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_AUTOML_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_AUTOML_DATASET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_DATA_LABELING_DATASET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    migrate_ml_engine_model_version_config: MigrateResourceRequest.MigrateMlEngineModelVersionConfig
    migrate_automl_model_config: MigrateResourceRequest.MigrateAutomlModelConfig
    migrate_automl_dataset_config: MigrateResourceRequest.MigrateAutomlDatasetConfig
    migrate_data_labeling_dataset_config: MigrateResourceRequest.MigrateDataLabelingDatasetConfig

    def __init__(self, migrate_ml_engine_model_version_config: _Optional[_Union[MigrateResourceRequest.MigrateMlEngineModelVersionConfig, _Mapping]]=..., migrate_automl_model_config: _Optional[_Union[MigrateResourceRequest.MigrateAutomlModelConfig, _Mapping]]=..., migrate_automl_dataset_config: _Optional[_Union[MigrateResourceRequest.MigrateAutomlDatasetConfig, _Mapping]]=..., migrate_data_labeling_dataset_config: _Optional[_Union[MigrateResourceRequest.MigrateDataLabelingDatasetConfig, _Mapping]]=...) -> None:
        ...

class BatchMigrateResourcesResponse(_message.Message):
    __slots__ = ('migrate_resource_responses',)
    MIGRATE_RESOURCE_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    migrate_resource_responses: _containers.RepeatedCompositeFieldContainer[MigrateResourceResponse]

    def __init__(self, migrate_resource_responses: _Optional[_Iterable[_Union[MigrateResourceResponse, _Mapping]]]=...) -> None:
        ...

class MigrateResourceResponse(_message.Message):
    __slots__ = ('dataset', 'model', 'migratable_resource')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MIGRATABLE_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    model: str
    migratable_resource: _migratable_resource_pb2.MigratableResource

    def __init__(self, dataset: _Optional[str]=..., model: _Optional[str]=..., migratable_resource: _Optional[_Union[_migratable_resource_pb2.MigratableResource, _Mapping]]=...) -> None:
        ...

class BatchMigrateResourcesOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'partial_results')

    class PartialResult(_message.Message):
        __slots__ = ('error', 'model', 'dataset', 'request')
        ERROR_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        DATASET_FIELD_NUMBER: _ClassVar[int]
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        error: _status_pb2.Status
        model: str
        dataset: str
        request: MigrateResourceRequest

        def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., model: _Optional[str]=..., dataset: _Optional[str]=..., request: _Optional[_Union[MigrateResourceRequest, _Mapping]]=...) -> None:
            ...
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    partial_results: _containers.RepeatedCompositeFieldContainer[BatchMigrateResourcesOperationMetadata.PartialResult]

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., partial_results: _Optional[_Iterable[_Union[BatchMigrateResourcesOperationMetadata.PartialResult, _Mapping]]]=...) -> None:
        ...