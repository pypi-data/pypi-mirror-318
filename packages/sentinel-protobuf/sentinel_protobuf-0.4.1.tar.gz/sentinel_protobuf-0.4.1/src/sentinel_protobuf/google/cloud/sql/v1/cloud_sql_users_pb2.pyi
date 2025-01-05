from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlUsersDeleteRequest(_message.Message):
    __slots__ = ("host", "instance", "name", "project")
    HOST_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    host: str
    instance: str
    name: str
    project: str
    def __init__(self, host: _Optional[str] = ..., instance: _Optional[str] = ..., name: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlUsersGetRequest(_message.Message):
    __slots__ = ("instance", "name", "project", "host")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    instance: str
    name: str
    project: str
    host: str
    def __init__(self, instance: _Optional[str] = ..., name: _Optional[str] = ..., project: _Optional[str] = ..., host: _Optional[str] = ...) -> None: ...

class SqlUsersInsertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: User
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class SqlUsersListRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlUsersUpdateRequest(_message.Message):
    __slots__ = ("host", "instance", "name", "project", "body")
    HOST_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    host: str
    instance: str
    name: str
    project: str
    body: User
    def __init__(self, host: _Optional[str] = ..., instance: _Optional[str] = ..., name: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UserPasswordValidationPolicy(_message.Message):
    __slots__ = ("allowed_failed_attempts", "password_expiration_duration", "enable_failed_attempts_check", "status", "enable_password_verification")
    ALLOWED_FAILED_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_EXPIRATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FAILED_ATTEMPTS_CHECK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PASSWORD_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    allowed_failed_attempts: int
    password_expiration_duration: _duration_pb2.Duration
    enable_failed_attempts_check: bool
    status: PasswordStatus
    enable_password_verification: bool
    def __init__(self, allowed_failed_attempts: _Optional[int] = ..., password_expiration_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., enable_failed_attempts_check: bool = ..., status: _Optional[_Union[PasswordStatus, _Mapping]] = ..., enable_password_verification: bool = ...) -> None: ...

class PasswordStatus(_message.Message):
    __slots__ = ("locked", "password_expiration_time")
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    locked: bool
    password_expiration_time: _timestamp_pb2.Timestamp
    def __init__(self, locked: bool = ..., password_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("kind", "password", "etag", "name", "host", "instance", "project", "type", "sqlserver_user_details", "password_policy", "dual_password_type")
    class SqlUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUILT_IN: _ClassVar[User.SqlUserType]
        CLOUD_IAM_USER: _ClassVar[User.SqlUserType]
        CLOUD_IAM_SERVICE_ACCOUNT: _ClassVar[User.SqlUserType]
        CLOUD_IAM_GROUP: _ClassVar[User.SqlUserType]
        CLOUD_IAM_GROUP_USER: _ClassVar[User.SqlUserType]
        CLOUD_IAM_GROUP_SERVICE_ACCOUNT: _ClassVar[User.SqlUserType]
    BUILT_IN: User.SqlUserType
    CLOUD_IAM_USER: User.SqlUserType
    CLOUD_IAM_SERVICE_ACCOUNT: User.SqlUserType
    CLOUD_IAM_GROUP: User.SqlUserType
    CLOUD_IAM_GROUP_USER: User.SqlUserType
    CLOUD_IAM_GROUP_SERVICE_ACCOUNT: User.SqlUserType
    class DualPasswordType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DUAL_PASSWORD_TYPE_UNSPECIFIED: _ClassVar[User.DualPasswordType]
        NO_MODIFY_DUAL_PASSWORD: _ClassVar[User.DualPasswordType]
        NO_DUAL_PASSWORD: _ClassVar[User.DualPasswordType]
        DUAL_PASSWORD: _ClassVar[User.DualPasswordType]
    DUAL_PASSWORD_TYPE_UNSPECIFIED: User.DualPasswordType
    NO_MODIFY_DUAL_PASSWORD: User.DualPasswordType
    NO_DUAL_PASSWORD: User.DualPasswordType
    DUAL_PASSWORD: User.DualPasswordType
    KIND_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SQLSERVER_USER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    DUAL_PASSWORD_TYPE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    password: str
    etag: str
    name: str
    host: str
    instance: str
    project: str
    type: User.SqlUserType
    sqlserver_user_details: SqlServerUserDetails
    password_policy: UserPasswordValidationPolicy
    dual_password_type: User.DualPasswordType
    def __init__(self, kind: _Optional[str] = ..., password: _Optional[str] = ..., etag: _Optional[str] = ..., name: _Optional[str] = ..., host: _Optional[str] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ..., type: _Optional[_Union[User.SqlUserType, str]] = ..., sqlserver_user_details: _Optional[_Union[SqlServerUserDetails, _Mapping]] = ..., password_policy: _Optional[_Union[UserPasswordValidationPolicy, _Mapping]] = ..., dual_password_type: _Optional[_Union[User.DualPasswordType, str]] = ...) -> None: ...

class SqlServerUserDetails(_message.Message):
    __slots__ = ("disabled", "server_roles")
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    SERVER_ROLES_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    server_roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, disabled: bool = ..., server_roles: _Optional[_Iterable[str]] = ...) -> None: ...

class UsersListResponse(_message.Message):
    __slots__ = ("kind", "items", "next_page_token")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[User]
    next_page_token: str
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
