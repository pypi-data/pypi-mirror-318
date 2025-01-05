from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.oslogin.common import common_pb2 as _common_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginProfileView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_PROFILE_VIEW_UNSPECIFIED: _ClassVar[LoginProfileView]
    BASIC: _ClassVar[LoginProfileView]
    SECURITY_KEY: _ClassVar[LoginProfileView]
LOGIN_PROFILE_VIEW_UNSPECIFIED: LoginProfileView
BASIC: LoginProfileView
SECURITY_KEY: LoginProfileView

class LoginProfile(_message.Message):
    __slots__ = ("name", "posix_accounts", "ssh_public_keys", "security_keys")
    class SshPublicKeysEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.SshPublicKey
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.SshPublicKey, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSIX_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_KEYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    posix_accounts: _containers.RepeatedCompositeFieldContainer[_common_pb2.PosixAccount]
    ssh_public_keys: _containers.MessageMap[str, _common_pb2.SshPublicKey]
    security_keys: _containers.RepeatedCompositeFieldContainer[SecurityKey]
    def __init__(self, name: _Optional[str] = ..., posix_accounts: _Optional[_Iterable[_Union[_common_pb2.PosixAccount, _Mapping]]] = ..., ssh_public_keys: _Optional[_Mapping[str, _common_pb2.SshPublicKey]] = ..., security_keys: _Optional[_Iterable[_Union[SecurityKey, _Mapping]]] = ...) -> None: ...

class CreateSshPublicKeyRequest(_message.Message):
    __slots__ = ("parent", "ssh_public_key")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ssh_public_key: _common_pb2.SshPublicKey
    def __init__(self, parent: _Optional[str] = ..., ssh_public_key: _Optional[_Union[_common_pb2.SshPublicKey, _Mapping]] = ...) -> None: ...

class DeletePosixAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSshPublicKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetLoginProfileRequest(_message.Message):
    __slots__ = ("name", "project_id", "system_id", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    system_id: str
    view: LoginProfileView
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., system_id: _Optional[str] = ..., view: _Optional[_Union[LoginProfileView, str]] = ...) -> None: ...

class GetSshPublicKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImportSshPublicKeyRequest(_message.Message):
    __slots__ = ("parent", "ssh_public_key", "project_id", "view", "regions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ssh_public_key: _common_pb2.SshPublicKey
    project_id: str
    view: LoginProfileView
    regions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., ssh_public_key: _Optional[_Union[_common_pb2.SshPublicKey, _Mapping]] = ..., project_id: _Optional[str] = ..., view: _Optional[_Union[LoginProfileView, str]] = ..., regions: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportSshPublicKeyResponse(_message.Message):
    __slots__ = ("login_profile", "details")
    LOGIN_PROFILE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    login_profile: LoginProfile
    details: str
    def __init__(self, login_profile: _Optional[_Union[LoginProfile, _Mapping]] = ..., details: _Optional[str] = ...) -> None: ...

class UpdateSshPublicKeyRequest(_message.Message):
    __slots__ = ("name", "ssh_public_key", "update_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    ssh_public_key: _common_pb2.SshPublicKey
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., ssh_public_key: _Optional[_Union[_common_pb2.SshPublicKey, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SecurityKey(_message.Message):
    __slots__ = ("public_key", "private_key", "universal_two_factor", "web_authn", "device_nickname")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    UNIVERSAL_TWO_FACTOR_FIELD_NUMBER: _ClassVar[int]
    WEB_AUTHN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    private_key: str
    universal_two_factor: UniversalTwoFactor
    web_authn: WebAuthn
    device_nickname: str
    def __init__(self, public_key: _Optional[str] = ..., private_key: _Optional[str] = ..., universal_two_factor: _Optional[_Union[UniversalTwoFactor, _Mapping]] = ..., web_authn: _Optional[_Union[WebAuthn, _Mapping]] = ..., device_nickname: _Optional[str] = ...) -> None: ...

class UniversalTwoFactor(_message.Message):
    __slots__ = ("app_id",)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    def __init__(self, app_id: _Optional[str] = ...) -> None: ...

class WebAuthn(_message.Message):
    __slots__ = ("rp_id",)
    RP_ID_FIELD_NUMBER: _ClassVar[int]
    rp_id: str
    def __init__(self, rp_id: _Optional[str] = ...) -> None: ...

class SignSshPublicKeyRequest(_message.Message):
    __slots__ = ("ssh_public_key", "parent")
    SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ssh_public_key: str
    parent: str
    def __init__(self, ssh_public_key: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...

class SignSshPublicKeyResponse(_message.Message):
    __slots__ = ("signed_ssh_public_key",)
    SIGNED_SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    signed_ssh_public_key: str
    def __init__(self, signed_ssh_public_key: _Optional[str] = ...) -> None: ...
