from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Container(_message.Message):
    __slots__ = ("name", "image", "command", "args", "env", "resources", "ports", "volume_mounts", "working_dir", "liveness_probe", "startup_probe", "depends_on")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNTS_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIR_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_PROBE_FIELD_NUMBER: _ClassVar[int]
    STARTUP_PROBE_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_ON_FIELD_NUMBER: _ClassVar[int]
    name: str
    image: str
    command: _containers.RepeatedScalarFieldContainer[str]
    args: _containers.RepeatedScalarFieldContainer[str]
    env: _containers.RepeatedCompositeFieldContainer[EnvVar]
    resources: ResourceRequirements
    ports: _containers.RepeatedCompositeFieldContainer[ContainerPort]
    volume_mounts: _containers.RepeatedCompositeFieldContainer[VolumeMount]
    working_dir: str
    liveness_probe: Probe
    startup_probe: Probe
    depends_on: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., image: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., args: _Optional[_Iterable[str]] = ..., env: _Optional[_Iterable[_Union[EnvVar, _Mapping]]] = ..., resources: _Optional[_Union[ResourceRequirements, _Mapping]] = ..., ports: _Optional[_Iterable[_Union[ContainerPort, _Mapping]]] = ..., volume_mounts: _Optional[_Iterable[_Union[VolumeMount, _Mapping]]] = ..., working_dir: _Optional[str] = ..., liveness_probe: _Optional[_Union[Probe, _Mapping]] = ..., startup_probe: _Optional[_Union[Probe, _Mapping]] = ..., depends_on: _Optional[_Iterable[str]] = ...) -> None: ...

class ResourceRequirements(_message.Message):
    __slots__ = ("limits", "cpu_idle", "startup_cpu_boost")
    class LimitsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    CPU_IDLE_FIELD_NUMBER: _ClassVar[int]
    STARTUP_CPU_BOOST_FIELD_NUMBER: _ClassVar[int]
    limits: _containers.ScalarMap[str, str]
    cpu_idle: bool
    startup_cpu_boost: bool
    def __init__(self, limits: _Optional[_Mapping[str, str]] = ..., cpu_idle: bool = ..., startup_cpu_boost: bool = ...) -> None: ...

class EnvVar(_message.Message):
    __slots__ = ("name", "value", "value_source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    value_source: EnvVarSource
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., value_source: _Optional[_Union[EnvVarSource, _Mapping]] = ...) -> None: ...

class EnvVarSource(_message.Message):
    __slots__ = ("secret_key_ref",)
    SECRET_KEY_REF_FIELD_NUMBER: _ClassVar[int]
    secret_key_ref: SecretKeySelector
    def __init__(self, secret_key_ref: _Optional[_Union[SecretKeySelector, _Mapping]] = ...) -> None: ...

