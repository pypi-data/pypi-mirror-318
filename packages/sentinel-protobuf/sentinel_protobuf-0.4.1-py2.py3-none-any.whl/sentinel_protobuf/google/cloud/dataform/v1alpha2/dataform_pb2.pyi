from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Repository(_message.Message):
    __slots__ = ('name', 'git_remote_settings')

    class GitRemoteSettings(_message.Message):
        __slots__ = ('url', 'default_branch', 'authentication_token_secret_version', 'token_status')

        class TokenStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TOKEN_STATUS_UNSPECIFIED: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
            NOT_FOUND: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
            INVALID: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
            VALID: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
        TOKEN_STATUS_UNSPECIFIED: Repository.GitRemoteSettings.TokenStatus
        NOT_FOUND: Repository.GitRemoteSettings.TokenStatus
        INVALID: Repository.GitRemoteSettings.TokenStatus
        VALID: Repository.GitRemoteSettings.TokenStatus
        URL_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_TOKEN_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
        TOKEN_STATUS_FIELD_NUMBER: _ClassVar[int]
        url: str
        default_branch: str
        authentication_token_secret_version: str
        token_status: Repository.GitRemoteSettings.TokenStatus

        def __init__(self, url: _Optional[str]=..., default_branch: _Optional[str]=..., authentication_token_secret_version: _Optional[str]=..., token_status: _Optional[_Union[Repository.GitRemoteSettings.TokenStatus, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    GIT_REMOTE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    git_remote_settings: Repository.GitRemoteSettings

    def __init__(self, name: _Optional[str]=..., git_remote_settings: _Optional[_Union[Repository.GitRemoteSettings, _Mapping]]=...) -> None:
        ...

class ListRepositoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRepositoriesResponse(_message.Message):
    __slots__ = ('repositories', 'next_page_token', 'unreachable')
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRepositoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
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

class UpdateRepositoryRequest(_message.Message):
    __slots__ = ('update_mask', 'repository')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    repository: Repository

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., repository: _Optional[_Union[Repository, _Mapping]]=...) -> None:
        ...

class DeleteRepositoryRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class FetchRemoteBranchesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FetchRemoteBranchesResponse(_message.Message):
    __slots__ = ('branches',)
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    branches: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, branches: _Optional[_Iterable[str]]=...) -> None:
        ...

class Workspace(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWorkspacesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListWorkspacesResponse(_message.Message):
    __slots__ = ('workspaces', 'next_page_token', 'unreachable')
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[Workspace]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workspaces: _Optional[_Iterable[_Union[Workspace, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWorkspaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWorkspaceRequest(_message.Message):
    __slots__ = ('parent', 'workspace', 'workspace_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workspace: Workspace
    workspace_id: str

    def __init__(self, parent: _Optional[str]=..., workspace: _Optional[_Union[Workspace, _Mapping]]=..., workspace_id: _Optional[str]=...) -> None:
        ...

class DeleteWorkspaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CommitAuthor(_message.Message):
    __slots__ = ('name', 'email_address')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    email_address: str

    def __init__(self, name: _Optional[str]=..., email_address: _Optional[str]=...) -> None:
        ...

class PullGitCommitsRequest(_message.Message):
    __slots__ = ('name', 'remote_branch', 'author')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    remote_branch: str
    author: CommitAuthor

    def __init__(self, name: _Optional[str]=..., remote_branch: _Optional[str]=..., author: _Optional[_Union[CommitAuthor, _Mapping]]=...) -> None:
        ...

class PushGitCommitsRequest(_message.Message):
    __slots__ = ('name', 'remote_branch')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    remote_branch: str

    def __init__(self, name: _Optional[str]=..., remote_branch: _Optional[str]=...) -> None:
        ...

class FetchFileGitStatusesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FetchFileGitStatusesResponse(_message.Message):
    __slots__ = ('uncommitted_file_changes',)

    class UncommittedFileChange(_message.Message):
        __slots__ = ('path', 'state')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            ADDED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            DELETED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            MODIFIED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            HAS_CONFLICTS: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
        STATE_UNSPECIFIED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        ADDED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        DELETED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        MODIFIED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        HAS_CONFLICTS: FetchFileGitStatusesResponse.UncommittedFileChange.State
        PATH_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        path: str
        state: FetchFileGitStatusesResponse.UncommittedFileChange.State

        def __init__(self, path: _Optional[str]=..., state: _Optional[_Union[FetchFileGitStatusesResponse.UncommittedFileChange.State, str]]=...) -> None:
            ...
    UNCOMMITTED_FILE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    uncommitted_file_changes: _containers.RepeatedCompositeFieldContainer[FetchFileGitStatusesResponse.UncommittedFileChange]

    def __init__(self, uncommitted_file_changes: _Optional[_Iterable[_Union[FetchFileGitStatusesResponse.UncommittedFileChange, _Mapping]]]=...) -> None:
        ...

class FetchGitAheadBehindRequest(_message.Message):
    __slots__ = ('name', 'remote_branch')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    remote_branch: str

    def __init__(self, name: _Optional[str]=..., remote_branch: _Optional[str]=...) -> None:
        ...

class FetchGitAheadBehindResponse(_message.Message):
    __slots__ = ('commits_ahead', 'commits_behind')
    COMMITS_AHEAD_FIELD_NUMBER: _ClassVar[int]
    COMMITS_BEHIND_FIELD_NUMBER: _ClassVar[int]
    commits_ahead: int
    commits_behind: int

    def __init__(self, commits_ahead: _Optional[int]=..., commits_behind: _Optional[int]=...) -> None:
        ...

class CommitWorkspaceChangesRequest(_message.Message):
    __slots__ = ('name', 'author', 'commit_message', 'paths')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    name: str
    author: CommitAuthor
    commit_message: str
    paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., author: _Optional[_Union[CommitAuthor, _Mapping]]=..., commit_message: _Optional[str]=..., paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class ResetWorkspaceChangesRequest(_message.Message):
    __slots__ = ('name', 'paths', 'clean')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    CLEAN_FIELD_NUMBER: _ClassVar[int]
    name: str
    paths: _containers.RepeatedScalarFieldContainer[str]
    clean: bool

    def __init__(self, name: _Optional[str]=..., paths: _Optional[_Iterable[str]]=..., clean: bool=...) -> None:
        ...

class FetchFileDiffRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class FetchFileDiffResponse(_message.Message):
    __slots__ = ('formatted_diff',)
    FORMATTED_DIFF_FIELD_NUMBER: _ClassVar[int]
    formatted_diff: str

    def __init__(self, formatted_diff: _Optional[str]=...) -> None:
        ...

class QueryDirectoryContentsRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'page_size', 'page_token')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    page_size: int
    page_token: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryDirectoryContentsResponse(_message.Message):
    __slots__ = ('directory_entries', 'next_page_token')

    class DirectoryEntry(_message.Message):
        __slots__ = ('file', 'directory')
        FILE_FIELD_NUMBER: _ClassVar[int]
        DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        file: str
        directory: str

        def __init__(self, file: _Optional[str]=..., directory: _Optional[str]=...) -> None:
            ...
    DIRECTORY_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    directory_entries: _containers.RepeatedCompositeFieldContainer[QueryDirectoryContentsResponse.DirectoryEntry]
    next_page_token: str

    def __init__(self, directory_entries: _Optional[_Iterable[_Union[QueryDirectoryContentsResponse.DirectoryEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class MakeDirectoryRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class MakeDirectoryResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemoveDirectoryRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class MoveDirectoryRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'new_path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    new_path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., new_path: _Optional[str]=...) -> None:
        ...

class MoveDirectoryResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReadFileRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class ReadFileResponse(_message.Message):
    __slots__ = ('file_contents',)
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    file_contents: bytes

    def __init__(self, file_contents: _Optional[bytes]=...) -> None:
        ...

class RemoveFileRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class MoveFileRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'new_path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    new_path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., new_path: _Optional[str]=...) -> None:
        ...

class MoveFileResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WriteFileRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'contents')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    contents: bytes

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., contents: _Optional[bytes]=...) -> None:
        ...

class WriteFileResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class InstallNpmPackagesRequest(_message.Message):
    __slots__ = ('workspace',)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: str

    def __init__(self, workspace: _Optional[str]=...) -> None:
        ...

class InstallNpmPackagesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CompilationResult(_message.Message):
    __slots__ = ('name', 'git_commitish', 'workspace', 'code_compilation_config', 'dataform_core_version', 'compilation_errors')

    class CodeCompilationConfig(_message.Message):
        __slots__ = ('default_database', 'default_schema', 'default_location', 'assertion_schema', 'vars', 'database_suffix', 'schema_suffix', 'table_prefix')

        class VarsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        DEFAULT_DATABASE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_LOCATION_FIELD_NUMBER: _ClassVar[int]
        ASSERTION_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        VARS_FIELD_NUMBER: _ClassVar[int]
        DATABASE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_SUFFIX_FIELD_NUMBER: _ClassVar[int]
        TABLE_PREFIX_FIELD_NUMBER: _ClassVar[int]
        default_database: str
        default_schema: str
        default_location: str
        assertion_schema: str
        vars: _containers.ScalarMap[str, str]
        database_suffix: str
        schema_suffix: str
        table_prefix: str

        def __init__(self, default_database: _Optional[str]=..., default_schema: _Optional[str]=..., default_location: _Optional[str]=..., assertion_schema: _Optional[str]=..., vars: _Optional[_Mapping[str, str]]=..., database_suffix: _Optional[str]=..., schema_suffix: _Optional[str]=..., table_prefix: _Optional[str]=...) -> None:
            ...

    class CompilationError(_message.Message):
        __slots__ = ('message', 'stack', 'path', 'action_target')
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        STACK_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        ACTION_TARGET_FIELD_NUMBER: _ClassVar[int]
        message: str
        stack: str
        path: str
        action_target: Target

        def __init__(self, message: _Optional[str]=..., stack: _Optional[str]=..., path: _Optional[str]=..., action_target: _Optional[_Union[Target, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMITISH_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    CODE_COMPILATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATAFORM_CORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    git_commitish: str
    workspace: str
    code_compilation_config: CompilationResult.CodeCompilationConfig
    dataform_core_version: str
    compilation_errors: _containers.RepeatedCompositeFieldContainer[CompilationResult.CompilationError]

    def __init__(self, name: _Optional[str]=..., git_commitish: _Optional[str]=..., workspace: _Optional[str]=..., code_compilation_config: _Optional[_Union[CompilationResult.CodeCompilationConfig, _Mapping]]=..., dataform_core_version: _Optional[str]=..., compilation_errors: _Optional[_Iterable[_Union[CompilationResult.CompilationError, _Mapping]]]=...) -> None:
        ...

class ListCompilationResultsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCompilationResultsResponse(_message.Message):
    __slots__ = ('compilation_results', 'next_page_token', 'unreachable')
    COMPILATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    compilation_results: _containers.RepeatedCompositeFieldContainer[CompilationResult]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, compilation_results: _Optional[_Iterable[_Union[CompilationResult, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCompilationResultRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCompilationResultRequest(_message.Message):
    __slots__ = ('parent', 'compilation_result')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    compilation_result: CompilationResult

    def __init__(self, parent: _Optional[str]=..., compilation_result: _Optional[_Union[CompilationResult, _Mapping]]=...) -> None:
        ...

class Target(_message.Message):
    __slots__ = ('database', 'schema', 'name')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    database: str
    schema: str
    name: str

    def __init__(self, database: _Optional[str]=..., schema: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class RelationDescriptor(_message.Message):
    __slots__ = ('description', 'columns', 'bigquery_labels')

    class ColumnDescriptor(_message.Message):
        __slots__ = ('path', 'description', 'bigquery_policy_tags')
        PATH_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_POLICY_TAGS_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedScalarFieldContainer[str]
        description: str
        bigquery_policy_tags: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, path: _Optional[_Iterable[str]]=..., description: _Optional[str]=..., bigquery_policy_tags: _Optional[_Iterable[str]]=...) -> None:
            ...

    class BigqueryLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_LABELS_FIELD_NUMBER: _ClassVar[int]
    description: str
    columns: _containers.RepeatedCompositeFieldContainer[RelationDescriptor.ColumnDescriptor]
    bigquery_labels: _containers.ScalarMap[str, str]

    def __init__(self, description: _Optional[str]=..., columns: _Optional[_Iterable[_Union[RelationDescriptor.ColumnDescriptor, _Mapping]]]=..., bigquery_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class CompilationResultAction(_message.Message):
    __slots__ = ('target', 'canonical_target', 'file_path', 'relation', 'operations', 'assertion', 'declaration')

    class Relation(_message.Message):
        __slots__ = ('dependency_targets', 'disabled', 'tags', 'relation_descriptor', 'relation_type', 'select_query', 'pre_operations', 'post_operations', 'incremental_table_config', 'partition_expression', 'cluster_expressions', 'partition_expiration_days', 'require_partition_filter', 'additional_options')

        class RelationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RELATION_TYPE_UNSPECIFIED: _ClassVar[CompilationResultAction.Relation.RelationType]
            TABLE: _ClassVar[CompilationResultAction.Relation.RelationType]
            VIEW: _ClassVar[CompilationResultAction.Relation.RelationType]
            INCREMENTAL_TABLE: _ClassVar[CompilationResultAction.Relation.RelationType]
            MATERIALIZED_VIEW: _ClassVar[CompilationResultAction.Relation.RelationType]
        RELATION_TYPE_UNSPECIFIED: CompilationResultAction.Relation.RelationType
        TABLE: CompilationResultAction.Relation.RelationType
        VIEW: CompilationResultAction.Relation.RelationType
        INCREMENTAL_TABLE: CompilationResultAction.Relation.RelationType
        MATERIALIZED_VIEW: CompilationResultAction.Relation.RelationType

        class IncrementalTableConfig(_message.Message):
            __slots__ = ('incremental_select_query', 'refresh_disabled', 'unique_key_parts', 'update_partition_filter', 'incremental_pre_operations', 'incremental_post_operations')
            INCREMENTAL_SELECT_QUERY_FIELD_NUMBER: _ClassVar[int]
            REFRESH_DISABLED_FIELD_NUMBER: _ClassVar[int]
            UNIQUE_KEY_PARTS_FIELD_NUMBER: _ClassVar[int]
            UPDATE_PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
            INCREMENTAL_PRE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
            INCREMENTAL_POST_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
            incremental_select_query: str
            refresh_disabled: bool
            unique_key_parts: _containers.RepeatedScalarFieldContainer[str]
            update_partition_filter: str
            incremental_pre_operations: _containers.RepeatedScalarFieldContainer[str]
            incremental_post_operations: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, incremental_select_query: _Optional[str]=..., refresh_disabled: bool=..., unique_key_parts: _Optional[_Iterable[str]]=..., update_partition_filter: _Optional[str]=..., incremental_pre_operations: _Optional[_Iterable[str]]=..., incremental_post_operations: _Optional[_Iterable[str]]=...) -> None:
                ...

        class AdditionalOptionsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        RELATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        SELECT_QUERY_FIELD_NUMBER: _ClassVar[int]
        PRE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        POST_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_TABLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PARTITION_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        PARTITION_EXPIRATION_DAYS_FIELD_NUMBER: _ClassVar[int]
        REQUIRE_PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        disabled: bool
        tags: _containers.RepeatedScalarFieldContainer[str]
        relation_descriptor: RelationDescriptor
        relation_type: CompilationResultAction.Relation.RelationType
        select_query: str
        pre_operations: _containers.RepeatedScalarFieldContainer[str]
        post_operations: _containers.RepeatedScalarFieldContainer[str]
        incremental_table_config: CompilationResultAction.Relation.IncrementalTableConfig
        partition_expression: str
        cluster_expressions: _containers.RepeatedScalarFieldContainer[str]
        partition_expiration_days: int
        require_partition_filter: bool
        additional_options: _containers.ScalarMap[str, str]

        def __init__(self, dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., disabled: bool=..., tags: _Optional[_Iterable[str]]=..., relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=..., relation_type: _Optional[_Union[CompilationResultAction.Relation.RelationType, str]]=..., select_query: _Optional[str]=..., pre_operations: _Optional[_Iterable[str]]=..., post_operations: _Optional[_Iterable[str]]=..., incremental_table_config: _Optional[_Union[CompilationResultAction.Relation.IncrementalTableConfig, _Mapping]]=..., partition_expression: _Optional[str]=..., cluster_expressions: _Optional[_Iterable[str]]=..., partition_expiration_days: _Optional[int]=..., require_partition_filter: bool=..., additional_options: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class Operations(_message.Message):
        __slots__ = ('dependency_targets', 'disabled', 'tags', 'relation_descriptor', 'queries', 'has_output')
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        QUERIES_FIELD_NUMBER: _ClassVar[int]
        HAS_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        disabled: bool
        tags: _containers.RepeatedScalarFieldContainer[str]
        relation_descriptor: RelationDescriptor
        queries: _containers.RepeatedScalarFieldContainer[str]
        has_output: bool

        def __init__(self, dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., disabled: bool=..., tags: _Optional[_Iterable[str]]=..., relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=..., queries: _Optional[_Iterable[str]]=..., has_output: bool=...) -> None:
            ...

    class Assertion(_message.Message):
        __slots__ = ('dependency_targets', 'parent_action', 'disabled', 'tags', 'select_query', 'relation_descriptor')
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        PARENT_ACTION_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        SELECT_QUERY_FIELD_NUMBER: _ClassVar[int]
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        parent_action: Target
        disabled: bool
        tags: _containers.RepeatedScalarFieldContainer[str]
        select_query: str
        relation_descriptor: RelationDescriptor

        def __init__(self, dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., parent_action: _Optional[_Union[Target, _Mapping]]=..., disabled: bool=..., tags: _Optional[_Iterable[str]]=..., select_query: _Optional[str]=..., relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=...) -> None:
            ...

    class Declaration(_message.Message):
        __slots__ = ('relation_descriptor',)
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        relation_descriptor: RelationDescriptor

        def __init__(self, relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=...) -> None:
            ...
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    ASSERTION_FIELD_NUMBER: _ClassVar[int]
    DECLARATION_FIELD_NUMBER: _ClassVar[int]
    target: Target
    canonical_target: Target
    file_path: str
    relation: CompilationResultAction.Relation
    operations: CompilationResultAction.Operations
    assertion: CompilationResultAction.Assertion
    declaration: CompilationResultAction.Declaration

    def __init__(self, target: _Optional[_Union[Target, _Mapping]]=..., canonical_target: _Optional[_Union[Target, _Mapping]]=..., file_path: _Optional[str]=..., relation: _Optional[_Union[CompilationResultAction.Relation, _Mapping]]=..., operations: _Optional[_Union[CompilationResultAction.Operations, _Mapping]]=..., assertion: _Optional[_Union[CompilationResultAction.Assertion, _Mapping]]=..., declaration: _Optional[_Union[CompilationResultAction.Declaration, _Mapping]]=...) -> None:
        ...

class QueryCompilationResultActionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token', 'filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class QueryCompilationResultActionsResponse(_message.Message):
    __slots__ = ('compilation_result_actions', 'next_page_token')
    COMPILATION_RESULT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    compilation_result_actions: _containers.RepeatedCompositeFieldContainer[CompilationResultAction]
    next_page_token: str

    def __init__(self, compilation_result_actions: _Optional[_Iterable[_Union[CompilationResultAction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class WorkflowInvocation(_message.Message):
    __slots__ = ('name', 'compilation_result', 'invocation_config', 'state', 'invocation_timing')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WorkflowInvocation.State]
        RUNNING: _ClassVar[WorkflowInvocation.State]
        SUCCEEDED: _ClassVar[WorkflowInvocation.State]
        CANCELLED: _ClassVar[WorkflowInvocation.State]
        FAILED: _ClassVar[WorkflowInvocation.State]
        CANCELING: _ClassVar[WorkflowInvocation.State]
    STATE_UNSPECIFIED: WorkflowInvocation.State
    RUNNING: WorkflowInvocation.State
    SUCCEEDED: WorkflowInvocation.State
    CANCELLED: WorkflowInvocation.State
    FAILED: WorkflowInvocation.State
    CANCELING: WorkflowInvocation.State

    class InvocationConfig(_message.Message):
        __slots__ = ('included_targets', 'included_tags', 'transitive_dependencies_included', 'transitive_dependents_included', 'fully_refresh_incremental_tables_enabled')
        INCLUDED_TARGETS_FIELD_NUMBER: _ClassVar[int]
        INCLUDED_TAGS_FIELD_NUMBER: _ClassVar[int]
        TRANSITIVE_DEPENDENCIES_INCLUDED_FIELD_NUMBER: _ClassVar[int]
        TRANSITIVE_DEPENDENTS_INCLUDED_FIELD_NUMBER: _ClassVar[int]
        FULLY_REFRESH_INCREMENTAL_TABLES_ENABLED_FIELD_NUMBER: _ClassVar[int]
        included_targets: _containers.RepeatedCompositeFieldContainer[Target]
        included_tags: _containers.RepeatedScalarFieldContainer[str]
        transitive_dependencies_included: bool
        transitive_dependents_included: bool
        fully_refresh_incremental_tables_enabled: bool

        def __init__(self, included_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., included_tags: _Optional[_Iterable[str]]=..., transitive_dependencies_included: bool=..., transitive_dependents_included: bool=..., fully_refresh_incremental_tables_enabled: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_TIMING_FIELD_NUMBER: _ClassVar[int]
    name: str
    compilation_result: str
    invocation_config: WorkflowInvocation.InvocationConfig
    state: WorkflowInvocation.State
    invocation_timing: _interval_pb2.Interval

    def __init__(self, name: _Optional[str]=..., compilation_result: _Optional[str]=..., invocation_config: _Optional[_Union[WorkflowInvocation.InvocationConfig, _Mapping]]=..., state: _Optional[_Union[WorkflowInvocation.State, str]]=..., invocation_timing: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=...) -> None:
        ...

class ListWorkflowInvocationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWorkflowInvocationsResponse(_message.Message):
    __slots__ = ('workflow_invocations', 'next_page_token', 'unreachable')
    WORKFLOW_INVOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workflow_invocations: _containers.RepeatedCompositeFieldContainer[WorkflowInvocation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workflow_invocations: _Optional[_Iterable[_Union[WorkflowInvocation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWorkflowInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWorkflowInvocationRequest(_message.Message):
    __slots__ = ('parent', 'workflow_invocation')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workflow_invocation: WorkflowInvocation

    def __init__(self, parent: _Optional[str]=..., workflow_invocation: _Optional[_Union[WorkflowInvocation, _Mapping]]=...) -> None:
        ...

class DeleteWorkflowInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelWorkflowInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class WorkflowInvocationAction(_message.Message):
    __slots__ = ('target', 'canonical_target', 'state', 'failure_reason', 'invocation_timing', 'bigquery_action')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PENDING: _ClassVar[WorkflowInvocationAction.State]
        RUNNING: _ClassVar[WorkflowInvocationAction.State]
        SKIPPED: _ClassVar[WorkflowInvocationAction.State]
        DISABLED: _ClassVar[WorkflowInvocationAction.State]
        SUCCEEDED: _ClassVar[WorkflowInvocationAction.State]
        CANCELLED: _ClassVar[WorkflowInvocationAction.State]
        FAILED: _ClassVar[WorkflowInvocationAction.State]
    PENDING: WorkflowInvocationAction.State
    RUNNING: WorkflowInvocationAction.State
    SKIPPED: WorkflowInvocationAction.State
    DISABLED: WorkflowInvocationAction.State
    SUCCEEDED: WorkflowInvocationAction.State
    CANCELLED: WorkflowInvocationAction.State
    FAILED: WorkflowInvocationAction.State

    class BigQueryAction(_message.Message):
        __slots__ = ('sql_script',)
        SQL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
        sql_script: str

        def __init__(self, sql_script: _Optional[str]=...) -> None:
            ...
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_TIMING_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_ACTION_FIELD_NUMBER: _ClassVar[int]
    target: Target
    canonical_target: Target
    state: WorkflowInvocationAction.State
    failure_reason: str
    invocation_timing: _interval_pb2.Interval
    bigquery_action: WorkflowInvocationAction.BigQueryAction

    def __init__(self, target: _Optional[_Union[Target, _Mapping]]=..., canonical_target: _Optional[_Union[Target, _Mapping]]=..., state: _Optional[_Union[WorkflowInvocationAction.State, str]]=..., failure_reason: _Optional[str]=..., invocation_timing: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., bigquery_action: _Optional[_Union[WorkflowInvocationAction.BigQueryAction, _Mapping]]=...) -> None:
        ...

class QueryWorkflowInvocationActionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryWorkflowInvocationActionsResponse(_message.Message):
    __slots__ = ('workflow_invocation_actions', 'next_page_token')
    WORKFLOW_INVOCATION_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workflow_invocation_actions: _containers.RepeatedCompositeFieldContainer[WorkflowInvocationAction]
    next_page_token: str

    def __init__(self, workflow_invocation_actions: _Optional[_Iterable[_Union[WorkflowInvocationAction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...