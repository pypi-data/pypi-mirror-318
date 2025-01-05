"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/generic.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/devtools/artifactregistry/v1/generic.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbb\x02\n\x0fGenericArtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\x9c\x01\xeaA\x98\x01\n/artifactregistry.googleapis.com/GenericArtifact\x12eprojects/{project}/locations/{location}/repositories/{repository}/genericArtifacts/{generic_artifact}B\xf7\x01\n\'com.google.devtools.artifactregistry.v1B\x0cGenericProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.generic_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x0cGenericProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_GENERICARTIFACT'].fields_by_name['create_time']._loaded_options = None
    _globals['_GENERICARTIFACT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GENERICARTIFACT'].fields_by_name['update_time']._loaded_options = None
    _globals['_GENERICARTIFACT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GENERICARTIFACT']._loaded_options = None
    _globals['_GENERICARTIFACT']._serialized_options = b'\xeaA\x98\x01\n/artifactregistry.googleapis.com/GenericArtifact\x12eprojects/{project}/locations/{location}/repositories/{repository}/genericArtifacts/{generic_artifact}'
    _globals['_GENERICARTIFACT']._serialized_start = 184
    _globals['_GENERICARTIFACT']._serialized_end = 499