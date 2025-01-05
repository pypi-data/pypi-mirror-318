from google.appengine.v1beta import app_yaml_pb2 as _app_yaml_pb2
from google.appengine.v1beta import deploy_pb2 as _deploy_pb2
from google.appengine.v1beta import network_settings_pb2 as _network_settings_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InboundServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INBOUND_SERVICE_UNSPECIFIED: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_MAIL: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_MAIL_BOUNCE: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_XMPP_ERROR: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_XMPP_MESSAGE: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_XMPP_SUBSCRIBE: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_XMPP_PRESENCE: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_CHANNEL_PRESENCE: _ClassVar[InboundServiceType]
    INBOUND_SERVICE_WARMUP: _ClassVar[InboundServiceType]

class ServingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVING_STATUS_UNSPECIFIED: _ClassVar[ServingStatus]
    SERVING: _ClassVar[ServingStatus]
    STOPPED: _ClassVar[ServingStatus]
INBOUND_SERVICE_UNSPECIFIED: InboundServiceType
INBOUND_SERVICE_MAIL: InboundServiceType
INBOUND_SERVICE_MAIL_BOUNCE: InboundServiceType
INBOUND_SERVICE_XMPP_ERROR: InboundServiceType
INBOUND_SERVICE_XMPP_MESSAGE: InboundServiceType
INBOUND_SERVICE_XMPP_SUBSCRIBE: InboundServiceType
INBOUND_SERVICE_XMPP_PRESENCE: InboundServiceType
INBOUND_SERVICE_CHANNEL_PRESENCE: InboundServiceType
INBOUND_SERVICE_WARMUP: InboundServiceType
SERVING_STATUS_UNSPECIFIED: ServingStatus
SERVING: ServingStatus
STOPPED: ServingStatus

