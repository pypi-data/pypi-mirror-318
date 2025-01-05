"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/acl_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/discoveryengine/v1alpha/acl_config.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/discoveryengine/v1alpha/common.proto"\xc5\x01\n\tAclConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12C\n\nidp_config\x18\x02 \x01(\x0b2/.google.cloud.discoveryengine.v1alpha.IdpConfig:`\xeaA]\n(discoveryengine.googleapis.com/AclConfig\x121projects/{project}/locations/{location}/aclConfigB\x9a\x02\n(com.google.cloud.discoveryengine.v1alphaB\x0eAclConfigProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.acl_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x0eAclConfigProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_ACLCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_ACLCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ACLCONFIG']._loaded_options = None
    _globals['_ACLCONFIG']._serialized_options = b'\xeaA]\n(discoveryengine.googleapis.com/AclConfig\x121projects/{project}/locations/{location}/aclConfig'
    _globals['_ACLCONFIG']._serialized_start = 207
    _globals['_ACLCONFIG']._serialized_end = 404