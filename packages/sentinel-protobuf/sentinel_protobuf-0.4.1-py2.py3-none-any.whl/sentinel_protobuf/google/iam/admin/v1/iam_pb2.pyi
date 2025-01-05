from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAccountKeyAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_ALG_UNSPECIFIED: _ClassVar[ServiceAccountKeyAlgorithm]
    KEY_ALG_RSA_1024: _ClassVar[ServiceAccountKeyAlgorithm]
    KEY_ALG_RSA_2048: _ClassVar[ServiceAccountKeyAlgorithm]

class ServiceAccountPrivateKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[ServiceAccountPrivateKeyType]
    TYPE_PKCS12_FILE: _ClassVar[ServiceAccountPrivateKeyType]
    TYPE_GOOGLE_CREDENTIALS_FILE: _ClassVar[ServiceAccountPrivateKeyType]

class ServiceAccountPublicKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_NONE: _ClassVar[ServiceAccountPublicKeyType]
    TYPE_X509_PEM_FILE: _ClassVar[ServiceAccountPublicKeyType]
    TYPE_RAW_PUBLIC_KEY: _ClassVar[ServiceAccountPublicKeyType]

class ServiceAccountKeyOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORIGIN_UNSPECIFIED: _ClassVar[ServiceAccountKeyOrigin]
    USER_PROVIDED: _ClassVar[ServiceAccountKeyOrigin]
    GOOGLE_PROVIDED: _ClassVar[ServiceAccountKeyOrigin]

class RoleView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASIC: _ClassVar[RoleView]
    FULL: _ClassVar[RoleView]
KEY_ALG_UNSPECIFIED: ServiceAccountKeyAlgorithm
KEY_ALG_RSA_1024: ServiceAccountKeyAlgorithm
KEY_ALG_RSA_2048: ServiceAccountKeyAlgorithm
TYPE_UNSPECIFIED: ServiceAccountPrivateKeyType
TYPE_PKCS12_FILE: ServiceAccountPrivateKeyType
TYPE_GOOGLE_CREDENTIALS_FILE: ServiceAccountPrivateKeyType
TYPE_NONE: ServiceAccountPublicKeyType
TYPE_X509_PEM_FILE: ServiceAccountPublicKeyType
TYPE_RAW_PUBLIC_KEY: ServiceAccountPublicKeyType
ORIGIN_UNSPECIFIED: ServiceAccountKeyOrigin
USER_PROVIDED: ServiceAccountKeyOrigin
GOOGLE_PROVIDED: ServiceAccountKeyOrigin
BASIC: RoleView
FULL: RoleView

class ServiceAccount(_message.Message):
    __slots__ = ('name', 'project_id', 'unique_id', 'email', 'display_name', 'etag', 'description', 'oauth2_client_id', 'disabled')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    unique_id: str
    email: str
    display_name: str
    etag: bytes
    description: str
    oauth2_client_id: str
    disabled: bool

    def __init__(self, name: _Optional[str]=..., project_id: _Optional[str]=..., unique_id: _Optional[str]=..., email: _Optional[str]=..., display_name: _Optional[str]=..., etag: _Optional[bytes]=..., description: _Optional[str]=..., oauth2_client_id: _Optional[str]=..., disabled: bool=...) -> None:
        ...

class CreateServiceAccountRequest(_message.Message):
    __slots__ = ('name', 'account_id', 'service_account')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    account_id: str
    service_account: ServiceAccount

    def __init__(self, name: _Optional[str]=..., account_id: _Optional[str]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=...) -> None:
        ...

class ListServiceAccountsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServiceAccountsResponse(_message.Message):
    __slots__ = ('accounts', 'next_page_token')
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    next_page_token: str

    def __init__(self, accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetServiceAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PatchServiceAccountRequest(_message.Message):
    __slots__ = ('service_account', 'update_mask')
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    service_account: ServiceAccount
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UndeleteServiceAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteServiceAccountResponse(_message.Message):
    __slots__ = ('restored_account',)
    RESTORED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    restored_account: ServiceAccount

    def __init__(self, restored_account: _Optional[_Union[ServiceAccount, _Mapping]]=...) -> None:
        ...

class EnableServiceAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DisableServiceAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListServiceAccountKeysRequest(_message.Message):
    __slots__ = ('name', 'key_types')

    class KeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_TYPE_UNSPECIFIED: _ClassVar[ListServiceAccountKeysRequest.KeyType]
        USER_MANAGED: _ClassVar[ListServiceAccountKeysRequest.KeyType]
        SYSTEM_MANAGED: _ClassVar[ListServiceAccountKeysRequest.KeyType]
    KEY_TYPE_UNSPECIFIED: ListServiceAccountKeysRequest.KeyType
    USER_MANAGED: ListServiceAccountKeysRequest.KeyType
    SYSTEM_MANAGED: ListServiceAccountKeysRequest.KeyType
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    key_types: _containers.RepeatedScalarFieldContainer[ListServiceAccountKeysRequest.KeyType]

    def __init__(self, name: _Optional[str]=..., key_types: _Optional[_Iterable[_Union[ListServiceAccountKeysRequest.KeyType, str]]]=...) -> None:
        ...

class ListServiceAccountKeysResponse(_message.Message):
    __slots__ = ('keys',)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[ServiceAccountKey]

    def __init__(self, keys: _Optional[_Iterable[_Union[ServiceAccountKey, _Mapping]]]=...) -> None:
        ...

class GetServiceAccountKeyRequest(_message.Message):
    __slots__ = ('name', 'public_key_type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    public_key_type: ServiceAccountPublicKeyType

    def __init__(self, name: _Optional[str]=..., public_key_type: _Optional[_Union[ServiceAccountPublicKeyType, str]]=...) -> None:
        ...

class ServiceAccountKey(_message.Message):
    __slots__ = ('name', 'private_key_type', 'key_algorithm', 'private_key_data', 'public_key_data', 'valid_after_time', 'valid_before_time', 'key_origin', 'key_type', 'disabled')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    VALID_AFTER_TIME_FIELD_NUMBER: _ClassVar[int]
    VALID_BEFORE_TIME_FIELD_NUMBER: _ClassVar[int]
    KEY_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    private_key_type: ServiceAccountPrivateKeyType
    key_algorithm: ServiceAccountKeyAlgorithm
    private_key_data: bytes
    public_key_data: bytes
    valid_after_time: _timestamp_pb2.Timestamp
    valid_before_time: _timestamp_pb2.Timestamp
    key_origin: ServiceAccountKeyOrigin
    key_type: ListServiceAccountKeysRequest.KeyType
    disabled: bool

    def __init__(self, name: _Optional[str]=..., private_key_type: _Optional[_Union[ServiceAccountPrivateKeyType, str]]=..., key_algorithm: _Optional[_Union[ServiceAccountKeyAlgorithm, str]]=..., private_key_data: _Optional[bytes]=..., public_key_data: _Optional[bytes]=..., valid_after_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., valid_before_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., key_origin: _Optional[_Union[ServiceAccountKeyOrigin, str]]=..., key_type: _Optional[_Union[ListServiceAccountKeysRequest.KeyType, str]]=..., disabled: bool=...) -> None:
        ...

class CreateServiceAccountKeyRequest(_message.Message):
    __slots__ = ('name', 'private_key_type', 'key_algorithm')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    name: str
    private_key_type: ServiceAccountPrivateKeyType
    key_algorithm: ServiceAccountKeyAlgorithm

    def __init__(self, name: _Optional[str]=..., private_key_type: _Optional[_Union[ServiceAccountPrivateKeyType, str]]=..., key_algorithm: _Optional[_Union[ServiceAccountKeyAlgorithm, str]]=...) -> None:
        ...

class UploadServiceAccountKeyRequest(_message.Message):
    __slots__ = ('name', 'public_key_data')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    public_key_data: bytes

    def __init__(self, name: _Optional[str]=..., public_key_data: _Optional[bytes]=...) -> None:
        ...

class DeleteServiceAccountKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DisableServiceAccountKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EnableServiceAccountKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SignBlobRequest(_message.Message):
    __slots__ = ('name', 'bytes_to_sign')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BYTES_TO_SIGN_FIELD_NUMBER: _ClassVar[int]
    name: str
    bytes_to_sign: bytes

    def __init__(self, name: _Optional[str]=..., bytes_to_sign: _Optional[bytes]=...) -> None:
        ...

class SignBlobResponse(_message.Message):
    __slots__ = ('key_id', 'signature')
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    signature: bytes

    def __init__(self, key_id: _Optional[str]=..., signature: _Optional[bytes]=...) -> None:
        ...

class SignJwtRequest(_message.Message):
    __slots__ = ('name', 'payload')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    payload: str

    def __init__(self, name: _Optional[str]=..., payload: _Optional[str]=...) -> None:
        ...

class SignJwtResponse(_message.Message):
    __slots__ = ('key_id', 'signed_jwt')
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_JWT_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    signed_jwt: str

    def __init__(self, key_id: _Optional[str]=..., signed_jwt: _Optional[str]=...) -> None:
        ...

class Role(_message.Message):
    __slots__ = ('name', 'title', 'description', 'included_permissions', 'stage', 'etag', 'deleted')

    class RoleLaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALPHA: _ClassVar[Role.RoleLaunchStage]
        BETA: _ClassVar[Role.RoleLaunchStage]
        GA: _ClassVar[Role.RoleLaunchStage]
        DEPRECATED: _ClassVar[Role.RoleLaunchStage]
        DISABLED: _ClassVar[Role.RoleLaunchStage]
        EAP: _ClassVar[Role.RoleLaunchStage]
    ALPHA: Role.RoleLaunchStage
    BETA: Role.RoleLaunchStage
    GA: Role.RoleLaunchStage
    DEPRECATED: Role.RoleLaunchStage
    DISABLED: Role.RoleLaunchStage
    EAP: Role.RoleLaunchStage
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    included_permissions: _containers.RepeatedScalarFieldContainer[str]
    stage: Role.RoleLaunchStage
    etag: bytes
    deleted: bool

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., included_permissions: _Optional[_Iterable[str]]=..., stage: _Optional[_Union[Role.RoleLaunchStage, str]]=..., etag: _Optional[bytes]=..., deleted: bool=...) -> None:
        ...

class QueryGrantableRolesRequest(_message.Message):
    __slots__ = ('full_resource_name', 'view', 'page_size', 'page_token')
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    full_resource_name: str
    view: RoleView
    page_size: int
    page_token: str

    def __init__(self, full_resource_name: _Optional[str]=..., view: _Optional[_Union[RoleView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryGrantableRolesResponse(_message.Message):
    __slots__ = ('roles', 'next_page_token')
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    next_page_token: str

    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListRolesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: RoleView
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[RoleView, str]]=..., show_deleted: bool=...) -> None:
        ...

class ListRolesResponse(_message.Message):
    __slots__ = ('roles', 'next_page_token')
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    next_page_token: str

    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRoleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRoleRequest(_message.Message):
    __slots__ = ('parent', 'role_id', 'role')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    role_id: str
    role: Role

    def __init__(self, parent: _Optional[str]=..., role_id: _Optional[str]=..., role: _Optional[_Union[Role, _Mapping]]=...) -> None:
        ...

class UpdateRoleRequest(_message.Message):
    __slots__ = ('name', 'role', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    role: Role
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., role: _Optional[_Union[Role, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRoleRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: bytes

    def __init__(self, name: _Optional[str]=..., etag: _Optional[bytes]=...) -> None:
        ...

class UndeleteRoleRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: bytes

    def __init__(self, name: _Optional[str]=..., etag: _Optional[bytes]=...) -> None:
        ...

class Permission(_message.Message):
    __slots__ = ('name', 'title', 'description', 'only_in_predefined_roles', 'stage', 'custom_roles_support_level', 'api_disabled', 'primary_permission')

    class PermissionLaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALPHA: _ClassVar[Permission.PermissionLaunchStage]
        BETA: _ClassVar[Permission.PermissionLaunchStage]
        GA: _ClassVar[Permission.PermissionLaunchStage]
        DEPRECATED: _ClassVar[Permission.PermissionLaunchStage]
    ALPHA: Permission.PermissionLaunchStage
    BETA: Permission.PermissionLaunchStage
    GA: Permission.PermissionLaunchStage
    DEPRECATED: Permission.PermissionLaunchStage

    class CustomRolesSupportLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUPPORTED: _ClassVar[Permission.CustomRolesSupportLevel]
        TESTING: _ClassVar[Permission.CustomRolesSupportLevel]
        NOT_SUPPORTED: _ClassVar[Permission.CustomRolesSupportLevel]
    SUPPORTED: Permission.CustomRolesSupportLevel
    TESTING: Permission.CustomRolesSupportLevel
    NOT_SUPPORTED: Permission.CustomRolesSupportLevel
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ONLY_IN_PREDEFINED_ROLES_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ROLES_SUPPORT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    API_DISABLED_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    only_in_predefined_roles: bool
    stage: Permission.PermissionLaunchStage
    custom_roles_support_level: Permission.CustomRolesSupportLevel
    api_disabled: bool
    primary_permission: str

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., only_in_predefined_roles: bool=..., stage: _Optional[_Union[Permission.PermissionLaunchStage, str]]=..., custom_roles_support_level: _Optional[_Union[Permission.CustomRolesSupportLevel, str]]=..., api_disabled: bool=..., primary_permission: _Optional[str]=...) -> None:
        ...

class QueryTestablePermissionsRequest(_message.Message):
    __slots__ = ('full_resource_name', 'page_size', 'page_token')
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    full_resource_name: str
    page_size: int
    page_token: str

    def __init__(self, full_resource_name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryTestablePermissionsResponse(_message.Message):
    __slots__ = ('permissions', 'next_page_token')
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    next_page_token: str

    def __init__(self, permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class QueryAuditableServicesRequest(_message.Message):
    __slots__ = ('full_resource_name',)
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    full_resource_name: str

    def __init__(self, full_resource_name: _Optional[str]=...) -> None:
        ...

class QueryAuditableServicesResponse(_message.Message):
    __slots__ = ('services',)

    class AuditableService(_message.Message):
        __slots__ = ('name',)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str

        def __init__(self, name: _Optional[str]=...) -> None:
            ...
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[QueryAuditableServicesResponse.AuditableService]

    def __init__(self, services: _Optional[_Iterable[_Union[QueryAuditableServicesResponse.AuditableService, _Mapping]]]=...) -> None:
        ...

class LintPolicyRequest(_message.Message):
    __slots__ = ('full_resource_name', 'condition')
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    full_resource_name: str
    condition: _expr_pb2.Expr

    def __init__(self, full_resource_name: _Optional[str]=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=...) -> None:
        ...

class LintResult(_message.Message):
    __slots__ = ('level', 'validation_unit_name', 'severity', 'field_name', 'location_offset', 'debug_message')

    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEVEL_UNSPECIFIED: _ClassVar[LintResult.Level]
        CONDITION: _ClassVar[LintResult.Level]
    LEVEL_UNSPECIFIED: LintResult.Level
    CONDITION: LintResult.Level

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[LintResult.Severity]
        ERROR: _ClassVar[LintResult.Severity]
        WARNING: _ClassVar[LintResult.Severity]
        NOTICE: _ClassVar[LintResult.Severity]
        INFO: _ClassVar[LintResult.Severity]
        DEPRECATED: _ClassVar[LintResult.Severity]
    SEVERITY_UNSPECIFIED: LintResult.Severity
    ERROR: LintResult.Severity
    WARNING: LintResult.Severity
    NOTICE: LintResult.Severity
    INFO: LintResult.Severity
    DEPRECATED: LintResult.Severity
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_UNIT_NAME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    level: LintResult.Level
    validation_unit_name: str
    severity: LintResult.Severity
    field_name: str
    location_offset: int
    debug_message: str

    def __init__(self, level: _Optional[_Union[LintResult.Level, str]]=..., validation_unit_name: _Optional[str]=..., severity: _Optional[_Union[LintResult.Severity, str]]=..., field_name: _Optional[str]=..., location_offset: _Optional[int]=..., debug_message: _Optional[str]=...) -> None:
        ...

class LintPolicyResponse(_message.Message):
    __slots__ = ('lint_results',)
    LINT_RESULTS_FIELD_NUMBER: _ClassVar[int]
    lint_results: _containers.RepeatedCompositeFieldContainer[LintResult]

    def __init__(self, lint_results: _Optional[_Iterable[_Union[LintResult, _Mapping]]]=...) -> None:
        ...