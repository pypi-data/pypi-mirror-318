"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/tool.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import data_store_connection_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_data__store__connection__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import inline_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_inline__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dialogflow/cx/v3beta1/tool.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a>google/cloud/dialogflow/cx/v3beta1/data_store_connection.proto\x1a/google/cloud/dialogflow/cx/v3beta1/inline.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\x88\x01\n\x11CreateToolRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool\x12;\n\x04tool\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.ToolB\x03\xe0A\x02"q\n\x10ListToolsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"e\n\x11ListToolsResponse\x127\n\x05tools\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.cx.v3beta1.Tool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"F\n\x0eGetToolRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool"\xed\x02\n\x12ExportToolsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool\x125\n\x05tools\x18\x02 \x03(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool\x12\x18\n\ttools_uri\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x12#\n\x14tools_content_inline\x18\x04 \x01(\x08B\x03\xe0A\x01H\x00\x12[\n\x0bdata_format\x18\x05 \x01(\x0e2A.google.cloud.dialogflow.cx.v3beta1.ExportToolsRequest.DataFormatB\x03\xe0A\x01"=\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04BLOB\x10\x01\x12\x08\n\x04JSON\x10\x02B\r\n\x0bdestination"\x83\x01\n\x13ExportToolsResponse\x12\x13\n\ttools_uri\x18\x01 \x01(\tH\x00\x12N\n\rtools_content\x18\x02 \x01(\x0b25.google.cloud.dialogflow.cx.v3beta1.InlineDestinationH\x00B\x07\n\x05tools"\x81\x01\n\x11UpdateToolRequest\x12;\n\x04tool\x18\x01 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.ToolB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"X\n\x11DeleteToolRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool\x12\r\n\x05force\x18\x02 \x01(\x08"\xe4\x16\n\x04Tool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x02\x12M\n\ropen_api_spec\x18\x04 \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.Tool.OpenApiToolH\x00\x12Q\n\x0fdata_store_spec\x18\x08 \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.Tool.DataStoreToolH\x00\x12P\n\x0eextension_spec\x18\x0b \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.Tool.ExtensionToolH\x00\x12N\n\rfunction_spec\x18\r \x01(\x0b25.google.cloud.dialogflow.cx.v3beta1.Tool.FunctionToolH\x00\x12I\n\ttool_type\x18\x0c \x01(\x0e21.google.cloud.dialogflow.cx.v3beta1.Tool.ToolTypeB\x03\xe0A\x03\x1a\xbe\x02\n\x0bOpenApiTool\x12\x1a\n\x0btext_schema\x18\x01 \x01(\tB\x03\xe0A\x02H\x00\x12T\n\x0eauthentication\x18\x02 \x01(\x0b27.google.cloud.dialogflow.cx.v3beta1.Tool.AuthenticationB\x03\xe0A\x01\x12K\n\ntls_config\x18\x03 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.Tool.TLSConfigB\x03\xe0A\x01\x12f\n\x18service_directory_config\x18\x04 \x01(\x0b2?.google.cloud.dialogflow.cx.v3beta1.Tool.ServiceDirectoryConfigB\x03\xe0A\x01B\x08\n\x06schema\x1a\xe4\x01\n\rDataStoreTool\x12\\\n\x16data_store_connections\x18\x01 \x03(\x0b27.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionB\x03\xe0A\x02\x12c\n\x0ffallback_prompt\x18\x03 \x01(\x0b2E.google.cloud.dialogflow.cx.v3beta1.Tool.DataStoreTool.FallbackPromptB\x03\xe0A\x02\x1a\x10\n\x0eFallbackPrompt\x1a"\n\rExtensionTool\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x1aw\n\x0cFunctionTool\x122\n\x0cinput_schema\x18\x01 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x123\n\routput_schema\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1a\x87\n\n\x0eAuthentication\x12^\n\x0eapi_key_config\x18\x01 \x01(\x0b2D.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.ApiKeyConfigH\x00\x12[\n\x0coauth_config\x18\x02 \x01(\x0b2C.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.OAuthConfigH\x00\x12s\n\x19service_agent_auth_config\x18\x03 \x01(\x0b2N.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.ServiceAgentAuthConfigH\x00\x12h\n\x13bearer_token_config\x18\x04 \x01(\x0b2I.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.BearerTokenConfigH\x00\x1a\xa3\x01\n\x0cApiKeyConfig\x12\x15\n\x08key_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07api_key\x18\x02 \x01(\tB\x03\xe0A\x02\x12f\n\x10request_location\x18\x03 \x01(\x0e2G.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.RequestLocationB\x03\xe0A\x02\x1a\xb1\x02\n\x0bOAuthConfig\x12q\n\x10oauth_grant_type\x18\x01 \x01(\x0e2R.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.OAuthConfig.OauthGrantTypeB\x03\xe0A\x02\x12\x16\n\tclient_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rclient_secret\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0etoken_endpoint\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06scopes\x18\x05 \x03(\tB\x03\xe0A\x01"I\n\x0eOauthGrantType\x12 \n\x1cOAUTH_GRANT_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11CLIENT_CREDENTIAL\x10\x01\x1a\xf3\x01\n\x16ServiceAgentAuthConfig\x12\x80\x01\n\x12service_agent_auth\x18\x01 \x01(\x0e2_.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuthB\x03\xe0A\x01"V\n\x10ServiceAgentAuth\x12"\n\x1eSERVICE_AGENT_AUTH_UNSPECIFIED\x10\x00\x12\x0c\n\x08ID_TOKEN\x10\x01\x12\x10\n\x0cACCESS_TOKEN\x10\x02\x1a\'\n\x11BearerTokenConfig\x12\x12\n\x05token\x18\x01 \x01(\tB\x03\xe0A\x02"Q\n\x0fRequestLocation\x12 \n\x1cREQUEST_LOCATION_UNSPECIFIED\x10\x00\x12\n\n\x06HEADER\x10\x01\x12\x10\n\x0cQUERY_STRING\x10\x02B\r\n\x0bauth_config\x1a\x95\x01\n\tTLSConfig\x12P\n\x08ca_certs\x18\x01 \x03(\x0b29.google.cloud.dialogflow.cx.v3beta1.Tool.TLSConfig.CACertB\x03\xe0A\x02\x1a6\n\x06CACert\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04cert\x18\x02 \x01(\x0cB\x03\xe0A\x02\x1aZ\n\x16ServiceDirectoryConfig\x12@\n\x07service\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service"L\n\x08ToolType\x12\x19\n\x15TOOL_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCUSTOMIZED_TOOL\x10\x01\x12\x10\n\x0cBUILTIN_TOOL\x10\x02:h\xeaAe\n\x1edialogflow.googleapis.com/Tool\x12Cprojects/{project}/locations/{location}/agents/{agent}/tools/{tool}B\x0f\n\rspecification"\x15\n\x13ExportToolsMetadata2\x91\n\n\x05Tools\x12\xc2\x01\n\nCreateTool\x125.google.cloud.dialogflow.cx.v3beta1.CreateToolRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Tool"S\xdaA\x0bparent,tool\x82\xd3\xe4\x93\x02?"7/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:\x04tool\x12\xc2\x01\n\tListTools\x124.google.cloud.dialogflow.cx.v3beta1.ListToolsRequest\x1a5.google.cloud.dialogflow.cx.v3beta1.ListToolsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v3beta1/{parent=projects/*/locations/*/agents/*}/tools\x12\xdc\x01\n\x0bExportTools\x126.google.cloud.dialogflow.cx.v3beta1.ExportToolsRequest\x1a\x1d.google.longrunning.Operation"v\xcaA*\n\x13ExportToolsResponse\x12\x13ExportToolsMetadata\x82\xd3\xe4\x93\x02C">/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:export:\x01*\x12\xaf\x01\n\x07GetTool\x122.google.cloud.dialogflow.cx.v3beta1.GetToolRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Tool"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}\x12\xcc\x01\n\nUpdateTool\x125.google.cloud.dialogflow.cx.v3beta1.UpdateToolRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Tool"]\xdaA\x10tool,update_mask\x82\xd3\xe4\x93\x02D2</v3beta1/{tool.name=projects/*/locations/*/agents/*/tools/*}:\x04tool\x12\xa3\x01\n\nDeleteTool\x125.google.cloud.dialogflow.cx.v3beta1.DeleteToolRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x97\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\tToolProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.tool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\tToolProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1'
    _globals['_CREATETOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool'
    _globals['_CREATETOOLREQUEST'].fields_by_name['tool']._loaded_options = None
    _globals['_CREATETOOLREQUEST'].fields_by_name['tool']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool'
    _globals['_GETTOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_uri']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_content_inline']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_content_inline']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['data_format']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['data_format']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETOOLREQUEST'].fields_by_name['tool']._loaded_options = None
    _globals['_UPDATETOOLREQUEST'].fields_by_name['tool']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['text_schema']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['text_schema']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['authentication']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['authentication']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['tls_config']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['tls_config']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['service_directory_config']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['service_directory_config']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['data_store_connections']._loaded_options = None
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['data_store_connections']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['fallback_prompt']._loaded_options = None
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['fallback_prompt']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_EXTENSIONTOOL'].fields_by_name['name']._loaded_options = None
    _globals['_TOOL_EXTENSIONTOOL'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['input_schema']._loaded_options = None
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['input_schema']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['output_schema']._loaded_options = None
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['output_schema']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['key_name']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['key_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['api_key']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['api_key']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['request_location']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['request_location']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['oauth_grant_type']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['oauth_grant_type']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_id']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_id']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_secret']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_secret']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['token_endpoint']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['token_endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['scopes']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['scopes']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG'].fields_by_name['service_agent_auth']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG'].fields_by_name['service_agent_auth']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG'].fields_by_name['token']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG'].fields_by_name['token']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['display_name']._loaded_options = None
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['cert']._loaded_options = None
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['cert']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_TLSCONFIG'].fields_by_name['ca_certs']._loaded_options = None
    _globals['_TOOL_TLSCONFIG'].fields_by_name['ca_certs']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_SERVICEDIRECTORYCONFIG'].fields_by_name['service']._loaded_options = None
    _globals['_TOOL_SERVICEDIRECTORYCONFIG'].fields_by_name['service']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_TOOL'].fields_by_name['display_name']._loaded_options = None
    _globals['_TOOL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL'].fields_by_name['description']._loaded_options = None
    _globals['_TOOL'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL'].fields_by_name['tool_type']._loaded_options = None
    _globals['_TOOL'].fields_by_name['tool_type']._serialized_options = b'\xe0A\x03'
    _globals['_TOOL']._loaded_options = None
    _globals['_TOOL']._serialized_options = b'\xeaAe\n\x1edialogflow.googleapis.com/Tool\x12Cprojects/{project}/locations/{location}/agents/{agent}/tools/{tool}'
    _globals['_TOOLS']._loaded_options = None
    _globals['_TOOLS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_TOOLS'].methods_by_name['CreateTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['CreateTool']._serialized_options = b'\xdaA\x0bparent,tool\x82\xd3\xe4\x93\x02?"7/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:\x04tool'
    _globals['_TOOLS'].methods_by_name['ListTools']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['ListTools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v3beta1/{parent=projects/*/locations/*/agents/*}/tools'
    _globals['_TOOLS'].methods_by_name['ExportTools']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['ExportTools']._serialized_options = b'\xcaA*\n\x13ExportToolsResponse\x12\x13ExportToolsMetadata\x82\xd3\xe4\x93\x02C">/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:export:\x01*'
    _globals['_TOOLS'].methods_by_name['GetTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['GetTool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}'
    _globals['_TOOLS'].methods_by_name['UpdateTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['UpdateTool']._serialized_options = b'\xdaA\x10tool,update_mask\x82\xd3\xe4\x93\x02D2</v3beta1/{tool.name=projects/*/locations/*/agents/*/tools/*}:\x04tool'
    _globals['_TOOLS'].methods_by_name['DeleteTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['DeleteTool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}'
    _globals['_CREATETOOLREQUEST']._serialized_start = 444
    _globals['_CREATETOOLREQUEST']._serialized_end = 580
    _globals['_LISTTOOLSREQUEST']._serialized_start = 582
    _globals['_LISTTOOLSREQUEST']._serialized_end = 695
    _globals['_LISTTOOLSRESPONSE']._serialized_start = 697
    _globals['_LISTTOOLSRESPONSE']._serialized_end = 798
    _globals['_GETTOOLREQUEST']._serialized_start = 800
    _globals['_GETTOOLREQUEST']._serialized_end = 870
    _globals['_EXPORTTOOLSREQUEST']._serialized_start = 873
    _globals['_EXPORTTOOLSREQUEST']._serialized_end = 1238
    _globals['_EXPORTTOOLSREQUEST_DATAFORMAT']._serialized_start = 1162
    _globals['_EXPORTTOOLSREQUEST_DATAFORMAT']._serialized_end = 1223
    _globals['_EXPORTTOOLSRESPONSE']._serialized_start = 1241
    _globals['_EXPORTTOOLSRESPONSE']._serialized_end = 1372
    _globals['_UPDATETOOLREQUEST']._serialized_start = 1375
    _globals['_UPDATETOOLREQUEST']._serialized_end = 1504
    _globals['_DELETETOOLREQUEST']._serialized_start = 1506
    _globals['_DELETETOOLREQUEST']._serialized_end = 1594
    _globals['_TOOL']._serialized_start = 1597
    _globals['_TOOL']._serialized_end = 4513
    _globals['_TOOL_OPENAPITOOL']._serialized_start = 2072
    _globals['_TOOL_OPENAPITOOL']._serialized_end = 2390
    _globals['_TOOL_DATASTORETOOL']._serialized_start = 2393
    _globals['_TOOL_DATASTORETOOL']._serialized_end = 2621
    _globals['_TOOL_DATASTORETOOL_FALLBACKPROMPT']._serialized_start = 2605
    _globals['_TOOL_DATASTORETOOL_FALLBACKPROMPT']._serialized_end = 2621
    _globals['_TOOL_EXTENSIONTOOL']._serialized_start = 2623
    _globals['_TOOL_EXTENSIONTOOL']._serialized_end = 2657
    _globals['_TOOL_FUNCTIONTOOL']._serialized_start = 2659
    _globals['_TOOL_FUNCTIONTOOL']._serialized_end = 2778
    _globals['_TOOL_AUTHENTICATION']._serialized_start = 2781
    _globals['_TOOL_AUTHENTICATION']._serialized_end = 4068
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG']._serialized_start = 3212
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG']._serialized_end = 3375
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG']._serialized_start = 3378
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG']._serialized_end = 3683
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG_OAUTHGRANTTYPE']._serialized_start = 3610
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG_OAUTHGRANTTYPE']._serialized_end = 3683
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG']._serialized_start = 3686
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG']._serialized_end = 3929
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG_SERVICEAGENTAUTH']._serialized_start = 3843
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG_SERVICEAGENTAUTH']._serialized_end = 3929
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG']._serialized_start = 3931
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG']._serialized_end = 3970
    _globals['_TOOL_AUTHENTICATION_REQUESTLOCATION']._serialized_start = 3972
    _globals['_TOOL_AUTHENTICATION_REQUESTLOCATION']._serialized_end = 4053
    _globals['_TOOL_TLSCONFIG']._serialized_start = 4071
    _globals['_TOOL_TLSCONFIG']._serialized_end = 4220
    _globals['_TOOL_TLSCONFIG_CACERT']._serialized_start = 4166
    _globals['_TOOL_TLSCONFIG_CACERT']._serialized_end = 4220
    _globals['_TOOL_SERVICEDIRECTORYCONFIG']._serialized_start = 4222
    _globals['_TOOL_SERVICEDIRECTORYCONFIG']._serialized_end = 4312
    _globals['_TOOL_TOOLTYPE']._serialized_start = 4314
    _globals['_TOOL_TOOLTYPE']._serialized_end = 4390
    _globals['_EXPORTTOOLSMETADATA']._serialized_start = 4515
    _globals['_EXPORTTOOLSMETADATA']._serialized_end = 4536
    _globals['_TOOLS']._serialized_start = 4539
    _globals['_TOOLS']._serialized_end = 5836