from google.api import annotations_pb2 as _annotations_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Repo(_message.Message):
    __slots__ = ('name', 'size', 'url', 'mirror_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    MIRROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    url: str
    mirror_config: MirrorConfig

    def __init__(self, name: _Optional[str]=..., size: _Optional[int]=..., url: _Optional[str]=..., mirror_config: _Optional[_Union[MirrorConfig, _Mapping]]=...) -> None:
        ...

class MirrorConfig(_message.Message):
    __slots__ = ('url', 'webhook_id', 'deploy_key_id')
    URL_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    webhook_id: str
    deploy_key_id: str

    def __init__(self, url: _Optional[str]=..., webhook_id: _Optional[str]=..., deploy_key_id: _Optional[str]=...) -> None:
        ...

class GetRepoRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListReposRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReposResponse(_message.Message):
    __slots__ = ('repos', 'next_page_token')
    REPOS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repos: _containers.RepeatedCompositeFieldContainer[Repo]
    next_page_token: str

    def __init__(self, repos: _Optional[_Iterable[_Union[Repo, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateRepoRequest(_message.Message):
    __slots__ = ('parent', 'repo')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    parent: str
    repo: Repo

    def __init__(self, parent: _Optional[str]=..., repo: _Optional[_Union[Repo, _Mapping]]=...) -> None:
        ...

class DeleteRepoRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...