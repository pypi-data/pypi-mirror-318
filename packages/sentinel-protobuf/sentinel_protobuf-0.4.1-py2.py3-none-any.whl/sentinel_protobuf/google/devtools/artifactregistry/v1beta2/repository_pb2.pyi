from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Repository(_message.Message):
    __slots__ = ('maven_config', 'name', 'format', 'description', 'labels', 'create_time', 'update_time', 'kms_key_name')

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[Repository.Format]
        DOCKER: _ClassVar[Repository.Format]
        MAVEN: _ClassVar[Repository.Format]
        NPM: _ClassVar[Repository.Format]
        APT: _ClassVar[Repository.Format]
        YUM: _ClassVar[Repository.Format]
        PYTHON: _ClassVar[Repository.Format]
    FORMAT_UNSPECIFIED: Repository.Format
    DOCKER: Repository.Format
    MAVEN: Repository.Format
    NPM: Repository.Format
    APT: Repository.Format
    YUM: Repository.Format
    PYTHON: Repository.Format

    class MavenRepositoryConfig(_message.Message):
        __slots__ = ('allow_snapshot_overwrites', 'version_policy')

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

        def __init__(self, allow_snapshot_overwrites: bool=..., version_policy: _Optional[_Union[Repository.MavenRepositoryConfig.VersionPolicy, str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MAVEN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    maven_config: Repository.MavenRepositoryConfig
    name: str
    format: Repository.Format
    description: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    kms_key_name: str

    def __init__(self, maven_config: _Optional[_Union[Repository.MavenRepositoryConfig, _Mapping]]=..., name: _Optional[str]=..., format: _Optional[_Union[Repository.Format, str]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., kms_key_name: _Optional[str]=...) -> None:
        ...

class ListRepositoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRepositoriesResponse(_message.Message):
    __slots__ = ('repositories', 'next_page_token')
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRepositoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRepositoryRequest(_message.Message):
    __slots__ = ('parent', 'repository_id', 'repository')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_ID_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    repository_id: str
    repository: Repository

    def __init__(self, parent: _Optional[str]=..., repository_id: _Optional[str]=..., repository: _Optional[_Union[Repository, _Mapping]]=...) -> None:
        ...

class UpdateRepositoryRequest(_message.Message):
    __slots__ = ('repository', 'update_mask')
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    repository: Repository
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, repository: _Optional[_Union[Repository, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRepositoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...