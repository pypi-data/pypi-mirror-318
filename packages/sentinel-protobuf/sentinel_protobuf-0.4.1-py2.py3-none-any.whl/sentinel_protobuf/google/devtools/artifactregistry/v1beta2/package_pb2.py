"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1beta2/package.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/artifactregistry/v1beta2/package.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x1fgoogle/protobuf/timestamp.proto"\x8f\x01\n\x07Package\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"L\n\x13ListPackagesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"t\n\x14ListPackagesResponse\x12C\n\x08packages\x18\x01 \x03(\x0b21.google.devtools.artifactregistry.v1beta2.Package\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"!\n\x11GetPackageRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"$\n\x14DeletePackageRequest\x12\x0c\n\x04name\x18\x01 \x01(\tB\x90\x02\n,com.google.devtools.artifactregistry.v1beta2B\x0cPackageProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1beta2.package_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\x0cPackageProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2'
    _globals['_PACKAGE']._serialized_start = 134
    _globals['_PACKAGE']._serialized_end = 277
    _globals['_LISTPACKAGESREQUEST']._serialized_start = 279
    _globals['_LISTPACKAGESREQUEST']._serialized_end = 355
    _globals['_LISTPACKAGESRESPONSE']._serialized_start = 357
    _globals['_LISTPACKAGESRESPONSE']._serialized_end = 473
    _globals['_GETPACKAGEREQUEST']._serialized_start = 475
    _globals['_GETPACKAGEREQUEST']._serialized_end = 508
    _globals['_DELETEPACKAGEREQUEST']._serialized_start = 510
    _globals['_DELETEPACKAGEREQUEST']._serialized_end = 546