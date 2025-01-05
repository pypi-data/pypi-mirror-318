from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipState(_message.Message):
    __slots__ = ("component_states", "state", "policy_content_state")
    class LifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[MembershipState.LifecycleState]
        NOT_INSTALLED: _ClassVar[MembershipState.LifecycleState]
        INSTALLING: _ClassVar[MembershipState.LifecycleState]
        ACTIVE: _ClassVar[MembershipState.LifecycleState]
        UPDATING: _ClassVar[MembershipState.LifecycleState]
        DECOMMISSIONING: _ClassVar[MembershipState.LifecycleState]
        CLUSTER_ERROR: _ClassVar[MembershipState.LifecycleState]
        HUB_ERROR: _ClassVar[MembershipState.LifecycleState]
        SUSPENDED: _ClassVar[MembershipState.LifecycleState]
        DETACHED: _ClassVar[MembershipState.LifecycleState]
    LIFECYCLE_STATE_UNSPECIFIED: MembershipState.LifecycleState
    NOT_INSTALLED: MembershipState.LifecycleState
    INSTALLING: MembershipState.LifecycleState
    ACTIVE: MembershipState.LifecycleState
    UPDATING: MembershipState.LifecycleState
    DECOMMISSIONING: MembershipState.LifecycleState
    CLUSTER_ERROR: MembershipState.LifecycleState
    HUB_ERROR: MembershipState.LifecycleState
    SUSPENDED: MembershipState.LifecycleState
    DETACHED: MembershipState.LifecycleState
    class ComponentStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OnClusterState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OnClusterState, _Mapping]] = ...) -> None: ...
    COMPONENT_STATES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POLICY_CONTENT_STATE_FIELD_NUMBER: _ClassVar[int]
    component_states: _containers.MessageMap[str, OnClusterState]
    state: MembershipState.LifecycleState
    policy_content_state: PolicyContentState
    def __init__(self, component_states: _Optional[_Mapping[str, OnClusterState]] = ..., state: _Optional[_Union[MembershipState.LifecycleState, str]] = ..., policy_content_state: _Optional[_Union[PolicyContentState, _Mapping]] = ...) -> None: ...

class PolicyContentState(_message.Message):
    __slots__ = ("template_library_state", "bundle_states", "referential_sync_config_state")
    class BundleStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OnClusterState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OnClusterState, _Mapping]] = ...) -> None: ...
    TEMPLATE_LIBRARY_STATE_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_STATES_FIELD_NUMBER: _ClassVar[int]
    REFERENTIAL_SYNC_CONFIG_STATE_FIELD_NUMBER: _ClassVar[int]
    template_library_state: OnClusterState
    bundle_states: _containers.MessageMap[str, OnClusterState]
    referential_sync_config_state: OnClusterState
    def __init__(self, template_library_state: _Optional[_Union[OnClusterState, _Mapping]] = ..., bundle_states: _Optional[_Mapping[str, OnClusterState]] = ..., referential_sync_config_state: _Optional[_Union[OnClusterState, _Mapping]] = ...) -> None: ...

class MembershipSpec(_message.Message):
    __slots__ = ("policy_controller_hub_config", "version")
    POLICY_CONTROLLER_HUB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    policy_controller_hub_config: HubConfig
    version: str
    def __init__(self, policy_controller_hub_config: _Optional[_Union[HubConfig, _Mapping]] = ..., version: _Optional[str] = ...) -> None: ...

