from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.dataflow.v1beta3 import environment_pb2 as _environment_pb2
from google.dataflow.v1beta3 import jobs_pb2 as _jobs_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[ParameterType]
    TEXT: _ClassVar[ParameterType]
    GCS_READ_BUCKET: _ClassVar[ParameterType]
    GCS_WRITE_BUCKET: _ClassVar[ParameterType]
    GCS_READ_FILE: _ClassVar[ParameterType]
    GCS_WRITE_FILE: _ClassVar[ParameterType]
    GCS_READ_FOLDER: _ClassVar[ParameterType]
    GCS_WRITE_FOLDER: _ClassVar[ParameterType]
    PUBSUB_TOPIC: _ClassVar[ParameterType]
    PUBSUB_SUBSCRIPTION: _ClassVar[ParameterType]
DEFAULT: ParameterType
TEXT: ParameterType
GCS_READ_BUCKET: ParameterType
GCS_WRITE_BUCKET: ParameterType
GCS_READ_FILE: ParameterType
GCS_WRITE_FILE: ParameterType
GCS_READ_FOLDER: ParameterType
GCS_WRITE_FOLDER: ParameterType
PUBSUB_TOPIC: ParameterType
PUBSUB_SUBSCRIPTION: ParameterType

class LaunchFlexTemplateResponse(_message.Message):
    __slots__ = ('job',)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: _jobs_pb2.Job

    def __init__(self, job: _Optional[_Union[_jobs_pb2.Job, _Mapping]]=...) -> None:
        ...

class ContainerSpec(_message.Message):
    __slots__ = ('image', 'metadata', 'sdk_info', 'default_environment')
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SDK_INFO_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    image: str
    metadata: TemplateMetadata
    sdk_info: SDKInfo
    default_environment: FlexTemplateRuntimeEnvironment

    def __init__(self, image: _Optional[str]=..., metadata: _Optional[_Union[TemplateMetadata, _Mapping]]=..., sdk_info: _Optional[_Union[SDKInfo, _Mapping]]=..., default_environment: _Optional[_Union[FlexTemplateRuntimeEnvironment, _Mapping]]=...) -> None:
        ...

