from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HttpMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP_METHOD_UNSPECIFIED: _ClassVar[HttpMethod]
    POST: _ClassVar[HttpMethod]
    GET: _ClassVar[HttpMethod]
    HEAD: _ClassVar[HttpMethod]
    PUT: _ClassVar[HttpMethod]
    DELETE: _ClassVar[HttpMethod]
    PATCH: _ClassVar[HttpMethod]
    OPTIONS: _ClassVar[HttpMethod]
HTTP_METHOD_UNSPECIFIED: HttpMethod
POST: HttpMethod
GET: HttpMethod
HEAD: HttpMethod
PUT: HttpMethod
DELETE: HttpMethod
PATCH: HttpMethod
OPTIONS: HttpMethod

class PullTarget(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PullMessage(_message.Message):
    __slots__ = ("payload", "tag")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    tag: str
    def __init__(self, payload: _Optional[bytes] = ..., tag: _Optional[str] = ...) -> None: ...

class AppEngineHttpTarget(_message.Message):
    __slots__ = ("app_engine_routing_override",)
    APP_ENGINE_ROUTING_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    app_engine_routing_override: AppEngineRouting
    def __init__(self, app_engine_routing_override: _Optional[_Union[AppEngineRouting, _Mapping]] = ...) -> None: ...

class AppEngineHttpRequest(_message.Message):
    __slots__ = ("http_method", "app_engine_routing", "relative_url", "headers", "payload")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_ROUTING_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    http_method: HttpMethod
    app_engine_routing: AppEngineRouting
    relative_url: str
    headers: _containers.ScalarMap[str, str]
    payload: bytes
    def __init__(self, http_method: _Optional[_Union[HttpMethod, str]] = ..., app_engine_routing: _Optional[_Union[AppEngineRouting, _Mapping]] = ..., relative_url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., payload: _Optional[bytes] = ...) -> None: ...

class AppEngineRouting(_message.Message):
    __slots__ = ("service", "version", "instance", "host")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    service: str
    version: str
    instance: str
    host: str
    def __init__(self, service: _Optional[str] = ..., version: _Optional[str] = ..., instance: _Optional[str] = ..., host: _Optional[str] = ...) -> None: ...

class HttpRequest(_message.Message):
    __slots__ = ("url", "http_method", "headers", "body", "oauth_token", "oidc_token")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    OAUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OIDC_TOKEN_FIELD_NUMBER: _ClassVar[int]
    url: str
    http_method: HttpMethod
    headers: _containers.ScalarMap[str, str]
    body: bytes
    oauth_token: OAuthToken
    oidc_token: OidcToken
    def __init__(self, url: _Optional[str] = ..., http_method: _Optional[_Union[HttpMethod, str]] = ..., headers: _Optional[_Mapping[str, str]] = ..., body: _Optional[bytes] = ..., oauth_token: _Optional[_Union[OAuthToken, _Mapping]] = ..., oidc_token: _Optional[_Union[OidcToken, _Mapping]] = ...) -> None: ...

class PathOverride(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class QueryOverride(_message.Message):
    __slots__ = ("query_params",)
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    query_params: str
    def __init__(self, query_params: _Optional[str] = ...) -> None: ...

class UriOverride(_message.Message):
    __slots__ = ("scheme", "host", "port", "path_override", "query_override", "uri_override_enforce_mode")
    class Scheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEME_UNSPECIFIED: _ClassVar[UriOverride.Scheme]
        HTTP: _ClassVar[UriOverride.Scheme]
        HTTPS: _ClassVar[UriOverride.Scheme]
    SCHEME_UNSPECIFIED: UriOverride.Scheme
    HTTP: UriOverride.Scheme
    HTTPS: UriOverride.Scheme
    class UriOverrideEnforceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        URI_OVERRIDE_ENFORCE_MODE_UNSPECIFIED: _ClassVar[UriOverride.UriOverrideEnforceMode]
        IF_NOT_EXISTS: _ClassVar[UriOverride.UriOverrideEnforceMode]
        ALWAYS: _ClassVar[UriOverride.UriOverrideEnforceMode]
    URI_OVERRIDE_ENFORCE_MODE_UNSPECIFIED: UriOverride.UriOverrideEnforceMode
    IF_NOT_EXISTS: UriOverride.UriOverrideEnforceMode
    ALWAYS: UriOverride.UriOverrideEnforceMode
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PATH_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QUERY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    URI_OVERRIDE_ENFORCE_MODE_FIELD_NUMBER: _ClassVar[int]
    scheme: UriOverride.Scheme
    host: str
    port: int
    path_override: PathOverride
    query_override: QueryOverride
    uri_override_enforce_mode: UriOverride.UriOverrideEnforceMode
    def __init__(self, scheme: _Optional[_Union[UriOverride.Scheme, str]] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., path_override: _Optional[_Union[PathOverride, _Mapping]] = ..., query_override: _Optional[_Union[QueryOverride, _Mapping]] = ..., uri_override_enforce_mode: _Optional[_Union[UriOverride.UriOverrideEnforceMode, str]] = ...) -> None: ...

class HttpTarget(_message.Message):
    __slots__ = ("uri_override", "http_method", "header_overrides", "oauth_token", "oidc_token")
    class Header(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class HeaderOverride(_message.Message):
        __slots__ = ("header",)
        HEADER_FIELD_NUMBER: _ClassVar[int]
        header: HttpTarget.Header
        def __init__(self, header: _Optional[_Union[HttpTarget.Header, _Mapping]] = ...) -> None: ...
    URI_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    HEADER_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    OAUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OIDC_TOKEN_FIELD_NUMBER: _ClassVar[int]
    uri_override: UriOverride
    http_method: HttpMethod
    header_overrides: _containers.RepeatedCompositeFieldContainer[HttpTarget.HeaderOverride]
    oauth_token: OAuthToken
    oidc_token: OidcToken
    def __init__(self, uri_override: _Optional[_Union[UriOverride, _Mapping]] = ..., http_method: _Optional[_Union[HttpMethod, str]] = ..., header_overrides: _Optional[_Iterable[_Union[HttpTarget.HeaderOverride, _Mapping]]] = ..., oauth_token: _Optional[_Union[OAuthToken, _Mapping]] = ..., oidc_token: _Optional[_Union[OidcToken, _Mapping]] = ...) -> None: ...

class OAuthToken(_message.Message):
    __slots__ = ("service_account_email", "scope")
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    service_account_email: str
    scope: str
    def __init__(self, service_account_email: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...

class OidcToken(_message.Message):
    __slots__ = ("service_account_email", "audience")
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    service_account_email: str
    audience: str
    def __init__(self, service_account_email: _Optional[str] = ..., audience: _Optional[str] = ...) -> None: ...
