from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import tool_pb2 as _tool_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HttpElementLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP_IN_UNSPECIFIED: _ClassVar[HttpElementLocation]
    HTTP_IN_QUERY: _ClassVar[HttpElementLocation]
    HTTP_IN_HEADER: _ClassVar[HttpElementLocation]
    HTTP_IN_PATH: _ClassVar[HttpElementLocation]
    HTTP_IN_BODY: _ClassVar[HttpElementLocation]
    HTTP_IN_COOKIE: _ClassVar[HttpElementLocation]

class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_TYPE_UNSPECIFIED: _ClassVar[AuthType]
    NO_AUTH: _ClassVar[AuthType]
    API_KEY_AUTH: _ClassVar[AuthType]
    HTTP_BASIC_AUTH: _ClassVar[AuthType]
    GOOGLE_SERVICE_ACCOUNT_AUTH: _ClassVar[AuthType]
    OAUTH: _ClassVar[AuthType]
    OIDC_AUTH: _ClassVar[AuthType]
HTTP_IN_UNSPECIFIED: HttpElementLocation
HTTP_IN_QUERY: HttpElementLocation
HTTP_IN_HEADER: HttpElementLocation
HTTP_IN_PATH: HttpElementLocation
HTTP_IN_BODY: HttpElementLocation
HTTP_IN_COOKIE: HttpElementLocation
AUTH_TYPE_UNSPECIFIED: AuthType
NO_AUTH: AuthType
API_KEY_AUTH: AuthType
HTTP_BASIC_AUTH: AuthType
GOOGLE_SERVICE_ACCOUNT_AUTH: AuthType
OAUTH: AuthType
OIDC_AUTH: AuthType

class Extension(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "update_time", "etag", "manifest", "extension_operations", "runtime_config", "tool_use_examples", "private_service_connect_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOL_USE_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SERVICE_CONNECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    manifest: ExtensionManifest
    extension_operations: _containers.RepeatedCompositeFieldContainer[ExtensionOperation]
    runtime_config: RuntimeConfig
    tool_use_examples: _containers.RepeatedCompositeFieldContainer[_tool_pb2.ToolUseExample]
    private_service_connect_config: ExtensionPrivateServiceConnectConfig
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., manifest: _Optional[_Union[ExtensionManifest, _Mapping]] = ..., extension_operations: _Optional[_Iterable[_Union[ExtensionOperation, _Mapping]]] = ..., runtime_config: _Optional[_Union[RuntimeConfig, _Mapping]] = ..., tool_use_examples: _Optional[_Iterable[_Union[_tool_pb2.ToolUseExample, _Mapping]]] = ..., private_service_connect_config: _Optional[_Union[ExtensionPrivateServiceConnectConfig, _Mapping]] = ...) -> None: ...

class ExtensionManifest(_message.Message):
    __slots__ = ("name", "description", "api_spec", "auth_config")
    class ApiSpec(_message.Message):
        __slots__ = ("open_api_yaml", "open_api_gcs_uri")
        OPEN_API_YAML_FIELD_NUMBER: _ClassVar[int]
        OPEN_API_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        open_api_yaml: str
        open_api_gcs_uri: str
        def __init__(self, open_api_yaml: _Optional[str] = ..., open_api_gcs_uri: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    API_SPEC_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    api_spec: ExtensionManifest.ApiSpec
    auth_config: AuthConfig
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., api_spec: _Optional[_Union[ExtensionManifest.ApiSpec, _Mapping]] = ..., auth_config: _Optional[_Union[AuthConfig, _Mapping]] = ...) -> None: ...

class ExtensionOperation(_message.Message):
    __slots__ = ("operation_id", "function_declaration")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_DECLARATION_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    function_declaration: _tool_pb2.FunctionDeclaration
    def __init__(self, operation_id: _Optional[str] = ..., function_declaration: _Optional[_Union[_tool_pb2.FunctionDeclaration, _Mapping]] = ...) -> None: ...

