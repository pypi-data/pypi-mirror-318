from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SourceContext(_message.Message):
    __slots__ = ('cloud_repo', 'cloud_workspace', 'gerrit', 'git')
    CLOUD_REPO_FIELD_NUMBER: _ClassVar[int]
    CLOUD_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    GERRIT_FIELD_NUMBER: _ClassVar[int]
    GIT_FIELD_NUMBER: _ClassVar[int]
    cloud_repo: CloudRepoSourceContext
    cloud_workspace: CloudWorkspaceSourceContext
    gerrit: GerritSourceContext
    git: GitSourceContext

    def __init__(self, cloud_repo: _Optional[_Union[CloudRepoSourceContext, _Mapping]]=..., cloud_workspace: _Optional[_Union[CloudWorkspaceSourceContext, _Mapping]]=..., gerrit: _Optional[_Union[GerritSourceContext, _Mapping]]=..., git: _Optional[_Union[GitSourceContext, _Mapping]]=...) -> None:
        ...

class ExtendedSourceContext(_message.Message):
    __slots__ = ('context', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    context: SourceContext
    labels: _containers.ScalarMap[str, str]

    def __init__(self, context: _Optional[_Union[SourceContext, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class AliasContext(_message.Message):
    __slots__ = ('kind', 'name')

    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANY: _ClassVar[AliasContext.Kind]
        FIXED: _ClassVar[AliasContext.Kind]
        MOVABLE: _ClassVar[AliasContext.Kind]
        OTHER: _ClassVar[AliasContext.Kind]
    ANY: AliasContext.Kind
    FIXED: AliasContext.Kind
    MOVABLE: AliasContext.Kind
    OTHER: AliasContext.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    kind: AliasContext.Kind
    name: str

    def __init__(self, kind: _Optional[_Union[AliasContext.Kind, str]]=..., name: _Optional[str]=...) -> None:
        ...

class CloudRepoSourceContext(_message.Message):
    __slots__ = ('repo_id', 'revision_id', 'alias_name', 'alias_context')
    REPO_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    repo_id: RepoId
    revision_id: str
    alias_name: str
    alias_context: AliasContext

    def __init__(self, repo_id: _Optional[_Union[RepoId, _Mapping]]=..., revision_id: _Optional[str]=..., alias_name: _Optional[str]=..., alias_context: _Optional[_Union[AliasContext, _Mapping]]=...) -> None:
        ...

class CloudWorkspaceSourceContext(_message.Message):
    __slots__ = ('workspace_id', 'snapshot_id')
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: CloudWorkspaceId
    snapshot_id: str

    def __init__(self, workspace_id: _Optional[_Union[CloudWorkspaceId, _Mapping]]=..., snapshot_id: _Optional[str]=...) -> None:
        ...

class GerritSourceContext(_message.Message):
    __slots__ = ('host_uri', 'gerrit_project', 'revision_id', 'alias_name', 'alias_context')
    HOST_URI_FIELD_NUMBER: _ClassVar[int]
    GERRIT_PROJECT_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    host_uri: str
    gerrit_project: str
    revision_id: str
    alias_name: str
    alias_context: AliasContext

    def __init__(self, host_uri: _Optional[str]=..., gerrit_project: _Optional[str]=..., revision_id: _Optional[str]=..., alias_name: _Optional[str]=..., alias_context: _Optional[_Union[AliasContext, _Mapping]]=...) -> None:
        ...

class GitSourceContext(_message.Message):
    __slots__ = ('url', 'revision_id')
    URL_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    revision_id: str

    def __init__(self, url: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
        ...

class RepoId(_message.Message):
    __slots__ = ('project_repo_id', 'uid')
    PROJECT_REPO_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    project_repo_id: ProjectRepoId
    uid: str

    def __init__(self, project_repo_id: _Optional[_Union[ProjectRepoId, _Mapping]]=..., uid: _Optional[str]=...) -> None:
        ...

class ProjectRepoId(_message.Message):
    __slots__ = ('project_id', 'repo_name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    repo_name: str

    def __init__(self, project_id: _Optional[str]=..., repo_name: _Optional[str]=...) -> None:
        ...

class CloudWorkspaceId(_message.Message):
    __slots__ = ('repo_id', 'name')
    REPO_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    repo_id: RepoId
    name: str

    def __init__(self, repo_id: _Optional[_Union[RepoId, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...