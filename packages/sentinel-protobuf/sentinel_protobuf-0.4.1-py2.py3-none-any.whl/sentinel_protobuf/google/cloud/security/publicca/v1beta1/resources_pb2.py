"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/security/publicca/v1beta1/resources.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/security/publicca/v1beta1/resources.proto\x12&google.cloud.security.publicca.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdd\x01\n\x12ExternalAccountKey\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06key_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bb64_mac_key\x18\x03 \x01(\x0cB\x03\xe0A\x03:\x84\x01\xeaA\x80\x01\n*publicca.googleapis.com/ExternalAccountKey\x12Rprojects/{project}/locations/{location}/externalAccountKeys/{external_account_key}B\x88\x02\n*com.google.cloud.security.publicca.v1beta1B\x0eResourcesProtoP\x01ZFcloud.google.com/go/security/publicca/apiv1beta1/publiccapb;publiccapb\xf8\x01\x01\xaa\x02&Google.Cloud.Security.PublicCA.V1Beta1\xca\x02&Google\\Cloud\\Security\\PublicCA\\V1beta1\xea\x02*Google::Cloud::Security::PublicCA::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.security.publicca.v1beta1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.security.publicca.v1beta1B\x0eResourcesProtoP\x01ZFcloud.google.com/go/security/publicca/apiv1beta1/publiccapb;publiccapb\xf8\x01\x01\xaa\x02&Google.Cloud.Security.PublicCA.V1Beta1\xca\x02&Google\\Cloud\\Security\\PublicCA\\V1beta1\xea\x02*Google::Cloud::Security::PublicCA::V1beta1'
    _globals['_EXTERNALACCOUNTKEY'].fields_by_name['name']._loaded_options = None
    _globals['_EXTERNALACCOUNTKEY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EXTERNALACCOUNTKEY'].fields_by_name['key_id']._loaded_options = None
    _globals['_EXTERNALACCOUNTKEY'].fields_by_name['key_id']._serialized_options = b'\xe0A\x03'
    _globals['_EXTERNALACCOUNTKEY'].fields_by_name['b64_mac_key']._loaded_options = None
    _globals['_EXTERNALACCOUNTKEY'].fields_by_name['b64_mac_key']._serialized_options = b'\xe0A\x03'
    _globals['_EXTERNALACCOUNTKEY']._loaded_options = None
    _globals['_EXTERNALACCOUNTKEY']._serialized_options = b'\xeaA\x80\x01\n*publicca.googleapis.com/ExternalAccountKey\x12Rprojects/{project}/locations/{location}/externalAccountKeys/{external_account_key}'
    _globals['_EXTERNALACCOUNTKEY']._serialized_start = 159
    _globals['_EXTERNALACCOUNTKEY']._serialized_end = 380