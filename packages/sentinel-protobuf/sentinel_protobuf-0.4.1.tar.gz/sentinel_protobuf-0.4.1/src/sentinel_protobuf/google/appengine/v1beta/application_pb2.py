"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/application.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/appengine/v1beta/application.proto\x12\x17google.appengine.v1beta\x1a\x1egoogle/protobuf/duration.proto"\x84\x08\n\x0bApplication\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12@\n\x0edispatch_rules\x18\x03 \x03(\x0b2(.google.appengine.v1beta.UrlDispatchRule\x12\x13\n\x0bauth_domain\x18\x06 \x01(\t\x12\x13\n\x0blocation_id\x18\x07 \x01(\t\x12\x13\n\x0bcode_bucket\x18\x08 \x01(\t\x12<\n\x19default_cookie_expiration\x18\t \x01(\x0b2\x19.google.protobuf.Duration\x12J\n\x0eserving_status\x18\n \x01(\x0e22.google.appengine.v1beta.Application.ServingStatus\x12\x18\n\x10default_hostname\x18\x0b \x01(\t\x12\x16\n\x0edefault_bucket\x18\x0c \x01(\t\x12D\n\x03iap\x18\x0e \x01(\x0b27.google.appengine.v1beta.Application.IdentityAwareProxy\x12\x12\n\ngcr_domain\x18\x10 \x01(\t\x12H\n\rdatabase_type\x18\x11 \x01(\x0e21.google.appengine.v1beta.Application.DatabaseType\x12N\n\x10feature_settings\x18\x12 \x01(\x0b24.google.appengine.v1beta.Application.FeatureSettings\x1a\x82\x01\n\x12IdentityAwareProxy\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12\x18\n\x10oauth2_client_id\x18\x02 \x01(\t\x12\x1c\n\x14oauth2_client_secret\x18\x03 \x01(\t\x12#\n\x1boauth2_client_secret_sha256\x18\x04 \x01(\t\x1aR\n\x0fFeatureSettings\x12\x1b\n\x13split_health_checks\x18\x01 \x01(\x08\x12"\n\x1ause_container_optimized_os\x18\x02 \x01(\x08"U\n\rServingStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x11\n\rUSER_DISABLED\x10\x02\x12\x13\n\x0fSYSTEM_DISABLED\x10\x03"z\n\x0cDatabaseType\x12\x1d\n\x19DATABASE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCLOUD_DATASTORE\x10\x01\x12\x13\n\x0fCLOUD_FIRESTORE\x10\x02\x12!\n\x1dCLOUD_DATASTORE_COMPATIBILITY\x10\x03"@\n\x0fUrlDispatchRule\x12\x0e\n\x06domain\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\tB\xd6\x01\n\x1bcom.google.appengine.v1betaB\x10ApplicationProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.application_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x10ApplicationProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_APPLICATION']._serialized_start = 103
    _globals['_APPLICATION']._serialized_end = 1131
    _globals['_APPLICATION_IDENTITYAWAREPROXY']._serialized_start = 706
    _globals['_APPLICATION_IDENTITYAWAREPROXY']._serialized_end = 836
    _globals['_APPLICATION_FEATURESETTINGS']._serialized_start = 838
    _globals['_APPLICATION_FEATURESETTINGS']._serialized_end = 920
    _globals['_APPLICATION_SERVINGSTATUS']._serialized_start = 922
    _globals['_APPLICATION_SERVINGSTATUS']._serialized_end = 1007
    _globals['_APPLICATION_DATABASETYPE']._serialized_start = 1009
    _globals['_APPLICATION_DATABASETYPE']._serialized_end = 1131
    _globals['_URLDISPATCHRULE']._serialized_start = 1133
    _globals['_URLDISPATCHRULE']._serialized_end = 1197