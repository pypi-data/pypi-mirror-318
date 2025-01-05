from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import data_store_connection_pb2 as _data_store_connection_pb2
from google.cloud.dialogflow.cx.v3beta1 import inline_pb2 as _inline_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateToolRequest(_message.Message):
    __slots__ = ('parent', 'tool')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tool: Tool

    def __init__(self, parent: _Optional[str]=..., tool: _Optional[_Union[Tool, _Mapping]]=...) -> None:
        ...

class ListToolsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListToolsResponse(_message.Message):
    __slots__ = ('tools', 'next_page_token')
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    next_page_token: str

    def __init__(self, tools: _Optional[_Iterable[_Union[Tool, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetToolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ExportToolsRequest(_message.Message):
    __slots__ = ('parent', 'tools', 'tools_uri', 'tools_content_inline', 'data_format')

    class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_FORMAT_UNSPECIFIED: _ClassVar[ExportToolsRequest.DataFormat]
        BLOB: _ClassVar[ExportToolsRequest.DataFormat]
        JSON: _ClassVar[ExportToolsRequest.DataFormat]
    DATA_FORMAT_UNSPECIFIED: ExportToolsRequest.DataFormat
    BLOB: ExportToolsRequest.DataFormat
    JSON: ExportToolsRequest.DataFormat
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_URI_FIELD_NUMBER: _ClassVar[int]
    TOOLS_CONTENT_INLINE_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tools: _containers.RepeatedScalarFieldContainer[str]
    tools_uri: str
    tools_content_inline: bool
    data_format: ExportToolsRequest.DataFormat

    def __init__(self, parent: _Optional[str]=..., tools: _Optional[_Iterable[str]]=..., tools_uri: _Optional[str]=..., tools_content_inline: bool=..., data_format: _Optional[_Union[ExportToolsRequest.DataFormat, str]]=...) -> None:
        ...

class ExportToolsResponse(_message.Message):
    __slots__ = ('tools_uri', 'tools_content')
    TOOLS_URI_FIELD_NUMBER: _ClassVar[int]
    TOOLS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    tools_uri: str
    tools_content: _inline_pb2.InlineDestination

    def __init__(self, tools_uri: _Optional[str]=..., tools_content: _Optional[_Union[_inline_pb2.InlineDestination, _Mapping]]=...) -> None:
        ...

class UpdateToolRequest(_message.Message):
    __slots__ = ('tool', 'update_mask')
    TOOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tool: Tool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, tool: _Optional[_Union[Tool, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteToolRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class Tool(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'open_api_spec', 'data_store_spec', 'extension_spec', 'function_spec', 'tool_type')

    class ToolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOOL_TYPE_UNSPECIFIED: _ClassVar[Tool.ToolType]
        CUSTOMIZED_TOOL: _ClassVar[Tool.ToolType]
        BUILTIN_TOOL: _ClassVar[Tool.ToolType]
    TOOL_TYPE_UNSPECIFIED: Tool.ToolType
    CUSTOMIZED_TOOL: Tool.ToolType
    BUILTIN_TOOL: Tool.ToolType

    class OpenApiTool(_message.Message):
        __slots__ = ('text_schema', 'authentication', 'tls_config', 'service_directory_config')
        TEXT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
        TLS_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SERVICE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        text_schema: str
        authentication: Tool.Authentication
        tls_config: Tool.TLSConfig
        service_directory_config: Tool.ServiceDirectoryConfig

        def __init__(self, text_schema: _Optional[str]=..., authentication: _Optional[_Union[Tool.Authentication, _Mapping]]=..., tls_config: _Optional[_Union[Tool.TLSConfig, _Mapping]]=..., service_directory_config: _Optional[_Union[Tool.ServiceDirectoryConfig, _Mapping]]=...) -> None:
            ...

    class DataStoreTool(_message.Message):
        __slots__ = ('data_store_connections', 'fallback_prompt')

        class FallbackPrompt(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        DATA_STORE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_PROMPT_FIELD_NUMBER: _ClassVar[int]
        data_store_connections: _containers.RepeatedCompositeFieldContainer[_data_store_connection_pb2.DataStoreConnection]
        fallback_prompt: Tool.DataStoreTool.FallbackPrompt

        def __init__(self, data_store_connections: _Optional[_Iterable[_Union[_data_store_connection_pb2.DataStoreConnection, _Mapping]]]=..., fallback_prompt: _Optional[_Union[Tool.DataStoreTool.FallbackPrompt, _Mapping]]=...) -> None:
            ...

    class ExtensionTool(_message.Message):
        __slots__ = ('name',)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str

        def __init__(self, name: _Optional[str]=...) -> None:
            ...

    class FunctionTool(_message.Message):
        __slots__ = ('input_schema', 'output_schema')
        INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        input_schema: _struct_pb2.Struct
        output_schema: _struct_pb2.Struct

        def __init__(self, input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...

    class Authentication(_message.Message):
        __slots__ = ('api_key_config', 'oauth_config', 'service_agent_auth_config', 'bearer_token_config')

        class RequestLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            REQUEST_LOCATION_UNSPECIFIED: _ClassVar[Tool.Authentication.RequestLocation]
            HEADER: _ClassVar[Tool.Authentication.RequestLocation]
            QUERY_STRING: _ClassVar[Tool.Authentication.RequestLocation]
        REQUEST_LOCATION_UNSPECIFIED: Tool.Authentication.RequestLocation
        HEADER: Tool.Authentication.RequestLocation
        QUERY_STRING: Tool.Authentication.RequestLocation

        class ApiKeyConfig(_message.Message):
            __slots__ = ('key_name', 'api_key', 'request_location')
            KEY_NAME_FIELD_NUMBER: _ClassVar[int]
            API_KEY_FIELD_NUMBER: _ClassVar[int]
            REQUEST_LOCATION_FIELD_NUMBER: _ClassVar[int]
            key_name: str
            api_key: str
            request_location: Tool.Authentication.RequestLocation

            def __init__(self, key_name: _Optional[str]=..., api_key: _Optional[str]=..., request_location: _Optional[_Union[Tool.Authentication.RequestLocation, str]]=...) -> None:
                ...

        class OAuthConfig(_message.Message):
            __slots__ = ('oauth_grant_type', 'client_id', 'client_secret', 'token_endpoint', 'scopes')

            class OauthGrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                OAUTH_GRANT_TYPE_UNSPECIFIED: _ClassVar[Tool.Authentication.OAuthConfig.OauthGrantType]
                CLIENT_CREDENTIAL: _ClassVar[Tool.Authentication.OAuthConfig.OauthGrantType]
            OAUTH_GRANT_TYPE_UNSPECIFIED: Tool.Authentication.OAuthConfig.OauthGrantType
            CLIENT_CREDENTIAL: Tool.Authentication.OAuthConfig.OauthGrantType
            OAUTH_GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
            TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            SCOPES_FIELD_NUMBER: _ClassVar[int]
            oauth_grant_type: Tool.Authentication.OAuthConfig.OauthGrantType
            client_id: str
            client_secret: str
            token_endpoint: str
            scopes: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, oauth_grant_type: _Optional[_Union[Tool.Authentication.OAuthConfig.OauthGrantType, str]]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., token_endpoint: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
                ...

        class ServiceAgentAuthConfig(_message.Message):
            __slots__ = ('service_agent_auth',)

            class ServiceAgentAuth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SERVICE_AGENT_AUTH_UNSPECIFIED: _ClassVar[Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth]
                ID_TOKEN: _ClassVar[Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth]
                ACCESS_TOKEN: _ClassVar[Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth]
            SERVICE_AGENT_AUTH_UNSPECIFIED: Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth
            ID_TOKEN: Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth
            ACCESS_TOKEN: Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth
            SERVICE_AGENT_AUTH_FIELD_NUMBER: _ClassVar[int]
            service_agent_auth: Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth

            def __init__(self, service_agent_auth: _Optional[_Union[Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth, str]]=...) -> None:
                ...

        class BearerTokenConfig(_message.Message):
            __slots__ = ('token',)
            TOKEN_FIELD_NUMBER: _ClassVar[int]
            token: str

            def __init__(self, token: _Optional[str]=...) -> None:
                ...
        API_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        OAUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SERVICE_AGENT_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
        BEARER_TOKEN_CONFIG_FIELD_NUMBER: _ClassVar[int]
        api_key_config: Tool.Authentication.ApiKeyConfig
        oauth_config: Tool.Authentication.OAuthConfig
        service_agent_auth_config: Tool.Authentication.ServiceAgentAuthConfig
        bearer_token_config: Tool.Authentication.BearerTokenConfig

        def __init__(self, api_key_config: _Optional[_Union[Tool.Authentication.ApiKeyConfig, _Mapping]]=..., oauth_config: _Optional[_Union[Tool.Authentication.OAuthConfig, _Mapping]]=..., service_agent_auth_config: _Optional[_Union[Tool.Authentication.ServiceAgentAuthConfig, _Mapping]]=..., bearer_token_config: _Optional[_Union[Tool.Authentication.BearerTokenConfig, _Mapping]]=...) -> None:
            ...

    class TLSConfig(_message.Message):
        __slots__ = ('ca_certs',)

        class CACert(_message.Message):
            __slots__ = ('display_name', 'cert')
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            CERT_FIELD_NUMBER: _ClassVar[int]
            display_name: str
            cert: bytes

            def __init__(self, display_name: _Optional[str]=..., cert: _Optional[bytes]=...) -> None:
                ...
        CA_CERTS_FIELD_NUMBER: _ClassVar[int]
        ca_certs: _containers.RepeatedCompositeFieldContainer[Tool.TLSConfig.CACert]

        def __init__(self, ca_certs: _Optional[_Iterable[_Union[Tool.TLSConfig.CACert, _Mapping]]]=...) -> None:
            ...

    class ServiceDirectoryConfig(_message.Message):
        __slots__ = ('service',)
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        service: str

        def __init__(self, service: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPEN_API_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_SPEC_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_SPEC_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    TOOL_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    open_api_spec: Tool.OpenApiTool
    data_store_spec: Tool.DataStoreTool
    extension_spec: Tool.ExtensionTool
    function_spec: Tool.FunctionTool
    tool_type: Tool.ToolType

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., open_api_spec: _Optional[_Union[Tool.OpenApiTool, _Mapping]]=..., data_store_spec: _Optional[_Union[Tool.DataStoreTool, _Mapping]]=..., extension_spec: _Optional[_Union[Tool.ExtensionTool, _Mapping]]=..., function_spec: _Optional[_Union[Tool.FunctionTool, _Mapping]]=..., tool_type: _Optional[_Union[Tool.ToolType, str]]=...) -> None:
        ...

class ExportToolsMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...