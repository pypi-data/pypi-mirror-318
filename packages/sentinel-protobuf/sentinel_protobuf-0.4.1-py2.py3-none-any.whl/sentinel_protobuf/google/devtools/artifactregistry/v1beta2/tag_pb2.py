"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1beta2/tag.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/devtools/artifactregistry/v1beta2/tag.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xb1\x01\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t:\x8a\x01\xeaA\x86\x01\n#artifactregistry.googleapis.com/Tag\x12_projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}"X\n\x0fListTagsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"h\n\x10ListTagsResponse\x12;\n\x04tags\x18\x01 \x03(\x0b2-.google.devtools.artifactregistry.v1beta2.Tag\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x1d\n\rGetTagRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"n\n\x10CreateTagRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06tag_id\x18\x02 \x01(\t\x12:\n\x03tag\x18\x03 \x01(\x0b2-.google.devtools.artifactregistry.v1beta2.Tag"\x7f\n\x10UpdateTagRequest\x12:\n\x03tag\x18\x01 \x01(\x0b2-.google.devtools.artifactregistry.v1beta2.Tag\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask" \n\x10DeleteTagRequest\x12\x0c\n\x04name\x18\x01 \x01(\tB\x8c\x02\n,com.google.devtools.artifactregistry.v1beta2B\x08TagProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1beta2.tag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\x08TagProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2'
    _globals['_TAG']._loaded_options = None
    _globals['_TAG']._serialized_options = b'\xeaA\x86\x01\n#artifactregistry.googleapis.com/Tag\x12_projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}'
    _globals['_TAG']._serialized_start = 158
    _globals['_TAG']._serialized_end = 335
    _globals['_LISTTAGSREQUEST']._serialized_start = 337
    _globals['_LISTTAGSREQUEST']._serialized_end = 425
    _globals['_LISTTAGSRESPONSE']._serialized_start = 427
    _globals['_LISTTAGSRESPONSE']._serialized_end = 531
    _globals['_GETTAGREQUEST']._serialized_start = 533
    _globals['_GETTAGREQUEST']._serialized_end = 562
    _globals['_CREATETAGREQUEST']._serialized_start = 564
    _globals['_CREATETAGREQUEST']._serialized_end = 674
    _globals['_UPDATETAGREQUEST']._serialized_start = 676
    _globals['_UPDATETAGREQUEST']._serialized_end = 803
    _globals['_DELETETAGREQUEST']._serialized_start = 805
    _globals['_DELETETAGREQUEST']._serialized_end = 837