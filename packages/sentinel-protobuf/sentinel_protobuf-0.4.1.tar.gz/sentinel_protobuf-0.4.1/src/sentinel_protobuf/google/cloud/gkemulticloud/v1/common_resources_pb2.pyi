from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Jwk(_message.Message):
    __slots__ = ("kty", "alg", "use", "kid", "n", "e", "x", "y", "crv")
    KTY_FIELD_NUMBER: _ClassVar[int]
    ALG_FIELD_NUMBER: _ClassVar[int]
    USE_FIELD_NUMBER: _ClassVar[int]
    KID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    CRV_FIELD_NUMBER: _ClassVar[int]
    kty: str
    alg: str
    use: str
    kid: str
    n: str
    e: str
    x: str
    y: str
    crv: str
    def __init__(self, kty: _Optional[str] = ..., alg: _Optional[str] = ..., use: _Optional[str] = ..., kid: _Optional[str] = ..., n: _Optional[str] = ..., e: _Optional[str] = ..., x: _Optional[str] = ..., y: _Optional[str] = ..., crv: _Optional[str] = ...) -> None: ...

class WorkloadIdentityConfig(_message.Message):
    __slots__ = ("issuer_uri", "workload_pool", "identity_provider")
    ISSUER_URI_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_POOL_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    issuer_uri: str
    workload_pool: str
    identity_provider: str
    def __init__(self, issuer_uri: _Optional[str] = ..., workload_pool: _Optional[str] = ..., identity_provider: _Optional[str] = ...) -> None: ...

class MaxPodsConstraint(_message.Message):
    __slots__ = ("max_pods_per_node",)
    MAX_PODS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    max_pods_per_node: int
    def __init__(self, max_pods_per_node: _Optional[int] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "status_detail", "error_detail", "verb", "requested_cancellation")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    status_detail: str
    error_detail: str
    verb: str
    requested_cancellation: bool
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., status_detail: _Optional[str] = ..., error_detail: _Optional[str] = ..., verb: _Optional[str] = ..., requested_cancellation: bool = ...) -> None: ...

class NodeTaint(_message.Message):
    __slots__ = ("key", "value", "effect")
    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EFFECT_UNSPECIFIED: _ClassVar[NodeTaint.Effect]
        NO_SCHEDULE: _ClassVar[NodeTaint.Effect]
        PREFER_NO_SCHEDULE: _ClassVar[NodeTaint.Effect]
        NO_EXECUTE: _ClassVar[NodeTaint.Effect]
    EFFECT_UNSPECIFIED: NodeTaint.Effect
    NO_SCHEDULE: NodeTaint.Effect
    PREFER_NO_SCHEDULE: NodeTaint.Effect
    NO_EXECUTE: NodeTaint.Effect
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    effect: NodeTaint.Effect
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., effect: _Optional[_Union[NodeTaint.Effect, str]] = ...) -> None: ...

class NodeKubeletConfig(_message.Message):
    __slots__ = ("insecure_kubelet_readonly_port_enabled", "cpu_manager_policy", "cpu_cfs_quota", "cpu_cfs_quota_period", "pod_pids_limit")
    INSECURE_KUBELET_READONLY_PORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CPU_MANAGER_POLICY_FIELD_NUMBER: _ClassVar[int]
    CPU_CFS_QUOTA_FIELD_NUMBER: _ClassVar[int]
    CPU_CFS_QUOTA_PERIOD_FIELD_NUMBER: _ClassVar[int]
    POD_PIDS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    insecure_kubelet_readonly_port_enabled: bool
    cpu_manager_policy: str
    cpu_cfs_quota: bool
    cpu_cfs_quota_period: str
    pod_pids_limit: int
    def __init__(self, insecure_kubelet_readonly_port_enabled: bool = ..., cpu_manager_policy: _Optional[str] = ..., cpu_cfs_quota: bool = ..., cpu_cfs_quota_period: _Optional[str] = ..., pod_pids_limit: _Optional[int] = ...) -> None: ...

