from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
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
    __slots__ = ('github_config', 'github_enterprise_config', 'gitlab_config', 'gitlab_enterprise_config', 'name', 'create_time', 'update_time', 'delete_time', 'labels', 'installation_state', 'disabled', 'reconciling', 'annotations', 'etag', 'uid', 'crypto_key_config')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    GITHUB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GITHUB_ENTERPRISE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GITLAB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GITLAB_ENTERPRISE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_STATE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    github_config: GitHubConfig
    github_enterprise_config: GitHubEnterpriseConfig
    gitlab_config: GitLabConfig
    gitlab_enterprise_config: GitLabEnterpriseConfig
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    installation_state: InstallationState
    disabled: bool
    reconciling: bool
    annotations: _containers.ScalarMap[str, str]
    etag: str
    uid: str
    crypto_key_config: CryptoKeyConfig

    def __init__(self, github_config: _Optional[_Union[GitHubConfig, _Mapping]]=..., github_enterprise_config: _Optional[_Union[GitHubEnterpriseConfig, _Mapping]]=..., gitlab_config: _Optional[_Union[GitLabConfig, _Mapping]]=..., gitlab_enterprise_config: _Optional[_Union[GitLabEnterpriseConfig, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., installation_state: _Optional[_Union[InstallationState, _Mapping]]=..., disabled: bool=..., reconciling: bool=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., uid: _Optional[str]=..., crypto_key_config: _Optional[_Union[CryptoKeyConfig, _Mapping]]=...) -> None:
        ...

class CryptoKeyConfig(_message.Message):
    __slots__ = ('key_reference',)
    KEY_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    key_reference: str

    def __init__(self, key_reference: _Optional[str]=...) -> None:
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

class GitHubConfig(_message.Message):
    __slots__ = ('github_app', 'authorizer_credential', 'app_installation_id', 'installation_uri')

    class GitHubApp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GIT_HUB_APP_UNSPECIFIED: _ClassVar[GitHubConfig.GitHubApp]
        DEVELOPER_CONNECT: _ClassVar[GitHubConfig.GitHubApp]
        FIREBASE: _ClassVar[GitHubConfig.GitHubApp]
    GIT_HUB_APP_UNSPECIFIED: GitHubConfig.GitHubApp
    DEVELOPER_CONNECT: GitHubConfig.GitHubApp
    FIREBASE: GitHubConfig.GitHubApp
    GITHUB_APP_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    APP_INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_URI_FIELD_NUMBER: _ClassVar[int]
    github_app: GitHubConfig.GitHubApp
    authorizer_credential: OAuthCredential
    app_installation_id: int
    installation_uri: str

    def __init__(self, github_app: _Optional[_Union[GitHubConfig.GitHubApp, str]]=..., authorizer_credential: _Optional[_Union[OAuthCredential, _Mapping]]=..., app_installation_id: _Optional[int]=..., installation_uri: _Optional[str]=...) -> None:
        ...

class GitHubEnterpriseConfig(_message.Message):
    __slots__ = ('host_uri', 'app_id', 'app_slug', 'private_key_secret_version', 'webhook_secret_secret_version', 'app_installation_id', 'installation_uri', 'service_directory_config', 'server_version', 'ssl_ca_certificate')
    HOST_URI_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_SLUG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_URI_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    SSL_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    host_uri: str
    app_id: int
    app_slug: str
    private_key_secret_version: str
    webhook_secret_secret_version: str
    app_installation_id: int
    installation_uri: str
    service_directory_config: ServiceDirectoryConfig
    server_version: str
    ssl_ca_certificate: str

    def __init__(self, host_uri: _Optional[str]=..., app_id: _Optional[int]=..., app_slug: _Optional[str]=..., private_key_secret_version: _Optional[str]=..., webhook_secret_secret_version: _Optional[str]=..., app_installation_id: _Optional[int]=..., installation_uri: _Optional[str]=..., service_directory_config: _Optional[_Union[ServiceDirectoryConfig, _Mapping]]=..., server_version: _Optional[str]=..., ssl_ca_certificate: _Optional[str]=...) -> None:
        ...

class ServiceDirectoryConfig(_message.Message):
    __slots__ = ('service',)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: str

    def __init__(self, service: _Optional[str]=...) -> None:
        ...

class OAuthCredential(_message.Message):
    __slots__ = ('oauth_token_secret_version', 'username')
    OAUTH_TOKEN_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    oauth_token_secret_version: str
    username: str

    def __init__(self, oauth_token_secret_version: _Optional[str]=..., username: _Optional[str]=...) -> None:
        ...

class GitLabConfig(_message.Message):
    __slots__ = ('webhook_secret_secret_version', 'read_authorizer_credential', 'authorizer_credential')
    WEBHOOK_SECRET_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    READ_AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    webhook_secret_secret_version: str
    read_authorizer_credential: UserCredential
    authorizer_credential: UserCredential

    def __init__(self, webhook_secret_secret_version: _Optional[str]=..., read_authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=...) -> None:
        ...

class UserCredential(_message.Message):
    __slots__ = ('user_token_secret_version', 'username')
    USER_TOKEN_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    user_token_secret_version: str
    username: str

    def __init__(self, user_token_secret_version: _Optional[str]=..., username: _Optional[str]=...) -> None:
        ...

class GitLabEnterpriseConfig(_message.Message):
    __slots__ = ('host_uri', 'webhook_secret_secret_version', 'read_authorizer_credential', 'authorizer_credential', 'service_directory_config', 'ssl_ca_certificate', 'server_version')
    HOST_URI_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    READ_AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SSL_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    host_uri: str
    webhook_secret_secret_version: str
    read_authorizer_credential: UserCredential
    authorizer_credential: UserCredential
    service_directory_config: ServiceDirectoryConfig
    ssl_ca_certificate: str
    server_version: str

    def __init__(self, host_uri: _Optional[str]=..., webhook_secret_secret_version: _Optional[str]=..., read_authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., authorizer_credential: _Optional[_Union[UserCredential, _Mapping]]=..., service_directory_config: _Optional[_Union[ServiceDirectoryConfig, _Mapping]]=..., ssl_ca_certificate: _Optional[str]=..., server_version: _Optional[str]=...) -> None:
        ...

class ListConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListConnectionsResponse(_message.Message):
    __slots__ = ('connections', 'next_page_token', 'unreachable')
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, connections: _Optional[_Iterable[_Union[Connection, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateConnectionRequest(_message.Message):
    __slots__ = ('parent', 'connection_id', 'connection', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection_id: str
    connection: Connection
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., connection_id: _Optional[str]=..., connection: _Optional[_Union[Connection, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateConnectionRequest(_message.Message):
    __slots__ = ('update_mask', 'connection', 'request_id', 'allow_missing', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    connection: Connection
    request_id: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., connection: _Optional[_Union[Connection, _Mapping]]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteConnectionRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class GitRepositoryLink(_message.Message):
    __slots__ = ('name', 'clone_uri', 'create_time', 'update_time', 'delete_time', 'labels', 'etag', 'reconciling', 'annotations', 'uid', 'webhook_id')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLONE_URI_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    clone_uri: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    etag: str
    reconciling: bool
    annotations: _containers.ScalarMap[str, str]
    uid: str
    webhook_id: str

    def __init__(self, name: _Optional[str]=..., clone_uri: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., reconciling: bool=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., webhook_id: _Optional[str]=...) -> None:
        ...

class CreateGitRepositoryLinkRequest(_message.Message):
    __slots__ = ('parent', 'git_repository_link', 'git_repository_link_id', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GIT_REPOSITORY_LINK_FIELD_NUMBER: _ClassVar[int]
    GIT_REPOSITORY_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    git_repository_link: GitRepositoryLink
    git_repository_link_id: str
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., git_repository_link: _Optional[_Union[GitRepositoryLink, _Mapping]]=..., git_repository_link_id: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class DeleteGitRepositoryLinkRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class ListGitRepositoryLinksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListGitRepositoryLinksResponse(_message.Message):
    __slots__ = ('git_repository_links', 'next_page_token', 'unreachable')
    GIT_REPOSITORY_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    git_repository_links: _containers.RepeatedCompositeFieldContainer[GitRepositoryLink]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, git_repository_links: _Optional[_Iterable[_Union[GitRepositoryLink, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetGitRepositoryLinkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FetchReadWriteTokenRequest(_message.Message):
    __slots__ = ('git_repository_link',)
    GIT_REPOSITORY_LINK_FIELD_NUMBER: _ClassVar[int]
    git_repository_link: str

    def __init__(self, git_repository_link: _Optional[str]=...) -> None:
        ...

class FetchReadTokenRequest(_message.Message):
    __slots__ = ('git_repository_link',)
    GIT_REPOSITORY_LINK_FIELD_NUMBER: _ClassVar[int]
    git_repository_link: str

    def __init__(self, git_repository_link: _Optional[str]=...) -> None:
        ...

class FetchReadTokenResponse(_message.Message):
    __slots__ = ('token', 'expiration_time', 'git_username')
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    GIT_USERNAME_FIELD_NUMBER: _ClassVar[int]
    token: str
    expiration_time: _timestamp_pb2.Timestamp
    git_username: str

    def __init__(self, token: _Optional[str]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., git_username: _Optional[str]=...) -> None:
        ...

class FetchReadWriteTokenResponse(_message.Message):
    __slots__ = ('token', 'expiration_time', 'git_username')
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    GIT_USERNAME_FIELD_NUMBER: _ClassVar[int]
    token: str
    expiration_time: _timestamp_pb2.Timestamp
    git_username: str

    def __init__(self, token: _Optional[str]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., git_username: _Optional[str]=...) -> None:
        ...

class FetchLinkableGitRepositoriesRequest(_message.Message):
    __slots__ = ('connection', 'page_size', 'page_token')
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    connection: str
    page_size: int
    page_token: str

    def __init__(self, connection: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchLinkableGitRepositoriesResponse(_message.Message):
    __slots__ = ('linkable_git_repositories', 'next_page_token')
    LINKABLE_GIT_REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    linkable_git_repositories: _containers.RepeatedCompositeFieldContainer[LinkableGitRepository]
    next_page_token: str

    def __init__(self, linkable_git_repositories: _Optional[_Iterable[_Union[LinkableGitRepository, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class LinkableGitRepository(_message.Message):
    __slots__ = ('clone_uri',)
    CLONE_URI_FIELD_NUMBER: _ClassVar[int]
    clone_uri: str

    def __init__(self, clone_uri: _Optional[str]=...) -> None:
        ...

class FetchGitHubInstallationsRequest(_message.Message):
    __slots__ = ('connection',)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: str

    def __init__(self, connection: _Optional[str]=...) -> None:
        ...

class FetchGitHubInstallationsResponse(_message.Message):
    __slots__ = ('installations',)

    class Installation(_message.Message):
        __slots__ = ('id', 'name', 'type')
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        type: str

        def __init__(self, id: _Optional[int]=..., name: _Optional[str]=..., type: _Optional[str]=...) -> None:
            ...
    INSTALLATIONS_FIELD_NUMBER: _ClassVar[int]
    installations: _containers.RepeatedCompositeFieldContainer[FetchGitHubInstallationsResponse.Installation]

    def __init__(self, installations: _Optional[_Iterable[_Union[FetchGitHubInstallationsResponse.Installation, _Mapping]]]=...) -> None:
        ...

class FetchGitRefsRequest(_message.Message):
    __slots__ = ('git_repository_link', 'ref_type', 'page_size', 'page_token')

    class RefType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REF_TYPE_UNSPECIFIED: _ClassVar[FetchGitRefsRequest.RefType]
        TAG: _ClassVar[FetchGitRefsRequest.RefType]
        BRANCH: _ClassVar[FetchGitRefsRequest.RefType]
    REF_TYPE_UNSPECIFIED: FetchGitRefsRequest.RefType
    TAG: FetchGitRefsRequest.RefType
    BRANCH: FetchGitRefsRequest.RefType
    GIT_REPOSITORY_LINK_FIELD_NUMBER: _ClassVar[int]
    REF_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    git_repository_link: str
    ref_type: FetchGitRefsRequest.RefType
    page_size: int
    page_token: str

    def __init__(self, git_repository_link: _Optional[str]=..., ref_type: _Optional[_Union[FetchGitRefsRequest.RefType, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchGitRefsResponse(_message.Message):
    __slots__ = ('ref_names', 'next_page_token')
    REF_NAMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ref_names: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, ref_names: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...