class SecretKeySelector(_message.Message):
    __slots__ = ("secret", "version")
    SECRET_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    secret: str
    version: str
    def __init__(self, secret: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class ContainerPort(_message.Message):
    __slots__ = ("name", "container_port")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_PORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    container_port: int
    def __init__(self, name: _Optional[str] = ..., container_port: _Optional[int] = ...) -> None: ...

class VolumeMount(_message.Message):
    __slots__ = ("name", "mount_path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    mount_path: str
    def __init__(self, name: _Optional[str] = ..., mount_path: _Optional[str] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("name", "secret", "cloud_sql_instance", "empty_dir", "nfs", "gcs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_DIR_FIELD_NUMBER: _ClassVar[int]
    NFS_FIELD_NUMBER: _ClassVar[int]
    GCS_FIELD_NUMBER: _ClassVar[int]
    name: str
    secret: SecretVolumeSource
    cloud_sql_instance: CloudSqlInstance
    empty_dir: EmptyDirVolumeSource
    nfs: NFSVolumeSource
    gcs: GCSVolumeSource
    def __init__(self, name: _Optional[str] = ..., secret: _Optional[_Union[SecretVolumeSource, _Mapping]] = ..., cloud_sql_instance: _Optional[_Union[CloudSqlInstance, _Mapping]] = ..., empty_dir: _Optional[_Union[EmptyDirVolumeSource, _Mapping]] = ..., nfs: _Optional[_Union[NFSVolumeSource, _Mapping]] = ..., gcs: _Optional[_Union[GCSVolumeSource, _Mapping]] = ...) -> None: ...

class SecretVolumeSource(_message.Message):
    __slots__ = ("secret", "items", "default_mode")
    SECRET_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODE_FIELD_NUMBER: _ClassVar[int]
    secret: str
    items: _containers.RepeatedCompositeFieldContainer[VersionToPath]
    default_mode: int
    def __init__(self, secret: _Optional[str] = ..., items: _Optional[_Iterable[_Union[VersionToPath, _Mapping]]] = ..., default_mode: _Optional[int] = ...) -> None: ...

class VersionToPath(_message.Message):
    __slots__ = ("path", "version", "mode")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    path: str
    version: str
    mode: int
    def __init__(self, path: _Optional[str] = ..., version: _Optional[str] = ..., mode: _Optional[int] = ...) -> None: ...

class CloudSqlInstance(_message.Message):
    __slots__ = ("instances",)
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instances: _Optional[_Iterable[str]] = ...) -> None: ...

class EmptyDirVolumeSource(_message.Message):
    __slots__ = ("medium", "size_limit")
    class Medium(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEDIUM_UNSPECIFIED: _ClassVar[EmptyDirVolumeSource.Medium]
        MEMORY: _ClassVar[EmptyDirVolumeSource.Medium]
    MEDIUM_UNSPECIFIED: EmptyDirVolumeSource.Medium
    MEMORY: EmptyDirVolumeSource.Medium
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    medium: EmptyDirVolumeSource.Medium
    size_limit: str
    def __init__(self, medium: _Optional[_Union[EmptyDirVolumeSource.Medium, str]] = ..., size_limit: _Optional[str] = ...) -> None: ...

class NFSVolumeSource(_message.Message):
    __slots__ = ("server", "path", "read_only")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    server: str
    path: str
    read_only: bool
    def __init__(self, server: _Optional[str] = ..., path: _Optional[str] = ..., read_only: bool = ...) -> None: ...

class GCSVolumeSource(_message.Message):
    __slots__ = ("bucket", "read_only", "mount_options")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    read_only: bool
    mount_options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, bucket: _Optional[str] = ..., read_only: bool = ..., mount_options: _Optional[_Iterable[str]] = ...) -> None: ...

class Probe(_message.Message):
    __slots__ = ("initial_delay_seconds", "timeout_seconds", "period_seconds", "failure_threshold", "http_get", "tcp_socket", "grpc")
    INITIAL_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    HTTP_GET_FIELD_NUMBER: _ClassVar[int]
    TCP_SOCKET_FIELD_NUMBER: _ClassVar[int]
    GRPC_FIELD_NUMBER: _ClassVar[int]
    initial_delay_seconds: int
    timeout_seconds: int
    period_seconds: int
    failure_threshold: int
    http_get: HTTPGetAction
    tcp_socket: TCPSocketAction
    grpc: GRPCAction
    def __init__(self, initial_delay_seconds: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., period_seconds: _Optional[int] = ..., failure_threshold: _Optional[int] = ..., http_get: _Optional[_Union[HTTPGetAction, _Mapping]] = ..., tcp_socket: _Optional[_Union[TCPSocketAction, _Mapping]] = ..., grpc: _Optional[_Union[GRPCAction, _Mapping]] = ...) -> None: ...

class HTTPGetAction(_message.Message):
    __slots__ = ("path", "http_headers", "port")
    PATH_FIELD_NUMBER: _ClassVar[int]
    HTTP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    path: str
    http_headers: _containers.RepeatedCompositeFieldContainer[HTTPHeader]
    port: int
    def __init__(self, path: _Optional[str] = ..., http_headers: _Optional[_Iterable[_Union[HTTPHeader, _Mapping]]] = ..., port: _Optional[int] = ...) -> None: ...

class HTTPHeader(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TCPSocketAction(_message.Message):
    __slots__ = ("port",)
    PORT_FIELD_NUMBER: _ClassVar[int]
    port: int
    def __init__(self, port: _Optional[int] = ...) -> None: ...

class GRPCAction(_message.Message):
    __slots__ = ("port", "service")
    PORT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    port: int
    service: str
    def __init__(self, port: _Optional[int] = ..., service: _Optional[str] = ...) -> None: ...
