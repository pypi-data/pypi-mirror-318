"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1beta2/file.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/devtools/artifactregistry/v1beta2/file.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x98\x01\n\x04Hash\x12E\n\x04type\x18\x01 \x01(\x0e27.google.devtools.artifactregistry.v1beta2.Hash.HashType\x12\r\n\x05value\x18\x02 \x01(\x0c":\n\x08HashType\x12\x19\n\x15HASH_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\x07\n\x03MD5\x10\x02"\xd4\x02\n\x04File\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\x12>\n\x06hashes\x18\x04 \x03(\x0b2..google.devtools.artifactregistry.v1beta2.Hash\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05owner\x18\x07 \x01(\t:y\xeaAv\n$artifactregistry.googleapis.com/File\x12Nprojects/{project}/locations/{location}/repositories/{repository}/files/{file}"Y\n\x10ListFilesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"k\n\x11ListFilesResponse\x12=\n\x05files\x18\x01 \x03(\x0b2..google.devtools.artifactregistry.v1beta2.File\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x1e\n\x0eGetFileRequest\x12\x0c\n\x04name\x18\x01 \x01(\tB\x8d\x02\n,com.google.devtools.artifactregistry.v1beta2B\tFileProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1beta2.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\tFileProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2'
    _globals['_FILE']._loaded_options = None
    _globals['_FILE']._serialized_options = b'\xeaAv\n$artifactregistry.googleapis.com/File\x12Nprojects/{project}/locations/{location}/repositories/{repository}/files/{file}'
    _globals['_HASH']._serialized_start = 158
    _globals['_HASH']._serialized_end = 310
    _globals['_HASH_HASHTYPE']._serialized_start = 252
    _globals['_HASH_HASHTYPE']._serialized_end = 310
    _globals['_FILE']._serialized_start = 313
    _globals['_FILE']._serialized_end = 653
    _globals['_LISTFILESREQUEST']._serialized_start = 655
    _globals['_LISTFILESREQUEST']._serialized_end = 744
    _globals['_LISTFILESRESPONSE']._serialized_start = 746
    _globals['_LISTFILESRESPONSE']._serialized_end = 853
    _globals['_GETFILEREQUEST']._serialized_start = 855
    _globals['_GETFILEREQUEST']._serialized_end = 885