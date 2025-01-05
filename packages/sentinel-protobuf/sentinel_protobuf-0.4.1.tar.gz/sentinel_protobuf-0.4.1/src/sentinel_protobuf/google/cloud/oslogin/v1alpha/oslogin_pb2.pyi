from google.api import annotations_pb2 as _annotations_pb2
from google.cloud.oslogin.common import common_pb2 as _common_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LoginProfile(_message.Message):
    __slots__ = ('name', 'posix_accounts', 'ssh_public_keys', 'suspended')

    class SshPublicKeysEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.SshPublicKey

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_common_pb2.SshPublicKey, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSIX_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    name: str
    posix_accounts: _containers.RepeatedCompositeFieldContainer[_common_pb2.PosixAccount]
    ssh_public_keys: _containers.MessageMap[str, _common_pb2.SshPublicKey]
    suspended: bool

    def __init__(self, name: _Optional[str]=..., posix_accounts: _Optional[_Iterable[_Union[_common_pb2.PosixAccount, _Mapping]]]=..., ssh_public_keys: _Optional[_Mapping[str, _common_pb2.SshPublicKey]]=..., suspended: bool=...) -> None:
        ...

class DeletePosixAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteSshPublicKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetLoginProfileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetSshPublicKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ImportSshPublicKeyRequest(_message.Message):
    __slots__ = ('parent', 'ssh_public_key', 'project_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ssh_public_key: _common_pb2.SshPublicKey
    project_id: str

    def __init__(self, parent: _Optional[str]=..., ssh_public_key: _Optional[_Union[_common_pb2.SshPublicKey, _Mapping]]=..., project_id: _Optional[str]=...) -> None:
        ...

class ImportSshPublicKeyResponse(_message.Message):
    __slots__ = ('login_profile',)
    LOGIN_PROFILE_FIELD_NUMBER: _ClassVar[int]
    login_profile: LoginProfile

    def __init__(self, login_profile: _Optional[_Union[LoginProfile, _Mapping]]=...) -> None:
        ...

class UpdateSshPublicKeyRequest(_message.Message):
    __slots__ = ('name', 'ssh_public_key', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    ssh_public_key: _common_pb2.SshPublicKey
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., ssh_public_key: _Optional[_Union[_common_pb2.SshPublicKey, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...