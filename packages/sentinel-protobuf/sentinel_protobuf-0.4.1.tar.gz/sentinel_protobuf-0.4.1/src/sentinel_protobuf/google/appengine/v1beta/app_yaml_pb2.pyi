from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuthFailAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_FAIL_ACTION_UNSPECIFIED: _ClassVar[AuthFailAction]
    AUTH_FAIL_ACTION_REDIRECT: _ClassVar[AuthFailAction]
    AUTH_FAIL_ACTION_UNAUTHORIZED: _ClassVar[AuthFailAction]

class LoginRequirement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_UNSPECIFIED: _ClassVar[LoginRequirement]
    LOGIN_OPTIONAL: _ClassVar[LoginRequirement]
    LOGIN_ADMIN: _ClassVar[LoginRequirement]
    LOGIN_REQUIRED: _ClassVar[LoginRequirement]

class SecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURE_UNSPECIFIED: _ClassVar[SecurityLevel]
    SECURE_DEFAULT: _ClassVar[SecurityLevel]
    SECURE_NEVER: _ClassVar[SecurityLevel]
    SECURE_OPTIONAL: _ClassVar[SecurityLevel]
    SECURE_ALWAYS: _ClassVar[SecurityLevel]
AUTH_FAIL_ACTION_UNSPECIFIED: AuthFailAction
AUTH_FAIL_ACTION_REDIRECT: AuthFailAction
AUTH_FAIL_ACTION_UNAUTHORIZED: AuthFailAction
LOGIN_UNSPECIFIED: LoginRequirement
LOGIN_OPTIONAL: LoginRequirement
LOGIN_ADMIN: LoginRequirement
LOGIN_REQUIRED: LoginRequirement
SECURE_UNSPECIFIED: SecurityLevel
SECURE_DEFAULT: SecurityLevel
SECURE_NEVER: SecurityLevel
SECURE_OPTIONAL: SecurityLevel
SECURE_ALWAYS: SecurityLevel

class ApiConfigHandler(_message.Message):
    __slots__ = ('auth_fail_action', 'login', 'script', 'security_level', 'url')
    AUTH_FAIL_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    auth_fail_action: AuthFailAction
    login: LoginRequirement
    script: str
    security_level: SecurityLevel
    url: str

    def __init__(self, auth_fail_action: _Optional[_Union[AuthFailAction, str]]=..., login: _Optional[_Union[LoginRequirement, str]]=..., script: _Optional[str]=..., security_level: _Optional[_Union[SecurityLevel, str]]=..., url: _Optional[str]=...) -> None:
        ...