class LaunchFlexTemplateParameter(_message.Message):
    __slots__ = ('job_name', 'container_spec', 'container_spec_gcs_path', 'parameters', 'launch_options', 'environment', 'update', 'transform_name_mappings')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LaunchOptionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class TransformNameMappingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_SPEC_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_SPEC_GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_NAME_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    container_spec: ContainerSpec
    container_spec_gcs_path: str
    parameters: _containers.ScalarMap[str, str]
    launch_options: _containers.ScalarMap[str, str]
    environment: FlexTemplateRuntimeEnvironment
    update: bool
    transform_name_mappings: _containers.ScalarMap[str, str]

    def __init__(self, job_name: _Optional[str]=..., container_spec: _Optional[_Union[ContainerSpec, _Mapping]]=..., container_spec_gcs_path: _Optional[str]=..., parameters: _Optional[_Mapping[str, str]]=..., launch_options: _Optional[_Mapping[str, str]]=..., environment: _Optional[_Union[FlexTemplateRuntimeEnvironment, _Mapping]]=..., update: bool=..., transform_name_mappings: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class FlexTemplateRuntimeEnvironment(_message.Message):
    __slots__ = ('num_workers', 'max_workers', 'zone', 'service_account_email', 'temp_location', 'machine_type', 'additional_experiments', 'network', 'subnetwork', 'additional_user_labels', 'kms_key_name', 'ip_configuration', 'worker_region', 'worker_zone', 'enable_streaming_engine', 'flexrs_goal', 'staging_location', 'sdk_container_image', 'disk_size_gb', 'autoscaling_algorithm', 'dump_heap_on_oom', 'save_heap_dumps_to_gcs_path', 'launcher_machine_type')

    class AdditionalUserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NUM_WORKERS_FIELD_NUMBER: _ClassVar[int]
    MAX_WORKERS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    TEMP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    WORKER_REGION_FIELD_NUMBER: _ClassVar[int]
    WORKER_ZONE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STREAMING_ENGINE_FIELD_NUMBER: _ClassVar[int]
    FLEXRS_GOAL_FIELD_NUMBER: _ClassVar[int]
    STAGING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SDK_CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    DUMP_HEAP_ON_OOM_FIELD_NUMBER: _ClassVar[int]
    SAVE_HEAP_DUMPS_TO_GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    num_workers: int
    max_workers: int
    zone: str
    service_account_email: str
    temp_location: str
    machine_type: str
    additional_experiments: _containers.RepeatedScalarFieldContainer[str]
    network: str
    subnetwork: str
    additional_user_labels: _containers.ScalarMap[str, str]
    kms_key_name: str
    ip_configuration: _environment_pb2.WorkerIPAddressConfiguration
    worker_region: str
    worker_zone: str
    enable_streaming_engine: bool
    flexrs_goal: _environment_pb2.FlexResourceSchedulingGoal
    staging_location: str
    sdk_container_image: str
    disk_size_gb: int
    autoscaling_algorithm: _environment_pb2.AutoscalingAlgorithm
    dump_heap_on_oom: bool
    save_heap_dumps_to_gcs_path: str
    launcher_machine_type: str

    def __init__(self, num_workers: _Optional[int]=..., max_workers: _Optional[int]=..., zone: _Optional[str]=..., service_account_email: _Optional[str]=..., temp_location: _Optional[str]=..., machine_type: _Optional[str]=..., additional_experiments: _Optional[_Iterable[str]]=..., network: _Optional[str]=..., subnetwork: _Optional[str]=..., additional_user_labels: _Optional[_Mapping[str, str]]=..., kms_key_name: _Optional[str]=..., ip_configuration: _Optional[_Union[_environment_pb2.WorkerIPAddressConfiguration, str]]=..., worker_region: _Optional[str]=..., worker_zone: _Optional[str]=..., enable_streaming_engine: bool=..., flexrs_goal: _Optional[_Union[_environment_pb2.FlexResourceSchedulingGoal, str]]=..., staging_location: _Optional[str]=..., sdk_container_image: _Optional[str]=..., disk_size_gb: _Optional[int]=..., autoscaling_algorithm: _Optional[_Union[_environment_pb2.AutoscalingAlgorithm, str]]=..., dump_heap_on_oom: bool=..., save_heap_dumps_to_gcs_path: _Optional[str]=..., launcher_machine_type: _Optional[str]=...) -> None:
        ...

class LaunchFlexTemplateRequest(_message.Message):
    __slots__ = ('project_id', 'launch_parameter', 'location', 'validate_only')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    launch_parameter: LaunchFlexTemplateParameter
    location: str
    validate_only: bool

    def __init__(self, project_id: _Optional[str]=..., launch_parameter: _Optional[_Union[LaunchFlexTemplateParameter, _Mapping]]=..., location: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class RuntimeEnvironment(_message.Message):
    __slots__ = ('num_workers', 'max_workers', 'zone', 'service_account_email', 'temp_location', 'bypass_temp_dir_validation', 'machine_type', 'additional_experiments', 'network', 'subnetwork', 'additional_user_labels', 'kms_key_name', 'ip_configuration', 'worker_region', 'worker_zone', 'enable_streaming_engine')

    class AdditionalUserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NUM_WORKERS_FIELD_NUMBER: _ClassVar[int]
    MAX_WORKERS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    TEMP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    BYPASS_TEMP_DIR_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    WORKER_REGION_FIELD_NUMBER: _ClassVar[int]
    WORKER_ZONE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STREAMING_ENGINE_FIELD_NUMBER: _ClassVar[int]
    num_workers: int
    max_workers: int
    zone: str
    service_account_email: str
    temp_location: str
    bypass_temp_dir_validation: bool
    machine_type: str
    additional_experiments: _containers.RepeatedScalarFieldContainer[str]
    network: str
    subnetwork: str
    additional_user_labels: _containers.ScalarMap[str, str]
    kms_key_name: str
    ip_configuration: _environment_pb2.WorkerIPAddressConfiguration
    worker_region: str
    worker_zone: str
    enable_streaming_engine: bool

    def __init__(self, num_workers: _Optional[int]=..., max_workers: _Optional[int]=..., zone: _Optional[str]=..., service_account_email: _Optional[str]=..., temp_location: _Optional[str]=..., bypass_temp_dir_validation: bool=..., machine_type: _Optional[str]=..., additional_experiments: _Optional[_Iterable[str]]=..., network: _Optional[str]=..., subnetwork: _Optional[str]=..., additional_user_labels: _Optional[_Mapping[str, str]]=..., kms_key_name: _Optional[str]=..., ip_configuration: _Optional[_Union[_environment_pb2.WorkerIPAddressConfiguration, str]]=..., worker_region: _Optional[str]=..., worker_zone: _Optional[str]=..., enable_streaming_engine: bool=...) -> None:
        ...

class ParameterMetadata(_message.Message):
    __slots__ = ('name', 'label', 'help_text', 'is_optional', 'regexes', 'param_type', 'custom_metadata')

    class CustomMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    REGEXES_FIELD_NUMBER: _ClassVar[int]
    PARAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    label: str
    help_text: str
    is_optional: bool
    regexes: _containers.RepeatedScalarFieldContainer[str]
    param_type: ParameterType
    custom_metadata: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., label: _Optional[str]=..., help_text: _Optional[str]=..., is_optional: bool=..., regexes: _Optional[_Iterable[str]]=..., param_type: _Optional[_Union[ParameterType, str]]=..., custom_metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class TemplateMetadata(_message.Message):
    __slots__ = ('name', 'description', 'parameters')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: _containers.RepeatedCompositeFieldContainer[ParameterMetadata]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[ParameterMetadata, _Mapping]]]=...) -> None:
        ...

