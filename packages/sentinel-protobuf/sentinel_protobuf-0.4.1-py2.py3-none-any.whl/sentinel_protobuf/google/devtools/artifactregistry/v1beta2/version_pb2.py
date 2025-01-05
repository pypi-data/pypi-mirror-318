"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1beta2/version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.artifactregistry.v1beta2 import tag_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/artifactregistry/v1beta2/version.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/devtools/artifactregistry/v1beta2/tag.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\x03\n\x07Version\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12C\n\x0crelated_tags\x18\x07 \x03(\x0b2-.google.devtools.artifactregistry.v1beta2.Tag\x12.\n\x08metadata\x18\x08 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03:\x96\x01\xeaA\x92\x01\n\'artifactregistry.googleapis.com/Version\x12gprojects/{project}/locations/{location}/repositories/{repository}/packages/{package}/versions/{version}"\xa8\x01\n\x13ListVersionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12C\n\x04view\x18\x04 \x01(\x0e25.google.devtools.artifactregistry.v1beta2.VersionView\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"t\n\x14ListVersionsResponse\x12C\n\x08versions\x18\x01 \x03(\x0b21.google.devtools.artifactregistry.v1beta2.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"f\n\x11GetVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12C\n\x04view\x18\x02 \x01(\x0e25.google.devtools.artifactregistry.v1beta2.VersionView"3\n\x14DeleteVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05force\x18\x02 \x01(\x08*@\n\x0bVersionView\x12\x1c\n\x18VERSION_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02B\x90\x02\n,com.google.devtools.artifactregistry.v1beta2B\x0cVersionProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1beta2.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\x0cVersionProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2'
    _globals['_VERSION'].fields_by_name['metadata']._loaded_options = None
    _globals['_VERSION'].fields_by_name['metadata']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION']._loaded_options = None
    _globals['_VERSION']._serialized_options = b"\xeaA\x92\x01\n'artifactregistry.googleapis.com/Version\x12gprojects/{project}/locations/{location}/repositories/{repository}/packages/{package}/versions/{version}"
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_VERSIONVIEW']._serialized_start = 1136
    _globals['_VERSIONVIEW']._serialized_end = 1200
    _globals['_VERSION']._serialized_start = 276
    _globals['_VERSION']._serialized_end = 688
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 691
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 859
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 861
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 977
    _globals['_GETVERSIONREQUEST']._serialized_start = 979
    _globals['_GETVERSIONREQUEST']._serialized_end = 1081
    _globals['_DELETEVERSIONREQUEST']._serialized_start = 1083
    _globals['_DELETEVERSIONREQUEST']._serialized_end = 1134