from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.cloudbuild.v2 import cloudbuild_pb2 as _cloudbuild_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Connection(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'github_config', 'github_enterprise_config', 'gitlab_config', 'bitbucket_data_center_config', 'bitbucket_cloud_config', 'installation_state', 'disabled', 'reconciling', 'annotations', 'etag')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GITHUB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GITHUB_ENTERPRISE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GITLAB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BITBUCKET_DATA_CENTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BITBUCKET_CLOUD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_STATE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    github_config: GitHubConfig
    github_enterprise_config: GitHubEnterpriseConfig
    gitlab_config: GitLabConfig
    bitbucket_data_center_config: BitbucketDataCenterConfig
    bitbucket_cloud_config: BitbucketCloudConfig
    installation_state: InstallationState
    disabled: bool
    reconciling: bool
    annotations: _containers.ScalarMap[str, str]
    etag: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., github_config: _Optional[_Union[GitHubConfig, _Mapping]]=..., github_enterprise_config: _Optional[_Union[GitHubEnterpriseConfig, _Mapping]]=..., gitlab_config: _Optional[_Union[GitLabConfig, _Mapping]]=..., bitbucket_data_center_config: _Optional[_Union[BitbucketDataCenterConfig, _Mapping]]=..., bitbucket_cloud_config: _Optional[_Union[BitbucketCloudConfig, _Mapping]]=..., installation_state: _Optional[_Union[InstallationState, _Mapping]]=..., disabled: bool=..., reconciling: bool=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=...) -> None:
        ...

class InstallationState(_message.Message):
    __slots__ = ('stage', 'message', 'action_uri')

    class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STAGE_UNSPECIFIED: _ClassVar[InstallationState.Stage]
        PENDING_CREATE_APP: _ClassVar[InstallationState.Stage]
        PENDING_USER_OAUTH: _ClassVar[InstallationState.Stage]
        PENDING_INSTALL_APP: _ClassVar[InstallationState.Stage]
        COMPLETE: _ClassVar[InstallationState.Stage]
    STAGE_UNSPECIFIED: InstallationState.Stage
    PENDING_CREATE_APP: InstallationState.Stage
    PENDING_USER_OAUTH: InstallationState.Stage
    PENDING_INSTALL_APP: InstallationState.Stage
    COMPLETE: InstallationState.Stage
    STAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_URI_FIELD_NUMBER: _ClassVar[int]
    stage: InstallationState.Stage
    message: str
    action_uri: str

    def __init__(self, stage: _Optional[_Union[InstallationState.Stage, str]]=..., message: _Optional[str]=..., action_uri: _Optional[str]=...) -> None:
        ...

