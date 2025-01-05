from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationErrorEnum(_message.Message):
    __slots__ = ()

    class AuthorizationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        UNKNOWN: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        USER_PERMISSION_DENIED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        DEVELOPER_TOKEN_NOT_ON_ALLOWLIST: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        DEVELOPER_TOKEN_PROHIBITED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        PROJECT_DISABLED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        AUTHORIZATION_ERROR: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        ACTION_NOT_PERMITTED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        INCOMPLETE_SIGNUP: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        CUSTOMER_NOT_ENABLED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        MISSING_TOS: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        DEVELOPER_TOKEN_NOT_APPROVED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        SERVICE_ACCESS_DENIED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        ACCESS_DENIED_FOR_ACCOUNT_TYPE: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        METRIC_ACCESS_DENIED: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        CLOUD_PROJECT_NOT_UNDER_ORGANIZATION: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
        ACTION_NOT_PERMITTED_FOR_SUSPENDED_ACCOUNT: _ClassVar[AuthorizationErrorEnum.AuthorizationError]
    UNSPECIFIED: AuthorizationErrorEnum.AuthorizationError
    UNKNOWN: AuthorizationErrorEnum.AuthorizationError
    USER_PERMISSION_DENIED: AuthorizationErrorEnum.AuthorizationError
    DEVELOPER_TOKEN_NOT_ON_ALLOWLIST: AuthorizationErrorEnum.AuthorizationError
    DEVELOPER_TOKEN_PROHIBITED: AuthorizationErrorEnum.AuthorizationError
    PROJECT_DISABLED: AuthorizationErrorEnum.AuthorizationError
    AUTHORIZATION_ERROR: AuthorizationErrorEnum.AuthorizationError
    ACTION_NOT_PERMITTED: AuthorizationErrorEnum.AuthorizationError
    INCOMPLETE_SIGNUP: AuthorizationErrorEnum.AuthorizationError
    CUSTOMER_NOT_ENABLED: AuthorizationErrorEnum.AuthorizationError
    MISSING_TOS: AuthorizationErrorEnum.AuthorizationError
    DEVELOPER_TOKEN_NOT_APPROVED: AuthorizationErrorEnum.AuthorizationError
    INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION: AuthorizationErrorEnum.AuthorizationError
    SERVICE_ACCESS_DENIED: AuthorizationErrorEnum.AuthorizationError
    ACCESS_DENIED_FOR_ACCOUNT_TYPE: AuthorizationErrorEnum.AuthorizationError
    METRIC_ACCESS_DENIED: AuthorizationErrorEnum.AuthorizationError
    CLOUD_PROJECT_NOT_UNDER_ORGANIZATION: AuthorizationErrorEnum.AuthorizationError
    ACTION_NOT_PERMITTED_FOR_SUSPENDED_ACCOUNT: AuthorizationErrorEnum.AuthorizationError

    def __init__(self) -> None:
        ...