class Fleet(_message.Message):
    __slots__ = ("project", "membership")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    project: str
    membership: str
    def __init__(self, project: _Optional[str] = ..., membership: _Optional[str] = ...) -> None: ...

class LoggingConfig(_message.Message):
    __slots__ = ("component_config",)
    COMPONENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    component_config: LoggingComponentConfig
    def __init__(self, component_config: _Optional[_Union[LoggingComponentConfig, _Mapping]] = ...) -> None: ...

class LoggingComponentConfig(_message.Message):
    __slots__ = ("enable_components",)
    class Component(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPONENT_UNSPECIFIED: _ClassVar[LoggingComponentConfig.Component]
        SYSTEM_COMPONENTS: _ClassVar[LoggingComponentConfig.Component]
        WORKLOADS: _ClassVar[LoggingComponentConfig.Component]
    COMPONENT_UNSPECIFIED: LoggingComponentConfig.Component
    SYSTEM_COMPONENTS: LoggingComponentConfig.Component
    WORKLOADS: LoggingComponentConfig.Component
    ENABLE_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    enable_components: _containers.RepeatedScalarFieldContainer[LoggingComponentConfig.Component]
    def __init__(self, enable_components: _Optional[_Iterable[_Union[LoggingComponentConfig.Component, str]]] = ...) -> None: ...

class MonitoringConfig(_message.Message):
    __slots__ = ("managed_prometheus_config", "cloud_monitoring_config")
    MANAGED_PROMETHEUS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLOUD_MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    managed_prometheus_config: ManagedPrometheusConfig
    cloud_monitoring_config: CloudMonitoringConfig
    def __init__(self, managed_prometheus_config: _Optional[_Union[ManagedPrometheusConfig, _Mapping]] = ..., cloud_monitoring_config: _Optional[_Union[CloudMonitoringConfig, _Mapping]] = ...) -> None: ...

class ManagedPrometheusConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class CloudMonitoringConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class BinaryAuthorization(_message.Message):
    __slots__ = ("evaluation_mode",)
    class EvaluationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATION_MODE_UNSPECIFIED: _ClassVar[BinaryAuthorization.EvaluationMode]
        DISABLED: _ClassVar[BinaryAuthorization.EvaluationMode]
        PROJECT_SINGLETON_POLICY_ENFORCE: _ClassVar[BinaryAuthorization.EvaluationMode]
    EVALUATION_MODE_UNSPECIFIED: BinaryAuthorization.EvaluationMode
    DISABLED: BinaryAuthorization.EvaluationMode
    PROJECT_SINGLETON_POLICY_ENFORCE: BinaryAuthorization.EvaluationMode
    EVALUATION_MODE_FIELD_NUMBER: _ClassVar[int]
    evaluation_mode: BinaryAuthorization.EvaluationMode
    def __init__(self, evaluation_mode: _Optional[_Union[BinaryAuthorization.EvaluationMode, str]] = ...) -> None: ...

class SecurityPostureConfig(_message.Message):
    __slots__ = ("vulnerability_mode",)
    class VulnerabilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VULNERABILITY_MODE_UNSPECIFIED: _ClassVar[SecurityPostureConfig.VulnerabilityMode]
        VULNERABILITY_DISABLED: _ClassVar[SecurityPostureConfig.VulnerabilityMode]
        VULNERABILITY_ENTERPRISE: _ClassVar[SecurityPostureConfig.VulnerabilityMode]
    VULNERABILITY_MODE_UNSPECIFIED: SecurityPostureConfig.VulnerabilityMode
    VULNERABILITY_DISABLED: SecurityPostureConfig.VulnerabilityMode
    VULNERABILITY_ENTERPRISE: SecurityPostureConfig.VulnerabilityMode
    VULNERABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    vulnerability_mode: SecurityPostureConfig.VulnerabilityMode
    def __init__(self, vulnerability_mode: _Optional[_Union[SecurityPostureConfig.VulnerabilityMode, str]] = ...) -> None: ...
