"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/vpcsc_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/artifactregistry/v1/vpcsc_config.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x98\x02\n\x0bVPCSCConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\x0cvpcsc_policy\x18\x02 \x01(\x0e2<.google.devtools.artifactregistry.v1.VPCSCConfig.VPCSCPolicy"@\n\x0bVPCSCPolicy\x12\x1c\n\x18VPCSC_POLICY_UNSPECIFIED\x10\x00\x12\x08\n\x04DENY\x10\x01\x12\t\n\x05ALLOW\x10\x02:e\xeaAb\n+artifactregistry.googleapis.com/VpcscConfig\x123projects/{project}/locations/{location}/vpcscConfig"Z\n\x15GetVPCSCConfigRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+artifactregistry.googleapis.com/VpcscConfig"\x93\x01\n\x18UpdateVPCSCConfigRequest\x12F\n\x0cvpcsc_config\x18\x01 \x01(\x0b20.google.devtools.artifactregistry.v1.VPCSCConfig\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\xfb\x01\n\'com.google.devtools.artifactregistry.v1B\x10VPCSCConfigProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.vpcsc_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x10VPCSCConfigProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_VPCSCCONFIG']._loaded_options = None
    _globals['_VPCSCCONFIG']._serialized_options = b'\xeaAb\n+artifactregistry.googleapis.com/VpcscConfig\x123projects/{project}/locations/{location}/vpcscConfig'
    _globals['_GETVPCSCCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVPCSCCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+artifactregistry.googleapis.com/VpcscConfig'
    _globals['_VPCSCCONFIG']._serialized_start = 190
    _globals['_VPCSCCONFIG']._serialized_end = 470
    _globals['_VPCSCCONFIG_VPCSCPOLICY']._serialized_start = 303
    _globals['_VPCSCCONFIG_VPCSCPOLICY']._serialized_end = 367
    _globals['_GETVPCSCCONFIGREQUEST']._serialized_start = 472
    _globals['_GETVPCSCCONFIGREQUEST']._serialized_end = 562
    _globals['_UPDATEVPCSCCONFIGREQUEST']._serialized_start = 565
    _globals['_UPDATEVPCSCCONFIGREQUEST']._serialized_end = 712