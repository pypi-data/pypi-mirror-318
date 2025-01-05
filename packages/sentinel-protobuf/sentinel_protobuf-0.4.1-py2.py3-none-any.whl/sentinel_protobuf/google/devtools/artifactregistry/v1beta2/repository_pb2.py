"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1beta2/repository.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/devtools/artifactregistry/v1beta2/repository.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb9\x07\n\nRepository\x12b\n\x0cmaven_config\x18\t \x01(\x0b2J.google.devtools.artifactregistry.v1beta2.Repository.MavenRepositoryConfigH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x06format\x18\x02 \x01(\x0e2;.google.devtools.artifactregistry.v1beta2.Repository.Format\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12P\n\x06labels\x18\x04 \x03(\x0b2@.google.devtools.artifactregistry.v1beta2.Repository.LabelsEntry\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0ckms_key_name\x18\x08 \x01(\t\x1a\xf8\x01\n\x15MavenRepositoryConfig\x12!\n\x19allow_snapshot_overwrites\x18\x01 \x01(\x08\x12p\n\x0eversion_policy\x18\x02 \x01(\x0e2X.google.devtools.artifactregistry.v1beta2.Repository.MavenRepositoryConfig.VersionPolicy"J\n\rVersionPolicy\x12\x1e\n\x1aVERSION_POLICY_UNSPECIFIED\x10\x00\x12\x0b\n\x07RELEASE\x10\x01\x12\x0c\n\x08SNAPSHOT\x10\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"^\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\n\n\x06DOCKER\x10\x01\x12\t\n\x05MAVEN\x10\x02\x12\x07\n\x03NPM\x10\x03\x12\x07\n\x03APT\x10\x05\x12\x07\n\x03YUM\x10\x06\x12\n\n\x06PYTHON\x10\x08:r\xeaAo\n*artifactregistry.googleapis.com/Repository\x12Aprojects/{project}/locations/{location}/repositories/{repository}B\x0f\n\rformat_config"\x84\x01\n\x17ListRepositoriesRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Repository\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x7f\n\x18ListRepositoriesResponse\x12J\n\x0crepositories\x18\x01 \x03(\x0b24.google.devtools.artifactregistry.v1beta2.Repository\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"X\n\x14GetRepositoryRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/Repository"\xbe\x01\n\x17CreateRepositoryRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Repository\x12\x15\n\rrepository_id\x18\x02 \x01(\t\x12H\n\nrepository\x18\x03 \x01(\x0b24.google.devtools.artifactregistry.v1beta2.Repository"\x94\x01\n\x17UpdateRepositoryRequest\x12H\n\nrepository\x18\x01 \x01(\x0b24.google.devtools.artifactregistry.v1beta2.Repository\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"[\n\x17DeleteRepositoryRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/RepositoryB\x93\x02\n,com.google.devtools.artifactregistry.v1beta2B\x0fRepositoryProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1beta2.repository_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\x0fRepositoryProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2'
    _globals['_REPOSITORY_LABELSENTRY']._loaded_options = None
    _globals['_REPOSITORY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_REPOSITORY']._loaded_options = None
    _globals['_REPOSITORY']._serialized_options = b'\xeaAo\n*artifactregistry.googleapis.com/Repository\x12Aprojects/{project}/locations/{location}/repositories/{repository}'
    _globals['_LISTREPOSITORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREPOSITORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Repository'
    _globals['_GETREPOSITORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREPOSITORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/Repository'
    _globals['_CREATEREPOSITORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREPOSITORYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Repository'
    _globals['_DELETEREPOSITORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREPOSITORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/Repository'
    _globals['_REPOSITORY']._serialized_start = 231
    _globals['_REPOSITORY']._serialized_end = 1184
    _globals['_REPOSITORY_MAVENREPOSITORYCONFIG']._serialized_start = 660
    _globals['_REPOSITORY_MAVENREPOSITORYCONFIG']._serialized_end = 908
    _globals['_REPOSITORY_MAVENREPOSITORYCONFIG_VERSIONPOLICY']._serialized_start = 834
    _globals['_REPOSITORY_MAVENREPOSITORYCONFIG_VERSIONPOLICY']._serialized_end = 908
    _globals['_REPOSITORY_LABELSENTRY']._serialized_start = 910
    _globals['_REPOSITORY_LABELSENTRY']._serialized_end = 955
    _globals['_REPOSITORY_FORMAT']._serialized_start = 957
    _globals['_REPOSITORY_FORMAT']._serialized_end = 1051
    _globals['_LISTREPOSITORIESREQUEST']._serialized_start = 1187
    _globals['_LISTREPOSITORIESREQUEST']._serialized_end = 1319
    _globals['_LISTREPOSITORIESRESPONSE']._serialized_start = 1321
    _globals['_LISTREPOSITORIESRESPONSE']._serialized_end = 1448
    _globals['_GETREPOSITORYREQUEST']._serialized_start = 1450
    _globals['_GETREPOSITORYREQUEST']._serialized_end = 1538
    _globals['_CREATEREPOSITORYREQUEST']._serialized_start = 1541
    _globals['_CREATEREPOSITORYREQUEST']._serialized_end = 1731
    _globals['_UPDATEREPOSITORYREQUEST']._serialized_start = 1734
    _globals['_UPDATEREPOSITORYREQUEST']._serialized_end = 1882
    _globals['_DELETEREPOSITORYREQUEST']._serialized_start = 1884
    _globals['_DELETEREPOSITORYREQUEST']._serialized_end = 1975