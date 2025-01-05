from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpstreamPolicy(_message.Message):
    __slots__ = ("id", "repository", "priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    repository: str
    priority: int
    def __init__(self, id: _Optional[str] = ..., repository: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class CleanupPolicyCondition(_message.Message):
    __slots__ = ("tag_state", "tag_prefixes", "version_name_prefixes", "package_name_prefixes", "older_than", "newer_than")
    class TagState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TAG_STATE_UNSPECIFIED: _ClassVar[CleanupPolicyCondition.TagState]
        TAGGED: _ClassVar[CleanupPolicyCondition.TagState]
        UNTAGGED: _ClassVar[CleanupPolicyCondition.TagState]
        ANY: _ClassVar[CleanupPolicyCondition.TagState]
    TAG_STATE_UNSPECIFIED: CleanupPolicyCondition.TagState
    TAGGED: CleanupPolicyCondition.TagState
    UNTAGGED: CleanupPolicyCondition.TagState
    ANY: CleanupPolicyCondition.TagState
    TAG_STATE_FIELD_NUMBER: _ClassVar[int]
    TAG_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    VERSION_NAME_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    OLDER_THAN_FIELD_NUMBER: _ClassVar[int]
    NEWER_THAN_FIELD_NUMBER: _ClassVar[int]
    tag_state: CleanupPolicyCondition.TagState
    tag_prefixes: _containers.RepeatedScalarFieldContainer[str]
    version_name_prefixes: _containers.RepeatedScalarFieldContainer[str]
    package_name_prefixes: _containers.RepeatedScalarFieldContainer[str]
    older_than: _duration_pb2.Duration
    newer_than: _duration_pb2.Duration
    def __init__(self, tag_state: _Optional[_Union[CleanupPolicyCondition.TagState, str]] = ..., tag_prefixes: _Optional[_Iterable[str]] = ..., version_name_prefixes: _Optional[_Iterable[str]] = ..., package_name_prefixes: _Optional[_Iterable[str]] = ..., older_than: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., newer_than: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CleanupPolicyMostRecentVersions(_message.Message):
    __slots__ = ("package_name_prefixes", "keep_count")
    PACKAGE_NAME_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    KEEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    package_name_prefixes: _containers.RepeatedScalarFieldContainer[str]
    keep_count: int
    def __init__(self, package_name_prefixes: _Optional[_Iterable[str]] = ..., keep_count: _Optional[int] = ...) -> None: ...

class CleanupPolicy(_message.Message):
    __slots__ = ("condition", "most_recent_versions", "id", "action")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[CleanupPolicy.Action]
        DELETE: _ClassVar[CleanupPolicy.Action]
        KEEP: _ClassVar[CleanupPolicy.Action]
    ACTION_UNSPECIFIED: CleanupPolicy.Action
    DELETE: CleanupPolicy.Action
    KEEP: CleanupPolicy.Action
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    MOST_RECENT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    condition: CleanupPolicyCondition
    most_recent_versions: CleanupPolicyMostRecentVersions
    id: str
    action: CleanupPolicy.Action
    def __init__(self, condition: _Optional[_Union[CleanupPolicyCondition, _Mapping]] = ..., most_recent_versions: _Optional[_Union[CleanupPolicyMostRecentVersions, _Mapping]] = ..., id: _Optional[str] = ..., action: _Optional[_Union[CleanupPolicy.Action, str]] = ...) -> None: ...

class VirtualRepositoryConfig(_message.Message):
    __slots__ = ("upstream_policies",)
    UPSTREAM_POLICIES_FIELD_NUMBER: _ClassVar[int]
    upstream_policies: _containers.RepeatedCompositeFieldContainer[UpstreamPolicy]
    def __init__(self, upstream_policies: _Optional[_Iterable[_Union[UpstreamPolicy, _Mapping]]] = ...) -> None: ...

class RemoteRepositoryConfig(_message.Message):
    __slots__ = ("docker_repository", "maven_repository", "npm_repository", "python_repository", "apt_repository", "yum_repository", "common_repository", "description", "upstream_credentials", "disable_upstream_validation")
    class UpstreamCredentials(_message.Message):
        __slots__ = ("username_password_credentials",)
        class UsernamePasswordCredentials(_message.Message):
            __slots__ = ("username", "password_secret_version")
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
            username: str
            password_secret_version: str
            def __init__(self, username: _Optional[str] = ..., password_secret_version: _Optional[str] = ...) -> None: ...
        USERNAME_PASSWORD_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        username_password_credentials: RemoteRepositoryConfig.UpstreamCredentials.UsernamePasswordCredentials
        def __init__(self, username_password_credentials: _Optional[_Union[RemoteRepositoryConfig.UpstreamCredentials.UsernamePasswordCredentials, _Mapping]] = ...) -> None: ...
    class DockerRepository(_message.Message):
        __slots__ = ("public_repository", "custom_repository")
        class PublicRepository(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PUBLIC_REPOSITORY_UNSPECIFIED: _ClassVar[RemoteRepositoryConfig.DockerRepository.PublicRepository]
            DOCKER_HUB: _ClassVar[RemoteRepositoryConfig.DockerRepository.PublicRepository]
        PUBLIC_REPOSITORY_UNSPECIFIED: RemoteRepositoryConfig.DockerRepository.PublicRepository
        DOCKER_HUB: RemoteRepositoryConfig.DockerRepository.PublicRepository
        class CustomRepository(_message.Message):
            __slots__ = ("uri",)
            URI_FIELD_NUMBER: _ClassVar[int]
            uri: str
            def __init__(self, uri: _Optional[str] = ...) -> None: ...
        PUBLIC_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        public_repository: RemoteRepositoryConfig.DockerRepository.PublicRepository
        custom_repository: RemoteRepositoryConfig.DockerRepository.CustomRepository
        def __init__(self, public_repository: _Optional[_Union[RemoteRepositoryConfig.DockerRepository.PublicRepository, str]] = ..., custom_repository: _Optional[_Union[RemoteRepositoryConfig.DockerRepository.CustomRepository, _Mapping]] = ...) -> None: ...
    class MavenRepository(_message.Message):
        __slots__ = ("public_repository", "custom_repository")
        class PublicRepository(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PUBLIC_REPOSITORY_UNSPECIFIED: _ClassVar[RemoteRepositoryConfig.MavenRepository.PublicRepository]
            MAVEN_CENTRAL: _ClassVar[RemoteRepositoryConfig.MavenRepository.PublicRepository]
        PUBLIC_REPOSITORY_UNSPECIFIED: RemoteRepositoryConfig.MavenRepository.PublicRepository
        MAVEN_CENTRAL: RemoteRepositoryConfig.MavenRepository.PublicRepository
        class CustomRepository(_message.Message):
            __slots__ = ("uri",)
            URI_FIELD_NUMBER: _ClassVar[int]
            uri: str
            def __init__(self, uri: _Optional[str] = ...) -> None: ...
        PUBLIC_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        public_repository: RemoteRepositoryConfig.MavenRepository.PublicRepository
        custom_repository: RemoteRepositoryConfig.MavenRepository.CustomRepository
        def __init__(self, public_repository: _Optional[_Union[RemoteRepositoryConfig.MavenRepository.PublicRepository, str]] = ..., custom_repository: _Optional[_Union[RemoteRepositoryConfig.MavenRepository.CustomRepository, _Mapping]] = ...) -> None: ...
    class NpmRepository(_message.Message):
        __slots__ = ("public_repository", "custom_repository")
        class PublicRepository(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PUBLIC_REPOSITORY_UNSPECIFIED: _ClassVar[RemoteRepositoryConfig.NpmRepository.PublicRepository]
            NPMJS: _ClassVar[RemoteRepositoryConfig.NpmRepository.PublicRepository]
        PUBLIC_REPOSITORY_UNSPECIFIED: RemoteRepositoryConfig.NpmRepository.PublicRepository
        NPMJS: RemoteRepositoryConfig.NpmRepository.PublicRepository
        class CustomRepository(_message.Message):
            __slots__ = ("uri",)
            URI_FIELD_NUMBER: _ClassVar[int]
            uri: str
            def __init__(self, uri: _Optional[str] = ...) -> None: ...
        PUBLIC_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        public_repository: RemoteRepositoryConfig.NpmRepository.PublicRepository
        custom_repository: RemoteRepositoryConfig.NpmRepository.CustomRepository
        def __init__(self, public_repository: _Optional[_Union[RemoteRepositoryConfig.NpmRepository.PublicRepository, str]] = ..., custom_repository: _Optional[_Union[RemoteRepositoryConfig.NpmRepository.CustomRepository, _Mapping]] = ...) -> None: ...
    class PythonRepository(_message.Message):
        __slots__ = ("public_repository", "custom_repository")
        class PublicRepository(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PUBLIC_REPOSITORY_UNSPECIFIED: _ClassVar[RemoteRepositoryConfig.PythonRepository.PublicRepository]
            PYPI: _ClassVar[RemoteRepositoryConfig.PythonRepository.PublicRepository]
        PUBLIC_REPOSITORY_UNSPECIFIED: RemoteRepositoryConfig.PythonRepository.PublicRepository
        PYPI: RemoteRepositoryConfig.PythonRepository.PublicRepository
        class CustomRepository(_message.Message):
            __slots__ = ("uri",)
            URI_FIELD_NUMBER: _ClassVar[int]
            uri: str
            def __init__(self, uri: _Optional[str] = ...) -> None: ...
        PUBLIC_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        public_repository: RemoteRepositoryConfig.PythonRepository.PublicRepository
        custom_repository: RemoteRepositoryConfig.PythonRepository.CustomRepository
        def __init__(self, public_repository: _Optional[_Union[RemoteRepositoryConfig.PythonRepository.PublicRepository, str]] = ..., custom_repository: _Optional[_Union[RemoteRepositoryConfig.PythonRepository.CustomRepository, _Mapping]] = ...) -> None: ...
    class AptRepository(_message.Message):
        __slots__ = ("public_repository", "custom_repository")
        class PublicRepository(_message.Message):
            __slots__ = ("repository_base", "repository_path")
            class RepositoryBase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                REPOSITORY_BASE_UNSPECIFIED: _ClassVar[RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase]
                DEBIAN: _ClassVar[RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase]
                UBUNTU: _ClassVar[RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase]
                DEBIAN_SNAPSHOT: _ClassVar[RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase]
            REPOSITORY_BASE_UNSPECIFIED: RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase
            DEBIAN: RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase
            UBUNTU: RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase
            DEBIAN_SNAPSHOT: RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase
            REPOSITORY_BASE_FIELD_NUMBER: _ClassVar[int]
            REPOSITORY_PATH_FIELD_NUMBER: _ClassVar[int]
            repository_base: RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase
            repository_path: str
            def __init__(self, repository_base: _Optional[_Union[RemoteRepositoryConfig.AptRepository.PublicRepository.RepositoryBase, str]] = ..., repository_path: _Optional[str] = ...) -> None: ...
        class CustomRepository(_message.Message):
            __slots__ = ("uri",)
            URI_FIELD_NUMBER: _ClassVar[int]
            uri: str
            def __init__(self, uri: _Optional[str] = ...) -> None: ...
        PUBLIC_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        public_repository: RemoteRepositoryConfig.AptRepository.PublicRepository
        custom_repository: RemoteRepositoryConfig.AptRepository.CustomRepository
        def __init__(self, public_repository: _Optional[_Union[RemoteRepositoryConfig.AptRepository.PublicRepository, _Mapping]] = ..., custom_repository: _Optional[_Union[RemoteRepositoryConfig.AptRepository.CustomRepository, _Mapping]] = ...) -> None: ...
    class YumRepository(_message.Message):
        __slots__ = ("public_repository", "custom_repository")
        class PublicRepository(_message.Message):
            __slots__ = ("repository_base", "repository_path")
            class RepositoryBase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                REPOSITORY_BASE_UNSPECIFIED: _ClassVar[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase]
                CENTOS: _ClassVar[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase]
                CENTOS_DEBUG: _ClassVar[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase]
                CENTOS_VAULT: _ClassVar[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase]
                CENTOS_STREAM: _ClassVar[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase]
                ROCKY: _ClassVar[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase]
                EPEL: _ClassVar[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase]
            REPOSITORY_BASE_UNSPECIFIED: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            CENTOS: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            CENTOS_DEBUG: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            CENTOS_VAULT: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            CENTOS_STREAM: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            ROCKY: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            EPEL: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            REPOSITORY_BASE_FIELD_NUMBER: _ClassVar[int]
            REPOSITORY_PATH_FIELD_NUMBER: _ClassVar[int]
            repository_base: RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase
            repository_path: str
            def __init__(self, repository_base: _Optional[_Union[RemoteRepositoryConfig.YumRepository.PublicRepository.RepositoryBase, str]] = ..., repository_path: _Optional[str] = ...) -> None: ...
        class CustomRepository(_message.Message):
            __slots__ = ("uri",)
            URI_FIELD_NUMBER: _ClassVar[int]
            uri: str
            def __init__(self, uri: _Optional[str] = ...) -> None: ...
        PUBLIC_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        public_repository: RemoteRepositoryConfig.YumRepository.PublicRepository
        custom_repository: RemoteRepositoryConfig.YumRepository.CustomRepository
        def __init__(self, public_repository: _Optional[_Union[RemoteRepositoryConfig.YumRepository.PublicRepository, _Mapping]] = ..., custom_repository: _Optional[_Union[RemoteRepositoryConfig.YumRepository.CustomRepository, _Mapping]] = ...) -> None: ...
    class CommonRemoteRepository(_message.Message):
        __slots__ = ("uri",)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str
        def __init__(self, uri: _Optional[str] = ...) -> None: ...
    DOCKER_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    MAVEN_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    NPM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    PYTHON_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    APT_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    YUM_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    COMMON_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_UPSTREAM_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    docker_repository: RemoteRepositoryConfig.DockerRepository
    maven_repository: RemoteRepositoryConfig.MavenRepository
    npm_repository: RemoteRepositoryConfig.NpmRepository
    python_repository: RemoteRepositoryConfig.PythonRepository
    apt_repository: RemoteRepositoryConfig.AptRepository
    yum_repository: RemoteRepositoryConfig.YumRepository
    common_repository: RemoteRepositoryConfig.CommonRemoteRepository
    description: str
    upstream_credentials: RemoteRepositoryConfig.UpstreamCredentials
    disable_upstream_validation: bool
    def __init__(self, docker_repository: _Optional[_Union[RemoteRepositoryConfig.DockerRepository, _Mapping]] = ..., maven_repository: _Optional[_Union[RemoteRepositoryConfig.MavenRepository, _Mapping]] = ..., npm_repository: _Optional[_Union[RemoteRepositoryConfig.NpmRepository, _Mapping]] = ..., python_repository: _Optional[_Union[RemoteRepositoryConfig.PythonRepository, _Mapping]] = ..., apt_repository: _Optional[_Union[RemoteRepositoryConfig.AptRepository, _Mapping]] = ..., yum_repository: _Optional[_Union[RemoteRepositoryConfig.YumRepository, _Mapping]] = ..., common_repository: _Optional[_Union[RemoteRepositoryConfig.CommonRemoteRepository, _Mapping]] = ..., description: _Optional[str] = ..., upstream_credentials: _Optional[_Union[RemoteRepositoryConfig.UpstreamCredentials, _Mapping]] = ..., disable_upstream_validation: bool = ...) -> None: ...

class Repository(_message.Message):
    __slots__ = ("maven_config", "docker_config", "virtual_repository_config", "remote_repository_config", "name", "format", "description", "labels", "create_time", "update_time", "kms_key_name", "mode", "cleanup_policies", "size_bytes", "satisfies_pzs", "cleanup_policy_dry_run", "vulnerability_scanning_config", "disallow_unspecified_mode", "satisfies_pzi")
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[Repository.Format]
        DOCKER: _ClassVar[Repository.Format]
        MAVEN: _ClassVar[Repository.Format]
        NPM: _ClassVar[Repository.Format]
        APT: _ClassVar[Repository.Format]
        YUM: _ClassVar[Repository.Format]
        PYTHON: _ClassVar[Repository.Format]
        KFP: _ClassVar[Repository.Format]
        GO: _ClassVar[Repository.Format]
        GENERIC: _ClassVar[Repository.Format]
    FORMAT_UNSPECIFIED: Repository.Format
    DOCKER: Repository.Format
    MAVEN: Repository.Format
    NPM: Repository.Format
    APT: Repository.Format
    YUM: Repository.Format
    PYTHON: Repository.Format
    KFP: Repository.Format
    GO: Repository.Format
    GENERIC: Repository.Format
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[Repository.Mode]
        STANDARD_REPOSITORY: _ClassVar[Repository.Mode]
        VIRTUAL_REPOSITORY: _ClassVar[Repository.Mode]
        REMOTE_REPOSITORY: _ClassVar[Repository.Mode]
    MODE_UNSPECIFIED: Repository.Mode
    STANDARD_REPOSITORY: Repository.Mode
    VIRTUAL_REPOSITORY: Repository.Mode
    REMOTE_REPOSITORY: Repository.Mode
    class MavenRepositoryConfig(_message.Message):
        __slots__ = ("allow_snapshot_overwrites", "version_policy")
        class VersionPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VERSION_POLICY_UNSPECIFIED: _ClassVar[Repository.MavenRepositoryConfig.VersionPolicy]
            RELEASE: _ClassVar[Repository.MavenRepositoryConfig.VersionPolicy]
            SNAPSHOT: _ClassVar[Repository.MavenRepositoryConfig.VersionPolicy]
        VERSION_POLICY_UNSPECIFIED: Repository.MavenRepositoryConfig.VersionPolicy
        RELEASE: Repository.MavenRepositoryConfig.VersionPolicy
        SNAPSHOT: Repository.MavenRepositoryConfig.VersionPolicy
        ALLOW_SNAPSHOT_OVERWRITES_FIELD_NUMBER: _ClassVar[int]
        VERSION_POLICY_FIELD_NUMBER: _ClassVar[int]
        allow_snapshot_overwrites: bool
        version_policy: Repository.MavenRepositoryConfig.VersionPolicy
        def __init__(self, allow_snapshot_overwrites: bool = ..., version_policy: _Optional[_Union[Repository.MavenRepositoryConfig.VersionPolicy, str]] = ...) -> None: ...
    class DockerRepositoryConfig(_message.Message):
        __slots__ = ("immutable_tags",)
        IMMUTABLE_TAGS_FIELD_NUMBER: _ClassVar[int]
        immutable_tags: bool
        def __init__(self, immutable_tags: bool = ...) -> None: ...
    class VulnerabilityScanningConfig(_message.Message):
        __slots__ = ("enablement_config", "last_enable_time", "enablement_state", "enablement_state_reason")
        class EnablementConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENABLEMENT_CONFIG_UNSPECIFIED: _ClassVar[Repository.VulnerabilityScanningConfig.EnablementConfig]
            INHERITED: _ClassVar[Repository.VulnerabilityScanningConfig.EnablementConfig]
            DISABLED: _ClassVar[Repository.VulnerabilityScanningConfig.EnablementConfig]
        ENABLEMENT_CONFIG_UNSPECIFIED: Repository.VulnerabilityScanningConfig.EnablementConfig
        INHERITED: Repository.VulnerabilityScanningConfig.EnablementConfig
        DISABLED: Repository.VulnerabilityScanningConfig.EnablementConfig
        class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[Repository.VulnerabilityScanningConfig.EnablementState]
            SCANNING_UNSUPPORTED: _ClassVar[Repository.VulnerabilityScanningConfig.EnablementState]
            SCANNING_DISABLED: _ClassVar[Repository.VulnerabilityScanningConfig.EnablementState]
            SCANNING_ACTIVE: _ClassVar[Repository.VulnerabilityScanningConfig.EnablementState]
        ENABLEMENT_STATE_UNSPECIFIED: Repository.VulnerabilityScanningConfig.EnablementState
        SCANNING_UNSUPPORTED: Repository.VulnerabilityScanningConfig.EnablementState
        SCANNING_DISABLED: Repository.VulnerabilityScanningConfig.EnablementState
        SCANNING_ACTIVE: Repository.VulnerabilityScanningConfig.EnablementState
        ENABLEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        LAST_ENABLE_TIME_FIELD_NUMBER: _ClassVar[int]
        ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
        ENABLEMENT_STATE_REASON_FIELD_NUMBER: _ClassVar[int]
        enablement_config: Repository.VulnerabilityScanningConfig.EnablementConfig
        last_enable_time: _timestamp_pb2.Timestamp
        enablement_state: Repository.VulnerabilityScanningConfig.EnablementState
        enablement_state_reason: str
        def __init__(self, enablement_config: _Optional[_Union[Repository.VulnerabilityScanningConfig.EnablementConfig, str]] = ..., last_enable_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., enablement_state: _Optional[_Union[Repository.VulnerabilityScanningConfig.EnablementState, str]] = ..., enablement_state_reason: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class CleanupPoliciesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CleanupPolicy
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CleanupPolicy, _Mapping]] = ...) -> None: ...
    MAVEN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCKER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_REPOSITORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REMOTE_REPOSITORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_POLICIES_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_POLICY_DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_SCANNING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISALLOW_UNSPECIFIED_MODE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    maven_config: Repository.MavenRepositoryConfig
    docker_config: Repository.DockerRepositoryConfig
    virtual_repository_config: VirtualRepositoryConfig
    remote_repository_config: RemoteRepositoryConfig
    name: str
    format: Repository.Format
    description: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    kms_key_name: str
    mode: Repository.Mode
    cleanup_policies: _containers.MessageMap[str, CleanupPolicy]
    size_bytes: int
    satisfies_pzs: bool
    cleanup_policy_dry_run: bool
    vulnerability_scanning_config: Repository.VulnerabilityScanningConfig
    disallow_unspecified_mode: bool
    satisfies_pzi: bool
    def __init__(self, maven_config: _Optional[_Union[Repository.MavenRepositoryConfig, _Mapping]] = ..., docker_config: _Optional[_Union[Repository.DockerRepositoryConfig, _Mapping]] = ..., virtual_repository_config: _Optional[_Union[VirtualRepositoryConfig, _Mapping]] = ..., remote_repository_config: _Optional[_Union[RemoteRepositoryConfig, _Mapping]] = ..., name: _Optional[str] = ..., format: _Optional[_Union[Repository.Format, str]] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., kms_key_name: _Optional[str] = ..., mode: _Optional[_Union[Repository.Mode, str]] = ..., cleanup_policies: _Optional[_Mapping[str, CleanupPolicy]] = ..., size_bytes: _Optional[int] = ..., satisfies_pzs: bool = ..., cleanup_policy_dry_run: bool = ..., vulnerability_scanning_config: _Optional[_Union[Repository.VulnerabilityScanningConfig, _Mapping]] = ..., disallow_unspecified_mode: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class ListRepositoriesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListRepositoriesResponse(_message.Message):
    __slots__ = ("repositories", "next_page_token")
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str
    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetRepositoryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRepositoryRequest(_message.Message):
    __slots__ = ("parent", "repository_id", "repository")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_ID_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    repository_id: str
    repository: Repository
    def __init__(self, parent: _Optional[str] = ..., repository_id: _Optional[str] = ..., repository: _Optional[_Union[Repository, _Mapping]] = ...) -> None: ...

class UpdateRepositoryRequest(_message.Message):
    __slots__ = ("repository", "update_mask")
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    repository: Repository
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, repository: _Optional[_Union[Repository, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteRepositoryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