class AuthConfig(_message.Message):
    __slots__ = ("api_key_config", "http_basic_auth_config", "google_service_account_config", "oauth_config", "oidc_config", "auth_type")
    class ApiKeyConfig(_message.Message):
        __slots__ = ("name", "api_key_secret", "http_element_location")
        NAME_FIELD_NUMBER: _ClassVar[int]
        API_KEY_SECRET_FIELD_NUMBER: _ClassVar[int]
        HTTP_ELEMENT_LOCATION_FIELD_NUMBER: _ClassVar[int]
        name: str
        api_key_secret: str
        http_element_location: HttpElementLocation
        def __init__(self, name: _Optional[str] = ..., api_key_secret: _Optional[str] = ..., http_element_location: _Optional[_Union[HttpElementLocation, str]] = ...) -> None: ...
    class HttpBasicAuthConfig(_message.Message):
        __slots__ = ("credential_secret",)
        CREDENTIAL_SECRET_FIELD_NUMBER: _ClassVar[int]
        credential_secret: str
        def __init__(self, credential_secret: _Optional[str] = ...) -> None: ...
    class GoogleServiceAccountConfig(_message.Message):
        __slots__ = ("service_account",)
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        service_account: str
        def __init__(self, service_account: _Optional[str] = ...) -> None: ...
    class OauthConfig(_message.Message):
        __slots__ = ("access_token", "service_account")
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        access_token: str
        service_account: str
        def __init__(self, access_token: _Optional[str] = ..., service_account: _Optional[str] = ...) -> None: ...
    class OidcConfig(_message.Message):
        __slots__ = ("id_token", "service_account")
        ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        id_token: str
        service_account: str
        def __init__(self, id_token: _Optional[str] = ..., service_account: _Optional[str] = ...) -> None: ...
    API_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HTTP_BASIC_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SERVICE_ACCOUNT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OIDC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    api_key_config: AuthConfig.ApiKeyConfig
    http_basic_auth_config: AuthConfig.HttpBasicAuthConfig
    google_service_account_config: AuthConfig.GoogleServiceAccountConfig
    oauth_config: AuthConfig.OauthConfig
    oidc_config: AuthConfig.OidcConfig
    auth_type: AuthType
    def __init__(self, api_key_config: _Optional[_Union[AuthConfig.ApiKeyConfig, _Mapping]] = ..., http_basic_auth_config: _Optional[_Union[AuthConfig.HttpBasicAuthConfig, _Mapping]] = ..., google_service_account_config: _Optional[_Union[AuthConfig.GoogleServiceAccountConfig, _Mapping]] = ..., oauth_config: _Optional[_Union[AuthConfig.OauthConfig, _Mapping]] = ..., oidc_config: _Optional[_Union[AuthConfig.OidcConfig, _Mapping]] = ..., auth_type: _Optional[_Union[AuthType, str]] = ...) -> None: ...

class RuntimeConfig(_message.Message):
    __slots__ = ("code_interpreter_runtime_config", "vertex_ai_search_runtime_config", "default_params")
    class CodeInterpreterRuntimeConfig(_message.Message):
        __slots__ = ("file_input_gcs_bucket", "file_output_gcs_bucket")
        FILE_INPUT_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
        FILE_OUTPUT_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
        file_input_gcs_bucket: str
        file_output_gcs_bucket: str
        def __init__(self, file_input_gcs_bucket: _Optional[str] = ..., file_output_gcs_bucket: _Optional[str] = ...) -> None: ...
    class VertexAISearchRuntimeConfig(_message.Message):
        __slots__ = ("serving_config_name", "engine_id")
        SERVING_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
        ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
        serving_config_name: str
        engine_id: str
        def __init__(self, serving_config_name: _Optional[str] = ..., engine_id: _Optional[str] = ...) -> None: ...
    CODE_INTERPRETER_RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERTEX_AI_SEARCH_RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    code_interpreter_runtime_config: RuntimeConfig.CodeInterpreterRuntimeConfig
    vertex_ai_search_runtime_config: RuntimeConfig.VertexAISearchRuntimeConfig
    default_params: _struct_pb2.Struct
    def __init__(self, code_interpreter_runtime_config: _Optional[_Union[RuntimeConfig.CodeInterpreterRuntimeConfig, _Mapping]] = ..., vertex_ai_search_runtime_config: _Optional[_Union[RuntimeConfig.VertexAISearchRuntimeConfig, _Mapping]] = ..., default_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ExtensionPrivateServiceConnectConfig(_message.Message):
    __slots__ = ("service_directory",)
    SERVICE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    service_directory: str
    def __init__(self, service_directory: _Optional[str] = ...) -> None: ...
