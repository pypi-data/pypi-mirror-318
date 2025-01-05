"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/file.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/devtools/artifactregistry/v1/file.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x93\x01\n\x04Hash\x12@\n\x04type\x18\x01 \x01(\x0e22.google.devtools.artifactregistry.v1.Hash.HashType\x12\r\n\x05value\x18\x02 \x01(\x0c":\n\x08HashType\x12\x19\n\x15HASH_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\x07\n\x03MD5\x10\x02"\x98\x04\n\x04File\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\x129\n\x06hashes\x18\x04 \x03(\x0b2).google.devtools.artifactregistry.v1.Hash\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\r\n\x05owner\x18\x07 \x01(\t\x123\n\nfetch_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12T\n\x0bannotations\x18\t \x03(\x0b2:.google.devtools.artifactregistry.v1.File.AnnotationsEntryB\x03\xe0A\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:y\xeaAv\n$artifactregistry.googleapis.com/File\x12Nprojects/{project}/locations/{location}/repositories/{repository}/files/{file}"\x99\x01\n\x10ListFilesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$artifactregistry.googleapis.com/File\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"f\n\x11ListFilesResponse\x128\n\x05files\x18\x01 \x03(\x0b2).google.devtools.artifactregistry.v1.File\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x0eGetFileRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/File"O\n\x11DeleteFileRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/File"\x87\x01\n\x11UpdateFileRequest\x12<\n\x04file\x18\x01 \x01(\x0b2).google.devtools.artifactregistry.v1.FileB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02B\xf4\x01\n\'com.google.devtools.artifactregistry.v1B\tFileProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\tFileProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_FILE_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_FILE_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_FILE'].fields_by_name['create_time']._loaded_options = None
    _globals['_FILE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['update_time']._loaded_options = None
    _globals['_FILE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['fetch_time']._loaded_options = None
    _globals['_FILE'].fields_by_name['fetch_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['annotations']._loaded_options = None
    _globals['_FILE'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_FILE']._loaded_options = None
    _globals['_FILE']._serialized_options = b'\xeaAv\n$artifactregistry.googleapis.com/File\x12Nprojects/{project}/locations/{location}/repositories/{repository}/files/{file}'
    _globals['_LISTFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$artifactregistry.googleapis.com/File'
    _globals['_GETFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/File'
    _globals['_DELETEFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/File'
    _globals['_UPDATEFILEREQUEST'].fields_by_name['file']._loaded_options = None
    _globals['_UPDATEFILEREQUEST'].fields_by_name['file']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFILEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFILEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_HASH']._serialized_start = 215
    _globals['_HASH']._serialized_end = 362
    _globals['_HASH_HASHTYPE']._serialized_start = 304
    _globals['_HASH_HASHTYPE']._serialized_end = 362
    _globals['_FILE']._serialized_start = 365
    _globals['_FILE']._serialized_end = 901
    _globals['_FILE_ANNOTATIONSENTRY']._serialized_start = 728
    _globals['_FILE_ANNOTATIONSENTRY']._serialized_end = 778
    _globals['_LISTFILESREQUEST']._serialized_start = 904
    _globals['_LISTFILESREQUEST']._serialized_end = 1057
    _globals['_LISTFILESRESPONSE']._serialized_start = 1059
    _globals['_LISTFILESRESPONSE']._serialized_end = 1161
    _globals['_GETFILEREQUEST']._serialized_start = 1163
    _globals['_GETFILEREQUEST']._serialized_end = 1239
    _globals['_DELETEFILEREQUEST']._serialized_start = 1241
    _globals['_DELETEFILEREQUEST']._serialized_end = 1320
    _globals['_UPDATEFILEREQUEST']._serialized_start = 1323
    _globals['_UPDATEFILEREQUEST']._serialized_end = 1458