"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/app_yaml.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/appengine/v1beta/app_yaml.proto\x12\x17google.appengine.v1beta\x1a\x1egoogle/protobuf/duration.proto"\xec\x01\n\x10ApiConfigHandler\x12A\n\x10auth_fail_action\x18\x01 \x01(\x0e2\'.google.appengine.v1beta.AuthFailAction\x128\n\x05login\x18\x02 \x01(\x0e2).google.appengine.v1beta.LoginRequirement\x12\x0e\n\x06script\x18\x03 \x01(\t\x12>\n\x0esecurity_level\x18\x04 \x01(\x0e2&.google.appengine.v1beta.SecurityLevel\x12\x0b\n\x03url\x18\x05 \x01(\t"\x93\x02\n\x0cErrorHandler\x12C\n\nerror_code\x18\x01 \x01(\x0e2/.google.appengine.v1beta.ErrorHandler.ErrorCode\x12\x13\n\x0bstatic_file\x18\x02 \x01(\t\x12\x11\n\tmime_type\x18\x03 \x01(\t"\x95\x01\n\tErrorCode\x12\x1a\n\x16ERROR_CODE_UNSPECIFIED\x10\x00\x12\x16\n\x12ERROR_CODE_DEFAULT\x10\x00\x12\x19\n\x15ERROR_CODE_OVER_QUOTA\x10\x01\x12\x1d\n\x19ERROR_CODE_DOS_API_DENIAL\x10\x02\x12\x16\n\x12ERROR_CODE_TIMEOUT\x10\x03\x1a\x02\x10\x01"\xe9\x05\n\x06UrlMap\x12\x11\n\turl_regex\x18\x01 \x01(\t\x12C\n\x0cstatic_files\x18\x02 \x01(\x0b2+.google.appengine.v1beta.StaticFilesHandlerH\x00\x128\n\x06script\x18\x03 \x01(\x0b2&.google.appengine.v1beta.ScriptHandlerH\x00\x12C\n\x0capi_endpoint\x18\x04 \x01(\x0b2+.google.appengine.v1beta.ApiEndpointHandlerH\x00\x12>\n\x0esecurity_level\x18\x05 \x01(\x0e2&.google.appengine.v1beta.SecurityLevel\x128\n\x05login\x18\x06 \x01(\x0e2).google.appengine.v1beta.LoginRequirement\x12A\n\x10auth_fail_action\x18\x07 \x01(\x0e2\'.google.appengine.v1beta.AuthFailAction\x12]\n\x1bredirect_http_response_code\x18\x08 \x01(\x0e28.google.appengine.v1beta.UrlMap.RedirectHttpResponseCode"\xdb\x01\n\x18RedirectHttpResponseCode\x12+\n\'REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED\x10\x00\x12#\n\x1fREDIRECT_HTTP_RESPONSE_CODE_301\x10\x01\x12#\n\x1fREDIRECT_HTTP_RESPONSE_CODE_302\x10\x02\x12#\n\x1fREDIRECT_HTTP_RESPONSE_CODE_303\x10\x03\x12#\n\x1fREDIRECT_HTTP_RESPONSE_CODE_307\x10\x04B\x0e\n\x0chandler_type"\xc4\x02\n\x12StaticFilesHandler\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x19\n\x11upload_path_regex\x18\x02 \x01(\t\x12R\n\x0chttp_headers\x18\x03 \x03(\x0b2<.google.appengine.v1beta.StaticFilesHandler.HttpHeadersEntry\x12\x11\n\tmime_type\x18\x04 \x01(\t\x12-\n\nexpiration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1d\n\x15require_matching_file\x18\x06 \x01(\x08\x12\x1c\n\x14application_readable\x18\x07 \x01(\x08\x1a2\n\x10HttpHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"$\n\rScriptHandler\x12\x13\n\x0bscript_path\x18\x01 \x01(\t")\n\x12ApiEndpointHandler\x12\x13\n\x0bscript_path\x18\x01 \x01(\t"\xeb\x01\n\x0bHealthCheck\x12\x1c\n\x14disable_health_check\x18\x01 \x01(\x08\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x19\n\x11healthy_threshold\x18\x03 \x01(\r\x12\x1b\n\x13unhealthy_threshold\x18\x04 \x01(\r\x12\x19\n\x11restart_threshold\x18\x05 \x01(\r\x121\n\x0echeck_interval\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12*\n\x07timeout\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration"\xf7\x01\n\x0eReadinessCheck\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x19\n\x11failure_threshold\x18\x03 \x01(\r\x12\x19\n\x11success_threshold\x18\x04 \x01(\r\x121\n\x0echeck_interval\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12*\n\x07timeout\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x124\n\x11app_start_timeout\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration"\xf2\x01\n\rLivenessCheck\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x19\n\x11failure_threshold\x18\x03 \x01(\r\x12\x19\n\x11success_threshold\x18\x04 \x01(\r\x121\n\x0echeck_interval\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12*\n\x07timeout\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x120\n\rinitial_delay\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration"(\n\x07Library\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t*t\n\x0eAuthFailAction\x12 \n\x1cAUTH_FAIL_ACTION_UNSPECIFIED\x10\x00\x12\x1d\n\x19AUTH_FAIL_ACTION_REDIRECT\x10\x01\x12!\n\x1dAUTH_FAIL_ACTION_UNAUTHORIZED\x10\x02*b\n\x10LoginRequirement\x12\x15\n\x11LOGIN_UNSPECIFIED\x10\x00\x12\x12\n\x0eLOGIN_OPTIONAL\x10\x01\x12\x0f\n\x0bLOGIN_ADMIN\x10\x02\x12\x12\n\x0eLOGIN_REQUIRED\x10\x03*y\n\rSecurityLevel\x12\x16\n\x12SECURE_UNSPECIFIED\x10\x00\x12\x12\n\x0eSECURE_DEFAULT\x10\x00\x12\x10\n\x0cSECURE_NEVER\x10\x01\x12\x13\n\x0fSECURE_OPTIONAL\x10\x02\x12\x11\n\rSECURE_ALWAYS\x10\x03\x1a\x02\x10\x01B\xd2\x01\n\x1bcom.google.appengine.v1betaB\x0cAppYamlProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.app_yaml_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x0cAppYamlProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_SECURITYLEVEL']._loaded_options = None
    _globals['_SECURITYLEVEL']._serialized_options = b'\x10\x01'
    _globals['_ERRORHANDLER_ERRORCODE']._loaded_options = None
    _globals['_ERRORHANDLER_ERRORCODE']._serialized_options = b'\x10\x01'
    _globals['_STATICFILESHANDLER_HTTPHEADERSENTRY']._loaded_options = None
    _globals['_STATICFILESHANDLER_HTTPHEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_AUTHFAILACTION']._serialized_start = 2547
    _globals['_AUTHFAILACTION']._serialized_end = 2663
    _globals['_LOGINREQUIREMENT']._serialized_start = 2665
    _globals['_LOGINREQUIREMENT']._serialized_end = 2763
    _globals['_SECURITYLEVEL']._serialized_start = 2765
    _globals['_SECURITYLEVEL']._serialized_end = 2886
    _globals['_APICONFIGHANDLER']._serialized_start = 100
    _globals['_APICONFIGHANDLER']._serialized_end = 336
    _globals['_ERRORHANDLER']._serialized_start = 339
    _globals['_ERRORHANDLER']._serialized_end = 614
    _globals['_ERRORHANDLER_ERRORCODE']._serialized_start = 465
    _globals['_ERRORHANDLER_ERRORCODE']._serialized_end = 614
    _globals['_URLMAP']._serialized_start = 617
    _globals['_URLMAP']._serialized_end = 1362
    _globals['_URLMAP_REDIRECTHTTPRESPONSECODE']._serialized_start = 1127
    _globals['_URLMAP_REDIRECTHTTPRESPONSECODE']._serialized_end = 1346
    _globals['_STATICFILESHANDLER']._serialized_start = 1365
    _globals['_STATICFILESHANDLER']._serialized_end = 1689
    _globals['_STATICFILESHANDLER_HTTPHEADERSENTRY']._serialized_start = 1639
    _globals['_STATICFILESHANDLER_HTTPHEADERSENTRY']._serialized_end = 1689
    _globals['_SCRIPTHANDLER']._serialized_start = 1691
    _globals['_SCRIPTHANDLER']._serialized_end = 1727
    _globals['_APIENDPOINTHANDLER']._serialized_start = 1729
    _globals['_APIENDPOINTHANDLER']._serialized_end = 1770
    _globals['_HEALTHCHECK']._serialized_start = 1773
    _globals['_HEALTHCHECK']._serialized_end = 2008
    _globals['_READINESSCHECK']._serialized_start = 2011
    _globals['_READINESSCHECK']._serialized_end = 2258
    _globals['_LIVENESSCHECK']._serialized_start = 2261
    _globals['_LIVENESSCHECK']._serialized_end = 2503
    _globals['_LIBRARY']._serialized_start = 2505
    _globals['_LIBRARY']._serialized_end = 2545