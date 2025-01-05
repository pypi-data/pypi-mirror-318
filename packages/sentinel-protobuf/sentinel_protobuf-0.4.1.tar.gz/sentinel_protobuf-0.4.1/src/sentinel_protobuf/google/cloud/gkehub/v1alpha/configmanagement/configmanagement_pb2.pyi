from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_STATE_UNSPECIFIED: _ClassVar[DeploymentState]
    NOT_INSTALLED: _ClassVar[DeploymentState]
    INSTALLED: _ClassVar[DeploymentState]
    ERROR: _ClassVar[DeploymentState]
DEPLOYMENT_STATE_UNSPECIFIED: DeploymentState
NOT_INSTALLED: DeploymentState
INSTALLED: DeploymentState
ERROR: DeploymentState

class MembershipState(_message.Message):
    __slots__ = ("cluster_name", "membership_spec", "operator_state", "config_sync_state", "policy_controller_state", "binauthz_state", "hierarchy_controller_state")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_SPEC_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_STATE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    POLICY_CONTROLLER_STATE_FIELD_NUMBER: _ClassVar[int]
    BINAUTHZ_STATE_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_CONTROLLER_STATE_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    membership_spec: MembershipSpec
    operator_state: OperatorState
    config_sync_state: ConfigSyncState
    policy_controller_state: PolicyControllerState
    binauthz_state: BinauthzState
    hierarchy_controller_state: HierarchyControllerState
    def __init__(self, cluster_name: _Optional[str] = ..., membership_spec: _Optional[_Union[MembershipSpec, _Mapping]] = ..., operator_state: _Optional[_Union[OperatorState, _Mapping]] = ..., config_sync_state: _Optional[_Union[ConfigSyncState, _Mapping]] = ..., policy_controller_state: _Optional[_Union[PolicyControllerState, _Mapping]] = ..., binauthz_state: _Optional[_Union[BinauthzState, _Mapping]] = ..., hierarchy_controller_state: _Optional[_Union[HierarchyControllerState, _Mapping]] = ...) -> None: ...

class MembershipSpec(_message.Message):
    __slots__ = ("config_sync", "policy_controller", "binauthz", "hierarchy_controller", "version")
    CONFIG_SYNC_FIELD_NUMBER: _ClassVar[int]
    POLICY_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    BINAUTHZ_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    config_sync: ConfigSync
    policy_controller: PolicyController
    binauthz: BinauthzConfig
    hierarchy_controller: HierarchyControllerConfig
    version: str
    def __init__(self, config_sync: _Optional[_Union[ConfigSync, _Mapping]] = ..., policy_controller: _Optional[_Union[PolicyController, _Mapping]] = ..., binauthz: _Optional[_Union[BinauthzConfig, _Mapping]] = ..., hierarchy_controller: _Optional[_Union[HierarchyControllerConfig, _Mapping]] = ..., version: _Optional[str] = ...) -> None: ...

class ConfigSync(_message.Message):
    __slots__ = ("git", "source_format")
    GIT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    git: GitConfig
    source_format: str
    def __init__(self, git: _Optional[_Union[GitConfig, _Mapping]] = ..., source_format: _Optional[str] = ...) -> None: ...

class GitConfig(_message.Message):
    __slots__ = ("sync_repo", "sync_branch", "policy_dir", "sync_wait_secs", "sync_rev", "secret_type", "https_proxy", "gcp_service_account_email")
    SYNC_REPO_FIELD_NUMBER: _ClassVar[int]
    SYNC_BRANCH_FIELD_NUMBER: _ClassVar[int]
    POLICY_DIR_FIELD_NUMBER: _ClassVar[int]
    SYNC_WAIT_SECS_FIELD_NUMBER: _ClassVar[int]
    SYNC_REV_FIELD_NUMBER: _ClassVar[int]
    SECRET_TYPE_FIELD_NUMBER: _ClassVar[int]
    HTTPS_PROXY_FIELD_NUMBER: _ClassVar[int]
    GCP_SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    sync_repo: str
    sync_branch: str
    policy_dir: str
    sync_wait_secs: int
    sync_rev: str
    secret_type: str
    https_proxy: str
    gcp_service_account_email: str
    def __init__(self, sync_repo: _Optional[str] = ..., sync_branch: _Optional[str] = ..., policy_dir: _Optional[str] = ..., sync_wait_secs: _Optional[int] = ..., sync_rev: _Optional[str] = ..., secret_type: _Optional[str] = ..., https_proxy: _Optional[str] = ..., gcp_service_account_email: _Optional[str] = ...) -> None: ...

class PolicyController(_message.Message):
    __slots__ = ("enabled", "template_library_installed", "audit_interval_seconds", "exemptable_namespaces", "referential_rules_enabled", "log_denies_enabled", "mutation_enabled")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_LIBRARY_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    AUDIT_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXEMPTABLE_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    REFERENTIAL_RULES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOG_DENIES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MUTATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    template_library_installed: bool
    audit_interval_seconds: int
    exemptable_namespaces: _containers.RepeatedScalarFieldContainer[str]
    referential_rules_enabled: bool
    log_denies_enabled: bool
    mutation_enabled: bool
    def __init__(self, enabled: bool = ..., template_library_installed: bool = ..., audit_interval_seconds: _Optional[int] = ..., exemptable_namespaces: _Optional[_Iterable[str]] = ..., referential_rules_enabled: bool = ..., log_denies_enabled: bool = ..., mutation_enabled: bool = ...) -> None: ...

class BinauthzConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class HierarchyControllerConfig(_message.Message):
    __slots__ = ("enabled", "enable_pod_tree_labels", "enable_hierarchical_resource_quota")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_POD_TREE_LABELS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HIERARCHICAL_RESOURCE_QUOTA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    enable_pod_tree_labels: bool
    enable_hierarchical_resource_quota: bool
    def __init__(self, enabled: bool = ..., enable_pod_tree_labels: bool = ..., enable_hierarchical_resource_quota: bool = ...) -> None: ...

class HierarchyControllerDeploymentState(_message.Message):
    __slots__ = ("hnc", "extension")
    HNC_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    hnc: DeploymentState
    extension: DeploymentState
    def __init__(self, hnc: _Optional[_Union[DeploymentState, str]] = ..., extension: _Optional[_Union[DeploymentState, str]] = ...) -> None: ...

class HierarchyControllerVersion(_message.Message):
    __slots__ = ("hnc", "extension")
    HNC_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    hnc: str
    extension: str
    def __init__(self, hnc: _Optional[str] = ..., extension: _Optional[str] = ...) -> None: ...

class HierarchyControllerState(_message.Message):
    __slots__ = ("version", "state")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    version: HierarchyControllerVersion
    state: HierarchyControllerDeploymentState
    def __init__(self, version: _Optional[_Union[HierarchyControllerVersion, _Mapping]] = ..., state: _Optional[_Union[HierarchyControllerDeploymentState, _Mapping]] = ...) -> None: ...

class OperatorState(_message.Message):
    __slots__ = ("version", "deployment_state", "errors")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    version: str
    deployment_state: DeploymentState
    errors: _containers.RepeatedCompositeFieldContainer[InstallError]
    def __init__(self, version: _Optional[str] = ..., deployment_state: _Optional[_Union[DeploymentState, str]] = ..., errors: _Optional[_Iterable[_Union[InstallError, _Mapping]]] = ...) -> None: ...