class SDKInfo(_message.Message):
    __slots__ = ('language', 'version')

    class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[SDKInfo.Language]
        JAVA: _ClassVar[SDKInfo.Language]
        PYTHON: _ClassVar[SDKInfo.Language]
    UNKNOWN: SDKInfo.Language
    JAVA: SDKInfo.Language
    PYTHON: SDKInfo.Language
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    language: SDKInfo.Language
    version: str

    def __init__(self, language: _Optional[_Union[SDKInfo.Language, str]]=..., version: _Optional[str]=...) -> None:
        ...

class RuntimeMetadata(_message.Message):
    __slots__ = ('sdk_info', 'parameters')
    SDK_INFO_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    sdk_info: SDKInfo
    parameters: _containers.RepeatedCompositeFieldContainer[ParameterMetadata]

    def __init__(self, sdk_info: _Optional[_Union[SDKInfo, _Mapping]]=..., parameters: _Optional[_Iterable[_Union[ParameterMetadata, _Mapping]]]=...) -> None:
        ...

class CreateJobFromTemplateRequest(_message.Message):
    __slots__ = ('project_id', 'job_name', 'gcs_path', 'parameters', 'environment', 'location')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_name: str
    gcs_path: str
    parameters: _containers.ScalarMap[str, str]
    environment: RuntimeEnvironment
    location: str

    def __init__(self, project_id: _Optional[str]=..., job_name: _Optional[str]=..., gcs_path: _Optional[str]=..., parameters: _Optional[_Mapping[str, str]]=..., environment: _Optional[_Union[RuntimeEnvironment, _Mapping]]=..., location: _Optional[str]=...) -> None:
        ...

