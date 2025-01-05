from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SSHKey(_message.Message):
    __slots__ = ('name', 'public_key')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    public_key: str

    def __init__(self, name: _Optional[str]=..., public_key: _Optional[str]=...) -> None:
        ...

class ListSSHKeysRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSSHKeysResponse(_message.Message):
    __slots__ = ('ssh_keys', 'next_page_token')
    SSH_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ssh_keys: _containers.RepeatedCompositeFieldContainer[SSHKey]
    next_page_token: str

    def __init__(self, ssh_keys: _Optional[_Iterable[_Union[SSHKey, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateSSHKeyRequest(_message.Message):
    __slots__ = ('parent', 'ssh_key', 'ssh_key_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ssh_key: SSHKey
    ssh_key_id: str

    def __init__(self, parent: _Optional[str]=..., ssh_key: _Optional[_Union[SSHKey, _Mapping]]=..., ssh_key_id: _Optional[str]=...) -> None:
        ...

class DeleteSSHKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...