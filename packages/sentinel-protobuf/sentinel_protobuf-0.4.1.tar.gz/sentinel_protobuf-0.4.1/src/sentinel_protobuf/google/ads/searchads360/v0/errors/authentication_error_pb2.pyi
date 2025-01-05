from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticationErrorEnum(_message.Message):
    __slots__ = ()

    class AuthenticationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        UNKNOWN: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        AUTHENTICATION_ERROR: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        CLIENT_CUSTOMER_ID_INVALID: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        CUSTOMER_NOT_FOUND: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        GOOGLE_ACCOUNT_DELETED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        GOOGLE_ACCOUNT_COOKIE_INVALID: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        GOOGLE_ACCOUNT_AUTHENTICATION_FAILED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        GOOGLE_ACCOUNT_USER_AND_ADS_USER_MISMATCH: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        LOGIN_COOKIE_REQUIRED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        NOT_ADS_USER: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        OAUTH_TOKEN_INVALID: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        OAUTH_TOKEN_EXPIRED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        OAUTH_TOKEN_DISABLED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        OAUTH_TOKEN_REVOKED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        OAUTH_TOKEN_HEADER_INVALID: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        LOGIN_COOKIE_INVALID: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        USER_ID_INVALID: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        TWO_STEP_VERIFICATION_NOT_ENROLLED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
        ADVANCED_PROTECTION_NOT_ENROLLED: _ClassVar[AuthenticationErrorEnum.AuthenticationError]
    UNSPECIFIED: AuthenticationErrorEnum.AuthenticationError
    UNKNOWN: AuthenticationErrorEnum.AuthenticationError
    AUTHENTICATION_ERROR: AuthenticationErrorEnum.AuthenticationError
    CLIENT_CUSTOMER_ID_INVALID: AuthenticationErrorEnum.AuthenticationError
    CUSTOMER_NOT_FOUND: AuthenticationErrorEnum.AuthenticationError
    GOOGLE_ACCOUNT_DELETED: AuthenticationErrorEnum.AuthenticationError
    GOOGLE_ACCOUNT_COOKIE_INVALID: AuthenticationErrorEnum.AuthenticationError
    GOOGLE_ACCOUNT_AUTHENTICATION_FAILED: AuthenticationErrorEnum.AuthenticationError
    GOOGLE_ACCOUNT_USER_AND_ADS_USER_MISMATCH: AuthenticationErrorEnum.AuthenticationError
    LOGIN_COOKIE_REQUIRED: AuthenticationErrorEnum.AuthenticationError
    NOT_ADS_USER: AuthenticationErrorEnum.AuthenticationError
    OAUTH_TOKEN_INVALID: AuthenticationErrorEnum.AuthenticationError
    OAUTH_TOKEN_EXPIRED: AuthenticationErrorEnum.AuthenticationError
    OAUTH_TOKEN_DISABLED: AuthenticationErrorEnum.AuthenticationError
    OAUTH_TOKEN_REVOKED: AuthenticationErrorEnum.AuthenticationError
    OAUTH_TOKEN_HEADER_INVALID: AuthenticationErrorEnum.AuthenticationError
    LOGIN_COOKIE_INVALID: AuthenticationErrorEnum.AuthenticationError
    USER_ID_INVALID: AuthenticationErrorEnum.AuthenticationError
    TWO_STEP_VERIFICATION_NOT_ENROLLED: AuthenticationErrorEnum.AuthenticationError
    ADVANCED_PROTECTION_NOT_ENROLLED: AuthenticationErrorEnum.AuthenticationError

    def __init__(self) -> None:
        ...