class InstallError(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class ConfigSyncState(_message.Message):
    __slots__ = ("version", "deployment_state", "sync_state")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    version: ConfigSyncVersion
    deployment_state: ConfigSyncDeploymentState
    sync_state: SyncState
    def __init__(self, version: _Optional[_Union[ConfigSyncVersion, _Mapping]] = ..., deployment_state: _Optional[_Union[ConfigSyncDeploymentState, _Mapping]] = ..., sync_state: _Optional[_Union[SyncState, _Mapping]] = ...) -> None: ...

class ConfigSyncVersion(_message.Message):
    __slots__ = ("importer", "syncer", "git_sync", "monitor", "reconciler_manager", "root_reconciler")
    IMPORTER_FIELD_NUMBER: _ClassVar[int]
    SYNCER_FIELD_NUMBER: _ClassVar[int]
    GIT_SYNC_FIELD_NUMBER: _ClassVar[int]
    MONITOR_FIELD_NUMBER: _ClassVar[int]
    RECONCILER_MANAGER_FIELD_NUMBER: _ClassVar[int]
    ROOT_RECONCILER_FIELD_NUMBER: _ClassVar[int]
    importer: str
    syncer: str
    git_sync: str
    monitor: str
    reconciler_manager: str
    root_reconciler: str
    def __init__(self, importer: _Optional[str] = ..., syncer: _Optional[str] = ..., git_sync: _Optional[str] = ..., monitor: _Optional[str] = ..., reconciler_manager: _Optional[str] = ..., root_reconciler: _Optional[str] = ...) -> None: ...

class ConfigSyncDeploymentState(_message.Message):
    __slots__ = ("importer", "syncer", "git_sync", "monitor", "reconciler_manager", "root_reconciler")
    IMPORTER_FIELD_NUMBER: _ClassVar[int]
    SYNCER_FIELD_NUMBER: _ClassVar[int]
    GIT_SYNC_FIELD_NUMBER: _ClassVar[int]
    MONITOR_FIELD_NUMBER: _ClassVar[int]
    RECONCILER_MANAGER_FIELD_NUMBER: _ClassVar[int]
    ROOT_RECONCILER_FIELD_NUMBER: _ClassVar[int]
    importer: DeploymentState
    syncer: DeploymentState
    git_sync: DeploymentState
    monitor: DeploymentState
    reconciler_manager: DeploymentState
    root_reconciler: DeploymentState
    def __init__(self, importer: _Optional[_Union[DeploymentState, str]] = ..., syncer: _Optional[_Union[DeploymentState, str]] = ..., git_sync: _Optional[_Union[DeploymentState, str]] = ..., monitor: _Optional[_Union[DeploymentState, str]] = ..., reconciler_manager: _Optional[_Union[DeploymentState, str]] = ..., root_reconciler: _Optional[_Union[DeploymentState, str]] = ...) -> None: ...

class SyncState(_message.Message):
    __slots__ = ("source_token", "import_token", "sync_token", "last_sync", "last_sync_time", "code", "errors")
    class SyncCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYNC_CODE_UNSPECIFIED: _ClassVar[SyncState.SyncCode]
        SYNCED: _ClassVar[SyncState.SyncCode]
        PENDING: _ClassVar[SyncState.SyncCode]
        ERROR: _ClassVar[SyncState.SyncCode]
        NOT_CONFIGURED: _ClassVar[SyncState.SyncCode]
        NOT_INSTALLED: _ClassVar[SyncState.SyncCode]
        UNAUTHORIZED: _ClassVar[SyncState.SyncCode]
        UNREACHABLE: _ClassVar[SyncState.SyncCode]
    SYNC_CODE_UNSPECIFIED: SyncState.SyncCode
    SYNCED: SyncState.SyncCode
    PENDING: SyncState.SyncCode
    ERROR: SyncState.SyncCode
    NOT_CONFIGURED: SyncState.SyncCode
    NOT_INSTALLED: SyncState.SyncCode
    UNAUTHORIZED: SyncState.SyncCode
    UNREACHABLE: SyncState.SyncCode
    SOURCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SYNC_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_TIME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    source_token: str
    import_token: str
    sync_token: str
    last_sync: str
    last_sync_time: _timestamp_pb2.Timestamp
    code: SyncState.SyncCode
    errors: _containers.RepeatedCompositeFieldContainer[SyncError]
    def __init__(self, source_token: _Optional[str] = ..., import_token: _Optional[str] = ..., sync_token: _Optional[str] = ..., last_sync: _Optional[str] = ..., last_sync_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., code: _Optional[_Union[SyncState.SyncCode, str]] = ..., errors: _Optional[_Iterable[_Union[SyncError, _Mapping]]] = ...) -> None: ...

class SyncError(_message.Message):
    __slots__ = ("code", "error_message", "error_resources")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    code: str
    error_message: str
    error_resources: _containers.RepeatedCompositeFieldContainer[ErrorResource]
    def __init__(self, code: _Optional[str] = ..., error_message: _Optional[str] = ..., error_resources: _Optional[_Iterable[_Union[ErrorResource, _Mapping]]] = ...) -> None: ...

class ErrorResource(_message.Message):
    __slots__ = ("source_path", "resource_name", "resource_namespace", "resource_gvk")
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GVK_FIELD_NUMBER: _ClassVar[int]
    source_path: str
    resource_name: str
    resource_namespace: str
    resource_gvk: GroupVersionKind
    def __init__(self, source_path: _Optional[str] = ..., resource_name: _Optional[str] = ..., resource_namespace: _Optional[str] = ..., resource_gvk: _Optional[_Union[GroupVersionKind, _Mapping]] = ...) -> None: ...

class GroupVersionKind(_message.Message):
    __slots__ = ("group", "version", "kind")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    group: str
    version: str
    kind: str
    def __init__(self, group: _Optional[str] = ..., version: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class PolicyControllerState(_message.Message):
    __slots__ = ("version", "deployment_state")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    version: PolicyControllerVersion
    deployment_state: GatekeeperDeploymentState
    def __init__(self, version: _Optional[_Union[PolicyControllerVersion, _Mapping]] = ..., deployment_state: _Optional[_Union[GatekeeperDeploymentState, _Mapping]] = ...) -> None: ...

class PolicyControllerVersion(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class BinauthzState(_message.Message):
    __slots__ = ("webhook", "version")
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    webhook: DeploymentState
    version: BinauthzVersion
    def __init__(self, webhook: _Optional[_Union[DeploymentState, str]] = ..., version: _Optional[_Union[BinauthzVersion, _Mapping]] = ...) -> None: ...

class BinauthzVersion(_message.Message):
    __slots__ = ("webhook_version",)
    WEBHOOK_VERSION_FIELD_NUMBER: _ClassVar[int]
    webhook_version: str
    def __init__(self, webhook_version: _Optional[str] = ...) -> None: ...

class GatekeeperDeploymentState(_message.Message):
    __slots__ = ("gatekeeper_controller_manager_state", "gatekeeper_audit", "gatekeeper_mutation")
    GATEKEEPER_CONTROLLER_MANAGER_STATE_FIELD_NUMBER: _ClassVar[int]
    GATEKEEPER_AUDIT_FIELD_NUMBER: _ClassVar[int]
    GATEKEEPER_MUTATION_FIELD_NUMBER: _ClassVar[int]
    gatekeeper_controller_manager_state: DeploymentState
    gatekeeper_audit: DeploymentState
    gatekeeper_mutation: DeploymentState
    def __init__(self, gatekeeper_controller_manager_state: _Optional[_Union[DeploymentState, str]] = ..., gatekeeper_audit: _Optional[_Union[DeploymentState, str]] = ..., gatekeeper_mutation: _Optional[_Union[DeploymentState, str]] = ...) -> None: ...
