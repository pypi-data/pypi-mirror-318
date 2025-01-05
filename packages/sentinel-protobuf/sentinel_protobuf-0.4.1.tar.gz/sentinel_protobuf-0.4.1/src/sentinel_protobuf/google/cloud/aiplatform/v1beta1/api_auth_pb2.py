"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/api_auth.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/aiplatform/v1beta1/api_auth.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xcd\x01\n\x07ApiAuth\x12O\n\x0eapi_key_config\x18\x01 \x01(\x0b25.google.cloud.aiplatform.v1beta1.ApiAuth.ApiKeyConfigH\x00\x1ab\n\x0cApiKeyConfig\x12R\n\x16api_key_secret_version\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersionB\r\n\x0bauth_configB\xe3\x01\n#com.google.cloud.aiplatform.v1beta1B\x0cApiAuthProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.api_auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0cApiAuthProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_APIAUTH_APIKEYCONFIG'].fields_by_name['api_key_secret_version']._loaded_options = None
    _globals['_APIAUTH_APIKEYCONFIG'].fields_by_name['api_key_secret_version']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_APIAUTH']._serialized_start = 144
    _globals['_APIAUTH']._serialized_end = 349
    _globals['_APIAUTH_APIKEYCONFIG']._serialized_start = 236
    _globals['_APIAUTH_APIKEYCONFIG']._serialized_end = 334