from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
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

class HttpTarget(_message.Message):
    __slots__ = ('uri', 'http_method', 'headers', 'body', 'oauth_token', 'oidc_token')

    class HeadersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    URI_FIELD_NUMBER: _ClassVar[int]
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    OAUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OIDC_TOKEN_FIELD_NUMBER: _ClassVar[int]
    uri: str
    http_method: HttpMethod
    headers: _containers.ScalarMap[str, str]
    body: bytes
    oauth_token: OAuthToken
    oidc_token: OidcToken

    def __init__(self, uri: _Optional[str]=..., http_method: _Optional[_Union[HttpMethod, str]]=..., headers: _Optional[_Mapping[str, str]]=..., body: _Optional[bytes]=..., oauth_token: _Optional[_Union[OAuthToken, _Mapping]]=..., oidc_token: _Optional[_Union[OidcToken, _Mapping]]=...) -> None:
        ...

class AppEngineHttpTarget(_message.Message):
    __slots__ = ('http_method', 'app_engine_routing', 'relative_uri', 'headers', 'body')

    class HeadersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_ROUTING_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_URI_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    http_method: HttpMethod
    app_engine_routing: AppEngineRouting
    relative_uri: str
    headers: _containers.ScalarMap[str, str]
    body: bytes

    def __init__(self, http_method: _Optional[_Union[HttpMethod, str]]=..., app_engine_routing: _Optional[_Union[AppEngineRouting, _Mapping]]=..., relative_uri: _Optional[str]=..., headers: _Optional[_Mapping[str, str]]=..., body: _Optional[bytes]=...) -> None:
        ...

class PubsubTarget(_message.Message):
    __slots__ = ('topic_name', 'data', 'attributes')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    data: bytes
    attributes: _containers.ScalarMap[str, str]

    def __init__(self, topic_name: _Optional[str]=..., data: _Optional[bytes]=..., attributes: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class AppEngineRouting(_message.Message):
    __slots__ = ('service', 'version', 'instance', 'host')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    service: str
    version: str
    instance: str
    host: str

    def __init__(self, service: _Optional[str]=..., version: _Optional[str]=..., instance: _Optional[str]=..., host: _Optional[str]=...) -> None:
        ...

class OAuthToken(_message.Message):
    __slots__ = ('service_account_email', 'scope')
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    service_account_email: str
    scope: str

    def __init__(self, service_account_email: _Optional[str]=..., scope: _Optional[str]=...) -> None:
        ...

class OidcToken(_message.Message):
    __slots__ = ('service_account_email', 'audience')
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    service_account_email: str
    audience: str

    def __init__(self, service_account_email: _Optional[str]=..., audience: _Optional[str]=...) -> None:
        ...