class Version(_message.Message):
    __slots__ = ('name', 'id', 'automatic_scaling', 'basic_scaling', 'manual_scaling', 'inbound_services', 'instance_class', 'network', 'zones', 'resources', 'runtime', 'runtime_channel', 'threadsafe', 'vm', 'app_engine_apis', 'beta_settings', 'env', 'serving_status', 'created_by', 'create_time', 'disk_usage_bytes', 'runtime_api_version', 'runtime_main_executable_path', 'service_account', 'handlers', 'error_handlers', 'libraries', 'api_config', 'env_variables', 'build_env_variables', 'default_expiration', 'health_check', 'readiness_check', 'liveness_check', 'nobuild_files_regex', 'deployment', 'version_url', 'endpoints_api_service', 'entrypoint', 'vpc_access_connector')

    class BetaSettingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class EnvVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class BuildEnvVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_SCALING_FIELD_NUMBER: _ClassVar[int]
    BASIC_SCALING_FIELD_NUMBER: _ClassVar[int]
    MANUAL_SCALING_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SERVICES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CLASS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    THREADSAFE_FIELD_NUMBER: _ClassVar[int]
    VM_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_APIS_FIELD_NUMBER: _ClassVar[int]
    BETA_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    SERVING_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_API_VERSION_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_MAIN_EXECUTABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    HANDLERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_HANDLERS_FIELD_NUMBER: _ClassVar[int]
    LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENV_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    BUILD_ENV_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    READINESS_CHECK_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_CHECK_FIELD_NUMBER: _ClassVar[int]
    NOBUILD_FILES_REGEX_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_URL_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_API_SERVICE_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    VPC_ACCESS_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    automatic_scaling: AutomaticScaling
    basic_scaling: BasicScaling
    manual_scaling: ManualScaling
    inbound_services: _containers.RepeatedScalarFieldContainer[InboundServiceType]
    instance_class: str
    network: Network
    zones: _containers.RepeatedScalarFieldContainer[str]
    resources: Resources
    runtime: str
    runtime_channel: str
    threadsafe: bool
    vm: bool
    app_engine_apis: bool
    beta_settings: _containers.ScalarMap[str, str]
    env: str
    serving_status: ServingStatus
    created_by: str
    create_time: _timestamp_pb2.Timestamp
    disk_usage_bytes: int
    runtime_api_version: str
    runtime_main_executable_path: str
    service_account: str
    handlers: _containers.RepeatedCompositeFieldContainer[_app_yaml_pb2.UrlMap]
    error_handlers: _containers.RepeatedCompositeFieldContainer[_app_yaml_pb2.ErrorHandler]
    libraries: _containers.RepeatedCompositeFieldContainer[_app_yaml_pb2.Library]
    api_config: _app_yaml_pb2.ApiConfigHandler
    env_variables: _containers.ScalarMap[str, str]
    build_env_variables: _containers.ScalarMap[str, str]
    default_expiration: _duration_pb2.Duration
    health_check: _app_yaml_pb2.HealthCheck
    readiness_check: _app_yaml_pb2.ReadinessCheck
    liveness_check: _app_yaml_pb2.LivenessCheck
    nobuild_files_regex: str
    deployment: _deploy_pb2.Deployment
    version_url: str
    endpoints_api_service: EndpointsApiService
    entrypoint: Entrypoint
    vpc_access_connector: VpcAccessConnector

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., automatic_scaling: _Optional[_Union[AutomaticScaling, _Mapping]]=..., basic_scaling: _Optional[_Union[BasicScaling, _Mapping]]=..., manual_scaling: _Optional[_Union[ManualScaling, _Mapping]]=..., inbound_services: _Optional[_Iterable[_Union[InboundServiceType, str]]]=..., instance_class: _Optional[str]=..., network: _Optional[_Union[Network, _Mapping]]=..., zones: _Optional[_Iterable[str]]=..., resources: _Optional[_Union[Resources, _Mapping]]=..., runtime: _Optional[str]=..., runtime_channel: _Optional[str]=..., threadsafe: bool=..., vm: bool=..., app_engine_apis: bool=..., beta_settings: _Optional[_Mapping[str, str]]=..., env: _Optional[str]=..., serving_status: _Optional[_Union[ServingStatus, str]]=..., created_by: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., disk_usage_bytes: _Optional[int]=..., runtime_api_version: _Optional[str]=..., runtime_main_executable_path: _Optional[str]=..., service_account: _Optional[str]=..., handlers: _Optional[_Iterable[_Union[_app_yaml_pb2.UrlMap, _Mapping]]]=..., error_handlers: _Optional[_Iterable[_Union[_app_yaml_pb2.ErrorHandler, _Mapping]]]=..., libraries: _Optional[_Iterable[_Union[_app_yaml_pb2.Library, _Mapping]]]=..., api_config: _Optional[_Union[_app_yaml_pb2.ApiConfigHandler, _Mapping]]=..., env_variables: _Optional[_Mapping[str, str]]=..., build_env_variables: _Optional[_Mapping[str, str]]=..., default_expiration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., health_check: _Optional[_Union[_app_yaml_pb2.HealthCheck, _Mapping]]=..., readiness_check: _Optional[_Union[_app_yaml_pb2.ReadinessCheck, _Mapping]]=..., liveness_check: _Optional[_Union[_app_yaml_pb2.LivenessCheck, _Mapping]]=..., nobuild_files_regex: _Optional[str]=..., deployment: _Optional[_Union[_deploy_pb2.Deployment, _Mapping]]=..., version_url: _Optional[str]=..., endpoints_api_service: _Optional[_Union[EndpointsApiService, _Mapping]]=..., entrypoint: _Optional[_Union[Entrypoint, _Mapping]]=..., vpc_access_connector: _Optional[_Union[VpcAccessConnector, _Mapping]]=...) -> None:
        ...

class EndpointsApiService(_message.Message):
    __slots__ = ('name', 'config_id', 'rollout_strategy', 'disable_trace_sampling')

    class RolloutStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED_ROLLOUT_STRATEGY: _ClassVar[EndpointsApiService.RolloutStrategy]
        FIXED: _ClassVar[EndpointsApiService.RolloutStrategy]
        MANAGED: _ClassVar[EndpointsApiService.RolloutStrategy]
    UNSPECIFIED_ROLLOUT_STRATEGY: EndpointsApiService.RolloutStrategy
    FIXED: EndpointsApiService.RolloutStrategy
    MANAGED: EndpointsApiService.RolloutStrategy
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TRACE_SAMPLING_FIELD_NUMBER: _ClassVar[int]
    name: str
    config_id: str
    rollout_strategy: EndpointsApiService.RolloutStrategy
    disable_trace_sampling: bool

    def __init__(self, name: _Optional[str]=..., config_id: _Optional[str]=..., rollout_strategy: _Optional[_Union[EndpointsApiService.RolloutStrategy, str]]=..., disable_trace_sampling: bool=...) -> None:
        ...

