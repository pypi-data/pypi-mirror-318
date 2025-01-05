from google.cloud.connectors.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_TYPE_UNSPECIFIED: _ClassVar[AuthType]
    USER_PASSWORD: _ClassVar[AuthType]
    OAUTH2_JWT_BEARER: _ClassVar[AuthType]
    OAUTH2_CLIENT_CREDENTIALS: _ClassVar[AuthType]
    SSH_PUBLIC_KEY: _ClassVar[AuthType]
    OAUTH2_AUTH_CODE_FLOW: _ClassVar[AuthType]
AUTH_TYPE_UNSPECIFIED: AuthType
USER_PASSWORD: AuthType
OAUTH2_JWT_BEARER: AuthType
OAUTH2_CLIENT_CREDENTIALS: AuthType
SSH_PUBLIC_KEY: AuthType
OAUTH2_AUTH_CODE_FLOW: AuthType

class AuthConfig(_message.Message):
    __slots__ = ('auth_type', 'user_password', 'oauth2_jwt_bearer', 'oauth2_client_credentials', 'ssh_public_key', 'additional_variables')

    class UserPassword(_message.Message):
        __slots__ = ('username', 'password')
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        username: str
        password: _common_pb2.Secret

        def __init__(self, username: _Optional[str]=..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]]=...) -> None:
            ...

    class Oauth2JwtBearer(_message.Message):
        __slots__ = ('client_key', 'jwt_claims')

        class JwtClaims(_message.Message):
            __slots__ = ('issuer', 'subject', 'audience')
            ISSUER_FIELD_NUMBER: _ClassVar[int]
            SUBJECT_FIELD_NUMBER: _ClassVar[int]
            AUDIENCE_FIELD_NUMBER: _ClassVar[int]
            issuer: str
            subject: str
            audience: str

            def __init__(self, issuer: _Optional[str]=..., subject: _Optional[str]=..., audience: _Optional[str]=...) -> None:
                ...
        CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
        JWT_CLAIMS_FIELD_NUMBER: _ClassVar[int]
        client_key: _common_pb2.Secret
        jwt_claims: AuthConfig.Oauth2JwtBearer.JwtClaims

        def __init__(self, client_key: _Optional[_Union[_common_pb2.Secret, _Mapping]]=..., jwt_claims: _Optional[_Union[AuthConfig.Oauth2JwtBearer.JwtClaims, _Mapping]]=...) -> None:
            ...

    class Oauth2ClientCredentials(_message.Message):
        __slots__ = ('client_id', 'client_secret')
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        client_id: str
        client_secret: _common_pb2.Secret

        def __init__(self, client_id: _Optional[str]=..., client_secret: _Optional[_Union[_common_pb2.Secret, _Mapping]]=...) -> None:
            ...

    class SshPublicKey(_message.Message):
        __slots__ = ('username', 'ssh_client_cert', 'cert_type', 'ssh_client_cert_pass')
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        SSH_CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
        CERT_TYPE_FIELD_NUMBER: _ClassVar[int]
        SSH_CLIENT_CERT_PASS_FIELD_NUMBER: _ClassVar[int]
        username: str
        ssh_client_cert: _common_pb2.Secret
        cert_type: str
        ssh_client_cert_pass: _common_pb2.Secret

        def __init__(self, username: _Optional[str]=..., ssh_client_cert: _Optional[_Union[_common_pb2.Secret, _Mapping]]=..., cert_type: _Optional[str]=..., ssh_client_cert_pass: _Optional[_Union[_common_pb2.Secret, _Mapping]]=...) -> None:
            ...
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_JWT_BEARER_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_CLIENT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    auth_type: AuthType
    user_password: AuthConfig.UserPassword
    oauth2_jwt_bearer: AuthConfig.Oauth2JwtBearer
    oauth2_client_credentials: AuthConfig.Oauth2ClientCredentials
    ssh_public_key: AuthConfig.SshPublicKey
    additional_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.ConfigVariable]

    def __init__(self, auth_type: _Optional[_Union[AuthType, str]]=..., user_password: _Optional[_Union[AuthConfig.UserPassword, _Mapping]]=..., oauth2_jwt_bearer: _Optional[_Union[AuthConfig.Oauth2JwtBearer, _Mapping]]=..., oauth2_client_credentials: _Optional[_Union[AuthConfig.Oauth2ClientCredentials, _Mapping]]=..., ssh_public_key: _Optional[_Union[AuthConfig.SshPublicKey, _Mapping]]=..., additional_variables: _Optional[_Iterable[_Union[_common_pb2.ConfigVariable, _Mapping]]]=...) -> None:
        ...

class AuthConfigTemplate(_message.Message):
    __slots__ = ('auth_type', 'config_variable_templates', 'display_name', 'description')
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VARIABLE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    auth_type: AuthType
    config_variable_templates: _containers.RepeatedCompositeFieldContainer[_common_pb2.ConfigVariableTemplate]
    display_name: str
    description: str

    def __init__(self, auth_type: _Optional[_Union[AuthType, str]]=..., config_variable_templates: _Optional[_Iterable[_Union[_common_pb2.ConfigVariableTemplate, _Mapping]]]=..., display_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...