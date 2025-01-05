"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.artifactregistry.v1 import tag_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/devtools/artifactregistry/v1/version.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/devtools/artifactregistry/v1/tag.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa4\x04\n\x07Version\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12>\n\x0crelated_tags\x18\x07 \x03(\x0b2(.google.devtools.artifactregistry.v1.Tag\x12.\n\x08metadata\x18\x08 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x12W\n\x0bannotations\x18\t \x03(\x0b2=.google.devtools.artifactregistry.v1.Version.AnnotationsEntryB\x03\xe0A\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x96\x01\xeaA\x92\x01\n\'artifactregistry.googleapis.com/Version\x12gprojects/{project}/locations/{location}/repositories/{repository}/packages/{package}/versions/{version}"\xb8\x01\n\x13ListVersionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12>\n\x04view\x18\x04 \x01(\x0e20.google.devtools.artifactregistry.v1.VersionView\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x06 \x01(\tB\x03\xe0A\x01"o\n\x14ListVersionsResponse\x12>\n\x08versions\x18\x01 \x03(\x0b2,.google.devtools.artifactregistry.v1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"a\n\x11GetVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x04view\x18\x02 \x01(\x0e20.google.devtools.artifactregistry.v1.VersionView"3\n\x14DeleteVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05force\x18\x02 \x01(\x08"\xb1\x01\n\x1aBatchDeleteVersionsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xfaA)\x12\'artifactregistry.googleapis.com/Version\x12>\n\x05names\x18\x02 \x03(\tB/\xe0A\x02\xfaA)\n\'artifactregistry.googleapis.com/Version\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"6\n\x1bBatchDeleteVersionsMetadata\x12\x17\n\x0ffailed_versions\x18\x02 \x03(\t"\x8b\x01\n\x14UpdateVersionRequest\x12B\n\x07version\x18\x01 \x01(\x0b2,.google.devtools.artifactregistry.v1.VersionB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask*@\n\x0bVersionView\x12\x1c\n\x18VERSION_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02B\xf7\x01\n\'com.google.devtools.artifactregistry.v1B\x0cVersionProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x0cVersionProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_VERSION_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_VERSION_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_VERSION'].fields_by_name['metadata']._loaded_options = None
    _globals['_VERSION'].fields_by_name['metadata']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['annotations']._loaded_options = None
    _globals['_VERSION'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_VERSION']._loaded_options = None
    _globals['_VERSION']._serialized_options = b"\xeaA\x92\x01\n'artifactregistry.googleapis.com/Version\x12gprojects/{project}/locations/{location}/repositories/{repository}/packages/{package}/versions/{version}"
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHDELETEVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b"\xfaA)\x12'artifactregistry.googleapis.com/Version"
    _globals['_BATCHDELETEVERSIONSREQUEST'].fields_by_name['names']._loaded_options = None
    _globals['_BATCHDELETEVERSIONSREQUEST'].fields_by_name['names']._serialized_options = b"\xe0A\x02\xfaA)\n'artifactregistry.googleapis.com/Version"
    _globals['_UPDATEVERSIONREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_UPDATEVERSIONREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_VERSIONVIEW']._serialized_start = 1675
    _globals['_VERSIONVIEW']._serialized_end = 1739
    _globals['_VERSION']._serialized_start = 295
    _globals['_VERSION']._serialized_end = 843
    _globals['_VERSION_ANNOTATIONSENTRY']._serialized_start = 640
    _globals['_VERSION_ANNOTATIONSENTRY']._serialized_end = 690
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 846
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 1030
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 1032
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 1143
    _globals['_GETVERSIONREQUEST']._serialized_start = 1145
    _globals['_GETVERSIONREQUEST']._serialized_end = 1242
    _globals['_DELETEVERSIONREQUEST']._serialized_start = 1244
    _globals['_DELETEVERSIONREQUEST']._serialized_end = 1295
    _globals['_BATCHDELETEVERSIONSREQUEST']._serialized_start = 1298
    _globals['_BATCHDELETEVERSIONSREQUEST']._serialized_end = 1475
    _globals['_BATCHDELETEVERSIONSMETADATA']._serialized_start = 1477
    _globals['_BATCHDELETEVERSIONSMETADATA']._serialized_end = 1531
    _globals['_UPDATEVERSIONREQUEST']._serialized_start = 1534
    _globals['_UPDATEVERSIONREQUEST']._serialized_end = 1673