"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/acl_config_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import acl_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_acl__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/discoveryengine/v1alpha/acl_config_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/discoveryengine/v1alpha/acl_config.proto"U\n\x13GetAclConfigRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/AclConfig"b\n\x16UpdateAclConfigRequest\x12H\n\nacl_config\x18\x01 \x01(\x0b2/.google.cloud.discoveryengine.v1alpha.AclConfigB\x03\xe0A\x022\xf8\x03\n\x10AclConfigService\x12\xd1\x01\n\x0fUpdateAclConfig\x12<.google.cloud.discoveryengine.v1alpha.UpdateAclConfigRequest\x1a/.google.cloud.discoveryengine.v1alpha.AclConfig"O\x82\xd3\xe4\x93\x02I2;/v1alpha/{acl_config.name=projects/*/locations/*/aclConfig}:\nacl_config\x12\xbb\x01\n\x0cGetAclConfig\x129.google.cloud.discoveryengine.v1alpha.GetAclConfigRequest\x1a/.google.cloud.discoveryengine.v1alpha.AclConfig"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1alpha/{name=projects/*/locations/*/aclConfig}\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa1\x02\n(com.google.cloud.discoveryengine.v1alphaB\x15AclConfigServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.acl_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x15AclConfigServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_GETACLCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACLCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/AclConfig'
    _globals['_UPDATEACLCONFIGREQUEST'].fields_by_name['acl_config']._loaded_options = None
    _globals['_UPDATEACLCONFIGREQUEST'].fields_by_name['acl_config']._serialized_options = b'\xe0A\x02'
    _globals['_ACLCONFIGSERVICE']._loaded_options = None
    _globals['_ACLCONFIGSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ACLCONFIGSERVICE'].methods_by_name['UpdateAclConfig']._loaded_options = None
    _globals['_ACLCONFIGSERVICE'].methods_by_name['UpdateAclConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02I2;/v1alpha/{acl_config.name=projects/*/locations/*/aclConfig}:\nacl_config'
    _globals['_ACLCONFIGSERVICE'].methods_by_name['GetAclConfig']._loaded_options = None
    _globals['_ACLCONFIGSERVICE'].methods_by_name['GetAclConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1alpha/{name=projects/*/locations/*/aclConfig}'
    _globals['_GETACLCONFIGREQUEST']._serialized_start = 273
    _globals['_GETACLCONFIGREQUEST']._serialized_end = 358
    _globals['_UPDATEACLCONFIGREQUEST']._serialized_start = 360
    _globals['_UPDATEACLCONFIGREQUEST']._serialized_end = 458
    _globals['_ACLCONFIGSERVICE']._serialized_start = 461
    _globals['_ACLCONFIGSERVICE']._serialized_end = 965