class GetTemplateRequest(_message.Message):
    __slots__ = ('project_id', 'gcs_path', 'view', 'location')

    class TemplateView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METADATA_ONLY: _ClassVar[GetTemplateRequest.TemplateView]
    METADATA_ONLY: GetTemplateRequest.TemplateView
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    gcs_path: str
    view: GetTemplateRequest.TemplateView
    location: str

    def __init__(self, project_id: _Optional[str]=..., gcs_path: _Optional[str]=..., view: _Optional[_Union[GetTemplateRequest.TemplateView, str]]=..., location: _Optional[str]=...) -> None:
        ...

class GetTemplateResponse(_message.Message):
    __slots__ = ('status', 'metadata', 'template_type', 'runtime_metadata')

    class TemplateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[GetTemplateResponse.TemplateType]
        LEGACY: _ClassVar[GetTemplateResponse.TemplateType]
        FLEX: _ClassVar[GetTemplateResponse.TemplateType]
    UNKNOWN: GetTemplateResponse.TemplateType
    LEGACY: GetTemplateResponse.TemplateType
    FLEX: GetTemplateResponse.TemplateType
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_METADATA_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    metadata: TemplateMetadata
    template_type: GetTemplateResponse.TemplateType
    runtime_metadata: RuntimeMetadata

    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., metadata: _Optional[_Union[TemplateMetadata, _Mapping]]=..., template_type: _Optional[_Union[GetTemplateResponse.TemplateType, str]]=..., runtime_metadata: _Optional[_Union[RuntimeMetadata, _Mapping]]=...) -> None:
        ...

class LaunchTemplateParameters(_message.Message):
    __slots__ = ('job_name', 'parameters', 'environment', 'update', 'transform_name_mapping')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class TransformNameMappingEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_NAME_MAPPING_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    parameters: _containers.ScalarMap[str, str]
    environment: RuntimeEnvironment
    update: bool
    transform_name_mapping: _containers.ScalarMap[str, str]

    def __init__(self, job_name: _Optional[str]=..., parameters: _Optional[_Mapping[str, str]]=..., environment: _Optional[_Union[RuntimeEnvironment, _Mapping]]=..., update: bool=..., transform_name_mapping: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class LaunchTemplateRequest(_message.Message):
    __slots__ = ('project_id', 'validate_only', 'gcs_path', 'dynamic_template', 'launch_parameters', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    validate_only: bool
    gcs_path: str
    dynamic_template: DynamicTemplateLaunchParams
    launch_parameters: LaunchTemplateParameters
    location: str

    def __init__(self, project_id: _Optional[str]=..., validate_only: bool=..., gcs_path: _Optional[str]=..., dynamic_template: _Optional[_Union[DynamicTemplateLaunchParams, _Mapping]]=..., launch_parameters: _Optional[_Union[LaunchTemplateParameters, _Mapping]]=..., location: _Optional[str]=...) -> None:
        ...

class LaunchTemplateResponse(_message.Message):
    __slots__ = ('job',)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: _jobs_pb2.Job

    def __init__(self, job: _Optional[_Union[_jobs_pb2.Job, _Mapping]]=...) -> None:
        ...

class InvalidTemplateParameters(_message.Message):
    __slots__ = ('parameter_violations',)

    class ParameterViolation(_message.Message):
        __slots__ = ('parameter', 'description')
        PARAMETER_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        parameter: str
        description: str

        def __init__(self, parameter: _Optional[str]=..., description: _Optional[str]=...) -> None:
            ...
    PARAMETER_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    parameter_violations: _containers.RepeatedCompositeFieldContainer[InvalidTemplateParameters.ParameterViolation]

    def __init__(self, parameter_violations: _Optional[_Iterable[_Union[InvalidTemplateParameters.ParameterViolation, _Mapping]]]=...) -> None:
        ...

class DynamicTemplateLaunchParams(_message.Message):
    __slots__ = ('gcs_path', 'staging_location')
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    STAGING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    gcs_path: str
    staging_location: str

    def __init__(self, gcs_path: _Optional[str]=..., staging_location: _Optional[str]=...) -> None:
        ...