class AutomaticScaling(_message.Message):
    __slots__ = ('cool_down_period', 'cpu_utilization', 'max_concurrent_requests', 'max_idle_instances', 'max_total_instances', 'max_pending_latency', 'min_idle_instances', 'min_total_instances', 'min_pending_latency', 'request_utilization', 'disk_utilization', 'network_utilization', 'custom_metrics', 'standard_scheduler_settings')
    COOL_DOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    MAX_IDLE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_TOTAL_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_PENDING_LATENCY_FIELD_NUMBER: _ClassVar[int]
    MIN_IDLE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MIN_TOTAL_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MIN_PENDING_LATENCY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    DISK_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METRICS_FIELD_NUMBER: _ClassVar[int]
    STANDARD_SCHEDULER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    cool_down_period: _duration_pb2.Duration
    cpu_utilization: CpuUtilization
    max_concurrent_requests: int
    max_idle_instances: int
    max_total_instances: int
    max_pending_latency: _duration_pb2.Duration
    min_idle_instances: int
    min_total_instances: int
    min_pending_latency: _duration_pb2.Duration
    request_utilization: RequestUtilization
    disk_utilization: DiskUtilization
    network_utilization: NetworkUtilization
    custom_metrics: _containers.RepeatedCompositeFieldContainer[CustomMetric]
    standard_scheduler_settings: StandardSchedulerSettings

    def __init__(self, cool_down_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., cpu_utilization: _Optional[_Union[CpuUtilization, _Mapping]]=..., max_concurrent_requests: _Optional[int]=..., max_idle_instances: _Optional[int]=..., max_total_instances: _Optional[int]=..., max_pending_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., min_idle_instances: _Optional[int]=..., min_total_instances: _Optional[int]=..., min_pending_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., request_utilization: _Optional[_Union[RequestUtilization, _Mapping]]=..., disk_utilization: _Optional[_Union[DiskUtilization, _Mapping]]=..., network_utilization: _Optional[_Union[NetworkUtilization, _Mapping]]=..., custom_metrics: _Optional[_Iterable[_Union[CustomMetric, _Mapping]]]=..., standard_scheduler_settings: _Optional[_Union[StandardSchedulerSettings, _Mapping]]=...) -> None:
        ...

class BasicScaling(_message.Message):
    __slots__ = ('idle_timeout', 'max_instances')
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    idle_timeout: _duration_pb2.Duration
    max_instances: int

    def __init__(self, idle_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_instances: _Optional[int]=...) -> None:
        ...

class ManualScaling(_message.Message):
    __slots__ = ('instances',)
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    instances: int

    def __init__(self, instances: _Optional[int]=...) -> None:
        ...

class CpuUtilization(_message.Message):
    __slots__ = ('aggregation_window_length', 'target_utilization')
    AGGREGATION_WINDOW_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TARGET_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    aggregation_window_length: _duration_pb2.Duration
    target_utilization: float

    def __init__(self, aggregation_window_length: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., target_utilization: _Optional[float]=...) -> None:
        ...

class RequestUtilization(_message.Message):
    __slots__ = ('target_request_count_per_second', 'target_concurrent_requests')
    TARGET_REQUEST_COUNT_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TARGET_CONCURRENT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    target_request_count_per_second: int
    target_concurrent_requests: int

    def __init__(self, target_request_count_per_second: _Optional[int]=..., target_concurrent_requests: _Optional[int]=...) -> None:
        ...