class HubConfig(_message.Message):
    __slots__ = ("install_spec", "audit_interval_seconds", "exemptable_namespaces", "referential_rules_enabled", "log_denies_enabled", "mutation_enabled", "monitoring", "policy_content", "constraint_violation_limit", "deployment_configs")
    class InstallSpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTALL_SPEC_UNSPECIFIED: _ClassVar[HubConfig.InstallSpec]
        INSTALL_SPEC_NOT_INSTALLED: _ClassVar[HubConfig.InstallSpec]
        INSTALL_SPEC_ENABLED: _ClassVar[HubConfig.InstallSpec]
        INSTALL_SPEC_SUSPENDED: _ClassVar[HubConfig.InstallSpec]
        INSTALL_SPEC_DETACHED: _ClassVar[HubConfig.InstallSpec]
    INSTALL_SPEC_UNSPECIFIED: HubConfig.InstallSpec
    INSTALL_SPEC_NOT_INSTALLED: HubConfig.InstallSpec
    INSTALL_SPEC_ENABLED: HubConfig.InstallSpec
    INSTALL_SPEC_SUSPENDED: HubConfig.InstallSpec
    INSTALL_SPEC_DETACHED: HubConfig.InstallSpec
    class DeploymentConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PolicyControllerDeploymentConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PolicyControllerDeploymentConfig, _Mapping]] = ...) -> None: ...
    INSTALL_SPEC_FIELD_NUMBER: _ClassVar[int]
    AUDIT_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXEMPTABLE_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    REFERENTIAL_RULES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOG_DENIES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MUTATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MONITORING_FIELD_NUMBER: _ClassVar[int]
    POLICY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_VIOLATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    install_spec: HubConfig.InstallSpec
    audit_interval_seconds: int
    exemptable_namespaces: _containers.RepeatedScalarFieldContainer[str]
    referential_rules_enabled: bool
    log_denies_enabled: bool
    mutation_enabled: bool
    monitoring: MonitoringConfig
    policy_content: PolicyContentSpec
    constraint_violation_limit: int
    deployment_configs: _containers.MessageMap[str, PolicyControllerDeploymentConfig]
    def __init__(self, install_spec: _Optional[_Union[HubConfig.InstallSpec, str]] = ..., audit_interval_seconds: _Optional[int] = ..., exemptable_namespaces: _Optional[_Iterable[str]] = ..., referential_rules_enabled: bool = ..., log_denies_enabled: bool = ..., mutation_enabled: bool = ..., monitoring: _Optional[_Union[MonitoringConfig, _Mapping]] = ..., policy_content: _Optional[_Union[PolicyContentSpec, _Mapping]] = ..., constraint_violation_limit: _Optional[int] = ..., deployment_configs: _Optional[_Mapping[str, PolicyControllerDeploymentConfig]] = ...) -> None: ...

class PolicyControllerDeploymentConfig(_message.Message):
    __slots__ = ("replica_count", "container_resources", "pod_anti_affinity", "pod_tolerations", "pod_affinity")
    class Affinity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AFFINITY_UNSPECIFIED: _ClassVar[PolicyControllerDeploymentConfig.Affinity]
        NO_AFFINITY: _ClassVar[PolicyControllerDeploymentConfig.Affinity]
        ANTI_AFFINITY: _ClassVar[PolicyControllerDeploymentConfig.Affinity]
    AFFINITY_UNSPECIFIED: PolicyControllerDeploymentConfig.Affinity
    NO_AFFINITY: PolicyControllerDeploymentConfig.Affinity
    ANTI_AFFINITY: PolicyControllerDeploymentConfig.Affinity
    class Toleration(_message.Message):
        __slots__ = ("key", "operator", "value", "effect")
        KEY_FIELD_NUMBER: _ClassVar[int]
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        key: str
        operator: str
        value: str
        effect: str
        def __init__(self, key: _Optional[str] = ..., operator: _Optional[str] = ..., value: _Optional[str] = ..., effect: _Optional[str] = ...) -> None: ...
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    POD_ANTI_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    POD_TOLERATIONS_FIELD_NUMBER: _ClassVar[int]
    POD_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    replica_count: int
    container_resources: ResourceRequirements
    pod_anti_affinity: bool
    pod_tolerations: _containers.RepeatedCompositeFieldContainer[PolicyControllerDeploymentConfig.Toleration]
    pod_affinity: PolicyControllerDeploymentConfig.Affinity
    def __init__(self, replica_count: _Optional[int] = ..., container_resources: _Optional[_Union[ResourceRequirements, _Mapping]] = ..., pod_anti_affinity: bool = ..., pod_tolerations: _Optional[_Iterable[_Union[PolicyControllerDeploymentConfig.Toleration, _Mapping]]] = ..., pod_affinity: _Optional[_Union[PolicyControllerDeploymentConfig.Affinity, str]] = ...) -> None: ...