class ErrorHandler(_message.Message):
    __slots__ = ('error_code', 'static_file', 'mime_type')

    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[ErrorHandler.ErrorCode]
        ERROR_CODE_DEFAULT: _ClassVar[ErrorHandler.ErrorCode]
        ERROR_CODE_OVER_QUOTA: _ClassVar[ErrorHandler.ErrorCode]
        ERROR_CODE_DOS_API_DENIAL: _ClassVar[ErrorHandler.ErrorCode]
        ERROR_CODE_TIMEOUT: _ClassVar[ErrorHandler.ErrorCode]
    ERROR_CODE_UNSPECIFIED: ErrorHandler.ErrorCode
    ERROR_CODE_DEFAULT: ErrorHandler.ErrorCode
    ERROR_CODE_OVER_QUOTA: ErrorHandler.ErrorCode
    ERROR_CODE_DOS_API_DENIAL: ErrorHandler.ErrorCode
    ERROR_CODE_TIMEOUT: ErrorHandler.ErrorCode
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    STATIC_FILE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    error_code: ErrorHandler.ErrorCode
    static_file: str
    mime_type: str

    def __init__(self, error_code: _Optional[_Union[ErrorHandler.ErrorCode, str]]=..., static_file: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
        ...

class UrlMap(_message.Message):
    __slots__ = ('url_regex', 'static_files', 'script', 'api_endpoint', 'security_level', 'login', 'auth_fail_action', 'redirect_http_response_code')

    class RedirectHttpResponseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED: _ClassVar[UrlMap.RedirectHttpResponseCode]
        REDIRECT_HTTP_RESPONSE_CODE_301: _ClassVar[UrlMap.RedirectHttpResponseCode]
        REDIRECT_HTTP_RESPONSE_CODE_302: _ClassVar[UrlMap.RedirectHttpResponseCode]
        REDIRECT_HTTP_RESPONSE_CODE_303: _ClassVar[UrlMap.RedirectHttpResponseCode]
        REDIRECT_HTTP_RESPONSE_CODE_307: _ClassVar[UrlMap.RedirectHttpResponseCode]
    REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED: UrlMap.RedirectHttpResponseCode
    REDIRECT_HTTP_RESPONSE_CODE_301: UrlMap.RedirectHttpResponseCode
    REDIRECT_HTTP_RESPONSE_CODE_302: UrlMap.RedirectHttpResponseCode
    REDIRECT_HTTP_RESPONSE_CODE_303: UrlMap.RedirectHttpResponseCode
    REDIRECT_HTTP_RESPONSE_CODE_307: UrlMap.RedirectHttpResponseCode
    URL_REGEX_FIELD_NUMBER: _ClassVar[int]
    STATIC_FILES_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    AUTH_FAIL_ACTION_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_HTTP_RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
    url_regex: str
    static_files: StaticFilesHandler
    script: ScriptHandler
    api_endpoint: ApiEndpointHandler
    security_level: SecurityLevel
    login: LoginRequirement
    auth_fail_action: AuthFailAction
    redirect_http_response_code: UrlMap.RedirectHttpResponseCode

    def __init__(self, url_regex: _Optional[str]=..., static_files: _Optional[_Union[StaticFilesHandler, _Mapping]]=..., script: _Optional[_Union[ScriptHandler, _Mapping]]=..., api_endpoint: _Optional[_Union[ApiEndpointHandler, _Mapping]]=..., security_level: _Optional[_Union[SecurityLevel, str]]=..., login: _Optional[_Union[LoginRequirement, str]]=..., auth_fail_action: _Optional[_Union[AuthFailAction, str]]=..., redirect_http_response_code: _Optional[_Union[UrlMap.RedirectHttpResponseCode, str]]=...) -> None:
        ...

class StaticFilesHandler(_message.Message):
    __slots__ = ('path', 'upload_path_regex', 'http_headers', 'mime_type', 'expiration', 'require_matching_file', 'application_readable')

    class HttpHeadersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PATH_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_PATH_REGEX_FIELD_NUMBER: _ClassVar[int]
    HTTP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_MATCHING_FILE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_READABLE_FIELD_NUMBER: _ClassVar[int]
    path: str
    upload_path_regex: str
    http_headers: _containers.ScalarMap[str, str]
    mime_type: str
    expiration: _duration_pb2.Duration
    require_matching_file: bool
    application_readable: bool

    def __init__(self, path: _Optional[str]=..., upload_path_regex: _Optional[str]=..., http_headers: _Optional[_Mapping[str, str]]=..., mime_type: _Optional[str]=..., expiration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., require_matching_file: bool=..., application_readable: bool=...) -> None:
        ...

class ScriptHandler(_message.Message):
    __slots__ = ('script_path',)
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    script_path: str

    def __init__(self, script_path: _Optional[str]=...) -> None:
        ...

class ApiEndpointHandler(_message.Message):
    __slots__ = ('script_path',)
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    script_path: str

    def __init__(self, script_path: _Optional[str]=...) -> None:
        ...

class HealthCheck(_message.Message):
    __slots__ = ('disable_health_check', 'host', 'healthy_threshold', 'unhealthy_threshold', 'restart_threshold', 'check_interval', 'timeout')
    DISABLE_HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RESTART_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    disable_health_check: bool
    host: str
    healthy_threshold: int
    unhealthy_threshold: int
    restart_threshold: int
    check_interval: _duration_pb2.Duration
    timeout: _duration_pb2.Duration

    def __init__(self, disable_health_check: bool=..., host: _Optional[str]=..., healthy_threshold: _Optional[int]=..., unhealthy_threshold: _Optional[int]=..., restart_threshold: _Optional[int]=..., check_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ReadinessCheck(_message.Message):
    __slots__ = ('path', 'host', 'failure_threshold', 'success_threshold', 'check_interval', 'timeout', 'app_start_timeout')
    PATH_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    APP_START_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    path: str
    host: str
    failure_threshold: int
    success_threshold: int
    check_interval: _duration_pb2.Duration
    timeout: _duration_pb2.Duration
    app_start_timeout: _duration_pb2.Duration

    def __init__(self, path: _Optional[str]=..., host: _Optional[str]=..., failure_threshold: _Optional[int]=..., success_threshold: _Optional[int]=..., check_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., app_start_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class LivenessCheck(_message.Message):
    __slots__ = ('path', 'host', 'failure_threshold', 'success_threshold', 'check_interval', 'timeout', 'initial_delay')
    PATH_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_FIELD_NUMBER: _ClassVar[int]
    path: str
    host: str
    failure_threshold: int
    success_threshold: int
    check_interval: _duration_pb2.Duration
    timeout: _duration_pb2.Duration
    initial_delay: _duration_pb2.Duration

    def __init__(self, path: _Optional[str]=..., host: _Optional[str]=..., failure_threshold: _Optional[int]=..., success_threshold: _Optional[int]=..., check_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., initial_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class Library(_message.Message):
    __slots__ = ('name', 'version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str

    def __init__(self, name: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...