class DiskUtilization(_message.Message):
    __slots__ = ('target_write_bytes_per_second', 'target_write_ops_per_second', 'target_read_bytes_per_second', 'target_read_ops_per_second')
    TARGET_WRITE_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TARGET_WRITE_OPS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TARGET_READ_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TARGET_READ_OPS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    target_write_bytes_per_second: int
    target_write_ops_per_second: int
    target_read_bytes_per_second: int
    target_read_ops_per_second: int

    def __init__(self, target_write_bytes_per_second: _Optional[int]=..., target_write_ops_per_second: _Optional[int]=..., target_read_bytes_per_second: _Optional[int]=..., target_read_ops_per_second: _Optional[int]=...) -> None:
        ...

class NetworkUtilization(_message.Message):
    __slots__ = ('target_sent_bytes_per_second', 'target_sent_packets_per_second', 'target_received_bytes_per_second', 'target_received_packets_per_second')
    TARGET_SENT_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TARGET_SENT_PACKETS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TARGET_RECEIVED_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TARGET_RECEIVED_PACKETS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    target_sent_bytes_per_second: int
    target_sent_packets_per_second: int
    target_received_bytes_per_second: int
    target_received_packets_per_second: int

    def __init__(self, target_sent_bytes_per_second: _Optional[int]=..., target_sent_packets_per_second: _Optional[int]=..., target_received_bytes_per_second: _Optional[int]=..., target_received_packets_per_second: _Optional[int]=...) -> None:
        ...

class CustomMetric(_message.Message):
    __slots__ = ('metric_name', 'target_type', 'target_utilization', 'single_instance_assignment', 'filter')
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    SINGLE_INSTANCE_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    target_type: str
    target_utilization: float
    single_instance_assignment: float
    filter: str

    def __init__(self, metric_name: _Optional[str]=..., target_type: _Optional[str]=..., target_utilization: _Optional[float]=..., single_instance_assignment: _Optional[float]=..., filter: _Optional[str]=...) -> None:
        ...

class StandardSchedulerSettings(_message.Message):
    __slots__ = ('target_cpu_utilization', 'target_throughput_utilization', 'min_instances', 'max_instances')
    TARGET_CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_THROUGHPUT_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    target_cpu_utilization: float
    target_throughput_utilization: float
    min_instances: int
    max_instances: int

    def __init__(self, target_cpu_utilization: _Optional[float]=..., target_throughput_utilization: _Optional[float]=..., min_instances: _Optional[int]=..., max_instances: _Optional[int]=...) -> None:
        ...

class Network(_message.Message):
    __slots__ = ('forwarded_ports', 'instance_tag', 'name', 'subnetwork_name', 'session_affinity')
    FORWARDED_PORTS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    forwarded_ports: _containers.RepeatedScalarFieldContainer[str]
    instance_tag: str
    name: str
    subnetwork_name: str
    session_affinity: bool

    def __init__(self, forwarded_ports: _Optional[_Iterable[str]]=..., instance_tag: _Optional[str]=..., name: _Optional[str]=..., subnetwork_name: _Optional[str]=..., session_affinity: bool=...) -> None:
        ...

class Volume(_message.Message):
    __slots__ = ('name', 'volume_type', 'size_gb')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    name: str
    volume_type: str
    size_gb: float

    def __init__(self, name: _Optional[str]=..., volume_type: _Optional[str]=..., size_gb: _Optional[float]=...) -> None:
        ...

class Resources(_message.Message):
    __slots__ = ('cpu', 'disk_gb', 'memory_gb', 'volumes', 'kms_key_reference')
    CPU_FIELD_NUMBER: _ClassVar[int]
    DISK_GB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    cpu: float
    disk_gb: float
    memory_gb: float
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    kms_key_reference: str

    def __init__(self, cpu: _Optional[float]=..., disk_gb: _Optional[float]=..., memory_gb: _Optional[float]=..., volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]]=..., kms_key_reference: _Optional[str]=...) -> None:
        ...

class VpcAccessConnector(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Entrypoint(_message.Message):
    __slots__ = ('shell',)
    SHELL_FIELD_NUMBER: _ClassVar[int]
    shell: str

    def __init__(self, shell: _Optional[str]=...) -> None:
        ...