class ResourceRequirements(_message.Message):
    __slots__ = ("limits", "requests")
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    limits: ResourceList
    requests: ResourceList
    def __init__(self, limits: _Optional[_Union[ResourceList, _Mapping]] = ..., requests: _Optional[_Union[ResourceList, _Mapping]] = ...) -> None: ...

class ResourceList(_message.Message):
    __slots__ = ("memory", "cpu")
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    memory: str
    cpu: str
    def __init__(self, memory: _Optional[str] = ..., cpu: _Optional[str] = ...) -> None: ...

class TemplateLibraryConfig(_message.Message):
    __slots__ = ("installation",)
    class Installation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTALLATION_UNSPECIFIED: _ClassVar[TemplateLibraryConfig.Installation]
        NOT_INSTALLED: _ClassVar[TemplateLibraryConfig.Installation]
        ALL: _ClassVar[TemplateLibraryConfig.Installation]
    INSTALLATION_UNSPECIFIED: TemplateLibraryConfig.Installation
    NOT_INSTALLED: TemplateLibraryConfig.Installation
    ALL: TemplateLibraryConfig.Installation
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    installation: TemplateLibraryConfig.Installation
    def __init__(self, installation: _Optional[_Union[TemplateLibraryConfig.Installation, str]] = ...) -> None: ...

class MonitoringConfig(_message.Message):
    __slots__ = ("backends",)
    class MonitoringBackend(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MONITORING_BACKEND_UNSPECIFIED: _ClassVar[MonitoringConfig.MonitoringBackend]
        PROMETHEUS: _ClassVar[MonitoringConfig.MonitoringBackend]
        CLOUD_MONITORING: _ClassVar[MonitoringConfig.MonitoringBackend]
    MONITORING_BACKEND_UNSPECIFIED: MonitoringConfig.MonitoringBackend
    PROMETHEUS: MonitoringConfig.MonitoringBackend
    CLOUD_MONITORING: MonitoringConfig.MonitoringBackend
    BACKENDS_FIELD_NUMBER: _ClassVar[int]
    backends: _containers.RepeatedScalarFieldContainer[MonitoringConfig.MonitoringBackend]
    def __init__(self, backends: _Optional[_Iterable[_Union[MonitoringConfig.MonitoringBackend, str]]] = ...) -> None: ...

class OnClusterState(_message.Message):
    __slots__ = ("state", "details")
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    state: MembershipState.LifecycleState
    details: str
    def __init__(self, state: _Optional[_Union[MembershipState.LifecycleState, str]] = ..., details: _Optional[str] = ...) -> None: ...

class BundleInstallSpec(_message.Message):
    __slots__ = ("exempted_namespaces",)
    EXEMPTED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    exempted_namespaces: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, exempted_namespaces: _Optional[_Iterable[str]] = ...) -> None: ...

class PolicyContentSpec(_message.Message):
    __slots__ = ("bundles", "template_library")
    class BundlesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BundleInstallSpec
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BundleInstallSpec, _Mapping]] = ...) -> None: ...
    BUNDLES_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    bundles: _containers.MessageMap[str, BundleInstallSpec]
    template_library: TemplateLibraryConfig
    def __init__(self, bundles: _Optional[_Mapping[str, BundleInstallSpec]] = ..., template_library: _Optional[_Union[TemplateLibraryConfig, _Mapping]] = ...) -> None: ...