class FetchLinkableRepositoriesRequest(_message.Message):
    __slots__ = ('connection', 'page_size', 'page_token')
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    connection: str
    page_size: int
    page_token: str

    def __init__(self, connection: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchLinkableRepositoriesResponse(_message.Message):
    __slots__ = ('repositories', 'next_page_token')
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GitHubConfig(_message.Message):
    __slots__ = ('authorizer_credential', 'app_installation_id')
    AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    APP_INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    authorizer_credential: OAuthCredential
    app_installation_id: int

    def __init__(self, authorizer_credential: _Optional[_Union[OAuthCredential, _Mapping]]=..., app_installation_id: _Optional[int]=...) -> None:
        ...

class GitHubEnterpriseConfig(_message.Message):
    __slots__ = ('host_uri', 'api_key', 'app_id', 'app_slug', 'private_key_secret_version', 'webhook_secret_secret_version', 'app_installation_id', 'service_directory_config', 'ssl_ca', 'server_version')
    HOST_URI_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_SLUG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SSL_CA_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    host_uri: str
    api_key: str
    app_id: int
    app_slug: str
    private_key_secret_version: str
    webhook_secret_secret_version: str
    app_installation_id: int
    service_directory_config: ServiceDirectoryConfig
    ssl_ca: str
    server_version: str

    def __init__(self, host_uri: _Optional[str]=..., api_key: _Optional[str]=..., app_id: _Optional[int]=..., app_slug: _Optional[str]=..., private_key_secret_version: _Optional[str]=..., webhook_secret_secret_version: _Optional[str]=..., app_installation_id: _Optional[int]=..., service_directory_config: _Optional[_Union[ServiceDirectoryConfig, _Mapping]]=..., ssl_ca: _Optional[str]=..., server_version: _Optional[str]=...) -> None:
        ...

class GitLabConfig(_message.Message):
    __slots__ = ('host_uri', 'webhook_secret_secret_version', 'read_authorizer_credential', 'authorizer_credential', 'service_directory_config', 'ssl_ca', 'server_version')
    HOST_URI_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    READ_AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SSL_CA_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    host_uri: str
    webhook_secret_secret_version: str
    read_authorizer_credential: UserCredential
    authorizer_credential: UserCredential
    service_directory_config: ServiceDirectoryConfig
    ssl_ca: str
    server_version: str

    def __init__(self, host_uri: _Optional[str]=..., webhook_secret_secret_version: _Optional[str]=..., read_authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., service_directory_config: _Optional[_Union[ServiceDirectoryConfig, _Mapping]]=..., ssl_ca: _Optional[str]=..., server_version: _Optional[str]=...) -> None:
        ...

class BitbucketDataCenterConfig(_message.Message):
    __slots__ = ('host_uri', 'webhook_secret_secret_version', 'read_authorizer_credential', 'authorizer_credential', 'service_directory_config', 'ssl_ca', 'server_version')
    HOST_URI_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    READ_AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SSL_CA_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    host_uri: str
    webhook_secret_secret_version: str
    read_authorizer_credential: UserCredential
    authorizer_credential: UserCredential
    service_directory_config: ServiceDirectoryConfig
    ssl_ca: str
    server_version: str

    def __init__(self, host_uri: _Optional[str]=..., webhook_secret_secret_version: _Optional[str]=..., read_authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., service_directory_config: _Optional[_Union[ServiceDirectoryConfig, _Mapping]]=..., ssl_ca: _Optional[str]=..., server_version: _Optional[str]=...) -> None:
        ...

class BitbucketCloudConfig(_message.Message):
    __slots__ = ('workspace', 'webhook_secret_secret_version', 'read_authorizer_credential', 'authorizer_credential')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    READ_AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    webhook_secret_secret_version: str
    read_authorizer_credential: UserCredential
    authorizer_credential: UserCredential

    def __init__(self, workspace: _Optional[str]=..., webhook_secret_secret_version: _Optional[str]=..., read_authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=...) -> None:
        ...

class ServiceDirectoryConfig(_message.Message):
    __slots__ = ('service',)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: str

    def __init__(self, service: _Optional[str]=...) -> None:
        ...

class Repository(_message.Message):
    __slots__ = ('name', 'remote_uri', 'create_time', 'update_time', 'annotations', 'etag', 'webhook_id')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URI_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    remote_uri: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    etag: str
    webhook_id: str

    def __init__(self, name: _Optional[str]=..., remote_uri: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., webhook_id: _Optional[str]=...) -> None:
        ...

class OAuthCredential(_message.Message):
    __slots__ = ('oauth_token_secret_version', 'username')
    OAUTH_TOKEN_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    oauth_token_secret_version: str
    username: str

    def __init__(self, oauth_token_secret_version: _Optional[str]=..., username: _Optional[str]=...) -> None:
        ...

class UserCredential(_message.Message):
    __slots__ = ('user_token_secret_version', 'username')
    USER_TOKEN_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    user_token_secret_version: str
    username: str

    def __init__(self, user_token_secret_version: _Optional[str]=..., username: _Optional[str]=...) -> None:
        ...

class CreateConnectionRequest(_message.Message):
    __slots__ = ('parent', 'connection', 'connection_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection: Connection
    connection_id: str

    def __init__(self, parent: _Optional[str]=..., connection: _Optional[_Union[Connection, _Mapping]]=..., connection_id: _Optional[str]=...) -> None:
        ...

class GetConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConnectionsResponse(_message.Message):
    __slots__ = ('connections', 'next_page_token')
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    next_page_token: str

    def __init__(self, connections: _Optional[_Iterable[_Union[Connection, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateConnectionRequest(_message.Message):
    __slots__ = ('connection', 'update_mask', 'allow_missing', 'etag')
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    connection: Connection
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    etag: str

    def __init__(self, connection: _Optional[_Union[Connection, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=..., etag: _Optional[str]=...) -> None:
        ...

class DeleteConnectionRequest(_message.Message):
    __slots__ = ('name', 'etag', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class CreateRepositoryRequest(_message.Message):
    __slots__ = ('parent', 'repository', 'repository_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    repository: Repository
    repository_id: str

    def __init__(self, parent: _Optional[str]=..., repository: _Optional[_Union[Repository, _Mapping]]=..., repository_id: _Optional[str]=...) -> None:
        ...

class BatchCreateRepositoriesRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateRepositoryRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateRepositoryRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateRepositoriesResponse(_message.Message):
    __slots__ = ('repositories',)
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=...) -> None:
        ...

class GetRepositoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRepositoriesRequest(_message.Message):
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

class ListRepositoriesResponse(_message.Message):
    __slots__ = ('repositories', 'next_page_token')
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteRepositoryRequest(_message.Message):
    __slots__ = ('name', 'etag', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class FetchReadWriteTokenRequest(_message.Message):
    __slots__ = ('repository',)
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    repository: str

    def __init__(self, repository: _Optional[str]=...) -> None:
        ...

class FetchReadTokenRequest(_message.Message):
    __slots__ = ('repository',)
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    repository: str

    def __init__(self, repository: _Optional[str]=...) -> None:
        ...

class FetchReadTokenResponse(_message.Message):
    __slots__ = ('token', 'expiration_time')
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    token: str
    expiration_time: _timestamp_pb2.Timestamp

    def __init__(self, token: _Optional[str]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class FetchReadWriteTokenResponse(_message.Message):
    __slots__ = ('token', 'expiration_time')
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    token: str
    expiration_time: _timestamp_pb2.Timestamp

    def __init__(self, token: _Optional[str]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ProcessWebhookRequest(_message.Message):
    __slots__ = ('parent', 'body', 'webhook_key')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    body: _httpbody_pb2.HttpBody
    webhook_key: str

    def __init__(self, parent: _Optional[str]=..., body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]]=..., webhook_key: _Optional[str]=...) -> None:
        ...

class FetchGitRefsRequest(_message.Message):
    __slots__ = ('repository', 'ref_type')

    class RefType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REF_TYPE_UNSPECIFIED: _ClassVar[FetchGitRefsRequest.RefType]
        TAG: _ClassVar[FetchGitRefsRequest.RefType]
        BRANCH: _ClassVar[FetchGitRefsRequest.RefType]
    REF_TYPE_UNSPECIFIED: FetchGitRefsRequest.RefType
    TAG: FetchGitRefsRequest.RefType
    BRANCH: FetchGitRefsRequest.RefType
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REF_TYPE_FIELD_NUMBER: _ClassVar[int]
    repository: str
    ref_type: FetchGitRefsRequest.RefType

    def __init__(self, repository: _Optional[str]=..., ref_type: _Optional[_Union[FetchGitRefsRequest.RefType, str]]=...) -> None:
        ...

class FetchGitRefsResponse(_message.Message):
    __slots__ = ('ref_names',)
    REF_NAMES_FIELD_NUMBER: _ClassVar[int]
    ref_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, ref_names: _Optional[_Iterable[str]]=...) -> None:
        ...