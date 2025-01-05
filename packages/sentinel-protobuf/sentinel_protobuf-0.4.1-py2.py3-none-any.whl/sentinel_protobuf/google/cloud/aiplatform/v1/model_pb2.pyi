from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import deployed_model_ref_pb2 as _deployed_model_ref_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import env_var_pb2 as _env_var_pb2
from google.cloud.aiplatform.v1 import explanation_pb2 as _explanation_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Model(_message.Message):
    __slots__ = ("name", "version_id", "version_aliases", "version_create_time", "version_update_time", "display_name", "description", "version_description", "predict_schemata", "metadata_schema_uri", "metadata", "supported_export_formats", "training_pipeline", "pipeline_job", "container_spec", "artifact_uri", "supported_deployment_resources_types", "supported_input_storage_formats", "supported_output_storage_formats", "create_time", "update_time", "deployed_models", "explanation_spec", "etag", "labels", "data_stats", "encryption_spec", "model_source_info", "original_model_info", "metadata_artifact", "base_model_source", "satisfies_pzs", "satisfies_pzi")
    class DeploymentResourcesType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED: _ClassVar[Model.DeploymentResourcesType]
        DEDICATED_RESOURCES: _ClassVar[Model.DeploymentResourcesType]
        AUTOMATIC_RESOURCES: _ClassVar[Model.DeploymentResourcesType]
        SHARED_RESOURCES: _ClassVar[Model.DeploymentResourcesType]
    DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED: Model.DeploymentResourcesType
    DEDICATED_RESOURCES: Model.DeploymentResourcesType
    AUTOMATIC_RESOURCES: Model.DeploymentResourcesType
    SHARED_RESOURCES: Model.DeploymentResourcesType
    class ExportFormat(_message.Message):
        __slots__ = ("id", "exportable_contents")
        class ExportableContent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EXPORTABLE_CONTENT_UNSPECIFIED: _ClassVar[Model.ExportFormat.ExportableContent]
            ARTIFACT: _ClassVar[Model.ExportFormat.ExportableContent]
            IMAGE: _ClassVar[Model.ExportFormat.ExportableContent]
        EXPORTABLE_CONTENT_UNSPECIFIED: Model.ExportFormat.ExportableContent
        ARTIFACT: Model.ExportFormat.ExportableContent
        IMAGE: Model.ExportFormat.ExportableContent
        ID_FIELD_NUMBER: _ClassVar[int]
        EXPORTABLE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
        id: str
        exportable_contents: _containers.RepeatedScalarFieldContainer[Model.ExportFormat.ExportableContent]
        def __init__(self, id: _Optional[str] = ..., exportable_contents: _Optional[_Iterable[_Union[Model.ExportFormat.ExportableContent, str]]] = ...) -> None: ...
    class DataStats(_message.Message):
        __slots__ = ("training_data_items_count", "validation_data_items_count", "test_data_items_count", "training_annotations_count", "validation_annotations_count", "test_annotations_count")
        TRAINING_DATA_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_DATA_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
        TEST_DATA_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
        TRAINING_ANNOTATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_ANNOTATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        TEST_ANNOTATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        training_data_items_count: int
        validation_data_items_count: int
        test_data_items_count: int
        training_annotations_count: int
        validation_annotations_count: int
        test_annotations_count: int
        def __init__(self, training_data_items_count: _Optional[int] = ..., validation_data_items_count: _Optional[int] = ..., test_data_items_count: _Optional[int] = ..., training_annotations_count: _Optional[int] = ..., validation_annotations_count: _Optional[int] = ..., test_annotations_count: _Optional[int] = ...) -> None: ...
    class OriginalModelInfo(_message.Message):
        __slots__ = ("model",)
        MODEL_FIELD_NUMBER: _ClassVar[int]
        model: str
        def __init__(self, model: _Optional[str] = ...) -> None: ...
    class BaseModelSource(_message.Message):
        __slots__ = ("model_garden_source", "genie_source")
        MODEL_GARDEN_SOURCE_FIELD_NUMBER: _ClassVar[int]
        GENIE_SOURCE_FIELD_NUMBER: _ClassVar[int]
        model_garden_source: ModelGardenSource
        genie_source: GenieSource
        def __init__(self, model_garden_source: _Optional[_Union[ModelGardenSource, _Mapping]] = ..., genie_source: _Optional[_Union[GenieSource, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ALIASES_FIELD_NUMBER: _ClassVar[int]
    VERSION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PREDICT_SCHEMATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_EXPORT_FORMATS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_JOB_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_SPEC_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_DEPLOYMENT_RESOURCES_TYPES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_INPUT_STORAGE_FORMATS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_OUTPUT_STORAGE_FORMATS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODELS_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    MODEL_SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
    METADATA_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_id: str
    version_aliases: _containers.RepeatedScalarFieldContainer[str]
    version_create_time: _timestamp_pb2.Timestamp
    version_update_time: _timestamp_pb2.Timestamp
    display_name: str
    description: str
    version_description: str
    predict_schemata: PredictSchemata
    metadata_schema_uri: str
    metadata: _struct_pb2.Value
    supported_export_formats: _containers.RepeatedCompositeFieldContainer[Model.ExportFormat]
    training_pipeline: str
    pipeline_job: str
    container_spec: ModelContainerSpec
    artifact_uri: str
    supported_deployment_resources_types: _containers.RepeatedScalarFieldContainer[Model.DeploymentResourcesType]
    supported_input_storage_formats: _containers.RepeatedScalarFieldContainer[str]
    supported_output_storage_formats: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    deployed_models: _containers.RepeatedCompositeFieldContainer[_deployed_model_ref_pb2.DeployedModelRef]
    explanation_spec: _explanation_pb2.ExplanationSpec
    etag: str
    labels: _containers.ScalarMap[str, str]
    data_stats: Model.DataStats
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    model_source_info: ModelSourceInfo
    original_model_info: Model.OriginalModelInfo
    metadata_artifact: str
    base_model_source: Model.BaseModelSource
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., version_id: _Optional[str] = ..., version_aliases: _Optional[_Iterable[str]] = ..., version_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., version_description: _Optional[str] = ..., predict_schemata: _Optional[_Union[PredictSchemata, _Mapping]] = ..., metadata_schema_uri: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., supported_export_formats: _Optional[_Iterable[_Union[Model.ExportFormat, _Mapping]]] = ..., training_pipeline: _Optional[str] = ..., pipeline_job: _Optional[str] = ..., container_spec: _Optional[_Union[ModelContainerSpec, _Mapping]] = ..., artifact_uri: _Optional[str] = ..., supported_deployment_resources_types: _Optional[_Iterable[_Union[Model.DeploymentResourcesType, str]]] = ..., supported_input_storage_formats: _Optional[_Iterable[str]] = ..., supported_output_storage_formats: _Optional[_Iterable[str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployed_models: _Optional[_Iterable[_Union[_deployed_model_ref_pb2.DeployedModelRef, _Mapping]]] = ..., explanation_spec: _Optional[_Union[_explanation_pb2.ExplanationSpec, _Mapping]] = ..., etag: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., data_stats: _Optional[_Union[Model.DataStats, _Mapping]] = ..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]] = ..., model_source_info: _Optional[_Union[ModelSourceInfo, _Mapping]] = ..., original_model_info: _Optional[_Union[Model.OriginalModelInfo, _Mapping]] = ..., metadata_artifact: _Optional[str] = ..., base_model_source: _Optional[_Union[Model.BaseModelSource, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class LargeModelReference(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ModelGardenSource(_message.Message):
    __slots__ = ("public_model_name",)
    PUBLIC_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    public_model_name: str
    def __init__(self, public_model_name: _Optional[str] = ...) -> None: ...

class GenieSource(_message.Message):
    __slots__ = ("base_model_uri",)
    BASE_MODEL_URI_FIELD_NUMBER: _ClassVar[int]
    base_model_uri: str
    def __init__(self, base_model_uri: _Optional[str] = ...) -> None: ...

class PredictSchemata(_message.Message):
    __slots__ = ("instance_schema_uri", "parameters_schema_uri", "prediction_schema_uri")
    INSTANCE_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    instance_schema_uri: str
    parameters_schema_uri: str
    prediction_schema_uri: str
    def __init__(self, instance_schema_uri: _Optional[str] = ..., parameters_schema_uri: _Optional[str] = ..., prediction_schema_uri: _Optional[str] = ...) -> None: ...

class ModelContainerSpec(_message.Message):
    __slots__ = ("image_uri", "command", "args", "env", "ports", "predict_route", "health_route", "grpc_ports", "deployment_timeout", "shared_memory_size_mb", "startup_probe", "health_probe")
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    PREDICT_ROUTE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_ROUTE_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORTS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SHARED_MEMORY_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    STARTUP_PROBE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_PROBE_FIELD_NUMBER: _ClassVar[int]
    image_uri: str
    command: _containers.RepeatedScalarFieldContainer[str]
    args: _containers.RepeatedScalarFieldContainer[str]
    env: _containers.RepeatedCompositeFieldContainer[_env_var_pb2.EnvVar]
    ports: _containers.RepeatedCompositeFieldContainer[Port]
    predict_route: str
    health_route: str
    grpc_ports: _containers.RepeatedCompositeFieldContainer[Port]
    deployment_timeout: _duration_pb2.Duration
    shared_memory_size_mb: int
    startup_probe: Probe
    health_probe: Probe
    def __init__(self, image_uri: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., args: _Optional[_Iterable[str]] = ..., env: _Optional[_Iterable[_Union[_env_var_pb2.EnvVar, _Mapping]]] = ..., ports: _Optional[_Iterable[_Union[Port, _Mapping]]] = ..., predict_route: _Optional[str] = ..., health_route: _Optional[str] = ..., grpc_ports: _Optional[_Iterable[_Union[Port, _Mapping]]] = ..., deployment_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., shared_memory_size_mb: _Optional[int] = ..., startup_probe: _Optional[_Union[Probe, _Mapping]] = ..., health_probe: _Optional[_Union[Probe, _Mapping]] = ...) -> None: ...

class Port(_message.Message):
    __slots__ = ("container_port",)
    CONTAINER_PORT_FIELD_NUMBER: _ClassVar[int]
    container_port: int
    def __init__(self, container_port: _Optional[int] = ...) -> None: ...

class ModelSourceInfo(_message.Message):
    __slots__ = ("source_type", "copy")
    class ModelSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_SOURCE_TYPE_UNSPECIFIED: _ClassVar[ModelSourceInfo.ModelSourceType]
        AUTOML: _ClassVar[ModelSourceInfo.ModelSourceType]
        CUSTOM: _ClassVar[ModelSourceInfo.ModelSourceType]
        BQML: _ClassVar[ModelSourceInfo.ModelSourceType]
        MODEL_GARDEN: _ClassVar[ModelSourceInfo.ModelSourceType]
        GENIE: _ClassVar[ModelSourceInfo.ModelSourceType]
        CUSTOM_TEXT_EMBEDDING: _ClassVar[ModelSourceInfo.ModelSourceType]
        MARKETPLACE: _ClassVar[ModelSourceInfo.ModelSourceType]
    MODEL_SOURCE_TYPE_UNSPECIFIED: ModelSourceInfo.ModelSourceType
    AUTOML: ModelSourceInfo.ModelSourceType
    CUSTOM: ModelSourceInfo.ModelSourceType
    BQML: ModelSourceInfo.ModelSourceType
    MODEL_GARDEN: ModelSourceInfo.ModelSourceType
    GENIE: ModelSourceInfo.ModelSourceType
    CUSTOM_TEXT_EMBEDDING: ModelSourceInfo.ModelSourceType
    MARKETPLACE: ModelSourceInfo.ModelSourceType
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COPY_FIELD_NUMBER: _ClassVar[int]
    source_type: ModelSourceInfo.ModelSourceType
    copy: bool
    def __init__(self, source_type: _Optional[_Union[ModelSourceInfo.ModelSourceType, str]] = ..., copy: bool = ...) -> None: ...

class Probe(_message.Message):
    __slots__ = ("exec", "period_seconds", "timeout_seconds")
    class ExecAction(_message.Message):
        __slots__ = ("command",)
        COMMAND_FIELD_NUMBER: _ClassVar[int]
        command: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, command: _Optional[_Iterable[str]] = ...) -> None: ...
    EXEC_FIELD_NUMBER: _ClassVar[int]
    PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    exec: Probe.ExecAction
    period_seconds: int
    timeout_seconds: int
    def __init__(self, exec: _Optional[_Union[Probe.ExecAction, _Mapping]] = ..., period_seconds: _Optional[int] = ..., timeout_seconds: _Optional[int] = ...) -> None: ...
