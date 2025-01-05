from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetryBuildRequest(_message.Message):
    __slots__ = ("name", "project_id", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    id: str
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RunBuildTriggerRequest(_message.Message):
    __slots__ = ("name", "project_id", "trigger_id", "source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    trigger_id: str
    source: RepoSource
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., trigger_id: _Optional[str] = ..., source: _Optional[_Union[RepoSource, _Mapping]] = ...) -> None: ...

class StorageSource(_message.Message):
    __slots__ = ("bucket", "object", "generation", "source_fetcher")
    class SourceFetcher(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_FETCHER_UNSPECIFIED: _ClassVar[StorageSource.SourceFetcher]
        GSUTIL: _ClassVar[StorageSource.SourceFetcher]
        GCS_FETCHER: _ClassVar[StorageSource.SourceFetcher]
    SOURCE_FETCHER_UNSPECIFIED: StorageSource.SourceFetcher
    GSUTIL: StorageSource.SourceFetcher
    GCS_FETCHER: StorageSource.SourceFetcher
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FETCHER_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    source_fetcher: StorageSource.SourceFetcher
    def __init__(self, bucket: _Optional[str] = ..., object: _Optional[str] = ..., generation: _Optional[int] = ..., source_fetcher: _Optional[_Union[StorageSource.SourceFetcher, str]] = ...) -> None: ...

class GitSource(_message.Message):
    __slots__ = ("url", "dir", "revision")
    URL_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    url: str
    dir: str
    revision: str
    def __init__(self, url: _Optional[str] = ..., dir: _Optional[str] = ..., revision: _Optional[str] = ...) -> None: ...

class RepoSource(_message.Message):
    __slots__ = ("project_id", "repo_name", "branch_name", "tag_name", "commit_sha", "dir", "invert_regex", "substitutions")
    class SubstitutionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    INVERT_REGEX_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    repo_name: str
    branch_name: str
    tag_name: str
    commit_sha: str
    dir: str
    invert_regex: bool
    substitutions: _containers.ScalarMap[str, str]
    def __init__(self, project_id: _Optional[str] = ..., repo_name: _Optional[str] = ..., branch_name: _Optional[str] = ..., tag_name: _Optional[str] = ..., commit_sha: _Optional[str] = ..., dir: _Optional[str] = ..., invert_regex: bool = ..., substitutions: _Optional[_Mapping[str, str]] = ...) -> None: ...

class StorageSourceManifest(_message.Message):
    __slots__ = ("bucket", "object", "generation")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    def __init__(self, bucket: _Optional[str] = ..., object: _Optional[str] = ..., generation: _Optional[int] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ("storage_source", "repo_source", "git_source", "storage_source_manifest")
    STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REPO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GIT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SOURCE_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    storage_source: StorageSource
    repo_source: RepoSource
    git_source: GitSource
    storage_source_manifest: StorageSourceManifest
    def __init__(self, storage_source: _Optional[_Union[StorageSource, _Mapping]] = ..., repo_source: _Optional[_Union[RepoSource, _Mapping]] = ..., git_source: _Optional[_Union[GitSource, _Mapping]] = ..., storage_source_manifest: _Optional[_Union[StorageSourceManifest, _Mapping]] = ...) -> None: ...

class BuiltImage(_message.Message):
    __slots__ = ("name", "digest", "push_timing")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_TIMING_FIELD_NUMBER: _ClassVar[int]
    name: str
    digest: str
    push_timing: TimeSpan
    def __init__(self, name: _Optional[str] = ..., digest: _Optional[str] = ..., push_timing: _Optional[_Union[TimeSpan, _Mapping]] = ...) -> None: ...

class UploadedPythonPackage(_message.Message):
    __slots__ = ("uri", "file_hashes", "push_timing")
    URI_FIELD_NUMBER: _ClassVar[int]
    FILE_HASHES_FIELD_NUMBER: _ClassVar[int]
    PUSH_TIMING_FIELD_NUMBER: _ClassVar[int]
    uri: str
    file_hashes: FileHashes
    push_timing: TimeSpan
    def __init__(self, uri: _Optional[str] = ..., file_hashes: _Optional[_Union[FileHashes, _Mapping]] = ..., push_timing: _Optional[_Union[TimeSpan, _Mapping]] = ...) -> None: ...

class UploadedMavenArtifact(_message.Message):
    __slots__ = ("uri", "file_hashes", "push_timing")
    URI_FIELD_NUMBER: _ClassVar[int]
    FILE_HASHES_FIELD_NUMBER: _ClassVar[int]
    PUSH_TIMING_FIELD_NUMBER: _ClassVar[int]
    uri: str
    file_hashes: FileHashes
    push_timing: TimeSpan
    def __init__(self, uri: _Optional[str] = ..., file_hashes: _Optional[_Union[FileHashes, _Mapping]] = ..., push_timing: _Optional[_Union[TimeSpan, _Mapping]] = ...) -> None: ...

class UploadedNpmPackage(_message.Message):
    __slots__ = ("uri", "file_hashes", "push_timing")
    URI_FIELD_NUMBER: _ClassVar[int]
    FILE_HASHES_FIELD_NUMBER: _ClassVar[int]
    PUSH_TIMING_FIELD_NUMBER: _ClassVar[int]
    uri: str
    file_hashes: FileHashes
    push_timing: TimeSpan
    def __init__(self, uri: _Optional[str] = ..., file_hashes: _Optional[_Union[FileHashes, _Mapping]] = ..., push_timing: _Optional[_Union[TimeSpan, _Mapping]] = ...) -> None: ...

class BuildStep(_message.Message):
    __slots__ = ("name", "env", "args", "dir", "id", "wait_for", "entrypoint", "secret_env", "volumes", "timing", "pull_timing", "timeout", "status", "allow_failure", "exit_code", "allow_exit_codes", "script", "automap_substitutions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENV_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    PULL_TIMING_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FAILURE_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXIT_CODES_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    AUTOMAP_SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    env: _containers.RepeatedScalarFieldContainer[str]
    args: _containers.RepeatedScalarFieldContainer[str]
    dir: str
    id: str
    wait_for: _containers.RepeatedScalarFieldContainer[str]
    entrypoint: str
    secret_env: _containers.RepeatedScalarFieldContainer[str]
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    timing: TimeSpan
    pull_timing: TimeSpan
    timeout: _duration_pb2.Duration
    status: Build.Status
    allow_failure: bool
    exit_code: int
    allow_exit_codes: _containers.RepeatedScalarFieldContainer[int]
    script: str
    automap_substitutions: bool
    def __init__(self, name: _Optional[str] = ..., env: _Optional[_Iterable[str]] = ..., args: _Optional[_Iterable[str]] = ..., dir: _Optional[str] = ..., id: _Optional[str] = ..., wait_for: _Optional[_Iterable[str]] = ..., entrypoint: _Optional[str] = ..., secret_env: _Optional[_Iterable[str]] = ..., volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., timing: _Optional[_Union[TimeSpan, _Mapping]] = ..., pull_timing: _Optional[_Union[TimeSpan, _Mapping]] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., status: _Optional[_Union[Build.Status, str]] = ..., allow_failure: bool = ..., exit_code: _Optional[int] = ..., allow_exit_codes: _Optional[_Iterable[int]] = ..., script: _Optional[str] = ..., automap_substitutions: bool = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("name", "path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class Results(_message.Message):
    __slots__ = ("images", "build_step_images", "artifact_manifest", "num_artifacts", "build_step_outputs", "artifact_timing", "python_packages", "maven_artifacts", "npm_packages")
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    BUILD_STEP_IMAGES_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    NUM_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    BUILD_STEP_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_TIMING_FIELD_NUMBER: _ClassVar[int]
    PYTHON_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    MAVEN_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    NPM_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    images: _containers.RepeatedCompositeFieldContainer[BuiltImage]
    build_step_images: _containers.RepeatedScalarFieldContainer[str]
    artifact_manifest: str
    num_artifacts: int
    build_step_outputs: _containers.RepeatedScalarFieldContainer[bytes]
    artifact_timing: TimeSpan
    python_packages: _containers.RepeatedCompositeFieldContainer[UploadedPythonPackage]
    maven_artifacts: _containers.RepeatedCompositeFieldContainer[UploadedMavenArtifact]
    npm_packages: _containers.RepeatedCompositeFieldContainer[UploadedNpmPackage]
    def __init__(self, images: _Optional[_Iterable[_Union[BuiltImage, _Mapping]]] = ..., build_step_images: _Optional[_Iterable[str]] = ..., artifact_manifest: _Optional[str] = ..., num_artifacts: _Optional[int] = ..., build_step_outputs: _Optional[_Iterable[bytes]] = ..., artifact_timing: _Optional[_Union[TimeSpan, _Mapping]] = ..., python_packages: _Optional[_Iterable[_Union[UploadedPythonPackage, _Mapping]]] = ..., maven_artifacts: _Optional[_Iterable[_Union[UploadedMavenArtifact, _Mapping]]] = ..., npm_packages: _Optional[_Iterable[_Union[UploadedNpmPackage, _Mapping]]] = ...) -> None: ...

class ArtifactResult(_message.Message):
    __slots__ = ("location", "file_hash")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    location: str
    file_hash: _containers.RepeatedCompositeFieldContainer[FileHashes]
    def __init__(self, location: _Optional[str] = ..., file_hash: _Optional[_Iterable[_Union[FileHashes, _Mapping]]] = ...) -> None: ...

class Build(_message.Message):
    __slots__ = ("name", "id", "project_id", "status", "status_detail", "source", "steps", "results", "create_time", "start_time", "finish_time", "timeout", "images", "queue_ttl", "artifacts", "logs_bucket", "source_provenance", "build_trigger_id", "options", "log_url", "substitutions", "tags", "secrets", "timing", "approval", "service_account", "available_secrets", "warnings", "failure_info")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNKNOWN: _ClassVar[Build.Status]
        PENDING: _ClassVar[Build.Status]
        QUEUED: _ClassVar[Build.Status]
        WORKING: _ClassVar[Build.Status]
        SUCCESS: _ClassVar[Build.Status]
        FAILURE: _ClassVar[Build.Status]
        INTERNAL_ERROR: _ClassVar[Build.Status]
        TIMEOUT: _ClassVar[Build.Status]
        CANCELLED: _ClassVar[Build.Status]
        EXPIRED: _ClassVar[Build.Status]
    STATUS_UNKNOWN: Build.Status
    PENDING: Build.Status
    QUEUED: Build.Status
    WORKING: Build.Status
    SUCCESS: Build.Status
    FAILURE: Build.Status
    INTERNAL_ERROR: Build.Status
    TIMEOUT: Build.Status
    CANCELLED: Build.Status
    EXPIRED: Build.Status
    class Warning(_message.Message):
        __slots__ = ("text", "priority")
        class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PRIORITY_UNSPECIFIED: _ClassVar[Build.Warning.Priority]
            INFO: _ClassVar[Build.Warning.Priority]
            WARNING: _ClassVar[Build.Warning.Priority]
            ALERT: _ClassVar[Build.Warning.Priority]
        PRIORITY_UNSPECIFIED: Build.Warning.Priority
        INFO: Build.Warning.Priority
        WARNING: Build.Warning.Priority
        ALERT: Build.Warning.Priority
        TEXT_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        text: str
        priority: Build.Warning.Priority
        def __init__(self, text: _Optional[str] = ..., priority: _Optional[_Union[Build.Warning.Priority, str]] = ...) -> None: ...
    class FailureInfo(_message.Message):
        __slots__ = ("type", "detail")
        class FailureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FAILURE_TYPE_UNSPECIFIED: _ClassVar[Build.FailureInfo.FailureType]
            PUSH_FAILED: _ClassVar[Build.FailureInfo.FailureType]
            PUSH_IMAGE_NOT_FOUND: _ClassVar[Build.FailureInfo.FailureType]
            PUSH_NOT_AUTHORIZED: _ClassVar[Build.FailureInfo.FailureType]
            LOGGING_FAILURE: _ClassVar[Build.FailureInfo.FailureType]
            USER_BUILD_STEP: _ClassVar[Build.FailureInfo.FailureType]
            FETCH_SOURCE_FAILED: _ClassVar[Build.FailureInfo.FailureType]
        FAILURE_TYPE_UNSPECIFIED: Build.FailureInfo.FailureType
        PUSH_FAILED: Build.FailureInfo.FailureType
        PUSH_IMAGE_NOT_FOUND: Build.FailureInfo.FailureType
        PUSH_NOT_AUTHORIZED: Build.FailureInfo.FailureType
        LOGGING_FAILURE: Build.FailureInfo.FailureType
        USER_BUILD_STEP: Build.FailureInfo.FailureType
        FETCH_SOURCE_FAILED: Build.FailureInfo.FailureType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        type: Build.FailureInfo.FailureType
        detail: str
        def __init__(self, type: _Optional[_Union[Build.FailureInfo.FailureType, str]] = ..., detail: _Optional[str] = ...) -> None: ...
    class SubstitutionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TimingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TimeSpan
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TimeSpan, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    QUEUE_TTL_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    LOGS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    BUILD_TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LOG_URL_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SECRETS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    project_id: str
    status: Build.Status
    status_detail: str
    source: Source
    steps: _containers.RepeatedCompositeFieldContainer[BuildStep]
    results: Results
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    timeout: _duration_pb2.Duration
    images: _containers.RepeatedScalarFieldContainer[str]
    queue_ttl: _duration_pb2.Duration
    artifacts: Artifacts
    logs_bucket: str
    source_provenance: SourceProvenance
    build_trigger_id: str
    options: BuildOptions
    log_url: str
    substitutions: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    secrets: _containers.RepeatedCompositeFieldContainer[Secret]
    timing: _containers.MessageMap[str, TimeSpan]
    approval: BuildApproval
    service_account: str
    available_secrets: Secrets
    warnings: _containers.RepeatedCompositeFieldContainer[Build.Warning]
    failure_info: Build.FailureInfo
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., project_id: _Optional[str] = ..., status: _Optional[_Union[Build.Status, str]] = ..., status_detail: _Optional[str] = ..., source: _Optional[_Union[Source, _Mapping]] = ..., steps: _Optional[_Iterable[_Union[BuildStep, _Mapping]]] = ..., results: _Optional[_Union[Results, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., images: _Optional[_Iterable[str]] = ..., queue_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., artifacts: _Optional[_Union[Artifacts, _Mapping]] = ..., logs_bucket: _Optional[str] = ..., source_provenance: _Optional[_Union[SourceProvenance, _Mapping]] = ..., build_trigger_id: _Optional[str] = ..., options: _Optional[_Union[BuildOptions, _Mapping]] = ..., log_url: _Optional[str] = ..., substitutions: _Optional[_Mapping[str, str]] = ..., tags: _Optional[_Iterable[str]] = ..., secrets: _Optional[_Iterable[_Union[Secret, _Mapping]]] = ..., timing: _Optional[_Mapping[str, TimeSpan]] = ..., approval: _Optional[_Union[BuildApproval, _Mapping]] = ..., service_account: _Optional[str] = ..., available_secrets: _Optional[_Union[Secrets, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[Build.Warning, _Mapping]]] = ..., failure_info: _Optional[_Union[Build.FailureInfo, _Mapping]] = ...) -> None: ...

class Artifacts(_message.Message):
    __slots__ = ("images", "objects", "maven_artifacts", "python_packages", "npm_packages")
    class ArtifactObjects(_message.Message):
        __slots__ = ("location", "paths", "timing")
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PATHS_FIELD_NUMBER: _ClassVar[int]
        TIMING_FIELD_NUMBER: _ClassVar[int]
        location: str
        paths: _containers.RepeatedScalarFieldContainer[str]
        timing: TimeSpan
        def __init__(self, location: _Optional[str] = ..., paths: _Optional[_Iterable[str]] = ..., timing: _Optional[_Union[TimeSpan, _Mapping]] = ...) -> None: ...
    class MavenArtifact(_message.Message):
        __slots__ = ("repository", "path", "artifact_id", "group_id", "version")
        REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        repository: str
        path: str
        artifact_id: str
        group_id: str
        version: str
        def __init__(self, repository: _Optional[str] = ..., path: _Optional[str] = ..., artifact_id: _Optional[str] = ..., group_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
    class PythonPackage(_message.Message):
        __slots__ = ("repository", "paths")
        REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        PATHS_FIELD_NUMBER: _ClassVar[int]
        repository: str
        paths: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, repository: _Optional[str] = ..., paths: _Optional[_Iterable[str]] = ...) -> None: ...
    class NpmPackage(_message.Message):
        __slots__ = ("repository", "package_path")
        REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_PATH_FIELD_NUMBER: _ClassVar[int]
        repository: str
        package_path: str
        def __init__(self, repository: _Optional[str] = ..., package_path: _Optional[str] = ...) -> None: ...
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MAVEN_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    PYTHON_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NPM_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    images: _containers.RepeatedScalarFieldContainer[str]
    objects: Artifacts.ArtifactObjects
    maven_artifacts: _containers.RepeatedCompositeFieldContainer[Artifacts.MavenArtifact]
    python_packages: _containers.RepeatedCompositeFieldContainer[Artifacts.PythonPackage]
    npm_packages: _containers.RepeatedCompositeFieldContainer[Artifacts.NpmPackage]
    def __init__(self, images: _Optional[_Iterable[str]] = ..., objects: _Optional[_Union[Artifacts.ArtifactObjects, _Mapping]] = ..., maven_artifacts: _Optional[_Iterable[_Union[Artifacts.MavenArtifact, _Mapping]]] = ..., python_packages: _Optional[_Iterable[_Union[Artifacts.PythonPackage, _Mapping]]] = ..., npm_packages: _Optional[_Iterable[_Union[Artifacts.NpmPackage, _Mapping]]] = ...) -> None: ...

class TimeSpan(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BuildOperationMetadata(_message.Message):
    __slots__ = ("build",)
    BUILD_FIELD_NUMBER: _ClassVar[int]
    build: Build
    def __init__(self, build: _Optional[_Union[Build, _Mapping]] = ...) -> None: ...

class SourceProvenance(_message.Message):
    __slots__ = ("resolved_storage_source", "resolved_repo_source", "resolved_storage_source_manifest", "file_hashes")
    class FileHashesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FileHashes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FileHashes, _Mapping]] = ...) -> None: ...
    RESOLVED_STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REPO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_STORAGE_SOURCE_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    FILE_HASHES_FIELD_NUMBER: _ClassVar[int]
    resolved_storage_source: StorageSource
    resolved_repo_source: RepoSource
    resolved_storage_source_manifest: StorageSourceManifest
    file_hashes: _containers.MessageMap[str, FileHashes]
    def __init__(self, resolved_storage_source: _Optional[_Union[StorageSource, _Mapping]] = ..., resolved_repo_source: _Optional[_Union[RepoSource, _Mapping]] = ..., resolved_storage_source_manifest: _Optional[_Union[StorageSourceManifest, _Mapping]] = ..., file_hashes: _Optional[_Mapping[str, FileHashes]] = ...) -> None: ...

class FileHashes(_message.Message):
    __slots__ = ("file_hash",)
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    file_hash: _containers.RepeatedCompositeFieldContainer[Hash]
    def __init__(self, file_hash: _Optional[_Iterable[_Union[Hash, _Mapping]]] = ...) -> None: ...

class Hash(_message.Message):
    __slots__ = ("type", "value")
    class HashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Hash.HashType]
        SHA256: _ClassVar[Hash.HashType]
        MD5: _ClassVar[Hash.HashType]
        SHA512: _ClassVar[Hash.HashType]
    NONE: Hash.HashType
    SHA256: Hash.HashType
    MD5: Hash.HashType
    SHA512: Hash.HashType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: Hash.HashType
    value: bytes
    def __init__(self, type: _Optional[_Union[Hash.HashType, str]] = ..., value: _Optional[bytes] = ...) -> None: ...

class Secrets(_message.Message):
    __slots__ = ("secret_manager", "inline")
    SECRET_MANAGER_FIELD_NUMBER: _ClassVar[int]
    INLINE_FIELD_NUMBER: _ClassVar[int]
    secret_manager: _containers.RepeatedCompositeFieldContainer[SecretManagerSecret]
    inline: _containers.RepeatedCompositeFieldContainer[InlineSecret]
    def __init__(self, secret_manager: _Optional[_Iterable[_Union[SecretManagerSecret, _Mapping]]] = ..., inline: _Optional[_Iterable[_Union[InlineSecret, _Mapping]]] = ...) -> None: ...

class InlineSecret(_message.Message):
    __slots__ = ("kms_key_name", "env_map")
    class EnvMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENV_MAP_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str
    env_map: _containers.ScalarMap[str, bytes]
    def __init__(self, kms_key_name: _Optional[str] = ..., env_map: _Optional[_Mapping[str, bytes]] = ...) -> None: ...

class SecretManagerSecret(_message.Message):
    __slots__ = ("version_name", "env")
    VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    version_name: str
    env: str
    def __init__(self, version_name: _Optional[str] = ..., env: _Optional[str] = ...) -> None: ...

class Secret(_message.Message):
    __slots__ = ("kms_key_name", "secret_env")
    class SecretEnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENV_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str
    secret_env: _containers.ScalarMap[str, bytes]
    def __init__(self, kms_key_name: _Optional[str] = ..., secret_env: _Optional[_Mapping[str, bytes]] = ...) -> None: ...

class CreateBuildRequest(_message.Message):
    __slots__ = ("parent", "project_id", "build")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    parent: str
    project_id: str
    build: Build
    def __init__(self, parent: _Optional[str] = ..., project_id: _Optional[str] = ..., build: _Optional[_Union[Build, _Mapping]] = ...) -> None: ...

class GetBuildRequest(_message.Message):
    __slots__ = ("name", "project_id", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    id: str
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ListBuildsRequest(_message.Message):
    __slots__ = ("parent", "project_id", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    project_id: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., project_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListBuildsResponse(_message.Message):
    __slots__ = ("builds", "next_page_token")
    BUILDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    builds: _containers.RepeatedCompositeFieldContainer[Build]
    next_page_token: str
    def __init__(self, builds: _Optional[_Iterable[_Union[Build, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CancelBuildRequest(_message.Message):
    __slots__ = ("name", "project_id", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    id: str
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ApproveBuildRequest(_message.Message):
    __slots__ = ("name", "approval_result")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    approval_result: ApprovalResult
    def __init__(self, name: _Optional[str] = ..., approval_result: _Optional[_Union[ApprovalResult, _Mapping]] = ...) -> None: ...

class BuildApproval(_message.Message):
    __slots__ = ("state", "config", "result")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BuildApproval.State]
        PENDING: _ClassVar[BuildApproval.State]
        APPROVED: _ClassVar[BuildApproval.State]
        REJECTED: _ClassVar[BuildApproval.State]
        CANCELLED: _ClassVar[BuildApproval.State]
    STATE_UNSPECIFIED: BuildApproval.State
    PENDING: BuildApproval.State
    APPROVED: BuildApproval.State
    REJECTED: BuildApproval.State
    CANCELLED: BuildApproval.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    state: BuildApproval.State
    config: ApprovalConfig
    result: ApprovalResult
    def __init__(self, state: _Optional[_Union[BuildApproval.State, str]] = ..., config: _Optional[_Union[ApprovalConfig, _Mapping]] = ..., result: _Optional[_Union[ApprovalResult, _Mapping]] = ...) -> None: ...

class ApprovalConfig(_message.Message):
    __slots__ = ("approval_required",)
    APPROVAL_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    approval_required: bool
    def __init__(self, approval_required: bool = ...) -> None: ...

class ApprovalResult(_message.Message):
    __slots__ = ("approver_account", "approval_time", "decision", "comment", "url")
    class Decision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DECISION_UNSPECIFIED: _ClassVar[ApprovalResult.Decision]
        APPROVED: _ClassVar[ApprovalResult.Decision]
        REJECTED: _ClassVar[ApprovalResult.Decision]
    DECISION_UNSPECIFIED: ApprovalResult.Decision
    APPROVED: ApprovalResult.Decision
    REJECTED: ApprovalResult.Decision
    APPROVER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    approver_account: str
    approval_time: _timestamp_pb2.Timestamp
    decision: ApprovalResult.Decision
    comment: str
    url: str
    def __init__(self, approver_account: _Optional[str] = ..., approval_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., decision: _Optional[_Union[ApprovalResult.Decision, str]] = ..., comment: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class GitRepoSource(_message.Message):
    __slots__ = ("uri", "repository", "ref", "repo_type", "github_enterprise_config")
    URI_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    REPO_TYPE_FIELD_NUMBER: _ClassVar[int]
    GITHUB_ENTERPRISE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    uri: str
    repository: str
    ref: str
    repo_type: GitFileSource.RepoType
    github_enterprise_config: str
    def __init__(self, uri: _Optional[str] = ..., repository: _Optional[str] = ..., ref: _Optional[str] = ..., repo_type: _Optional[_Union[GitFileSource.RepoType, str]] = ..., github_enterprise_config: _Optional[str] = ...) -> None: ...

class GitFileSource(_message.Message):
    __slots__ = ("path", "uri", "repository", "repo_type", "revision", "github_enterprise_config")
    class RepoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[GitFileSource.RepoType]
        CLOUD_SOURCE_REPOSITORIES: _ClassVar[GitFileSource.RepoType]
        GITHUB: _ClassVar[GitFileSource.RepoType]
        BITBUCKET_SERVER: _ClassVar[GitFileSource.RepoType]
        GITLAB: _ClassVar[GitFileSource.RepoType]
    UNKNOWN: GitFileSource.RepoType
    CLOUD_SOURCE_REPOSITORIES: GitFileSource.RepoType
    GITHUB: GitFileSource.RepoType
    BITBUCKET_SERVER: GitFileSource.RepoType
    GITLAB: GitFileSource.RepoType
    PATH_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REPO_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    GITHUB_ENTERPRISE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    path: str
    uri: str
    repository: str
    repo_type: GitFileSource.RepoType
    revision: str
    github_enterprise_config: str
    def __init__(self, path: _Optional[str] = ..., uri: _Optional[str] = ..., repository: _Optional[str] = ..., repo_type: _Optional[_Union[GitFileSource.RepoType, str]] = ..., revision: _Optional[str] = ..., github_enterprise_config: _Optional[str] = ...) -> None: ...

class BuildTrigger(_message.Message):
    __slots__ = ("resource_name", "id", "description", "name", "tags", "trigger_template", "github", "pubsub_config", "webhook_config", "autodetect", "build", "filename", "git_file_source", "create_time", "disabled", "substitutions", "ignored_files", "included_files", "filter", "source_to_build", "service_account", "repository_event_config")
    class SubstitutionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    GITHUB_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTODETECT_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    GIT_FILE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    IGNORED_FILES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_FILES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TO_BUILD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_EVENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: str
    description: str
    name: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    trigger_template: RepoSource
    github: GitHubEventsConfig
    pubsub_config: PubsubConfig
    webhook_config: WebhookConfig
    autodetect: bool
    build: Build
    filename: str
    git_file_source: GitFileSource
    create_time: _timestamp_pb2.Timestamp
    disabled: bool
    substitutions: _containers.ScalarMap[str, str]
    ignored_files: _containers.RepeatedScalarFieldContainer[str]
    included_files: _containers.RepeatedScalarFieldContainer[str]
    filter: str
    source_to_build: GitRepoSource
    service_account: str
    repository_event_config: RepositoryEventConfig
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[str] = ..., description: _Optional[str] = ..., name: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., trigger_template: _Optional[_Union[RepoSource, _Mapping]] = ..., github: _Optional[_Union[GitHubEventsConfig, _Mapping]] = ..., pubsub_config: _Optional[_Union[PubsubConfig, _Mapping]] = ..., webhook_config: _Optional[_Union[WebhookConfig, _Mapping]] = ..., autodetect: bool = ..., build: _Optional[_Union[Build, _Mapping]] = ..., filename: _Optional[str] = ..., git_file_source: _Optional[_Union[GitFileSource, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disabled: bool = ..., substitutions: _Optional[_Mapping[str, str]] = ..., ignored_files: _Optional[_Iterable[str]] = ..., included_files: _Optional[_Iterable[str]] = ..., filter: _Optional[str] = ..., source_to_build: _Optional[_Union[GitRepoSource, _Mapping]] = ..., service_account: _Optional[str] = ..., repository_event_config: _Optional[_Union[RepositoryEventConfig, _Mapping]] = ...) -> None: ...

class RepositoryEventConfig(_message.Message):
    __slots__ = ("repository", "repository_type", "pull_request", "push")
    class RepositoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPOSITORY_TYPE_UNSPECIFIED: _ClassVar[RepositoryEventConfig.RepositoryType]
        GITHUB: _ClassVar[RepositoryEventConfig.RepositoryType]
        GITHUB_ENTERPRISE: _ClassVar[RepositoryEventConfig.RepositoryType]
        GITLAB_ENTERPRISE: _ClassVar[RepositoryEventConfig.RepositoryType]
    REPOSITORY_TYPE_UNSPECIFIED: RepositoryEventConfig.RepositoryType
    GITHUB: RepositoryEventConfig.RepositoryType
    GITHUB_ENTERPRISE: RepositoryEventConfig.RepositoryType
    GITLAB_ENTERPRISE: RepositoryEventConfig.RepositoryType
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_FIELD_NUMBER: _ClassVar[int]
    repository: str
    repository_type: RepositoryEventConfig.RepositoryType
    pull_request: PullRequestFilter
    push: PushFilter
    def __init__(self, repository: _Optional[str] = ..., repository_type: _Optional[_Union[RepositoryEventConfig.RepositoryType, str]] = ..., pull_request: _Optional[_Union[PullRequestFilter, _Mapping]] = ..., push: _Optional[_Union[PushFilter, _Mapping]] = ...) -> None: ...

class GitHubEventsConfig(_message.Message):
    __slots__ = ("installation_id", "owner", "name", "pull_request", "push")
    INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUSH_FIELD_NUMBER: _ClassVar[int]
    installation_id: int
    owner: str
    name: str
    pull_request: PullRequestFilter
    push: PushFilter
    def __init__(self, installation_id: _Optional[int] = ..., owner: _Optional[str] = ..., name: _Optional[str] = ..., pull_request: _Optional[_Union[PullRequestFilter, _Mapping]] = ..., push: _Optional[_Union[PushFilter, _Mapping]] = ...) -> None: ...

class PubsubConfig(_message.Message):
    __slots__ = ("subscription", "topic", "service_account_email", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PubsubConfig.State]
        OK: _ClassVar[PubsubConfig.State]
        SUBSCRIPTION_DELETED: _ClassVar[PubsubConfig.State]
        TOPIC_DELETED: _ClassVar[PubsubConfig.State]
        SUBSCRIPTION_MISCONFIGURED: _ClassVar[PubsubConfig.State]
    STATE_UNSPECIFIED: PubsubConfig.State
    OK: PubsubConfig.State
    SUBSCRIPTION_DELETED: PubsubConfig.State
    TOPIC_DELETED: PubsubConfig.State
    SUBSCRIPTION_MISCONFIGURED: PubsubConfig.State
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    topic: str
    service_account_email: str
    state: PubsubConfig.State
    def __init__(self, subscription: _Optional[str] = ..., topic: _Optional[str] = ..., service_account_email: _Optional[str] = ..., state: _Optional[_Union[PubsubConfig.State, str]] = ...) -> None: ...

class WebhookConfig(_message.Message):
    __slots__ = ("secret", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WebhookConfig.State]
        OK: _ClassVar[WebhookConfig.State]
        SECRET_DELETED: _ClassVar[WebhookConfig.State]
    STATE_UNSPECIFIED: WebhookConfig.State
    OK: WebhookConfig.State
    SECRET_DELETED: WebhookConfig.State
    SECRET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    secret: str
    state: WebhookConfig.State
    def __init__(self, secret: _Optional[str] = ..., state: _Optional[_Union[WebhookConfig.State, str]] = ...) -> None: ...

class PullRequestFilter(_message.Message):
    __slots__ = ("branch", "comment_control", "invert_regex")
    class CommentControl(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMMENTS_DISABLED: _ClassVar[PullRequestFilter.CommentControl]
        COMMENTS_ENABLED: _ClassVar[PullRequestFilter.CommentControl]
        COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY: _ClassVar[PullRequestFilter.CommentControl]
    COMMENTS_DISABLED: PullRequestFilter.CommentControl
    COMMENTS_ENABLED: PullRequestFilter.CommentControl
    COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY: PullRequestFilter.CommentControl
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COMMENT_CONTROL_FIELD_NUMBER: _ClassVar[int]
    INVERT_REGEX_FIELD_NUMBER: _ClassVar[int]
    branch: str
    comment_control: PullRequestFilter.CommentControl
    invert_regex: bool
    def __init__(self, branch: _Optional[str] = ..., comment_control: _Optional[_Union[PullRequestFilter.CommentControl, str]] = ..., invert_regex: bool = ...) -> None: ...

class PushFilter(_message.Message):
    __slots__ = ("branch", "tag", "invert_regex")
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    INVERT_REGEX_FIELD_NUMBER: _ClassVar[int]
    branch: str
    tag: str
    invert_regex: bool
    def __init__(self, branch: _Optional[str] = ..., tag: _Optional[str] = ..., invert_regex: bool = ...) -> None: ...

class CreateBuildTriggerRequest(_message.Message):
    __slots__ = ("parent", "project_id", "trigger")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    project_id: str
    trigger: BuildTrigger
    def __init__(self, parent: _Optional[str] = ..., project_id: _Optional[str] = ..., trigger: _Optional[_Union[BuildTrigger, _Mapping]] = ...) -> None: ...

class GetBuildTriggerRequest(_message.Message):
    __slots__ = ("name", "project_id", "trigger_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    trigger_id: str
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., trigger_id: _Optional[str] = ...) -> None: ...

class ListBuildTriggersRequest(_message.Message):
    __slots__ = ("parent", "project_id", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    project_id: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., project_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListBuildTriggersResponse(_message.Message):
    __slots__ = ("triggers", "next_page_token")
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    triggers: _containers.RepeatedCompositeFieldContainer[BuildTrigger]
    next_page_token: str
    def __init__(self, triggers: _Optional[_Iterable[_Union[BuildTrigger, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteBuildTriggerRequest(_message.Message):
    __slots__ = ("name", "project_id", "trigger_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    trigger_id: str
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., trigger_id: _Optional[str] = ...) -> None: ...

class UpdateBuildTriggerRequest(_message.Message):
    __slots__ = ("project_id", "trigger_id", "trigger", "update_mask")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    trigger_id: str
    trigger: BuildTrigger
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, project_id: _Optional[str] = ..., trigger_id: _Optional[str] = ..., trigger: _Optional[_Union[BuildTrigger, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class BuildOptions(_message.Message):
    __slots__ = ("source_provenance_hash", "requested_verify_option", "machine_type", "disk_size_gb", "substitution_option", "dynamic_substitutions", "automap_substitutions", "log_streaming_option", "worker_pool", "pool", "logging", "env", "secret_env", "volumes", "default_logs_bucket_behavior")
    class VerifyOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_VERIFIED: _ClassVar[BuildOptions.VerifyOption]
        VERIFIED: _ClassVar[BuildOptions.VerifyOption]
    NOT_VERIFIED: BuildOptions.VerifyOption
    VERIFIED: BuildOptions.VerifyOption
    class MachineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BuildOptions.MachineType]
        N1_HIGHCPU_8: _ClassVar[BuildOptions.MachineType]
        N1_HIGHCPU_32: _ClassVar[BuildOptions.MachineType]
        E2_HIGHCPU_8: _ClassVar[BuildOptions.MachineType]
        E2_HIGHCPU_32: _ClassVar[BuildOptions.MachineType]
        E2_MEDIUM: _ClassVar[BuildOptions.MachineType]
    UNSPECIFIED: BuildOptions.MachineType
    N1_HIGHCPU_8: BuildOptions.MachineType
    N1_HIGHCPU_32: BuildOptions.MachineType
    E2_HIGHCPU_8: BuildOptions.MachineType
    E2_HIGHCPU_32: BuildOptions.MachineType
    E2_MEDIUM: BuildOptions.MachineType
    class SubstitutionOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUST_MATCH: _ClassVar[BuildOptions.SubstitutionOption]
        ALLOW_LOOSE: _ClassVar[BuildOptions.SubstitutionOption]
    MUST_MATCH: BuildOptions.SubstitutionOption
    ALLOW_LOOSE: BuildOptions.SubstitutionOption
    class LogStreamingOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STREAM_DEFAULT: _ClassVar[BuildOptions.LogStreamingOption]
        STREAM_ON: _ClassVar[BuildOptions.LogStreamingOption]
        STREAM_OFF: _ClassVar[BuildOptions.LogStreamingOption]
    STREAM_DEFAULT: BuildOptions.LogStreamingOption
    STREAM_ON: BuildOptions.LogStreamingOption
    STREAM_OFF: BuildOptions.LogStreamingOption
    class LoggingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGGING_UNSPECIFIED: _ClassVar[BuildOptions.LoggingMode]
        LEGACY: _ClassVar[BuildOptions.LoggingMode]
        GCS_ONLY: _ClassVar[BuildOptions.LoggingMode]
        STACKDRIVER_ONLY: _ClassVar[BuildOptions.LoggingMode]
        CLOUD_LOGGING_ONLY: _ClassVar[BuildOptions.LoggingMode]
        NONE: _ClassVar[BuildOptions.LoggingMode]
    LOGGING_UNSPECIFIED: BuildOptions.LoggingMode
    LEGACY: BuildOptions.LoggingMode
    GCS_ONLY: BuildOptions.LoggingMode
    STACKDRIVER_ONLY: BuildOptions.LoggingMode
    CLOUD_LOGGING_ONLY: BuildOptions.LoggingMode
    NONE: BuildOptions.LoggingMode
    class DefaultLogsBucketBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED: _ClassVar[BuildOptions.DefaultLogsBucketBehavior]
        REGIONAL_USER_OWNED_BUCKET: _ClassVar[BuildOptions.DefaultLogsBucketBehavior]
        LEGACY_BUCKET: _ClassVar[BuildOptions.DefaultLogsBucketBehavior]
    DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED: BuildOptions.DefaultLogsBucketBehavior
    REGIONAL_USER_OWNED_BUCKET: BuildOptions.DefaultLogsBucketBehavior
    LEGACY_BUCKET: BuildOptions.DefaultLogsBucketBehavior
    class PoolOption(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    SOURCE_PROVENANCE_HASH_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_VERIFY_OPTION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTION_OPTION_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTOMAP_SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    LOG_STREAMING_OPTION_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    POOL_FIELD_NUMBER: _ClassVar[int]
    LOGGING_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENV_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOGS_BUCKET_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    source_provenance_hash: _containers.RepeatedScalarFieldContainer[Hash.HashType]
    requested_verify_option: BuildOptions.VerifyOption
    machine_type: BuildOptions.MachineType
    disk_size_gb: int
    substitution_option: BuildOptions.SubstitutionOption
    dynamic_substitutions: bool
    automap_substitutions: bool
    log_streaming_option: BuildOptions.LogStreamingOption
    worker_pool: str
    pool: BuildOptions.PoolOption
    logging: BuildOptions.LoggingMode
    env: _containers.RepeatedScalarFieldContainer[str]
    secret_env: _containers.RepeatedScalarFieldContainer[str]
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    default_logs_bucket_behavior: BuildOptions.DefaultLogsBucketBehavior
    def __init__(self, source_provenance_hash: _Optional[_Iterable[_Union[Hash.HashType, str]]] = ..., requested_verify_option: _Optional[_Union[BuildOptions.VerifyOption, str]] = ..., machine_type: _Optional[_Union[BuildOptions.MachineType, str]] = ..., disk_size_gb: _Optional[int] = ..., substitution_option: _Optional[_Union[BuildOptions.SubstitutionOption, str]] = ..., dynamic_substitutions: bool = ..., automap_substitutions: bool = ..., log_streaming_option: _Optional[_Union[BuildOptions.LogStreamingOption, str]] = ..., worker_pool: _Optional[str] = ..., pool: _Optional[_Union[BuildOptions.PoolOption, _Mapping]] = ..., logging: _Optional[_Union[BuildOptions.LoggingMode, str]] = ..., env: _Optional[_Iterable[str]] = ..., secret_env: _Optional[_Iterable[str]] = ..., volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., default_logs_bucket_behavior: _Optional[_Union[BuildOptions.DefaultLogsBucketBehavior, str]] = ...) -> None: ...

class ReceiveTriggerWebhookRequest(_message.Message):
    __slots__ = ("name", "body", "project_id", "trigger", "secret")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    name: str
    body: _httpbody_pb2.HttpBody
    project_id: str
    trigger: str
    secret: str
    def __init__(self, name: _Optional[str] = ..., body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]] = ..., project_id: _Optional[str] = ..., trigger: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class ReceiveTriggerWebhookResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GitHubEnterpriseConfig(_message.Message):
    __slots__ = ("name", "host_url", "app_id", "create_time", "webhook_key", "peered_network", "secrets", "display_name", "ssl_ca")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_URL_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_KEY_FIELD_NUMBER: _ClassVar[int]
    PEERED_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SSL_CA_FIELD_NUMBER: _ClassVar[int]
    name: str
    host_url: str
    app_id: int
    create_time: _timestamp_pb2.Timestamp
    webhook_key: str
    peered_network: str
    secrets: GitHubEnterpriseSecrets
    display_name: str
    ssl_ca: str
    def __init__(self, name: _Optional[str] = ..., host_url: _Optional[str] = ..., app_id: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., webhook_key: _Optional[str] = ..., peered_network: _Optional[str] = ..., secrets: _Optional[_Union[GitHubEnterpriseSecrets, _Mapping]] = ..., display_name: _Optional[str] = ..., ssl_ca: _Optional[str] = ...) -> None: ...

class GitHubEnterpriseSecrets(_message.Message):
    __slots__ = ("private_key_version_name", "webhook_secret_version_name", "oauth_secret_version_name", "oauth_client_id_version_name")
    PRIVATE_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SECRET_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CLIENT_ID_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    private_key_version_name: str
    webhook_secret_version_name: str
    oauth_secret_version_name: str
    oauth_client_id_version_name: str
    def __init__(self, private_key_version_name: _Optional[str] = ..., webhook_secret_version_name: _Optional[str] = ..., oauth_secret_version_name: _Optional[str] = ..., oauth_client_id_version_name: _Optional[str] = ...) -> None: ...

class WorkerPool(_message.Message):
    __slots__ = ("name", "display_name", "uid", "annotations", "create_time", "update_time", "delete_time", "state", "private_pool_v1_config", "etag")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WorkerPool.State]
        CREATING: _ClassVar[WorkerPool.State]
        RUNNING: _ClassVar[WorkerPool.State]
        DELETING: _ClassVar[WorkerPool.State]
        DELETED: _ClassVar[WorkerPool.State]
        UPDATING: _ClassVar[WorkerPool.State]
    STATE_UNSPECIFIED: WorkerPool.State
    CREATING: WorkerPool.State
    RUNNING: WorkerPool.State
    DELETING: WorkerPool.State
    DELETED: WorkerPool.State
    UPDATING: WorkerPool.State
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_POOL_V1_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    annotations: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    state: WorkerPool.State
    private_pool_v1_config: PrivatePoolV1Config
    etag: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., uid: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[WorkerPool.State, str]] = ..., private_pool_v1_config: _Optional[_Union[PrivatePoolV1Config, _Mapping]] = ..., etag: _Optional[str] = ...) -> None: ...

class PrivatePoolV1Config(_message.Message):
    __slots__ = ("worker_config", "network_config", "private_service_connect")
    class WorkerConfig(_message.Message):
        __slots__ = ("machine_type", "disk_size_gb")
        MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        machine_type: str
        disk_size_gb: int
        def __init__(self, machine_type: _Optional[str] = ..., disk_size_gb: _Optional[int] = ...) -> None: ...
    class NetworkConfig(_message.Message):
        __slots__ = ("peered_network", "egress_option", "peered_network_ip_range")
        class EgressOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EGRESS_OPTION_UNSPECIFIED: _ClassVar[PrivatePoolV1Config.NetworkConfig.EgressOption]
            NO_PUBLIC_EGRESS: _ClassVar[PrivatePoolV1Config.NetworkConfig.EgressOption]
            PUBLIC_EGRESS: _ClassVar[PrivatePoolV1Config.NetworkConfig.EgressOption]
        EGRESS_OPTION_UNSPECIFIED: PrivatePoolV1Config.NetworkConfig.EgressOption
        NO_PUBLIC_EGRESS: PrivatePoolV1Config.NetworkConfig.EgressOption
        PUBLIC_EGRESS: PrivatePoolV1Config.NetworkConfig.EgressOption
        PEERED_NETWORK_FIELD_NUMBER: _ClassVar[int]
        EGRESS_OPTION_FIELD_NUMBER: _ClassVar[int]
        PEERED_NETWORK_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
        peered_network: str
        egress_option: PrivatePoolV1Config.NetworkConfig.EgressOption
        peered_network_ip_range: str
        def __init__(self, peered_network: _Optional[str] = ..., egress_option: _Optional[_Union[PrivatePoolV1Config.NetworkConfig.EgressOption, str]] = ..., peered_network_ip_range: _Optional[str] = ...) -> None: ...
    class PrivateServiceConnect(_message.Message):
        __slots__ = ("network_attachment", "public_ip_address_disabled", "route_all_traffic")
        NETWORK_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_IP_ADDRESS_DISABLED_FIELD_NUMBER: _ClassVar[int]
        ROUTE_ALL_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
        network_attachment: str
        public_ip_address_disabled: bool
        route_all_traffic: bool
        def __init__(self, network_attachment: _Optional[str] = ..., public_ip_address_disabled: bool = ..., route_all_traffic: bool = ...) -> None: ...
    WORKER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SERVICE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    worker_config: PrivatePoolV1Config.WorkerConfig
    network_config: PrivatePoolV1Config.NetworkConfig
    private_service_connect: PrivatePoolV1Config.PrivateServiceConnect
    def __init__(self, worker_config: _Optional[_Union[PrivatePoolV1Config.WorkerConfig, _Mapping]] = ..., network_config: _Optional[_Union[PrivatePoolV1Config.NetworkConfig, _Mapping]] = ..., private_service_connect: _Optional[_Union[PrivatePoolV1Config.PrivateServiceConnect, _Mapping]] = ...) -> None: ...

class CreateWorkerPoolRequest(_message.Message):
    __slots__ = ("parent", "worker_pool", "worker_pool_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    worker_pool: WorkerPool
    worker_pool_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., worker_pool: _Optional[_Union[WorkerPool, _Mapping]] = ..., worker_pool_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class GetWorkerPoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteWorkerPoolRequest(_message.Message):
    __slots__ = ("name", "etag", "allow_missing", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    allow_missing: bool
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., etag: _Optional[str] = ..., allow_missing: bool = ..., validate_only: bool = ...) -> None: ...

class UpdateWorkerPoolRequest(_message.Message):
    __slots__ = ("worker_pool", "update_mask", "validate_only")
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    worker_pool: WorkerPool
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    def __init__(self, worker_pool: _Optional[_Union[WorkerPool, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class ListWorkerPoolsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListWorkerPoolsResponse(_message.Message):
    __slots__ = ("worker_pools", "next_page_token")
    WORKER_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    worker_pools: _containers.RepeatedCompositeFieldContainer[WorkerPool]
    next_page_token: str
    def __init__(self, worker_pools: _Optional[_Iterable[_Union[WorkerPool, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateWorkerPoolOperationMetadata(_message.Message):
    __slots__ = ("worker_pool", "create_time", "complete_time")
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    worker_pool: str
    create_time: _timestamp_pb2.Timestamp
    complete_time: _timestamp_pb2.Timestamp
    def __init__(self, worker_pool: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateWorkerPoolOperationMetadata(_message.Message):
    __slots__ = ("worker_pool", "create_time", "complete_time")
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    worker_pool: str
    create_time: _timestamp_pb2.Timestamp
    complete_time: _timestamp_pb2.Timestamp
    def __init__(self, worker_pool: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteWorkerPoolOperationMetadata(_message.Message):
    __slots__ = ("worker_pool", "create_time", "complete_time")
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    worker_pool: str
    create_time: _timestamp_pb2.Timestamp
    complete_time: _timestamp_pb2.Timestamp
    def __init__(self, worker_pool: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
